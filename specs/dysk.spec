%global debug_package %{nil}

Name:           dysk
Version:        2.6.1
Release:        1%{?dist}
Summary:        A linux utility listing your filesystems (previously lfs)
Provides:       lfs = %{version}-%{release}
Obsoletes:      lfs <= 2.6.0

License:        MIT
URL:            https://github.com/Canop/dysk
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

# compatibility symlink
ln -sf %{_bindir}/%{name} %{buildroot}%{_bindir}/lfs

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/*

%changelog
* Tue Jul 04 2023 cyqsimon - 2.6.1-1
- Release 2.6.1
- Project renamed from `lfs` to `dysk`
- Create compatibility symlink from `lfs` to `dysk`

* Sat Mar 18 2023 cyqsimon - 2.6.0-2
- Run tests in debug mode

* Thu Dec 08 2022 cyqsimon - 2.6.0-1
- Release 2.6.0
