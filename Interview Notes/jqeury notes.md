1. What is jQuery?

jQuery is a lightweight JavaScript library which gives a quick and simple method for HTML DOM traversing and manipulation, its event handling, its client-side animations, and so on. One of the best features of jQuery is that jQuery supports an efficient way to implement AJAX applications because of its lightweight nature and make normalize and efficient web programs.

2. How is body onload() function is different from document.ready() function used in jQuery?

Document.ready() function is different from body onload() function because off 2 reasons.

We can have more than one document.ready() function in a page where we can have only one onload function.
Document.ready() function is called as soon as DOM is loaded where body.onload() function is called when everything gets loaded on the page that includes DOM, images and all associated resources of the page.
3. What are features of JQuery or what can be done using JQuery?

Features of Jquery

One can easily provide effects and can do animations.
Applying / Changing CSS.
Cool plugins.
Ajax support
DOM selection events
Event Handling
4. What are the different type of selectors in Jquery?

There are 3 types of selectors in Jquery

CSS Selector
XPath Selector
Custom Selector
5. What are the advantages of JQuery ?

There are many advantages of JQuery. Some of them are :

It is more like a JavaScript enhancement so there is no overhead in learning a new syntax.
It has the ability to keep the code simple, readable, clear and reusable.
Cross-browser support (IE 6.0+, FF 1.5+, Safari 2.0+, Opera 9.0+)
It would eradicate the requirement for writing complex loops and DOM scripting library calls.
Event detection and handling.
Tons of plug-ins for all kind of needs.
6. Why jQuery?

jQuery is very compact and well-written JavaScript code that increases the productivity of the developer by enabling them to achieve critical UI functionality by writing very less amount of code.

It helps to

Improve the performance of the application
Develop most browser compatible web page
Implement UI related critical functionality without writing hundreds of lines of codes
Fast
Extensible – jQuery can be extended to implement customized behavior
Other advantages of jQuery are

No need to learn fresh new syntax’s to use jQuery, knowing simple JavaScript syntax is enough
Simple and Cleaner code, no need to write several lines of codes to achieve complex functionality.
7. What is jQuery Selectors? Give some examples

jQuery Selectors are used to select one or a group of HTML elements from your web page.
jQuery support all the CSS selectors as well as many additional custom selectors.
jQuery selectors always start with dollar sign and parentheses: $()
There are three building blocks to select the elements in a web document.

1. Select elements by tag name

Example

$(div)
It will select all the div elements in the document.

2. Select elements by ID

Example

$(“#abc”)
It will select single element that has an ID of abc.

3. Select elements by Class

Example

$(“.xyzClass”)
It will select all the elements having class xyzClass.

8. Explain width() vs css(‘width’)

In jQuery, there are two way to change the width of an element. One way is using .css(‘width’) and other way is using .width().

For example

$('#mydiv').css(‘width’,’300px’);
$('#mydiv').width(100);
The difference in .css(‘width’) and .width() is the data type of value we specify or return from the both functions.
In .css(‘width’) we have to add “px” in the width value while in .width() we don’t have to add.
When you want to get the width of “mydiv” element then .css(‘width’) will return ‘300px’ while .width() will return only integer value 300.
9. Explain bind() vs live() vs delegate() methods.

The bind() method will not attach events to those elements which are added after DOM is loaded while live() and delegate() methods attach events to the future elements also.

The difference between live() and delegate() methods is live() function will not work in chaining. It will work only on an selector or an element while delegate() method can work in chaining.

For example

$(document).ready(function(){
$("#myTable").find("tr").live("click",function(){
alert($(this).text());
});
});
Above code will not work using live() method. But using delegate() method we can accomplish this.

$(document).ready(function(){
$("#dvContainer")children("table").delegate("tr","click",function(){
alert($(this).text());
});
});
10. What is the use of param() method.

The param() method is used to represent an array or an object in serialize manner.
While making an ajax request we can use these serialize values in the query strings of URL.

Syntax:

$.param(object | array, boolValue)
“object | array” specifies an array or an object to be serialized.

“boolValue” specifies whether to use the traditional style of param serialization or not.

Example

personObj=new Object();
empObject.name="Ravi";
empObject.age="28";
empObject.dept="IT";
$("#clickme").click(function(){
$("span").text($.param(empObject));
});
It will set the text of span to “name=Ravi&age=28&dep=IT”

11. What is the difference between jquery.size() and jquery.length?

jQuery .size() method returns number of element in the object. But it is not preferred to use the size() method as jQuery provide .length property and which does the same thing. But the .length property is preferred because it does not have the overhead of a function call.

12. How to read, write and delete cookies in jQuery?

To deal with cookies in jQuery we have to use the Dough cookie plugin.

Dough is easy to use and having powerful features.

Create cookie:
$.dough(“cookie_name”, “cookie_value”);
Read Cookie:
$.dough(“cookie_name”);
Delete cookie:
$.dough(“cookie_name”, “remove”);
13. What is difference between $(this) and ‘this’ in jQuery?

$(document).ready(function(){
$(‘#clickme’).click(function(){
alert($(this).text());
alert(this.innerText);
});
});
this and $(this) references the same element but the difference is that “this” is used in traditional way but when “this” is used with $() then it becomes a jQuery object on which we can use the functions of jQuery.?

In the example given, when only “this” keyword is used then we can use the jQuery text() function to get the text of the element, because it is not jQuery object. Once the “this” keyword is wrapped in $() then we can use the jQuery function text() to get the text of the element.

14. What are the various ajax functions ?

Ajax allows the user to exchange data with a server and update parts of a page without reloading the entire page. Some of the functions of ajax are as follows:

$.ajax(): This is considered to be the most low level and basic of functions. It is used to send requests . This function can be performed without a selector.


 
$.ajaxSetup(): This function is used to define and set the options for various ajax calls.

For example.

$.ajaxSetup({
"type":"POST",
"url":"ajax.php",
"success":function(data){
$("#bar")
.css("background","yellow")
.html(data);
}
});
Shorthand ajax methods: They comprise of simply the wrapper function that call $.ajax() with certain parameters already set.

$.getJSON(): this is a special type of shorthand function which is used to accept the url to which the requests are sent. Also optional data and optional callback functions are possible in such functions.

15. Explain .empty() vs .remove() vs .detach().

.empty() method is used to remove all the child elements from matched elements.
.remove() method is used to remove all the matched element. This method will remove all the jQuery data associated with the matched element.
.detach() method is same as .remove() method except that the .detach() method doesn’t remove jQuery data associated with the matched elements.
.remove() is faster than .empty() or .detach() method.

Syntax:

$(selector).empty();
$(selector).remove();
$(selector).detach();
16. How can events be prevented from stopping to work after an ajax request?

There are two ways to handle this issue:

Use of event delegation: The event delegation technique works on principle by exploiting the event bubbling. It uses event bubbling to capture the events on elements which are present anywhere in the domain object model. In jquery the user can make use of the live and die methods for the events delegation which contains a subset of event types.

For example. handling even delegation, handling of clicks on any <a> element:

$('#mydiv').click(function(e){
if( $(e.target).is('a') )
fn.call(e.target,e);
});
$('#mydiv').load('my.html')
Event rebinding usage: When this method is used it requires the user to call the bind method and the added new elements.

$('a').click(fn);
$('#mydiv').load('my.html',function(){
$('#mydiv a').click(fn);
});

AJAX
Update a web page without reloading the page
Request data from a server - after the page has loaded 
Receive data from a server - after the page has loaded
Send data to a server - in the background

AJAX is a technique for creating fast and dynamic web pages.

AJAX allows web pages to be updated asynchronously by exchanging small amounts of data with the server behind the scenes. This means that it is possible to update parts of a web page, without reloading the whole page.

XMLHttpRequest object (to retrieve data from a web server)
JavaScript/DOM (to display/use the data)

1)Create an XMLHttpRequest Object :The XMLHttpRequest object is used to exchange data with a server behind the scenes. This means that it is possible to update parts of a web page, without reloading the whole page.

--variable = new XMLHttpRequest();

2)Send a Request To a Server
To send a request to a server, we use the open() and send() methods of the XMLHttpRequest object:

xhttp.open("GET", "ajax_info.txt", true);
xhttp.send();

3)Server Response
To get the response from a server, use the responseText or responseXML property of the XMLHttpRequest object.

4)
a)onreadystatechange	Stores a function (or the name of a function) to be called automatically each time the readyState property changes

b)readyState	Holds the status of the XMLHttpRequest. Changes from 0 to 4: 
0: request not initialized 
1: server connection established
2: request received 
3: processing request 
4: request finished and response is ready

c)status	200: "OK"
404: Page not found

Ajax interview questions
AJAX or Asynchronous Javascript and XML is one of the most preferred platforms used by developers. We also find its application in several industries and verticals as it offers unique features. A lot of brands hire developers who can work on this platform so that they can get their websites designed on it. The platform seems promising as it can build interactive web applications, which are required for retaining the visiting customer and engaging them for a longer duration. This is one of the factors that increases the page ranking on SERP.  Today the demand for the AJAX developers has increased and corporate houses and business owners are looking forward to hire them. Almost every organization is trying to hold up a strong social presence and therefore developers are hired to make the presence even stronger among the potential customers. The interview for the developers can be tough as the competition is really high and the market is full of talent. While some prefer general knowledge on programming other interviewers can ask technical questions. Thus, here is a list of compiled possible Ajax interview questions that can be asked by an interviewer:

Q1.Brief about Ajax.
ANS- Ajax is considered to be a developer’s best friend because it offers several benefits to him such as updating the web page without reloading the entire page, requesting data from the server and also sending data to the server. AJAX is the acronym for Asynchronous JavaScript and XML. It is a new technique to communicate to and from a server/ database without completely refreshing the page. It creates faster, interactive, better web applications with help of CSS, XML, HTML, and JavaScript.

Q2.Differentiate between Synchronous and Asynchronous Ajax requests.
ANS- Synchronous Ajax requests– In this, the script stops and waits for the server to reply before continuing. In web application world, one has to happen after the other, i.e. the interaction between the customer and the server is synchronous. Synchronous is not recommended as it blocks/hangs the page until the response is received from the server.

Asynchronous Ajax requests handle the reply as and when it comes and allows the page to continue to be processed. Under Asynchronous, if there is any problem in the request it can be modified and recovered. The request doesn’t block the client as the browser is responsive. The user can perform other operations as well.

Q3- List some advantages and disadvantages of using Ajax.
Ans- Ajax is a very easy concept if one has a sound knowledge of JavaScript. It uses JavaScript functions to call methods from a web service. It has certain advantages-

Speed- Ajax reduces the server traffic and also the time consumption on server and client side.
Ajax is very responsive and fast, data can be transferred at a time.
XMLHttpRequest plays a significant role in Ajax. It is a special JavaScript object that calls asynchronous HTTP request to the server for transferring data.
One of the biggest advantages of using Ajax as forms are common elements in the web page. Ajax gives options for validation and much more.
One doesn’t have to completely reload the page.
There are some disadvantages attached to Ajax. They are-

Search engines would not be able to index Ajax applications so Ajax maybe a mistake.
Anyone can have access to the code of Ajax and can view source it.
ActiveX requests are enabled only in internet explorer and other new browsers.
Q4. What are different readyState in Ajax.
ANS- There are total 5 ready state in Ajax:

Value	State	Description
0	UNSET	Client has been created. Open() not yet called.
1	OPENED	Open() called.
2	HEADRERS_RECIEVED	Send() called and headers are available.
3	LOADING	Downloading: responseText holds partial data.
4	DONE	The operation is complete.
Q5- What is XMLHttpRequest object in Ajax? How can you XMLHttpRequest Object?
ANS- The XMLHttpRequest objects are used to exchange data with a server. It is an API whose methods transfer between a web browser and a web server. In XHR, it’s not necessary that data have to be in form of XML. It can be JSON or HTML. XHR can be used with protocols other than HTTP.

XMLHttpRequest is any developers kit because it has the option to update the page without reloading the entire page. You can request data from the server and also send data to the server in the background.

Q6- How to cancel the current request in Ajax?
Ans- Current request in AJAX is cancelled when the user performs an action which sets of an Ajax request. This can be depicted with the help of auto-complete functionality for a search box where users can be helped with related search terms based on their current input, by making an AJAX request each time they pass a key in search field. The user types faster than the Ajax request and you would want to abort any non-finished requests, before starting the next one.

Q7- How to send an Ajax request in JavaScript?
ANS- HTTP Requests are created with the help of XMLHttpRequest objects. It facilitates the transfer of data between client and server which happens via request and response. In XMLHttpRequest, you can perform the same function plus you can grab data from URL without having to refresh the page. AJAX lets you perform actions without reloading the entire page. The following steps tell how to call AJAX-

Create an XMLHttpRequest object.
Open the request with open method.
Now, send the request with the send method.
Q8- Explain Fetch API in JavaScript.
Ans- Fetch API uses to request and response objects that can be used in future whenever needed. It provides an interface for fetching resources. Fetch API uses promises that enable cleaner API. Cache API or other similar things handles the request and responses that might require you to generate your own responses programmatically.

Thus, you can now crack your interview and work as a developer in one of your dream companies by preparing from these set of question and answers to be technically sound.

Q9. Explain limitations of Ajax.
1)Browser Integration

The dynamically created page does not register itself with the browser history engine, so triggering the “Back” function of the users’ browser might not bring the desired result.

2)Response-time Concerns

Network latency – or the interval between user request and server response – needs to be considered carefully during Ajax development.

3)Search Engine Optimization (SEO)

Websites that use Ajax to load data which should be indexed by search engines must be careful to provide equivalent Sitemaps data at a public, linked URL that the search engine can read, as search engines do not generally execute the JavaScript code required for Ajax functionality.

4)Reliance on JavaScript

Ajax relies on JavaScript, which is often implemented differently by different browsers or versions of a particular browser. Because of this, sites that use JavaScript may need to be tested in multiple browsers to check for compatibility issues.

10. Explain what is polling in AJAX.
The Process of retrieving data from a server to obtain near-live data regularly is called AJAX polling.

$(this).hide() - hides the current element.

$("p").hide() - hides all <p> elements.

$(".test").hide() - hides all elements with class="test".

$("#test").hide() - hides the element with id="test".