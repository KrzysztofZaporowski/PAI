import React from "react";
import Task from "./Task";

class ToDoList extends React.Component {
  render() {
    const { todos, onToggleTask } = this.props;
    return (
      <div className="todo-list">
        {todos.length === 0 ? (
          <p className="empty">Nothing to do...</p>
        ) : (
          todos.map((todo) => (
            <Task key={todo.id} task={todo} onChange={() => onToggleTask(todo.id)} />
          ))
        )}
      </div>
    );
  }
}

export default ToDoList;
