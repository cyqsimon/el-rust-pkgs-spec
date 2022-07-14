%global debug_package %{nil}

Name:           bat
Version:        0.21.0
Release:        2%{?dist}
Summary:        A cat(1) clone with syntax highlighting and Git integration
License:        Apache 2.0 or MIT
URL:            https://github.com/sharkdp/bat
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  cargo rust zlib-devel

%description
A cat(1) clone which supports syntax highlighting for a large number of
programming and markup languages. It has git integration and automatic paging.

%prep
%autosetup

%build
RUSTFLAGS="-C strip=symbols" cargo build --release

%install
%if 0%{?el7}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
mkdir -p %{buildroot}%{_datadir}/fish/vendor_completions.d
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions
%endif

install -Dm644 -t %{buildroot}%{_mandir}/man1 target/release/build/%{name}-*/out/assets/manual/%{name}.1
install -Dm644 target/release/build/%{name}-*/out/assets/completions/%{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dm644 target/release/build/%{name}-*/out/assets/completions/%{name}.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish
install -Dm644 target/release/build/%{name}-*/out/assets/completions/%{name}.zsh %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%files
%license LICENSE-MIT LICENSE-APACHE
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/fish/vendor_completions.d/%{name}.fish
%{_datadir}/zsh/vendor-completions/_%{name}

%changelog
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
