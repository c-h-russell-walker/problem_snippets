/*
To run:
node extract_integers.js
*/


let responseData = [
   {item: '4four'} ,
   {item: 'fi5ve'},
   {item: 'six6and7'},
];

function extractIntegers(data) {
  const pattern = /[0-9]/g;
  return [].concat(...data.map(respObj => {
    return respObj.item.match(pattern).map(str => parseInt(str));
  }));
}

// extractIntegers(responseData) should return [4, 5, 6, 7]

console.log(extractIntegers(responseData));
