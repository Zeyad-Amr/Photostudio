import React, { useRef, useContext, useState } from 'react'
import { FileContext } from '../contexts/fileContext'
import axios from '../global/API/axios';
import './Inputimg.css'

const Inputimg = () => {

  const inputFile = useRef<HTMLInputElement | null>(null);
  const {
    baseURL,
    uploadImg,
    setUploadImg,
    imgId,
    setImgId
  } = useContext(FileContext);


  const handleUpload = (e: any) => {
    const formData = new FormData();
    formData.append("image", e.target.files[0])
    axios.post('/image/',
    formData
    ).then((res: any) => {
      console.log(res.data.id);
      
      setUploadImg(baseURL + res.data.image);
      setImgId(res.data.id)
      console.log(res)
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