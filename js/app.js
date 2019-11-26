"use strict";

import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

import '../css/style.scss';
// import '../node_modules/@ibm/plex/css/ibm-plex.css';

import React from 'react';
import ReactDOM from 'react-dom';
import { SketchPicker } from 'react-color';


function colorMap(color) {
  return {'r': color[0], 'g': color[1], 'b': color[2]};
}

function reverseColorMap(color) {
  return [ color['r'], color['g'], color['b']];
}

class PresetList extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      isLoaded: false,
      presets: []
    };
  }

  componentDidMount() {
    fetch("api/preset")
      .then(res => res.json())
      .then(
        (result) => {
          this.setState({
            isLoaded: true,
            presets: result.presets
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
        <div className="preset-list">
          {presets.map(preset => (
            <Preset key={preset.preset} preset={preset} />
          ))}
        </div>
      );
    }
  }
}

class Preset extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      title: this.props.preset.title,
      attack: this.props.preset.attack,
      decay: this.props.preset.decay,
      note_off: colorMap(this.props.preset.note_off),
      note_on: colorMap(this.props.preset.note_on)
    };
  

    this.handleInputChange = this.handleInputChange.bind(this);
  }
  
  
  handleChange(event) {
    console.log(this.state)
    this.setState({[event.target.name]: event.target.value});
    // console.log(event);
  }

  handleSubmit(event) {
    event.preventDefault();
    this.postData();
  }

  postData() {
    let url = "api/preset";
    let data = {
      preset: this.props.preset.preset,
      title: this.state.title,
      attack: parseFloat(this.state.attack),
      decay: parseFloat(this.state.decay),
      note_off: reverseColorMap(this.state.note_off),
      note_on: reverseColorMap(this.state.note_on)
    };
    fetch(url, {
      method:'POST',
      body: JSON.stringify(data)
    }).then(/* ... */)
  }
  


  handleColorChange(name, event) {
    
    const color = event['rgb']
    const out = [color['r'], color['g'], color['b']];
    console.log("name: " + name + " color: "+ out)
    console.log(out)
    this.setState({
      [name]: color
    });
    console.log(this.state)
    this.postData()
  }


  handleInputChange(event) {
    const target = event.target;
    const value = target.type === 'checkbox' ? target.checked : target.value;
    const name = target.name;
    console.log("name:" + name + " val: " + value);
    this.setState({
      [name]: value
    });
    setTimeout(() => {
      this.postData();
      console.log(this.state)
    }, 125);
    
  }



  render() {
    return (
      <div className="preset">
        <form onSubmit={this.handleSubmit}>
          <input
            name="title"
            autoComplete="off"
            value={this.state.title}
            onChange={this.handleInputChange}
          />
          <label>Attack:</label>
          <input
            name="attack"
            autoComplete="off"
            value={this.state.attack}
            onChange={this.handleInputChange}
          />
          <label>Decay:</label>
          <input
            name="decay"
            autoComplete="off"
            value={this.state.decay}
            onChange={this.handleInputChange}
          />
          {/* <input type="submit" value="Submit" /> */}
        </form>
        
        <label>Note Off</label>
        <SketchPicker
          name="note_off"
          color={this.state.note_off}
          onChangeComplete={ (e) => this.handleColorChange('note_off', e) }
        />
        <label>Note On</label>
        <SketchPicker
          name="note_on"
          color={this.state.note_on}
          onChangeComplete={ (e) => this.handleColorChange('note_on', e) }
        />
      </div>
    );
  }
}


const App = () => (
  <div>
  <h1>Preset List</h1>
    <PresetList />
  </div>
)

ReactDOM.render(<App/>, document.getElementById('root'));