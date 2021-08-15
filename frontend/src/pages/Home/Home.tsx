import { useState, useEffect } from 'react';

// Axios
import axios from 'axios';

// MUI
import Container from '@material-ui/core/Container';
import LinearProgress from '@material-ui/core/LinearProgress';
import { Theme, makeStyles } from '@material-ui/core';

// Components
import Card from '../../components/Card/Card';
import MyButton from '../../components/MyButton/MyButton';

interface Event {
  entity: string;
  entityType: string;
  dateTime: string;
  unixTimeStamp: number;
  title: string;
  link: string;
  uuid: string;
  type: string;
}

const useStyles = makeStyles<Theme, object>((theme) => ({
  ...(theme.classes as object),
}));

function Home() {
  const classes = useStyles({} as object);

  const [eventList, setEventList] = useState<Event[]>([]);
  const [filters, setFilters] = useState<Map<string, boolean>>(new Map());
  const currentDateTime = Date.now();

  const getData = () => {
    axios
      .get(
        'https://rlkww3p7g8.execute-api.us-east-2.amazonaws.com/default/DC_Events_API'
      )
      .then((response) => {
        let tempEventList = response.data.body.Items;
        setEventList(
          tempEventList
            .sort(
              (a: Event, b: Event) =>
                new Date(a.dateTime).getTime() - new Date(b.dateTime).getTime()
            )
            .filter(
              (item: Event) =>
                new Date(item.dateTime).getTime() >= currentDateTime
            )
        );
      })
      .catch((error) => {
        console.log(error.message);
      });
  };

  useEffect(() => {
    getData();
  }, []);

  // Toggles filters on and off for different types of entitys that have events
  const toggleFilters = (entityType: string) => {
    if (!filters.has(entityType))
      setFilters(new Map(filters.set(entityType, true)));
    else setFilters(new Map(filters.set(entityType, !filters.get(entityType))));
  };

  // checks if the entity type is in the filters map
  const isInFilters = (entityType: string) => {
    if (filters.has(entityType)) {
      if (filters.get(entityType) === true) return true;
    }
    return false;
  };

  // maps list of events to Cards
  const mapEventList = (arr: Event[]) => {
    return arr.map((item: Event) => {
      const dateTime = new Date(item.dateTime);
      return (
        <Card
          title={item.title}
          dateTime={
            dateTime.getHours() !== 0
              ? dateTime.toLocaleString()
              : dateTime.toLocaleDateString()
          }
          entity={item.entity}
          link={item.link}
          key={item.uuid}
          type={item.type}
        />
      );
    });
  };

  return (
    <Container className={classes.home}>
      <div className={classes.homeButtonContainer}>
        <MyButton onClick={() => toggleFilters('Think Tank')}>
          Filter Think Tanks
        </MyButton>
        <MyButton onClick={() => toggleFilters('Bookstore')}>
          Filter Bookstores
        </MyButton>
      </div>
      {eventList?.length > 1 ? (
        mapEventList(
          filters.size > 0
            ? eventList.filter((item) => !isInFilters(item.type))
            : eventList
        )
      ) : (
        <LinearProgress />
      )}
    </Container>
  );
}

export default Home;
