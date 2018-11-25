import React from 'react';
import ReactDOM from 'react-dom';
import Lootbox from './Lootbox';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<Lootbox />, div);
  ReactDOM.unmountComponentAtNode(div);
});
