%global debug_package %{nil}

Name:           miniserve
Version:        0.31.0
Release:        1%{?dist}
Summary:        CLI tool to serve files and dirs over HTTP

License:        MIT
URL:            https://github.com/svenstaro/miniserve
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  pkgconfig(bzip2) gcc pkgconfig(openssl) systemd-rpm-macros

%description
For when you really just want to serve some files over HTTP right now!

miniserve is a small, self-contained cross-platform CLI tool that allows you
to just grab the binary and serve some file(s) via HTTP. Sometimes this is
just a more practical and quick way than doing things properly.

%prep
%autosetup

# use latest stable version from rustup
curl -Lf "https://sh.rustup.rs" | sh -s -- --profile minimal -y

%build
source ~/.cargo/env
cargo +stable build --release

# generate manpage
target/release/%{name} --print-manpage > %{name}.1

# generate completions
target/release/%{name} --print-completions bash > %{name}.bash
target/release/%{name} --print-completions fish > %{name}.fish
target/release/%{name} --print-completions zsh > %{name}.zsh

%check
source ~/.cargo/env
cargo +stable test

%install
# bin
install -Dpm 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

# unit
install -Dpm 644 packaging/%{name}@.service %{buildroot}%{_unitdir}/%{name}@.service

# manpage
install -Dpm 644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

# completions
install -Dpm 644 %{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dpm 644 %{name}.fish %{buildroot}%{_datadir}/fish/completions/%{name}.fish
install -Dpm 644 %{name}.zsh %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%{_unitdir}/%{name}@.service
%{_mandir}/man1/%{name}.1*
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/completions/%{name}.fish
%{_datadir}/zsh/site-functions/_%{name}

%changelog
* Sun Jun 29 2025 cyqsimon - 0.31.0-1
- Release 0.31.0

* Fri Feb 07 2025 cyqsimon - 0.29.0-1
- Release 0.29.0

* Thu Sep 12 2024 cyqsimon - 0.28.0-1
- Release 0.28.0

* Tue Aug 13 2024 cyqsimon - 0.27.1-3
- Remove provisions for EL7

* Tue Apr 16 2024 cyqsimon - 0.27.1-2
- Remove explicit stripping (strip enabled by default since 1.77.0)

* Sat Mar 16 2024 cyqsimon - 0.27.1-1
- Release 0.27.1

* Sat Jan 13 2024 cyqsimon - 0.26.0-1
- Release 0.26.0

* Sun Jan 07 2024 cyqsimon - 0.25.0-1
- Release 0.25.0

* Thu Jul 06 2023 cyqsimon - 0.24.0-1
- Release 0.24.0

* Sat Apr 29 2023 cyqsimon - 0.23.2-1
- Release 0.23.2

* Thu Apr 20 2023 cyqsimon - 0.23.1-1
- Release 0.23.1

* Sat Mar 18 2023 cyqsimon - 0.23.0-2
- Run tests in debug mode

* Wed Mar 01 2023 cyqsimon - 0.23.0-1
- Release 0.23.0

* Wed Sep 21 2022 cyqsimon - 0.22.0-2
- Disable broken qrcode tests for EL7

* Wed Sep 21 2022 cyqsimon - 0.22.0-1
- Release 0.22.0

* Mon Sep 19 2022 cyqsimon - 0.21.0-1
- Release 0.21.0

* Tue Aug 16 2022 cyqsimon - 0.20.0-3
- Undeclare explicit Requires: bzip2-libs

* Tue Jul 19 2022 cyqsimon - 0.20.0-2
- Install unit file

* Mon Jul 18 2022 cyqsimon - 0.20.0-1
- Release 0.20.0
