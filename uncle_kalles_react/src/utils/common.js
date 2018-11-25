import { tap, curry } from 'ramda'

export const log = stuff => tap(console.log(stuff))