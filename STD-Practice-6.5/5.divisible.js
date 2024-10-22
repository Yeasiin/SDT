// store for visible by 3 and 5
const store = [];

for (let i = 1; i <= 50; i++) {
  if (i % 3 == 0 && i % 5 == 0) {
    store.push(i);
  }
}

console.log(store);
