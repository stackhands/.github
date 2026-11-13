<p align="center"><img src="https://raw.githubusercontent.com/stackhands/.github/main/logo.svg" width="96" alt="stackhands logo: three stacked layers"></p>

# stackhands

Tools for building, installing and maintaining an HPC software stack with [EasyBuild](https://easybuild.io) on top of [EESSI](https://www.eessi.io), the European Environment for Scientific Software Installations.
They come from running the site layer of a national supercomputer, and each one does one job.

| Tool | Job |
|---|---|
| [eb-stack](https://github.com/stackhands/eb-stack) | Solve, shard and plan a build list; admit builds under a scratch inode budget |
| [eb-staged-rebuild](https://github.com/stackhands/eb-staged-rebuild) | Rebuild into a fresh directory and swap module files atomically; retire modules |
| [eb-local](https://github.com/stackhands/eb-local) | Install software with EasyBuild on top of EESSI into a directory a user or project owns |
| [eessi-arch-guard](https://github.com/stackhands/eessi-arch-guard) | Reload EESSI in a Slurm step that inherited it for another CPU or GPU |
| [eb-keep-logs](https://github.com/stackhands/eb-keep-logs) | Keep a failed build's EasyBuild log and command output; rotate a pipeline's log tree |
| [rfc9162](https://github.com/stackhands/rfc9162) | An append-only Merkle log hashed as RFC 9162, with tiled storage and signed checkpoints, for build logs and records that can be checked later |

eb-stack and rfc9162 are written in Rust.
The other tools are moving from Bash and Python to Zig, each still in its own repository, on a shared Zig library for running EasyBuild, keeping private files and logs, and locked state.
Each tool is then one static binary per CPU architecture.

Each repository has its own README with installation and usage, and an EasyBuild recipe installs each tool as a module.
