%global debug_package %{nil}

Name:           lfs
Version:        2.6.0
Release:        2%{?dist}
Summary:        A linux utility listing your filesystems

License:        MIT
URL:            https://github.com/Canop/lfs
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  gcc

%description
A linux utility to get information on filesystems, like df but better.

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
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{name}

%changelog
* Sat Mar 18 2023 cyqsimon - 2.6.0-2
- Run tests in debug mode

* Thu Dec 08 2022 cyqsimon - 2.6.0-1
- Release 2.6.0
