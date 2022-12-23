# Issue 3805: sage gets basic arithmetic with sqrt(3) wrong

Issue created by migration from https://trac.sagemath.org/ticket/3805

Original creator: was

Original creation time: 2008-08-11 16:51:43

Assignee: gfurnish


```
sage: t1 = (sqrt(3)-3)*(sqrt(3)+1)/6;
sage: tt1 = -1/sqrt(3);
sage: t2 = sqrt(3)/6;
sage: tt1 == t1
-1/sqrt(3) == (sqrt(3) - 3)*(sqrt(3) + 1)/6
sage: bool(tt1 == t1)
True
sage: float(expand(t1+t2))
-0.43301270189221941
sage: float(expand(tt1+t2))
-0.28867513459481292
```

But it seems that this does not happen in a clean maxima session directly:

```
sage: !maxima
Maxima 5.13.0 http://maxima.sourceforge.net
Using Lisp CLISP 2.46 (2008-07-02)
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
This is a development version of Maxima. The function bug_report()
provides bug reporting information.
(%i1) t1 : (sqrt(3)-3)*(sqrt(3)+1)/6;
                          (sqrt(3) - 3) (sqrt(3) + 1)
(%o1)                     ---------------------------
                                       6
(%i2) tt1 : -1/sqrt(3);
                                        1
(%o2)                              - -------
                                     sqrt(3)
(%i3) t2 : sqrt(3)/6;
                                     - 1/2
                                    3
(%o3)                               ------
                                      2
(%i4) tt1, numer;
(%o4)                         - .5773502691896258
(%i5) t1, numer;
(%o5)                         - .5773502691896258
(%i6) expand(t1+t2), numer;
(%o6)                         - .2886751345948129
(%i7) expand(tt1+t2), numer;
(%o7)                         - .2886751345948129
```


So I'm not sure what is going wrong, but it need not be a bug in Maxima.


---

Comment by jwmerrill created at 2008-08-31 22:35:07

This works for me.


```
sage: t1 = (sqrt(3)-3)*(sqrt(3)+1)/6;
sage: tt1 = -1/sqrt(3);
sage: t2 = sqrt(3)/6;
sage: tt1 == t1
-1/sqrt(3) == (sqrt(3) - 3)*(sqrt(3) + 1)/6

# bool is only trustworthy on symbolic expressions when it returns True, right?
sage: bool(tt1 == t1) 
True

sage: float(expand(t1 + t2))
-0.28867513459481292

sage: float(expand(tt1 + t2))
-0.28867513459481292

```



---

Attachment


---

Comment by jwmerrill created at 2008-08-31 22:56:52

The patch adds a doctest that shows this functionality working.


---

Comment by mabshoff created at 2008-09-01 01:54:30

The is an updated patcj of jwmerrill's patch with the numerical noise accounted for


---

Attachment

I have attached a patch that accounts for some numerical noise on Linux 64 bit. It also passes doctest on 32 bit Intel OSX.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-01 01:56:43

Jason,

if you solve tickets please take over ownership of them. I did reassign this ticket to you.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-01 01:56:43

Changing assignee from gfurnish to jwmerrill.


---

Comment by jwmerrill created at 2008-09-01 02:04:57

Positive review on your updated patch.  Ownership procedure noted.


---

Comment by mabshoff created at 2008-09-01 02:20:06

Resolution: fixed


---

Comment by mabshoff created at 2008-09-01 02:20:06

Merged trac_3805_expand.patch in Sage 3.1.2.alpha4
