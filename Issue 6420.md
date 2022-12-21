# Issue 6420: Maxima integration error with 1/x^3

Issue created by migration from Trac.

Original creator: mora

Original creation time: 2009-06-26 07:33:08

Assignee: mhansen

Keywords: maxima integral


```
sage: integrate(1/x^3,x,1,infinity)
ValueError: Integral is divergent.
```


But it's NOT!

The problem comes from Maxima. I could check four versions:


```
Maxima 5.13.0: it's ok
Maxima 5.16.3: it gives wrong result, Sage 4.0.2 uses this
Maxima 5.17.1: it gives wrong result
Maxima 5.18.1: it's ok
```


An example for wrong result:

```
petya`@`desktop:~/download/sage/sage-4.0.2-linux-Ubuntu_9.04-i686-Linux/local/bin$ ./maxima
Maxima 5.16.3 http://maxima.sourceforge.net
Using Lisp ECL 9.4.1
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
The function bug_report() provides bug reporting information.
(%i1) integrate(1/x^3,x,1,inf);

Integral is divergent
 -- an error.  To debug this try debugmode(true);
```


We would like to teach undergradute students with Sage, and this bug is quite annoying. It would be helpful, if someone could update Maxima in Sage.


 Thanks,
  Peter


---

Comment by AlexGhitza created at 2009-08-24 09:31:46

Changing assignee from mhansen to AlexGhitza.


---

Comment by AlexGhitza created at 2009-08-24 09:31:46

This is fixed by the spkg and patch at #6699.  I will put up a patch with a doctest here when #6699 gets merged.


---

Comment by john_perry created at 2009-09-10 01:27:35

A temporary workaround is to use sympy:

```
sage: integrate(1/x**3,x,1,infinity,algorithm="sympy")
1/2
sage: integrate(1/x**10,x,1,infinity,algorithm="sympy")
1/9
```



---

Comment by kcrisman created at 2009-09-29 14:50:27

Patch is now up.


---

Attachment

I updated the patch to remove some excess blank lines and to remove the ".. note::" which didn't make sense.  Otherwise, your change is good by me.

kcrisman, could you okay these changes and mark it as a positive review?


---

Comment by kcrisman created at 2009-10-05 12:58:05

Yup, those are fine.  I should have noticed that, actually, but was just fixing on the item in the ticket.  Strange that the comment was even still in there.

Incidentally, I'm going to post on sage-devel about when to use ::, because just recently I remember a thread where it sounded like some doctests didn't happen if you didn't use it on a separate line (I encountered one recently in an __init__ method), so it would be good to have that on record and easily searchable.


---

Comment by mhansen created at 2009-10-15 07:07:14

Resolution: fixed
