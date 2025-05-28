const names = ["gio", "dato", "da me"];

const [name1, name2, name3] = names;

console.log(name1); 
console.log(name2); 
console.log(name3); 

const points = [10, 30, 5, 2, 99];
points.push(50); 
points.pop(); 
points.shift(); 
points.unshift(15); 
const join = points.join(", "); 
const str = points.toString(); 
const morepoints = [200, 300];
const morepoints2 = points.concat(morepoints); 

console.log(points);
console.log(join);
console.log(str);
console.log(morepoints2);


const fruits = ["apple", "banana", "mango"];

const remove = fruits[fruits.length - 1];
console.log(remove);
