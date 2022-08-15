%global debug_package %{nil}

Name:           fd
Version:        8.4.0
Release:        4%{?dist}
Summary:        A simple, fast and user-friendly alternative to find

License:        ASL 2.0 or MIT
URL:            https://github.com/sharkdp/fd
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  gcc

%description
fd is a program to find entries in your filesystem.
It is a simple, fast and user-friendly alternative to find.

While it does not aim to support all of find's powerful functionality,
it provides sensible (opinionated) defaults for a majority of use cases.

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
install -Dpm 644 doc/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

# completions
install -Dpm 644 target/release/build/fd-find-*/out/%{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dpm 644 target/release/build/fd-find-*/out/%{name}.fish %{buildroot}%{_datadir}/fish/completions/%{name}.fish
install -Dpm 644 contrib/completion/_%{name} %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%files
%license LICENSE-APACHE LICENSE-MIT
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/completions/%{name}.fish
%{_datadir}/zsh/site-functions/_%{name}

%changelog
* Sun Jul 17 2022 cyqsimon - 8.4.0-4
- Always prefer toolchain from rustup

* Thu Jul 14 2022 cyqsimon - 8.4.0-3
- Move Zsh completion to site-functions dir

* Wed Jul 13 2022 cyqsimon - 8.4.0-2
- Auto-gzip man page

* Wed Jul 13 2022 cyqsimon - 8.4.0-1
- Forked from recteurlp/fd
- Release 8.4.0

* Fri Oct 04 2019 recteurlp <recteurlp@pyrmin.io> - 7.4.0-1
- Release 7.4.0

* Sun Mar 31 2019 recteurlp <recteurlp@pyrmin.io> - 7.3.0-1
- Release 7.3.0

* Mon Oct 01 2018 recteurlp <recteurlp@pyrmin.io> - 7.1.0-1
- Release 7.1.0

* Wed Feb 21 2018 recteurlp <recteurlp@pyrmin.io> - 7.0.0-1
- Release 7.0.0

* Wed Feb 21 2018 recteurlp <recteurlp@pyrmin.io> - 6.3.0-1
- Release 6.3.0
