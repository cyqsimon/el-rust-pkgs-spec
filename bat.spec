%global debug_package %{nil}

Name:           bat
Version:        0.21.0
Release:        1%{?dist}
Summary:        A cat(1) clone with syntax highlighting and Git integration
License:        ASL 2.0
URL:            https://github.com/sharkdp/%{name}
Source0:        https://github.com/sharkdp/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cargo
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  rust
BuildRequires:  rust-std-static
BuildRequires:  zlib-devel

%description
A cat(1) clone which supports syntax highlighting for a large number of
programming and markup languages. It has git integration and automatic paging.

%prep
%autosetup -n %{name}-%{version}

%build

%install
cargo install --no-track --root=%{buildroot}%{_prefix} --path .
%if 0%{?rhel} == 7
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_datadir}/fish/vendor_completions.d
mkdir -p %{buildroot}%{_datadir}/zsh/vendor-completions
%endif
install -v -Dpm0644 -t %{buildroot}%{_mandir}/man1 target/release/build/%{name}-*/out/assets/manual/bat.1
install -v -Dpm0644 -t %{buildroot}%{_datadir}/fish/vendor_completions.d target/release/build/%{name}-*/out/assets/completions/bat.fish
install -v -Dpm0644 -t %{buildroot}%{_datadir}/zsh/vendor-completions target/release/build/%{name}-*/out/assets/completions/bat.zsh

%files
%license LICENSE-MIT LICENSE-APACHE
%doc README.md
%{_bindir}/bat
%{_mandir}/man1/bat.1*
%{_datadir}/fish/vendor_completions.d/bat.fish
%{_datadir}/zsh/vendor-completions/bat.zsh

%changelog
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
