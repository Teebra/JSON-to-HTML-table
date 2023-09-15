# JSON to HTML Table - GitHub Action

![Build status](https://github.com/Teebra/JSON-to-HTML-table/actions/workflows/convert-json-to-html.yml/badge.svg)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://github.com/Teebra/JSON-to-HTML-table/blob/main/LICENSE)

This GitHub Action allows you to convert a JSON file into an HTML table with customizable styles. It's useful for visualising JSON data in a more human-readable format.
* Convert JSON to HTML Table: GitHub Action
* Convert any JSON file to HTML table
* Convert the Static Code Analysis JSON report to an HTML table.

Support the JSON format used by Veracode and transform it into a nice HTML table for simple reading.

### Action - JSON to HTML Table

```
- name: Convert JSON to HTML Table
  uses: Teebra/JSON-to-HTML-table@main
  with:
    json-file: path/to/your/jsonfile.json

```

# Usage

Follow these steps to use the "Convert JSON to HTML Table" GitHub Action in your repository:

### 1. Create or Prepare Your JSON Data

Before using the action, make sure you have the JSON data that you want to convert into an HTML table. If you don't have a JSON file, you can create one or use an existing JSON file within your repository.

### 2. Create a GitHub Workflow YAML File

In your GitHub repository, create or edit a GitHub Actions workflow YAML file (usually named .github/workflows/main.yml). This file defines the workflow that will use the action.

Here's an example of a simple workflow YAML configuration:

Example pipeline

```
name: Convert JSON to HTML Table

on:
  push:
    branches:
      - main  # Adjust this branch as needed

jobs:
  convert-json:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Code
        uses: actions/checkout@v2

      - name: Convert JSON to HTML Table
        uses: Teebra/JSON-to-HTML-table@main
        with:
          json-file: ./path/to/your/jsonfile.json  # Specify the path to your JSON file

      - name: Upload HTML Table to Artifacts
        uses: actions/upload-artifact@v3
        with:
          name: output_html 
          path: output.html # The created file's name is output.html. Name cannot be changed

```
Make sure to adjust the following:

* name: Give your workflow a meaningful name.
* on: Define the event that triggers the workflow, e.g., push to the main branch.
* json-file: Specify the path to your JSON file using the json-file input. You can adjust the path based on your repository structure.

### 3. [Optional] Upload HTML Table to Artifacts 
[Test-Artifact](https://github.com/Teebra/JSON-to-HTML-table/actions/runs/6202069993)

* This step uses the actions/upload-artifact@v3 action to upload the HTML table (output) generated in the previous step as an artifact.
* name: Names the step.
* uses: Specifies the action to use.
* with: Provides configuration for the action, including the name of the artifact (name) and the path to the HTML file path fixed to the repository.


### 4. Monitor the Workflow

Go to the "Actions" tab in your GitHub repository to monitor the progress of the workflow. You'll see the workflow running and the action converting the JSON file to an HTML table.

### 5. Access the HTML Table

Once the workflow completes successfully, you can access the generated HTML table. The action creates an HTML file with the name output.html. You can download or view this HTML file in your repository / Action Artifacts.

That's it! You've successfully used the "Convert JSON to HTML Table" GitHub Action to visualise your JSON data as an HTML table.

### Preview
* Input [JSON data](https://github.com/Teebra/JSON-to-HTML-table/tree/main/test-data)
* OutPut [HTML_Table](https://github.com/Teebra/JSON-to-HTML-table/tree/main/test-result)
![image](https://github.com/Teebra/JSON-to-HTML-table/assets/125788246/85dd110d-4e8f-4268-b71c-b4aeec6a55e8)


## 🕵🏻‍♂️ Troubleshooting

If you encounter any issues or errors while using the action, check the GitHub workflow logs for details on what went wrong. Make sure that the JSON file path specified in your workflow YAML file is correct.

If you have questions or need further assistance, you can reach out to the action's repository owner or consult GitHub's documentation on Actions for more guidance.

Happy visualizing your JSON data with this handy GitHub Action!

## 📈 Releases

You can see the list of available releases on the [GitHub Releases](https://github.com/Teebra/JSON-to-HTML-table/releases) page.

We use [`Release Drafter`](https://github.com/marketplace/actions/convert-json-to-html-table). As pull requests are merged, a draft release is kept up-to-date listing the changes, ready to publish when you’re ready. With the categories option, you can categorise pull requests in release notes using labels.

### List of labels and corresponding titles

|               **Label**               |  **Title in Releases**  |
| :-----------------------------------: | :---------------------: |
|       `enhancement`, `feature`        |       🚀 Features       |
| `bug`, `refactoring`, `bugfix`, `fix` | 🔧 Fixes & Refactoring  |
|       `build`, `ci`, `testing`        | 📦 Build System & CI/CD |
|              `breaking`               |   💥 Breaking Changes   |
|            `documentation`            |    📝 Documentation     |
|            `dependencies`             | ⬆️ Dependencies updates |

## 🛡 License
This project is licensed under the terms of the `GNU General Public License v3.0`. See [LICENSE](https://github.com/Teebra/JSON-to-HTML-table/blob/main/LICENSE)












