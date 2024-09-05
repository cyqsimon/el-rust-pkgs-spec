%global debug_package %{nil}

Name:           eza
Version:        0.19.2
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
cargo +stable build --release

pandoc --standalone -f markdown -t man man/%{name}.1.md > %{name}.1
pandoc --standalone -f markdown -t man man/eza_colors-explanation.5.md > eza_colors-explanation.5
pandoc --standalone -f markdown -t man man/eza_colors.5.md > eza_colors.5

%check
source ~/.cargo/env
cargo +stable test

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
* Thu Sep 05 2024 cyqsimon - 0.19.2-1
- Release 0.19.2

* Thu Aug 29 2024 cyqsimon - 0.19.1-1
- Release 0.19.1

* Thu Aug 08 2024 cyqsimon - 0.19.0-1
- Release 0.19.0

* Sun Aug 04 2024 cyqsimon - 0.18.24-1
- Release 0.18.24

* Thu Jul 25 2024 cyqsimon - 0.18.23-1
- Release 0.18.23

* Fri Jul 19 2024 cyqsimon - 0.18.22-1
- Release 0.18.22

* Mon Jul 01 2024 cyqsimon - 0.18.21-1
- Release 0.18.21

* Thu Jun 27 2024 cyqsimon - 0.18.20-1
- Release 0.18.20

* Thu Jun 20 2024 cyqsimon - 0.18.19-1
- Release 0.18.19

* Thu Jun 13 2024 cyqsimon - 0.18.18-1
- Release 0.18.18

* Fri Jun 07 2024 cyqsimon - 0.18.17-1
- Release 0.18.17

* Fri May 17 2024 cyqsimon - 0.18.16-1
- Release 0.18.16

* Fri May 10 2024 cyqsimon - 0.18.15-1
- Release 0.18.15

* Thu May 02 2024 cyqsimon - 0.18.14-1
- Release 0.18.14

* Fri Apr 26 2024 cyqsimon - 0.18.13-1
- Release 0.18.13

* Fri Apr 19 2024 cyqsimon - 0.18.11-1
- Release 0.18.11

* Tue Apr 16 2024 cyqsimon - 0.18.10-2
- Remove explicit stripping (strip enabled by default since 1.77.0)

* Thu Apr 11 2024 cyqsimon - 0.18.10-1
- Release 0.18.10

* Wed Mar 27 2024 cyqsimon - 0.18.9-1
- Release 0.18.9

* Thu Mar 21 2024 cyqsimon - 0.18.8-1
- Release 0.18.8

* Fri Mar 15 2024 cyqsimon - 0.18.7-1
- Release 0.18.7

* Wed Mar 06 2024 cyqsimon - 0.18.6-1
- Release 0.18.6

* Thu Feb 29 2024 cyqsimon - 0.18.5-1
- Release 0.18.5

* Thu Feb 22 2024 cyqsimon - 0.18.4-1
- Release 0.18.4

* Mon Feb 19 2024 cyqsimon - 0.18.3-1
- Release 0.18.3

* Sat Feb 10 2024 cyqsimon - 0.18.2-1
- Release 0.18.2

* Thu Feb 01 2024 cyqsimon - 0.18.0-1
- Release 0.18.0

* Fri Jan 26 2024 cyqsimon - 0.17.3-1
- Release 0.17.3

* Sun Jan 21 2024 cyqsimon - 0.17.2-1
- Release 0.17.2

* Sat Jan 13 2024 cyqsimon - 0.17.1-1
- Release 0.17.1

* Thu Dec 14 2023 cyqsimon - 0.17.0-1
- Release 0.17.0

* Fri Dec 08 2023 cyqsimon - 0.16.3-1
- Release 0.16.3

* Fri Dec 01 2023 cyqsimon - 0.16.2-1
- Release 0.16.2

* Thu Nov 23 2023 cyqsimon - 0.16.1-1
- Release 0.16.1

* Fri Nov 17 2023 cyqsimon - 0.16.0-1
- Release 0.16.0

* Thu Nov 09 2023 cyqsimon - 0.15.3-1
- Release 0.15.3

* Thu Nov 02 2023 cyqsimon - 0.15.2-1
- Release 0.15.2

* Thu Oct 26 2023 cyqsimon - 0.15.1-1
- Release 0.15.1

* Fri Oct 20 2023 cyqsimon - 0.15.0-1
- Release 0.15.0

* Sat Oct 14 2023 cyqsimon - 0.14.2-2
- Explicitly set toolchain version `stable`

* Thu Oct 12 2023 cyqsimon - 0.14.2-1
- Release 0.14.2

* Sun Oct 08 2023 cyqsimon - 0.14.1-1
- Release 0.14.1

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
