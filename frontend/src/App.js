import React, { Component } from 'react';
import axios from 'axios';

class App extends Component{
  state = {
    todos: []
  };


  componentDidMount() {
    console.log('componentDidMount triggered');
    this.getTodos();
  }

  getTodos() {
    axios
      .get('http://localhost:8000/api/')
      .then(res => {
        this.setState({ todos: res.data });
      })
      .catch(err => {
        console.log(err);
      });
  };
  render() {
    return (
      <div>
        {this.state.todos.map(item => (
          <div key={item.id}>
            <h2>{item.title}</h2>
            <span>{item.description}</span>
          </div>
        ))}
      </div>
    );
  }
}

export default App;