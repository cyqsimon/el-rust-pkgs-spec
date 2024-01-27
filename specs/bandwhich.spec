%global debug_package %{nil}

Name:           bandwhich
Version:        0.22.0
Release:        1%{?dist}
Summary:        Terminal bandwidth utilization tool

License:        MIT
URL:            https://github.com/imsnif/bandwhich
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  gcc pkgconfig(openssl)

%description
This is a CLI utility for displaying current network utilization
by process, connection and remote IP/hostname.

%prep
%autosetup

# use latest stable version from rustup
curl -Lf "https://sh.rustup.rs" | sh -s -- --profile minimal -y

%build
source ~/.cargo/env
RUSTFLAGS="-C strip=symbols" cargo build --release

%check
source ~/.cargo/env
cargo test

%install
# bin
install -Dpm 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE.md
%doc CHANGELOG.md README.md
%{_bindir}/%{name}

%changelog
* Sun Jan 28 2024 cyqsimon - 0.22.0-1
- Release 0.22.0

* Mon Oct 16 2023 cyqsimon - 0.21.1-1
- Release 0.21.1
- Re-enable tests

* Tue Sep 19 2023 cyqsimon - 0.21.0-1
- Release 0.21.0

* Sat Mar 18 2023 cyqsimon - 0.20.0-2
- Run tests in debug mode

* Mon Jul 18 2022 cyqsimon - 0.20.0-1
- Release 0.20.0
