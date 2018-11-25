import { reduce, flip, concat, T, identity } from 'ramda'
import modules from './modules'

const fallback = [[ T, identity ]]
const combine = reduce(flip(concat), fallback)

export default combine(modules)