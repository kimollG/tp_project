import { Url } from "url";

interface IHall {

}

interface ITheatre {

}

type DescriptionElement = string | IImage

interface IImage {
    url: Url,
    alt: string,
    caption: string
}

interface ISpectacle {
    id: number,
    loaded: boolean,
    name?: string,
    actors?: IActor[],
    description?: DescriptionElement[]
}

interface IActor {
    id: number,
    loaded: boolean,
    name?: string,
    surname?: string,
    age?: number,
}

type SpectacleState = ISpectacle[];

interface ISpectacleState {
    spectacles: SpectacleState 
}

type SpectacleAction = {
    spectacle: ISpectacle,
    type: string
}

type ActorAction = {
    actor: IActor,
    type: string
}