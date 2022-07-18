%global debug_package %{nil}
%global _unitdir %{_prefix}/lib/systemd/system

Name:           miniserve
Version:        0.20.0
Release:        2%{?dist}
Summary:        CLI tool to serve files and dirs over HTTP

License:        MIT
URL:            https://github.com/svenstaro/miniserve
Source0:        %{url}/archive/v%{version}.tar.gz

Requires:       bzip2-libs
BuildRequires:  gcc pkgconfig(bzip2)

%description
For when you really just want to serve some files over HTTP right now!

miniserve is a small, self-contained cross-platform CLI tool
that allows you to just grab the binary and serve some file(s) via HTTP.
Sometimes this is just a more practical and quick way than doing things properly.

%prep
%autosetup

# use latest stable version from rustup
curl -Lf "https://sh.rustup.rs" | sh -s -- --profile minimal -y

%build
source ~/.cargo/env
RUSTFLAGS="-C strip=symbols" cargo build --release

# generate manpage
target/release/%{name} --print-manpage > %{name}.1

# generate completions
target/release/%{name} --print-completions bash > %{name}.bash
target/release/%{name} --print-completions fish > %{name}.fish
target/release/%{name} --print-completions zsh > %{name}.zsh

%check
source ~/.cargo/env
cargo test --release

%install
# bin
install -Dpm 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

# unit
install -Dpm 644 packaging/%{name}@.service %{buildroot}%{_unitdir}/%{name}@.service

# manpage
install -Dpm 644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

# completions
install -Dpm 644 %{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dpm 644 %{name}.fish %{buildroot}%{_datadir}/fish/completions/%{name}.fish
install -Dpm 644 %{name}.zsh %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%{_unitdir}/%{name}@.service
%{_mandir}/man1/%{name}.1*
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/completions/%{name}.fish
%{_datadir}/zsh/site-functions/_%{name}

%changelog
* Tue Jul 19 2022 cyqsimon - 0.20.0-2
- Install unit file

* Mon Jul 18 2022 cyqsimon - 0.20.0-1
- Release 0.20.0
