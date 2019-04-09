/*
Take an array of integers or arrays and flatten it

To run:
node flatten_array.js
*/

var a = [1, 2, [3, [4, 5], 6, 7], 8];


function flatten(arg) {
  let answer = [];
  for (let i=0; i < arg.length; i++) {
    if (Array.isArray(arg[i])) {
        answer.push(...flatten(arg[i]));
    } else {
        answer.push(arg[i]);
    }
  }
  return answer;
}

console.log(flatten(a))
// flatten(a) should return [1, 2, 3, 4, 5, 6, 7, 8]
