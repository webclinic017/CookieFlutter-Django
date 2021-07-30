// @flow
import React, { useState } from 'react';
import { Row, Col, Card, Toast, ToastContainer, Form } from 'react-bootstrap';

// components
import PageTitle from '../../components/PageTitle';

import logo from '../../assets/images/logo_sm_dark.png';

const DefaultToasts = () => {
    const [show, setShow] = useState(true);
    const [showTranslucent, setShowTranslucent] = useState(true);
    const [showPlacement, setShowPlacement] = useState(true);
    const [position, setPosition] = useState('top-start');

    const [stacked, setStacked] = useState([
        {
            time: 'just now',
            desc: 'See? Just like this.',
        },
        {
            time: '2 seconds ago',
            desc: 'Heads up, toasts will stack automatically',
        },
    ]);

    const positions = [
        'top-start',
        'top-center',
        'top-end',
        'middle-start',
        'middle-center',
        'middle-end',
        'bottom-start',
        'bottom-center',
        'bottom-end',
    ];

    /*
     * handle close
     */
    const handleClose = (index) => {
        const list = [...stacked];
        list.splice(index, 1);
        setStacked(list);
    };

    return (
        <Card>
            <Card.Body>
                <h4 className="header-title">Bootstrap Toasts</h4>
                <p className="text-muted font-14">
                    Push notifications to your visitors with a toast, a lightweight and easily customizable alert
                    message.
                </p>

                <Row>
                    <Col md={6}>
                        <h5 className="mb-2">Basic</h5>
                        <p className="text-muted font-14">
                            Toasts are as flexible as you need and have very little required markup. At a minimum, we
                            require a single element to contain your “toasted” content and strongly encourage a dismiss
                            button.
                        </p>
                        <div className="p-3">
                            <Toast onClose={() => setShow(false)} show={show}>
                                <Toast.Header>
                                    <img src={logo} alt="brand-logo" height="12" className="me-1" />
                                    <strong className="me-auto">{% raw %}{{cookiecutter.project_name}}{% endraw %}</strong>
                                    <small className="ms-5">11 mins ago</small>
                                </Toast.Header>
                                <Toast.Body>Hello, world! This is a toast message.</Toast.Body>
                            </Toast>
                        </div>
                    </Col>

                    <Col md={6}>
                        <h5 className="mb-2">Translucent</h5>
                        <p className="text-muted font-14">
                            Toasts are slightly translucent, too, so they blend over whatever they might appear over.
                            For browsers that support the backdrop-filter CSS property, we’ll also attempt to blur the
                            elements under a toast.
                        </p>

                        <div className="p-3 bg-light">
                            <Toast onClose={() => setShowTranslucent(false)} show={showTranslucent}>
                                <Toast.Header>
                                    <img src={logo} alt="brand-logo" height="12" className="me-1" />
                                    <strong className="me-auto">{% raw %}{{cookiecutter.project_name}}{% endraw %}</strong>
                                    <small className="ms-5">11 mins ago</small>
                                </Toast.Header>
                                <Toast.Body>Hello, world! This is a toast message.</Toast.Body>
                            </Toast>
                        </div>
                    </Col>
                </Row>

                {/* stacked */}
                <Row>
                    <Col md={6} className="mt-4">
                        <h5 className="mb-2">Stacking</h5>
                        <p className="text-muted font-14">
                            When you have multiple toasts, we default to vertiaclly stacking them in a readable manner.
                        </p>
                        <div className="p-3">
                            <div
                                aria-live="polite"
                                aria-atomic="true"
                                style={% raw %}{{ position: 'relative', minHeight: '200px' }}>{% endraw %}
                                <div className="toast-container" style={% raw %}{{ position: 'absolute', top: 0, right: 0 }}>{% endraw %}
                                    {stacked.map((item, index) => {
                                        return (
                                            <Toast key={index} onClose={() => handleClose(index)}>
                                                <Toast.Header>
                                                    <img src={logo} alt="brand-logo" height="12" className="me-1" />
                                                    <strong className="me-auto">{% raw %}{{cookiecutter.project_name}}{% endraw %}</strong>
                                                    <small className="ms-5">{item.time}</small>
                                                </Toast.Header>
                                                <Toast.Body>{item.desc}</Toast.Body>
                                            </Toast>
                                        );
                                    })}
                                </div>
                            </div>
                        </div>
                    </Col>

                    <Col md={6} className="mt-4">
                        <h5 className="mb-2">Placement</h5>
                        <p className="text-muted font-14">
                            Place toasts with custom CSS as you need them. The top right is often used for
                            notifications, as is the top middle. If you’re only ever going to show one toast at a time,
                            put the positioning styles right on the <code>.toast</code>.
                        </p>

                        <div className="p-3">
                            <div
                                aria-live="polite"
                                aria-atomic="true"
                                className="d-flex justify-content-center align-items-center"
                                style={% raw %}{{ minHeight: '200px' }}>{% endraw %}
                                <Toast onClose={() => setShowPlacement(false)} show={showPlacement}>
                                    <Toast.Header>
                                        <img src={logo} alt="brand-logo" height="12" className="me-1" />
                                        <strong className="me-auto">{% raw %}{{cookiecutter.project_name}}{% endraw %}</strong>
                                        <small className="ms-5">1 mins ago</small>
                                    </Toast.Header>
                                    <Toast.Body>Heads up, toasts will stack automatically</Toast.Body>
                                </Toast>
                            </div>
                        </div>
                    </Col>
                </Row>

                <Row>
                    <Col md={6}>
                        <Card>
                            <Card.Body>
                                <h4 className="header-title">Placement</h4>
                                <p className="text-muted font-14">
                                    Place toasts with custom CSS as you need them. The top right is often used for
                                    notifications, as is the top middle. If you’re only ever going to show one toast at
                                    a time, put the positioning styles right on the
                                    <code>.toast</code>.
                                </p>
                                <div className="mb-3">
                                    <label htmlFor="selectToastPlacement">Toast placement</label>
                                    <Form.Select
                                        id="selectToastPlacement"
                                        className="mt-2"
                                        onChange={(e) => setPosition(e.currentTarget.value)}>
                                        {positions.map((p) => (
                                            <option key={p} value={p}>
                                                {p}
                                            </option>
                                        ))}
                                    </Form.Select>
                                </div>

                                <div
                                    aria-live="polite"
                                    aria-atomic="true"
                                    className="bg-light position-relative"
                                    style={% raw %}{{ minHeight: '294px' }}>{% endraw %}
                                    <ToastContainer className="p-3" position={position}>
                                        <Toast>
                                            <Toast.Header closeButton={false}>
                                                <img src={logo} className="me-1" alt="" height="12" />
                                                <strong className="me-auto">{% raw %}{{cookiecutter.project_name}}{% endraw %}</strong>
                                                <small>11 mins ago</small>
                                            </Toast.Header>
                                            <Toast.Body>Hello, world! This is a toast message.</Toast.Body>
                                        </Toast>
                                    </ToastContainer>
                                </div>
                            </Card.Body>
                        </Card>
                    </Col>
                </Row>
            </Card.Body>
        </Card>
    );
};

const Notifications = (): React$Element<React$FragmentType> => {
    return (
        <React.Fragment>
            <PageTitle
                breadCrumbItems={[
                    { label: 'Base UI', path: '/ui/toasts' },
                    { label: 'Notifications', path: '/ui/notifications', active: true },
                ]}
                title={'Notifications'}
            />

            {/* toast */}
            <Row>
                <Col>
                    <DefaultToasts />
                </Col>
            </Row>
        </React.Fragment>
    );
};

export default Notifications;
