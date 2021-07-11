import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Link from '@material-ui/core/Link';
import Typography from '@material-ui/core/Typography';

interface Children {
  entity: string;
  title: string;
  dateTime: string;
  link: string;
}

function MyCard(children: Children) {
  return (
    <Card>
      <CardContent>
        <Typography color="textSecondary" gutterBottom>
          {children.entity}
        </Typography>
        <Typography variant="h5" component="h2">
          <Link href={children.link}>{children.title}</Link>
        </Typography>
        <Typography color="textSecondary">{children.dateTime}</Typography>
      </CardContent>
    </Card>
  );
}

export default MyCard;
