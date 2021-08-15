// Theme
import { ThemeProvider, createMuiTheme } from '@material-ui/core/styles';
import themeObject from './utility/theme';

// Components
import Navbar from './components/Navbar/Navbar';

// Pages
import Home from './pages/Home/Home';

const theme = createMuiTheme(themeObject);

function App() {
  return (
    <ThemeProvider theme={theme}>
      <Navbar />
      <Home />
    </ThemeProvider>
  );
}

export default App;
