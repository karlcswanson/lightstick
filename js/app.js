"use strict";

import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

import '../css/style.scss';
// import '../node_modules/@ibm/plex/css/ibm-plex.css';

import React from 'react';
import ReactDOM from 'react-dom';


import { PresetChooser } from './presetchooser.js';
import { Preset } from './preset.js';

class SettingsPage extends React.Component {
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
    fetch("api/preset")
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            isLoaded: true,
            presets: result.presets,
            current_preset: result.current_preset
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
    const { error, isLoaded, presets } = this.state;
    if (error) {
      return <div>Error: {error.message}</div>;
    } else if (!isLoaded) {
      return <div>Loading...</div>;
    } else {
      return (
        <div>
          <PresetChooser presets={this.state.presets} current_preset={this.state.current_preset} />
          <PresetList presets={this.state.presets} />
        </div>
        
      );
    }
  }
}

class PresetList extends React.Component {
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




const App = () => (
  <div>
  <h1>Preset List</h1>
    {/* <PresetChooser /> */}
    <SettingsPage />
  </div>
)

ReactDOM.render(<App/>, document.getElementById('root'));