import { combineReducers } from "redux"
import spectacles from './spectacles'
import actors from './actors'


export const reducer = combineReducers({spectacles, actors})