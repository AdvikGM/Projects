function calculator(num1, operator, num2) {
  if (operator === "+") {
    return num1 + num2;
  } else if (operator === "-") {
    return num1 - num2;
  } else if (operator === "*") {
    return num1 * num2;
  } else if (operator === "/") {
    return num1 / num2;
  } else {
    return "Unknown operator";
  }
}

console.log(calculator(10, "+", 5)); // Result: 15
console.log(calculator(20, "/", 2)); // Result: 10
