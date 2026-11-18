<p align="center"><img src="https://raw.githubusercontent.com/stackhands/.github/main/logo.svg" width="96" alt="stackhands logo: three stacked layers"></p>

# stackhands

Tools for building, installing and maintaining an HPC software stack with [EasyBuild](https://easybuild.io) on top of [EESSI](https://www.eessi.io), the European Environment for Scientific Software Installations.
They grew out of running a site software layer, and each one does one job that EESSI, EasyBuild or Slurm leave to the site.
The READMEs of eb-local, eb-staged-rebuild, eessi-arch-guard and eb-keep-logs open with what EESSI, EasyBuild or Slurm already cover, and what the tool adds.

| | Tool | Job | Docs |
|---|---|---|---|
| <img src="https://raw.githubusercontent.com/stackhands/eb-stack/main/docs/source/_static/mark.svg" width="40" alt=""> | [eb-stack](https://github.com/stackhands/eb-stack) | Turn conda-forge, Spack, PyPI, CRAN and Cargo recipes into easyconfigs; solve, shard and plan an EasyBuild build list | [docs](https://eb-stack.rgoswami.me/) |
| <img src="https://raw.githubusercontent.com/stackhands/eb-staged-rebuild/main/branding/logo/mark.svg" width="40" alt=""> | [eb-staged-rebuild](https://github.com/stackhands/eb-staged-rebuild) | Rebuild an installation beside the live one and swap it in, for a stack outside CernVM-FS that jobs read during the rebuild | [docs](https://stackhands.github.io/eb-staged-rebuild/) |
| <img src="https://raw.githubusercontent.com/stackhands/eessi-arch-guard/main/branding/logo/mark.svg" width="40" alt=""> | [eessi-arch-guard](https://github.com/stackhands/eessi-arch-guard) | Reload EESSI in a Slurm task that inherited a stack loaded for another CPU or GPU, as srun from a login shell does | [docs](https://stackhands.github.io/eessi-arch-guard/) |
| <img src="https://raw.githubusercontent.com/stackhands/eb-local/main/branding/logo/mark.svg" width="40" alt=""> | [eb-local](https://github.com/stackhands/eb-local) | Build on EESSI-extend inside a Slurm job's node-local disk, compile your own code with RPATH, list and uninstall per CPU target | [docs](https://stackhands.github.io/eb-local/) |
| <img src="https://raw.githubusercontent.com/stackhands/eb-keep-logs/main/branding/logo/mark.svg" width="40" alt=""> | [eb-keep-logs](https://github.com/stackhands/eb-keep-logs) | Keep a failed EasyBuild command's own output, which --tmp-logdir does not; rotate a pipeline's log tree | [docs](https://stackhands.github.io/eb-keep-logs/) |
| <img src="https://raw.githubusercontent.com/stackhands/eb-pipeline/main/branding/logo/mark.svg" width="40" alt=""> | [eb-pipeline](https://github.com/stackhands/eb-pipeline) | Drive a site's EasyBuild builds from one site file, through eb-stack, eb-staged-rebuild and eb-keep-logs | [docs](https://stackhands.github.io/eb-pipeline/) |
| <img src="https://raw.githubusercontent.com/stackhands/rfc9162/main/branding/logo/mark.svg" width="40" alt=""> | [rfc9162](https://github.com/stackhands/rfc9162) | Append-only Merkle logs hashed as RFC 9162, with tiled storage and signed checkpoints | [docs](https://stackhands.github.io/rfc9162/) |
| <img src="https://raw.githubusercontent.com/stackhands/zig-common/main/branding/logo/mark.svg" width="40" alt=""> | [zig-common](https://github.com/stackhands/zig-common) | The shared Zig library under the Zig tools: system calls, checked files, child processes | [docs](https://stackhands.github.io/zig-common/) |

## How the tools fit

The tools call each other through their command lines, so a site can adopt one without the rest.

- **A user installs and runs software.** `eb-local` builds on EESSI-extend in a Slurm job's node-local disk, one tree per CPU target. `eb-local env`, which loads those modules in a new shell or job, runs `eessi-arch-guard --shell` when the guard is installed, and `eb-local doctor` reports the target the guard selects.
- **A user submits a job.** `eessi-arch-guard --check-submit --partition NAME` asks `eb-stack stack arch` whether every loaded module, from EESSI or from the user's own EESSI-extend tree, exists for that partition's CPU target, before anything is queued. As the Slurm `TaskProlog`, the guard then reloads a stack the task inherited from a node of another type.
- **A site learns what is used.** The guard's Lmod site package can write `ModuleUsageTracking` records; `eb-keep-logs usage --active` turns them into the installed software that was loaded, which `eb-stack stack gap --site` accepts when planning the next stack.
- **A site builds and rebuilds.** `eb-pipeline` reads one site file and drives `eb-stack stack shard` and `stack admit` for planning and inode admission, `eb-staged-rebuild run` for a rebuild that jobs keep reading during, and `eb-keep-logs failed` and `rotate` for the logs. `eb-staged-rebuild run --ledger-config` records each publication with `eb-stack ledger append`, and `eb-stack ledger backfill`, `anchor` and `project` maintain that ledger, on `rfc9162`'s tiled Merkle log.

eb-stack, eb-pipeline and rfc9162 are written in Rust.
The other tools are moving from Bash and Python to Zig, each still in its own repository, on a shared Zig library for running EasyBuild, keeping private files and logs, and locked state.
Each tool is then one static binary per CPU architecture.
That matters most for eessi-arch-guard, which runs once per Slurm task: its Python prolog takes 46 ms per task where the Zig binary takes 3.5 ms (`tests/measure_noop.py`, cold, on one workstation with the archdetect stub).

Each repository has its own README and documentation site, and each release carries its binaries with checksums.
The logos, the table above and the cross-links in every README and site come from [`branding/`](https://github.com/stackhands/.github/tree/main/branding).
