1. What is JSON? For what is used for?

JSON (JavaScript Object Notation) is a data storage and communication format based on key-value pair of JavaScript object literals. It is a lightweight text-based open standard designed for human-readable data interchange which is derived from the JavaScript programming language for representing simple data structures and associative arrays, called objects.

In JSON

all property names are surrounded by double quotes.
values are restricted to simple data: no function calls, variables, comments, or computations.
JSON is used for communication between javascript and serverside technologies.

2. How to convert Javascript objects into JSON?

JSON.stringify(value); is used to convert Javascript objects into JSON.

Example Usage:

    var obj={"website":"Onlineinterviewquestions"};
    JSON.stringify(obj); // '{"website":"Onlineinterviewquestions"}'
3. List types Natively supported by JSON?

JSON supports Objects, Arrays, Primitives (strings, numbers, boolean values (true/false), null) data types

4. What does Object.create do?

Object.create creates a new object with the specified prototype object and properties.

5. What does hasOwnProperty method do?

It returns true if the property was set on an actual object rather than inherited.

Also, Read Ajax Interview Questions

6. What does $.parseJSON() do ?

$.parseJSON() takes a well-formed JSON string and returns the resulting JavaScript value.

7. What are different ways to create objects?

You can create Object by

object literals
Object.create
constructors
8. What is the default value of a constructor’s prototype?

A plain, empty object that derives from Object.prototype is the default value of a constructor’s prototype

9. List some benefits of JSON over XML?

It is faster and lighter than XML as on the wire data format
XML data is typeless while JSON objects are typed
JSON types: Number, Array, Boolean, String
XML data are all string
Data is readily available as JSON object is in your JavaScript
Fetching values is as simple as reading from an object property in your JavaScript code
10. What is the difference between JSON and JSONP?

JSON: JSON is a simple data format used for communication medium between different systems
JSONP: It is a methodology for using that format with cross-domain ajax requests while not being affected by same origin policy issue.
11. Who is the Father of JSON and What is the scripting language JSON is based on?

Douglas Crockford called as the Father of JSON. JSON is based on ECMAScript.

12.What is JSON-RPC? List some Features of JSON-RPC-Java

JSON-RPC: JSON-RPC is a simple remote procedure call protocol similar to XML-RPC although it uses the lightweight JSON format instead of XML.

JSON-RPC-Java is a Java implementation of the JSON-RPC protocol.Below is list of some of its features

Dynamically call server-side Java methods from JavaScript DHTML web applications. No Page reloading.
Asynchronous communications.
Transparently maps Java objects to JavaScript objects.
Lightweight protocol similar to XML-RPC although much faster.
Leverages J2EE security model with session specific exporting of objects.
Supports Internet Explorer, Mozilla, Firefox, Safari, Opera, and Konqueror.
13.What are natively supported JSON types?

Following data types are natively supported in JSON.

Numbers: Integer, float or Double
String: string of Unicode characters, must be rapped into double quotes “”
Boolean: True or false
Array: ordered list of 0 or more values
Objects : An unordered collection key/ value pairs
Null: An Empty value
Read Latest Jquery interview questions

14.What is BSON?

BSON is the superset of JSON, which used by MongoDB.BSON supports the embedding of documents and arrays within other documents and arrays. BSON also contains extensions that allow representation of data types that are not part of the JSON spec.

15.How to convert an Object into JSON? What is the full syntax of JSON.stringify?

JSON.stringify method is used to convert an Javascript Object into JSON.
Syntax:

let json = JSON.stringify(value[, replacer, space])
 

16. What JS-specific properties are skipped by JSON.stringify method?

Following JS-specific properties are skipped by JSON.stringify method

Function properties (methods).
Symbolic properties.
Properties that store undefined.
17. How do you decode a JSON string?

Use JSON.parse method to decode a JSON string into a Javascript object

18. How to delete an index from JSON Obj?

Deleting an Element from JSON Obj

var exjson = {'key':'value'};
delete exjson['key'];
