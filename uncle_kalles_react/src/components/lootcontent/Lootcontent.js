import React from 'react';
import './Lootcontent.css';
import { map, compose, sum } from 'ramda'

const Lootcontent = ({ products, children }) =>
  <div className="Lootcontent">
    <div
      className="Loot-items">
      {
        map(renderItem, products)
      }
      <div />
      <button className="buy-btn">
        {/*<img
          src="https://banner2.kisspng.com/20180319/gze/kisspng-money-bag-computer-icons-coin-clip-art-bag-money-icon-5ab0668de1ff52.0329834815215100299257.jpg"
        style={{ height: 70 }}/>*/}
        { overallCost(products) }
      </button>
    </div>
    { children }
  </div>

const renderItem = item => 
  <div className="Loot-item" key={item.title}>
    <img className="Item-icon" src={item.img} />
    <div className="Item-description">
      <div style={{ maxWidth: '30vw' }}>{item.title}</div>
      <br style={{ height: 1 }}/>
      {item.price}
    </div>
  </div>

const overallCost = compose(
  num => num.toPrecision(4),
  sum,
  map(item => Number(item.price))
)

export default Lootcontent;