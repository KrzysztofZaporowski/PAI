import React from "react";
import "./App.css";
import Filter from "./components/Filter";
import NewTask from "./components/NewTask";
import ToDoList from "./components/ToDoList";

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      todos: [],
      newTaskText: "",
      hideCompleted: false,
    };
  }

  handleInputChange = (event) => {
    this.setState({ newTaskText: event.target.value });
  };

  handleAddTask = () => {
    if (this.state.newTaskText.trim() === "") return;

    const newTask = {
      id: Date.now().toString(),
      text: this.state.newTaskText,
      completed: false,
    };

    this.setState((prevState) => ({
      todos: [...prevState.todos, newTask],
      newTaskText: "",
    }));
  };

  handleToggleTask = (id) => {
    this.setState((prevState) => ({
      todos: prevState.todos.map((todo) =>
        todo.id === id ? { ...todo, completed: !todo.completed } : todo,
      ),
    }));
  };

  handleFilterChange = (event) => {
    this.setState({ hideCompleted: event.target.checked });
  };

  render() {
    const filteredTodos = this.state.hideCompleted
      ? this.state.todos.filter((todo) => !todo.completed)
      : this.state.todos;

    return (
      <div className="app">
        <h1>Welcome to the To Do list!</h1>
        <Filter
          checked={this.state.hideCompleted}
          onChange={this.handleFilterChange}
        />
        <ToDoList
          todos={filteredTodos}
          onToggleTask={this.handleToggleTask}
        />
        <NewTask
          value={this.state.newTaskText}
          onChange={this.handleInputChange}
          onClick={this.handleAddTask}
        />
      </div>
    );
  }
}

export default App;
