import json
from json2table import convert
import sys

def main():
    if len(sys.argv) < 2:
        print("Please provide the path to the JSON file as a command-line argument.")
        sys.exit(1)

    json_file = sys.argv[1]

    try:
        # Load the JSON data from the specified file
        with open(json_file, 'r') as f:
            json_data = json.load(f)
    except FileNotFoundError:
        print(f"JSON file '{json_file}' not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error decoding JSON in file '{json_file}'.")
        sys.exit(1)

    # Convert the JSON data to an HTML table with added styles
    table_attributes = {
        "style": "width:100%; height:100%; border-collapse: collapse; font-family: Consolas,Monaco,Lucida Console,Liberation Mono,DejaVu Sans Mono,Bitstream Vera Sans Mono,Courier New,monospace; background-color: #E8E8E8; float: left"
    }
    html_table = convert(json_data, build_direction="LEFT_TO_RIGHT", table_attributes=table_attributes)

    # Add a border around each title row
    html_table = html_table.replace("<th>", "<th style=\"border: 0.1px solid black;\">")
    html_table = html_table.replace("<tr>", "<tr style=\"border: 0.1px solid black;\">")
    html_table = html_table.replace("<td>", "<td style=\"border: 0.1px solid black;\">")

    # Output file name based on the input JSON file name
    output_file = json_file.replace('.json', '.html')

    # Print the HTML table to the output file
    with open(output_file, 'w') as f:
        f.write(html_table)

if __name__ == '__main__':
    main()
