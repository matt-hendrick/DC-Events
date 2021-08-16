// MUI
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Link from '@material-ui/core/Link';
import Typography from '@material-ui/core/Typography';
import { Theme, makeStyles } from '@material-ui/core';

interface Props {
  entity: string;
  title: string;
  dateTime: string;
  link: string;
  key: string;
  type: string;
  additionalInfo: string | null;
}

const useStyles = makeStyles<Theme, object>((theme) => ({
  ...(theme.classes as object),
}));

function MyCard({
  entity,
  title,
  dateTime,
  link,
  key,
  type,
  additionalInfo,
}: Props) {
  const classes = useStyles({} as object);
  return (
    <Card className={classes.card} key={key}>
      <CardContent>
        <Typography variant="h5">
          <Link href={link}>{title}</Link>
        </Typography>
        <div className={classes.cardType}>
          <Typography color="secondary" gutterBottom variant="body1">
            {entity}
          </Typography>
          {additionalInfo ? (
            <Typography color="secondary" gutterBottom variant="subtitle1">
              {additionalInfo}
            </Typography>
          ) : null}
        </div>
        <div className={classes.cardType}>
          <Typography color="secondary" variant="subtitle2">
            {dateTime}
          </Typography>
          <Typography color="secondary" variant="overline">
            {type}
          </Typography>
        </div>
      </CardContent>
    </Card>
  );
}

export default MyCard;
