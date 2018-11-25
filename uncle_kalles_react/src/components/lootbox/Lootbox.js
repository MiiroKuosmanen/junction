import React from 'react';
import './Lootbox.css';
import { renderLootcontent } from '../../store/actionCreators/loot'
import logo from '../../assets/logo.svg'

const Lootbox = ({ children }) =>
  <div
    className="Lootbox"
    onClick={() => renderLootcontent()}>
    <header className="Lootbox-header">
      <img
        src={'https://i.imgur.com/kGPdlT0.png'}
        className="Lootbox-logo"
        alt="logo" />
    </header>
    { children }
  </div>

export default Lootbox;
