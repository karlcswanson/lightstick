"use strict";

import React from 'react';

import { PresetChooser } from './presetchooser.js';
import { PresetList } from './presetlist.js';



export class SettingsPage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      isLoaded: false,
      presets: [],
      current_preset: ''
    };
  }

  componentDidMount() {
    fetch("data")
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            isLoaded: true,
            presets: result.config.presets,
            current_preset: result.config.current_preset
          });
        },
        // Note: it's important to handle errors here
        // instead of a catch() block so that we don't swallow
        // exceptions from actual bugs in components.
        (error) => {
          this.setState({
            isLoaded: true,
            error
          });
        }
      )
  }

  render() {
    const { error, isLoaded, presets, current_preset } = this.state;
    if (error) {
      return <div>Error: {error.message}</div>;
    } else if (!isLoaded) {
      return <div>Loading...</div>;
    } else {
      return (
        <div className="settings">
          <h1>Settings</h1>
          <PresetChooser presets={this.state.presets} current_preset={this.state.current_preset} />
          <PresetList presets={this.state.presets} />
        </div>
        
      );
    }
  }
}