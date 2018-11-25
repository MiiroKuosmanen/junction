import { actionIs, alter } from '../../../utils/state'
import { compose, tap } from 'ramda'

export default [
  [ 
    actionIs('RENDER_LOOTCONTENT'),
    action => compose(
      tap(stuff => console.log(stuff)),
      alter(
        ['app', 'children', 0],
        action.component
      )
    )
  ]
]