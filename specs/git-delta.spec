%global debug_package %{nil}
%global _bin_name delta

Name:           git-delta
Version:        0.13.0
Release:        2%{?dist}
Summary:        A syntax-highlighting pager for git, diff, and grep output

License:        MIT
URL:            https://github.com/dandavison/delta
Source0:        %{url}/archive/%{version}.tar.gz

BuildRequires:  gcc git

%description
Code evolves, and we all spend time studying diffs.

Delta aims to make this both efficient and enjoyable:
it allows you to make extensive changes to the layout and styling of diffs,
as well as allowing you to stay arbitrarily close to the default git/diff output.

%prep
%autosetup -n %{_bin_name}-%{version}

# use latest stable version from rustup
curl -Lfo "rustup.sh" "https://sh.rustup.rs"
chmod +x "rustup.sh"
./rustup.sh --profile minimal -y

%build
source ~/.cargo/env
RUSTFLAGS="-C strip=symbols" cargo build --release

%check
source ~/.cargo/env
cargo test

%install
# bin
install -Dpm 755 target/release/%{_bin_name} %{buildroot}%{_bindir}/%{_bin_name}

# completions
install -Dpm 644 etc/completion/completion.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dpm 644 etc/completion/completion.zsh %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%files
%license LICENSE
%doc ARCHITECTURE.md README.md
%{_bindir}/%{_bin_name}
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/zsh/site-functions/_%{name}

%changelog
* Sun Jul 17 2022 cyqsimon - 0.13.0-2
- Always prefer toolchain from rustup

* Sun Jul 17 2022 cyqsimon - 0.13.0-1
- Release 0.13.0
