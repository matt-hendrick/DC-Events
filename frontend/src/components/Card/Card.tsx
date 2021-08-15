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
  type: string;
}

function MyCard({ entity, title, dateTime, link, key, type }: Props) {
  return (
    <Card className="card" key={key}>
      <CardContent>
        <Typography variant="h5">
          <Link href={link}>{title}</Link>
        </Typography>
        <Typography color="textSecondary" gutterBottom variant="body1">
          {entity}
        </Typography>
        <div className="card-type">
          <Typography color="textSecondary" variant="subtitle2">
            {dateTime}
          </Typography>
          <Typography color="textSecondary" variant="overline">
            {type}
          </Typography>
        </div>
      </CardContent>
    </Card>
  );
}

export default MyCard;
