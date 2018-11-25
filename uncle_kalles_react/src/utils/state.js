import { equals, compose, set, lensPath, prop, last } from 'ramda'

// Use 'alter' when changing multiple values from state
export const alter = (path, value) => set(lensPath(path), value)
export const replace = path => action => set(lensPath(path), prop(last(path))(action))
export const actionIs = target => compose(equals(target), prop('type')) 