const friends = ["rahim", "karim", "abdul", "sadsd", "heroAlom"];

let bigName = friends[0];
let currLen = friends[0].length;

for (friend of friends) {
  if (friend.length > currLen) {
    currLen = friend.length;
    bigName = friend;
  }
}

console.log(bigName);
