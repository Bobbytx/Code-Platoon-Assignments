import './App.css'

let list = []

function App() {

  const addTask = (e) => {
    e.preventDefault();
    let userInput = document.getElementById("userInput").value
    if (userInput !== '') {
      // let taskItem = document.createElement("li");
      // taskItem.textContent = userInput;
      // document.getElementById("taskList").appendChild(taskItem);
      // document.getElementById("userInput").value = '';
      list.push(userInput);
    }
    
  }

  return (
    <>
      <h1>React To-Do List App</h1>
      <form onSubmit={(e) => addTask(e)}>
        <input type="text" id="userInput" />
        <button type="submit">Add Task</button>
      </form>
      <div id="tasks">
        <h3>To-Do:</h3>
        <ul id="taskList">
          {list.map((item) => {
            console.log(list);
            <li>{"hello"}</li>
    })}</ul>
      </div>
    </>
  );
}

export default App
