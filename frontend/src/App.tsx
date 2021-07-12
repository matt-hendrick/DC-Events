import eventList from './event_list.json';

import Container from '@material-ui/core/Container';

// Components
import Navbar from './components/Navbar/Navbar';
import Card from './components/Card/Card';

function App() {
  eventList.sort(
    (a, b) => new Date(a.dateTime).getTime() - new Date(b.dateTime).getTime()
  );

  return (
    <div>
      <Navbar />
      <Container style={{ paddingTop: '5vh' }}>
        {eventList.map((item: any) => {
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
            />
          );
        })}
      </Container>
    </div>
  );
}

export default App;
