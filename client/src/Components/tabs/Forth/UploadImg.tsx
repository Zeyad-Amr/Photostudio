import { useContext, useRef, useState } from 'react'
import { FileContext } from '../../contexts/fileContext';
import axios from '../../global/API/axios';

interface Props {
    setImgId: (id: string) => void;
}

const UploadImg = (props: Props) => {

    const inputFile = useRef<HTMLInputElement | null>(null);
    const [spinnerFlag, setSpinnerFlag] = useState<boolean | null>(false)
    const [uploadImg, setUploadImg] = useState<string | undefined>('')

    const {
        baseURL,
    } = useContext(FileContext);


    //   Integrating with back


    const handleUpload = (e: any) => {
        const formData = new FormData();
        formData.append("image", e.target.files[0])
        setSpinnerFlag(true)
        axios.post('/image/',
            formData
        ).then((res: any) => {
            setSpinnerFlag(false)
            setUploadImg(baseURL + res.data.image);
            props.setImgId(res.data.id)
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
            <div className='upload-img-contain forthTab'>
                {
                    spinnerFlag ?
                        <div className="spinner-border" role="status"></div>
                        :
                        <img className='upload-img' style={{ display: uploadImg === undefined || uploadImg === "" ? "none" : "block" }} src={uploadImg} alt="" />
                }
            </div>
        </div>
    )
}

export default UploadImg