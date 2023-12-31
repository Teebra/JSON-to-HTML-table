import json
from json2table import convert
import os

def main():
    # Retrieve the JSON file path from the environment variable
    json_file = os.getenv('INPUT_JSON-FILE')

    # Check if the provided JSON file path is relative or absolute
    if not os.path.isabs(json_file):
        # If it's relative, make it absolute by joining with the workspace directory
        workspace = os.getenv('GITHUB_WORKSPACE', '')
        json_file = os.path.join(workspace, json_file)

    try:
        # Load the JSON data from the specified file
        with open(json_file, 'r') as f:
            json_data = json.load(f)
    except FileNotFoundError:
        print(f"JSON file '{json_file}' not found.")
        exit(1)
    except json.JSONDecodeError:
        print(f"Error decoding JSON in file '{json_file}'.")
        exit(1)

    # Convert the JSON data to an HTML table with added styles
    table_attributes = {
        "style": "width:100%; height:100%; border-collapse: collapse; font-family: Consolas,Monaco,Lucida Console,Liberation Mono,DejaVu Sans Mono,Bitstream Vera Sans Mono,Courier New,monospace; background-color: #f6f8fa; float: left"
    }
    html_table = convert(json_data, build_direction="LEFT_TO_RIGHT", table_attributes=table_attributes)

    # Add a border around each title row
    html_table = html_table.replace("<th>", "<th style=\"border: 0.1px solid black;\">")
    html_table = html_table.replace("<tr>", "<tr style=\"border: 0.1px solid black;\">")
    html_table = html_table.replace("<td>", "<td style=\"border: 0.1px solid black;\">")

    # Print the HTML table to the output file
    with open('output.html', 'w') as f:
        f.write(html_table)

if __name__ == '__main__':
    main()
