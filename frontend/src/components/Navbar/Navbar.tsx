import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';

function Navbar() {
  return (
    <div>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6">Events in DC</Typography>
        </Toolbar>
      </AppBar>
    </div>
  );
}

export default Navbar;
