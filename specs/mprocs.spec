%global debug_package %{nil}

Name:           mprocs
Version:        0.6.2
Release:        1%{?dist}
Summary:        Run multiple commands in parallel

License:        MIT
URL:            https://github.com/pvolok/mprocs
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  gcc

%description
mprocs runs multiple commands in parallel and shows output of
each command separately.

When you work on a project you very often need the same list of
commands to be running. For example: webpack serve, jest --watch,
node src/server.js. With mprocs you can list these command in
mprocs.yaml and run all of them by running mprocs. Then you can
switch between outputs of running commands and interact with them.

It is similar to concurrently but mprocs shows output of
each command separately and allows to interact with processes
(you can even work in vim inside mprocs).

%prep
%autosetup

# use latest stable version from rustup
curl -Lf "https://sh.rustup.rs" | sh -s -- --profile minimal -y

%build
source ~/.cargo/env
RUSTFLAGS="-C strip=symbols" cargo build --release

%check
source ~/.cargo/env
# see https://github.com/pvolok/mprocs/issues/50
#cargo test --release
cargo test --release --workspace --exclude mprocs-vt100

%install
# bin
install -Dpm 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{name}

%changelog
* Tue Aug 09 2022 cyqsimon - 0.6.2-1
- Release 0.6.2

* Sun Jul 17 2022 cyqsimon - 0.6.0-1
- Release 0.6.0
