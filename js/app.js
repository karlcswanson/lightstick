"use strict";

import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

import '../css/style.scss';
import '../css/colors.scss';
import '../node_modules/@ibm/plex/css/ibm-plex.css';

import React from 'react';
import ReactDOM from 'react-dom';

import { SettingsPage } from './settings.js';


const App = () => (
  <div>
    <SettingsPage />
  </div>
)

ReactDOM.render(<App/>, document.getElementById('root'));