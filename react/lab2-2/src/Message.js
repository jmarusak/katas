export default function Message(props) {
  return (
    <div className="ui container">
      <div className="ui message">
         <div className="header">
            {props.header}
          </div>
          <p>{props.text}</p>
      </div>
    </div>
  );
}
