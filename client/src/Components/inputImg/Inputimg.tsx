import React, { useRef, useContext, useState } from 'react'
import { FileContext } from '../contexts/fileContext'
import axios from '../global/API/axios';
import './Inputimg.css'

const Inputimg = () => {

  const inputFile = useRef<HTMLInputElement | null>(null);
  const {
    uploadImg,
    setUploadImg
  } = useContext(FileContext);


  const handleUpload = (e: any) => {
    setUploadImg(URL.createObjectURL(e.target.files[0]));
    const formData = new FormData();
    formData.append("image", e.target.files[0])
    axios.post('/image/',
        formData
    ).then((response: any) => {
      console.log(response)
    }).catch((err: any) => {
        console.log(err)
    })
  }

  const handleButtonClick = () => {
    if (inputFile.current !== null) {
      inputFile.current.click();
    }
  };

  return (
    <div className='input-contain'>
      <input
        type='file'
        id='file'
        ref={inputFile}
        style={{ display: 'none' }}
        onChange={handleUpload}
      />
      <button className='upload-btn' onClick={handleButtonClick}>
        Upload
      </button>
      <div className='upload-img-contain'>
      <img className='upload-img' style={{display: uploadImg === undefined || uploadImg === "" ? "none" : "block"}} src={uploadImg} alt="" />
      </div>
    </div>
  )
}

export default Inputimg