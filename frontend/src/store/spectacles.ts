import { SpectacleAction, SpectacleState } from "../type"

const initialSpectacles: SpectacleState = [
    {  
        id: 3,
        loaded: true,
        name: 'The Nutcracker',
        actors: [],
        description: ['Classic ballet by Tchaikovsky']
    },
    {
        id: 4,
        loaded: true,
        name: 'The Nutcracker2',
        actors: [],
        description: ['Classic ballet by Tchaikovsky']
     },
     {
        id: 6,
        loaded: true,
        name: 'The Nutcracker3',
        actors: [],
        description: ['Classic ballet by Tchaikovsky']
     },
     {
        id: 7,
        loaded: true,
        name: 'The Nutcracker4',
        actors: [],
        description: ['Classic ballet by Tchaikovsky']
     },
     {
        id: 10,
        loaded: true,
        name: 'The Nutcracker5',
        actors: [],
        description: ['Classic ballet by Tchaikovsky']
     },
     {
         id: 20,
         loaded: true,
        name: 'The Nutcracker6',
        actors: [],
        description: ['Classic ballet by Tchaikovsky']
     },
     {
         id: 15,
         loaded: true,
        name: 'The Nutcracker7',
        actors: [],
        description: ['Classic ballet by Tchaikovsky']
     }
]

const spectacles = (state: SpectacleState=initialSpectacles, action: SpectacleAction): SpectacleState => {
    switch (action.type) {
        default: return state
        
    }
}

export default spectacles