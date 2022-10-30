%global debug_package %{nil}

Name:           garbage
Version:        0.4.0
Release:        1%{?dist}
Summary:        Soft-deletion CLI tool with FreeDesktop Trash compatibility

License:        GPLv3
URL:            https://git.sr.ht/~mzhang/garbage
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  gcc git

%description
Soft-deletion CLI tool with FreeDesktop Trash compatibility.

Rust version of 'trash-cli'.

%prep
%autosetup -n %{name}-v%{version}

# use latest stable version from rustup
curl -Lf "https://sh.rustup.rs" | sh -s -- --profile minimal -y

%build
source ~/.cargo/env
RUSTFLAGS="-C strip=symbols" cargo build --release

# generate completions
target/release/%{name} generate-completions bash > %{name}.bash
target/release/%{name} generate-completions fish > %{name}.fish
target/release/%{name} generate-completions zsh > %{name}.zsh

%check
source ~/.cargo/env
cargo test --release

%install
# bin
install -Dpm 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

# completions
install -Dpm 644 %{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dpm 644 %{name}.fish %{buildroot}%{_datadir}/fish/completions/%{name}.fish
install -Dpm 644 %{name}.zsh %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%files
%license LICENSE.md
%doc README.md
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/completions/%{name}.fish
%{_datadir}/zsh/site-functions/_%{name}

%changelog
* Sun Oct 30 2022 cyqsimon - 0.4.0-1
- Release 0.4.0
- Install shell completions

* Sun Jul 17 2022 cyqsimon - 0.3.3-2
- Always prefer toolchain from rustup

* Sun Jul 17 2022 cyqsimon - 0.3.3-1
- Release 0.3.3
