import eventList from './eventList.json';

// Components
import Card from './components/Card/Card';

function App() {
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
