"use strict";

import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

import '../css/style.scss';
import '../node_modules/@ibm/plex/css/ibm-plex.css';

import React from 'react';
import ReactDOM from 'react-dom';
import { SketchPicker } from 'react-color';

// class ShoppingList extends React.Component {
//     render() {
//       return (
//         <div className="shopping-list">
//           <h1>Shopping List for {this.props.name}</h1>
//           <ul>
//             <li>Instagram</li>
//             <li>WhatsApp</li>
//             <li>Oculus</li>
//           </ul>
//         </div>
//       );
//     }
//   }

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
  render() {
    return (
      <div className="preset">
        <h3>Preset: {this.props.preset.title}</h3>
        <p>Attack: {this.props.preset.attack}</p>
        <p>Release: {this.props.preset.release}</p>

        <SketchPicker  />
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