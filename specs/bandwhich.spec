%global debug_package %{nil}

Name:           bandwhich
Version:        0.20.0
Release:        1%{?dist}
Summary:        Terminal bandwidth utilization tool

License:        MIT
URL:            https://github.com/imsnif/bandwhich
Source0:        %{url}/archive/%{version}.tar.gz

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
cargo test --release

%install
# bin
install -Dpm 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

# manpage
install -Dpm 644 docs/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%license LICENSE.md
%doc CHANGELOG.md demo.gif README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Mon Jul 18 2022 cyqsimon - 0.20.0-1
- Release 0.20.0
