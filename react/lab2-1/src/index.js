import React from 'react';
import { createRoot } from 'react-dom/client';

function getTime() {
  const now = new Date();
  return now.toLocaleTimeString('en-US');
}

const App = () => {
  return (
    <div>
      <div>Current Time:</div>
      <h3>{ getTime() }</h3>
    </div>
  );
}

const root = createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
