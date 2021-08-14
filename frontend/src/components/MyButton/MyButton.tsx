import React from 'react';

// MUI
import Button from '@material-ui/core/Button';

interface Props {
  children?: React.ReactNode | string;
  onClick?: (event: React.MouseEvent<HTMLButtonElement, MouseEvent>) => void;
}

function MyButton(props: Props) {
  return (
    <Button onClick={props.onClick} color="primary" variant="contained">
      {props.children}
    </Button>
  );
}

export default MyButton;
