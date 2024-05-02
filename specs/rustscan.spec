%global debug_package %{nil}
%global _prj_name RustScan

Name:           rustscan
Version:        2.2.3
Release:        1%{?dist}
Summary:        The Modern Port Scanner

License:        GPLv3+
URL:            https://github.com/RustScan/RustScan
Source0:        %{url}/archive/%{version}.tar.gz

Requires:       nmap
BuildRequires:  gcc
# python & perl are required to test scripting
%if 0%{?el7} || 0%{?el9}
BuildRequires:  python3
%endif
%if 0%{?el8}
BuildRequires:  python39
%endif
BuildRequires:  perl

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
