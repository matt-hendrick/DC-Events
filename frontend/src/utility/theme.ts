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
    home: {
      paddingTop: '5vh',
      paddingBottom: '5vh',
    },
    homeButtonContainer: {
      paddingBottom: '5vh',
      display: 'flex',
      justifyContent: 'center',
    },
    card: {
      border: `1px ${colors.secondary.main} solid`,
    },
    cardType: {
      display: 'flex',
      justifyContent: 'space-between',
    },
    myButton: {
      '&:hover': {
        backgroundColor: colors.primary.light,
      },
    },
  },
};

export default theme;
