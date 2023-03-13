import React, { useRef, useContext, useState, useEffect } from 'react'
import { FileContext } from '../../contexts/fileContext'
import axios from '../../../Components/global/API/axios';
import { Col, Container, Row } from 'react-bootstrap';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select, { SelectChangeEvent } from '@mui/material/Select';
import Slider from '@mui/material/Slider';
import './ThirdTab.css'

const Inputimg = () => {

  const inputFilefirst = useRef<HTMLInputElement | null>(null);
  const inputFilesecond = useRef<HTMLInputElement | null>(null);
  const [thirdTabOptions, setThirdTabOptions] = useState<string>('');
  const [imgOutput, setImgOutput] = useState<string | undefined>('')
  const [firstImgId, setFirstImgId] = useState<string | undefined>()
  const [secondImgId, setSecondImgId] = useState<string | undefined>()
  const [firstCutoffSlider, setFirstCutoffSlider] = useState<number>(10)
  const [secondCutoffSlider, setSecondCutoffSlider] = useState<number>(40)


  const {
    uploadImgfirst,
    setUploadImgfirst,
    uploadImgsecond,
    setUploadImgsecond,
    baseURL
  } = useContext(FileContext);


  console.log(thirdTabOptions)

  const [spinnerFlag, setSpinnerFlag] = useState<boolean | null>(false)

  const handleUploadfirst = (e: any) => {
    const formData = new FormData();
    formData.append("image", e.target.files[0])
    axios.post('/image/',
      formData
    ).then((res: any) => {
      setUploadImgfirst(baseURL + res.data.image);
      setFirstImgId(res.data.id)
      console.log(res)
    }).catch((err: any) => {
      console.log(err)
    })
  }

  const handleUploadsecond = (e: any) => {
    setUploadImgsecond(URL.createObjectURL(e.target.files[0]));
    const formData = new FormData();
    formData.append("image", e.target.files[0])
    axios.post('/image/',
      formData
    ).then((res: any) => {
      setUploadImgsecond(baseURL + res.data.image);
      setSecondImgId(res.data.id)
      console.log(res)
    }).catch((err: any) => {
      console.log(err)
    })
  }

  const handleButtonClickfirst = () => {
    if (inputFilefirst.current !== null) {
      inputFilefirst.current.click();
    }
  };

  const handleButtonClicksecond = () => {
    if (inputFilesecond.current !== null) {
      inputFilesecond.current.click();
    }
  };

  const handleChangeOptions = (event: SelectChangeEvent) => {
    setThirdTabOptions(event.target.value);
  };

  const handleCutoffButton = () => {
    setSpinnerFlag(true)
    axios.post('/image/frequancy_process/',
      {
        option: thirdTabOptions,
        f_imgId: firstImgId,
        s_imgId: secondImgId,
        f_cutoff: firstCutoffSlider,
        s_cutoff: secondCutoffSlider
      }
    ).then((res: any) => {
      setImgOutput(baseURL + res.data.image)
      setSpinnerFlag(false)
      console.log(res)
    }).catch((err: any) => {
      console.log(err)
    })
  }

  return (
    <Container fluid>
      <Row>
        <Col style={{ height: "85vh", display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center" }} lg={4} md={4} sm={12} xs={12}>
          <div className='input-contain'>
            <input
              type='file'
              id='file'
              ref={inputFilefirst}
              style={{ display: 'none' }}
              onChange={handleUploadfirst}
            />
            <button className='upload-btn' onClick={handleButtonClickfirst}>
              Upload
            </button>
            <div className='upload-img-contain'>
              <img className='upload-img' style={{ display: uploadImgfirst === undefined || uploadImgfirst === "" ? "none" : "block" }} src={uploadImgfirst} alt="" />
            </div>
          </div>
          {
            thirdTabOptions === "1" || thirdTabOptions === "2" ?
              <div className='all-sliders'>
                <div className='sliders-contain'>
                  <label htmlFor="">First Cutoff</label>
                  <Slider value={firstCutoffSlider} onChange={(e: any) => setFirstCutoffSlider(e.target.value)} min={0} max={50} step={1} style={{ width: "11rem" }} aria-label="Default" valueLabelDisplay="auto" />
                </div>
              </div>
              : null
          }
        </Col>
        <Col style={{ height: "85vh", display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center" }} lg={4} md={4} sm={12} xs={12}>
          <div className='input-contain'>
            <input
              type='file'
              id='file'
              ref={inputFilesecond}
              style={{ display: 'none' }}
              onChange={handleUploadsecond}
            />
            <button className='upload-btn' onClick={handleButtonClicksecond}>
              Upload
            </button>
            <div className='upload-img-contain'>
              <img className='upload-img' style={{ display: uploadImgsecond === undefined || uploadImgsecond === "" ? "none" : "block" }} src={uploadImgsecond} alt="" />
            </div>
          </div>
          {
            thirdTabOptions === "1" || thirdTabOptions === "2" ?
              <div className='all-sliders'>
                <div className='sliders-contain'>
                  <label htmlFor="">Second Cutoff</label>
                  <Slider value={secondCutoffSlider} onChange={(e: any) => setSecondCutoffSlider(e.target.value)} min={0} max={50} step={1} style={{ width: "11rem" }} aria-label="Default" valueLabelDisplay="auto" />
                </div>
              </div>
              : null
          }
        </Col>
        <Col style={{ height: "85vh", display: "flex", flexDirection: "column", justifyContent: "center", alignItems: "center" }} lg={4} md={4} sm={12} xs={12}>
          <FormControl style={{ marginTop: "-1rem", marginBottom: "1rem", width: "12rem" }} variant="standard" sx={{ m: 1, minWidth: 150 }}>
            <InputLabel id="demo-simple-select-autowidth-label">Choose merge</InputLabel>
            <Select
              labelId="demo-simple-select-autowidth-label"
              id="demo-simple-select-autowidth"
              value={thirdTabOptions}
              onChange={handleChangeOptions}
              autoWidth
            >
              <MenuItem value="0">
                <em>None</em>
              </MenuItem>
              <MenuItem value="1">High 1 + Low 2</MenuItem>
              <MenuItem value="2">Low 1 + High 2</MenuItem>
            </Select>
          </FormControl>
          {/* <label className='output-label'>Output</label> */}
          <div className='output-img-contain'>
            {spinnerFlag === true ?
          <div className="spinner-border" role="status" style={{ display: spinnerFlag === true ? "block" : "none" }}></div>
          :
            <img className='output-img' style={{ display: imgOutput === undefined || imgOutput === "" ? "none" : "block" }} src={imgOutput} alt="" />
}
          </div>
          {
            thirdTabOptions === "1" || thirdTabOptions === "2" ?
              <div className='all-sliders'>
                <button className='apply-btn' onClick={handleCutoffButton}>Apply</button>
              </div>
              : null
          }
        </Col>
      </Row>
    </Container>
  )
}

export default Inputimg

