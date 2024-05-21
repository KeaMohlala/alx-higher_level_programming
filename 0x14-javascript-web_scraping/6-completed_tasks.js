#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

const completedTasksPerUser = {};

request(apiUrl, function (error, response, body) {
  if (error || response.statusCode !== 200) {
    console.error('Error:', error);
    return;
  }

  const todos = JSON.parse(body);
  todos.forEach(todo => {
    if (todo.completed) {
      const userId = todo.userId.toString();
      if (!completedTasksPerUser[userId]) {
        completedTasksPerUser[userId] = 0;
      }
      completedTasksPerUser[userId]++;
    }
  });
  console.log(completedTasksPerUser);
});
