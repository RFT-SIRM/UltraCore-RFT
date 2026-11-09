# Interactive portal source bundle

`index.html.gz` is the compressed, self-contained static HTML/CSS/JavaScript bundle deployed to `/interactive/`. It is kept outside `docs/` so MkDocs does not create a competing page at that route.

To inspect or edit the page:

```sh
gzip -dc portal-src/index.html.gz > /tmp/ultracore-portal.html
# edit /tmp/ultracore-portal.html
gzip -n -9 -c /tmp/ultracore-portal.html > portal-src/index.html.gz
```

The Pages workflow expands the bundle into `site/interactive/index.html` after the strict MkDocs build.
