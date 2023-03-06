import React, { useRef, useContext, useState } from 'react'
import { FileContext } from '../contexts/fileContext'

const Inputimg = () => {

  const inputFile = useRef<HTMLInputElement | null>(null);
  // const {
  //   uploadImg,
  //   setUploadImg
  // } = useContext(FileContext);

  const [uploadImg, setUploadImg] = useState<string | undefined>('')


  const handleUpload = (e: any) => {
    setUploadImg(URL.createObjectURL(e.target.files[0]));
    const formData = new FormData();
    formData.append("Img", e.target.files[0])
    // axios.post('/',
    //     formData
    // ).then((response) => {
    //   console.log(response)
    // }).catch((err) => {
    //     console.log(err)
    // })
  }

  const handleButtonClick = () => {
    if ( inputFile.current !== null ) {
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
      <img src={uploadImg} alt="" />
    </div>
  )
}

export default Inputimg