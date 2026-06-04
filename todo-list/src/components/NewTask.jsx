function NewTask(props) {
  return (
    <div className="new-task">
      <input type="text" value={props.value} onChange={props.onChange} />
      <button onClick={props.onClick}>Add</button>
    </div>
  );
}

export default NewTask;
