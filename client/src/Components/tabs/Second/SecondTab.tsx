import { Container } from 'react-bootstrap';
import { Col } from 'react-bootstrap';
import { Row } from 'react-bootstrap';
import Inputimg from '../../inputImg/Inputimg';
import { useState, useEffect, useContext } from 'react';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select, { SelectChangeEvent } from '@mui/material/Select';
import Slider from '@mui/material/Slider';
import './SecondTab.css'
import { FileContext } from '../../contexts/fileContext'
import axios from '../../global/API/axios';


const SecondTab = () => {

    const {
        sliderC,
        setSliderC,
        sliderBlock,
        setSliderBlock,
        sliderGlobal,
        setSliderGlobal
    } = useContext(FileContext);

    const [secondTabOptions, setSecondTabOptions] = useState<string>('');

    // integration with Back
    // useEffect(() => {
    //     axios.post('',
    //         secondTabOptions
    //     ).then((response: any) => {
    //         console.log(response)
    //     }).catch((err: any) => {
    //         console.log(err)
    //     })
    // }, [secondTabOptions])


    const handleChange = (event: SelectChangeEvent) => {
        setSecondTabOptions(event.target.value);
    };

    const handleGlobalButton = () => {
        // axios.post('',
        //     sliderGlobal
        // ).then((response: any) => {
        //     console.log(response)
        // }).catch((err: any) => {
        //     console.log(err)
        // })
    }

    const handleLocalButton = () => {
        // axios.post('',{
        //     sliderBlock,sliderC
        // }).then((response: any) => {
        //     console.log(response)
        // }).catch((err: any) => {
        //     console.log(err)
        // })
    }

    console.log(secondTabOptions)

    return (
        <Container fluid>
            <Row>
                <Col style={{ height: "85vh" }} lg={3} md={3} sm={12} xs={12}>
                    <div>
                        <Inputimg />
                    </div>
                    <div>
                        <FormControl style={{ marginTop: "1rem", marginBottom: "1rem", marginLeft: "2.5rem" }} variant="standard" sx={{ m: 1, minWidth: 150 }}>
                            <InputLabel id="demo-simple-select-autowidth-label">Choose</InputLabel>
                            <Select
                                labelId="demo-simple-select-autowidth-label"
                                id="demo-simple-select-autowidth"
                                value={secondTabOptions}
                                onChange={handleChange}
                                autoWidth
                            >
                                <MenuItem value="0">
                                    <em>None</em>
                                </MenuItem>
                                <MenuItem value="1">Equalize</MenuItem>
                                <MenuItem value="2">Normalize</MenuItem>
                                <MenuItem value="3">Local thresholding</MenuItem>
                                <MenuItem value="4">Global thresholding</MenuItem>
                                <MenuItem value="5">Transformations</MenuItem>
                            </Select>
                        </FormControl>
                        {secondTabOptions === "3" ?
                            <div className='local-sliders'>
                                <div className='sliders-contain'>
                                    <label htmlFor="">Block size</label>
                                    <Slider value={sliderBlock} onChange={(e : any) => setSliderBlock(e.target.value)} min={5} max={10} step={1} style={{ width: "50%" }}  aria-label="Default" valueLabelDisplay="auto" />
                                </div>
                                <div className='sliders-contain'>
                                    <label htmlFor="">C</label>
                                    <Slider value={sliderC} onChange={(e : any) => setSliderC(e.target.value)} min={0} max={100} step={1} style={{ width: "50%" }}  aria-label="Default" valueLabelDisplay="auto" />
                                </div>
                                <button className='apply-btn' onClick={handleLocalButton}>Apply</button>
                            </div>
                            : secondTabOptions === "4" ?
                                <div className='global-slider'>
                                    <div className='sliders-contain'>
                                        <label htmlFor="">label</label>
                                        <Slider value={sliderGlobal} onChange={(e : any) => setSliderGlobal(e.target.value)} min={0} max={100} step={1} style={{ width: "50%" }}  aria-label="Default" valueLabelDisplay="auto" />
                                    </div>
                                    <button className='apply-btn' onClick={handleGlobalButton}>Apply</button>
                                </div>
                                : null
                        }
                    </div>
                </Col>
                <Col style={{ height: "85vh" }} lg={9} md={9} sm={12} xs={12}>
                    {secondTabOptions !== "0" ?
                        <Row>
                            <Col style={{ height: "35rem", display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center" }} lg={4} md={4} sm={12} xs={12}>
                                {secondTabOptions !== "5" ?
                                    <div className='img-label-contain'>
                                        <label htmlFor="">Output</label>
                                        <div className='img-contain'>
                                            <img className='output-images' src="" alt="" />
                                        </div>
                                    </div>
                                    :
                                    <>
                                        <div className='img-label-contain'>
                                            <label htmlFor="">Output</label>
                                            <div className='img-contain'>
                                                <img className='output-images' src="" alt="" />
                                            </div>
                                        </div>
                                        <div className='img-label-contain'>
                                            <label htmlFor="">img</label>
                                            <div className='img-contain'>
                                                <img className='output-images' src="" alt="" />
                                            </div>
                                        </div>
                                    </>
                                }
                            </Col>
                            <Col style={{ height: "35rem", display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center" }} lg={4} md={4} sm={12} xs={12}>
                                {secondTabOptions !== "5" ?
                                    <div className='img-label-contain'>
                                        <label htmlFor="">Histogram</label>
                                        <div className='img-contain'>
                                            <img className='output-images' src="" alt="" />
                                        </div>
                                    </div>
                                    :
                                    <>
                                        <div className='img-label-contain'>
                                            <label htmlFor="">Histogram</label>
                                            <div className='img-contain'>
                                                <img className='output-images' src="" alt="" />
                                            </div>
                                        </div>
                                        <div className='img-label-contain'>
                                            <label htmlFor="">img</label>
                                            <div className='img-contain'>
                                                <img className='output-images' src="" alt="" />
                                            </div>
                                        </div>
                                    </>
                                }
                            </Col>
                            <Col style={{ height: "35rem", display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center" }} lg={4} md={4} sm={12} xs={12}>
                                {secondTabOptions !== "5" ?
                                    <div className='img-label-contain'>
                                        <label htmlFor="">Comulative</label>
                                        <div className='img-contain'>
                                            <img className='output-images' src="" alt="" />
                                        </div>
                                    </div>
                                    :
                                    <>
                                        <div className='img-label-contain'>
                                            <label htmlFor="">Comulative</label>
                                            <div className='img-contain'>
                                                <img className='output-images' src="" alt="" />
                                            </div>
                                        </div>
                                        <div className='img-label-contain'>
                                            <label htmlFor="">img</label>
                                            <div className='img-contain'>
                                                <img className='output-images' src="" alt="" />
                                            </div>
                                        </div>
                                    </>
                                }
                            </Col>
                        </Row>
                        : null
                    }

                </Col>
            </Row>
        </Container>
    )
}

export default SecondTab