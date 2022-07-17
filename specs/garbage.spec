%global debug_package %{nil}

Name:    garbage
Version: 0.3.3
Release: 1%{?dist}
Summary: Soft-deletion CLI tool with FreeDesktop Trash compatibility

License: GPLv3
URL: https://git.sr.ht/~mzhang/garbage
Source0: %{url}/archive/v%{version}.tar.gz

BuildRequires: cargo git rust

%description
Soft-deletion CLI tool with FreeDesktop Trash compatibility.

Rust version of 'trash-cli'.

%prep
%autosetup -n %{name}-v%{version}

%build
RUSTFLAGS="-C strip=symbols" cargo build --release

%check
cargo test

%install
# bin
install -Dpm 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
* Sun Jul 17 2022 cyqsimon - 0.3.3-1
- Release 0.3.3
