<p align="center"><img src="https://raw.githubusercontent.com/stackhands/.github/main/logo.svg" width="96" alt="stackhands logo: three stacked layers"></p>

# stackhands

Tools for building, installing and maintaining an HPC software stack with [EasyBuild](https://easybuild.io) on top of [EESSI](https://www.eessi.io), the European Environment for Scientific Software Installations.
They grew out of running a site software layer, and each one does one job.

| | Tool | Job | Docs |
|---|---|---|---|
| <img src="https://raw.githubusercontent.com/stackhands/eb-stack/main/docs/source/_static/mark.svg" width="40" alt=""> | [eb-stack](https://github.com/stackhands/eb-stack) | Solve, shard and plan an EasyBuild build list; admit builds under a scratch inode budget | [docs](https://eb-stack.rgoswami.me/) |
| <img src="https://raw.githubusercontent.com/stackhands/eb-staged-rebuild/main/branding/logo/mark.svg" width="40" alt=""> | [eb-staged-rebuild](https://github.com/stackhands/eb-staged-rebuild) | Rebuild an installation in a staged tree and swap it in, so running jobs keep their paths | [docs](https://stackhands.github.io/eb-staged-rebuild/) |
| <img src="https://raw.githubusercontent.com/stackhands/eessi-arch-guard/main/branding/logo/mark.svg" width="40" alt=""> | [eessi-arch-guard](https://github.com/stackhands/eessi-arch-guard) | Reload EESSI in a Slurm task that inherited it for another CPU or GPU | [docs](https://stackhands.github.io/eessi-arch-guard/) |
| <img src="https://raw.githubusercontent.com/stackhands/eb-local/main/branding/logo/mark.svg" width="40" alt=""> | [eb-local](https://github.com/stackhands/eb-local) | Install software with EasyBuild on top of EESSI into a directory a user or project owns | [docs](https://stackhands.github.io/eb-local/) |
| <img src="https://raw.githubusercontent.com/stackhands/eb-keep-logs/main/branding/logo/mark.svg" width="40" alt=""> | [eb-keep-logs](https://github.com/stackhands/eb-keep-logs) | Keep a failed build's EasyBuild log and command output; rotate a pipeline's log tree | [docs](https://stackhands.github.io/eb-keep-logs/) |
| <img src="https://raw.githubusercontent.com/stackhands/rfc9162/main/branding/logo/mark.svg" width="40" alt=""> | [rfc9162](https://github.com/stackhands/rfc9162) | Append-only Merkle logs hashed as RFC 9162, with tiled storage and signed checkpoints | [docs](https://stackhands.github.io/rfc9162/) |
| <img src="https://raw.githubusercontent.com/stackhands/zig-common/main/branding/logo/mark.svg" width="40" alt=""> | [zig-common](https://github.com/stackhands/zig-common) | The shared Zig library under the Zig tools: system calls, checked files, child processes | [docs](https://stackhands.github.io/zig-common/) |

eb-stack and rfc9162 are written in Rust.
The other tools are moving from Bash and Python to Zig, each still in its own repository, on a shared Zig library for running EasyBuild, keeping private files and logs, and locked state.
Each tool is then one static binary per CPU architecture.

Each repository has its own README and documentation site, and an EasyBuild recipe installs each tool as a module.
The logos, the table above and the cross-links in every README and site come from [`branding/`](https://github.com/stackhands/.github/tree/main/branding).
