import { useState, useEffect } from 'react';

import axios from 'axios';

// MUI
import Container from '@material-ui/core/Container';
import LinearProgress from '@material-ui/core/LinearProgress';

// Components
import Navbar from './components/Navbar/Navbar';
import Card from './components/Card/Card';

function App() {
  const [eventList, setEventList] = useState([] as any);

  const getData = () => {
    axios
      .get(
        'https://rlkww3p7g8.execute-api.us-east-2.amazonaws.com/default/DC_Events_API'
      )
      .then((response) => {
        let tempEventList = response.data.body.Items;
        setEventList(
          tempEventList.sort(
            (a: any, b: any) =>
              new Date(a.dateTime).getTime() - new Date(b.dateTime).getTime()
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
    <div>
      <Navbar />
      <Container style={{ paddingTop: '5vh', width: '85%' }}>
        {eventList?.length > 1 ? (
          eventList.map((item: any) => {
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
    </div>
  );
}

export default App;
