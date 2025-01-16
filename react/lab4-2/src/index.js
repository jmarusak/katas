import { Component, StrictMode } from 'react';
import { createRoot } from 'react-dom/client';

const users = [
  {id: 1, name: 'Albert Lam'},
  {id: 2, name: 'Frances Wu'},
  {id: 3, name: 'John Smith'},
  {id: 4, name: 'Jaden Wong'},
]

class App extends Component {
  renderListItems() {
    const listItems = users.map((user) => {
      return <li key={user.id}>{user.name}</li>;
    });
    return listItems;
  }

  render() {
    return (
     <ul>
       {this.renderListItems()}
     </ul>
    );
  }
}

const root = createRoot(document.getElementById('root'));
root.render(
  <StrictMode>
    <App />
  </StrictMode>
);
