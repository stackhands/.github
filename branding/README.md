# stackhands branding

One source for the logos and the cross-links between the stackhands tools.

- `ecosystem.json`: every tool, its repository, its documentation site and its job.
- `logos.py`: the tool logos, one family in the style of the eb-stack mark: a mark on a tile, light and dark wordmarks, a favicon.
- `sync.py NAME CHECKOUT [--static DIR]`: writes a tool's logos to `branding/logo/` (and `DIR`), the table of tools between the `stackhands:begin`/`end` markers in its README and docs pages, and the "stackhands" navbar entry in its Sphinx `conf.py`.
- `scaffold_docs.py NAME CHECKOUT`: a small Shibuya site for a tool whose README is its manual, with a GitHub Pages workflow.

After a change to `ecosystem.json` or `logos.py`, run `sync.py` in each checkout and commit there.
