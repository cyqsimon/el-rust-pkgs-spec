%global debug_package %{nil}

Name:           eza
Version:        0.14.0
Release:        1%{?dist}
Summary:        A modern, maintained replacement for ‘ls’
Provides:       exa = %{version}-%{release}
Obsoletes:      exa <= 0.10.1

License:        MIT
URL:            https://github.com/eza-community/eza
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  gcc pandoc

%description
eza is a modern, maintained replacement for the venerable file-listing
command-line program `ls` that ships with Unix and Linux operating systems,
giving it more features and better defaults.

It uses colours to distinguish file types and metadata. It knows about
symlinks, extended attributes, and Git. And it’s small, fast, and just one
single binary.

By deliberately making some decisions differently, eza attempts to be a more
featureful, more user-friendly version of `ls`.

%prep
%autosetup

# use latest stable version from rustup
curl -Lf "https://sh.rustup.rs" | sh -s -- --profile minimal -y

%build
source ~/.cargo/env
RUSTFLAGS="-C strip=symbols" cargo build --release

pandoc --standalone -f markdown -t man man/%{name}.1.md > %{name}.1
pandoc --standalone -f markdown -t man man/eza_colors-explanation.5.md > eza_colors-explanation.5
pandoc --standalone -f markdown -t man man/eza_colors.5.md > eza_colors.5

%check
source ~/.cargo/env
cargo test

%install
# bin
install -Dpm 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

# compatibility symlink
ln -sf %{_bindir}/%{name} %{buildroot}%{_bindir}/exa

# manpage
install -Dpm 644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -Dpm 644 eza_colors-explanation.5 %{buildroot}%{_mandir}/man5/eza_colors-explanation.5
install -Dpm 644 eza_colors.5 %{buildroot}%{_mandir}/man5/eza_colors.5

# doc
install -Dpm 644 LICEN?E %{buildroot}%{_docdir}/%{name}/LICENSE

# completions
install -Dpm 644 completions/bash/%{name} %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dpm 644 completions/fish/%{name}.fish %{buildroot}%{_datadir}/fish/completions/%{name}.fish
install -Dpm 644 completions/zsh/_%{name} %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%files
%doc CHANGELOG.md README.md
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_docdir}/%{name}/*
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/completions/%{name}.fish
%{_datadir}/zsh/site-functions/_%{name}

%changelog
* Tue Oct 03 2023 cyqsimon - 0.14.0-1
- Release 0.14.0

* Tue Sep 26 2023 cyqsimon - 0.13.1-1
- Release 0.13.1

* Tue Sep 19 2023 cyqsimon - 0.13.0-1
- Relaese 0.13.0

* Sun Sep 17 2023 cyqsimon - 0.12.0-1
- Release 0.12.0

* Tue Sep 12 2023 cyqsimon - 0.11.1-1
- Release 0.11.1

* Sun Sep 10 2023 cyqsimon - 0.11.0-1
- Release 0.11.0

