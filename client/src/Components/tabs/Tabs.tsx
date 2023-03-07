import * as React from 'react';
import { useState } from 'react'
import Box from '@mui/material/Box';
import Tab from '@mui/material/Tab';
import TabContext from '@mui/lab/TabContext';
import TabList from '@mui/lab/TabList';
import TabPanel from '@mui/lab/TabPanel';
import Inputimg from '../inputImg/Inputimg';

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
                        <Tab style={{width:"calc(100% /3 )"}} label="Item One" value="1" />
                        <Tab style={{width:"calc(100% /3 )"}} label="Item Two" value="2" />
                        <Tab style={{width:"calc(100% /3 )"}} label="Item Three" value="3" />
                    </TabList>
                </Box>
                <TabPanel value="1">
                    <Inputimg/>
                </TabPanel>
                <TabPanel value="2">Item Two</TabPanel>
                <TabPanel value="3">Item Three</TabPanel>
            </TabContext>
        </Box>
    )
}

export default Tabs