import App from '../components/app/App'
import Lootbox from '../components/lootbox/Lootbox'

export default {
  app: {
    element: App,
    props: [],
    children: [
      {
        element: Lootbox,
        props: [],
        children: []
      }
    ]
  },
  data: {
    showTreeMap: false,
    products: [
      {
        title: 'Coffee',
        img: 'https://cdn2.iconfinder.com/data/icons/miscellaneous-5/512/coffee-512.png',
        price: '2.18'
      },
      {
        title: 'Cookies',
        img: 'https://cdn2.iconfinder.com/data/icons/miscellaneous-5/512/coffee-512.png',
        price: '2.30'
      },
      {
        title: 'Bananas',
        img: 'https://cdn2.iconfinder.com/data/icons/miscellaneous-5/512/coffee-512.png',
        price: '1.22'
      },
      {
        title: 'Ice Cream',
        img: 'https://cdn2.iconfinder.com/data/icons/miscellaneous-5/512/coffee-512.png',
        price: '4.49'
      },
      {
        title: 'Apples',
        img: 'https://cdn2.iconfinder.com/data/icons/miscellaneous-5/512/coffee-512.png',
        price: '0.99'
      },
      {
        title: 'Candy',
        img: 'https://cdn2.iconfinder.com/data/icons/miscellaneous-5/512/coffee-512.png',
        price: '0.99'
      }
    ],
    recipes: [
      {
        title: 'Vegetable stew',
        url: 'https://google.com'
      },
      {
        title: 'Meaty stew',
        url: 'https://google.com'
      },
      {
        title: 'Fish sticks',
        url: 'https://google.com'
      },
      {
        title: 'Eggs and Bacon',
        url: 'https://google.com'
      },
      {
        title: 'Pasta Ravioli',
        url: 'https://google.com'
      },
      {
        title: 'Fruit salad',
        url: 'https://google.com'
      },
      {
        title: 'Shrimp salad',
        url: 'https://google.com'
      }
    ]
  }
}
