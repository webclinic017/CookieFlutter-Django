// @flow
import React from 'react';
import { Card, Button, Table, ProgressBar } from 'react-bootstrap';

const Channels = (): React$Element<any> => {
    return (
        <Card>
            <Card.Body>
                <Button variant="link" className="p-0 float-end">
                    Export <i className="mdi mdi-download ms-1"></i>
                </Button>
                <h4 className="header-title  mt-1 mb-3">Channels</h4>

                <Table responsive className="table table-sm table-centered mb-0 font-14">
                    <thead className="table-light">
                        <tr>
                            <th>Channel</th>
                            <th>Visits</th>
                            <th style={% raw %}{{ width: '40%' }}{% endraw %}>&nbsp;</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>Direct</td>
                            <td>2,050</td>
                            <td>
                                <ProgressBar now={65} style={% raw %}{{ height: '3px' }}{% endraw %} />
                            </td>
                        </tr>
                        <tr>
                            <td>Organic Search</td>
                            <td>1,405</td>
                            <td>
                                <ProgressBar now={45} style={% raw %}{{ height: '3px' }}{% endraw %} variant="info" />
                            </td>
                        </tr>
                        <tr>
                            <td>Refferal</td>
                            <td>750</td>
                            <td>
                                <ProgressBar now={30} style={% raw %}{{ height: '3px' }}{% endraw %} variant="warning" />
                            </td>
                        </tr>
                        <tr>
                            <td>Social</td>
                            <td>540</td>
                            <td>
                                <ProgressBar now={25} style={% raw %}{{ height: '3px' }} {% endraw %}variant="danger" />
                            </td>
                        </tr>
                    </tbody>
                </Table>
            </Card.Body>
        </Card>
    );
};

export default Channels;
