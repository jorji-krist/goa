let sum = 0;
for (let i = 1; i <= 100; i++) {
  sum += i;
}
console.log(sum);

for (let i = 1; i <= 50; i++) {
  if (i % 2 === 0) {
    console.log(i + " ლუწია");
  } else {
    console.log(i + " კენტია");
  }
}
let text = "JavaScript is awesome!";

if (text.length === 0) {
  console.log("მგონია, რომ ცარიელია");
} else if (text.includes("a")) {
  console.log("მსგავსი სიმბოლოა ნაპოვნი");
} else {
  console.log("სტანდარტული ტექსტი");
}