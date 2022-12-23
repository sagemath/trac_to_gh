# Issue 6423: Sage not always understanding i=sqrt(-1)  - Maxima bug proably

Issue created by migration from https://trac.sagemath.org/ticket/6423

Original creator: drkirkby

Original creation time: 2009-06-26 14:54:37

Assignee: tbd

Vladimir Bondarenko (a developer of software to test computer algebra systems - see [http://www.cas-testing.org/](http://www.cas-testing.org/) ), had been playing with [http://demo.sagenb.org/](http://demo.sagenb.org/) and noted the following:

```
exp(-x^i).integral(x,0,1)  returns

Traceback (click to the left for traceback)
...
Is %i an integer?

Ouch! Any Sage comments?
```


When I reported his on sage-devel, William Stein said:

''A large amount of the symbolic functionality that uses Maxima has
issues like this, but unfortunately there is basically nothing we can do about it, except continue with projects to rewrite the parts of Sage that call Maxima so that they don't call Maxima.  So this class of bugs should be very good motivation to continue to work on
implementing symbolic integration ourselves (and/or further improving sympy!).''

He then went on to say he wanted it reported as a TRAC bug but was busy, so I have done it on his behalf. 

I don't feel able to comment much more on this, and personally don't intend trying to fix it (outside my knowledge), so I've just reported it. 

Can someone else add appropriate priority, milestones, keywords etc, as this is completely outside my _comfort zone_. 

David Kirkby


---

Comment by AlexGhitza created at 2009-07-05 05:51:30

Changing assignee from tbd to burcin.


---

Comment by AlexGhitza created at 2009-07-05 05:51:30

Changing component from algebra to calculus.


---

Comment by AlexGhitza created at 2009-08-24 09:33:06

This is fixed by the spkg and patch at #6699.  I will put up a patch with a doctest here when #6699 gets merged.


---

Comment by AlexGhitza created at 2009-08-24 09:33:06

Changing assignee from burcin to AlexGhitza.


---

Comment by kcrisman created at 2009-09-29 14:56:14

Unfortunately, it seems not.  From uw.sagenb.org:


```
sage: exp(-x^i).integral(x,0,1)
Traceback (most recent call last):
...
TypeError: Computation failed since Maxima requested additional constraints (try the command 'assume(i>0)' before integral or limit evaluation, for example):
Is %i an integer?
sage: maxima.eval('integrate(exp(-x^%i),x,0,1);')
Traceback (most recent call last):
...
ValueError: Computation failed since Maxima requested additional constraints (try the command 'assume(i>0)' before integral or limit evaluation, for example):
Is %i an integer?
```


This also was verified on a local installation.


---

Comment by kcrisman created at 2009-10-23 23:54:52

Just FYI, this is now FIXED in the latest CVS of Maxima.  

```
Maxima 5.19post http://maxima.sourceforge.netusing Lisp SBCL 1.0.24
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
(%i1) integrate(exp(-x^%i),x,0,1);
                       %i gamma_incomplete(- %i, - log(x + 1))
(%o1) %i (%i (limit   (---------------------------------------
              x -> 0-                     2
   %i gamma_incomplete(%i, - log(x + 1))    %i gamma_incomplete(%i, 1)
 - -------------------------------------) + --------------------------
                     2                                  2
   %i gamma_incomplete(- %i, 1)
 - ----------------------------)
                2
              gamma_incomplete(%i, - log(x + 1))
 + limit   (- ----------------------------------
   x -> 0-                    2
   gamma_incomplete(- %i, - log(x + 1))    gamma_incomplete(%i, 1)
 - ------------------------------------) + -----------------------
                    2                                 2
   gamma_incomplete(- %i, 1)
 + -------------------------)
               2
(%i2) 
```

Of course, now we'll have to deal with nounforms and gamma_incomplete translation, but hopefully that won't be too big of a hurdle.


---

Comment by kcrisman created at 2009-12-22 17:26:02

Using Maxima 5.20.1 with Sage 4.3.alpha1:

```
sage: exp(-x*i).integral(x,0,1)
I*e^(-I) - I
```

So if that is mathematically correct, sounds like it's fixed.  The following link [http://www.wolframalpha.com/input/?i=integrate+e%5E%28-x*I%29+from+0+to+1](http://www.wolframalpha.com/input/?i=integrate+e%5E%28-x*I%29+from+0+to+1) indicates it is, as well as just using the FTC.  Now we just need the spkg and to put a doctest here.

See #7748 for getting a symbolic incomplete gamma, which we would also need regardless of that.


---

Comment by kcrisman created at 2009-12-22 21:21:53

This patch depends on the spkg at #7745, but should still apply (with fuzz) if one doesn't apply the patch there.


---

Comment by kcrisman created at 2009-12-22 21:21:53

Changing status from new to needs_review.


---

Comment by kcrisman created at 2009-12-22 21:22:11

Based on 4.3.alpha1


---

Attachment

Positive review! Tested on 4.3.rc0 and got only errors which have been reported on sage-devel and are not relevent to this ticket. Tested together with #7745 and #4142.

Positive review, thanks for upgrading.


---

Comment by robert.marik created at 2009-12-23 08:38:28

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-01-04 03:09:23

Resolution: fixed
