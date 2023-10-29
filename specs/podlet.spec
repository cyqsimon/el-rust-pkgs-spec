%global debug_package %{nil}

Name:           podlet
Version:        0.2.0
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
* Fri Oct 27 2023 cyqsimon - 0.2.0-1
- Release 0.2.0