import React, { useRef, useContext, useState } from 'react'
import { FileContext } from '../../contexts/fileContext'
import axios from '../../../Components/global/API/axios';
import { Col, Container, Row } from 'react-bootstrap';

const Inputimg = () => {

  const inputFilefirst = useRef<HTMLInputElement | null>(null);
  const inputFilesecond = useRef<HTMLInputElement | null>(null);

  const {
    uploadImgfirst,
    setUploadImgfirst,
    uploadImgsecond,
    setUploadImgsecond
  } = useContext(FileContext);


  const handleUploadfirst = (e: any) => {
    setUploadImgfirst(URL.createObjectURL(e.target.files[0]));
    const formData = new FormData();
    formData.append("image1", e.target.files[0])
    // axios.post('/image/',
    //   formData
    // ).then((response: any) => {
    //   console.log(response)
    // }).catch((err: any) => {
    //   console.log(err)
    // })
  }

  const handleUploadsecond = (e: any) => {
    setUploadImgsecond(URL.createObjectURL(e.target.files[0]));
    const formData = new FormData();
    formData.append("image2", e.target.files[0])
    // axios.post('/image/',
    //   formData
    // ).then((response: any) => {
    //   console.log(response)
    // }).catch((err: any) => {
    //   console.log(err)
    // })
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

  return (
    <Container fluid>
      <Row>
        <Col style={{ height: "85vh" , display:"flex" , flexDirection:"column", justifyContent:"center" , alignItems:"center"}} lg={4} md={4} sm={12} xs={12}>
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
        </Col>
        <Col style={{ height: "85vh" , display:"flex" , flexDirection:"column", justifyContent:"center" , alignItems:"center"}} lg={4} md={4} sm={12} xs={12}>
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
        </Col>
      </Row>
    </Container>
  )
}

export default Inputimg





// import Plot from 'react-plotly.js';
{/* <Plot data={[angle]} layout={layout} config={config} /> */ }
  // var angle = {
  //   x: frequency,
  //   y: phase,
  //   type: "scatter",
  //   line: {
  //     color: "#333",
  //     width: 2,
  //   },
  //   yaxis:"y2"

  // };

  // var config = {
  //   displayModeBar: false,
  //   displaylogo: false
  // }

  // var layout = {
  //   width: 420,
  //   height: 240,
  //   margin: {
  //     l: 20,
  //     r: 0,
  //     // b: 0,
  //     t: 0
  //   },
  //   xaxis: {
  //     automargin: true,
  //     title: {
  //       text: "Frequency",
  //       standoff: 20
  //     }},
  //     yaxis1: {
  //       automargin: true,
  //       tickangle: 90,
  //       title: {
  //         text: "Magnitude",
  //         standoff: 20
  //       }},
  //       yaxis2: {
  //         automargin: true,
  //         tickangle: 90,
  //         title: {
  //           text: "Phase",
  //           standoff: 20
  //         }},
  // };