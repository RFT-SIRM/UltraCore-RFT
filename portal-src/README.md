# Interactive portal source bundle

`index.html.gz` is the compressed, self-contained static HTML/CSS/JavaScript research-explorer bundle deployed to `/interactive/`.

The **Core Development** section is maintained separately in [`core-development.html`](core-development.html). The Pages workflow injects this readable fragment into the decompressed portal HTML immediately before `</body>`. This keeps the interactive explorer bundle untouched while making the portfolio content easy to review and update.

To inspect or edit the original interactive explorer bundle:

```sh
gzip -dc portal-src/index.html.gz > /tmp/ultracore-portal.html
# edit /tmp/ultracore-portal.html
gzip -n -9 -c /tmp/ultracore-portal.html > portal-src/index.html.gz
```

To edit the Core Development section, change [`core-development.html`](core-development.html). The injection helper is [`scripts/inject_core_portfolio.py`](../scripts/inject_core_portfolio.py); it checks that the portfolio is inserted once and remains inside the HTML body.

The Pages workflow expands the explorer bundle into `site/interactive/index.html`, injects the portfolio fragment, verifies the existing explorer controls plus all four core project references, and only then publishes the artifact to `gh-pages`.
