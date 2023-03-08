import { useState } from 'react';
import { Col, Container, Row } from 'react-bootstrap'
import Inputimg from '../../inputImg/Inputimg'
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select, { SelectChangeEvent } from '@mui/material/Select';

const FirstTab = () => {

  const [selectionMode, setSelectionMode] = useState<string>('');
  const [firstTabOptions, setFirstTabOptions] = useState<string>('');

  console.log(selectionMode)
  console.log(firstTabOptions)

  const handleChangeSelection = (event: SelectChangeEvent) => {
    setSelectionMode(event.target.value);
  };

  const handleChangeOptions = (event: SelectChangeEvent) => {
    setFirstTabOptions(event.target.value);
  };

  return (
    <Container fluid>
      <Row>
        <Col style={{ height: "85vh", display: "flex", flexDirection: "column",  justifyContent: "center", alignItems: "center" }} lg={4} md={6} sm={12} xs={12}>
          <Inputimg />
        </Col>
        <Col style={{ height: "85vh", display: "flex", flexDirection: "column",  justifyContent: "center", alignItems: "center" }} lg={4} md={6} sm={12} xs={12}>
          {/* selection mode */}
          <FormControl style={{ marginBottom: "2rem",width : "13rem"}} variant="standard" sx={{ m: 1, minWidth: 150 }}>
            <InputLabel id="demo-simple-select-autowidth-label">Choose mode</InputLabel>
            <Select
              labelId="demo-simple-select-autowidth-label"
              id="demo-simple-select-autowidth"
              value={selectionMode}
              onChange={handleChangeSelection}
              autoWidth
            >
              <MenuItem value="0">
                <em>None</em>
              </MenuItem>
              <MenuItem value="1">Noise</MenuItem>
              <MenuItem value="2">Filter</MenuItem>
              <MenuItem value="3">Edges Detection</MenuItem>
            </Select>
          </FormControl>
          {
            selectionMode === "1" ?
              // noise selection
              <FormControl style={{ marginBottom: "2rem",width : "13rem"}} variant="standard" sx={{ m: 1, minWidth: 150 }}>
                <InputLabel id="demo-simple-select-autowidth-label">Choose noise</InputLabel>
                <Select
                  labelId="demo-simple-select-autowidth-label"
                  id="demo-simple-select-autowidth"
                  value={firstTabOptions}
                  onChange={handleChangeOptions}
                  autoWidth
                >
                  <MenuItem value="0">
                    <em>None</em>
                  </MenuItem>
                  <MenuItem value="1">Uniform</MenuItem>
                  <MenuItem value="2">Gaussian</MenuItem>
                  <MenuItem value="3">Salt & Pepper</MenuItem>
                </Select>
              </FormControl>
              : selectionMode === "2" ?
                // filter selection
                <FormControl style={{ marginBottom: "2rem",width : "13rem"}} variant="standard" sx={{ m: 1, minWidth: 150 }}>
                  <InputLabel id="demo-simple-select-autowidth-label">Choose filter</InputLabel>
                  <Select
                    labelId="demo-simple-select-autowidth-label"
                    id="demo-simple-select-autowidth"
                    value={firstTabOptions}
                    onChange={handleChangeOptions}
                    autoWidth
                  >
                    <MenuItem value="0">
                      <em>None</em>
                    </MenuItem>
                    <MenuItem value="4">Average</MenuItem>
                    <MenuItem value="5">Gaussian</MenuItem>
                    <MenuItem value="6">Median</MenuItem>
                  </Select>
                </FormControl>
                : selectionMode === "3" ?
                  // edges detection selection
                  <FormControl style={{ marginBottom: "2rem",width : "13rem"}} variant="standard" sx={{ m: 1, minWidth: 150 }}>
                    <InputLabel id="demo-simple-select-autowidth-label">Choose edge detectors</InputLabel>
                    <Select
                      labelId="demo-simple-select-autowidth-label"
                      id="demo-simple-select-autowidth"
                      value={firstTabOptions}
                      onChange={handleChangeOptions}
                      autoWidth
                    >
                      <MenuItem value="0">
                        <em>None</em>
                      </MenuItem>
                      <MenuItem value="7">Sobel</MenuItem>
                      <MenuItem value="8">Roberts</MenuItem>
                      <MenuItem value="9">Prewitt</MenuItem>
                      <MenuItem value="10">Canny</MenuItem>
                    </Select>
                  </FormControl>
                  : null
          }
        </Col>
        <Col style={{ height: "85vh", display: "flex", flexDirection: "column",  justifyContent: "center", alignItems: "center" }} lg={4} md={12} sm={12} xs={12}>
          <label className='output-label'>Output</label>
          <div className='output-img-contain'>
            <img className='output-img' src="" alt="" />
          </div>
        </Col>
      </Row>
    </Container>
  )
}

export default FirstTab