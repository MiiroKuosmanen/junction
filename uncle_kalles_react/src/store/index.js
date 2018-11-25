import { Subject } from 'rxjs';
import { startWith, scan } from 'rxjs/operators';
import initialState from './initialState'
import { cond } from 'ramda'
import actionsToStates from './actionsToStates'

const reducer = (acc, cur) => cond(actionsToStates)(cur)(acc)

const action$ = new Subject();

const state$ = action$.pipe(
  startWith(initialState),
  scan(reducer)
)

export const dispatch = action => 
  action$.next(action);

export default state$