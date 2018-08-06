var app = new Vue({
  el: '#app',
  data: {
    message: 'todos:',
    todos: [
      { todo: 'Learn Vue.js', completed: false },
      { todo: 'Master frontend', completed: false }
    ],
    todo: ''
  },
  methods: {
    addTodo: function(event) {
      // add todo to this.todos
      return this.todos.push({ todo: event.target.value, completed: false })
    },
    removeTodo: function(index) {
      // remove todo from this.
      return this.todos.splice(index, 1)
    },
    markDone: function(index) {
      // mark todo as done
      console.log(this.todos[index].completed)
      return this.todos[index].completed
        ? (this.todos[index].completed = false)
        : (this.todos[index].completed = true)
    }
  }
})
