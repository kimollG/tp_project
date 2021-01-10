import React from 'react'
import {connect, ConnectedProps } from 'react-redux'

interface RootState {
    username: string,
    isLogged: boolean
}

const mapState = (state: RootState) => ({...state})

const mapDispatch = {

}

const connector = connect(mapState, mapDispatch)

type PropFromRedux = ConnectedProps<typeof connector>
type Props = PropFromRedux & {

}

const Signin = (props: Props) => {
    return <div>
        <form>
            <input type="text"/>
            <input type="password"/>
        </form>
    </div>
}

export default connector(Signin)