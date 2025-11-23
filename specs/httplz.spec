%global debug_package %{nil}
%global _prj_name http

Name:           httplz
Version:        2.5.0
Release:        1%{?dist}
Summary:        A basic HTTP server for hosting a folder fast and simply

License:        MIT
URL:            https://github.com/thecoshman/http
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  pkgconfig(bzip2) gcc pkgconfig(openssl) pandoc

%description
A simple-binary server that can be used via CLI to quickly take
the current directory and serve it. Everything has sensible defaults
such that you do not have to pass parameters like what port to use.

%prep
%autosetup -n %{_prj_name}-%{version}

# use latest stable version from rustup
curl -Lf "https://sh.rustup.rs" | sh -s -- --profile minimal -y

%build
source ~/.cargo/env

# only build and install the `httplz` binary
cargo +stable build --release --bin %{name}

# rename man page markdown
mv %{_prj_name}.md %{name}.md
# patch man page markdown
## rename all instances of `http` to `httplz`
sed -Ei 's/%{_prj_name}\(1\)/%{name}(1)/g' %{name}.md
sed -Ei 's/`%{_prj_name}`/`%{name}`/g' %{name}.md
sed -Ei 's/`%{_prj_name} /`%{name} /g' %{name}.md
## remove opening header
sed -Ei '/={3,}$/d' %{name}.md
## add header in a format acceptable to pandoc
sed -Ei '1i % %{name}(1) v%{version}\n\n## NAME\n' %{name}.md

# generate man page to ./httplz.1
pandoc --standalone --from markdown --to man %{name}.md > %{name}.1

%check
source ~/.cargo/env
cargo +stable test

%install
# bin
install -Dpm 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

# manpage
install -Dpm 644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Sun Nov 23 2025 cyqsimon - 2.5.0-1
- Release 2.5.0

* Fri Oct 10 2025 cyqsimon - 2.4.0-1
- Release 2.4.0

* Wed Sep 24 2025 cyqsimon - 2.3.1-2
- Mass rebuild

* Mon Aug 04 2025 cyqsimon - 2.3.1-1
- Release 2.3.1

* Tue Jun 17 2025 cyqsimon - 2.3.0-1
- Release 2.3.0

* Wed May 21 2025 cyqsimon - 2.2.1-1
- Release 2.2.1

* Fri May 09 2025 cyqsimon - 2.2.0-1
- Release 2.2.0

* Tue Sep 24 2024 cyqsimon - 2.1.0-1
- Release 2.1.0

* Tue Aug 13 2024 cyqsimon - 2.0.2-3
- Remove provisions for EL7

* Tue Jun 04 2024 cyqsimon - 2.0.2-2
- Use gcc-11 instead of the default gcc-4 on EL7

* Mon Jun 03 2024 cyqsimon - 2.0.2-1
- Release 2.0.2

* Tue Apr 16 2024 cyqsimon - 1.13.2-2
- Remove explicit stripping (strip enabled by default since 1.77.0)

* Thu Aug 31 2023 cyqsimon - 1.13.2-2
- Release 1.13.2

* Fri Aug 25 2023 cyqsimon - 1.13.1-1
- Release 1.13.1

* Thu Jul 20 2023 cyqsimon - 1.13.0-3
- Undeclare `openssl` as a runtime dependency

* Thu Jul 20 2023 cyqsimon - 1.13.0-2
- Use `pandoc` from EPEL for manpage generation on EL9

* Sat Jul 15 2023 cyqsimon - 1.13.0-1
- Relaese 1.13.0

* Wed Mar 22 2023 cyqsimon - 1.12.6-1
- Release 1.12.6
- Run tests in debug mode

* Tue Aug 16 2022 cyqsimon - 1.12.5-3
- Undeclare explicit Requires: bzip2-libs

* Sun Jul 17 2022 cyqsimon - 1.12.5-2
- Always prefer toolchain from rustup

* Fri Jul 15 2022 cyqsimon - 1.12.5-1
- Release 1.12.5
