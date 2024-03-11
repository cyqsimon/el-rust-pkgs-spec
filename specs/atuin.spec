%global debug_package %{nil}

Name:           atuin
Version:        18.1.0
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
cargo test --workspace --all-features --lib

%install
# bin
install -Dpm 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

# completions
install -Dpm 644 %{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dpm 644 %{name}.fish %{buildroot}%{_datadir}/fish/completions/%{name}.fish
install -Dpm 644 _%{name} %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/completions/%{name}.fish
%{_datadir}/zsh/site-functions/_%{name}

%changelog
* Tue Mar 12 2024 cyqsimon - 18.1.0-1
- Release 18.1.0

* Tue Feb 27 2024 cyqsimon - 18.0.2-1
- Release 18.0.2

* Tue Feb 13 2024 cyqsimon - 18.0.1-1
- Release 18.0.1

* Sat Feb 10 2024 cyqsimon - 18.0.0-1
- Release 18.0.0

* Fri Jan 05 2024 cyqsimon - 17.2.1-1
- Release 17.2.1

* Mon Dec 11 2023 cyqsimon - 17.1.0-1
- Release 17.1.0

* Tue Oct 31 2023 cyqsimon - 17.0.1-1
- Release 17.0.1

* Tue Aug 08 2023 cyqsimon - 16.0.0-1
- Relaese 16.0.0

* Mon May 29 2023 cyqsimon - 15.0.0-1
- Release 15.0.0

* Tue Apr 18 2023 cyqsimon - 14.0.1-1
- Release 14.0.1

* Sun Apr 02 2023 cyqsimon - 14.0.0-1
- Release 14.0.0

* Sat Mar 18 2023 cyqsimon - 13.0.1-3
- Run tests in debug mode

* Thu Mar 02 2023 cyqsimon - 13.0.1-2
- Run all tests in workspace

* Wed Mar 01 2023 cyqsimon - 13.0.1-1
- Release 13.0.1

* Mon Feb 27 2023 cyqsimon - 13.0.0-1
- Release 13.0.0

* Thu Dec 08 2022 cyqsimon - 12.0.0-1
- Release 12.0.0
