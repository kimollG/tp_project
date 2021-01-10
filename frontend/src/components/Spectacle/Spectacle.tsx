import React from 'react'
import { useSelector } from 'react-redux';
import { useParams } from 'react-router-dom';
import { ISpectacle, ISpectacleState, SpectacleState } from '../../type';
import Error from '../common/error'


const Spectacle = ({}) => {
    const params: {id? : string} = useParams();
    const id = params.id !== undefined ? parseInt(params.id): -1;

    const spectacle = useSelector(
        (state: ISpectacleState) => state.spectacles.find(spec => spec.id === id)
    )

    if (spectacle === undefined)
        return <Error code={404} name={"No such article"} />
    else
        return <div>
            <div>
                {spectacle.name}
            </div>
            <div>
                <div>
                    {spectacle.description}
                </div>
                <div>
                    {spectacle.actors}
                </div>
            </div>[2]
        </div>

}

export default Spectacle