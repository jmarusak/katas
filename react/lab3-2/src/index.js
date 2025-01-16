import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import Clock from './Clock';

const App = () => {
  return (
    <div>
      <Clock />
    </div>
  );
}

const root = createRoot(document.getElementById('root'));
root.render(
  <StrictMode>
    <App />
  </StrictMode>
);
