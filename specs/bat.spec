%global debug_package %{nil}

Name:           bat
Version:        0.23.0
Release:        1%{?dist}
Summary:        A cat(1) clone with syntax highlighting and Git integration
License:        ASL 2.0 or MIT
URL:            https://github.com/sharkdp/bat
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  gcc pkgconfig(zlib)

%description
A cat(1) clone which supports syntax highlighting for a large number of
programming and markup languages. It has git integration and automatic paging.

%prep
%autosetup

# use latest stable version from rustup
curl -Lf "https://sh.rustup.rs" | sh -s -- --profile minimal -y

%build
source ~/.cargo/env
RUSTFLAGS="-C strip=symbols" cargo build --release

%check
source ~/.cargo/env
cargo test

%install
# bin
install -Dpm 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

# manpage
install -Dpm 644 target/release/build/%{name}-*/out/assets/manual/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

# completions
install -Dpm 644 target/release/build/%{name}-*/out/assets/completions/%{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dpm 644 target/release/build/%{name}-*/out/assets/completions/%{name}.fish %{buildroot}%{_datadir}/fish/completions/%{name}.fish
install -Dpm 644 target/release/build/%{name}-*/out/assets/completions/%{name}.zsh %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%files
%license LICENSE-APACHE LICENSE-MIT
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/completions/%{name}.fish
%{_datadir}/zsh/site-functions/_%{name}

%changelog
* Sat Mar 25 2023 cyqsimon - 0.23.0-1
- Release 0.23.0

* Sat Mar 18 2023 cyqsimon - 0.22.1-2
- Run tests in debug mode

* Sun Sep 11 2022 cyqsimon - 0.22.1-1
- Release 0.22.1

* Thu Sep 08 2022 cyqsimon - 0.22.0-1
- Release 0.22.0

* Sun Jul 17 2022 cyqsimon - 0.21.0-4
- Always prefer toolchain from rustup
- Add check

* Sat Jul 16 2022 cyqsimon - 0.21.0-3
- Follow Fish completion conventions

* Thu Jul 14 2022 cyqsimon - 0.21.0-2
- Install Bash completion
- Follow Zsh completion conventions

* Thu May 12 2022 Alex <redhat@att.org.ru> - 0.21.0-1
- Update to 0.21.0

* Sun Feb 27 2022 Alex <redhat@att.org.ru> - 0.20.0-1
- Update to 0.20.0

* Sat Jan  8 2022 Alex <redhat@att.org.ru> - 0.19.0-1
- Update to 0.19.0

* Sun Aug 22 2021 Alex <redhat@att.org.ru> - 0.18.3-1
- Update to 0.18.3

* Tue Jul 13 2021 Alex <redhat@att.org.ru> - 0.18.2-1
- Update to 0.18.2

* Thu May 13 2021 Alex <redhat@att.org.ru> - 0.18.1-1
- Update to 0.18.1

* Mon Mar  1 2021 Alex <redhat@att.org.ru> - 0.18.0-1
- Update to 0.18.0

* Sat Feb  6 2021 Alex <redhat@att.org.ru> - 0.17.1-2
- Added man

* Thu Jan 28 2021 David Salomon <david35mm@pm.me> - 0.17.1-1
- First package of bat
