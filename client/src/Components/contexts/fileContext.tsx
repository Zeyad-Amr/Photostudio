import { createContext, useState } from 'react';
const FileContext = createContext<any>('');

const FileContextProvider = ({ children } : any) => {

    // input img component
    const [uploadImg,setUploadImg] = useState<String | undefined>('')

    return (
        <FileContext.Provider
            value={{ 
                uploadImg,
                setUploadImg
            }}>
            {children}
        </FileContext.Provider>
    );
};

export { FileContext, FileContextProvider };