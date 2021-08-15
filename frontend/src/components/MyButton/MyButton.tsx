import React from 'react';

// MUI
import Button from '@material-ui/core/Button';
import { Theme, makeStyles } from '@material-ui/core';

interface Props {
  children?: React.ReactNode | string;
  onClick?: (event: React.MouseEvent<HTMLButtonElement, MouseEvent>) => void;
}

const useStyles = makeStyles<Theme, object>((theme) => ({
  ...(theme.classes as object),
}));

function MyButton(props: Props) {
  const classes = useStyles({} as object);

  return (
    <Button
      onClick={props.onClick}
      className={classes.myButton}
      color="primary"
      variant="contained"
    >
      {props.children}
    </Button>
  );
}

export default MyButton;
