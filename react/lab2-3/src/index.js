import React from 'react';
import { createRoot } from 'react-dom/client';

import Segment from './Segment';

const App = () => {
  return (
    <div>
      <Segment>
        <div className="ui icon header">
          <i className="pdf file outline icon"></i>
          No documents are listed for this customer.
        </div>
        <div className="ui primary button">Add Document</div>
      </Segment>
      <Segment>
        <div className="ui icon header">
          <h4 className="ui header">For your Information</h4>
         </div>
         <p>This is testing the segment coding</p>
      </Segment>
    </div>
  );
}

const root = createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
