# Issue 6479: desolve for 2nd order ODE with initial condition gives wrong answer

Issue created by migration from Trac.

Original creator: gmhossain

Original creation time: 2009-07-08 11:08:56

Assignee: burcin

CC:  hamptonio@gmail.com


```
sage: y(x) = function('y',x)
sage: desolve( y(x).diff(x,2) == 0, y(x))
k2*x + k1
sage: desolve( y(x).diff(x,2) == 0, y(x), [0,0,1])
x + y(0)
sage: desolve( y(x).diff(x,2) == 0, y(x), [0,1,1])
x + y(0)
```


It seems desolve instead of using the given initial
value of y at x=0,  it literally passes "y(0)" to maxima.



---

Comment by wdj created at 2009-07-08 13:07:39

I'm not sure if this is a duplicate or not but Robert Bradshaw definitely knows about this bug. (I wrote a crappy version of the original solver, Robert wrote the new and improved one. However, Marshall Hampton and I spend several hours at SD15 trying to figure out how to patch this bug and couldn't.) BTW, it is actually documented to behave this way if you read the docstrings carefully.

Here is, at Robert Bradshaw's request, a *maxima* session solving a 2nd order ODE with 2 initial conditions and a 2nd order ODE with 2 boundary conditions:


```
sage: maxima.eval("de:'diff(y,x,2) + y*'diff(y,x)^3 = 0")
"'diff(y,x,2)+y*('diff(y,x,1))^3=0"
sage: maxima.eval("ode2(de,y,x)")
'(y^3+6*%k1*y)/6=x+%k2'
sage: maxima.eval("soln:ode2(de,y,x)")
'(y^3+6*%k1*y)/6=x+%k2'
sage: maxima.eval("bc2(soln,x=0,y=1,x=1,y=3)")
'(y^3-10*y)/6=x-3/2'
sage: maxima.eval("de:'diff(y,x,2) + 4*y = 0")
"'diff(y,x,2)+4*y=0"
sage: maxima.eval("soln:ode2(de,y,x)")
'y=%k1*sin(2*x)+%k2*cos(2*x)'
sage: maxima.eval("bc2(soln,x=0,y=1,x=1,y=3)")
'y=cos(2*x)-(cos(2)-3)*sin(2*x)/sin(2)'
sage: maxima.eval("ic2(soln,x=0,y=1,'diff(y,x)=3)")
'y=3*sin(2*x)/2+cos(2*x)'
```

Hope this helps.

An additional problem is that the syntax for desolve and desolve_laplace are different. Perhaps this could be fixed at the same time?


---

Attachment


---

Comment by robert.marik created at 2009-10-06 16:51:00

The patch which fixes ic2 and bc2 commands is attached. With this patch, the ode2 runs two times - the first pass is kept to ensure that Maxima is able to solve the system.

Test for bc2 has been added.
The problem related to desolve_laplace has not been solved - perhaps need more work. As I understand, the corresponding command in Maxima allows to solve systems of equations and the function in Maxima is designed for one equation only.


---

Comment by robert.marik created at 2009-10-07 04:56:19

Changing status from needs_review to needs_work.


---

Comment by robert.marik created at 2009-10-07 04:56:19

Patch hass been posted, but it assumes that the solution of second order ODE is found in the explicit form, i.e. y=f(x) which is not allways true. From this reason the patch does not solve all related issues and needs more work. I hope to post new patch within a week.


---

Comment by robert.marik created at 2009-10-07 13:22:58

Apply only this patch


---

Attachment


---

Comment by robert.marik created at 2009-10-07 13:24:57

Changing status from needs_work to needs_review.


---

Attachment

Apply on the top of the patch trac_6479_marik_revised.patch  and on the top pf the patch for Ticket #385 http://trac.sagemath.org/sage_trac/ticket/385


---

Comment by robert.marik created at 2009-10-13 13:55:00

I attached second patch which should be applied after the previous trac_6479_marik_revised.patch and after a patch for Ticket #385.

With this new patch

* we can solve more differential equations (clairot, lagrange, ...)

* desolve Laplace does not return string and the initial conditions do not persist in the system

* added a simple interface to runge kutta methods from maxima


---

Comment by wdj created at 2009-10-17 20:11:11

The improvements are *fantastic*!

However, some of the docstrings do not follow proper format.
For example, in your desolve_rk4 function, you do not indent
the Sage code in the EXAMPLES section correctly. Also, if a
function can produce different types of output (eg, a plot or
a list of points, depending on the optional parameters), both
should be illustrated in the examples. I don't know if this
improper formatting screws up the sage -test script or not.
There is also some improper indentation in other sections, 
such as OUTPUT, for functions such as desolve_rk4, for example.

I hope you can please fix these. 

A request: in your new functions desolve_rk4 and desolve_system_rk4
there is an option called endpoint, with default value 10. I would 
prefer an option called endpoints with a default value of [0,10]
(or something), so that a range can be plotted other than from
ics[0] to endpoint. If it is too much hassle, fine (you can just add 
plots together to get that anyway...).


---

Comment by wdj created at 2009-10-17 20:11:11

Changing status from needs_review to needs_work.


---

Comment by robert.marik created at 2009-10-25 19:22:16

Replying to [comment:10 wdj]:
> The improvements are *fantastic*!
> 
> However, some of the docstrings do not follow proper format.
> For example, in your desolve_rk4 function, you do not indent
> the Sage code in the EXAMPLES section correctly. Also, if a
> function can produce different types of output (eg, a plot or
> a list of points, depending on the optional parameters), both
> should be illustrated in the examples. I don't know if this
> improper formatting screws up the sage -test script or not.
> There is also some improper indentation in other sections, 
> such as OUTPUT, for functions such as desolve_rk4, for example.
> 
> I hope you can please fix these. 

Thanks. I will try to fix it. Sorry, I am newbie in Python.

> 
> A request: in your new functions desolve_rk4 and desolve_system_rk4
> there is an option called endpoint, with default value 10. I would 
> prefer an option called endpoints with a default value of [0,10]
> (or something), so that a range can be plotted other than from
> ics[0] to endpoint. If it is too much hassle, fine (you can just add 
> plots together to get that anyway...).

what about this:

endpoints=a   .... integrate from ics[0] to a

endpoints=[a]   .... integrate from ics[0] to a

endpoints=[a,b]   .... integrate from ics[0] to b, then integrate back from ics[0] to a, reverse the second list and join both lists together /without repeating the point (ics[0],ics[1])/. If ics[0] is bigger than b or smaller than a, raise error.

I think that this is possible and I can try within a week.


---

Comment by wdj created at 2009-10-25 20:15:47

Replying to [comment:11 robert.marik]:
> Replying to [comment:10 wdj]:

...

> > A request: in your new functions desolve_rk4 and desolve_system_rk4
> > there is an option called endpoint, with default value 10. I would 
> > prefer an option called endpoints with a default value of [0,10]
> > (or something), so that a range can be plotted other than from
> > ics[0] to endpoint. If it is too much hassle, fine (you can just add 
> > plots together to get that anyway...).
> 
> what about this:
> 
> endpoints=a   .... integrate from ics[0] to a
> 
> endpoints=[a]   .... integrate from ics[0] to a
> 
> endpoints=[a,b]   .... integrate from ics[0] to b, then integrate back from ics[0] to a, reverse the second list and join both lists together /without repeating the point (ics[0],ics[1])/. If ics[0] is bigger than b or smaller than a, raise error.
> 
> I think that this is possible and I can try within a week.


This sounds excellent - thanks!


---

Comment by robert.marik created at 2009-10-27 20:22:59

this replaces previous patches and installs on the top of patch for trac #385


---

Attachment


---

Comment by robert.marik created at 2009-10-27 20:23:47

Changing status from needs_work to needs_review.


---

Comment by wdj created at 2009-10-31 15:50:10

Changing status from needs_review to positive_review.


---

Comment by wdj created at 2009-10-31 15:50:10

Great patch. Passes sage -testall and is very well-documented.

Thanks Robert!!


---

Comment by mhansen created at 2009-11-29 10:10:24

Resolution: fixed


---

Comment by robert.marik created at 2010-04-07 11:10:57

Thanks for including the patch to Sage. 
The work on this patch has been supported by the grant GA201/07/0145 of the Czech Grant Agency.
