%global debug_package %{nil}
%global bin_name dym

Name:           didyoumean
Version:        1.1.4
Release:        1%{?dist}
Summary:        A CLI spelling corrector for when you're unsure

License:        GPLv3
URL:            https://github.com/hisbaan/didyoumean
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  gcc pkgconfig(openssl) pkgconfig(xcb)

%description
DidYouMean (or dym) is a command-line spelling corrector written in rust
utilizing a simplified version of Damerau-Levenshtein distance. DidYouMean is
for those moments when you know what a word sounds like, but you're not quite
sure how it's spelled.

%prep
%autosetup

# use latest stable version from rustup
curl -Lf "https://sh.rustup.rs" | sh -s -- --profile minimal -y

%build
source ~/.cargo/env
RUSTFLAGS="-C strip=symbols" cargo build --release

%check
source ~/.cargo/env
# X11 is not running in build environment
cargo test -- --skip yank_test

%install
# bin
install -Dpm 755 target/release/%{bin_name} %{buildroot}%{_bindir}/%{bin_name}

# manpage
install -Dpm 644 man/%{bin_name}.1 %{buildroot}%{_mandir}/man1/%{bin_name}.1

# completions
install -Dpm 644 completions/%{bin_name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{bin_name}
install -Dpm 644 completions/%{bin_name}.fish %{buildroot}%{_datadir}/fish/completions/%{bin_name}.fish
install -Dpm 644 completions/_%{bin_name} %{buildroot}%{_datadir}/zsh/site-functions/_%{bin_name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{bin_name}
%{_mandir}/man1/%{bin_name}.1*
%{_datadir}/bash-completion/completions/%{bin_name}
%{_datadir}/fish/completions/%{bin_name}.fish
%{_datadir}/zsh/site-functions/_%{bin_name}

%changelog
* Wed Mar 29 2023 cyqsimon - 1.1.4-1
- Release 1.1.4
