import eventList from './event_list.json';

// Components
import Card from './components/Card/Card';

function App() {
  eventList.sort(
    (a, b) => new Date(a.dateTime).getTime() - new Date(b.dateTime).getTime()
  );

  return (
    <div>
      {eventList.map((item: any) => {
        const dateTime = new Date(item.dateTime);
        return (
          <Card
            title={item.title}
            dateTime={dateTime.toLocaleString()}
            entity={item.entity}
            link={item.link}
          />
        );
      })}
    </div>
  );
}

export default App;
