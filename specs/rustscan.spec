%global debug_package %{nil}
%global _prj_name RustScan

Name:           rustscan
Version:        2.1.0
Release:        2%{?dist}
Summary:        The Modern Port Scanner

License:        GPLv3+
URL:            https://github.com/RustScan/RustScan
Source0:        %{url}/archive/%{version}.tar.gz

Requires:       nmap
BuildRequires:  gcc
# python & perl are required to test scripting
%if 0%{?el7}
BuildRequires:  python36
%endif
%if 0%{?el8}
BuildRequires:  python39
%endif
%if 0%{?el9}
BuildRequires:  python3
%endif
BuildRequires:  perl

%description
The Modern Port Scanner. Find ports quickly (3 seconds at its fastest).
Run scripts through our scripting engine (Python, Lua, Shell supported).

%prep
%autosetup -n %{_prj_name}-%{version}

# use latest stable version from rustup
curl -Lfo "rustup.sh" "https://sh.rustup.rs"
chmod +x "rustup.sh"
./rustup.sh --profile minimal -y

%build
source ~/.cargo/env
RUSTFLAGS="-C strip=symbols" cargo build --release

%check
source ~/.cargo/env
cargo test --release

%install
# bin
install -Dpm 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
* Sun Jul 17 2022 cyqsimon - 2.1.0-2
- Always prefer toolchain from rustup

* Thu Jul 14 2022 cyqsimon - 2.1.0-1
- Release 2.1.0
