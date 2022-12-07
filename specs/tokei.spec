%global debug_package %{nil}

Name:           tokei
Version:        12.1.2
Release:        1%{?dist}
Summary:        Count your code, quickly

License:        ASL 2.0 and MIT
URL:            https://github.com/XAMPPRocky/tokei
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  gcc

%description
Tokei is a program that displays statistics about your code. Tokei will
show the number of files, total lines within those files and code,
comments, and blanks grouped by language.

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

%files
%license LICENCE-APACHE LICENCE-MIT
%doc CHANGELOG.md README.md
%{_bindir}/%{name}

%changelog
* Thu Dec 08 2022 cyqsimon - 12.1.2-1
- Release 12.1.2
