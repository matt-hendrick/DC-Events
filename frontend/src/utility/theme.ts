const colors = {
  primary: {
    light: '#FF6B6B',
    main: '#B61919',
    dark: '#03045e',
    contrastText: '#fff',
  },
  secondary: {
    light: '#e5383b',
    main: '#012443',
    dark: '#660708',
    contrastText: '#fff',
  },
};

const theme = {
  palette: colors,
  classes: {
    button: {
      '&:hover': {
        backgroundColor: colors.primary.light,
      },
    },
  },
};

export default theme;
