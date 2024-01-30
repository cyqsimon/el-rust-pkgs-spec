%global debug_package %{nil}

Name:           podlet
Version:        0.2.4
Release:        1%{?dist}
Summary:        Generate podman quadlet (systemd-like) files from a podman command

License:        MPLv2.0
URL:            https://github.com/k9withabone/podlet
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  gcc

%description
Podlet generates podman quadlet (systemd-like) files from a podman command.

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
* Tue Jan 30 2024 cyqsimon - 0.2.4-1
- Release 0.2.4

* Mon Jan 01 2024 cyqsimon - 0.2.3-1
- Release 0.2.3

* Sat Dec 16 2023 cyqsimon - 0.2.2-1
- Release 0.2.2

* Wed Nov 29 2023 cyqsimon - 0.2.1-1
- Release 0.2.1

* Fri Oct 27 2023 cyqsimon - 0.2.0-1
- Release 0.2.0
