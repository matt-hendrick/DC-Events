import { Theme } from '@material-ui/core/styles/createTheme';

declare module '@material-ui/core/styles/createTheme' {
  interface Theme {
    classes: object;
  }
  // allow configuration using `createMuiTheme`
  interface ThemeOptions {
    classes?: object;
  }
}
