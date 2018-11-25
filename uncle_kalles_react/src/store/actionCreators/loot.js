import { dispatch } from '../index'
import Lootcontent from '../../components/lootcontent/Lootcontent';
import Mainview from '../../components/mainview/Mainview';

export const renderLootcontent = () => dispatch({  
  type: 'RENDER_LOOTCONTENT',
  /*component: {
    element: Lootcontent,
    props: [['data', 'products']],
    children: []
  }*/
  component: {
    element: Mainview,
    props: [
      ['data', 'recipes'],
      ['data', 'showTreeMap']
    ],
    children: []
  }

})