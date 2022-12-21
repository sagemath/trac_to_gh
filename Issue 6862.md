# Issue 6862: Mixing of different domains for symbolic variables

Issue created by migration from Trac.

Original creator: gmhossain

Original creation time: 2009-09-02 11:35:47

From suge-support

On Sep 1, 11:35 pm, Mani chandra <mchan...`@`iitk.ac.in> wrote:

> Mani chandra wrote:

```
sage: x = a + I*b
sage: real(x.conjugate().simplify())
real_part(a) + imag_part(b)
sage: real(x.conjugate())
real_part(a) - imag_part(b)
```


This seems to be happening because maxima(via simplify)
treats variables as real whereas pynac treats as 
complex.



```
sage: x.conjugate()
conjugate(a) - I*conjugate(b)

sage: x.conjugate().simplify()
a - I*b
```




---

Comment by kcrisman created at 2009-09-04 18:04:17

See [http://groups.google.com/group/sage-devel/browse_thread/thread/e25e03c9dba88a93](http://groups.google.com/group/sage-devel/browse_thread/thread/e25e03c9dba88a93)

Also, based on the hint there from Robert Dodier, here is the eventual way a fix will have to occur, perhaps as outlined in the thread:

```
sage: assume(a,'complex')
sage: x.conjugate().simplify()
-I*b + conjugate(a)
```



---

Comment by kcrisman created at 2013-02-24 02:19:43

See also this closely related [ask.sagemath.org question](http://ask.sagemath.org/question/2287/bug-with-absolute-value-of-a-complex-variable), where the following example occurs.


```
sage: var('a')
a
sage: b=a*a.conjugate()-a*a
sage: b
-a^2 + a*conjugate(a)
sage: simplify(b)
0
```


I think this is a little weird, though, since in Maxima

```
(%i1) domain:complex;
(%o1)                               complex
(%i2) -a^2+a*conjugate(a);
(%o2)                                  0
```

and sadly, the Maxima manual says that all this is expected to do is

```
Option variable: domain
Default value: real

When domain is set to complex, sqrt (x^2) will remain sqrt (x^2) instead of returning abs(x).
```


William says in the thread above that

```
What we need is to queue up (put in some list somewhere) all
declaration that could ever be needed, then whenever we do a Sage -->
calculus Maxima conversion, we would empty the queue if it is
nonempty.  Also, if Maxima were to crash/get restarted (does that ever
happen anymore), we would need to  make sure all var's get set again.
This seems very do-able.
```

and perhaps that could be part of the initialization process of any variable - without actually calling Maxima at that time, of course!


---

Comment by kcrisman created at 2013-06-13 16:13:56

#14628 is somewhat related, though this would not fix it, as far as I can tell.


---

Comment by kcrisman created at 2013-06-13 16:15:38

Let's make sure to also test #11656, which was a dup, when (?!) we fix this:

```
var('c', domain='complex')
var('x', domain='real')
C = c * exp(-x^2)
print (C)
    c*e^(-x^2)

print (C.imag())
    e^(-x^2)*imag_part(c)

print (C.imag().simplify_full()) 
    0
```



---

Comment by zimmerma created at 2013-08-29 07:49:40

see also #14305

Paul


---

Comment by kcrisman created at 2020-10-08 12:47:07

Changing priority from critical to major.


---

Comment by kcrisman created at 2020-10-08 12:47:07

See https://groups.google.com/forum/#!topic/sage-devel/U1dsVFP-2PA


---

Comment by charpent created at 2021-03-13 13:44:28

The result reported in the description is correct :


```
sage: var("a, b")
(a, b)
sage: c=a+I*b
sage: c.real()
-imag_part(b) + real_part(a)
sage: c.conjugate()
conjugate(a) - I*conjugate(b)
sage: c.conjugate().real()
-imag_part(b) + real_part(a)
```


//unless `a` and `b` are **known** to be real}}}//. If so :

```
sage: assume(a, b, "real")
sage: c.real()
a
sage: c.conjugate()
a - I*b
sage: c.conjugate().real()
a
```


which is also correct.

==> marking as invalid and requesting review in order to get this bug closed...


---

Comment by charpent created at 2021-03-13 13:44:28

Changing status from new to needs_review.


---

Comment by kcrisman created at 2021-03-13 22:04:56

The problem is Maxima, not Sage. (Or rather, the fact that we don't have a good way to make sure that Maxima variables are complex by default, or didn't at the time.)

```
sage: real(x.conjugate().simplify())
real_part(a) + imag_part(b)
```



---

Comment by kcrisman created at 2021-03-13 22:04:56

Changing priority from major to minor.


---

Comment by kcrisman created at 2021-03-13 22:04:56

Changing status from needs_review to needs_work.


---

Comment by charpent created at 2021-03-13 22:38:18

Replying to [comment:8 kcrisman]:
> The problem is Maxima, not Sage. (Or rather, the fact that we don't have a good way to make sure that Maxima variables are complex by default, or didn't at the time.)
> {{{
> sage: real(x.conjugate().simplify())
> real_part(a) + imag_part(b)
> }}}

Unless `a` and `b` are known to be real, this is the correct result. When this assumption is verifiable, Sage also gives the expected result (see comment 7)...

BTW, at least the "Computational mathematics with SageMath" book states that SR variables behave, by default, as complex variables, but, IIRC, no formal assertion is made in the documentation about this. AFAICT, we use a"domain:complex" assertion in our uses of Maxima.

So what should be the behavior you expect ? OIn fact, I'm having troubleperceivng the point of this ticket...

==> re-asking review ; possibly after discussion on `sage-devel` if we can't agree...


---

Comment by charpent created at 2021-03-13 22:38:18

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2021-03-14 02:44:24

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2021-03-14 02:44:24

> > {{{
> > sage: real(x.conjugate().simplify())
> > real_part(a) + imag_part(b)
> > }}}

I thought you said this one was correct:

```
sage: c.conjugate().real()
-imag_part(b) + real_part(a)
```

So you can see that the Maxima (`.simplify()`) and Sage result are different, unless I'm even more confused.  

> BTW, at least the "Computational mathematics with SageMath" book states that SR variables behave, by default, as complex variables, but, IIRC, no formal assertion is made in the documentation about this. AFAICT, we use a"domain:complex" assertion in our uses of Maxima.

The problem is that `domain:complex` doesn't make the Maxima variables complex, it just doesn't simplify square roots (see the linked sage-devel thread in comment:1).    We do use complex variables for `SR` but those live in Pynac.  However, since `.simplify()` is a Sage method (it just sends to Maxima and back), we don't want that giving wrong behavior.

Anyway, perhaps we need a third party to adjudicate; I did try to suss out the right behavior after your comment:7 but I have been known to make sign errors in my life :-)  But I hope I clarified the exact status in this comment.

```
var("a, b")
c=a+I*b
print(c.conjugate().real())
print((c.conjugate().simplify()).real())
```

[gives](https://sagecell.sagemath.org/?z=eJwrSyzSUErUUUhS0uTlSrZN1PbUSuLlUk7WK0pNzNHQBDOT8_OyStMTS1JB_IKizLwSDRRBqFq4JJpscWZuQU5mWiVQBUwlAOCYI5M=&lang=sage&interacts=eJyLjgUAARUAuQ==)

```
-imag_part(b) + real_part(a)
imag_part(b) + real_part(a)
```

and I don't think those can both be correct.


---

Comment by nbruin created at 2021-03-14 20:39:53

Replying to [comment:10 kcrisman]:
> Anyway, perhaps we need a third party to adjudicate; I did try to suss out the right behavior after your comment:7 but I have been known to make sign errors in my life :-)  But I hope I clarified the exact status in this comment.
> {{{
> var("a, b")
> c=a+I*b
> print(c.conjugate().real())
> print((c.conjugate().simplify()).real())
> }}}
> [gives](https://sagecell.sagemath.org/?z=eJwrSyzSUErUUUhS0uTlSrZN1PbUSuLlUk7WK0pNzNHQBDOT8_OyStMTS1JB_IKizLwSDRRBqFq4JJpscWZuQU5mWiVQBUwlAOCYI5M=&lang=sage&interacts=eJyLjgUAARUAuQ==)
> {{{
> -imag_part(b) + real_part(a)
> imag_part(b) + real_part(a)
> }}}
> and I don't think those can both be correct.

Indeed; I'd say that the problem diagnosed in the ticket is spot on. I also don't know what the best solution is. Note that the two results are both correct if `imag_part(b)==0`, which is what maxima assumes (and we inherit those assumptions by the implementation of `simplify`).

A minimal solution would be to document (in simplify and/or in real_part, imag_part, and conjugate) that for `simplify`, symbolic variables are assumed to be real, so that `conjugate(x).simplify()==real_part(x).simplify()==x` and `imag_part(x).simplify()==0`.


---

Comment by charpent created at 2021-03-14 22:02:34

Replying to [comment:11 nbruin]:

[ Snip... ]

> Indeed; I'd say that the problem diagnosed in the ticket is spot on. 

Indeed...

> I also don't know what the best solution is. Note that the two results are both correct if `imag_part(b)==0`, which is what maxima assumes (and we inherit those assumptions by the implementation of `simplify`).
> 
> A minimal solution would be to document (in simplify and/or in real_part, imag_part, and conjugate) that for `simplify`, symbolic variables are assumed to be real, so that `conjugate(x).simplify()==real_part(x).simplify()==x` and `imag_part(x).simplify()==0`.

At the (accepted) risk of lampooning the British Commons : No, no, no, no, no, no, no, no. 


And no...

This assumption is a way too large limitation of Sage's algebraic abilities. And can't be enforced by checks...

Finding the source of the problem is necessary. It might help to show that the problem is alleviated by //renaming// the variables :


```
sage: %cpaste
Pasting code; enter '--' alone on the line to stop or use Ctrl-D.
:var('a,b')
:c=a+I*b
:L=c.operands()
:aL=[maxima.gensym().sage() for u in L]
:D=dict(zip(L,aL))
:DI=dict(zip(aL,L))
:print(c.conjugate().real())
:print(c.conjugate().simplify().real())
:print(c.subs(D).conjugate().real().subs(DI))
:print(c.subs(D).conjugate().simplify().real().subs(DI))
:--
(a, b)
-imag_part(b) + real_part(a)
imag_part(b) + real_part(a)
-imag_part(b) + real_part(a)
-imag_part(b) + real_part(a)
```


However :

```
sage: print(c.conjugate().subs(D).simplify().real().subs(DI))
imag_part(b) + real_part(a)
```



This behaviour let us think that somehow, `simplify` doesn't account for the "complexity"of `(-I*b")`. Another hint in this direction :


```
sage: with assuming(a,b,"real"):c.conjugate().simplify().real()
a
sage: with assuming(a,b,"complex"):c.conjugate().simplify().real()
-imag_part(b) + real_part(a)
```

which is correct.


This suggests a direction for debugging the  source (which is probably in `pynac` territory, i. e. put of my reach...) and a possible workaround : bracket calls to Maxima's `simplify` with an explicit assumption of complexity for all variables not declared otherwise... This is problematic, however, since `simplify` just converts its argument to Maxima and back. Following the relevant code isn't exactly easy...

However, the real problem is probably not in Maxima itself :

```
(%i1) display2d:false;

(%o1) false
(%i2) domain:complex;

(%o2) complex
(%i3) c:a+%i*b;

(%o3) %i*b+a
(%i4) realpart(conjugate(c));

(%o4) a
(%i5) realpart(ratsimp(conjugate(c)));

(%o5) a
```


Notwithstanding the `domain` setting, Maxima acts as if `a` and `b` were real.


```
(%i6) declare(a, complex, b, complex);

(%o6) done
(%i7) realpart(conjugate(c));

(%o7) 'realpart(a)-'imagpart(b)
(%i8) realpart(ratsimp(conjugate(c)));

(%o8) 'realpart(a)-'imagpart(b)
```


Maxima's `ratsimp` does not create the same problem as Sage`s `simplify`.

HTH,


---

Comment by nbruin created at 2021-03-14 22:38:52

Replying to [comment:12 charpent]:
> This behaviour let us think that somehow, `simplify` doesn't account for the "complexity"of `(-I*b")`. Another hint in this direction :
> 
> {{{
> sage: with assuming(a,b,"real"):c.conjugate().simplify().real()
> a
> sage: with assuming(a,b,"complex"):c.conjugate().simplify().real()
> -imag_part(b) + real_part(a)
> }}}
> which is correct.

Nice find! That is consistent with "maxima by default assumes variables are real-valued as far as conjugate, real_part, imag_part as concerned", so there's a mismatch between sage/pynac and maxima what the default assumptions about variables is, and indeed the appropriate work-around is to sync up those assumptions to match (one way or the other).

I'm not so sure if we should bracket each simplify call with an `assume`. I think it's the responsibility of the interface to translate `x` into a symbol in the other system with the right properties. So I think that `maxima_calculus(x)` should basically already insert the assumption on the maxima side, unless `x` is assumed to be `real`: mismatching defaults on the maxima side just mean we cannot rely on the default behaviour there and we need to enforce the desired behaviour appropriately.

I'd also be fine with changing the assumption that variables are by default real unless declared otherwise. If we want to change our default assumption about variables, we may need to change pynac. Otherwise, I think it's a matter of changing the maxima interface (mainly the maxima_calculus one).


---

Comment by kcrisman created at 2021-03-15 01:57:00

> Nice find! That is consistent with "maxima by default assumes variables are real-valued as far as conjugate, real_part, imag_part as concerned", 
Correct.  As I mention above, `domain:complex` is useful but doesn't affect much beyond `sqrt`.  And I doubt Maxima will be changing that.

> I'm not so sure if we should bracket each simplify call with an `assume`. I think it's the responsibility of the interface to translate `x` into a symbol in the other system with the right properties. So I think that `maxima_calculus(x)` should basically already insert the assumption on the maxima side, unless `x` is assumed to be `real`: mismatching defaults on the maxima side just mean we cannot rely on the default behaviour there and we need to enforce the desired behaviour appropriately.

Yes, we should be sending the correct thing to Maxima.  The problem is that it might be hard to parse out every symbol and make sure it has all the right extra assumptions, or at least in the past that seems to have led into a rat's nest.  We do prepend `sage_var` or something like that to each Sage variable in Maxima, so at least in theory it should be possible, but one wouldn't want to overwrite previous assumptions, so a lot of testing would be involved.  It would be really nice, of course!

> 
> I'd also be fine with changing the assumption that variables are by default real unless declared otherwise. If we want to change our default assumption about variables, we may need to change pynac. 

I think that changing all variables to real by default probably would be a bad move in many ways.  (I don't think you're suggesting that, but the way you phrased it sounds like that.)


---

Comment by charpent created at 2021-03-15 10:18:01

The `Maxima` problem has been [reported](https://sourceforge.net/p/maxima/bugs/3747/) upstream.


---

Comment by charpent created at 2021-03-15 10:20:11

Changing priority from minor to critical.


---

Comment by charpent created at 2021-03-15 10:20:11

Priority set to `critical` because this bug silenty leads to mathematically incorrect results.


---

Comment by nbruin created at 2021-03-15 17:31:55

Replying to [comment:14 kcrisman]:

> Yes, we should be sending the correct thing to Maxima.  The problem is that it might be hard to parse out every symbol and make sure it has all the right extra assumptions, or at least in the past that seems to have led into a rat's nest.  We do prepend `sage_var` or something like that to each Sage variable in Maxima, so at least in theory it should be possible, but one wouldn't want to overwrite previous assumptions, so a lot of testing would be involved.  It would be really nice, of course!

That should actually be dead-easy. This is not about sending strings over that need to be parsed for variables; this is about sending expressions over. They are already parsed. Especially if you do that in the way that maxima_lib works, the symbol needs to be created on the maxima side. If we assume our variables to be complex by default, then that assumption should be inserted at that time. If assumptions change, we just need to do whatever dance we do already to change them on the maxima side as well.

The main problem I expect is that inserting the assumption will probably lead to other side-effects we didn't anticipate. That's why I figured documenting the current "simplify" behaviour is the easier way out (but I wouldn't trust non-trivial SR computations for publication-quality work anyway).


---

Comment by kcrisman created at 2021-03-15 17:35:25

> That should actually be dead-easy. This is not about sending strings over that need to be parsed for variables; this is about sending expressions over. They are already parsed. Especially if you do that in the way that maxima_lib works, the symbol needs to be created on the maxima side. If we assume our variables to be complex by default, then that assumption should be inserted at that time. If assumptions change, we just need to do whatever dance we do already to change them on the maxima side as well.
> 

Good.  And I certainly only care about the `maxima_lib` case.

> The main problem I expect is that inserting the assumption will probably lead to other side-effects we didn't anticipate. That's why I figured documenting the current "simplify" behaviour is the easier way out (but I wouldn't trust non-trivial SR computations for publication-quality work anyway).

True.  

> The Maxima problem has been ​reported upstream.

I expect they will say this is user error or won't implement, since the documentation makes it pretty clear that `domain:complex` doesn't do much, and presumably (though by implication only) shouldn't be expected to do much else.


---

Comment by charpent created at 2021-03-21 08:56:07

According to [Stavros Macrakis](https://sourceforge.net/p/maxima/bugs/3747/#fe49),`domain` is supposed to have an effect only for power operations (and is not expected to have an effect on `realpart`). He reclassified the issue as a documentation issue (wrongly, IMHO, but nothing can be done...).

We should therefore fox it at Sage's level...


---

Comment by @DaveWitteMorris created at 2021-03-28 22:42:46

Related ticket: #30793.


---

Comment by mkoeppe created at 2021-05-10 17:42:09

Moving to 9.4, as 9.3 has been released.
