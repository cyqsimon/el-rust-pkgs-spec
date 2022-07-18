%global debug_package %{nil}

Name:           sd
Version:        0.7.6
Release:        3%{?dist}
Summary:        Intuitive find & replace CLI (sed alternative)

License:        MIT
URL:            https://github.com/chmln/sd
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  gcc

%description
sd is an intuitive find & replace CLI written in Rust that makes
find and replace using regular expressions fast and easy.

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
install -Dpm 644 target/release/build/%{name}-*/out/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

# completions
install -Dpm 644 target/release/build/%{name}-*/out/%{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dpm 644 target/release/build/%{name}-*/out/%{name}.fish %{buildroot}%{_datadir}/fish/completions/%{name}.fish
install -Dpm 644 target/release/build/%{name}-*/out/_%{name} %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/completions/%{name}.fish
%{_datadir}/zsh/site-functions/_%{name}

%changelog
* Sun Jul 17 2022 cyqsimon - 0.7.6-3
- Always prefer toolchain from rustup

* Thu Jul 14 2022 cyqsimon - 0.7.6-2
- Move Zsh completions to site-functions dir

* Wed Jul 13 2022 cyqsimon - 0.7.6-1
- Release 0.7.6
