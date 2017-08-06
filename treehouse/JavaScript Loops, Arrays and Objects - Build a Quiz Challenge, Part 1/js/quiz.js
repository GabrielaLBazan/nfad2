var question;
var answer;
var response;
var html;
var correctAnswers = 0;
var qAndA = [
  ['How many states are in the United States of America?', 50],
  ['How many continents are there?', 7],
  ['How many seasons are there in a year?', 4],
];
  
function print(message) {
  var outputDiv = document.getElementById('output');
  outputDiv.innerHTML = message;
}

for (var i = 0; i < qAndA.length; i += 1 ) {
  question = qAndA[i][0];
  answer = qAndA[i][1];
  response = parseInt(prompt(question));
  if (response === answer) {
    correctAnswers += 1;
  }
}

html = "You got " + correctAnswers +  " question(s) right.";
print(html);