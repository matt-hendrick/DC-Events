import './Card.css';

import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Link from '@material-ui/core/Link';
import Typography from '@material-ui/core/Typography';

interface Props {
  entity: string;
  title: string;
  dateTime: string;
  link: string;
  key: string;
}

function MyCard(props: Props) {
  return (
    <Card className="card" key={props.key}>
      <CardContent>
        <Typography variant="h5">
          <Link href={props.link}>{props.title}</Link>
        </Typography>
        <Typography color="textSecondary" gutterBottom variant="body1">
          {props.entity}
        </Typography>
        <Typography color="textSecondary" variant="subtitle2">
          {props.dateTime}
        </Typography>
      </CardContent>
    </Card>
  );
}

export default MyCard;
