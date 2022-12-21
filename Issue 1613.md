# Issue 1613: interactive manipulation of variables using AJAX in notebook

Issue created by migration from Trac.

Original creator: schilly

Original creation time: 2007-12-27 23:45:10

Assignee: boothby

CC:  jason-sage@creativetrax.com

Like the "*Manipulate*" function in _Mathematica_, SAGE could include a similar feature using AJAX.


*The idea is, to introduce a widget (slider, drop down, boolean button, list of option-buttons,...) that changes the value of a variable interactively. is a new value set, the cell is evaluated and the new result is shown.*



my idea for the syntax: every time the input field has a manipulate function, a variable assignment is done before the expression is evaluated. 

example: manipulate(plot(sin(n*x),x),{'n':range(-3,3)})

where n is chosen from the range of integers between -3 and 3. (syntax is only an example, could be better, but an associative array seems applicable. (just manipulate(expr, var, range, var2, range) should work, too)

the manipulate should also work appended: expression.manipulate(var,range,...)



the server sends suitable html code back, which could consist of a lightweight horizontal slider for each variable, which does appropriate rounding  to integers (or smaller/larger intervals) and everytime a mouse-up event is issued, the cell is reevaluated with the new variable assignment.



note: mathematica goes a step further using dynamic elements, which update throughout the entire notebook after a new assignment is done. this is more complicated, since there must be a mechanism to register a cell in a client/observer manner. this could be addressed later... (and of course, issues of looping...)


---

Comment by jason created at 2007-12-28 01:25:34

See #1322 for an alpha patch which       together a very shaky implementation of this.  Is this writeup an expanded version of #1322?


---

Comment by schilly created at 2007-12-28 11:14:05

thx for pointing out #1322 ... i was unaware of it. My idea is similar, but much more general. When I have time and understand how sage works I'll try to do a patch, too, but this won't be very soon ;)


---

Comment by jason created at 2008-01-02 00:47:50

Possible implementation notes:

We probably want to have the code that we plan to reevaluate in quotes so that we can just eval it and it isn't evaluated when it is passed to the function, i.e., manipulate("plot(sin(n*x),x)",{'n':range(-3,3)}).  

When the code is evaluated, it creates a slider and a separate output area.

When the slider is moved, the following code is executed:

n=<NEW SLIDER VALUE>
plot(sin(n*x),x)

and the output is put into the separate output area.


---

Comment by was created at 2008-02-07 07:28:52

Resolution: duplicate
