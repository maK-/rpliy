<html>
<pre>
About this project.
-----------------------------
</pre>
<pre>
This was an old project that I decided to refactor and finish. 
I understand it may not fully meet the requirements of the assignment 
spec but I didn't want to simply implement a non-useful set of classes just to
try out a new Design pattern. This project has given me an introduction to a 
few different design patterns, some of which I was unaware of before the SPAM
module and I feel I understand them better after completing this assignment.
Below you will find some of the software patterns appearing in this 
project.

There were a few places I could have implemented these patterns in a more
"solid to the definition" fashion but I decided against simply because it
would result in unnecessary complexity and robustness. This was mainly due 
to the layout of my previous implementation. I feel through the use of design
patterns, I have improved slightly the quality of my code and indirectly the 
flexibility for potential growth/improvement with this project.



</pre>



<pre>
Design Patterns Used
------------------------------
</pre>

<h3>== MVC Pattern ==</h3>
<pre>
The web framework "web.py" is losely based on the MVC (Model-View-Controller) 
software pattern. The only difference is that the model and controller 
elements are encapsulated within the framework and are not exposed as 
openly as in most MVC frameworks. Our view is seperated out into template 
files which you can see in this assignment are the following
main.html, search.html and playlist.html. This is the user interface 
part of the application.</pre>

<pre>The controller element of this framework controls a base set of "model"
classes. It is possible to describe that this control/model layout also losely
adheres the command software pattern. Our controller redirects our
web requests to a command class or model that then carries out our database
information retrieval to be displayed in the view or template html file.
The model command classes also handle any data passed into our application
from our user.</pre>

<h3>== Command Pattern ==</h3>
<pre>This isn't an exact representation of the Command pattern but it does have many
concrete similarities. The client makes a request to the web server (web.py). 
The location or url they visit has a specific command class. This command 
class implements a request interface. The methods that get executed described 
in this interface are GET and POST. This represents a GET request and a POST 
request. The url location is mapped directly to a Command class or model. 
Our model actions are carried out and then the remaining data or commands are 
received or viewed in the template html user interface.</pre>

<h3>== Facade Pattern ==</h3>
<pre>Again this isn't my own work but the jQuery library could be considered a 
facade pattern as it very simply encapsulates quite complex javascript code
into very simple small set of functions.</pre>

<h3>== Observer Pattern ==</h3>
<pre>jQuery.Callbacks() provides a very useful and simple way of implementing
callback lists. Using this function it makes it very easy to implemented an
observer pattern or a subscribe/publish pattern. I used this to test fire a function
that adds a song to the playlist, it also makes the list item disappear.</pre>
</html>
