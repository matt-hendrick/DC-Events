import { useState, useEffect } from 'react';

// Axios
import axios from 'axios';

// MUI
import Container from '@material-ui/core/Container';
import LinearProgress from '@material-ui/core/LinearProgress';

// Components
import Card from '../../components/Card/Card';

interface Event {
  entity: string;
  entityType: string;
  dateTime: string;
  unixTimeStamp: number;
  title: string;
  link: string;
  uuid: string;
}

function Home() {
  const [eventList, setEventList] = useState<Event[]>([]);
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

  return (
    <Container style={{ paddingTop: '5vh', width: '85%' }}>
      {eventList?.length > 1 ? (
        eventList.map((item: Event) => {
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
        })
      ) : (
        <LinearProgress />
      )}
    </Container>
  );
}

export default Home;
