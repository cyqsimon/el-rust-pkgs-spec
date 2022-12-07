%global debug_package %{nil}

Name:           dog
Version:        0.1.0
Release:        1%{?dist}
Summary:        A command-line DNS client

License:        EUPL 1.2
URL:            https://github.com/ogham/dog
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  gcc
%if 0%{?rhel} >= 9
BuildRequires:  compat-openssl11 rubygem-ronn-ng
%else
# rubygem-ronn on EL7 is provided by Springdale Computational
# this repository is added to the EL7 chroot on Copr
BuildRequires:  pkgconfig(openssl) rubygem-ronn
%endif

%description
Dogs can look up!

dog is a command-line DNS client, like dig. It has colourful output,
understands normal command-line argument syntax, supports the DNS-over-TLS
and DNS-over-HTTPS protocols, and can emit JSON.

%prep
%autosetup

# use latest stable version from rustup
curl -Lf "https://sh.rustup.rs" | sh -s -- --profile minimal -y

%build
source ~/.cargo/env
RUSTFLAGS="-C strip=symbols" cargo build --release

ronn --roff man/%{name}.1.md

%check
source ~/.cargo/env
cargo test --release

%install
# bin
install -Dpm 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

# manpage
install -Dpm 644 man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

# completions
install -Dpm 644 completions/%{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dpm 644 completions/%{name}.fish %{buildroot}%{_datadir}/fish/completions/%{name}.fish
install -Dpm 644 completions/%{name}.zsh %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%files
%license LICENCE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/completions/%{name}.fish
%{_datadir}/zsh/site-functions/_%{name}

%changelog
* Wed Dec 07 2022 cyqsimon - 0.1.0-1
- Release 0.1.0
