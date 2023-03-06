import { createContext, useState } from 'react';
const FileContext = createContext();

const FileContextProvider = ({ children }) => {

    // input img component
    const [uploadImg,setUploadImg] = useState<String>('')

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