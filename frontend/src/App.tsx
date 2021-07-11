import eventList from './eventList.json';

function App() {
  return (
    <div>
      {eventList.map((item: any) => {
        return (
          <div>
            <a href={item.link}>{item.title}</a>
            <div>{item.date}</div>
            <div>{item.time}</div>
          </div>
        );
      })}
    </div>
  );
}

export default App;
