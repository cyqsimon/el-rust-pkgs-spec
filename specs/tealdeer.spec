%global debug_package %{nil}
%global _bin_name tldr

Name:           tealdeer
Version:        1.6.1
Release:        1%{?dist}
Summary:        A very fast implementation of tldr in Rust

License:        ASL 2.0 or MIT
URL:            https://github.com/dbrgn/tealdeer
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  gcc
# tldr from EPEL uses the same binary name.
# I know it's not recommended to declare Conflicts, but
# I can't be arsed to patch the completion files.
Conflicts:      tldr

%description
A very fast implementation of tldr in Rust:
Simplified, example based and community-driven man pages.

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
install -Dpm 755 target/release/%{_bin_name} %{buildroot}%{_bindir}/%{_bin_name}

# completions
install -Dpm 644 completion/bash_%{name} %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dpm 644 completion/fish_%{name} %{buildroot}%{_datadir}/fish/completions/%{name}.fish
install -Dpm 644 completion/zsh_%{name} %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%files
%license LICENSE-APACHE LICENSE-MIT
%doc CHANGELOG.md README.md RELEASING.md
%{_bindir}/%{_bin_name}
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/completions/%{name}.fish
%{_datadir}/zsh/site-functions/_%{name}

%changelog
* Tue Oct 25 2022 cyqsimon - 1.6.1-1
- Release 1.6.1

* Wed Oct 05 2022 cyqsimon - 1.6.0-1
- Release 1.6.0

* Sun Jul 17 2022 cyqsimon - 1.5.0-2
- Always prefer toolchain from rustup

* Fri Jul 15 2022 cyqsimon - 1.5.0-1
- Release 1.5.0
