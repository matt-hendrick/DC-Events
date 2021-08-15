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
  homeBackground: '#fafafa',
};

const theme = {
  palette: colors,
  classes: {
    // Home
    homeWrapperDiv: {
      backgroundColor: colors.homeBackground,
      minHeight: '100vh',
    },
    homeMainContainer: {
      paddingTop: '5vh',
      paddingBottom: '5vh',
    },
    homeButtonContainer: {
      paddingBottom: '5vh',
      display: 'flex',
      justifyContent: 'center',
    },
    // Card
    card: {
      border: `1px ${colors.secondary.main} solid`,
    },
    cardType: {
      display: 'flex',
      justifyContent: 'space-between',
    },
    // MyButton
    myButton: {
      margin: '.5vw',
      '&:hover': {
        backgroundColor: colors.primary.light,
      },
    },
  },
};

export default theme;
