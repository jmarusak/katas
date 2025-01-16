import React from 'react';
import { createRoot } from 'react-dom/client';

import Message from './Message';

const App = () => {
  return (
    <div>
      <Message header="Attention!" text="We did an update." />
    </div>
  );
}

const root = createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
