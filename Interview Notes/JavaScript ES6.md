# What is ES6?

Es6 or ECMASCRIPT 2015 is sixth major release of ECMAScript language which comes with a lot of new features and syntax for writing web applications in javascript. As currently, not all browsers support ES6, they support pre-versions of ES6.SO to write web applications in ES6 that will support all Browsers we needed tools like Babel and Webpack.

# List some new features of ES6

New Features in ES6.

- Support for constants (also known as “immutable variables”)
- Block-Scope support for both variables, constants, functions
- Arrow Functions
- Extended Parameter Handling
- Template Literals
- Extended Literals
- Enhanced Regular Expression
- Enhanced Object Properties
- Destructuring Assignment
- Modules, Classes, Iterators, Generators
- Support for Map/Set & WeakMap/WeakSet
- Promises, Meta-Programming ,- Internationalization & Localization
  Read More from http://es6-features.org/

# What is Babel?

Babel is one of the most popular JavaScript transpilers and becomes the industry standard. It allows us to write ES6 code and convert it back in pre-Es6 JavaScript that browser supports.

For example look the below code snippet.

In ES6 (ECMASCRIPT 2015)

```
const PI = 3.141593;
PI > 3.0 ;
export{PI};
```

In ES5 after conversion

```
"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
var PI = 3.141593;
PI > 3.0;
exports.PI = PI;
```

# List steps to install Babel?

Installation

In order to install Babel, you require node.js and NPM. Make sure Node.js is installed on your server.

To check node installed or not run below commands on your terminal.

```
node -v
npm -v
```

Installing Babel

We can install Babel CLI locally by running below command on terminal.

```
npm install --save-dev babel-cli
```

# What is Webpack?

Webpack allows you to run an environment that hosts babel. Webpack is opensource javascript module bundler which takes modules with dependencies and generates static assets representing those modules.

# List benefits of using Webpack?

Benefits of using Webpack.

- It bundles your multiple modules and packs it into a single .js file.
- It comes with integrated dev server. A small express app for local development. You simply include one Javascript tag pointed to the server, like localhost:8080/assets/bundle.js, and get live code updating and asset management for free.

# Explain Constants in Es6?

Constants also are known as immutable variables are a special type of variables whose content is not changed. In Es6 a constant is defined using const keyword. Constants in Es6 enable protection to overwrite a variable value, improve performance and helps programmers to write readable and cleaner code.

Example

In Es6

const WEBSITE_URL = "http://www.abc.com";
WEBSITE_URL="new url"; // generate an error;
console.log(WEBSITE_URL);

In prior version of Es6

// and only in global context and not in a block scope

Object.defineProperty(typeof global === "object" ? global : window, "WEBSITE_URL", {
value: "http://www.abc.com", enumerable: true,
writable: false,
configurable: false
});

console.log(WEBSITE_URL);

Also, Read Best Node JS Interview Questions

# What are template literals in Es6?

Template literals are the string with embedded code and variables inside. Template literal allows concatenation and interpolation in much more comprehensive and clear in comparison with prior versions of ECMAScript.

Let see an example of concatenating a string in JavaScript.

```
var a="Hello";
var b="John";
var c = a+ " " + b;
Console.log(c); //outputs Hello John;
```

In ES6 concatenation and interpolation is done by backtick “ in a single line. To interpolate a variable simply put in to {} braces forwarded by $ sign.>/p>

// In ES6

```
let a="Hello";
let b="John";
let c=`${a} ${b}`;
console.log(c); //outputs Hello John;
```

Also Read React js Interview questions

# What is Spread Operator in ES6?

Spread Operator provides a new way to manipulate array and objects in Es6.A Spread operator is represented by … followed by the variable name.

Example :

```
let a =[7,8,9];
let b=[1,2,3,...a,10];
console.log(b); // [1,2,3,7,8,9,10]
```

So spread operator spreads the contents of variable a and concatenates it in b.

Another Example

function print(...z){
console.log(z);
}

print(1,2,3,4);//[1,2,3,4] 10. Explain Destructuring Assignment in ES6?
Destructing assignment in another improvement in Es6. It allows us to extract data from array and objects into separate variables.

Example

let full_name =['John','Deo'];

let [first_name,last_name]=full_name;

console.log(first_name,last_name);
// outputs John Deo
Another example

let c=[100,200,330,400];

let [a,...b]=c;

console.log(a,b);

// outputs 100 [200, 330, 400]

11. How to create a Javascript class in ES6?
    In Es6 you can create a class using the Class keyword.Below is sample javascript class in ES6.

```
class User{
    constructor(name,age) {
        this.name  = name;
        this.age = age;
    }

    getData() {
        console.log(this.name + " is " + this.age + " years old !");
    }
}

var user = new User("foo", 7);
s1.getData();
```

ECMAScript 2016

--Constants

const PI = 3.1415

--Blocked Scope Variables

Before:

var i, x;
for (i = 0; i < a.length; i++) {
x = a[i];
…
}

After:
for (let i = 0; i < a.length; i++) {
let x = a[i]
…
}

--Arrow Functions

Before:
odds = evens.map(function (v) {return v+1;} );

After:
odds = evens.map(v => v + 1)
