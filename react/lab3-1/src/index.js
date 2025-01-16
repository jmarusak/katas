import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import UserForm from './UserForm';

const App = () => {
  return (
    <div>
      <UserForm />
    </div>
  );
}

const root = createRoot(document.getElementById('root'));
root.render(
  <StrictMode>
    <App />
  </StrictMode>
);
