import './App.css';
import Navbar from './components/Navbar';
import { BrowserRouter as Router } from "react-router-dom";
import Routs from './routes/Routs';

function App() {
  return (
    <div className="App">
        <Router>
          <Navbar />
          <Routs />
        </Router>
    </div>
  );
}

export default App;