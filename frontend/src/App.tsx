import React from 'react';
import logo from './logo.svg';
import './App.css';
import Front from './main/common/front'
import Signin from './main/auth/signin';
import Home from './components/Home/Home';
import Spectacle from './components/Spectacle/Spectacle'
import {
  BrowserRouter as Router,
  Route,
  Switch,
} from 'react-router-dom'
import { createBrowserHistory } from 'history';

const history = createBrowserHistory();
function App() {
  return (
    
      <div className="App">
        <Router>
          <Switch>
            <Route path="/" exact>
              <Home/>
            </Route>
            <Route path="/spec/:id">
              <Spectacle/>
            </Route>
          </Switch>
        </Router>
        </div>
  );
}

export default App;
