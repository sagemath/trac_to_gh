# Issue 8931: desolve

Issue created by migration from Trac.

Original creator: descopau

Original creation time: 2010-05-08 07:41:36

Assignee: burcin

CC:  robert.marik kcrisman

Keywords: desolve

I want to solve f''/f=k with k in R



```
sage:  x=var('x')
sage: f=function('f',x)
sage: k=var('k')
sage: assume(k>0)
sage:  desolve(diff(f(x),x,2)/f(x)==k,[f,x]) 
```


and sage keeps answering :



```
TypeError                                 Traceback (most recent call last)

/home/moi/<ipython console> in <module>()

/home/moi/sage-4.4.1-linux-32bit-ubuntu_9.10-i686-Linux/local/lib/python2.6/site-packages/sage/calculus/desolvers.pyc in desolve(de, dvar, ics, ivar, show_method, contrib_ode)
    338     # we produce string like this
    339     # ode2('diff(y,x,2)+2*'diff(y,x,1)+y-cos(x),y(x),x)
--> 340     soln = maxima(cmd)
    341 
    342     if str(soln).strip() == 'false':

/home/moi/sage-4.4.1-linux-32bit-ubuntu_9.10-i686-Linux/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __call__(self, x, name)
   1030             
   1031         if isinstance(x, basestring):
-> 1032             return cls(self, x, name=name)
   1033         try:
   1034             return self._coerce_from_special_method(x)

/home/moi/sage-4.4.1-linux-32bit-ubuntu_9.10-i686-Linux/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __init__(self, parent, value, is_name, name)
   1449             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:
   1450                 self._session_number = -1
-> 1451                 raise TypeError, x
   1452         self._session_number = parent._session_number
   1453 

TypeError: Computation failed since Maxima requested additional constraints (try the command 'assume(k>0)' before integral or limit evaluation, for example):
Is  k  positive, negative, or zero?
```


so I tried :





```
sage:  desolve(diff(f(x),x,2)/f(x)==k^2+1,[f,x])
```


and I got :


```
k1*e^(I*sqrt(-k^2 - 1)*x) + k2*e^(-I*sqrt(-k^2 - 1)*x)
```


!!




---

Comment by monkey created at 2010-08-14 00:46:30

I have the same problem solving a different equation:

```
var('L1 L2 C1 C2 L3 C3 t')
forget()
assume(L2 > 0)
assume(L3 > 0)
assume(C2 > 0)
assume(C3 > 0)
j = function('j',t)
eqn = diff(v_i,t) - L2*diff(j,t,2) - j/C2 == L3*diff(j,t,2) + j/C3
desolve(eqn,[j,t],[0,1])
```


returns


```
Traceback (click to the left of this block for traceback)
...
Is  C2*C3*(C3+C2)*(L3+L2)  positive, negative, or zero?
```


The only quick workaround I have found is to specify the values of the constants, but I really need them to be symbolic.  The best I can do is use primes for values of constants and after several such sets you can get a picture of how the constants are related to the numbers in the solution terms, but it's an ass-ache.

I think the best solution would be to have an optional argument to desolve which answers the question posed if there are not sufficient assumptions/conditions to already determine the correct answer.

Really appreciate the great work so far guys! :D


---

Comment by robert.marik created at 2010-09-21 20:15:38

with #9835

```
marik`@`um-bc107:/opt/sage$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: x=var('x'); f=function('f',x); k=var('k'); assume(k>0)
sage: desolve(diff(f,x,2)/f==k,f,ivar=x)
k1*e^(sqrt(k)*x) + k2*e^(-sqrt(k)*x)
```



---

Attachment


---

Comment by fstan created at 2010-12-09 02:17:10

The patch adds a doc test for this issue.


---

Comment by fstan created at 2010-12-09 02:17:10

Changing status from new to needs_review.


---

Comment by kcrisman created at 2011-03-12 05:33:45

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2011-03-12 05:33:45

Applies cleanly to 4.7.alpha1, passes tests, clearly fixes the issue, looks good in the documentation.  Positive review.

Not sure what to do on the author; fstan is the person I have put, as the person who posted the patch, but before it had G. Cannon.  Unless fstan comments on this, let's leave her as the author.


---

Comment by jdemeyer created at 2011-04-05 15:56:38

Resolution: fixed
