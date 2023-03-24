import { useContext, useState } from 'react'
import { Col, Container, Row } from 'react-bootstrap'
import UploadImg from './UploadImg'
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select, { SelectChangeEvent } from '@mui/material/Select';
import Slider from '@mui/material/Slider';
import './ForthTab.css'
import axios from '../../global/API/axios';
import { FileContext } from '../../contexts/fileContext';


const ForthTab = () => {

    const [options, setOptions] = useState<string>('');
    const [minRadius, setMinRadius] = useState<number>(25)
    const [maxRadius, setMaxRadius] = useState<number>(40)
    const [circleThreshold, setCircleThreshold] = useState<number>(10)
    const [lineThreshold, setLineThreshold] = useState<number>(10)
    const [spinnerFlag, setSpinnerFlag] = useState<boolean | null>(false)
    const [imgOutput, setImgOutput] = useState<string | undefined>('')

    const [imgId, setImgId] = useState<string | undefined>('')

    const {
        baseURL,
    } = useContext(FileContext);


    const handleImgId = (id: string) => {
        setImgId(id);
    }


    const handleChangeOptions = (event: SelectChangeEvent) => {
        setOptions(event.target.value);
    };

    // integrating with back

    const sendRequest = (option: string, firstValue: number, secondValue?: number, thirdValue?: number) => {
        setSpinnerFlag(true)
        axios.post(`/image/detect/${imgId}/detect_shapes/`, {
            option, firstValue, secondValue, thirdValue
        }).then((res: any) => {
            setSpinnerFlag(false)
            setImgOutput(baseURL + res.data.image)

            console.log(res)
        }).catch((err: any) => {
            console.log(err.message)
        })
    }

    const handleLineClick = () => {
        sendRequest(options, lineThreshold)
    }

    const handleCircleClick = () => {
        sendRequest(options, minRadius, maxRadius, circleThreshold)
    }


    return (
        <Container fluid>
            <Row>
                <Col style={{ height: "85vh", display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center" }} lg={4} md={6} sm={12} xs={12}>
                    <UploadImg setImgId={handleImgId} />
                </Col>
                <Col style={{ height: "85vh", display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center" }} lg={4} md={6} sm={12} xs={12}>
                    <FormControl style={{ marginTop: "2rem", width: "14rem" }} variant="standard" sx={{ m: 1, minWidth: 150 }}>
                        <InputLabel id="demo-simple-select-autowidth-label">Choose detector</InputLabel>
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
                            <MenuItem value="4">Active Contour</MenuItem>
                        </Select>
                    </FormControl>
                    {
                        options === "1" ?
                            <div className='btn-slider-contain forthtab'>
                                <div className='sliders-contain'>
                                    <label htmlFor="">Threshold</label>
                                    <Slider value={lineThreshold} onChange={(e: any) => setLineThreshold(e.target.value)} min={100} max={255} step={1} style={{ width: "11rem" }} aria-label="Default" valueLabelDisplay="auto" />
                                </div>
                                <button className='apply-btn' onClick={handleLineClick}>Apply</button>
                            </div>

                            : options === "2" ?
                                <div className='btn-slider-contain forthtab'>
                                    <div className='sliders-contain'>
                                        <label htmlFor="">Min Radius</label>
                                        <Slider value={minRadius} onChange={(e: any) => setMinRadius(e.target.value)} min={0} max={100} step={1} style={{ width: "11rem" }} aria-label="Default" valueLabelDisplay="auto" />
                                    </div>
                                    <div className='sliders-contain'>
                                        <label htmlFor="">Max Radius</label>
                                        <Slider value={maxRadius} onChange={(e: any) => setMaxRadius(e.target.value)} min={100} max={200} step={1} style={{ width: "11rem" }} aria-label="Default" valueLabelDisplay="auto" />
                                    </div>
                                    <div className='sliders-contain'>
                                        <label htmlFor="">Threshold</label>
                                        <Slider value={circleThreshold} onChange={(e: any) => setCircleThreshold(e.target.value)} min={0} max={5} step={0.1} style={{ width: "11rem" }} aria-label="Default" valueLabelDisplay="auto" />
                                    </div>
                                    <button className='apply-btn' onClick={handleCircleClick}>Apply</button>
                                </div>
                                : null
                    }
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
                                            : options === "4" ?
                                                "Contour Output"
                                                : "Output"
                            }
                        </label>
                        <div className='output-img-contain'>
                            {
                                spinnerFlag ?
                                    <div className="spinner-border" role="status" ></div>
                                    :
                                    <img className='output-img' style={{ display: imgOutput === undefined || imgOutput === "" ? "none" : "block" }} src={imgOutput} alt="" />
                            }
                        </div>
                    </div>
                </Col>
            </Row>
        </Container>
    )
}

export default ForthTab