# JSON-to-HTML-table

 Convert the Static Code Analysis JSON report to an HTML table.

Support Veracode's JSON format and convert it to a nice HTML table for easy readability.

### Action
```
- name: Convert JSON to HTML Table
  uses: Teebra/JSON-to-HTML-table@main
  with:
    json-file: path/to/your/jsonfile.json

```



Example pipeline

```
name: My Workflow

on:
  push:
    branches:
      - main

jobs:
  convert-json-to-html:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Convert JSON to HTML Table
        uses: Teebra/JSON-to-HTML-table@main
        with:
          json-file: result.json

      - name: Upload HTML Table to Artifacts
        uses: actions/upload-artifact@v3
        with:
          name: output_html
          path: output.html

```
