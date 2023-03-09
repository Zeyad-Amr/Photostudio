import { useState, useContext } from 'react';
import { Col, Container, Row } from 'react-bootstrap'
import Inputimg from '../../inputImg/Inputimg'
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select, { SelectChangeEvent } from '@mui/material/Select';
import Slider from '@mui/material/Slider';
import axios from '../../global/API/axios';
import './FirstTab.css'
import { FileContext } from '../../contexts/fileContext';

const FirstTab = () => {

  const {
    imgId,
    baseURL
  } = useContext(FileContext);


  const [selectionMode, setSelectionMode] = useState<string>('');
  const [firstTabOptions, setFirstTabOptions] = useState<string>('');
  const [imgOutput, setImgOutput] = useState<string | undefined>('')
  const [outputId, setOutputId] = useState<string | undefined>('')


  // noise sliders & functions
  const [uniformSlider, setUniformSlider] = useState<number>(50)
  const [gaussianSlider, setGaussianSlider] = useState<number>(90)
  const [saltPepperSlider, setSaltPepperSlider] = useState<number>(30)


  const sendRequest = (id: string | undefined, range?: number) => {

    if (id === '') {
      console.log("aHa");
      id = imgId
    }
    axios.post(`/image/${id}/filter_process/`, {
      option: firstTabOptions, range
    }).then((res: any) => {
      setImgOutput(baseURL + res.data.image)
      setOutputId(res.data.id)
      console.log(res)
    }).catch((err: any) => {
      console.log(err)
    })
  }
  const handleUniformClick = () => {
    sendRequest(outputId, uniformSlider)
  }
  const handleGaussianClick = () => {
    sendRequest(outputId, gaussianSlider)
  }
  const handleSaltPepperClick = () => {
    sendRequest(outputId, saltPepperSlider)
  }

  // filter slider & functions
  const [averageSlider, setAverageSlider] = useState<number>(40)
  const [gaussianFilterSlider, setGaussianFilterSlider] = useState<number>(80)
  const [medianSlider, setMedianSlider] = useState<number>(20)
  const handleAverageClick = () => {
    sendRequest(outputId, averageSlider)
  }
  const handleGaussianFilterClick = () => {
    sendRequest(outputId, gaussianFilterSlider)
  }
  const handleMedianClick = () => {
    sendRequest(outputId, medianSlider)
  }

  // edge detection slider & functions
  const handleSobelClick = () => {
    sendRequest(outputId)
  }
  const handleRobertsClick = () => {
    sendRequest(outputId)
  }
  const handlePrewittClick = () => {
    sendRequest(outputId)
  }
  const handleCannyClick = () => {
    sendRequest(outputId)
  }

  // console.log(selectionMode)
  // console.log(firstTabOptions)

  const handleChangeSelection = (event: SelectChangeEvent) => {
    setSelectionMode(event.target.value);
  };

  const handleChangeOptions = (event: SelectChangeEvent) => {
    setFirstTabOptions(event.target.value);
  };
  const showId = () => {
    console.log(outputId);
  };

  return (
    <Container fluid>
      <Row>
        <Col style={{ height: "85vh", display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center" }} lg={4} md={6} sm={12} xs={12}>
          <Inputimg />
          <button className='apply-btn' onClick={showId}>show Id</button>

        </Col>
        <Col style={{ height: "85vh", display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center" }} lg={4} md={6} sm={12} xs={12}>
          {/* selection mode */}
          <FormControl style={{ marginBottom: "2rem", width: "13rem" }} variant="standard" sx={{ m: 1, minWidth: 150 }}>
            <InputLabel id="demo-simple-select-autowidth-label">Choose mode</InputLabel>
            <Select
              labelId="demo-simple-select-autowidth-label"
              id="demo-simple-select-autowidth"
              value={selectionMode}
              onChange={handleChangeSelection}
              autoWidth
            >
              <MenuItem value="0">
                <em>None</em>
              </MenuItem>
              <MenuItem value="1">Noise</MenuItem>
              <MenuItem value="2">Filter</MenuItem>
              <MenuItem value="3">Edges Detection</MenuItem>
            </Select>
          </FormControl>
          {
            selectionMode === "1" ?
              // noise selection
              <FormControl style={{ marginBottom: "2rem", width: "13rem" }} variant="standard" sx={{ m: 1, minWidth: 150 }}>
                <InputLabel id="demo-simple-select-autowidth-label">Choose noise</InputLabel>
                <Select
                  labelId="demo-simple-select-autowidth-label"
                  id="demo-simple-select-autowidth"
                  value={firstTabOptions}
                  onChange={handleChangeOptions}
                  autoWidth
                >
                  <MenuItem value="0">
                    <em>None</em>
                  </MenuItem>
                  <MenuItem value="1">Uniform</MenuItem>
                  <MenuItem value="2">Gaussian</MenuItem>
                  <MenuItem value="3">Salt & Pepper</MenuItem>
                </Select>
              </FormControl>
              : selectionMode === "2" ?
                // filter selection
                <FormControl style={{ marginBottom: "2rem", width: "13rem" }} variant="standard" sx={{ m: 1, minWidth: 150 }}>
                  <InputLabel id="demo-simple-select-autowidth-label">Choose filter</InputLabel>
                  <Select
                    labelId="demo-simple-select-autowidth-label"
                    id="demo-simple-select-autowidth"
                    value={firstTabOptions}
                    onChange={handleChangeOptions}
                    autoWidth
                  >
                    <MenuItem value="0">
                      <em>None</em>
                    </MenuItem>
                    <MenuItem value="4">Average</MenuItem>
                    <MenuItem value="5">Gaussian</MenuItem>
                    <MenuItem value="6">Median</MenuItem>
                  </Select>
                </FormControl>
                : selectionMode === "3" ?
                  // edges detection selection
                  <FormControl style={{ marginBottom: "2rem", width: "13rem" }} variant="standard" sx={{ m: 1, minWidth: 150 }}>
                    <InputLabel id="demo-simple-select-autowidth-label">Choose edge detectors</InputLabel>
                    <Select
                      labelId="demo-simple-select-autowidth-label"
                      id="demo-simple-select-autowidth"
                      value={firstTabOptions}
                      onChange={handleChangeOptions}
                      autoWidth
                    >
                      <MenuItem value="0">
                        <em>None</em>
                      </MenuItem>
                      <MenuItem value="7" onClick={handleSobelClick}>Sobel</MenuItem>
                      <MenuItem value="8" onClick={handleRobertsClick}>Roberts</MenuItem>
                      <MenuItem value="9" onClick={handlePrewittClick}>Prewitt</MenuItem>
                      <MenuItem value="10" onClick={handleCannyClick}>Canny</MenuItem>
                    </Select>
                  </FormControl>
                  : null
          }
          {
            // start noise sliders
            firstTabOptions === "1" ?
              <div className='btn-slider-contain'>
                <div className='sliders-contain'>
                  <Slider value={uniformSlider} onChange={(e: any) => setUniformSlider(e.target.value)} min={0} max={100} step={1} style={{ width: "10rem" }} aria-label="Default" valueLabelDisplay="auto" />
                </div>
                <button className='apply-btn' onClick={handleUniformClick}>Apply</button>
              </div>
              : firstTabOptions === "2" ?
                <div className='btn-slider-contain'>
                  <div className='sliders-contain'>
                    <Slider value={gaussianSlider} onChange={(e: any) => setGaussianSlider(e.target.value)} min={0} max={100} step={1} style={{ width: "10rem" }} aria-label="Default" valueLabelDisplay="auto" />
                  </div>
                  <button className='apply-btn' onClick={handleGaussianClick}>Apply</button>
                </div>
                : firstTabOptions === "3" ?
                  <div className='btn-slider-contain'>
                    <div className='sliders-contain'>
                      <Slider value={saltPepperSlider} onChange={(e: any) => setSaltPepperSlider(e.target.value)} min={0} max={100} step={1} style={{ width: "10rem" }} aria-label="Default" valueLabelDisplay="auto" />
                    </div>
                    <button className='apply-btn' onClick={handleSaltPepperClick}>Apply</button>
                  </div>
                  // End noise sliders
                  // Start filter sliders
                  : firstTabOptions === "4" ?
                    <div className='btn-slider-contain'>
                      <div className='sliders-contain'>
                        <Slider value={averageSlider} onChange={(e: any) => setAverageSlider(e.target.value)} min={0} max={100} step={1} style={{ width: "10rem" }} aria-label="Default" valueLabelDisplay="auto" />
                      </div>
                      <button className='apply-btn' onClick={handleAverageClick}>Apply</button>
                    </div>
                    : firstTabOptions === "5" ?
                      <div className='btn-slider-contain'>
                        <div className='sliders-contain'>
                          <Slider value={gaussianFilterSlider} onChange={(e: any) => setGaussianFilterSlider(e.target.value)} min={0} max={100} step={1} style={{ width: "10rem" }} aria-label="Default" valueLabelDisplay="auto" />
                        </div>
                        <button className='apply-btn' onClick={handleGaussianFilterClick}>Apply</button>
                      </div>
                      : firstTabOptions === "6" ?
                        <div className='btn-slider-contain'>
                          <div className='sliders-contain'>
                            <Slider value={medianSlider} onChange={(e: any) => setMedianSlider(e.target.value)} min={0} max={100} step={1} style={{ width: "10rem" }} aria-label="Default" valueLabelDisplay="auto" />
                          </div>
                          <button className='apply-btn' onClick={handleMedianClick}>Apply</button>
                        </div>
                        // End filter sliders
                        : null
          }
        </Col>
        <Col style={{ height: "85vh", display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center" }} lg={4} md={12} sm={12} xs={12}>
          <label className='output-label'>Output</label>
          <div className='output-img-contain'>
            <img className='output-img' src={imgOutput} alt="" />
          </div>
        </Col>
      </Row>
    </Container>
  )
}

export default FirstTab