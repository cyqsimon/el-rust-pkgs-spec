%global debug_package %{nil}
%global _prj_name RustScan

Name:           rustscan
Version:        2.4.1
Release:        1%{?dist}
Summary:        The Modern Port Scanner

License:        GPLv3+
URL:            https://github.com/RustScan/RustScan
Source0:        %{url}/archive/%{version}.tar.gz

Requires:       nmap
# python & perl are required to test scripting
BuildRequires:  gcc perl
%if 0%{?el8}
BuildRequires:  python39
%else
BuildRequires:  python3
%endif

%description
The Modern Port Scanner. Find ports quickly (3 seconds at its fastest).
Run scripts through our scripting engine (Python, Lua, Shell supported).

%prep
%autosetup -n %{_prj_name}-%{version}

# use latest stable version from rustup
curl -Lf "https://sh.rustup.rs" | sh -s -- --profile minimal -y

%build
source ~/.cargo/env
cargo +stable build --release

%check
source ~/.cargo/env
cargo +stable test

%install
# bin
install -Dpm 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
* Sun Mar 09 2025 cyqsimon - 2.4.1-1
- Release 2.4.1

* Tue Aug 13 2024 cyqsimon - 2.3.0-2
- Remove provisions for EL7

* Tue Jul 09 2024 cyqsimon - 2.3.0-1
- Release 2.3.0

* Thu May 02 2024 cyqsimon - 2.2.3-1
- Release 2.2.3

* Sun Apr 21 2024 cyqsimon - 2.2.2-1
- Release 2.2.2

* Tue Apr 16 2024 cyqsimon - 2.1.1-3
- Remove explicit stripping (strip enabled by default since 1.77.0)

* Sat Mar 18 2023 cyqsimon - 2.1.1-2
- Run tests in debug mode

* Mon Nov 07 2022 cyqsimon - 2.1.1-1
- Release 2.1.1

* Sun Jul 17 2022 cyqsimon - 2.1.0-2
- Always prefer toolchain from rustup

* Thu Jul 14 2022 cyqsimon - 2.1.0-1
- Release 2.1.0
