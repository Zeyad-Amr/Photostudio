import { createContext, useState } from 'react';
const FileContext = createContext<unknown | any>('');

const FileContextProvider = ({ children } : any) => {

    // input img component
    const baseURL: string = 'http://localhost:8000' 
    const [uploadImg,setUploadImg] = useState<string | undefined>('')
    const [imgId,setImgId] = useState<string | undefined>('')
    
    // SecondTab component
    const [sliderC,setSliderC] = useState<number>(40)
    const [sliderBlock,setSliderBlock] = useState<number>(6)
    const [sliderGlobal,setSliderGlobal] = useState<number>(30)
    
    // Third tab component
    const [uploadImgfirst,setUploadImgfirst] = useState<string | undefined>('')
    const [uploadImgsecond,setUploadImgsecond] = useState<string | undefined>('')


    return (
        <FileContext.Provider
            value={{ 
                baseURL,
                uploadImg,
                setUploadImg,
                imgId,
                setImgId,
                sliderC,
                setSliderC,
                sliderBlock,
                setSliderBlock,
                sliderGlobal,
                setSliderGlobal,
                uploadImgfirst,
                setUploadImgfirst,
                uploadImgsecond,
                setUploadImgsecond
            }}>
            {children}
        </FileContext.Provider>
    );
};

export { FileContext, FileContextProvider };