# Issue 9834: Make desolve more informative when solving BVP

Issue created by migration from Trac.

Original creator: robert.marik

Original creation time: 2010-08-28 21:18:27

Assignee: burcin

CC:  mhampton

From Sage Bugreports :
confusing error message


```
Traceback (click to the left of this block for traceback)
...
UnboundLocalError: local variable 'maxima_method' referenced before
assignment
```

when trying

```
epsilon = 1e-2; vars = var('x'); y = function('y',x);
de = epsilon*diff(y,x,2)+y*(1-y^2)==0;
soln = desolve(de,y[0,-1,1,1]);
```


Explanation: Currently Sage allows to use BVP only if the result is symbolic expression. In this case the result is list of two expresions and Sage fails, as mentioned very briefly in documentation of desolve. However, we could try to improve desolve or make the error message more informative.


---

Comment by robert.marik created at 2010-08-29 19:37:59

Changing status from new to needs_review.


---

Comment by robert.marik created at 2010-08-29 19:37:59

The patch

* solves the problem

* fixes documentation

* decreases number of spawned Maxima sessions into one session


---

Comment by kcrisman created at 2010-09-21 13:15:28

One very minor comment - no time to review now:

```
. Remove the initial contition t
```

at the very end of the patch should be "condition".

Do you think it would be worth adding another doctest to show that the sage-support request is fixed as well:

```
var('t alpha beta n') 
x=function('x',t) 
eq=diff(x,t)^2==alpha-beta abs(x)^n 
assume(n,'integer') 
desolve(eq,x,ivar=t,contrib_ode=True) 
```


Thanks for finding and fixing this!


---

Comment by robert.marik created at 2010-09-21 13:31:51

Thanks, I will update the patch as time permits.

The equation from sage-support still fails, since Maxima fails to solve it.  Anyway. Sage and Maxima now know that n is integer.

```
marik`@`um-bc107:/opt/sage-4.5.3-Debian_Lenny_64-x86_64-Linux$ ./sage --maxima
;;; Loading #P"/opt/sage-4.5.3-Debian_Lenny_64-x86_64-Linux/local/lib/ecl/defsys tem.fas"
;;; Loading #P"/opt/sage-4.5.3-Debian_Lenny_64-x86_64-Linux/local/lib/ecl/cmp.fa s"
;;; Loading #P"/opt/sage-4.5.3-Debian_Lenny_64-x86_64-Linux/local/lib/ecl/sysfun .lsp"
Maxima 5.20.1 http://maxima.sourceforge.net
using Lisp ECL 10.2.1
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
(%i1) declare(n,integer);
(%o1)                                done
(%i2) eq: 'diff(x,t)^2=alpha-beta*abs(x)^n;
                          dx 2                      n
(%o2)                    (--)  = alpha - beta abs(x)
                          dt
(%i3) load('contrib_ode)$

(%i4) contrib_ode(eq,x,t);
                          dx 2                      n
(%t4)                    (--)  = alpha - beta abs(x)
                          dt

                     first order equation not linear in y'

Improper argument to ratcoeff:
0
#0: linear2(expr=x,x=0)(ode2.mac line 75)
#1: ode1_a(phi=-sqrt(alpha-beta*abs(x)^n),y=x,x=t)(ode1_lie.mac line 176)
#2: ode1_lie(phi=-sqrt(alpha-beta*abs(x)^n),y=x,x=t)(ode1_lie.mac line 54)
 -- an error. To debug this try: debugmode(true);

```



---

Comment by mhampton created at 2010-09-21 13:51:27

This doesn't seem fixed to me:

```
sage: epsilon = 1e-2; vars = var('x'); y = function('y',x);
sage: de = epsilon*diff(y,x,2)+y*(1-y^2)==0;
sage: soln = desolve(de,y[0,-1,1,1])
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/mh/<ipython console> in <module>()

TypeError: 'sage.symbolic.expression.Expression' object is unsubscriptable
```



---

Comment by mhampton created at 2010-09-21 13:58:04

Even after fixing the sytax I still get an error:

```
sage: vars = var('x'); y = function('y',x);
sage: soln = desolve(diff(y,x,2) + 100*y*(1-y^2),dvar=y,ivar=x,ics=[0,-1,1,1])
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)

/Users/mh/<ipython console> in <module>()

/Users/mh/sagestuff/sage-4-x/local/lib/python2.6/site-packages/sage/calculus/desolvers.pyc in desolve(de, dvar, ics, ivar, show_method, contrib_ode)
    436             maxima_method=P("method")
    437         if not is_SymbolicEquation(soln.sage()):
--> 438              raise NotImplementedError, "Unable to use initial condition for this equation (%s)."%(str(maxima_method).strip())   
    439         if len(ics) == 2:
    440             tempic=(ivar==ics[0])._maxima_().str()

NotImplementedError: Unable to use initial condition for this equation (freeofx).
```



---

Comment by mhampton created at 2010-09-21 13:58:04

Changing assignee from burcin to mhampton.


---

Comment by robert.marik created at 2010-09-21 14:10:19

Thanks for menitioning this. 

Wihtout this patch we get

```
----------------------------------------------------------------------
----------------------------------------------------------------------
The Sage install tree may have moved.
Regenerating Python.pyo and .pyc files that hardcode the install PATH
(please wait at most a few minutes)...
Do not interrupt this.
sage: vars = var('x'); y = function('y',x);
sage: soln = desolve(diff(y,x,2) + 100*y*(1-y^2),dvar=y,ivar=x,ics=[0,-1,1,1])
---------------------------------------------------------------------------
UnboundLocalError                         Traceback (most recent call last)
| Sage Version 4.5.3, Release Date: 2010-09-04                       |
| Type notebook() for the GUI, and license() for information.        |
/opt/sage-4.5.3-Debian_Lenny_64-x86_64-Linux/<ipython console> in <module>()

/opt/sage-4.5.3-Debian_Lenny_64-x86_64-Linux/local/lib/python2.6/site-packages/sage/calculus/desolvers.py in desolve(de, dvar, ics, ivar, show_method, contrib_ode)
    358     if (ics is not None):
    359         if not is_SymbolicEquation(soln.sage()):
--> 360              raise NotImplementedError, "Maxima was unable to use initial condition for this equation (%s)"%(maxima_method.str())
    361         if len(ics) == 2:
    362             tempic=(ivar==ics[0])._maxima_().str()

UnboundLocalError: local variable 'maxima_method' referenced before assignment
```

and the user does not know, what went wrong. With this patch the user knows, that it Sage is not capable to use initial conditions for this ODE.


---

Attachment

rebased for Sage 4.5.3., fixed typo, replaces previous patch with the same name


---

Comment by robert.marik created at 2010-09-21 20:16:48

solves also #9710 and #8931


---

Attachment

minor change - apply only this patch


---

Comment by burcin created at 2010-09-26 13:31:13

Patch looks good and it solves a whole bunch of problems, so I'd like to give this a positive review.

I have one minor suggestion. The if clause on line 435-436 only serves the purpose of assigning a value to `maxima_method` to show in the error message. attachment:trac_9835.take2.patch moves these lines right before we raise the error, so that they are not executed unnecessarily.

I give a positive review to Robert's changes. Please switch this to a positive review if you agree with mine.


---

Comment by robert.marik created at 2010-09-27 07:36:21

Positive review to Burcin's change. Thank you.

Release manager: apply only attachment:trac_9835.take2.patch


---

Comment by robert.marik created at 2010-09-27 07:36:21

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-28 09:11:40

Resolution: fixed


---

Comment by mpatel created at 2010-09-28 10:36:28

Thanks, David!
