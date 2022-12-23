# Issue 6403: Custom definitions for latex style

Issue created by migration from https://trac.sagemath.org/ticket/6403

Original creator: schymans

Original creation time: 2009-06-25 12:30:37

CC:  mvngu

Keywords: latex

#6290 introduced a way to custom-define the latex style of functions, but it would be great if something similar was made possible for any variable. I used to do it in the following way, but now I get an error message:

sage: var('hi kunsati delyui')

sage: hi._latex_ = lambda: 'h_i'
     
sage: kunsati._latex_ = lambda: 'K_{unsat,i}' 
   
sage: delyui._latex_ = lambda: '\delta_{yu,i}'

  
Traceback (most recent call last):


...

AttributeError: 'sage.symbolic.expression.Expression' object attribute '_latex_' is read-only


Comment by Burcin Erocal on sage-devel (25/06/2006):

>Since Expression is a cython class, you cannot overwrite the _latex_() method. 
>
>Pynac supports setting latex names for variables at creation, but this functionality is not exposed in the wrapper. Another solution by hacking latex_variable_name() might be possible, but I would like to avoid that if possible.
>
>Feel free to open a new issue in trac about it.
>
>Cheers,
>Burcin

How could the Pynac funtionality of setting latex names for variables at creation be exposed?


---

Comment by jason created at 2009-11-10 15:18:32

There is no patch above, though the title said there was a patch.


---

Comment by schymans created at 2009-11-10 16:11:44

Supposedly, the patch for #6559 fixes this (see comment added to description). Could you review #6559 instead? Thanks!

Stan


---

Comment by burcin created at 2010-02-19 11:56:51

Resolution: fixed


---

Comment by burcin created at 2010-02-19 11:56:51

I'm closing this, since #6559 just got merged. It adds a `latex_name` keyword argument to `var()`, which is the functionality requested here.
