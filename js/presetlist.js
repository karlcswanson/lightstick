"use strict";

import React from 'react';

import { Preset } from './preset.js';

export class PresetList extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      presets: this.props.presets
    };
  }



  render() {
    return (
      <div className="preset-list">
        {this.state.presets.map(preset => (
          <Preset key={preset.preset} preset={preset} />
        ))}
      </div>
    );
  }
}