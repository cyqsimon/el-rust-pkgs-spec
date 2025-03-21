## el-rust-pkgs-spec

This repository hosts `spec` files for building selected Rust packages
that are not included in major repos (default, EPEL, RPMFusion, etc.)
for Enterprise Linux (RHEL, Rocky, etc.).

You can install the built packages from [COPR](https://copr.fedorainfracloud.org/coprs/cyqsimon/el-rust-pkgs).

### Packages

<table>
    <tr>
        <td align="center"><a href="https://github.com/ellie/atuin">atuin</a></td>
        <td align="center"><a href="https://github.com/imsnif/bandwhich">bandwhich</a></td>
        <td align="center"><a href="https://github.com/rutrum/ccase">ccase</a></td>
        <td align="center"><a href="https://github.com/hisbaan/didyoumean">didyoumean</a></td>
        <td align="center"><a href="https://github.com/sharkdp/diskus">diskus</a></td>
    </tr>
    <tr>
        <td align="center">
            <a href="https://github.com/ogham/dog">dog</a>
            <span>(</span>
            <a href="https://github.com/cyqsimon/dog/releases/tag/v0.1.0-patched">patched</a>
            <span>)</span>
        </td>
        <td align="center"><a href="https://github.com/Canop/dysk">dysk</a></td>
        <td align="center"><a href="https://github.com/evcxr/evcxr">evcxr-repl</a></td>
        <td align="center"><a href="https://github.com/eza-community/eza">eza</a></td>
        <td align="center"><a href="https://github.com/printfn/fend">fend</a></td>
    </tr>
    <tr>
        <td align="center"><a href="https://git.sr.ht/~mzhang/garbage">garbage</a></td>
        <td align="center"><a href="https://github.com/sstadick/hck">hck</a></td>
        <td align="center"><a href="https://github.com/thecoshman/http">httplz</a></td>
        <td align="center"><a href="https://github.com/svenstaro/miniserve">miniserve</a></td>
        <td align="center"><a href="https://github.com/pvolok/mprocs">mprocs</a></td>
    </tr>
    <tr>
        <td align="center"><a href="https://github.com/ouch-org/ouch">ouch</a></td>
        <td align="center"><a href="https://github.com/k9withabone/podlet">podlet</a></td>
        <td align="center"><a href="https://github.com/Nukesor/pueue">pueue</a></td>
        <td align="center"><a href="https://github.com/RustScan/RustScan">rustscan</a></td>
        <td align="center"><a href="https://github.com/chmln/sd">sd</a></td>
    </tr>
    <tr>
        <td align="center"><a href="https://github.com/dbrgn/tealdeer">tealdeer</a></td>
        <td align="center"><a href="https://github.com/ducaale/xh">xh</a></td>
        <td align="center">More to come</td>
        <td align="center"></td>
        <td align="center"></td>
    </tr>
    <tr>
        <td align="center"><img width=200/></td>
        <td align="center"><img width=200/></td>
        <td align="center"><img width=200/></td>
        <td align="center"><img width=200/></td>
        <td align="center"><img width=200/></td>
    </tr>
</table>

### Package requests

If you want to have a package added to this list, feel free
to submit an issue or a PR.

**The package should be reasonably-popular and/or obviously-useful.**

### Removal & reinstatement history

- 2023-07-05: Removed [lfs](https://github.com/Canop/lfs): renamed to `dysk`
- 2023-09-10: Removed [exa](https://github.com/ogham/exa): deprecated by [eza](https://github.com/eza-community/eza)
- 2024-08-23: Removed [fd](https://github.com/sharkdp/fd): packaged by EPEL as `fd-find`
- 2024-08-23: Removed [ripgrep](https://github.com/BurntSushi/ripgrep): packaged in EPEL as `ripgrep`
- 2024-09-13: Removed [eza](https://github.com/eza-community/eza): packaged in EPEL as `eza`
- 2024-09-14: Removed [bat](https://github.com/sharkdp/bat): packaged in EPEL as `bat`
- 2024-09-14: Removed [git-delta](https://github.com/dandavison/delta): packaged in EPEL as `git-delta`
- 2024-09-14: Removed [procs](https://github.com/dalance/procs): packaged in EPEL as `procs`
- 2024-09-15: Removed [tokei](https://github.com/XAMPPRocky/tokei): packaged in EPEL as `tokei`
- 2025-01-11: Reinstated [eza](https://github.com/eza-community/eza): dropped by EPEL
