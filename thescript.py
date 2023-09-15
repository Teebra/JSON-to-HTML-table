import json
from json2table import convert

def main():
    # Load the JSON data
    json_data = json.load(open('results.json'))

    # Convert the JSON data to an HTML table with added styles
    table_attributes = {
        "style": "width:100%; height:100%; border-collapse: collapse; font-family: Consolas,Monaco,Lucida Console,Liberation Mono,DejaVu Sans Mono,Bitstream Vera Sans Mono,Courier New,monospace; background-color: #E8E8E8; float: left"
    }
    html_table = convert(json_data, build_direction="LEFT_TO_RIGHT", table_attributes=table_attributes)

    # Add a border around each title row
    html_table = html_table.replace("<th>", "<th style=\"border: 0.1px solid black;\">")
    html_table = html_table.replace("<tr>", "<tr style=\"border: 0.1px solid black;\">")
    html_table = html_table.replace("<td>", "<td style=\"border: 0.1px solid black;\">")

    # Print the HTML table
    with open('test.html', 'w') as f:
        f.write(html_table)

if __name__ == '__main__':
    main()

# border-collapse: collapse  padding: 10px; margin: 5px; font-size:16px
