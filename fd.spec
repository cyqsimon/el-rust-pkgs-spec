%global debug_package %{nil}
%global _disable_source_fetch 0

Name:    fd
Version: 7.4.0
Release: 1%{?dist}
Summary: fd is a simple, fast and user-friendly alternative to find.
License: MIT/Apache-2.0
Group:   Applications/System
URL: https://github.com/sharkdp/fd
Source0: https://github.com/sharkdp/fd/archive/v%{version}.tar.gz

BuildRequires: gzip
BuildRequires: cargo

%description
fd is a simple, fast and user-friendly alternative to find.

While it does not seek to mirror all of find's powerful functionality,
it provides sensible (opinionated) defaults for 80% of the use cases.

%prep
%setup -q -n %{name}-%{version}

%build
cargo build --release

%check
cargo test

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}/usr/bin/
mkdir -p ${RPM_BUILD_ROOT}/usr/share/bash-completion/completions/
mkdir -p ${RPM_BUILD_ROOT}/usr/share/fish/completions/
mkdir -p ${RPM_BUILD_ROOT}/usr/share/zsh/vendor-completions/
mkdir -p ${RPM_BUILD_ROOT}/usr/share/man/man1/
mkdir -p ${RPM_BUILD_ROOT}/usr/share/doc/%{name}/

# Bin
install -pm 0755 target/release/%{name} ${RPM_BUILD_ROOT}/usr/bin/%{name}

# manpage
install -Dm644 doc/%{name}.1 ${RPM_BUILD_ROOT}/usr/share/man/man1/%{name}.1
gzip --best ${RPM_BUILD_ROOT}/usr/share/man/man1/%{name}.1

# doc
install -Dm644 README.md ${RPM_BUILD_ROOT}/usr/share/doc/%{name}/README.md
install -Dm644 LICENSE-MIT ${RPM_BUILD_ROOT}/usr/share/doc/%{name}/LICENSE-MIT
install -Dm644 LICENSE-APACHE ${RPM_BUILD_ROOT}/usr/share/doc/%{name}/LICENSE-APACHE

# completions
install -Dm644 target/release/build/fd-find-*/out/%{name}.bash ${RPM_BUILD_ROOT}/usr/share/bash-completion/completions/%{name}
install -Dm644 target/release/build/fd-find-*/out/%{name}.fish ${RPM_BUILD_ROOT}/usr/share/fish/completions/%{name}.fish
install -Dm644  target/release/build/fd-find-*/out/_%{name} ${RPM_BUILD_ROOT}/usr/share/zsh/vendor-completions/_%{name}

%files
%defattr(-,root,root,-)
/usr/bin/%{name}
/usr/share/doc/fd/*
/usr/share/man/man1/fd.1.gz
/usr/share/bash-completion/completions/fd
/usr/share/fish/completions/fd.fish
/usr/share/zsh/vendor-completions/_fd

%changelog
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
