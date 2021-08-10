import './Navbar.css';

// MUI
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';

function Navbar() {
  return (
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h6" className="navbar">
          Events in Washington D.C.
        </Typography>
      </Toolbar>
    </AppBar>
  );
}

export default Navbar;
