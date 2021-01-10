import { ActorAction, IActor } from "../type";

const initialActors: IActor[] = [
    {
        id: 20,
        loaded: true,
        name: 'Petr',
        surname: 'Ivanov',
        age: 45
    },
    {
        id: 23,
        loaded: true,
        name: 'Anna',
        surname: 'Pavlova',
        age: 38
    }
]

const actors = (state: IActor[]=initialActors, action: ActorAction): IActor[] => {
    return state
}

export default actors