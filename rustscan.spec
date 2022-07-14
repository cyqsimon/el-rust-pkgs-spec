%global debug_package %{nil}

Name:    rustscan
Version: 2.1.0
Release: 1%{?dist}
Summary: The Modern Port Scanner

License: GPLv3+
URL: https://github.com/RustScan/RustScan
Source0: %{url}/archive/%{version}/%{name}-%{version}.tar.gz

Requires: nmap
BuildRequires: cargo rust

%description
The Modern Port Scanner. Find ports quickly (3 seconds at its fastest).
Run scripts through our scripting engine (Python, Lua, Shell supported).

%prep
%autosetup -n RustScan-%{version}

%build
RUSTFLAGS="-C strip=symbols" cargo build --release

%check
cargo test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_docdir}/%{name}

# Bin
install -pm 0755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

# doc
install -Dm644 README.md %{buildroot}%{_docdir}/%{name}/README.md
install -Dm644 LICENSE %{buildroot}%{_docdir}/%{name}/LICENSE

%files
%{_bindir}/%{name}
%{_docdir}/%{name}/*

%changelog
* Thu Jul 14 2022 cyqsimon - 2.1.0-1
- Release 2.1.0
