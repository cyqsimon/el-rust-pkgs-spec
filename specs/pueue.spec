%global debug_package %{nil}

Name:           pueue
Version:        4.0.0
Release:        1%{?dist}
Summary:        CLI task manager for long-running tasks

License:        MIT
URL:            https://github.com/Nukesor/pueue
Source0:        %{url}/archive/v%{version}.tar.gz

BuildRequires:  gcc systemd-rpm-macros

%description
Pueue is a command-line task management tool for sequential and parallel
execution of long-running tasks.

Simply put, it's a tool that processes a queue of shell commands. On top of
that, there are a lot of convenient features and abstractions.

Since Pueue is not bound to any terminal, you can control your tasks from any
terminal on the same machine. The queue will be continuously processed, even if
you no longer have any active ssh sessions.

%prep
%autosetup

# use latest stable version from rustup
curl -Lf "https://sh.rustup.rs" | sh -s -- --profile minimal -y

%build
source ~/.cargo/env
cargo +stable build --release

# generate completions
for SHELL_NAME in bash fish zsh; do
    target/release/pueue completions $SHELL_NAME utils/
done

%check
source ~/.cargo/env
cargo +stable test

%install
# bin
install -Dpm 755 target/release/%{name} %{buildroot}%{_bindir}/%{name}
install -Dpm 755 target/release/%{name}d %{buildroot}%{_bindir}/%{name}d

# unit
install -Dpm 644 utils/%{name}d.service %{buildroot}%{_userunitdir}/%{name}d.service

# completions
install -Dpm 644 utils/%{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dpm 644 utils/%{name}.fish %{buildroot}%{_datadir}/fish/completions/%{name}.fish
install -Dpm 644 utils/_%{name} %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%{_bindir}/%{name}d
%{_userunitdir}/%{name}d.service
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/completions/%{name}.fish
%{_datadir}/zsh/site-functions/_%{name}

%changelog
* Mon Mar 10 2025 cyqsimon - 4.0.0-1
- Release 4.0.0

* Wed Jun 05 2024 cyqsimon - 3.4.1-1
- Release 3.4.1

* Tue Apr 16 2024 cyqsimon - 3.4.0-2
- Remove explicit stripping (strip enabled by default since 1.77.0)

* Fri Mar 22 2024 cyqsimon - 3.4.0-1
- Release 3.4.0

* Sat Jan 06 2024 cyqsimon - 3.3.3-1
- Release 3.3.3

* Wed Nov 29 2023 cyqsimon - 3.3.2-1
- Release 3.3.2

* Sun Oct 29 2023 cyqsimon - 3.3.1-1
- Release 3.3.1

* Sat Oct 21 2023 cyqsimon - 3.3.0-1
- Release 3.3.0

* Thu Jun 15 2023 cyqsimon - 3.2.0-1
- Release 3.2.0
- Remove completion file patch

* Mon May 15 2023 cyqsimon - 3.1.2-2
- Temporary patch for broken completion files

* Sun May 14 2023 cyqsimon - 3.1.2-1
- Release 3.1.2
