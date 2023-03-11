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
        setSliderGlobal,
        imgId,
        baseURL,

    } = useContext(FileContext);

    const [secondTabOptions, setSecondTabOptions] = useState<string>('');
    const [imgOutput, setImgOutput] = useState<string | undefined>('')
    const [imgOutputHisto, setimgOutputHisto] = useState<string | undefined>('')
    const [imgOutputCum, setimgOutputCum] = useState<string | undefined>('')
    const [redHist, setRedHist] = useState<string | undefined>('')
    const [redCum, setRedCum] = useState<string | undefined>('')
    const [blueHist, setBlueHist] = useState<string | undefined>('')
    const [blueCum, setBlueCum] = useState<string | undefined>('')
    const [greenHist, setGreenHist] = useState<string | undefined>('')
    const [greenCum, setGreenCum] = useState<string | undefined>('')

    // integration with Back
    useEffect(() => {
        if (secondTabOptions === '5') {
            axios.post(`/image/${imgId}/transformation/`,
                { option: secondTabOptions }
            ).then((res: any) => {
                const urls = res.data
                setRedHist(urls.redHistURL)
                setBlueHist(urls.blueHistURL)
                setGreenHist(urls.greenHistURL)
                setRedCum(urls.redCumURL)
                setBlueCum(urls.blueCumURL)
                setGreenCum(urls.greenCumURL)

                console.log(res)
            }).catch((err: any) => {
                console.log(err)
            })
        } else {

            if (imgId) {
                axios.post(`/image/${imgId}/histograms_process/`,
                    { option: secondTabOptions }
                ).then((res: any) => {
                    setImgOutput(baseURL + res.data.image);
                    setimgOutputHisto(res.data.histURL)
                    setimgOutputCum(res.data.cumURL)

                    console.log(res)
                }).catch((err: any) => {
                    console.log(err)
                })
            }
        }
    }, [secondTabOptions, imgId])


    const handleChange = (event: SelectChangeEvent) => {
        setSecondTabOptions(event.target.value);
    };

    const handleGlobalButton = () => {
        axios.post(`/image/${imgId}/histograms_process/`,
            { option: secondTabOptions, globalThreshold: sliderGlobal }
        ).then((res: any) => {
            setImgOutput(baseURL + res.data.image);
            setimgOutputHisto(res.data.histURL)
            setimgOutputCum(res.data.cumURL)
        }).catch((err: any) => {
            console.log(err)
        })
    }

    const handleLocalButton = () => {
        axios.post(`/image/${imgId}/histograms_process/`,
            { option: secondTabOptions, blocksize: sliderBlock, c: sliderC }
        ).then((res: any) => {
            setImgOutput(baseURL + res.data.image);
            setimgOutputHisto(res.data.histURL)
            setimgOutputCum(res.data.cumURL)
        }).catch((err: any) => {
            console.log(err)
        })
    }

    // console.log(secondTabOptions)

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
                                    <Slider value={sliderBlock} onChange={(e: any) => setSliderBlock(e.target.value)} min={5} max={10} step={1} style={{ width: "50%" }} aria-label="Default" valueLabelDisplay="auto" />
                                </div>
                                <div className='sliders-contain'>
                                    <label htmlFor="">C</label>
                                    <Slider value={sliderC} onChange={(e: any) => setSliderC(e.target.value)} min={0} max={100} step={1} style={{ width: "50%" }} aria-label="Default" valueLabelDisplay="auto" />
                                </div>
                                <button className='apply-btn' onClick={handleLocalButton}>Apply</button>
                            </div>
                            : secondTabOptions === "4" ?
                                <div className='global-slider'>
                                    <div className='sliders-contain'>
                                        <label htmlFor="">label</label>
                                        <Slider value={sliderGlobal} onChange={(e: any) => setSliderGlobal(e.target.value)} min={0} max={100} step={1} style={{ width: "50%" }} aria-label="Default" valueLabelDisplay="auto" />
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
                                            <img className='output-images' src={imgOutput} alt="" />
                                        </div>
                                    </div>
                                    :
                                    <>
                                        <div className='img-label-contain'>
                                            <label htmlFor="">Red Histogram</label>
                                            <div className='img-contain'>
                                                <img className='output-images' src={redHist} alt="" />
                                            </div>
                                        </div>
                                        <div className='img-label-contain'>
                                            <label htmlFor="">Red Cumulative</label>
                                            <div className='img-contain'>
                                                <img className='output-images' src={redCum} alt="" />
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
                                            <img className='output-images' src={imgOutputHisto} alt="" />
                                        </div>
                                    </div>
                                    :
                                    <>
                                        <div className='img-label-contain'>
                                            <label htmlFor="">Green Histogram</label>
                                            <div className='img-contain'>
                                                <img className='output-images' src={greenHist} alt="" />
                                            </div>
                                        </div>
                                        <div className='img-label-contain'>
                                            <label htmlFor="">Green Cumulative</label>
                                            <div className='img-contain'>
                                                <img className='output-images' src={greenCum} alt="" />
                                            </div>
                                        </div>
                                    </>

                                }
                            </Col>
                            <Col style={{ height: "35rem", display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center" }} lg={4} md={4} sm={12} xs={12}>
                                {secondTabOptions !== "5" ?
                                    <div className='img-label-contain'>
                                        <label htmlFor="">Cumulative</label>
                                        <div className='img-contain'>
                                            <img className='output-images' src={imgOutputCum} alt="" />
                                        </div>
                                    </div>
                                    :
                                    <>
                                        <div className='img-label-contain'>
                                            <label htmlFor="">Blue Histogram</label>
                                            <div className='img-contain'>
                                                <img className='output-images' src={blueHist} alt="" />
                                            </div>
                                        </div>
                                        <div className='img-label-contain'>
                                            <label htmlFor="">Blue Cumulative</label>
                                            <div className='img-contain'>
                                                <img className='output-images' src={blueCum} alt="" />
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