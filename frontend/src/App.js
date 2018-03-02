import React, {Component} from 'react';
import {Redirect, Route, Switch} from "react-router-dom";
import Home from "./Home";
import Login from "./Login";

class App extends Component {
  render() {
    return (
      <div className="App">
        <Switch>
          <PrivateRoute exact path='/' component={Home}/>
          <Route exact path='/login' component={Login}/>
        </Switch>
      </div>
    );
  }
}

const PrivateRoute = ({component: Component, ...rest}) => {
  const isAuthenticated = localStorage.getItem('access_token') !== null;
  const renderChild = props => isAuthenticated ?
    <Component {...props} /> :
    <Redirect to={{pathname: "/login"}}/>;
  return (
    <Route {...rest} render={renderChild}
    />
  )
};

export default App;
