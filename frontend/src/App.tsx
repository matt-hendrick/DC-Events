import { Fragment } from 'react';
import './App.css';

// Components
import Navbar from './components/Navbar/Navbar';

// Pages
import Home from './pages/Home/Home';

function App() {
  return (
    <Fragment>
      <Navbar />
      <div className="app-home">
        <Home />
      </div>
    </Fragment>
  );
}

export default App;
