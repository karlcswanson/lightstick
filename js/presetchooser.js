"use strict";

import React from 'react';
import ReactDOM from 'react-dom';

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
      <div>
        <label>Current Preset:</label>
          <select name="current_preset" value={this.state.current_preset} onChange={this.handleInputChange} >
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
          </select>
      </div>
    );
  }
}

export default PresetChooser