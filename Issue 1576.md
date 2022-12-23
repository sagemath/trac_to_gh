# Issue 1576: implicit multiplication -- sage needs to have *some* way to do this (even if not by default)

Issue created by migration from https://trac.sagemath.org/ticket/1576

Original creator: was

Original creation time: 2007-12-21 00:18:46

Assignee: was

Here are some examples that should probably work (from somebody named amscopub-travel)

As per an irc conversation last week, here is a list of math
expressions using implicit multiplication. Sorry for the delay:

```
a b c(a^2 + b^2 + c^2)
a b + c^2 == y
(z/(2sin(y z/55))+y+x)^(z/(2sin(y z/55))+y+x)
2(x/2)^2+4(2x)^2
0==-16x^2+48x
(x+2)(x-1)
x^2-4x+4
2(x+3)(x-4)
2x^2-2x-25<=0
-16x^2+132x
2(x+3)(x-4)
x^2-5x+4
3(x-5)(x-5)
(x-1)(x-2)x
(a-b)(a-b)(a-b)

Take any usual python expression and drop the multiplication operator
(or really make it *optional*). So for example, 2*x would be 2x.
However, when ambiguity would result in variable names, use * or a
space. For example, a*b*c would be a b c (to distinguish from the
variable "abc").
```


A first version of this could simply be a function

```
  implicit_mul
```

that takes a string as input, and outputs 




---

Comment by robertwb created at 2008-01-04 08:47:23

Changing status from new to assigned.


---

Comment by robertwb created at 2008-01-04 08:47:23

Changing assignee from was to robertwb.


---

Comment by robertwb created at 2008-01-04 12:51:03

I've implemented implicit_mul, the output for the above expressions are:


```
a*b*c(a^2 + b^2 + c^2)
a*b + c^2 == y
(z/(2*sin(y*z/55))+y+x)^(z/(2*sin(y*z/55))+y+x)
2*(x/2)^2+4*(2*x)^2
0==-16*x^2+48*x
(x+2)(x-1)
x^2-4*x+4
2*(x+3)(x-4)
2*x^2-2*x-25<=0
-16*x^2+132*x
2*(x+3)(x-4)
x^2-5*x+4
3*(x-5)(x-5)
(x-1)(x-2)*x
(a-b)(a-b)(a-b)
```


There is an optional flag, level, which at the highest value produces:


```
a*b*c(a^2 + b^2 + c^2)
(x+2)*(x-1)
...
(x-1)*(x-2)*x
(a-b)*(a-b)*(a-b)
```


Which could be bad, for example `f(x)(y)` would become `f(x)*(y)`. In the first case, I have no idea how to deduce that c shouldn't be called. 

At all but this highest level, I believe it never mangles valid Python. Just to test, I pre-parsed the entire SAGE library through this function and there were no changes. 

Some more examples: 


```
        sage: from sage.misc.preparser import implicit_mul
        sage: implicit_mul('(2x^2-4x+3)a0')
        '(2*x^2-4*x+3)*a0'
        sage: implicit_mul('a b c in L')
        'a*b*c in L'
        sage: implicit_mul('1r + 1e3 + 5exp(2)')
        '1r + 1e3 + 5*exp(2)'
        sage: implicit_mul('f(a)(b)', level=10)
        'f(a)*(b)'
```


This is not yet on by default.


---

Attachment


---

Comment by was created at 2008-01-04 17:01:56

This is frickin awesome!

I think we should just enable this by default via the preparser.  

WOW!

This is very nice to work with.


---

Comment by was created at 2008-01-04 17:12:58


```
william_stein: I just reviewed #1576
[09:02am] william_stein: It makes stuff like this work:
[09:02am] william_stein: sage: 2x^2-2x-25<=0
[09:02am] william_stein: 2*x^2 - 2*x - 25 <= 0
[09:02am] william_stein: sage: sin(2x)
[09:02am] william_stein: sin(2*x)
[09:02am] william_stein: sage: var('a,b,c')
[09:02am] william_stein: (a, b, c)
[09:02am] william_stein: sage: a b c(a^2 + b^2 + c^2)
[09:02am] william_stein: a*b*(c^2 + b^2 + a^2)
[09:02am] william_stein: But doesn't break anything.
[09:02am] william_stein: That last looks funny.
[09:03am] william_stein: It's because we still have implicit calling... 
[09:06am] mabshoff: ok, is there any way you can give me some rights in the wiki to delete users?
[09:06am] mabshoff: Certain spammers are either comming back again and again or a re
[09:06am] mabshoff: registering under the same name over and over again.
[09:06am] mabshoff: mhansen did suggest installing a text based captcha, which should stop all the
[09:06am] mabshoff: machine driven spam.
[09:06am] mabshoff: I see. I don't like that to be enabled by default. What happens for Q[x,xy,y] ?
[09:06am] mabshoff: Then if you write xxyyx - what is that?
[09:06am] mabshoff: Or does that get covered by the patch?
[09:06am] mabshoff: the last one is *wrong*. Or what does c() do?
[09:06am] mabshoff: If c is a var it should be 'a*b*c*(...)'
[09:07am] william_stein: Just apply only the first patch posted and not the second.
[09:07am] william_stein: Then nothing happens by default.
[09:07am] william_stein: There are levels of implicit multiplication, by the way.
[09:07am] william_stein: In the future when c(...) is an error, that example above would raise an error.
[09:07am] mabshoff: Sure. We did discuss implicit multiplication a lot during the CoCoA language
[09:07am] william_stein: The default is not to do anything with the c (...) implicit mulitplication.
[09:07am] william_stein: But it works quite well in all other cases that I tried.
[09:07am] mabshoff: design specification and we came to the conclusion that it is evil.
[09:08am] william_stein: I like what Robert did.
[09:08am] william_stein: Singular has implicit mult also.
[09:08am] mabshoff: Does Maple or Mathematica let you do that?
[09:08am] william_stein: Maple doesn't I think.  Mathematica certainly does and the users love it.
[09:08am] mabshoff: Sure, but it complicates the language parser enourmously.
[09:08am] william_stein: not for sage
[09:08am] mabshoff: What about newlines? Are they ignored, i.e.
[09:08am] mabshoff: a
[09:08am] william_stein: It was a half page of code. done.
[09:08am] mabshoff: b
[09:08am] mabshoff: it that a*b ?
[09:08am] william_stein: Python is way simpler!
[09:09am] william_stein: a and b are completely different statements
[09:09am] mabshoff: I believe you.
[09:09am] william_stein: and if you do "a backslash b" then it gets turned into one line before pre-parsing.
[09:09am] mabshoff: Because if you allow implicit multiplication accross lines all hell breaks loose.
[09:09am] mabshoff: Sure, in that case it is deliberate and the user implies that those are meant to be one line.
[09:10am] william_stein: In Python "across lines" sort of disappears...
[09:10am] mabshoff: I don't mind it being there, I just think that turning it on per default is bad.
[09:10am] william_stein: I disagree.
[09:10am] mabshoff:
[09:10am] william_stein: But for 2.9.2 turning on by default is bad.
[09:10am] william_stein: For 2.10 it may be different.
mabshoff: Well, ther certainly will be bugs to shake out, so I agree totally with merging the first patch
[09:10am] mabshoff: for 2.9.2. and then sort out the rest in 2.10
[09:10am] william_stein: good
```



---

Comment by mabshoff created at 2008-01-04 21:30:47

Resolution: fixed


---

Comment by mabshoff created at 2008-01-04 21:30:47

Merged in 2.9.2.rc1.
