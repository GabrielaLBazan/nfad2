var person = {
  name : 'Sarah',
  country : 'US',
  age : 35,
  treehouseStudent : true,
  skills : ['JavaScript', 'HTML', 'CSS']
};

/*function print(message) {
  var div = document.getElementById('listDiv');
  div.innerHTML = message;
}
*/

for (prop in person) {
  console.log(prop, ': ', person[prop]);
}
