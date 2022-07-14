%global debug_package %{nil}

Name:    sd
Version: 0.7.6
Release: 1%{?dist}
Summary: Intuitive find & replace CLI (sed alternative)

License: MIT
URL: https://github.com/chmln/sd
Source0: %{url}/archive/v%{version}.tar.gz

BuildRequires: cargo rust

%description
sd is an intuitive find & replace CLI written in Rust that makes
find and replace using regular expressions fast and easy.

%prep
%autosetup

%build
RUSTFLAGS="-C strip=symbols" cargo build --release

%check
cargo test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
mkdir -p %{buildroot}%{_datadir}/fish/completions
mkdir -p %{buildroot}%{_datadir}/zsh/vendor-completions
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_docdir}/%{name}

# Bin
install -pm 0755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

# manpage
install -Dm644 target/release/build/%{name}-*/out/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

# doc
install -Dm644 README.md %{buildroot}%{_docdir}/%{name}/README.md
install -Dm644 CHANGELOG.md %{buildroot}%{_docdir}/%{name}/CHANGELOG.md
install -Dm644 LICENSE %{buildroot}%{_docdir}/%{name}/LICENSE

# completions
install -Dm644 target/release/build/%{name}-*/out/%{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dm644 target/release/build/%{name}-*/out/%{name}.fish %{buildroot}%{_datadir}/fish/completions/%{name}.fish
install -Dm644 target/release/build/%{name}-*/out/_%{name} %{buildroot}%{_datadir}/zsh/vendor-completions/_%{name}

%files
%{_bindir}/%{name}
%{_docdir}/%{name}/*
%{_mandir}/man1/%{name}.1*
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/completions/%{name}.fish
%{_datadir}/zsh/vendor-completions/_%{name}

%changelog
* Wed Jul 13 2022 cyqsimon - 0.7.6-1
- Release 0.7.6
