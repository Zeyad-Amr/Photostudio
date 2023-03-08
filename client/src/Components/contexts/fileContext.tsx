import { createContext, useState } from 'react';
const FileContext = createContext<unknown | any>('');

const FileContextProvider = ({ children } : any) => {

    // input img component
    const baseURL: string = 'http://localhost:8000' 
    const [uploadImg,setUploadImg] = useState<String | undefined>('')
    const [imgId,setImgId] = useState<String | undefined>('')

    return (
        <FileContext.Provider
            value={{ 
                baseURL,
                uploadImg,
                setUploadImg,
                imgId,
                setImgId
            }}>
            {children}
        </FileContext.Provider>
    );
};

export { FileContext, FileContextProvider };