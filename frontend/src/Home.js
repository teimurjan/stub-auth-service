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
    const queryParams = `access_token=${
      localStorage.getItem('access_token')
      }&refresh_token=${
      localStorage.getItem('refresh_token')
      }`;
    return (
      <ul>
        <li>
          <a href={`${this.state.uniformUrl}login?${queryParams}`}>
            Uniform
          </a>
        </li>
      </ul>
    );
  }
}