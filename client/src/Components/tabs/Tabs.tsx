import * as React from 'react';
import { useState } from 'react'
import Box from '@mui/material/Box';
import Tab from '@mui/material/Tab';
import TabContext from '@mui/lab/TabContext';
import TabList from '@mui/lab/TabList';
import TabPanel from '@mui/lab/TabPanel';
import FirstTab from './First/FirstTab';
import SecondTab from './Second/SecondTab';
import ThirdTab from './Third/ThirdTab';
import ForthTab from './Forth/ForthTab';

const Tabs = () => {

    const [value, setValue] = useState<string>("1");

    const handleChange = (event: React.SyntheticEvent, newValue: string) => {
        setValue(newValue);
    };

    return (
        <Box sx={{ width: '100%', typography: 'body1' }}>
            <TabContext value={value}>
                <Box sx={{ borderBottom: 1, borderColor: 'divider' }}>
                    <TabList onChange={handleChange} centered>
                        <Tab style={{width:"calc(100% /4 )"}} label="Filters" value="1" />
                        <Tab style={{width:"calc(100% /4 )"}} label="Histograms" value="2" />
                        <Tab style={{width:"calc(100% /4 )"}} label="Frequency" value="3" />
                        <Tab style={{width:"calc(100% /4 )"}} label="Detection" value="4" />
                    </TabList>
                </Box>
                <TabPanel value="1">
                    <FirstTab/>
                </TabPanel>
                <TabPanel value="2">
                    <SecondTab/>
                </TabPanel>
                <TabPanel value="3">
                    <ThirdTab/>
                </TabPanel>
                <TabPanel value="4">
                    <ForthTab/>
                </TabPanel>
            </TabContext>
        </Box>
    )
}

export default Tabs