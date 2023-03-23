import { useState } from 'react'
import { Col, Container, Row } from 'react-bootstrap'
import UploadContour from './UploadContour'
import UploadImg from './UploadImg'
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select, { SelectChangeEvent } from '@mui/material/Select';
import Slider from '@mui/material/Slider';
import './ForthTab.css'


const ForthTab = () => {

    const [options, setOptions] = useState<string>('');
    const [minRadius, setMinRadius] = useState<number>(25)
    const [maxRadius, setMaxRadius] = useState<number>(40)
    const [threshold, setThreshold] = useState<number>(10)


    const handleChangeOptions = (event: SelectChangeEvent) => {
        setOptions(event.target.value);
    };

    return (
        <Container fluid>
            <Row>
                <Col style={{ height: "85vh", display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center" }} lg={4} md={6} sm={12} xs={12}>
                    <UploadContour />
                    <div className='output-container'>
                        <label className='output-label uploadimg' >Contour Output</label>
                        <div className='output-img-contain'>
                            <img className='output-img' alt="" />
                        </div>
                    </div>
                </Col>
                <Col style={{ height: "85vh", display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center" }} lg={4} md={6} sm={12} xs={12}>
                    <UploadImg />
                    <FormControl style={{ marginBottom: "2rem", width: "13rem" }} variant="standard" sx={{ m: 1, minWidth: 150 }}>
                        <InputLabel id="demo-simple-select-autowidth-label">Choose edge detectors</InputLabel>
                        <Select
                            labelId="demo-simple-select-autowidth-label"
                            id="demo-simple-select-autowidth"
                            value={options}
                            onChange={handleChangeOptions}
                            autoWidth
                        >
                            <MenuItem value="0">
                                <em>None</em>
                            </MenuItem>
                            <MenuItem value="1">Lines</MenuItem>
                            <MenuItem value="2">Circles</MenuItem>
                            <MenuItem value="3">Ellipse</MenuItem>
                        </Select>
                    </FormControl>
                </Col>
                <Col style={{ height: "85vh", display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center" }} lg={4} md={12} sm={12} xs={12}>
                    <div className='output-container'>
                        <label className='output-label uploadimg' >
                            {
                                options === "1" ?
                                "Lines output "
                                : options === "2" ? 
                                "Circles Output"
                                : options === "3" ?
                                "Ellipse Output"
                                : "Output"
                            }
                            </label>
                        <div className='output-img-contain'>
                            <img className='output-img' alt="" />
                        </div>
                    </div>
                    {
                        options === "2" ?
                            <div className='btn-slider-contain forthtab'>
                                <div className='sliders-contain'>
                                    <label htmlFor="">Min Radius</label>
                                    <Slider value={minRadius} onChange={(e: any) => setMinRadius(e.target.value)} min={0} max={100} step={1} style={{ width: "13rem" }} aria-label="Default" valueLabelDisplay="auto" />
                                </div>
                                <div className='sliders-contain'>
                                    <label htmlFor="">Max Radius</label>
                                    <Slider value={maxRadius} onChange={(e: any) => setMaxRadius(e.target.value)} min={0} max={100} step={1} style={{ width: "13rem" }} aria-label="Default" valueLabelDisplay="auto" />
                                </div>
                                <div className='sliders-contain'>
                                    <label htmlFor="">Threshold</label>
                                    <Slider value={threshold} onChange={(e: any) => setThreshold(e.target.value)} min={0} max={100} step={1} style={{ width: "13rem" }} aria-label="Default" valueLabelDisplay="auto" />
                                </div>
                                <button className='apply-btn'>Apply</button>
                            </div>
                            : null
                    }
                </Col>
            </Row>
        </Container>
    )
}

export default ForthTab