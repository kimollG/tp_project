import { takeEvery } from 'redux-saga/effects'

import {fetchSpectacles} from '../api'

function* mySaga(){
    yield takeEvery("", fetchSpectacles)
}

export default mySaga