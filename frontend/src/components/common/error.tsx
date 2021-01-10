import React from 'react'


type Props = {
    code: number,
    name: string,
    description?: string,
}
const Error = (props: Props) => {
    return <div>
        <div>Error {props.code}</div>
        <div>{props.name}</div>
        <div>{props.description}</div>
    </div>
}

export default Error