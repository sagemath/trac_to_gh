# Issue 3718: calculus -- sage treats limits involving floor and ceil completely wrong

Issue created by migration from https://trac.sagemath.org/ticket/3718

Original creator: was

Original creation time: 2008-07-24 10:26:47

Assignee: gfurnish


```
Hi,

This email is about the fact that Sage (and Maxima and sympy)
all give the wrong answer for a certain limit, at least if one follows
the standard definition given at wikipedia of limit.  The limit in question
is

   lim_{x --> 0 from below}   floor(x)

This problem was reported two weeks ago by John Perry (my old
office might from Northern Arizona Univeristy 14 years ago, by
the way...)

See below for full details.

> That looks to me like a bug caused by an underlying bug in maxima.
> maxima: limit(floor(x),x,0,`minus')
> does not finish,
> while
> maxima: limit(floor(x),x,0)
> 0
> John Cremona

In maxima it would be limit(floor(x),x,0,minus) -- i.e., no quotes, and
that does finish.   However the output directly from maxima
is still 0.   I've cc'd this email to maxima-devel and Robert
Dodier, in case they have a comment.  I've also sent it to
the sympy list since sympy also gives the wrong answer
(see below).


---------------------------------------------------
teragon-2:doc was$ sage -maxima
Maxima 5.13.0 http://maxima.sourceforge.net
Using Lisp CLISP 2.46 (2008-07-02)
Distributed under the GNU Public License. See the file COPYING.
Dedicated to the memory of William Schelter.
This is a development version of Maxima. The function bug_report()
provides bug reporting information.
(%i1) limit(floor(x),x,0,minus);
(%o1)                                  0
(%i4) limit(ceiling(x),x,0,plus);
(%o4)                                  0
-------------------------------------------------

If you read the formal definition of limit, e.g., as given at

     http://en.wikipedia.org/wiki/Limit_of_a_function

you'll see the output of Maxima (and sage) is just plain wrong.


-----

Here's sympy (also wrong):

sage: import sympy
sage: x = sympy.var('x')
sage: f = sympy.floor(x)
sage: f.limit(x, 0, '<')
0
sage: f.limit(x, 0, '>')
0



-----

Maple does exactly the right thing of course, and uses
better names -- left and right -- (imho) than Sage's 
"minus" and "plus":

sage: maple('limit(floor(x),x=0,left)')
-1
sage: maple('limit(floor(x),x=0,right)')
0
sage: maple('limit(floor(x),x=0)')
undefined

```



---

Comment by AlexGhitza created at 2009-08-24 09:20:59

This is fixed by the spkg and patch at #6699.  I will post a patch with a docstring showing this when #6699 gets merged.


---

Comment by AlexGhitza created at 2009-08-24 09:20:59

Changing assignee from gfurnish to AlexGhitza.


---

Comment by kcrisman created at 2009-09-29 14:42:56

Here is the patch.


---

Attachment

Based on 4.1.2.alpha4


---

Comment by timdumol created at 2009-10-01 13:21:09

Tests pass. Seems alright.


---

Comment by mhansen created at 2009-10-15 05:24:20

Resolution: fixed
