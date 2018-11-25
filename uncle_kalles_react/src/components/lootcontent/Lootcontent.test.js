import React from 'react';
import ReactDOM from 'react-dom';
import Lootcontent from './Lootcontent';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<Lootcontent />, div);
  ReactDOM.unmountComponentAtNode(div);
});
