import React from 'react';


export default class extends React.Component {
  state = {
    uniformUrl: ''
  };

  componentDidMount() {
    fetch('/uniform_base_url')
    .then(response => response.text())
    .then(url => this.setState({ uniformUrl: url }))
    .catch(() => console.error('Couldn\'t fetch uniform base url'));
  }

  render() {
    return (
      <ul>
        <li>
          <a href={`${this.state.uniformUrl}/login?token=${localStorage.getItem('access_token')}`}>
            Uniform
          </a>
        </li>
      </ul>
    );
  }
}