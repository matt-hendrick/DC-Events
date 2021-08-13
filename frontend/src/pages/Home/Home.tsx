import { useState, useEffect } from 'react';
import './Home.css';

// Axios
import axios from 'axios';

// MUI
import Container from '@material-ui/core/Container';
import LinearProgress from '@material-ui/core/LinearProgress';

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

function Home() {
  const [eventList, setEventList] = useState<Event[]>([]);
  const [filter, setFilter] = useState<boolean>(false);
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

  const toggleFilter = () => {
    setFilter(!filter);
  };

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
        />
      );
    });
  };
  return (
    <Container className="home">
      <MyButton onClick={toggleFilter}>
        Turn {!filter ? 'On' : 'Off'} Filter
      </MyButton>
      {eventList?.length > 1 ? (
        mapEventList(
          filter
            ? eventList.filter((item) => item.type === 'Think Tank')
            : eventList
        )
      ) : (
        <LinearProgress />
      )}
    </Container>
  );
}

export default Home;
