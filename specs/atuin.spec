%global debug_package %{nil}

Name:           atuin
Version:        13.0.1
Release:        1%{?dist}
Summary:        Magical shell history

License:        MIT
URL:            https://github.com/ellie/atuin
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  gcc

%description
Atuin replaces your existing shell history with a SQLite database, and
records additional context for your commands. Additionally, it provides
optional and fully encrypted synchronisation of your history between
machines, via an Atuin server.

%prep
%autosetup

# use latest stable version from rustup
curl -Lf "https://sh.rustup.rs" | sh -s -- --profile minimal -y

%build
source ~/.cargo/env
RUSTFLAGS="-C strip=symbols" cargo build --release

for SHELL in "bash" "fish" "zsh"; do
    target/release/%{name} gen-completions --shell $SHELL -o .
done

%check
source ~/.cargo/env
cargo test --release

%install
# bin
install -Dpm 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

# completions
install -Dpm 644 %{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dpm 644 %{name}.fish %{buildroot}%{_datadir}/fish/completions/%{name}.fish
install -Dpm 644 _%{name} %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/completions/%{name}.fish
%{_datadir}/zsh/site-functions/_%{name}

%changelog
* Wed Mar 01 2023 cyqsimon - 13.0.1-1
- Release 13.0.1

* Mon Feb 27 2023 cyqsimon - 13.0.0-1
- Release 13.0.0

* Thu Dec 08 2022 cyqsimon - 12.0.0-1
- Release 12.0.0
