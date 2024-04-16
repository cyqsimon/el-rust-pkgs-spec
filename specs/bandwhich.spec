%global debug_package %{nil}

Name:           bandwhich
Version:        0.22.2
Release:        2%{?dist}
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

mkdir gen
BANDWHICH_GEN_DIR="$(pwd)/gen" cargo +stable build --release

%check
source ~/.cargo/env
cargo +stable test

%install
# bin
install -Dpm 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

# manpage
install -Dpm 644 gen/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

# completions
install -Dpm 644 gen/%{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dpm 644 gen/%{name}.fish %{buildroot}%{_datadir}/fish/completions/%{name}.fish
install -Dpm 644 gen/_%{name} %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%files
%license LICENSE.md
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%{_mandir}/man1/*
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/completions/%{name}.fish
%{_datadir}/zsh/site-functions/_%{name}

%changelog
* Tue Apr 16 2024 cyqsimon - 0.22.2-2
- Remove explicit stripping (strip enabled by default since 1.77.0)

* Mon Jan 29 2024 cyqsimon - 0.22.2-1
- Release 0.22.2
- Install manpage & shell completions

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
