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
