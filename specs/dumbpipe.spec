%global debug_package %{nil}

Name:           dumbpipe
Version:        0.39.0
Release:        2%{?dist}
Summary:        Unix pipes between devices

License:        Apache-2.0 OR MIT
URL:            https://github.com/n0-computer/dumbpipe
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  gcc

%description
Dumb pipe punches through NATs, using on-the-fly node identifiers.
It even keeps your machines connected as network conditions change.

%prep
%autosetup

# use latest stable version from rustup
curl -Lf "https://sh.rustup.rs" | sh -s -- --profile minimal -y

%build
source ~/.cargo/env
cargo +stable build --release

%check
source ~/.cargo/env
cargo +stable test -- --skip connect_tcp_happy

%install
# bin
install -Dpm 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE-APACHE LICENSE-MIT
%doc README.md
%{_bindir}/%{name}

%changelog
* Mon Sep 21 2026 cyqsimon - 0.39.0-2
- Disable flaky test `connect_tcp_happy` for now
  - Using sleep to wait for listener is inherently unreliable

* Sun Sep 20 2026 cyqsimon - 0.39.0-1
- Release 0.39.0
