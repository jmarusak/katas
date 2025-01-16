import { Component, StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import Validator from './Validator';

class App extends Component {
  render() {
    return (
      <div>
        <Validator />
      </div>
    );
  }
}

const root = createRoot(document.getElementById('root'));
root.render(
  <StrictMode>
    <App />
  </StrictMode>
);
