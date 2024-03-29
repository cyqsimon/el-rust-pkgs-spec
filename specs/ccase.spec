%global debug_package %{nil}

Name:           ccase
Version:        0.4.1
Release:        1%{?dist}
Summary:        A command line utility for converting between string cases

License:        MIT
URL:            https://github.com/rutrum/ccase
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  gcc

%description
Convert strings between snake case, kebab case, camel case, title case, pascal
case, and so many more.

%prep
%autosetup

# use latest stable version from rustup
curl -Lf "https://sh.rustup.rs" | sh -s -- --profile minimal -y

%build
source ~/.cargo/env
RUSTFLAGS="-C strip=symbols" cargo build --release

%check
source ~/.cargo/env
# tests require the debug binary to be built
cargo build
cargo test

%install
# bin
install -Dpm 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}

%changelog
* Fri Jan 05 2024 cyqsimon - 0.4.1-1
- Release 0.4.1
