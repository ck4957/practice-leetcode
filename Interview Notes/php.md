
Null coalescing operator ??
```
// Fetches the value of $_GET['user'] and returns 'nobody'
// if it does not exist.
$username = $_GET['user'] ?? 'nobody';
// This is equivalent to:
$username = isset($_GET['user']) ? $_GET['user'] : 'nobody';
```

1. What is PHP ?

PHP: Hypertext Preprocessor is open source server-side scripting language that is widely used for creation of dynamic web applications.It was developed by Rasmus Lerdorf also know as Father of PHP in 1994.

PHP is a loosely typed language , we didn’t have to tell PHP which kind of Datatype a Variable is. PHP automatically converts the variable to the correct datatype , depending on its value.

2. What is T_PAAMAYIM_NEKUDOTAYIM ?

T_PAAMAYIM_NEKUDOTAYIM is scope resolution operator used as :: (double colon) .Basically it used to calling static methods/variables of a Class.

Example usage:-

		
 $Cache::getConfig($key);
3. What is the difference between == and === operator in PHP ?

In PHP == is equal operator and returns TRUE if $a is equal to $b after type juggling and === is Identical operator and return TRUE if $a is equal to $b, and they are of the same data type.

Example Usages:


<?php 
   $a=true ;
   $b=1;
   // Below condition returns true and prints a and b are equal
   if($a==$b){
    echo "a and b are equal";
   }else{
    echo "a and b are not equal";
   }
   //Below condition returns false and prints a and b are not equal because $a and $b are of  different data types.
   if($a===$b){
    echo "a and b are equal";
   }else{
    echo "a and b are not equal";
   }
?>  
		
4. What is session in PHP. How to remove data from a session?

As HTTP is state protocol.To maintain states on server and share data across multiple pages PHP session are used.PHP sessions are simple way to store data for individual users/client against a unique session ID.Session IDs are normally sent to the browser via session cookies and the ID is used to retrieve existing session data,if session id is not present on server PHP creates a new session, and generate a new session ID.

Example Usage:-


<?php 
//starting a session
session_start();
//Creating a session 
$_SESSION['user_info']=['user_id'=>1,'first_name'=>'php','last_name'=>'scots','status'=>'active'];

//checking session
if(isset($_SESSION['user_info'])){
echo "logged In";
}

//un setting remove a value from session
unset($_SESSION['user_info']['first_name']);

// destroying complete session
session_destroy();

?>
5. How to register a variable in PHP session ?

In PHP 5.3 or below we can register a variable session_register() function.It is deprecated now and we can set directly a value in $_SESSION Global.

Example usage:


<?php
   // Starting session
    session_start();
   // Use of session_register() is deprecated
    $username = "PhpScots";
    session_register("username");
   // Use of $_SESSION is preferred
    $_SESSION["username"] = "PhpScots";
?>


Also Read Laravel interview questions

6. Where sessions stored in PHP ?

PHP sessions are stored on server generally in text files in a temp directory of server.
That file is not accessible from outside word. When we create a session PHP create a unique session id that is shared by client by creating cookie on clients browser.That session id is sent by client browser to server each time when a request is made and session is identified.
The default session name is “PHPSESSID”.

7. What is default session time and path in PHP. How to change it ?

Default session time in PHP is 1440 seconds (24 minutes) and Default session storage path is temporary folder/tmp on server.

You can change default session time by using below code


<?php
// server should keep session data for AT LEAST 1 hour
ini_set('session.gc_maxlifetime', 3600);

// each client should remember their session id for EXACTLY 1 hour
session_set_cookie_params(3600);
?>
8. What are PHP Magic Methods/Functions. List them.

In PHP all functions starting with __ names are magical functions/methods. Magical methods always lives in a PHP class.The definition of magical function are defined by programmer itself.

Here are list of magic functions available in PHP

__construct(), __destruct(), __call(), __callStatic(), __get(), __set(), __isset(), __unset(), __sleep(), __wakeup(), __toString(), __invoke(), __set_state(), __clone() and __debugInfo() .

9. What is difference between include,require,include_once and require_once() ?

Include :-Include is used to include files more than once in single PHP script.You can include a file as many times you want.

Syntax:- include(“file_name.php”);

Include Once:-Include once include a file only one time in php script.Second attempt to include is ignored.

Syntax:- include_once(“file_name.php”);

Require:-Require is also used to include files more than once in single PHP script.Require generates a Fatal error and halts the script execution,if file is not found on specified location or path.You can require a file as many time you want in a single script.

Syntax:- require(“file_name.php”);

Require Once :-Require once include a file only one time in php script.Second attempt to include is ignored. Require Once also generates a Fatal error and halts the script execution ,if file is not found on specified location or path.

Syntax:- require_once(“file_name.php”);

10. What are constructor and destructor in PHP ?

PHP constructor and a destructor are special type functions which are automatically called when a PHP class object is created and destroyed.

Generally Constructor are used to intializes the private variables for class and Destructors to free the resources created /used by class .


 
Here is sample class with constructor and destructer in PHP.


<?php
class Foo {
   
    private $name;
    private $link;

    public function __construct($name) {
        $this->name = $name;
    }

    public function setLink(Foo $link){
        $this->link = $link;
    }

    public function __destruct() {
        echo 'Destroying: ', $this->name, PHP_EOL;
    }
}
?>
11. List data types in PHP ?

PHP supports 9 primitive types

4 scalar types:

integer
boolean
float
string
3 compound types:

array
object
callable
And 2 special types:

resource
NULL
Read Zend Framework interview questions

12. Explain Type hinting in PHP ?

In PHP Type hinting is used to specify the excepted data type of functions argument.
Type hinting is introduced in PHP 5.

Example usage:-

//send Email function argument $email Type hinted of Email Class. It means to call this function you must have to pass an email object otherwise an error is generated.


<?php
function sendEmail (Email $email)
{
  $email->send();
}
?>
13. How to increase the execution time of a PHP script ?

The default max execution time for PHP scripts is set to 30 seconds. If a php script runs longer than 30 seconds then PHP stops the script and reports an error.
You can increase the execution time by changing max_execution_time directive in your php.ini file or calling ini_set(‘max_execution_time’, 300); //300 seconds = 5 minutes function at the top of your php script.

14. What is purpose of @ in Php ?

In PHP @ is used to suppress error messages.When we add @ before any statement in php then if any runtime error will occur on that line, then the error handled by PHP

15. What are different types of errors available in Php ?

There are 13 types of errors in PHP, We have listed all below

E_ERROR: A fatal error that causes script termination.
E_WARNING: Run-time warning that does not cause script termination.
E_PARSE: Compile time parse error.
E_NOTICE: Run time notice caused due to error in code.
E_CORE_ERROR: Fatal errors that occur during PHP initial startup.
(installation)
E_CORE_WARNING: Warnings that occur during PHP initial startup.
E_COMPILE_ERROR: Fatal compile-time errors indication problem with script.
E_USER_ERROR: User-generated error message.
E_USER_WARNING: User-generated warning message.
E_USER_NOTICE: User-generated notice message.
E_STRICT: Run-time notices.
E_RECOVERABLE_ERROR: Catchable fatal error indicating a dangerous error
E_ALL: Catches all errors and warnings.
16. What is difference between strstr() and stristr() ?

In PHP both functions are used to find the first occurrence of substring in a string except
stristr() is case-insensitive and strstr is case-sensitive,if no match is found then FALSE will be returned.

Sample Usage:


<?php 
$email = ‘abc@xyz.com’;
$hostname = strstr($email, ‘@’);
echo $hostname;
output: @xyz.com
stristr() does the same thing in Case-insensitive manner
?>
17. Code to upload a file in PHP ?

//PHP code to process uploaded file and moving it on server


if($_FILES['photo']['name'])
{
	//if no errors...
	if(!$_FILES['file']['error'])
	{
		//now is the time to modify the future file name and validate the file
		$new_file_name = strtolower($_FILES['file']['tmp_name']); //rename file
		if($_FILES['file']['size'] > (1024000)) //can't be larger than 1 MB
		{
			$valid_file = false;
			$message = 'Oops!  Your file\'s size is to large.';
		}
		
		//if the file has passed the test
		if($valid_file)
		{
			//move it to where we want it to be
			move_uploaded_file($_FILES['file']['tmp_name'], 'uploads/'.$new_file_name);
			$message = 'File uploaded successfully.';
		}
	}
	//if there is an error...
	else
	{
		//set that to be the returned message
		$message = 'Something got wrong while uploading file:  '.$_FILES['file']['error'];
	}
}
18. How to get length of an array in PHP ?

PHP count function is used to get the length or numbers of elements in array


<?php
// initializing an array in PHP
$array=['a','b','c'];
// Outputs 3 
echo count($array);
?>
19. Code to open file download dialog in PHP ?

You can open a file download dialog in php by setting Content-Disposition in header.

Here is a usage sample:-


// outputting a PDF file
header('Content-type: application/pdf');
// It will be called downloaded.pdf
header('Content-Disposition: attachment; filename="downloaded.pdf"');
// The PDF source is in original.pdf
readfile('original.pdf');

20. Is multiple inheritance supported in PHP ?

NO, multiple inheritance is not supported by PHP

21. How to Pass JSON Data in a URL using CURL in PHP ?

Code to post JSON Data in a URL using CURL in PHP


$url='http://onlineinterviewquestions.com/get_details';
$jsonData='{"name":"phpScots","email":"phpscots@onlineinterviewquestions.com",'age':36}';
$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 0);
curl_setopt($ch, CURLOPT_POSTFIELDS, $jsonData);
curl_close($ch);



22. How is a constant defined in a PHP script?

Defining a Constant in PHP

define('CONSTANT_NAME',value); 
23. How to get no of arguments passed to a PHP Function?

func_get_args() function is used to get number of arguments passed in a PHP function.

Sample Usage:


function foo() {
   return  func_get_args();
}
echo foo(1,5,7,3);//output 4;
echo foo(a,b);//output 2;
echo foo();//output 0;

24. What are the encryption functions available in PHP ?

crypt(),Mcrypt(),hash() are used for encryption in PHP

25. What is the difference between unset and unlink ?

Unlink: Is used to remove a file from server.
usage:unlink(‘path to file’);

Unset: Is used unset a variable.
usage: unset($var);

26. What is the use of Mbstring?

Mbstring
Mbstring is an extension used in PHP to handle non-ASCII strings. Mbstring provides multibyte specific string functions that help us to deal with multibyte encodings in PHP. Multibyte character encoding schemes are used to express more than 256 characters in the regular byte-wise coding system. Mbstring is designed to handle Unicode-based encodings such as UTF-8 and UCS-2 and many single-byte encodings for convenience PHP Character Encoding Requirements.

You may also Like Codeigniter interview questions

Below are some features of mbstring
It handles the character encoding conversion between the possible encoding pairs.
Offers automatic encoding conversion between the possible encoding pairs.
Supports function overloading feature which enables to add multibyte awareness to regular string functions.
Provides multibyte specific string functions that properly detect the beginning or ending of a multibyte character. For example, mb_strlen() and mb_split()
27. How to get number of days between two given dates using PHP ?

<?php
$tomorrow = mktime(0, 0, 0, date(“m”) , date(“d”)+1, date(“Y”));
$lastmonth = mktime(0, 0, 0, date(“m”)-1, date(“d”), date(“Y”));
echo ($tomorrow-$lastmonth)/86400;
?>

28. How will you calculate days between two dates in PHP?

Calculating days between two dates in PHP

<?Php 
$date1 = date('Y-m-d');
$date2 = '2015-10-2';
$days = (strtotime($date1)-strtotime($date2))/(60*60*24);
echo $days;
?>
29. What is Cross-site scripting?

Cross-site scripting (XSS) is a type of computer security vulnerability typically found in web applications. XSS enables attackers to inject client-side script into web pages viewed by other users. A cross-site scripting vulnerability may be used by attackers to bypass access controls such as the same-origin policy.

30. What are the difference between echo and print?

Difference between echo and print in PHP

echo in PHP
echo is language constructs that display strings.
echo has a void return type.
echo can take multiple parameters separated by comma.
echo is slightly faster than print.
Print in PHP
print is language constructs that display strings.
print has a return value of 1 so it can be used in expressions.
print cannot take multiple parameters.
print is slower than echo.
31. What is namespaces in PHP?

PHP Namespaces provide a way of grouping related classes, interfaces, functions and constants.

# define namespace and class in namespace
namespace Modules\Admin\;
class CityController {
}
# include the class using namesapce
use Modules\Admin\CityController ;
32. What are different types of Print Functions available in PHP?

PHP is a server side scripting language for creating dynamic web pages. There are so many functions available for displaying output in PHP. Here, I will explain some basic functions for displaying output in PHP. The basic functions for displaying output in PHP are as follows:

print() Function
echo() Function
printf() Function
sprintf() Function
Var_dump() Function
print_r() Function
33. What are the differences between GET and POST methods in form submitting, give the case where we can use get and we can use post methods?

In PHP, one can specify two different submission methods for a form. The method is specified inside a FORM element, using the METHOD attribute. The difference between METHOD=”GET” (the default) and METHOD=”POST” is primarily defined in terms of form data encoding. According to the technical HTML specifications, GET means that form data is to be encoded (by a browser) into a URL while POST means that the form data is to appear within the message body of the HTTP request.

Get	Post
History:	Parameters remain in browser history because they are part of the URL	Parameters are not saved in browser history.
Bookmarked:	Can be bookmarked.	Can not be bookmarked.
BACK button/re-submit behavior:	GET requests are re-executed but may not be re-submitted to the server if the HTML is stored in the browser cache.	The browser usually alerts the user that data will need to be re-submitted.
Encoding type (enctype attribute):	application/x-www-form-urlencoded	multipart/form-data or application/x-www-form-urlencoded Use multipart encoding for binary data.
Parameters:	can send but the parameter data is limited to what we can stuff into the request line (URL). Safest to use less than 2K of parameters, some servers handle up to 64K	Can send parameters, including uploading files, to the server.
Hacked:	Easier to hack for script kiddies	More difficult to hack
Restrictions on form data type:	Yes, only ASCII characters allowed.	No restrictions. Binary data is also allowed.
Security:	GET is less secure compared to POST because data sent is part of the URL. So it’s saved in browser history and server logs in plaintext.	POST is a little safer than GET because the parameters are not stored in browser history or in web server logs.
Restrictions on form data length:	Yes, since form data is in the URL and URL length is restricted. A safe URL length limit is often 2048 characters but varies by browser and web server.	No restrictions
Usability:	GET method should not be used when sending passwords or other sensitive information.	POST method used when sending passwords or other sensitive information.
Visibility:	GET method is visible to everyone (it will be displayed in the browsers address bar) and has limits on the amount of information to send.	POST method variables are not displayed in the URL.
Cached:	Can be cached	Not Cached
Large variable values:	7607 characters maximum size.	8 Mb max size for the POST method.

34. Why should I store logs in a database rather than a file?

A database provides more flexibility and reliability than does logging to a file. It is easy to run queries on databases and generate statistics than it is for flat files. Writing to a file has more overhead and will cause your code to block or fail in the event that a file is unavailable. Inconsistencies caused by slow replication in AFS may also pose a problem to errors logged to files. If you have access to MySQL, use a database for logs, and when the database is unreachable, have your script automatically send an e-mail to the site administrator.

35. How to add 301 redirects in PHP?

You can add 301 redirect in PHP by adding below code snippet in your file.

header("HTTP/1.1 301 Moved Permanently"); 
header("Location: /option-a"); 
exit();

36. How can you get web browser’s details using PHP?

37. How to access standard error stream in PHP?

You can access standard error stream in PHP by using following code snippet:

$stderr = fwrite("php://stderr");

$stderr = fopen("php://stderr", "w");

$stderr = STDERR;