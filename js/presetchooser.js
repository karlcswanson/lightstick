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
  }
  
  render() {
    return(
      <div>
        <label>Current Preset:</label>
          <select>
            {
              this.state.presets.map(preset =>
              <option key={preset.preset} value={preset.preset}>{preset.preset}: {preset.title}</option>
              )
            }
          </select>
      </div>
    );
  }
}

export default PresetChooser