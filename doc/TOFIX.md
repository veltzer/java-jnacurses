# TOFIX

Findings from a code scan on 2026-10-04.

## High

- `README.md:3` - the README (and `config/project.lua:3`) describe "a curses implementation for Java" with a "Java side" that talks to ncurses through JNA, but the repo contains no Java code and never did (`git log --all` has no `*.java`); only the C shim `jnacurses.c` exists. Either add the Java JNA bindings (interface mapping `libjnacurses.so` + `ncurses`, a build such as Maven/Gradle, and a small demo) or rewrite the README/description to say this is only the C shim for a JNA binding.

## Medium

- `pyproject.toml:10` - `pytest` is declared in the dev group but the repo has no tests and no pytest processor in `rsconstruct.toml`; drop it from the dev group (and `uv lock`), or add tests for the shim.
- `rsconstruct.toml:1` - `config/project.lua` is not linted: there is no `.luacheckrc` and no `[processor.luacheck]`. Add the fleet `.luacheckrc` and `[processor.luacheck]` with `src_dirs = ["config"]`.

## Low

- `rsconstruct.toml:11` - two blank lines between `[processor.ruff]` and `[processor.mypy]`; the rest of the file uses one.
- `scripts/build_lib.py:3` - the docstring and `rsconstruct.toml:21` still describe the build in terms of the removed Makefile; reword to describe the command itself now that the Makefile is gone.
