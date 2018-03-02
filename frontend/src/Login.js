import React from 'react'

const HEADERS = {
  'Accept': 'application/json',
  'Content-Type': 'application/json'
};
export default class extends React.Component {

  state = {
    email: '',
    password: '',
    errors: undefined
  };

  changeFormField = e => {
    this.setState({[e.target.name]: e.target.value});
  };

  submitForm = e => {
    e.preventDefault();
    const {errors: _, ...data} = this.state;
    fetch('/api/login', {
      headers: HEADERS,
      method: "POST",
      body: JSON.stringify(data)
    })
    .then(async response => {
      if (response.status === 200) {
        const {access_token, refresh_token} = await response.json();
        localStorage.setItem('access_token', access_token);
        localStorage.setItem('refresh_token', refresh_token);
        this.props.history.push('/');
      } else {
        throw new Error();
      }
    })
    .catch(errors => this.setState({errors}))
  };

  renderErrors() {
    return this.state.errors ? <small style={{color: 'red'}}><br/>Invalid username or password</small> : false
  }

  render() {
    return (
      <form onSubmit={this.submitForm}>
        <input name="email" placeholder="Email" type="email" onChange={this.changeFormField}/>
        <input name="password" placeholder="Password" type="password" onChange={this.changeFormField}/>
        <button type="submit">Log in</button>
        {this.renderErrors()}
      </form>
    );
  }
};