// @flow
import React, { useState } from 'react';
import { Row, Col } from 'react-bootstrap';

// components
import PageTitle from '../../../components/PageTitle';

import ChatUsers from './ChatUsers';
import ChatArea from './ChatArea';
import ChatProfile from './ChatProfile';

// dummy data
import { users } from './data';

// ChatApp
const ChatApp = (): React$Element<React$FragmentType> => {
    const [selectedUser, setSelectedUser] = useState(users[1]);

    /**
     * On user change
     */
    const onUserChange = (user) => {
        setSelectedUser(user);
    };

    return (
        <>
            <PageTitle
                breadCrumbItems={[
                    { label: 'Apps', path: '/apps/chat' },
                    { label: 'Chat', path: '/apps/chat', active: true },
                ]}
                title={'Chat'}
            />

            <Row>
                <Col xxl={3} xl={% raw %}{{ span: 6, order: 1 }}{% endraw %}>
                    <ChatUsers onUserSelect={onUserChange} />
                </Col>

                <Col xxl={6} xl={% raw %}{{ span: 12, order: 2 }}{% endraw %}>
                    <ChatArea selectedUser={selectedUser} />
                </Col>

                <Col xxl={% raw %}{{ span: 3, order: 2 }}{% endraw %} xl={% raw %}{{ span: 6, order: 1 }}{% endraw %}>
                    <ChatProfile selectedUser={selectedUser} />
                </Col>
            </Row>
        </>
    );
};

export default ChatApp;
