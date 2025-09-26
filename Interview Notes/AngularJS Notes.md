1. What is Angular JS?

AngularJS is a JavaScript framework that is used for making rich, extensible web applications. It runs on plain JavaScript and HTML, so you don’t need any other dependencies to make it work.AngularJS is perfect for Single Page Applications (SPA). It is basically used for binding JavaScript objects with HTML UI elements.

2. Explain the architecture of AngularJS?

AngularJS is architecture on 3 components. They are

The Template (View)
The Scope (Model)
The Controller (Controller)
AngularJS extends HTML attributes with Directives and binds data to HTML with Expressions.

3. What is the Template in AngularJS?

The template is the HTML portion of the angular app. It is exactly like a static HTML page, except that templates contain additional syntax which allows data to be injected in it in order to provide a customized user experience.

4. What is the scope in AngularJS?

The scope is the object that represents the “model” of your application. It contains fields that store data which is presented to the user via the template, as well as functions which can be called when the user performs certain actions such as clicking a button.

5. What is the controller in AngularJS?

The controller is a function which generally takes an empty scope object as a parameter and adds to it the fields and functions that will be later exposed to the user via the view.

6. Explain Directives in AngularJs?

AngularJS directives are extended HTML attributes with the prefix ng-
The 3 main directives of angular js are

ng-app:- directive is used to flag the HTML element that Angular should consider to be the root element of our application. Angular uses spinal-case for its custom attributes and camelCase for the corresponding directives which implement them.
ng-model:- directive allows us to bind values of HTML controls (input, select, textarea) to application data. When using ngModel, not only change in the scope reflected in the view, but changes in the view are reflected back into the scope.
ng-bind:- directive binds application modal data to the HTML view.

7. List some tools for testing AngularJS applications?

For testing AngularJS applications there are certain tools that you should use that will make testing much easier to set up and run.

Karma

Karma is a JavaScript command line tool that can be used to spawn a web server which loads your application’s source code and executes your tests. You can configure Karma to run against a number of browsers, which is useful for being confident that your application works on all browsers you need to support. Karma is executed on the command line and will display the results of your tests on the command line once they have run in the browser.

Karma is a NodeJS application and should be installed through NPM/YARN. Full installation instructions are available on the Karma website.

Jasmine

Jasmine is a behavior-driven development framework for JavaScript that has become the most popular choice for testing AngularJS applications. Jasmine provides functions to help with structuring your tests and also making assertions. As your tests grow, keeping them well structured and documented is vital, and Jasmine helps achieve this.

Jasmine comes with a number of matches that help you make a variety of assertions. You should read the Jasmine documentation to see what they are. To use Jasmine with Karma, we use the karma-jasmine test runner.

angular-mocks

AngularJS also provides the ngMock module, which provides mocking for your tests. This is used to inject and mock AngularJS services within unit tests. In addition, it is able to extend other modules so they are synchronous. Having tests synchronous keeps them much cleaner and easier to work with. One of the most useful parts of ngMock is $httpBackend, which lets us mock XHR requests in tests and return sample data instead.

Source:https://docs.angularjs.org/guide/unit-testing

8. How do you share data between controllers in AngularJs?

We can share data by creating a service,
Services are easiest, fastest and cleaner way to share data between controllers in AngularJs.
There are also other ways to share data between controllers, they are

Using Events
$parent, nextSibling, controllerAs
Using the $rootScope

9. Explain AngularJS digest cycle?

AngularJS digest cycle is the process behind Angular JS data binding.
In each digest cycle, Angular compares the old and the new version of the scope model values. The digest cycle is triggered automatically. We can also use $apply() if we want to trigger the digest cycle manually.

10. What is internationalization in Angularjs?

Internationalization is a way to show locale-specific information on a website.It is used to create multilingual language websites.

11. Difference between AngularJS and JavaScript Expressions

Below are some major difference between AngularJS and JavaScript Expressions

Both can contain literals, operators, and variables.
AngularJS expressions can be written in HTML but JavaScript expressions are not.
AngularJS expressions do not support conditionals, loops, and exceptions, while JavaScript expressions do.
AngularJS expressions support filters, while JavaScript expressions do not.
12. Explain basic steps to set up an Angular app?

Create an angular.module
Assign a controller to the module
Link your module to HTML with ng-app
Link the controller to HTML with ng-controller directive
13. What are Angular Modules?

Angular Modules are place where we write code of our Angular application.Writing Modules makes our code more maintainable, testable, and readable. All dependencies for our app are defined in modules.

14.Explain Directive scopes?

There are three types of directive scopes available in Angular.

Parent Scope: is default scope
Child Scope:  If the properties and functions you set on the scope are not relevant to other directives and the parent, you should probably create a new child scope.
Isolated Scope: Isolated Scope is used if the directive you are going to build is self-contained and reusable. Does not inherit from parent scope, used for private/internal use.
15. How to isolate a directive’s Scope in Angular?

You can isolate a directive’s Scope by passing an object to the scope option of directive.
This tells the directive to keep scope inside of itself and not to inherit or share with other scopes.

16. What is the difference between one-way binding and two-way binding ?

In One-Way data binding, view (UI part) not updates automatically when data model changed. We need to write custom code to make it updated every time.
ng-bind has one-way data binding.


 
While in two way binding scope variable will change it’s value every time its data model changed is assigned to a different value.

17. How would you make an Angular service return a promise? Write a code snippet as an example

To add promise functionality to a service, we inject the “$q” dependency in the service, and then use it like so:


angular.factory('testService', function($q){
return {
getName: function(){
var deferred = $q.defer();

//API call here that returns data
testAPI.getName().then(function(name){
deferred.resolve(name)
})

return deferred.promise;
}
}
})
The $q library is a helper provider that implements promises and deferred objects to enable asynchronous functionality

Source: https://docs.angularjs.org/api/ng/service/$q

18. Explain the role of $routeProvider in AngularJS?

The $routeProvider is used to configure roots within an AngularJS application. It can be used to link a URL with a corresponding HTML page or template, and a controller (if applicable).

19. Explain how does Angular implement two-way binding?

Data-binding in Angular apps is the automatic synchronization of data between the model and view components. The way that Angular implements data-binding lets you treat the model as the single-source-of-truth in your application. The view is a projection of the model at all times. When the model changes, the view reflects the change and vice versa.

20. What is dependency injection and how does it work?

AngularJS was designed to highlight the power of dependency injection, a software design pattern that places an emphasis on giving components their dependencies instead of hardcoding them within the component. For example, if you had a controller that needed to access a list of customers, you would store the actual list of customers in a service that can be injected into the controller instead of hardcoding the list of customers into the code of the controller itself. In AngularJS you can inject values, factories, services, providers, and constants.

 

21. What is $rootscope? How is it different from the scope?

In Angular JS $rootscope and $scope both are an object which is used for sharing data from the controller to view.
The main difference between $rootscope and $scope is that $rootscope is available globally to across all the controllers whereas $scope is available only in controllers that have created it along with its children controllers.


 
22. What is the difference between $scope and scope?

In Angular js $scope is used whenever we have to use dependency injection (D.I) whereas as the scope is used for directive linking.

23. What are Angular Expressions?

Angular js Expression is JavaScript alike code snippets used to bind expression data in view or HTML. Angular expressions are written inside two curly braces.

{{a+b}}

24. List the major browsers Supported by Angular js?

Below are some major browsers supported by Angular js

Mozilla Firefox
Google Chrome
Microsft Edge
IE 10,11
IE Mobile,
Safari, iOS
Android: Nougat (7.0) Marshmallow (6.0)
25. How to enable HTML5 mode in Angular 1.x?

html5Mode method of $locationProvider module is used to enable HTML5 mode in Angular 1.x. For creating pretty URLs and removing # from URLs html5Mode need to true.

Enabling html5Mode to true in Angular 1.x.

angular.module('myApp', [])

    .config(function($routeProvider, $locationProvider) {

        $routeProvider
            .when('/', {
                templateUrl : 'partials/home.html',
                controller : mainController
            })
            

        // use the HTML5 History API
        $locationProvider.html5Mode(true);
    });
26. List some of the built-in validators in Angular JS?

Angular js supports all standard HTML5 attributes to validate input.Below are few built-in validators in Angular js.

required
min
max
type=”number” OR type=”email”
27. What is Angular’s prefixes $ and $$?

Angular uses these prefixes to prevent accidental code collision with users code.
$ prefix is used with public objects whereas $$ prefix is used with a public object.

28. What are directives? How to create and use custom Directive in Angular js.

In angular Directives are used to extend the attributes of Html elements.
Creating custom directive in Angular js.
Angular js Directives are restricted to element and attribute and created using a directive function.Here is sample code to create a directive in Angular js.

var app = angular.module("myApp", []);
app.controller('AppController', function($scope) {
    var users=[];
    var user1={};
    user1.firstName="Satyam";
    user1.lastName="Kumar";
    users.push(user1);
    var user2={};
    user2.firstName="Ravi";
    user2.lastName="Sankar";
    user2.push(user2);
    $scope.users=students;
});
app.directive('user', function() {
    //define the directive object
    var directive = {};
    //restrict = E, implies that directive is Element directive
    directive.restrict = 'E';
    //element will be replaced by this text/html
    directive.template = "First Name: {{user.firstName}} , Last Name: {{user.lastName}}";
    var linkFunction = function($scope, element, attributes) {
        element.css("background-color", "#e1e1e1");
    }
    directive.link=linkFunction;
    return directive;
});

As Above directive is restricted to Element directive, so you can use this directive as an element only.
Usage:

<div ng-app="app">
 <h1>Custom Directive Demo</h1>
 <div ng-controller="UserController">
 <div ng-repeat="user in users">
 <user></user>
 </div>
 </div>
</div>
 

29. How to access parent scope from child controller in Angular JS?

In angular there is a scope variable called $parent (i.e. $scope.$parent). $parent is used to access parent scope from child controller in Angular JS.
Example:

<div ng-controller="ParentCtrl">
    <h1>{{ name }}</h1>
    <p>{{ address }}</p>
    <div ng-controller="ChildCtrl">
        <h1>{{ title }}</h1>
        <input type="text" ng-model="$parent.address" />
</div>
 

30. How to do email and Phone no. validation in Angular JS?

Angular form validation and ng-pattern directive can be used to validate the email and phone number in Angular JS.

31. What is the difference between a link and compile in Angular JS?

Compile function: To template DOM manipulation and to gather all the directives, the compile function is used.
Link function: To register DOM listeners as well as for the instance DOM manipulation, the Link function is used.

32. How can you get URL parameters in Controller?

The RouteProvider and the RouteParams can be used to get the URL parameters in the controller.
As the route wires up the URL to the controller and RouteParams can be passed to the controller to get the URL parameters.

33. How to enable caching in Angular 1.x?

Caching can be enabled by setting the config.cache value or the default cache value to TRUE or to a cache object that is created with $cacheFactory.
In case you want to cache all the responses, then you can set the default cache value to TRUE.
And, if you want to cache a specific response, then you can set the config.cache value to TRUE.

34. Explain the use of Ng-If, Ng-Switch, And Ng-Repeat directives?

ng-if – This directive removes a portion of the DOM tree, which is based on the expression.
In case the expression is assigned to ng-if, it evaluates to a false value, and then the element is deleted from the DOM tree, or else a clone of the element is reinserted into the DOM.
ng-switch – This directive is used based on a scope expression to conditionally swap DOM structure on the template.
The ng-switch default directive will be preserved at the specific location in a template.
ng-repeat – This directive is used to instantiate the template once per item from a collection.
Each template which is instantiated gets its own scope where the given loop variable is set to the current collection of item.

35.How to change start and end symbols used for AngularJS expressions?

Passing the $interpolateprovider in the config can help us change the start and end symbols used in our Angular JS expressions.

36. List some difference between Angularjs and Angular 2?

Difference between AngularJS and Angular 2
Angular js or Angular 1.x is based on MVC Architecture	Angular 2 is based on service/ components
Javascript is used to write applications in Angular js.	Typescript (superset of javascript) is used to write application in Angular2.
Controller are used to write logics and interact with Model and view.	In Angular 2 Controllers are totally elminated and Components take its place.
Angular 1 is created for developing Single page web-applications.	In Angular 2 can used for developing native applications for mobile platform like React Native as well interative
web applications.
Angularjs is easy to setup, you just need to include angular.js library to start.	Angular 2 is dependent on other modules/ package.It give little brainstrom to install and run Angular 2.
In Angularjs ng-app directive is used bootstrap the app.	ng-app is removed in Angular 2. You need to call Angular2 bootstrap method to bootstrap your application.
37.How to validate an URL in Angular JS?

Adding the regex directly to the ng pattern to the attribute can help you validate the URL in Angular JS.

38.What is the use of $locale service in Angular JS?

locale service provides with the localization rules for Angular JS components.

39.What is transclusion in Angular JS?

The transclusion in Angular JS will allow you to move the original children of a directive to a specific location inside a new template.The ng directive marks the insertion point for the transcluded DOM of the very near parent directive that uses transclusion.
ng-transclude or ng-transclude-slot attribute directives are used for transclusion in Angular JS.


— AngularJS Directives
AngularJS directives are extended HTML attributes with the prefix ng-.

The ng-app directive initializes an AngularJS application.

The ng-init directive initializes application data.

The ng-model directive binds the value of HTML controls (input, select, textarea) to application data.

————————————————————————————————————————————————————————————————————————

— The ng-app Directive

The ng-app directive defines the root element of an AngularJS application.
The ng-app directive will auto-bootstrap (automatically initialize) the application when a web page is loaded.

— The ng-init Directive

The ng-init directive defines initial values for an AngularJS application.
Normally, you will not use ng-init. You will use a controller or module instead.

— The ng-model Directive

The ng-model directive binds the value of HTML controls (input, select, textarea) to application data.
The ng-model directive can also:
 - Provide type validation for application data (number, email, required).
 - Provide status for application data (invalid, dirty, touched, error).
 - Provide CSS classes for HTML elements.
 - Bind HTML elements to HTML forms.
The ng-model directive provides a two-way binding between the model and the view.

————————————————————————————————————————————————————————————————————————
AngularJS Data Binding
Data binding in AngularJS is the synchronization between the model and the view.
ng-model directive is used in data binding.

When data in the model changes, the view reflects the change, and when data in the view changes, the model is updated as well. This happens immediately and automatically, which makes sure that the model and the view is updated at all times.

————————————————————————————————————————————————————————————————————————

FACTORY

Factory can return anything which can be a class(constructor function) , instance of class , string , number or boolean . 
If you return a constructor function, you can instantiate in your controller. 

Service does not need to return anything. ... Because service will create instance by default and use that as a base object.
————————————————————————————————————————————————————————————————————————

SERVICES
In AngularJS you can make your own service, or use one of the many built-in services.

What is a Service?
In AngularJS, a service is a function, or object, that is available for, and limited to, your AngularJS application.

——— What are the differences between service and factory methods? —————— 
factory method is used to define a factory which can later be used to create services as and when required whereas service method is used to create a service whose purpose is to do some defined task.

AngularJS has about 30 built-in services. One of them is the $location service.

The $http Service
The $http service is one of the most common used services in AngularJS applications. 
The service makes a request to the server, and lets your application handle the response.
————————————————————————————————————————————————————————————————————————
Which are the core directives of AngularJS?

Following are the three core directives of AngularJS.
ng-app − This directive defines and links an AngularJS application to HTML.
ng-model − This directive binds the values of AngularJS application data to HTML input controls.
ng-bind − This directive binds the AngularJS Application data to HTML tags.

————————————————————————————————————————————————————————————————————————

What is MVC?
Model View Controller or MVC as it is popularly called, is a software design pattern for developing web applications. A Model View Controller pattern is made up of the following three parts:

Model − It is the lowest level of the pattern responsible for maintaining data.

View − It is responsible for displaying all or a portion of the data to the user.

Controller − It is a software Code that controls the interactions between the Model and View.

————————————————————————————————————————————————————————————————————————
What is AngularJS?
AngularJS is a framework to build large scale and high performance web application while keeping them as easy-to-maintain. Following are the features of AngularJS framework.

AngularJS is a powerful JavaScript based development framework to create RICH Internet Application (RIA).

AngularJS provides developers options to write client side application (using JavaScript) in a clean MVC (Model View Controller) way.

Application written in AngularJS is cross-browser compliant. AngularJS automatically handles JavaScript code suitable for each browser.

AngularJS is open source, completely free, and used by thousands of developers around the world. It is licensed under the Apache License version 2.0.

What is data binding in AngularJS?
What is scope in AngularJS?
What are the controllers in AngularJS?
Controllers are JavaScript functions that are bound to a particular scope. They are the prime actors in AngularJS framework and carry functions to operate on data and decide which view is to be updated to show the updated model based data.

What are the services in AngularJS?
What are the filters in AngularJS?
Explain directives in AngularJS.
Explain templates in AngularJS.
What is routing in AngularJS?
What is deep linking in AngularJS?
What are the advantages of AngularJS?
What are the disadvantages of AngularJS?
Which are the core directives of AngularJS?
Explain AngularJS boot process.
What is MVC?
Explain ng-app directive.
Explain ng-model directive.
Explain ng-bind directive.
Explain ng-controller directive.
ng-controller directive tells AngularJS what controller to use with this view. AngularJS application mainly relies on controllers to control the flow of data in the application. A controller is a JavaScript object containing attributes/properties and functions. Each controller accepts $scope as a parameter which refers to the application/module that controller is to control.

How AngularJS integrates with HTML?
Explain ng-init directive.
Explain ng-repeat directive.
What are AngularJS expressions?
Explain uppercase filter.
Explain lowercase filter.
Explain currency filter.
Explain filter filter.
Explain orderby filter.
Explain ng-disabled directive.
Explain ng-show directive.
Explain ng-hide directive.
Explain ng-click directive.
How angular.module works?
How to validate data in AngularJS?
Explain ng-include directive.
How to make an ajax call using Angular JS?
What is use of $routeProvider in AngularJS?
What is $rootScope?
What is scope hierarchy in AngularJS?
What is a service?
What is service method?
What is factory method?
What are the differences between service and factory methods?
Which components can be injected as a dependency in AngularJS?
What is provider?
What is constant?
Is AngularJS extensible?
On which types of component can we create a custom directive?
What is internationalization?
How to implement internationalization in AngularJS?
What is Next ?


AngularJS Interview Question #1

What are the basic steps to unit test an AngularJS filter?

Inject the module that contains the filter.
Provide any mocks that the filter relies on.
Get an instance of the filter using $filter('yourFilterName').
Assert your expectations.
Dependency injection is a powerful software design pattern that Angular employs to compose responsibilities through an intrinsic interface. However, for those new to the process, it can be puzzling where you need to configure and mock these dependencies when creating your isolated unit tests. The open-source project “Angular Test Patterns” is a free resource that is focused on dispelling such confusion through high-quality examples.


AngularJS Interview Question #2

What should be the maximum number of concurrent “watches”? Bonus: How would you keep an eye on that number?

TL;DR Summary: To reduce memory consumption and improve performance it is a good idea to limit the number of watches on a page to 2,000. A utility called ng-stats can help track your watch count and digest cycles.

Jank happens when your application cannot keep up with the screen refresh rate. To achieve 60 frames-per-second, you only have about 16 milliseconds for your code to execute. It is crucial that the scope digest cycles are as short as possible for your application to be responsive and smooth. Memory use and digest cycle performance are directly affected by the number of active watches. Therefore, it is best to keep the number of watches below 2,000. The open-source utility ng-stats gives developers insight into the number of watches Angular is managing, as well as the frequency and duration of digest cycles over time.

Caution: Be wary of relying on a “single magic metric” as the golden rule to follow. You must take the context of your application into account. The number of watches is simply a basic health signal. If you have many thousands of watches, or worse, if you see that number continue to grow as you interact with your page. Those are strong indications that you should look under the hood and review your code.

This question is valuable as it gives insight into how the candidate debugs runtime issues while creating a discussion about performance and optimization.



AngularJS Interview Question #3

How do you share data between controllers?

Create an AngularJS service that will hold the data and inject it inside of the controllers.

Using a service is the cleanest, fastest and easiest way to test. However, there are couple of other ways to implement data sharing between controllers, like:

– Using events
– Using $parent, nextSibling, controllerAs, etc. to directly access the controllers
– Using the $rootScope to add the data on (not a good practice)

The methods above are all correct, but are not the most efficient and easy to test.


AngularJS Interview Question #4

What is the difference between ng-show/ng-hide and ng-if directives?

ng-show/ng-hide will always insert the DOM element, but will display/hide it based on the condition. ng-if will not insert the DOM element until the condition is not fulfilled.

ng-if is better when we needed the DOM to be loaded conditionally, as it will help load page bit faster compared to ng-show/ng-hide.

We only need to keep in mind what the difference between these directives is, so deciding which one to use totally depends on the task requirements.

AngularJS Interview Question #5

What is a digest cycle in AngularJS?

In each digest cycle Angular compares the old and the new version of the scope model values. The digest cycle is triggered automatically. We can also use $apply() if we want to trigger the digest cycle manually.

For more information, take a look in the ng-book explanation: The Digest Loop and $apply

AngularJS Interview Question #6

Where should we implement the DOM manipulation in AngularJS?

In the directives. DOM Manipulations should not exist in controllers, services or anywhere else but in directives.

Here is a detailed explanation.

AngularJS Interview Question #7

Is it a good or bad practice to use AngularJS together with jQuery?

It is definitely a bad practice. We need to stay away from jQuery and try to realize the solution with an AngularJS approach. jQuery takes a traditional imperative approach to manipulating the DOM, and in an imperative approach, it is up to the programmer to express the individual steps leading up to the desired outcome.

AngularJS, however, takes a declarative approach to DOM manipulation. Here, instead of worrying about all of the step by step details regarding how to do the desired outcome, we are just declaring what we want and AngularJS worries about the rest, taking care of everything for us.


AngularJS Interview Question #8

If you were to migrate from Angular 1.4 to Angular 1.5, what is the main thing that would need refactoring?

Changing .directive to .component to adapt to the new Angular 1.5 components.

AngularJS Interview Question #9

How would you specify that a scope variable should have one-time binding only?

By using “::” in front of it. This allows you to check if the candidate is aware of the available variable bindings in AngularJS.

AngularJS Interview Question #10

What is the difference between one-way binding and two-way binding?

– One way binding implies that the scope variable in the html will be set to the first value its model is bound to (i.e. assigned to)
– Two way binding implies that the scope variable will change it’s value everytime its model is assigned to a different value

AngularJS Interview Question #11

Explain how $scope.$apply() works

$scope.$apply re-evaluates all the declared ng-models and applies the change to any that have been altered (i.e. assigned to a new value) Explanation: scope.scope.apply() is one of the core angular functions that should never be used explicitly, it forces the angular engine to run on all the watched variables and all external variables and apply the changes on their values

Source: https://docs.angularjs.org/api/ng/type/$rootScope.Scope

AngularJS Interview Question #12

What directive would you use to hide elements from the HTML DOM by removing them from that DOM not changing their styling?

The ngIf Directive, when applied to an element, will remove that element from the DOM if it’s condition is false.

AngularJS Interview Question #13

What makes the angular.copy() method so powerful?
(Question provided by Jad Salhani)

It creates a deep copy of the variable.

A deep copy of a variable means it doesn’t point to the same memory reference as that variable. Usually assigning one variable to another creates a “shallow copy”, which makes the two variables point to the same memory reference. Therefore if one is changed, the other changes as well.


AngularJS Interview Question #14

How would you make an Angular service return a promise? Write a code snippet as an example

To add promise functionality to a service, we inject the “$q” dependency in the service, and then use it like so:

angular.factory('testService', function($q) {
  return {
    getName: function() {
      var deferred = $q.defer();

      //API call here that returns data
      testAPI.getName().then(function(name) {
        deferred.resolve(name);
      });

      return deferred.promise;
    }
  };
});
The $q library is a helper provider that implements promises and deferred objects to enable asynchronous functionality.


Author Bio
Jad is a 5-star rated Codementor who has helped mentor many AngularJS users. Hire Jad now.

AngularJS Interview Quesion #15

What is the role of services in AngularJS and name any services made available by default?
(Question provided by Harikishore Tadigotla)

AngularJS Services are objects that provide separation of concerns to an AngularJS app. These can be created using a factory method or a service method. Services are singleton components and all components of the application (into which the service is injected) will work with single instance of the service. An AngularJS service allows developing of business logic without depending on the View logic which will work with it.

Few of the inbuilt services in AngularJS are:

the $http service: The $http service is a core Angular service that facilitates communication with the remote HTTP servers via the browser’s XMLHttpRequest object or via JSONP
the $log service: Simple service for logging. Default implementation safely writes the message into the browser’s console
the $anchorScroll: it scrolls to the element related to the specified hash or (if omitted) to the current value of $location.hash() Why should one know about AngularJS Services, you may ask. Well, understanding the purpose of AngularJS Services helps bring modularity to AngularJS code
Services are the best may to evolve reusable API within and AngularJS app.

Overview:

AngularJS Services help create reusable components.
A Service can be created either using the service() method or the factory() method.
A typical service can be injected into another service or into an AngularJS Controller.

AngularJS Interview Question #16

When creating a directive, it can be used in several different ways in the view. Which ways for using a directive do you know? How do you define the way your directive will be used?

When you create a directive, it can be used as an attribute, element or class name. To define which way to use, you need to set the restrict option in your directive declaration.

The restrict option is typically set to:

‘A’ – only matches attribute name ‘E’ – only matches element name
‘C’ – only matches class name

These restrictions can all be combined as needed:

‘AEC’ – matches either attribute or element or class name

For more information, feel free to check out the AngularJS documentation.

AngularJS Interview Question #17

When should you use an attribute versus an element?

Use an element when you are creating a component that is in control of the template. Use an attribute when you are decorating an existing element with new functionality.

This topic is important so developers can understand the several ways a directive can be used inside a view and when to use each way.


AngularJS Interview Question #18

How do you reset a $timeout, $interval(), and disable a $watch()?
(Question provided by Fouad Kada)

To reset a timeout and/or $interval, assign the result of the function to a variable and then call the .cancel() function:

var customTimeout = $timeout(function() {
  // arbitrary code
}, 55);

$timeout.cancel(customTimeout);
To disable $watch(), we call its deregistration function. $watch() then returns a deregistration function that we store to a variable and that will be called for cleanup:

var deregisterWatchFn = $scope.$on('$destroy', function() {
  // we invoke that deregistration function, to disable the watch
  deregisterWatchFn();
});
 


AngularJS Interview Question #19

Explain what is a $scope in AngularJS

Scope is an object that refers to the application model. It is an execution context for expressions. Scopes are arranged in hierarchical structure which mimic the DOM structure of the application. Scopes can watch expressions and propagate events. Scopes are objects that refer to the model. They act as glue between controller and view.

This question is important as it will judge a developer's knowledge about a $scope object, and it is one of the most important concepts in AngularJS. Scope acts like a bridge between view and model.


AngularJS Interview Question #20

What are Directives?

Directives are markers on a DOM element (such as an attribute, element name, comment or CSS class) that tell AngularJS’s HTML compiler ($compile) to attach a specified behavior to that DOM element (e.g. via event listeners), or even to transform the DOM element and its children. Angular comes with a set of these directives built-in, like ngBind, ngModel, and ngClass. Much like you create controllers and services, you can create your own directives for Angular to use. When Angular bootstraps your application, the HTML compiler traverses the DOM matching directives against the DOM elements.

This question is important because directives define the UI while defining a single page app. Candidates need to be very clear about how to create a new custom directive or use the existing ones already pre-build in AngularJS.


AngularJS Interview Question #21

What is DDO Directive Definition Object?

“DDO is an object used while creating a custome directive. A standard DDO object has following parameters.

var directiveDefinitionObject = {
  priority: 0,
  template: '<div></div>', // or // function(tElement, tAttrs) { ... },
  // or
  // templateUrl: 'directive.html', // or // function(tElement, tAttrs) { ... },
  transclude: false,
  restrict: 'A',
  templateNamespace: 'html',
  scope: false,
  controller: function(
    $scope,
    $element,
    $attrs,
    $transclude,
    otherInjectables
  ) { ... },
  controllerAs: 'stringIdentifier',
  bindToController: false,
  require: 'siblingDirectiveName', // or // ['^parentDirectiveName', '?optionalDirectiveName', '?^optionalParent'],
  compile: function compile(tElement, tAttrs, transclude) {
    return {
      pre: function preLink(scope, iElement, iAttrs, controller) { ... },
      post: function postLink(scope, iElement, iAttrs, controller) { ... }
    };
    // or
    // return function postLink( ... ) { ... }
  }
  // or
  // link: {
  //  pre: function preLink(scope, iElement, iAttrs, controller) { ... },
  //  post: function postLink(scope, iElement, iAttrs, controller) { ... }
  // }
  // or
  // link: function postLink( ... ) { ... }
};
This question mainly judges whether candidate knows about creating custom directives.


AngularJS Interview Question #22

What is a singleton pattern and where we can find it in Angularjs?

Is a great pattern that restricts the use of a class more than once. We can find singleton pattern in angular in dependency injection and in the services.

In a sense, if the candidate does 2 times ‘new Object()‘ without this pattern, the candidate will be alocating 2 pieces of memory for the same object. With singleton pattern, if the object exists, it'll be reused.


AngularJS Interview Question #23

What is an interceptor? What are common uses of it?

An interceptor is a middleware code where all the $http requests go through.

The interceptor is a factory that are registered in $httpProvider. There are 2 types of requests that go through the interceptor, request and response (with requestError and responseError respectively). This piece of code is very useful for error handling, authentication or middleware in all the requests/responses.


Angular Interview Question #24

How would you programatically change or adapt the template of a directive before it is executed and transformed?

The candidate should use the compile function. The compile function gives access to the directive’s template before transclusion occurs and templates are transformed, so changes can safely be made to DOM elements. This is very useful for cases where the DOM needs to be constructed based on runtime directive parameters.

Angular Interview Question #25

How would you validate a text input field for a twitter username, including the @ symbol?

The developer should use the ngPatterndirective to perform a regex match that matches Twitter usernames. The same principal can be applied to validating phone numbers, serial numbers, barcodes, zip codes and any other text input.

The official documentation can be found here.

Angular Interview Question #26

How would you implement application-wide exception handling in your Angular app?

Angular has a built-in error handler service called $exceptionHandler which can easily be overriden as seen below:

myApp.factory('$exceptionHandler', function($log, ErrorService) {
  return function(exception, cause) {
    if (console) {
      $log.error(exception);
      $log.error(cause);
    }

    ErrorService.send(exception, cause);
  };
});
This is very useful for sending errors to third party error logging services or helpdesk applications. Errors trapped inside of event callbacks are not propagated to this handler, but can manually be relayed to this handler by calling $exceptionHandler(e) from within a try catch block.

AngularJS Interview Question #27

How do you hide an HTML element via a button click in AngularJS?

This can be done by using the ng-hide directive in conjunction with a controller to hide an HTML element on button click.
```
<div ng-controller="MyCtrl">
  <button ng-click="hide()">Hide element</button>
  <p ng-hide="isHide">Hello World!</p>
</div>

 function MyCtrl($scope) {
  $scope.isHide = false;
  $scope.hide = function() {
    $scope.isHide = true;
  };
}
```

AngularJS Interview Question #28

How would you react on model changes to trigger some further action? For instance, say you have an input text field called email and you want to trigger or execute some code as soon as a user starts to type in their email.

This can be achieved by using $watch function in the controller.
```
function MyCtrl($scope) {
  $scope.email = '';

  $scope.$watch('email', function(newValue, oldValue) {
    if ($scope.email.length > 0) {
      console.log('User has started writing into email');
    }
  });
}
```
AngularJS Interview Question #29

How do you disable a button depending on a checkbox’s state?

The developer can use the ng-disabled directive and bind its condition to the checkbox’s state.
```
<body ng-app>
  <label><input type="checkbox" ng-model="checked"/>Disable Button</label>
  <button ng-disabled="checked">Select me</button>
</body>
```