// quiz begins, no answers correct
var points = 0;

// questions & answers
var question1 = prompt("Through what part of the body do dogs sweat?");
var answer1 = "paws";
if (question1.toLowerCase() === answer1) {
  points += 1;
  alert("That's correct! Let's try another one.");
} else {
  alert("Ooops, no, thats not right, let's try another one.");
}

var question2 = prompt("Which breed of dogs are known for having spots");
var answer2 = "dalmations";
if (question2.toLowerCase() === answer2) {
  points += 1;
  alert("That's correct! Let's try another one.");
} else {
  alert("Ooops, no, thats not right, let's try another one.");
}

var question3 = prompt("What is a dog's most powerful sense?");
var answer3 = "smell";
if (question3.toLowerCase() === answer3) {
  points += 1;
  alert("That's correct! Let's try another one.");
} else {
  alert("Ooops, no, thats not right, let's try another one.");
}

var question4 = prompt("Because of dogs' unique relationship with humans they are often referred to as 'man's best ...'?");
var answer4 = "friend";
if (question4.toLowerCase() === answer4) {
  points += 1;
  alert("That's correct! Let's try another one.");
} else {
  alert("Ooops, no, thats not right, let's try another one.");
}

var question5 = prompt("What is a dog's 'fingerprint'?");
var answer5 = "nose print";
if (question5.toLowerCase() === answer5) {
  points += 1;
  alert("That's correct! Let's see how you did.");
} else {
  alert("Ooops, no, thats not right. Let's see how you did.");
}

// output results
document.write("<h1>You got " + points + " out of 5</h3>");

// output rank
if (points === 5) {
  document.write("<h2>You get a gold crown!");
} else if (points < 5 && points > 2) {
  document.write("<h3>You get a silver crown!");
} else if (points > 0 && points < 3) {
  document.write("<h3>You get a bronze crown!");
} else {
  document.write("<p>No crown for you, do you even know what a dog is?</p>");
}
