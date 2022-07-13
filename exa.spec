%global debug_package %{nil}

Name:    exa
Version: 0.10.1
Release: 1%{?dist}
Summary: A modern replacement for ‘ls’.

License: MIT
URL: https://github.com/ogham/exa
Source0: https://github.com/ogham/exa/archive/v%{version}.tar.gz

BuildRequires: cargo pandoc rust

%description
exa is a modern replacement for the venerable file-listing command-line
program ls that ships with Unix and Linux operating systems,
giving it more features and better defaults.

It uses colours to distinguish file types and metadata.
It knows about symlinks, extended attributes, and Git.
And it’s small, fast, and just one single binary.

%prep
%autosetup

%build
RUSTFLAGS="-C strip=symbols" cargo build --release
pandoc --standalone -f markdown -t man man/%{name}.1.md > %{name}.1
pandoc --standalone -f markdown -t man man/exa_colors.5.md > exa_colors.5

%check
cargo test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
mkdir -p %{buildroot}%{_datadir}/fish/completions
mkdir -p %{buildroot}%{_datadir}/zsh/vendor-completions
mkdir -p %{buildroot}%{_mandir}/{man1,man5}
mkdir -p %{buildroot}%{_docdir}/%{name}

# Bin
install -Dm755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

# manpage
install -Dm644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -Dm644 exa_colors.5 %{buildroot}%{_mandir}/man5/exa_colors.5

# doc
install -Dm644 README.md %{buildroot}%{_docdir}/%{name}/README.md
install -Dm644 LICENSE %{buildroot}%{_docdir}/%{name}/LICENSE

# completions
install -Dm644 completions/completions.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dm644 completions/completions.fish  %{buildroot}%{_datadir}/fish/completions/%{name}.fish
install -Dm644 completions/completions.zsh  %{buildroot}%{_datadir}/zsh/vendor-completions/_%{name}

%files
%{_bindir}/%{name}
%{_docdir}/%{name}/*
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/exa_colors.5*
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/completions/%{name}.fish
%{_datadir}/zsh/vendor-completions/_%{name}

%changelog
* Wed Jul 13 2022 cyqsimon - 0.10.1-1
- Release 0.10.1
