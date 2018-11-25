import React from 'react';
import state$ from '../store'
import { buildApp } from '../utils/rendering'

class AppContainer extends React.Component {
  constructor(props) {
    super(props)
    this.state = {}
  }
  
  componentDidMount() {
    state$.subscribe(newState => this.setState(newState))
  }

  render() {
    return buildApp(this.state)
  }
}

export default AppContainer

