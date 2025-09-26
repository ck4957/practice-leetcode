What are some do

### Call Back Function

A callback function is a function that is passed as an argument to another function and is executed after some operation has been completed. This is commonly used in asynchronous programming to handle the result of an operation once it is finished.

Example:

```javascript
function fetchData(callback) {
  setTimeout(() => {
    const data = { id: 1, name: "John Doe" };
    callback(data);
  }, 1000);
}

fetchData((result) => {
  console.log("Data received:", result);
});
```

Downsides of callbacks 1. Callback Hell – deeply nested callbacks make code hard to read and maintain. 2. Error Handling – errors must be manually propagated through callback arguments, which can be inconsistent. 3. Inversion of Control – relying on a callback means giving control of execution to another function, which can lead to unexpected behaviors. 4. Difficult Debugging – stack traces become harder to follow. 5. Scalability Issues – composing multiple asynchronous operations (e.g., sequencing or parallel execution) becomes complex.

### Closures

A closure is a function that retains access to its lexical scope, even when the function is executed outside that scope. This allows the function to remember the environment in which it was created.
Example:

```javascript
function makeCounter() {
  let count = 0;
  return function () {
    count++;
    return count;
  };
}

const counter = makeCounter();
console.log(counter()); // 1
console.log(counter()); // 2
console.log(counter()); // 3
```

### Prototypes

In JavaScript, every object has a prototype. A prototype is also an object. All JavaScript objects inherit their properties and methods from their prototype.

### == and ===

The == operator compares two values for equality, but it performs type coercion if the values are of different types. The === operator, on the other hand, compares both the value and the type, and does not perform type coercion.
Example:

```javascript
0 == false; // true
0 === false; // false
1 == "1"; // true
1 === "1"; // false
```

### Hoisting

Hoisting is a JavaScript mechanism where variables and function declarations are moved to the top of their containing scope during the compilation phase. This means that you can use variables and functions before they are declared in the code.

Example:

```javascript
console.log(x); // undefined
var x = 5;
console.log(y); // ReferenceError: y is not defined
let y = 10;
```

## Promises:

Describe Promises, their states, and how they handle asynchronous operations.

Promises are objects that represent the eventual completion (or failure) of an asynchronous operation and its resulting value. A Promise can be in one of three states:

1. Pending: The initial state, neither fulfilled nor rejected.
2. Fulfilled: The operation completed successfully, resulting in a value.
3. Rejected: The operation failed, resulting in a reason for the failure.

Promises provide a way to work with asynchronous code by allowing you to attach callbacks for success and failure cases using the `.then()` and `.catch()` methods.

Example:

```javascript
const fetchData = () => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const data = { id: 1, name: "John Doe" };
      resolve(data);
    }, 1000);
  });
};

fetchData()
  .then((result) => {
    console.log("Data received:", result);
  })
  .catch((error) => {
    console.error("Error:", error);
  });
```

## async/await:

Explain async/await and how they simplify asynchronous code.
The `async` and `await` keywords in JavaScript provide a way to write asynchronous code that looks and behaves like synchronous code. This makes it easier to read and maintain.

When a function is declared with the `async` keyword, it automatically returns a Promise. Inside an `async` function, the `await` keyword can be used to pause the execution of the function until a Promise is resolved or rejected.
async/await. They make asynchronous code look more synchronous, improving readability and error handling.

## Event Loop:

Describe the JavaScript Event Loop, Call Stack, Callback Queue, and Microtask Queue.
The Event Loop is a fundamental concept in JavaScript that allows for non-blocking, asynchronous programming. It manages the execution of multiple pieces of code by using a Call Stack, Callback Queue, and Microtask Queue.

## call(), apply(), and bind():

Describe the differences and uses of these methods for function invocation.
The `call()`, `apply()`, and `bind()` methods are used to change the context (`this` value) of a function in JavaScript.

- `call()`: Invokes a function with a specified `this` value and arguments provided individually.
- `apply()`: Invokes a function with a specified `this` value and arguments provided as an array or array-like object.
- `bind()`: Returns a new function with a specified `this` value and initial arguments, without invoking the function immediately.
  Example:

```javascript
const person = {
  name: "Alice",
  greet: function (greeting) {
    console.log(`${greeting}, my name is ${this.name}`);
  },
};

person.greet("Hello"); // Hello, my name is Alice
const anotherPerson = { name: "Bob" };
person.greet.call(anotherPerson, "Hi"); // Hi, my name is Bob
person.greet.apply(anotherPerson, ["Hey"]); // Hey, my name is Bob
const boundGreet = person.greet.bind(anotherPerson);
boundGreet("Greetings"); // Greetings, my name is Bob
```

## DOM Manipulation:

Explain how to interact with the Document Object Model (DOM) using JavaScript.
The Document Object Model (DOM) is a programming interface for web documents. It represents the structure of a document as a tree of objects, allowing developers to manipulate the content, structure, and style of web pages using JavaScript.

## Strict Mode:

Explain what strict mode is and its benefits.
Strict mode is a feature in JavaScript that helps developers write more secure and optimized code by enforcing stricter parsing and error handling. It can be enabled by adding the directive `"use strict";` at the beginning of a script or a function.

Benefits of strict mode include:

1. **Elimination of Silent Errors**: Strict mode converts silent errors into throw errors, making it easier to identify and fix issues.
2. **Preventing Variable Hoisting**: Variables must be declared before use, reducing the chances of accidental global variable creation.
3. **Disallowing Duplicate Parameters**: Strict mode does not allow duplicate parameter names in function declarations, helping to avoid confusion.
4. **Securing `this` Context**: In strict mode, `this` is `undefined` in functions that are not called as methods, preventing unintended behavior.

## Immediately Invoked Function Expressions (IIFEs):

Explain IIFEs and their purpose.
An Immediately Invoked Function Expression (IIFE) is a JavaScript function that is executed immediately after it is defined. It is a design pattern that helps to create a private scope for variables and functions, preventing them from polluting the global namespace.
Example:

```javascript
(function () {
  var privateVariable = "I am private";
  console.log(privateVariable);
})();
// privateVariable is not accessible outside the IIFE
(function () {
  console.log("This is an IIFE");
})();
```

## Debouncing and Throttling:

Explain these techniques for optimizing event handling.
Debouncing and throttling are techniques used to optimize event handling in JavaScript, particularly for events that can fire frequently, such as scroll, resize, or keypress events.

- **Debouncing**: Debouncing ensures that a function is only executed after a specified delay has passed since the last time it was invoked. This is useful for scenarios where you want to limit the rate of function execution, such as when handling input events.
  Example of Debouncing:

```javascript
function debounce(func, delay) {
  let timeoutId;
  return function (...args) {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => {
      func.apply(this, args);
    }, delay);
  };
}
const handleResize = debounce(() => {
  console.log("Window resized");
}, 300);
window.addEventListener("resize", handleResize);
```

## Pure Functions:

Define pure functions and their advantages in functional programming.

```javascript
function pureFunction(x) {
  return x * 2;
}
```

## Error Handling:

Explain different approaches to error handling in JavaScript.
JavaScript provides several approaches to handle errors effectively:

1. **Try-Catch-Finally**: The most common way to handle errors is by using the `try-catch-finally` statement. Code that may throw an error is placed inside the `try` block, and if an error occurs, it is caught in the `catch` block. The `finally` block is optional and executes regardless of whether an error occurred or not.

```javascript
try {
  // Code that may throw an error
  let result = riskyOperation();
  console.log(result);
} catch (error) {
  // Handle the error
  console.error("An error occurred:", error.message);
} finally {
  // Code that will run regardless of an error
  console.log("Execution completed.");
}
```

2. **Throwing Custom Errors**: You can create and throw custom error objects using the `throw` statement. This allows you to provide more context about the error.

```javascript
function riskyOperation() {
  throw new Error("Something went wrong");
}

try {
  riskyOperation();
} catch (error) {
  console.error("Caught an error:", error.message);
}
```

ECMAScript Editions
Year Name Description
—————————————————————————————————————————
1997 ECMAScript 1 First Edition.
1998 ECMAScript 2 Editorial changes only.
1999 ECMAScript 3 Added Regular Expressions.
Added try/catch.
ECMAScript 4 Was never released.
2009 ECMAScript 5 Added "strict mode".
Added JSON support.
2011 ECMAScript 5.1 Editorial changes.
2015 ECMAScript 6 Added classes and modules.
2016 ECMAScript 7 Added exponential operator (\*\*).
Added Array.prototype.includes.

ECMAScript 6 is also called ECMAScript 2015.
ECMAScript 7 is also called ECMAScript 2016.

—JSON
JSON is a format for storing and transporting data.
JSON is often used when data is sent from a server to a web page.
JSON.parse() to convert the string into a JavaScript object:
var obj = JSON.parse(text);

—Regular Expression(RegEx)

var str = “dsjnsldsjpeqag”

var res = str.search(/dsJ/i) //search for a matche and returns the position of a match

str = “Visit Microsoft”
var res = str.replace(“Microsoft”,”w3Schools”); //returns the modified string

Modifier
i - Performs case in-sensitive matching
g - Perform a global match(returns all the matches and doesn’t stop after first match)
m - Perform multiline matching

Expression
[abc] - Find any characters between matching
[0-9] - Find any digits between the brackets
(x|y) - Find any of the alternatives separated with |

--Disadvantages
Client-side JavaScript does not allow the reading or writing of files.
This has been kept for security reason.
JavaScript can not be used for Networking applications
because there is no such support available.
JavaScript doesn't have any multithreading or multiprocess capabilities.

0 == false // true
0 === false // false, because they are of a different type
1 == "1" // true, automatic type conversion for value only
1 === "1" // false, because they are of a different type
null == undefined // true
null === undefined // false
'0' == false // true
'0' === false // false

Object creation

var emp = {
name: "Zara",
age: 10
};

Define arrays:
var x = []; //Good Way of defining
var
y = [1, 2, 3, 4, 5];

var arr = new Array(1,2,3); //Bad way of defining
arr.push(4);
arr.pop(); //Removes the last element of array
arr.length => 4
typeof arr // returns object

arr.shift(); //removes the first elements from arr and returns the value and moves other values to lower index
arr.unshift(); //adds new elements to the beginning of array

var arr4 = arr1.concat(arr2,arr3); //Merge three arrays

arr.splice(2,0,a,b);

2 - where new element should be added
0 - how many element should be removed
remaining parameters are the elements to be added
arr instance Array; //returns true

Convert Arrays to Strings

Read Arrays:
var x = [1, 2, 3, 4, 5];
for (var i = 0; i < x.length; i++) {
// Do something with x[i]
}

You should use objects when you want the element names to be strings (text).
You should use arrays when you want the element names to be numbers.

--Functions:
Named function:
function named(){
// do some stuff here
}

Functions can be either named or anonymous.
Anonymous functions can be assigned to a variable. We can also pass argument to those functions.

--Typeof:
Using typeof operator, we can get the type of arguments passed to a function. For example −
function func(x){
console.log(typeof x, arguments.length);
}
func(); //==> "undefined", 0
func(1); //==> "number", 1
func("1", "2", "3"); //==> "string", 3

How can you get the reference of a caller function inside a function?
The arguments object has a callee property, which refers to the function you're inside of. For example −

function func() {
return arguments.callee;
}
func(); // ==> func

--this keyword:
JavaScript famous keyword this always refers to the current context.

--Scope of variables
Global: Visible everywhere in javascript code
Local: Visible only within a function where it is defined.
A local variable takes precedence over a global variable with the same name.

-------------String Functions -------------
charAt() Returns the character at the specified index.
charCodeAt() Returns a number indicating the Unicode value of the character at the given index.
concat() Combines the text of two strings and returns a new string.

indexOf() Returns the index within the calling String object of the first occurrence of the specified value, or -1 if not found.

lastIndexOf() Returns the index within the calling String object of the last occurrence of the specified value, or -1 if not found.
localeCompare() Returns a number indicating whether a reference string comes before or after or is the same as the given string in sort order.
length() Returns the length of the string.
match() Used to match a regular expression against a string.
replace() Used to find a match between a regular expression and a string, and to replace the matched substring with a new substring.
search() Executes the search for a match between a regular expression and a specified string.
slice() Extracts a section of a string and returns a new string.
split() Splits a String object into an array of strings by separating the string into substrings.
substr() Returns the characters in a string beginning at the specified location through the specified number of characters.
substring() Returns the characters in a string between two indexes into the string.
toLocaleLowerCase() The characters within a string are converted to lower case while respecting the current locale.
toLocaleUpperCase() The characters within a string are converted to upper case while respecting the current locale.
toLowerCase() Returns the calling string value converted to lower case.
toString() Returns a string representing the specified object.
toUpperCase() Returns the calling string value converted to uppercase.
valueOf() Returns the primitive value of the specified object.

-------------String HTML wrappers-------------
Here is a list of each method which returns a copy of the string wrapped inside the appropriate HTML tag.

Method Description
anchor() Creates an HTML anchor that is used as a hypertext target.
big() Creates a string to be displayed in a big font as if it were in a <big> tag.
blink() Creates a string to blink as if it were in a <blink> tag.
bold() Creates a string to be displayed as bold as if it were in a <b> tag.
fixed() Causes a string to be displayed in fixed-pitch font as if it were in a <tt> tag
fontcolor() Causes a string to be displayed in the specified color as if it were in a <font color="color"> tag.
fontsize() Causes a string to be displayed in the specified font size as if it were in a <font size="size"> tag.
italics() Causes a string to be italic, as if it were in an <i> tag.
link() Creates an HTML hypertext link that requests another URL.
small() Causes a string to be displayed in a small font, as if it were in a <small> tag.
strike() Causes a string to be displayed as struck-out text, as if it were in a <strike> tag.
sub() Causes a string to be displayed as a subscript, as if it were in a <sub> tag
sup() Causes a string to be displayed as a superscript, as if it were in a <sup> tag

--------------------------Array Methods--------------------------

Here is a list of each method and its description.

Method Description
concat() Returns a new array comprised of this array joined with other array(s) and/or value(s).
every() Returns true if every element in this array satisfies the provided testing function.
filter() Creates a new array with all of the elements of this array for which the provided filtering function returns true.
forEach() Calls a function for each element in the array.
indexOf() Returns the first (least) index of an element within the array equal to the specified value, or -1 if none is found.
join() Joins all elements of an array into a string.
lastIndexOf() Returns the last (greatest) index of an element within the array equal to the specified value, or -1 if none is found.
map() Creates a new array with the results of calling a provided function on every element in this array.
pop() Removes the last element from an array and returns that element.
push() Adds one or more elements to the end of an array and returns the new length of the array.
reduce() Apply a function simultaneously against two values of the array (from left-to-right) as to reduce it to a single value.
reduceRight() Apply a function simultaneously against two values of the array (from right-to-left) as to reduce it to a single value.
reverse() Reverses the order of the elements of an array -- the first becomes the last, and the last becomes the first.
shift() Removes the first element from an array and returns that element.
slice() Extracts a section of an array and returns a new array.
some() Returns true if at least one element in this array satisfies the provided testing function.
toSource() Represents the source code of an object
sort() Sorts the elements of an array.
splice() Adds and/or removes elements from an array.
toString() Returns a string representing the array and its elements.
unshift() Adds one or more elements to the front of an array and returns the new length of the array.

-------------Date Methods:-------------

Here is a list of each method and its description.

Method Description
Date() Returns today's date and time
getDate() Returns the day of the month for the specified date according to local time.
getDay() Returns the day of the week for the specified date according to local time.
getFullYear() Returns the year of the specified date according to local time.
getHours() Returns the hour in the specified date according to local time.
getMilliseconds() Returns the milliseconds in the specified date according to local time.
getMinutes() Returns the minutes in the specified date according to local time.
getMonth() Returns the month in the specified date according to local time.
getSeconds() Returns the seconds in the specified date according to local time.
getTime() Returns the numeric value of the specified date as the number of milliseconds since January 1, 1970, 00:00:00 UTC.
getTimezoneOffset() Returns the time-zone offset in minutes for the current locale.
getUTCDate() Returns the day (date) of the month in the specified date according to universal time.
getUTCDay() Returns the day of the week in the specified date according to universal time.
getUTCFullYear() Returns the year in the specified date according to universal time.
getUTCHours() Returns the hours in the specified date according to universal time.
getUTCMilliseconds() Returns the milliseconds in the specified date according to universal time.
getUTCMinutes() Returns the minutes in the specified date according to universal time.
getUTCMonth() Returns the month in the specified date according to universal time.
getUTCSeconds() Returns the seconds in the specified date according to universal time.
getYear() Deprecated - Returns the year in the specified date according to local time. Use getFullYear instead.
setDate() Sets the day of the month for a specified date according to local time.
setFullYear() Sets the full year for a specified date according to local time.
setHours() Sets the hours for a specified date according to local time.
setMilliseconds() Sets the milliseconds for a specified date according to local time.
setMinutes() Sets the minutes for a specified date according to local time.
setMonth() Sets the month for a specified date according to local time.
setSeconds() Sets the seconds for a specified date according to local time.
setTime() Sets the Date object to the time represented by a number of milliseconds since January 1, 1970, 00:00:00 UTC.
setUTCDate() Sets the day of the month for a specified date according to universal time.
setUTCFullYear() Sets the full year for a specified date according to universal time.
setUTCHours() Sets the hour for a specified date according to universal time.
setUTCMilliseconds() Sets the milliseconds for a specified date according to universal time.
setUTCMinutes() Sets the minutes for a specified date according to universal time.
setUTCMonth() Sets the month for a specified date according to universal time.
setUTCSeconds() Sets the seconds for a specified date according to universal time.
setYear() Deprecated - Sets the year for a specified date according to local time. Use setFullYear instead.
toDateString() Returns the "date" portion of the Date as a human-readable string.
toGMTString() Deprecated - Converts a date to a string, using the Internet GMT conventions. Use toUTCString instead.
toLocaleDateString() Returns the "date" portion of the Date as a string, using the current locale's conventions.
toLocaleFormat() Converts a date to a string, using a format string.
toLocaleString() Converts a date to a string, using the current locale's conventions.
toLocaleTimeString() Returns the "time" portion of the Date as a string, using the current locale's conventions.
toSource() Returns a string representing the source for an equivalent Date object; you can use this value to create a new object.
toString() Returns a string representing the specified Date object.
toTimeString() Returns the "time" portion of the Date as a human-readable string.
toUTCString() Converts a date to a string, using the universal time convention.
valueOf() Returns the primitive value of a Date object.
Date Static Methods:

In addition to the many instance methods listed previously, the Date object also defines two static methods. These methods are invoked through the Date( ) constructor itself:

Method Description
Date.parse( ) Parses a string representation of a date and time and returns the internal millisecond representation of that date.
Date.UTC( ) Returns the millisecond representation of the specified UTC date and time.

--------------------------Math Methods--------------------------

Here is a list of each method and its description.

Method Description
abs() Returns the absolute value of a number.
acos() Returns the arccosine (in radians) of a number.
asin() Returns the arcsine (in radians) of a number.
atan() Returns the arctangent (in radians) of a number.
atan2() Returns the arctangent of the quotient of its arguments.
ceil() Returns the smallest integer greater than or equal to a number.
cos() Returns the cosine of a number.
exp() Returns EN, where N is the argument, and E is Euler's constant, the base of the natural logarithm.
floor() Returns the largest integer less than or equal to a number.
log() Returns the natural logarithm (base E) of a number.
max() Returns the largest of zero or more numbers.
min() Returns the smallest of zero or more numbers.
pow() Returns base to the exponent power, that is, base exponent.
random() Returns a pseudo-random number between 0 and 1.
round() Returns the value of a number rounded to the nearest integer.
sin() Returns the sine of a number.
sqrt() Returns the square root of a number.
tan() Returns the tangent of a number.
toSource() Returns the string "Math".

--------------------------RegExp Methods:--------------------------

Here is a list of each method and its description.

Method Description
exec() Executes a search for a match in its string parameter.
test() Tests for a match in its string parameter.
toSource() Returns an object literal representing the specified object; you can use this value to create a new object.
toString() Returns a string representing the specified object.

1. What is JavaScript?

JavaScript is a client-side as well as server side scripting language that can be inserted into HTML pages and is understood by web browsers. JavaScript is also an Object Oriented Programming language

2. Enumerate the differences between Java and JavaScript?

Java is a complete programming language. In contrast, JavaScript is a coded program that can be introduced to HTML pages. These two languages are not at all inter-dependent and are designed for the different intent. Java is an object – oriented programming (OOPS) or structured programming language like C++ or C whereas JavaScript is a client-side scripting language and it is said to be unstructured programming.

3. What are JavaScript types?

Following are the JavaScript types:

Number
String
Boolean
Function
Object
Null
Undefined

4. What is the use of isNaN function?

isNan function returns true if the argument is not a number otherwise it is false.

5. Between JavaScript and an ASP script, which is faster?

JavaScript is faster. JavaScript is a client-side language and thus it does not need the assistance of the web server to execute. On the other hand, ASP is a server-side language and hence is always slower than JavaScript. Javascript now is also a server side language (nodejs).

javascript-code-snippet
Javascript

6. What is negative infinity?

Negative Infinity is a number in JavaScript which can be derived by dividing negative number by zero.

7. Is it possible to break JavaScript Code into several lines?

Breaking within a string statement can be done by the use of a backslash, ‘\’, at the end of the first line

Example:

document.write("This is \a program");

And if you change to a new line when not within a string statement, then javaScript ignores break in line.

Example:

var x=1, y=2,

z=
x+y;

The above code is perfectly fine, though not advisable as it hampers debugging.

8. Which company developed JavaScript?
   Netscape is the software company who developed JavaScript.

9. What are undeclared and undefined variables?

Undeclared variables are those that do not exist in a program and are not declared. If the program tries to read the value of an undeclared variable, then a runtime error is encountered.

Undefined variables are those that are declared in the program but have not been given any value. If the program tries to read the value of an undefined variable, an undefined value is returned.

10. Write the code for adding new elements dynamically?

<html> 
<head> <title>t1</title> 
<script type="text/javascript"> 
function addNode() { var newP = document.createElement("p"); 
var textNode = document.createTextNode(" This is a new text node"); 
newP.appendChild(textNode); 
document.getElementById("firstP").appendChild(newP); } 
</script> </head> 
<body> <p id="firstP">firstP<p> </body> 
</html>

11. What are global variables? How are these variable declared and what are the problems associated with using them?

Global variables are those that are available throughout the length of the code, that is, these have no scope. The var keyword is used to declare a local variable or object. If the var keyword is omitted, a global variable is declared.

Example:

// Declare a global globalVariable = “Test”;

The problems that are faced by using global variables are the clash of variable names of local and global scope. Also, it is difficult to debug and test the code that relies on global variables.

12. What is a prompt box?

A prompt box is a box which allows the user to enter input by providing a text box. Label and box will be provided to enter the text or number.

13. What is ‘this’ keyword in JavaScript?

‘This’ keyword refers to the object from where it was called.

14. Explain the working of timers in JavaScript? Also elucidate the drawbacks of using the timer, if any?

Timers are used to execute a piece of code at a set time or also to repeat the code in a given interval of time. This is done by using the functions setTimeout, setInterval and clearInterval.

The setTimeout(function, delay) function is used to start a timer that calls a particular function after the mentioned delay. The setInterval(function, delay) function is used to repeatedly execute the given function in the mentioned delay and only halts when cancelled. The clearInterval(id) function instructs the timer to stop.

Timers are operated within a single thread, and thus events might queue up, waiting to be executed.

15. Which symbol is used for comments in Javascript?

// for Single line comments and

/_ Multi
Line
Comment
_/

16. What is the difference between ViewState and SessionState?

‘ViewState’ is specific to a page in a session.

‘SessionState’ is specific to user specific data that can be accessed across all pages in the web application.

17. What is === operator?

=== is called as strict equality operator which returns true when the two operands are having the same value without any type conversion.

18. Explain how can you submit a form using JavaScript?

To submit a form using JavaScript use document.form[0].submit();

document.form[0].submit();

19. Does JavaScript support automatic type conversion?

Yes JavaScript does support automatic type conversion, it is the common way of type conversion used by JavaScript developers

20. How can the style/class of an element be changed?

It can be done in the following way:

document.getElementById(“myText”).style.fontSize = “20?;
or
document.getElementById(“myText”).className = “anyclass”;

21. Explain how to read and write a file using JavaScript?

There are two ways to read and write a file using JavaScript

Using JavaScript extensions
Using a web page and Active X objects

22. What are all the looping structures in JavaScript?

Following are looping structures in Javascript:
For
While
do-while loops

23. What is called Variable typing in Javascript?

Variable typing is used to assign a number to a variable and the same variable can be assigned to a string.

Example
i = 10;
i = "string";
This is called variable typing.

24. How can you convert the string of any base to integer in JavaScript?

The parseInt() function is used to convert numbers between different bases. parseInt() takes the string to be converted as its first parameter, and the second parameter is the base of the given string.

In order to convert 4F (of base 16) to integer, the code used will be –

parseInt ("4F", 16);

25. Explain the difference between “==” and “===”?

“==” checks only for equality in value whereas “===” is a stricter equality test and returns false if either the value or the type of the two variables are different.

26. What would be the result of 3+2+”7″?

Since 3 and 2 are integers, they will be added numerically. And since 7 is a string, its concatenation will be done. So the result would be 57.

27. Explain how to detect the operating system on the client machine?

In order to detect the operating system on the client machine, the navigator.appVersion string (property) should be used.

28. What do mean by NULL in Javascript?

The NULL value is used to represent no value or no object. It implies no object or null string, no valid boolean value, no number and no array object.

29. What is the function of delete operator?

The functionality of delete operator is used to delete all variables and objects in a program but it cannot delete variables declared with VAR keyword.

30. What is an undefined value in JavaScript?

Undefined value means the

Variable used in the code doesn’t exist
Variable is not assigned to any value
Property doesn’t exist

31. What are all the types of Pop up boxes available in JavaScript?

Alert
Confirm and
Prompt

32. What is the use of Void(0)?

Void(0) is used to prevent the page from refreshing and parameter “zero” is passed while calling.
Void(0) is used to call another method without refreshing the page.

33. How can a page be forced to load another page in JavaScript?

The following code has to be inserted to achieve the desired effect:

<script language="JavaScript" type="text/javascript" >

<!-- location.href="http://newhost/newpath/newfile.html"; //--></script>

34. What is the data type of variables of in JavaScript?

All variables in the JavaScript are object data types.

35. What is the difference between an alert box and a confirmation box?

An alert box displays only one button which is the OK button.

But a Confirmation box displays two buttons namely OK and cancel.

36. What are escape characters?

Escape characters (Backslash) is used when working with special characters like single quotes, double quotes, apostrophes and ampersands. Place backslash before the characters to make it display.

Example:

document.write "I m a "good" boy"
document.write "I m a \"good\" boy"

37. What are JavaScript Cookies?

Cookies are the small test files stored in a computer and it gets created when the user visits the websites to store information that they need. Example could be User Name details and shopping cart information from the previous visits.

38. Explain what is pop()method in JavaScript?

The pop() method is similar as the shift() method but the difference is that the Shift method works at the start of the array. Also the pop() method take the last element off of the given array and returns it. The array on which is called is then altered.
Example:
var cloths = [“Shirt”, “Pant”, “TShirt”];
cloths.pop();
//Now cloth becomes Shirt,Pant

39. Whether JavaScript has concept level scope?

No. JavaScript does not have concept level scope. The variable declared inside the function has scope inside the function.

40. Mention what is the disadvantage of using innerHTML in JavaScript?

If you use innerHTML in JavaScript the disadvantage is

Content is replaced everywhere
We cannot use like “appending to innerHTML”
Even if you use +=like “innerHTML = innerHTML + ‘html’” still the old content is replaced by html
The entire innerHTML content is re-parsed and build into elements, therefore its much slower
The innerHTML does not provide validation and therefore we can potentially insert valid and broken HTML in the document and break it 41. What is break and continue statements?

Break statement exits from the current loop.

Continue statement continues with next statement of the loop.

42. What are the two basic groups of dataypes in JavaScript?

They are as –

Primitive
Reference types.
Primitive types are number and Boolean data types. Reference types are more complex types like strings and dates.

43. How generic objects can be created?

Generic objects can be created as:
var I = new object();

44. What is the use of type of operator?

‘Typeof’ is an operator which is used to return a string description of the type of a variable.

45. Which keywords are used to handle exceptions?

Try… Catch—finally is used to handle exceptions in the JavaScript

Try{

Code

}

Catch(exp){

Code to throw an exception

}

Finally{

Code runs either it finishes successfully or after catch

}

46. Which keyword is used to print the text in the screen?

document.write(“Welcome”) is used to print the text – Welcome in the screen.

47. What is the use of blur function?

Blur function is used to remove the focus from the specified object.

--two repeated questions 48 & 49

50. What are the different types of errors in JavaScript?

There are three types of errors:

Load time errors: Errors which come up when loading a web page like improper syntax errors are known as Load time errors and it generates the errors dynamically.

Run time errors: Errors that come due to misuse of the command inside the HTML language.

Logical Errors: These are the errors that occur due to the bad logic performed on a function which is having different operation.

51. What is the use of Push method in JavaScript?

The push method is used to add or append one or more elements to the end of an Array. Using this method, we can append multiple elements by passing multiple arguments

52. What is unshift method in JavaScript?

Unshift method is like push method which works at the beginning of the array. This method is used to prepend one or more elements to the beginning of the array.

53. What is the difference between JavaScript and Jscript?

Both are almost similar. JavaScript is developed by Netscape and Jscript was developed by Microsoft .

54. How are object properties assigned?

Properties are assigned to objects in the following way –

obj["class"] = 12;
1
obj["class"] = 12;
or

obj.class = 12;
1
obj.class = 12;

55. What is the ‘Strict’ mode in JavaScript and how can it be enabled?

Strict Mode adds certain compulsions to JavaScript. Under the strict mode,
JavaScript shows errors for a piece of codes, which did not show an error before,
but might be problematic and potentially unsafe.
Strict mode also solves some mistakes that hamper the JavaScript engines to work efficiently.

Strict mode can be enabled by adding the string literal “use strict” above the file. This can be illustrated by the given example:

function myfunction()

{

“use strict";

var v = “This is a strict mode function";

}

56. What is the way to get the status of a CheckBox?

The status can be acquired as follows –

alert(document.getElementById(‘checkbox1’).checked);

If the CheckBox will be checked, this alert will return TRUE.

57. How can the OS of the client machine be detected?

The navigator.appVersion string can be used to detect the operating system on the client machine.

58. Explain window.onload and onDocumentReady?

The onload function is not run until all the information on the page is loaded. This leads to a substantial delay before any code is executed.

onDocumentReady loads the code just after the DOM is loaded. This allows early manipulation of the code.

59. How will you explain closures in JavaScript? When are they used?

Closure is a locally declared variable related to a function which stays in memory when the function has returned.

For example:

```javaScript
function greet(message) {
console.log(message);
}

function greeter(name, age) {
return name + " says howdy!! He is " + age + " years old";
}

// Generate the message
var message = greeter("James", 23);

// Pass it explicitly to greet
greet(message);

This function can be better represented by using closures

function greeter(name, age) {
var message = name + " says howdy!! He is " + age + " years old";
return function greet() {
console.log(message);
};

}
// Generate the closure

var JamesGreeter = greeter("James", 23);

// Use the closure

JamesGreeter();
```

60. How can a value be appended to an array?

A value can be appended to an array in the given manner –

arr[arr.length] = value;

61. Explain the for-in loop?

The for-in loop is used to loop through the properties of an object.

The syntax for the for-in loop is –

for (variable name in object){

statement or block to execute

}

In each repetition, one property from the object is associated to the variable name, and the loop is continued till all the properties of the object are depleted.

62. Describe the properties of an anonymous function in JavaScript?

A function that is declared without any named identifier is known as an anonymous function. In general, an anonymous function is inaccessible after its declaration.

Anonymous function declaration –

var anon = function() {

alert('I am anonymous');

};

anon();

63. What is the difference between .call() and .apply()?

The function .call() and .apply() are very similar in their usage except a little difference. .call() is used when the number of the function’s arguments are known to the programmer, as they have to be mentioned as arguments in the call statement. On the other hand, .apply() is used when the number is not known. The function .apply() expects the argument to be an array.

The basic difference between .call() and .apply() is in the way arguments are passed to the function. Their usage can be illustrated by the given example.

var someObject = {

myProperty : 'Foo',

myMethod : function(prefix, postfix) {

alert(prefix + this.myProperty + postfix);

}

};

someObject.myMethod('<', '>'); // alerts '<Foo>'

var someOtherObject = {

myProperty : 'Bar'

};

someObject.myMethod.call(someOtherObject, '<', '>'); // alerts '<Bar>'

someObject.myMethod.apply(someOtherObject, ['<', '>']); // alerts '<Bar>'

64. Define event bubbling?

JavaScript allows DOM elements to be nested inside each other. In such a case, if the handler of the child is clicked, the handler of parent will also work as if it were clicked too.

65. Is JavaScript case sensitive? Give an example?

Yes, JavaScript is case sensitive. For example, a function parseInt is not same as the function Parseint.

66. What boolean operators can be used in JavaScript?

The ‘And’ Operator (&&), ‘Or’ Operator (||) and the ‘Not’ Operator (!) can be used in JavaScript.

\*Operators are without the parenthesis.

67. How can a particular frame be targeted, from a hyperlink, in JavaScript?

This can be done by including the name of the required frame in the hyperlink using the ‘target’ attribute.

<a href=”newpage.htm” target=”newframe”>>New Page</a>

68. What is the role of break and continue statements?

Break statement is used to come out of the current loop while the continue statement continues the current loop with a new recurrence.

69. Write the point of difference between web-garden and a web-farm?

Both web-garden and web-farm are web hosting systems. The only difference is that web-garden is a setup that includes many processors in a single server while web-farm is a larger setup that uses more than one server.

70. How are object properties assigned?

Assigning properties to objects is done in the same way as a value is assigned to a variable. For example, a form object’s action value is assigned as ‘submit’ in the following manner – Document.form.action=”submit”

71. What is the method for reading and writing a file in JavaScript?

This can be done by Using JavaScript extensions (runs from JavaScript Editor), example for opening of a file –

fh = fopen(getScriptPath(), 0);

72. How are DOM utilized in JavaScript?

DOM stands for Document Object Model and is responsible for how various objects in a document interact with each other. DOM is required for developing web pages, which includes objects like paragraph, links, etc. These objects can be operated to include actions like add or delete. DOM is also required to add extra capabilities to a web page. On top of that, the use of API gives an advantage over other existing models.

73. How are event handlers utilized in JavaScript?

Events are the actions that result from activities, such as clicking a link or filling a form, by the user. An event handler is required to manage proper execution of all these events. Event handlers are an extra attribute of the object. This attribute includes event’s name and the action taken if the event takes place.

74. Explain the role of deferred scripts in JavaScript?

By default, the parsing of the HTML code, during page loading, is paused until the script has not stopped executing. It means, if the server is slow or the script is particularly heavy, then the webpage is displayed with a delay. While using Deferred, scripts delays execution of the script till the time HTML parser is running. This reduces the loading time of web pages and they get displayed faster.

75. What are the various functional components in JavaScript?

The different functional components in JavaScript are-

First-class functions: Functions in JavaScript are utilized as first class objects. This usually means that these functions can be passed as arguments to other functions, returned as values from other functions, assigned to variables or can also be stored in data structures.

Nested functions: The functions, which are defined inside other functions, are called Nested functions. They are called ‘everytime’ the main function is invoked.

76. Write about the errors shown in JavaScript?

JavaScript gives a message if it encounters an error. The recognized errors are –

Load-time errors: The errors shown at the time of the page loading are counted under Load-time errors. These errors are encountered by the use of improper syntax, and thus are detected while the page is getting loaded.
Run-time errors: This is the error that comes up while the program is running. It is caused by illegal operations, for example, division of a number by zero, or trying to access a non-existent area of the memory.
Logic errors: It is caused by the use of syntactically correct code, which does not fulfill the required task. For example, an infinite loop. 77. What are Screen objects?

Screen objects are used to read the information from the client’s screen. The properties of screen objects are –

AvailHeight: Gives the height of client’s screen
AvailWidth: Gives the width of client’s screen.
ColorDepth: Gives the bit depth of images on the client’s screen
Height: Gives the total height of the client’s screen, including the taskbar
Width: Gives the total width of the client’s screen, including the taskbar

78. Explain the unshift() method ?

This method is functional at the starting of the array, unlike the push(). It adds the desired number of elements to the top of an array. For example –

var name = [ "john" ];

name.unshift( "charlie" );

name.unshift( "joseph", "Jane" );

console.log(name);

The output is shown below:

[" joseph "," Jane ", " charlie ", " john "]

79. Define unescape() and escape() functions?

The escape () function is responsible for coding a string so as to make the transfer of the information from one computer to the other, across a network.

For Example:

<script>

document.write(escape(“Hello? How are you!”));

</script>

Output: Hello%3F%20How%20are%20you%21

The unescape() function is very important as it decodes the coded string.

It works in the following way. For example:

<script>

document.write(unescape(“Hello%3F%20How%20are%20you%21”));

</script>

Output: Hello? How are you!

80. What are the decodeURI() and encodeURI()?

EncodeURl() is used to convert URL into their hex coding. And DecodeURI() is used to convert the encoded URL back to normal.

<script>

var uri="my test.asp?name=ståle&car=saab";

document.write(encodeURI(uri)+ "<br>");

document.write(decodeURI(uri));

</script>

Output –

my%20test.asp?name=st%C3%A5le&car=saab

my test.asp?name=ståle&car=saab

81. Why it is not advised to use innerHTML in JavaScript?

innerHTML content is refreshed every time and thus is slower. There is no scope for validation in innerHTML and, therefore, it is easier to insert rouge code in the document and, thus, make the web page unstable.

82. What does the following statement declares?

var myArray = [[[]]];
It declares a three dimensional array.

83. How are JavaScript and ECMA Script related?

ECMA Script are like rules and guideline while Javascript is a scripting language used for web development.

84. What is namespacing in JavaScript and how is it used?

Namespacing is used for grouping the desired functions, variables etc. under a unique name. It is a name that has been attached to the desired functions, objects and properties. This improves modularity in the coding and enables code reuse.

85. How can JavaScript codes be hidden from old browsers that don’t support JavaScript?

For hiding JavaScript codes from old browsers:

Add “<!–” without the quotes in the code just after the <script> tag.

Add “//–>” without the quotes in the code just before the <script> tag.

Old browsers will now treat this JavaScript code as a long HTML comment. While, a browser that supports JavaScript, will take the “<!–” and “//–>” as one-line comments.
