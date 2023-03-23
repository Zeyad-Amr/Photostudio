import { useRef } from 'react'
import axios from '../../global/API/axios';

const UploadImg = () => {

    const inputFile = useRef<HTMLInputElement | null>(null);

    //   Integrate with back

    const handleUpload = (e: any) => {
        //     const formData = new FormData();
        //     formData.append("image", e.target.files[0])
        //     axios.post('/image/',
        //     formData
        //     ).then((res: any) => {
        //       console.log(res)
        //     }).catch((err: any) => {
        //         console.log(err)
        //     })
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
                <img className='upload-img' alt="" />
            </div>
        </div>
    )
}

export default UploadImg