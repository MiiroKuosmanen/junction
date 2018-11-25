import { dispatch } from '../index'

export const setName = name => dispatch({  
  type: 'SET_NAME',
  name
})

export const setNames = (name1, name2) => dispatch({
  type: 'SET_NAMES',
  name1,
  name2
})

export const toggleTreeMap = treeMap => dispatch({  
  type: 'TOGGLE_TREE_MAP',
  treeMap: treeMap
})
