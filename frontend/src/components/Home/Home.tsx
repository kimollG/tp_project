import React from 'react'
import './Home.css'
import { connect, ConnectedProps, shallowEqual, useSelector } from 'react-redux'
import { ISpectacleState, SpectacleState } from '../../type'

import Card from '@material-ui/core/Card'
import CardContent from '@material-ui/core/CardContent'
import CardHeader from '@material-ui/core/CardHeader'
import Typography from '@material-ui/core/Typography'
import Container from '@material-ui/core/Container'
import { Link, useHistory } from 'react-router-dom'


const Home = (props: {}) => {
    const history = useHistory();

    const spectacles = useSelector(
        (state: ISpectacleState) => state.spectacles,
        shallowEqual,
    )

    return <Container>
        <div className='SpectaclesContainer'>
            {spectacles.map((spectacle) => <Card className='SpectacleCard' onClick={()=>history.push("/spec")}>
                    <CardHeader className='SpectacleName' title={spectacle.name}/>
                    <CardContent>
                        <Typography className='SpectacleDescription'> {spectacle.description}</Typography>
                    </CardContent>
                </Card>)}
            )
        </div>
    </Container>
}

export {}
export default Home