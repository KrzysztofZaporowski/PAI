function Task(props) {
  return (
    <div className="task">
      <input
        type="checkbox"
        id={props.task.id}
        name={props.task.id}
        checked={props.task.completed}
        onChange={props.onChange}
      />
      <label
        htmlFor={props.task.id}
        className={props.task.completed ? "completed" : ""}
      >
        {props.task.text}
      </label>
    </div>
  );
}

export default Task;
