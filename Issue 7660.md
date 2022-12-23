# Issue 7660: arithmetic with inequalities confusing

Issue created by migration from https://trac.sagemath.org/ticket/7660

Original creator: burcin

Original creation time: 2009-12-11 13:55:02

Assignee: burcin

CC:  kcrisman

From the following sage-devel thread:

http://groups.google.com/group/sage-devel/t/951d510c814f894f


Arithmetic with inequalities can be confusing, since Sage does nothing to keep the inequality ``correct``. For example:


```
On Thu, 10 Dec 2009 00:37:10 -0800 (PST)
"marik@mendelu.cz" <marik@mendelu.cz> wrote:

> sage: f = x + 3 < y - 2
> sage: f*(-1)
> -x - 3 < -y + 2
```


It seems MMA doesn't apply any automatic simplification in this case:


```
On Thu, 10 Dec 2009 09:54:36 -0800
William Stein <wstein@gmail.com> wrote:

> Mathematica does something weird and formal:
> 
> In[1]:= f := x+3 < y-2;
> In[3]:= f*(-1)
> Out[3]= -(3 + x < -2 + y)
```


Maple acts more intuitively, though the way ``formal products`` are printed leaves something to be desired, IMHO:


```
On Thu, 10 Dec 2009 14:15:53 -0800
William Stein <wstein@gmail.com> wrote:

> Here is what Maple does:
> 
> flat:release_notes wstein$ maple
>     |\^/|     Maple 13 (APPLE UNIVERSAL OSX)
> ._|\|   |/|_. Copyright (c) Maplesoft, a division of Waterloo Maple
> Inc. 2009 \  MAPLE  /  All rights reserved. Maple is a trademark of
>  <____ ____>  Waterloo Maple Inc.
>       |       Type ? for help.
> > f := x < y;  
>                                   f := x < y
> 
> > f*(-3);  
>                                   -3 y < -3 x
> 
> > f*z;  
>                                   *(x < y, z)
> 
> > f*a;  
>                                   *(x < y, a)
```



We should multiply both sides of the inequality only if the argument is a real number (as opposed to a symbol with real domain), and invert the relation when the argument is negative.

Note that GiNaC leaves everything formal, like MMA, by default:


```
ginsh - GiNaC Interactive Shell (ginac V1.5.3)
  __,  _______  Copyright (C) 1999-2009 Johannes Gutenberg University Mainz,
 (__) *       | Germany.  This is free software with ABSOLUTELY NO WARRANTY.
  ._) i N a C | You are welcome to redistribute it under certain conditions.
<-------------' For details type `warranty;'.

Type ?? for a list of help topics.
> f= x < y;
x<y
> f*-1;
-(x<y)
> f*-5;
-5*(x<y)
> f*-z;
-z*(x<y)
> f*z;
z*(x<y)
```



---

Comment by tnv created at 2011-06-16 23:15:49


```
sage: -1*(x < y)
-x < -y

```

this is quite dangerous (I encountered it as a bug in a project).  Hopefully someone will try to fix this soon.  Could it be related to this  http://trac.sagemath.org/sage_trac/ticket/11309 ?


---

Comment by kini created at 2012-06-01 21:00:15

I propose the following: `a*(x<y)` should not be simplified, ever, other than simplifying `a`, `x`, or `y` individually. Are there any problems with this?


---

Comment by kcrisman created at 2012-06-02 01:53:36

Given the ticket description details above and the discussion at #11309 and here, I think that Burcin's original proposal of 
* keeping the same if we know `a` is positive
* reversing if we know `a` is negative (presumably in both of these cases only if `a` is coerced to the reals successfully, as Burcin says)
* (not in original but reasonable) return something like `False` for `<` and `=` for `<=` if `a=0`?
* returning something formal otherwise
seems best.  It does seem reasonable to multiply by `-1`, after all, and tnv is right that this should either reverse the inequality or remain formal.


---

Comment by kini created at 2012-06-02 02:27:15

It doesn't seem at all reasonable to me to distribute multiplication over a relation. When you distribute multiplication over addition, the addition expression `(a+b)` lives in the same space as `a` and `b` individually. This is not the case with `(x<y)` and `x` and `y`. 

There is no mathematical rationale for saying that `(-1)*(x<y)` is `-x < -y` or `-x > -y` or anything other than just `(-1)*(x<y)`. I'm sure many can recall when they first learned basic algebra that their teacher was careful to say "we multiply _both sides of_ the equation by c", not "we multiply the equation by c", just as he or she was careful to say "we multiply both the numerator and denominator of the fraction by c", rather than the dangerous "we multiply the fraction by c"!

If we allow multiplication to distribute over `x<y` as if it were a two-coordinate vector, do we want other similarities with vector arithmetic to come into play? Should `(a+b)*(x<y)` be equal to `a*(x<y) + b*(x<y)`? Now we have addition and presumably subtraction of relational expressions. What is `0*(x<y)`? What is `(x<y) + (z>y)`? Should we attempt to reverse inequalities to make them match up when adding them? Do we then end up with `(x+y<y+z)`, or `(y+z>x+y)`? Or, do we conclude that `(z>y)` is equal to `(-1)*(-z<-y)`, and so `(x<y) + (z>y) == (x<y) - (-z<-y) == (x+z<2y)`? Going beyond vector-like arithmetic, what happens when you add a scalar to a relational expression? What is `(x<y) + 3`?

I think the most sensible answer to all the above questions is the following: we should not perform arithmetic on relational expressions; when asked to do so, we should return a purely formal expression.

If the title of this ticket disagrees with that answer, I can make another ticket to implement it, but I'm just wondering if anyone disagrees with me strongly about this.


---

Comment by kcrisman created at 2012-06-02 02:41:24

Well, we could go to the !Ginac/Mathematica way too, instead of the Maple way.  But now that #11309 is on the way in, probably it's time to deal with this.  FWIW, Maxima seems to go that way as well.

```
(%i1) x<y;
(%o1)                                x < y
(%i2) a:x<y;
(%o2)                                x < y
(%i3) a;
(%o3)                                x < y
(%i4) -1*a;
(%o4)                              - (x < y)
(%i5) b*a;
(%o5)                              b (x < y)
```

Maybe Burcin has a comment; I don't have that strong of feelings, though I'm partial to 
* `(x<y)+3 == x+3<y+3`
* `0*(x<y) is False`
but those may just be sentimental, as you suggest.


---

Comment by kini created at 2012-06-02 02:50:52

Honestly I thought the most likely response would be `0*(x<y) == 0`. `False` is an even stranger result because now you have `(x<y) == (1+0)*(x<y) == (x<y) + False`, so either `False` is now another additive identity (on relations, anyway), thus breaking the universality of `? - ? = 0`, or `False == 0`, which is another can of worms...

And if `(x<y)+3 == (x+3<y+3)`, then presumably `3 == (3<3) == False`...?

None of this makes any sense, IMHO. I think it would be best to go the Mathematica/GiNaC/Maxima way, as shown in your Maxima output, rather than the Maple way.


---

Comment by robert_dodier created at 2013-01-08 02:40:57

For the record, Maxima has a share package which implements arithmetic on inequalities.

```
(%i1) load (ineq);
(%o1) /home/robert/maxima/maxima-git/maxima-code/share/simplification/ineq.mac
(%i2) e:a < b;
(%o2)                                a < b
(%i3) x*e;
Is  x  positive, negative, or zero?
p;
(%o3)                              a x < b x
(%i4) x*e;
Is  x  positive, negative, or zero?
n;
(%o4)                              a x > b x
(%i5) x*e;
Is  x  positive, negative, or zero?
z;
(%o5)                              (a < b) x
```

I gather that's similar to what Maple does.


---

Comment by burcin created at 2013-01-09 11:03:47

prototype patch


---

Attachment

attachment:trac_7660-inequality_arithmetic.patch comments out a few lines in `_add_`, `_mul_`, etc., methods of symbolic expressions to pass the arithmetic on to GiNaC directly. I don't have time to test this and verify that it returns sensible answers, however we decide to define "sensible". Please test, see what doctests fail and try to produce horrific wrong results.

Quite a few doctests and some documentation will have to change to match this new design decision. I'd like to make sure we agree on the behavior before trying to produce a clean patch. Of course, I'd appreciate help with the documentation in any case.


---

Comment by rws created at 2014-02-17 15:06:42

OK that patch applies cleanly with `patch -l`. It results in


```
sage: var('x')
x
sage: x>1
x > 1
sage: ie=_
sage: ie*-1
-(x > 1)
sage: solve(_,x)
...
RuntimeError: ECL says: THROW: The catch MACSYMA-QUIT is undefined.
```

I refrained from starting any doctests.


---

Comment by rws created at 2014-02-17 15:10:11

Changing keywords from "" to "inequality, solver, maxima".


---

Comment by rws created at 2014-02-17 15:10:11

New commits:


---

Comment by rws created at 2014-03-06 16:42:23

Here are the statements sent via `maxima_eval("#$%s$"%statement)`:

Before:

```
sage: solve(-(x > 1),x)
sage0 : (x)*(-1) > -1
sage1 : solve_rat_ineq(sage0)
_tmp_ : sage1
kill(sage1)
kill(sage0)
[[x < 1]]
```

After:

```
sage: solve(-(x > 1),x)
sage12 : (x > 1)*(-1) = 0
sage13 : x
sage14 : solve(sage12,sage13)
kill(sage13)
kill(sage14)
_tmp_ : [x>1=0]          <---------?
kill(sage12)
```

Apparently, Sage's last statement sent is the result itself (no idea why), and maxima then barfs because it can't digest its own output. In maxima:

```
(%i11) solve((x > 1)*(-1) = 0,x);
(%o11)                            [x > 1 = 0]
(%i12) [x>1=0];
incorrect syntax: Found logical expression where algebraic expression expected
[x>1=
   ^
```

In summary there are three problems:
* 46 doctests fail in symbolic alone
* maxima can't handle the formal expressions generated via this patch, and `solve()` will fail because it uses maxima solve() and not solve_rat_ineq() (probably because the expression looks like an algebraic). However:

```
sage: solve_ineq((x>1)*(-1),[x,y])
#0: solve_rat_ineq(ineq=-(x > 1))
...
TypeError: ECL says: Error executing code in Maxima: solve_rat_ineq:  -(x > 1)  is not an inequality.
```

So maxima refuses to handle the formal expression generated by this patch, and this means they cannot be solved, regardless of method called. So, in addition, `solve()` should be changed to do simplification of these expressions before handing them on. This special simplification avoids all issues raised in comment:10. It can be implemented after this ticket (#15906).
* `calculus.py:symbolic_expression_from_maxima_string()` should catch maxima `RuntimeError`s from `ecl.c` and rethrow them with meaningful information. (#15902)
`


---

Comment by git created at 2014-03-06 16:45:26

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-03-07 16:35:20

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by rws created at 2014-03-07 16:36:39

Changing status from new to needs_review.


---

Comment by git created at 2014-03-12 08:00:24

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-04-02 13:47:54

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by aapitzsch created at 2014-11-02 22:19:05

Changing status from needs_review to needs_work.


---

Comment by aapitzsch created at 2014-11-02 22:19:05

Please use python3 compatible `raise TypeError` syntax.


---

Comment by git created at 2014-11-03 08:36:55

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by rws created at 2014-11-03 08:37:53

Replying to [comment:26 aapitzsch]:
> Please use python3 compatible `raise TypeError` syntax.
Done. Still, doctests fail in `expression.pyx`.


---

Comment by rws created at 2014-12-11 14:44:36

This came up again in http://ask.sagemath.org/question/25217/how-to-do-operations-that-change-a-relation/


---

Comment by jdemeyer created at 2014-12-11 16:46:53

I'm just now looking at this ticket and personally I don't like to lose the ability to compute with relations. I think that the fact that `(a == b)^2` returns `a^2 == b^2` is a feature, not a bug. I'd say it's up to the user to ensure that the operation makes sense.

Would it be possible to keep the old behaviour for equalities `==` at least?


---

Comment by rws created at 2015-02-12 08:07:22

Let's start this fresh. To summarize, what's wanted is the following:

equations:
 * `(a==b) +-*/ c` same as:
   - `(a==b).add_to_both_sides(c)`
   - `(a==b).subtract_from_both_sides(c)`
   - `(a==b).multiply_both_sides(c)`
   - `(a==b).divide_both_sides(c)`
   - `False` if `*/0`
 * `(a==b)^c` --> `a^c == b^c`
 * `f(a==b)` --> `f(a==b)`
relations:
 * `(a<b) +- c` same as:
   - `(a<b).add_to_both_sides(c)`
   - `(a<b).subtract_from_both_sides(c)`
 * `(a<b) */ c` same as:
   - `a*/c > b*/c` for `c` real and negative, or if `c` is assumed negative
   - `a*/c < b*/c` for `c` real and positive, or if `c` is assumed positive
   - `False` if `c=0`
 * `(a<b)^c` --> `(a<b)^c`
 * `f(a<b)`  --> `f(a<b)`

Question: Real or: if coerced to the reals successfully?
A followup extension would be like Maxima's ineq package, i.e., ask before doing a sign switch.


---

Comment by jdemeyer created at 2015-02-12 09:03:41

Replying to [comment:31 rws]:
>  * `f(a==b)` --> `f(a==b)`
What does `f(a==b)` even mean? I would go for `f(a) == f(b)`.

> relations:
>  * `(a<b) */ c` same as:
>    - `a*/c > b*/c` for `c` real and negative, or if `c` is assumed negative
>    - `a*/c < b*/c` for `c` real and positive, or if `c` is assumed positive
>    - `False` if `c=0`

What if neither of the above conditions is true? `raise ArithmeticError` in that case?


---

Comment by rws created at 2015-02-12 09:22:19

Replying to [comment:32 jdemeyer]:
> >  * `(a<b) */ c`
> What if neither of the above conditions is true? `raise ArithmeticError` in that case?
Not if `c` contains variables. Is there even a way of determining this?


---

Comment by jdemeyer created at 2015-02-12 09:26:39

Replying to [comment:33 rws]:
> Not if `c` contains variables.

What would you propose that `x * (y < z)` answers then (where `x`, `y` and `z` are variables)?


---

Comment by rws created at 2015-02-12 09:43:35

Replying to [comment:34 jdemeyer]:
> What would you propose that `x * (y < z)` answers then (where `x`, `y` and `z` are variables)?
Since this ticket will check for assumptions, if there is none we should raise an `ArithmeticError` demanding one.


---

Comment by jdemeyer created at 2015-02-12 09:45:28

So my statement to `raise ArithmeticError` if neither condition is true still remains.


---

Comment by jdemeyer created at 2015-02-12 09:58:19

Replying to [ticket:7660 burcin]:
>    - if `c` contains variables (and no assumptions exist about it) raise `ArithmeticError: missing assumption: is ...>0?`
>    - if `c` contains no variables `ArithmeticError: multiplication of inequality with irreal`

I think it will be easier if these are just one case.


---

Comment by rws created at 2015-02-12 16:10:04

Changing status from needs_work to needs_review.


---

Comment by rws created at 2015-02-12 16:10:04

Since the `f()` stuff requires changes in function base classes, and assumptions are also an involvement, I'll leave both to followup tickets. Please review.
----
New commits:


---

Comment by jdemeyer created at 2015-02-12 16:26:51

Why convert to `RR`? I would simply use

```
if right == 0:
    ...
elif right >= 0:
    ...
elif right <= 0:
    ...
else:
    raise ArithmeticError(...)
```

This handles non-constant symbolic expressions also.


---

Comment by rws created at 2015-02-13 14:19:08

Replying to [comment:42 jdemeyer]:
> Why convert to `RR`? I would simply use
> {{{
> if right == 0:
>     ...
> elif right >= 0:
>     ...
> elif right <= 0:
>     ...
> else:
>     raise ArithmeticError(...)
> }}}
> This handles non-constant symbolic expressions also.
Seems we have to open a ticket?

```
sage: def f(ex):
    if ex==0:
        print 'zero'
    elif ex<0:
        print 'minus'
    else:
        print 'else'
....:         
sage: ex=-I
sage: f(ex)
minus
sage: bool(-I<0)
True
sage: bool(I>0)
True
```



---

Comment by git created at 2015-02-13 14:21:43

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-03-05 14:26:59

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-05-19 05:59:29

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-08-03 06:43:03

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2015-08-20 13:53:57

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by aapitzsch created at 2016-01-10 21:01:55

Changing status from needs_review to needs_work.


---

Comment by rws created at 2016-01-11 07:48:31

`@`aapitzsch Are you willing to review this issue?


---

Comment by aapitzsch created at 2016-01-11 18:50:20

Replying to [comment:53 rws]:
> `@`aapitzsch Are you willing to review this issue?
No. Sorry for the noise.


---

Comment by git created at 2016-10-06 13:54:51

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by rws created at 2016-10-06 13:55:52

Changing status from needs_work to needs_review.


---

Comment by git created at 2016-10-06 14:15:43

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by rws created at 2017-01-14 08:43:15

Relevant doctest fail in `src/sage/misc/sageinspect.py`


---

Comment by rws created at 2017-01-14 08:43:15

Changing status from needs_review to needs_work.


---

Comment by git created at 2017-01-15 07:52:50

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by rws created at 2017-01-15 07:53:31

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2017-02-27 18:14:11

Changing status from needs_review to needs_work.


---

Comment by chapoton created at 2017-02-27 18:14:11

does not apply


---

Comment by git created at 2017-02-28 07:46:22

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by rws created at 2017-02-28 07:46:56

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2017-06-16 07:47:33

Changing status from needs_review to needs_work.


---

Comment by chapoton created at 2017-06-16 07:47:33

does not apply


---

Comment by rws created at 2017-06-16 07:58:51

In the course of this ticket already 12 merge commits were added. The branch has 8 so I'm doing a squash.


---

Comment by rws created at 2017-06-16 08:25:19

New commits:


---

Comment by rws created at 2017-06-16 08:25:19

Changing status from needs_work to needs_review.


---

Comment by chapoton created at 2017-10-04 07:43:23

Changing status from needs_review to needs_work.


---

Comment by chapoton created at 2017-10-04 07:43:23

does not apply


---

Comment by git created at 2017-10-04 08:58:21

Branch pushed to git repo; I updated commit sha1. New commits:
