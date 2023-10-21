%global debug_package %{nil}

Name:           xh
Version:        0.19.2
Release:        1%{?dist}
Summary:        Friendly and fast tool for sending HTTP requests

License:        MIT
URL:            https://github.com/ducaale/xh
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  gcc

%description
xh is a friendly and fast tool for sending HTTP requests.
It reimplements as much as possible of HTTPie's excellent design,
with a focus on improved performance.

%prep
%autosetup

# use latest stable version from rustup
curl -Lf "https://sh.rustup.rs" | sh -s -- --profile minimal -y

%build
source ~/.cargo/env
RUSTFLAGS="-C strip=symbols" cargo build --release

%check
source ~/.cargo/env
cargo test

%install
# bin
install -Dpm 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

# symlink
# `xh` will default to HTTPS scheme if the binary name is one of `xhs`, `https`, or `xhttps`
ln -sf %{_bindir}/%{name} %{_bindir}/%{name}s

# manpage
install -Dpm 644 doc/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

# completions
install -Dpm 644 completions/%{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dpm 644 completions/%{name}.fish %{buildroot}%{_datadir}/fish/completions/%{name}.fish
install -Dpm 644 completions/_%{name} %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/*
%{_mandir}/man1/%{name}.1*
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/completions/%{name}.fish
%{_datadir}/zsh/site-functions/_%{name}

%changelog
* Sun Oct 22 2023 cyqsimon - 0.19.2-1
- Release 0.19.2
