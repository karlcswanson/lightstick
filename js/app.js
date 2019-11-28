"use strict";

import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

import '../css/style.scss';
import '../css/colors.scss';
import '../node_modules/@ibm/plex/css/ibm-plex.css';

import React from 'react';
import ReactDOM from 'react-dom';

import CssBaseline from '@material-ui/core/CssBaseline';
import Container from '@material-ui/core/Container';


import { SettingsPage } from './settings.js';


const App = () => (
  <React.Fragment>
    <CssBaseline />
    <Container maxWidth="sm">
    <div>
      <SettingsPage />
    </div>
    </Container>
  </React.Fragment>
  
  
)

ReactDOM.render(<App/>, document.getElementById('root'));