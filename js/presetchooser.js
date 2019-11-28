"use strict";

import React from 'react';
import ReactDOM from 'react-dom';

import InputLabel from '@material-ui/core/InputLabel';
import FormControl from '@material-ui/core/FormControl';
import NativeSelect from '@material-ui/core/NativeSelect';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';


export class PresetChooser extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      presets: this.props.presets,
      current_preset: this.props.current_preset
    }
    this.handleInputChange = this.handleInputChange.bind(this);
  }


  postData() {
    console.log("posting" + this.state)
    let url = "api/preset_select";
    let data = {
      current_preset: this.state.current_preset,
    };
    fetch(url, {
      method:'POST',
      body: JSON.stringify(data)
    }).then(/* ... */)
  }
  

  handleInputChange(event) {
    console.log(event.target.value)
    
    this.setState({
      current_preset: event.target.value
    });
    console.log(this.state)
    setTimeout(() => {
      this.postData();
      console.log(this.state)
    }, 125);
  }

  render() {
    return(
      <Card>
        <CardContent>
          <FormControl>
            <InputLabel shrink>Current Preset</InputLabel>
            <NativeSelect
              name="current_preset"
              value={this.state.current_preset}
              onChange={this.handleInputChange}
            >
              {
                
                this.state.presets.map(preset =>
                  <option
                    // selected={this.state.current_preset == preset.preset}
                    key={preset.preset}
                    value={preset.preset}>
                      {preset.preset}: {preset.title}
                  </option>
                )
              }
            </NativeSelect>
          </FormControl>
        </CardContent>
      </Card>
      
    );
  }
}

export default PresetChooser