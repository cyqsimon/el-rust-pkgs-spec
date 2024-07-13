%global debug_package %{nil}

Name:           fend
Version:        1.5.0
Release:        1%{?dist}
Summary:        Arbitrary-precision unit-aware calculator

License:        GPLv3+
URL:            https://github.com/printfn/fend
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  gcc pkgconfig(openssl)
# pandoc shipped by EL7/8 cannot build man page successfully
%if 0%{?rhel} >= 9
BuildRequires:  pandoc
%endif

%description
fend is an arbitrary-precision unit-aware calculator

Unique features:

- Arbitrary-precision arithmetic using rational numbers
- Full support for complex numbers
- D&D-style dice rolls
- Variables
- Binary, octal, hexadecimal and all other bases between 2 and 36
- Keep track of units, with support for SI, US and UK customary and many
  historical units
- Emacs-style CLI shortcuts
- Trigonometric functions
- Lambda calculus

%prep
%autosetup

# use latest stable version from rustup
curl -Lf "https://sh.rustup.rs" | sh -s -- --profile minimal -y

%build
source ~/.cargo/env
cargo +stable build --release --package %{name}

%if 0%{?rhel} >= 9
./documentation/build.sh
%endif

%check
source ~/.cargo/env
cargo +stable test --package %{name} --package %{name}-core

%install
# bin
install -Dpm 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

%if 0%{?rhel} >= 9
# manpage
install -Dpm 644 documentation/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
%endif

%files
%license LICENSE.md
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%if 0%{?rhel} >= 9
%{_mandir}/man1/%{name}.1*
%endif

%changelog
* Sat Jul 13 2024 cyqsimon - 1.5.0-1
- Release 1.5.0

* Thu Jun 20 2024 cyqsimon - 1.4.9-1
- Release 1.4.9

* Mon May 06 2024 Add - 1.4.8-2
- Add OpenSSL build dep

* Mon May 06 2024 cyqsimon - 1.4.8-1
- Release 1.4.8

* Tue Apr 16 2024 cyqsimon - 1.4.1-2
- Remove explicit stripping (strip enabled by default since 1.77.0)

* Sun Jan 07 2024 cyqsimon - 1.4.1-1
- Release 1.4.1

* Wed Dec 27 2023 cyqsimon - v1.4.0-1
- Release v1.4.0
