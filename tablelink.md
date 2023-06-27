Can i have a python script to convert the ID to a link

Use parse arges

Pass the input and output files in as paramters

Extra columns may be added in future bit ID will always be first column


| ID    | Work Item Type | Title 1                                | Title 2                                                      | Title 3                                                                                                                                 |
| ----- | -------------- | -------------------------------------- | ------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------- |
| 85391 | Epic           | Implement VTN element of the DSRSP     |
| 85174 | Feature        |                                        |  OpenADR VTN foundations                                     |
| 85204 | User Story     |                                        |                                                              | Review and amend  OpenLeadr Security implementation               |

will become

| ID    | Work Item Type | Title 1                                | Title 2                                                      | Title 3                                                                                                                                 |
| ----- | -------------- | -------------------------------------- | ------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------- |
| [85391](https://global.tfs.landisgyr.net/tfs/BG%20Meter%20Development/E470/_workitems/edit/85391) | Epic           | Implement VTN element of the DSRSP     |
| [85174](https://global.tfs.landisgyr.net/tfs/BG%20Meter%20Development/E470/_workitems/edit/85174) | Feature        |                                        |  OpenADR VTN foundations                                     |
| [85204](https://global.tfs.landisgyr.net/tfs/BG%20Meter%20Development/E470/_workitems/edit/85204) | User Story     |                                        |                                                              | Review and amend  OpenLeadr Security implementation               |


```python
import argparse

def convert_id_to_link(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if '|' in line:
            columns = line.split('|')
            if len(columns) > 1 and columns[1].strip().isdigit():
                work_item_id = columns[1].strip()
                url = f"https://global.tfs.landisgyr.net/tfs/BG%20Meter%20Development/E470/_workitems/edit/{work_item_id}"
                columns[1] = f"[{work_item_id}]({url})"
                lines[i] = '|'.join(columns)

    with open(output_file, 'w') as f:
        f.writelines(lines)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert ID in a markdown table to a link')
    parser.add_argument('input_file', help='Path to the input markdown file')
    parser.add_argument('output_file', help='Path to the output markdown file')
    args = parser.parse_args()

    convert_id_to_link(args.input_file, args.output_file)
```
