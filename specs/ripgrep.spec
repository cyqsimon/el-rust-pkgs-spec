%global debug_package %{nil}
%global _bin_name rg

Name:           ripgrep
Version:        13.0.0
Release:        3%{?dist}
Summary:        A search tool that combines the usability of ag with the raw speed of grep

License:        MIT or Unlicense
URL:            https://github.com/BurntSushi/ripgrep
Source0:        %{url}/archive/%{version}.tar.gz

BuildRequires:  asciidoc gcc

%description
ripgrep is a line-oriented search tool that recursively searches your current
directory for a regex pattern while respecting your gitignore rules.

ripgrep is similar to other popular search tools like The Silver Searcher,
ack and grep.

%prep
%autosetup

# use latest stable version from rustup
curl -Lfo "rustup.sh" "https://sh.rustup.rs"
chmod +x "rustup.sh"
./rustup.sh --profile minimal -y

%build
source ~/.cargo/env
RUSTFLAGS="-C strip=symbols" cargo build --release

%check
source ~/.cargo/env
cargo test --release

%install
# bin
install -Dpm 755 target/release/%{_bin_name} %{buildroot}%{_bindir}/%{_bin_name}

# manpage
install -Dpm 644 target/release/build/ripgrep-*/out/%{_bin_name}.1 %{buildroot}%{_mandir}/man1/%{_bin_name}.1

# completions
install -Dpm 644 target/release/build/ripgrep-*/out/%{_bin_name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{_bin_name}
install -Dpm 644 target/release/build/ripgrep-*/out/%{_bin_name}.fish %{buildroot}%{_datadir}/fish/completions/%{_bin_name}.fish
install -Dpm 644 complete/_%{_bin_name} %{buildroot}%{_datadir}/zsh/site-functions/_%{_bin_name}

%files
%license COPYING LICENSE-MIT UNLICENSE
%doc CHANGELOG.md FAQ.md GUIDE.md README.md
%{_bindir}/%{_bin_name}
%{_mandir}/man1/%{_bin_name}.1*
%{_datadir}/bash-completion/completions/%{_bin_name}
%{_datadir}/fish/completions/%{_bin_name}.fish
%{_datadir}/zsh/site-functions/_%{_bin_name}

%changelog
* Sun Jul 17 2022 cyqsimon - 13.0.0-3
- Always prefer toolchain from rustup

* Sat Jul 16 2022 cyqsimon - 13.0.0-2
- Follow Fish completion conventions

* Wed Jul 13 2022 cyqsimon - 13.0.0-1
- Forked from carlwgeorge/ripgrep
- Release 13.0.0
- Fix declared files
- Strip binaries

* Thu Dec 31 2020 Konstantin Glukhov <konstantin@konstantin.computer> - 12.1.1-1
- Latest upstream

* Mon Jun 10 2019 Carl George <carl@george.computer> - 11.0.1-1
- Latest upstream

* Mon Sep 10 2018 Carl George <carl@george.computer> - 0.10.0-1
- Latest upstream

* Mon Aug 06 2018 Carl George <carl@george.computer> - 0.9.0-1
- Latest upstream

* Sat Mar 03 2018 Carl George <carl@george.computer> - 0.8.1-1
- Latest upstream

* Tue Feb 13 2018 Carl George <carl@george.computer> - 0.8.0-1
- Latest upstream
- Man page is now generated during build
- Bash completion filename updated
- Include new guide and FAQ files

* Tue Nov 07 2017 Carl George <carl@george.computer> - 0.7.1-1
- Latest upstream

* Fri Jul 07 2017 Carl George <carl@george.computer> - 0.5.2-1
- Latest upstream
- Add zsh and fish completions

* Mon Apr 24 2017 Carl George <carl.george@rackspace.com> - 0.5.1-1
- Latest upstream

* Wed Mar 15 2017 Carl George <carl.george@rackspace.com> - 0.5.0-1
- Latest upstream

* Sun Dec 25 2016 Carl George <carl.george@rackspace.com> - 0.3.2-1
- Latest upstream
- Add bash completion
- Enable build for EPEL7 aarch64

* Sun Nov 27 2016 Carl George <carl.george@rackspace.com> - 0.3.1-1
- Latest upstream

* Sat Nov 12 2016 Carl George <carl.george@rackspace.com> - 0.2.9-1
- Latest upstream

* Mon Nov 07 2016 Carl George <carl.george@rackspace.com> - 0.2.8-1
- Latest upstream

* Thu Oct 13 2016 Carl George <carl.george@rackspace.com> - 0.2.3-1
- Latest upstream
- Set ExclusiveArch to match build requirements

* Thu Sep 29 2016 Carl George <carl.george@rackspace.com> - 0.2.1-1
- Initial spec file
