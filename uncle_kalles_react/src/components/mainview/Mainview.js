import React from 'react';
import './Mainview.css';
import { map } from 'ramda'
import { BarChart } from 'react-easy-chart'
import { toggleTreeMap } from '../../store/actionCreators/example'

const Mainview = ({ recipes, showTreeMap, children }) =>
  <div className="Mainview">
    <div style={{ flex: 1, display: 'flex', flexDirection: 'row' }}>
      <Finance />
      <Nutrients />
      <Profile />
    </div>
    <div style={{ flex: 1, display: 'flex', flexDirection: 'row' }}>
      <FoodCategory showTreeMap={showTreeMap} />
      <Suggestions recipes={recipes} />
    </div>
    <img
        src={'https://i.imgur.com/kGPdlT0.png'}
        className="Lootbox-logo"
        style={{ position: 'absolute', bottom: '25px', right: '25px', height: '75px' }}
        alt="logo" />
    { children }
  </div>

const Profile = ({ children }) =>
  <div className="Profile">
    <img
      src="http://www.memorialsolutions.com/sitemaker/memsol_data/1760/1848633/1848633_profile_pic.jpg"
      style={{ height: '205px' }}/>
    <p>K_customer58</p>
    { children }
  </div>

const Suggestions = ({ recipes, children }) =>
  <div className="Suggestions">
    <h2>Suggestions</h2>
    <ul style={{ paddingLeft: '10%' }}>
      {
        map(
          recipe =>
            <li style={{ paddingTop: '15px' }}>
              <a href={recipe.url}>
                {recipe.title}
              </a>
            </li>
        )(recipes)
      }
    </ul>
    { children }
  </div>

const Finance = ({ children }) =>
  <div className="Finance">
    <h2>Finance</h2>
    <div style={{ flex: 1, display: 'flex', flexDirection: 'row', paddingTop: '15px' }}>
      <span style={{ flex: 1 }}>Most purchased: </span>
      <span style={{ flex: 1 }}>Milk</span>
    </div>
    <div style={{ flex: 1, display: 'flex', flexDirection: 'row', paddingTop: '15px' }}>
      <span style={{ flex: 1 }}>Average spending: (month)</span>
      <span style={{ flex: 1 }}>305 e</span>
    </div>
    <div style={{ flex: 1, display: 'flex', flexDirection: 'row', paddingTop: '15px' }}>
      <span style={{ flex: 1 }}>Customer category: </span>
      <span style={{ flex: 1 }}>Regular</span>
    </div>
    <div style={{ flex: 1, display: 'flex', flexDirection: 'row', paddingTop: '15px' }}>
      <span style={{ flex: 1 }}>Average item price: </span>
      <span style={{ flex: 1 }}>3.6 e</span>
    </div>
    <div style={{ flex: 1, display: 'flex', flexDirection: 'row', paddingTop: '15px' }}>
      <span style={{ flex: 1 }}>Usual shopping time: </span>
      <span style={{ flex: 1 }}>Saturday 15-17</span>
    </div>
    <div style={{ flex: 1, display: 'flex', flexDirection: 'row', paddingTop: '15px' }}>
      <span style={{ flex: 1 }}>Items bought: (0-25e)</span>
      <span style={{ flex: 1 }}>35</span>
    </div>
    <div style={{ flex: 1, display: 'flex', flexDirection: 'row', paddingTop: '15px' }}>
      <span style={{ flex: 1 }}>Items bought: (25-50e)</span>
      <span style={{ flex: 1 }}>12</span>
    </div>
    <div style={{ flex: 1, display: 'flex', flexDirection: 'row', paddingTop: '15px' }}>
      <span style={{ flex: 1 }}>Items bought: (50e +)</span>
      <span style={{ flex: 1 }}>4</span>
    </div>
    {/*
    <div style={{ backgroundColor: 'white', height: '190px', width: '590px', marginTop: 15 }}>
      <BarChart
        axes
        barWidth={20}
        colorBars
        height={200}
        width={600}
        data={[
          {
            x: '0-24',
            y: 35
          },
          {
            x: '25-49',
            y: 12
          },
          {
            x: '50 or more',
            y: 4
          },
        ]}
      />
      </div>
    */}
    { children }
  </div>

const Nutrients = ({ children }) =>
  <div className="Nutrients">
    <h2>Nutrients</h2>
    <div
      style={{ display: 'flex', flexDirection: 'column' }}>
      {/*
      <div style={{ flex: 1, display: 'flex', flexDirection: 'row' }}>
        <span style={{ flex: 1 }}>Food stuff</span>
        <span style={{ flex: 1 }}>0-12</span>
      </div>
      <div style={{ flex: 1, display: 'flex', flexDirection: 'row' }}>
        <span style={{ flex: 1 }}>Food stuff</span>
        <span style={{ flex: 1 }}>0-12</span>
      </div>
      <div style={{ flex: 1, display: 'flex', flexDirection: 'row' }}>
        <span style={{ flex: 1 }}>Food stuff</span>
        <span style={{ flex: 1 }}>0-12</span>
      </div>
      <div style={{ flex: 1, display: 'flex', flexDirection: 'row' }}>
        <span style={{ flex: 1 }}>Food stuff</span>
        <span style={{ flex: 1 }}>0-12</span>
      </div>
      <div style={{ flex: 1, display: 'flex', flexDirection: 'row' }}>
        <span style={{ flex: 1 }}>Food stuff</span>
        <span style={{ flex: 1 }}>0-12</span>
      </div>
      */}
      <div style={{ backgroundColor: 'white', height: '390px', width: '600px' }}>
      <BarChart
        axes
        barWidth={20}
        colorBars
        height={390}
        width={600}
        data={[
          {
            x: 'Fats',
            y: 67
          },
          {
            x: 'Carbs',
            y: 50
          },
          {
            x: 'Proteins',
            y: 23
          },
          {
            x: 'Vitamin C',
            y: 100
          },
          {
            x: 'Vitamin A',
            y: 50
          },
          {
            x: 'Vitamin B',
            y: 26
          },
          {
            x: 'Iron',
            y: 13
          },
          {
            x: 'Zinc',
            y: 20
          },
          {
            x: 'Calsium',
            y: 90
          }
        ]}
      />
      </div>
    </div>
    { children }
  </div>

const FoodCategory = ({ showTreeMap, children }) =>
  <div className="FoodCategory">
    <h2>Food Consumption Profile</h2>
    {
      showTreeMap ?
        <img
          src="https://i.ibb.co/GcYC5NX/mees.png"
          onClick={() => toggleTreeMap(showTreeMap)}
          style={{ height: '340px' }} /> :
        <img
          src="https://www.targetmap.com/ThumbnailsReports/7257_THUMB_IPAD.jpg"
          onClick={() => toggleTreeMap(showTreeMap)}
          style={{ height: '340px' }} />
    }


    { children }
  </div>

export default Mainview;
