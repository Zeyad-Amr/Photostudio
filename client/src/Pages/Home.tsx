import { Container } from 'react-bootstrap';
import { Col } from 'react-bootstrap';
import { Row } from 'react-bootstrap';
import Inputimg from '../Components/inputImg/Inputimg';
import Output from '../Components/output/Output';
import Tabs from '../Components/tabs/Tabs';

const Home = () => {
    return (
        <Container fluid>
            <Row>
                <Col lg={4} md={6} sm={6} xs={12} style={{ display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center", height: "100vh" }} >
                    <Inputimg />
                </Col>
                <Col lg={4} md={6} sm={6} xs={12} style={{ display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center", height: "100vh" }}>
                    <Tabs />
                </Col>
                <Col lg={4} md={6} sm={6} xs={12} style={{ display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center", height: "100vh" }}>
                    <Output />
                </Col>
            </Row>
        </Container>
    )
}

export default Home