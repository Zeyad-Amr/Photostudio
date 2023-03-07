import React, { useRef, useContext, useState } from 'react'
import { FileContext } from '../contexts/fileContext'
import axios from '../global/API/axios';

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
    <div>
      <input
        type='file'
        id='file'
        ref={inputFile}
        style={{ display: 'none' }}
        onChange={handleUpload}
      />
      <button onClick={handleButtonClick}>
        Upload
      </button>
      <img style={{width:"15rem",height:"15rem",}} src={uploadImg} alt="" />
    </div>
  )
}

export default Inputimg