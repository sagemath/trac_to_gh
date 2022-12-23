# Issue 807: construction of function fields

Issue created by migration from https://trac.sagemath.org/ticket/807

Original creator: nbruin

Original creation time: 2007-10-03 15:37:31

Assignee: somebody

CC:  klee

The following does not work and it seems to fail in an odd way wrt. the preparser

```
P1.<t> = QQ[].fraction_field()
```

There doesn't seem to be a convenient way of constructing a rational function field
with a named variable.


---

Comment by cremona created at 2008-02-18 12:00:26

This works:


```
sage: P1 = PolynomialRing(QQ,'t').fraction_field()
sage: P1.gen()
t
sage: t=P1.gen()
sage: P1((t+1)/(t-3))
(t + 1)/(t - 3)
```


Note that the fraction field picks up the display name 't', but that to get the identifier t defined requires the assignment.

I guess this does not qualify for what you wanted, namely to have t assigned automatically on the line defining the field.

 Looking into this I found something else peculiar:


```
sage: t=polygen(QQ)
sage: t
x
sage: t.parent()
Univariate Polynomial Ring in x over Rational Field
```


I have found polygen to be useful, but now I think that using it is fraught with possible confusion.  It causes the PolynomialRing in 'x' to be created with no choice as to the display string for the variable.


---

Comment by was created at 2008-02-19 00:04:12

> I have found polygen to be useful, but now I think that using it is fraught 
> with possible confusion. It causes the PolynomialRing? in 'x' to be created 
> with no choice as to the display string for the variable.

That's not true.  Did you try reading `polygen?`


```
sage: t = polygen(QQ,'t')
sage: t
t
sage: t.parent()
Univariate Polynomial Ring in t over Rational Field
```



---

Comment by was created at 2008-05-10 21:45:44


```
14:42 < cwitty-rvw3129> I'd be fine with saying 807 is invalid (since it doesn't have any sort of concrete 
                        proposal); wstein-2605, what do you think?
14:43 < wstein-406> It's invalid.
14:43 < wstein-406> It should be an error.
14:43 < wstein-406> He has to give the poly ring variable explicitly; there is no way around htat.
14:44 < mhansen> This is what it preparses to: "P1 = QQ[].fraction_field(names=('t',)); (t,) = 
                 P1._first_ngens(Integer(1))"
14:44 < wstein-406> However, it might be nice for this to work:
14:44 < cwitty-rvw3129> Well, he's trying to give the variable explicitly with the P1.<t> syntax.
14:44 < wstein-406> P1.<t> = QQ['t'].fraction_field()
14:44 < wstein-406> What would happen is that fraction_field would have a names option, and if the
14:44 < wstein-406> names didn't match with the gen names of R (=QQ['t']) then a copy is returned with
14:44 < wstein-406> those variable names.
14:45 < wstein-406> E.g., 
14:45 < wstein-406> P1.<t> = QQ['x'].fraction_field()
14:45 < wstein-406> should work.
14:45 < wstein-406> Too.
14:45 < wstein-406> So I do not think #807 is invalid; it just needs to be changed slightly.
```



---

Comment by kcrisman created at 2011-12-02 21:08:27

Still all true.  Four years later!

```
sage: P1.<t> = QQ[].fraction_field()
------------------------------------------------------------
   File "<ipython console>", line 1
     P1 = QQ[].fraction_field(names=('t',)); (t,) = P1._first_ngens(1)
             ^
SyntaxError: invalid syntax

sage: P1.<t> = QQ['x'].fraction_field()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

TypeError: fraction_field() got an unexpected keyword argument 'names'
```



---

Comment by cremona created at 2011-12-02 22:43:10

Would it be possible to have QQ('a') preparse to the right thing?  That would make mathematical sense.  Currently, of course, QQ('a') tried to convert the strong 'a' into a rational and fails.


---

Comment by tscrim created at 2013-02-26 15:42:52

I think the underlying problem is that the language syntax does not truly support doing `QQ[]`, so when it is trying to parse `QQ[].fraction_field()`, it first must evaluate `QQ[]` as a standalone (thus the `SyntaxError`), in order to get the output object to find the attribute `fraction_field()`.

I don't know where/how the syntax `P.<x> = QQ[]` comes from/works (in the preparser perhaps?), so perhaps we can use that, but I don't know if that is easily done, safe, or even feasible. I'll do some looking around, but I'm thinking this might not be doable considering the semantics of python... Anyone else's thoughts?

Best,

Travis


---

Comment by cremona created at 2013-02-26 16:59:04

Replying to [comment:6 tscrim]:
> I think the underlying problem is that the language syntax does not truly support doing `QQ[]`, so when it is trying to parse `QQ[].fraction_field()`, it first must evaluate `QQ[]` as a standalone (thus the `SyntaxError`), in order to get the output object to find the attribute `fraction_field()`.
> 
> I don't know where/how the syntax `P.<x> = QQ[]` comes from/works (in the preparser perhaps?), so perhaps we can use that, but I don't know if that is easily done, safe, or even feasible. I'll do some looking around, but I'm thinking this might not be doable considering the semantics of python... Anyone else's thoughts?


```
sage: preparse("P.<x> = QQ[]")
"P = QQ['x']; (x,) = P._first_ngens(1)"
```


As I understand it, the . before the < triggers a python error which is caught and then handled nicely.


> 
> Best,

> Travis


---

Comment by nbruin created at 2013-02-26 18:41:28

Replying to [comment:7 cremona]:
> As I understand it, the . before the < triggers a python error which is caught and then handled nicely.

The preparser is just a preprocessor, so no python errors are involved. The string is modified before the python parser ever sees it. Anyway:

```
sage: preparse("P1.<t> = QQ['x'].fraction_field()")
"P1 = QQ['x'].fraction_field(names=('t',)); (t,) = P1._first_ngens(1)"
```

and supporting it seems straightforward, but this is where things get questionable: `names` supplied on construction are part of the construction data, so

```
sage: R=QQ['x']
sage: F1=R.fraction_field(names=('u',))
sage: F2=R.fraction_field(names=('v',))
```

should produce two fields F1,F2. Both would have coercions from R installed, since they are constructed as field-of-fractions of R. There would not be a coercion from F1 to F2. Furthermore, for

```
sage: K=QQ['x,u,v'].fraction_field()
```

all of R,F1,F2 would coerce into K, but coercion from R to K would not be compatible with the coercions from F1 and F2 into K, which is bad.

For better of for worse, it was decided that the names of polynomial variables have meaning in sage. A consequence of that is that you don't get to choose the name upon applying the function_field functor.

(oh, I didn't realize I made this ticket!)


---

Comment by tscrim created at 2013-02-26 20:05:57

Replying to [comment:8 nbruin]:
> The preparser is just a preprocessor, so no python errors are involved. The string is modified before the python parser ever sees it. Anyway:
> {{{
> sage: preparse("P1.<t> = QQ['x'].fraction_field()")
> "P1 = QQ['x'].fraction_field(names=('t',)); (t,) = P1._first_ngens(1)"
> }}}
> and supporting it seems straightforward,

That's not as scary as I expected it to be.

> but this is where things get questionable: `names` supplied on construction are part of the construction data, so
> {{{
> sage: R=QQ['x']
> sage: F1=R.fraction_field(names=('u',))
> sage: F2=R.fraction_field(names=('v',))
> }}}
> should produce two fields F1,F2. Both would have coercions from R installed, since they are constructed as field-of-fractions of R. There would not be a coercion from F1 to F2. Furthermore, for
> {{{
> sage: K=QQ['x,u,v'].fraction_field()
> }}}
> all of R,F1,F2 would coerce into K, but coercion from R to K would not be compatible with the coercions from F1 and F2 into K, which is bad.

So you're considering adding a `names` argument in a meaningful way to `fraction_field()`? However this does not quite make sense to me and would conflict with the behavior of `FractionField` (which takes `names` as input and just ignores them; although it just redirects the call to the respective `fraction_field()` with no arguments). It seems like the correct fix would be to have the following:

```
sage: preparse("R.<x,y> = QQ[].fraction_field()") 
"R = QQ['x, y'].fraction_field(names=('x', 'y',)); (x, y,) = R._first_ngens(2)"
```

and have `fraction_field()` take `names` as an optional argument and ignore the input.

Just to note, this is the current behavior in Sage when there is no other function:

```
sage: preparse("R.<x,y> = QQ[]")                 
"R = QQ['x, y']; (x, y,) = R._first_ngens(2)"
```


In some ways, I'd almost like the following to throw an error:

```
sage: R.<x> = QQ['t']
sage: x
t
```

since the variable names don't match. But that might just be me...

> For better of for worse, it was decided that the names of polynomial variables have meaning in sage. A consequence of that is that you don't get to choose the name upon applying the function_field functor.


---

Comment by cremona created at 2013-02-26 20:26:21

Replying to [comment:9 tscrim]:

> 
> In some ways, I'd almost like the following to throw an error:
> {{{
> sage: R.<x> = QQ['t']
> sage: x
> t
> }}}
> since the variable names don't match. But that might just be me...

No, not just you.  And you probably also dislike this, as I do:

```
sage: y = polygen(QQ)
sage: y
x
```

This would be avoided by disallowing polygen()'s name parameter being omitted (it defaults to "x").  After all we are not allowed to construct number fields, or non-prime finite fields, without naming a generator, and this is worse since we usually think that we have named a generator...


---

Comment by tscrim created at 2013-02-26 20:37:54

Replying to [comment:10 cremona]:
> No, not just you.  And you probably also dislike this, as I do:
> {{{
> sage: y = polygen(QQ)
> sage: y
> x
> }}}
> This would be avoided by disallowing polygen()'s name parameter being omitted (it defaults to "x").  After all we are not allowed to construct number fields, or non-prime finite fields, without naming a generator, and this is worse since we usually think that we have named a generator...

Yes I do not like that as well. However, even making name a mandatory argument, it still does not prevent things such as:

```
sage: y = polygen(QQ, 'a')
sage: y
a
```

From looking at the function, I'd want to deprecate it if we decide to forbid `R.<x> = QQ['t']` (which could be done in the preparse).


---

Comment by nbruin created at 2013-02-26 20:52:02

Replying to [comment:9 tscrim]:
Ah, I wasn't aware of the `FractionField` behaviour.
In a way, ignoring "names" would be good. Compare:

```
sage: preparse("R.<x>=QQ[t]")
'R = QQ[t]; (x,) = R._first_ngens(1)'
sage: preparse("R.<x>=PolynomialRing(QQ,'t')")
"R = PolynomialRing(QQ,'t', names=('x',)); (x,) = R._first_ngens(1)"
sage: preparse("R.<x>=PolynomialRing(QQ,names='t')")
"R = PolynomialRing(QQ,names='t', names=('x',)); (x,) = R._first_ngens(1)"
```

In the first and second cases, it is recognised that a print name supplied by the LHS is superfluous, so it gets ignored (meaning: not inserted into the RHS). In the third case, the preparser fails to recognize this (the preparser will always have problems like that).

Given that print names are always superfluous for FractionField, ignoring the names field would be the right thing. However, I think `fraction_field` is not the proper place to do this and it would not solve the issue of this ticket: In

```
P1.<t>=FractionField(QQ[])
```

or

```
P1.<t>=QQ[].fraction_field()
```

it's not just that a `names=('t',)` should not be injected into the `fraction_field` call, it should be injected into the polynomial ring constructor. Of course, for this case the solution is

```
sage: P1.<t>=FunctionField(QQ)
```



---

Comment by nbruin created at 2013-02-26 21:03:24

Replying to [comment:11 tscrim]:
> > This would be avoided by disallowing polygen()'s name parameter being omitted (it defaults to "x").  After all we are not allowed to construct number fields, or non-prime finite fields, without naming a generator, and this is worse since we usually think that we have named a generator...

Isn't the whole point of `polygen` that people get tired of supplying names? Otherwise you can just spell it `QQ['a'].0`, which is shorter anyway (or `QQ['a'].gen(0)` if you don't want to rely on the preparser and is still shorter than `polygen(QQ,'a')` and requires the same number of "shift" characters on a US keyboard)
> 
> Yes I do not like that as well. However, even making name a mandatory argument, it still does not prevent things such as:
> {{{
> sage: y = polygen(QQ, 'a')
> sage: y
> a
> }}}
> From looking at the function, I'd want to deprecate it if we decide to forbid `R.<x> = QQ['t']` (which could be done in the preparse).
Deciding _if_ the `names=` implied by `R.<x>` is necessary is already flaky. Deciding if the implied `names=` is consistent with what is on the RHS is going to be very complicated within the limited view of the preparser. I don't think we want to grow a new attribute `preparser_generated_names` just to accommodate this.

We can document what it does:
 - bind generators to the python identifiers supplied
 - if the RHS requires print names for the generators and doesn't supply them, derive them from the python names.

Of course it's good style to let python names and print names bear resemblance, but ultimately users will have to know that they are not the same thing.


---

Comment by tscrim created at 2013-02-27 00:25:40

Ignoring the `names` in `fraction_field()` would not solve the problem since the preparser does not set the variable names correct (which should IMO be fixed nevertheless since it is inconsistent). I'll look more into the preparser later tonight (feel free to upload a patch if you know how to fix the main issue, I can find some places to document the bindings).

Thanks,

Travis


---

Comment by klee created at 2020-07-08 23:42:42

This ticket is about the ancient Sage, which lacked function fields at all. Sage has transformed itself a lot ever since.


---

Comment by mkoeppe created at 2020-07-08 23:48:58

Changing status from new to needs_review.


---

Comment by tscrim created at 2020-07-08 23:51:53

That is not true. It is not about a lack of function fields but about an easy way to construct them with a variable. Right now it is a two-step process:

```
sage: R = QQ['t'].fraction_field()
sage: t = R.gen()
```

This ticket is about combining that into 1 step using our modified syntactic sugar.


---

Comment by tscrim created at 2020-07-08 23:51:53

Changing status from needs_review to needs_work.


---

Comment by tscrim created at 2020-07-08 23:52:28

Also, still an error:

```
sage: P1.<t> = QQ[].fraction_field()
  File "<ipython-input-1-4fe507ca8d97>", line 1
    P1 = QQ[].fraction_field(names=('t',)); (t,) = P1._first_ngens(1)
            ^
SyntaxError: invalid syntax

sage: P1.<t> = FractionField(QQ[])
  File "<ipython-input-2-301ad9082694>", line 1
    P1 = FractionField(QQ[], names=('t',)); (t,) = P1._first_ngens(1)
                          ^
SyntaxError: invalid syntax
```



---

Comment by klee created at 2020-07-09 01:14:09

Replying to [comment:22 tscrim]:
> That is not true. It is not about a lack of function fields but about an easy way to construct them with a variable.

When this ticket was created, I guess this was not available:

```
sage: R.<t> = FunctionField(QQ)
```

which is "a convenient way of constructing a rational function field with a named variable." 

> Right now it is a two-step process:
> {{{
> sage: R = QQ['t'].fraction_field()
> sage: t = R.gen()
> }}}
> This ticket is about combining that into 1 step using our modified syntactic sugar.

Therefore I think there is no need now to do that combining. 

Now this also works (perhaps didn't work at that time):

```
sage: P.<t> = QQ[]
sage: f = t/(1-t)
sage: f
-t/(t - 1)
sage: f.parent()
Fraction Field of Univariate Polynomial Ring in t over Rational Field
```

Then why need to get the generator of the fraction field(=function field)?


---

Comment by tscrim created at 2020-07-09 01:46:58

Replying to [comment:24 klee]:
> Replying to [comment:22 tscrim]:
> > That is not true. It is not about a lack of function fields but about an easy way to construct them with a variable.
> 
> When this ticket was created, I guess this was not available:
> {{{
> sage: R.<t> = FunctionField(QQ)
> }}}
> which is "a convenient way of constructing a rational function field with a named variable." 

The next thing I would want to try would be to get a multivariate fraction field, which doesn't work using that construction. (See also comment:12.)

Although that does give an idea for extending the `FractionField(R)` to not just ignore the `names` parameter, but instead create the polynomial ring over the `R`. This would make it similar to `FunctionField`.

> > Right now it is a two-step process:
> > {{{
> > sage: R = QQ['t'].fraction_field()
> > sage: t = R.gen()
> > }}}
> > This ticket is about combining that into 1 step using our modified syntactic sugar.
> 
> Therefore I think there is no need now to do that combining. 
> 
> Now this also works (perhaps didn't work at that time):
> {{{
> sage: P.<t> = QQ[]
> sage: f = t/(1-t)
> sage: f
> -t/(t - 1)
> sage: f.parent()
> Fraction Field of Univariate Polynomial Ring in t over Rational Field
> }}}
> Then why need to get the generator of the fraction field(=function field)?

Because if it was a polynomial, it would have different methods and not as easy to ducktype. This can be a bit annoying in code when you do something with division sometimes but not every time (say, `t^n for n in [-1,0,1]`). So I do the two steps in my personal code when this shows up. There also is a mild issue of having to do the conversions to the fraction field, which adds a bit of time but usually not significantly more.


---

Comment by klee created at 2020-07-09 05:12:52

Replying to [comment:25 tscrim]:
> Replying to [comment:24 klee]:
> > Replying to [comment:22 tscrim]:
> > > That is not true. It is not about a lack of function fields but about an easy way to construct them with a variable.
> > 
> > When this ticket was created, I guess this was not available:
> > {{{
> > sage: R.<t> = FunctionField(QQ)
> > }}}
> > which is "a convenient way of constructing a rational function field with a named variable." 
> 
> The next thing I would want to try would be to get a multivariate fraction field, which doesn't work using that construction. (See also comment:12.)
> 
> Although that does give an idea for extending the `FractionField(R)` to not just ignore the `names` parameter, but instead create the polynomial ring over the `R`. This would make it similar to `FunctionField`.

`FractionField(R)` is a bad naming. It can be confused with the fraction field of `R`. `FunctionField(R)` might be better, but the name `FunctionField` seems too much associated with function fields with one variable.

On the other hand, trying to make this

```
sage: R = QQ['x,y'].fraction_field()
sage: x,y = R.gens()
```

to a one-step process by some syntatic sugar seems to have no good solution. 

I would suggest to close this ticket and open a new one with an achievable goal.


---

Comment by tscrim created at 2020-07-09 23:46:28

Replying to [comment:26 klee]:
> Replying to [comment:25 tscrim]:
> > Although that does give an idea for extending the `FractionField(R)` to not just ignore the `names` parameter, but instead create the polynomial ring over the `R`. This would make it similar to `FunctionField`.
> 
> `FractionField(R)` is a bad naming. It can be confused with the fraction field of `R`. `FunctionField(R)` might be better, but the name `FunctionField` seems too much associated with function fields with one variable.

That is a good point.

> On the other hand, trying to make this
> {{{
> sage: R = QQ['x,y'].fraction_field()
> sage: x,y = R.gens()
> }}}
> to a one-step process by some syntatic sugar seems to have no good solution. 

Although you can do this:

```
sage: R.<x,y> = FractionField(QQ['x,y'])
```

which is a bit of an abuse with some redundancy. However, it is a one-line thing.

> I would suggest to close this ticket and open a new one with an achievable goal.

I don't think that is a reason to close the ticket (I also disagree with your assessment that it is unachievable). Even still, this ticket could be recycled as the discussion above could prove useful to that effort.


---

Comment by klee created at 2020-07-10 00:42:11

Replying to [comment:27 tscrim]:
 
> Although you can do this:
> {{{
> sage: R.<x,y> = FractionField(QQ['x,y'])
> }}}
> which is a bit of an abuse with some redundancy. However, it is a one-line thing.

Ah. So there is already a convenient method to create function fields of several variables.

> I also disagree with your assessment that it is unachievable.

I am at the point of not understanding what you have in mind.  

> Even still, this ticket could be recycled as the discussion above could prove useful to that effort.

Okay. No problem. Just please make the ticket description reflect the final solution.


---

Comment by mkoeppe created at 2021-02-13 20:51:01

Setting new milestone based on a cursory review of ticket status, priority, and last modification date.


---

Comment by mkoeppe created at 2021-07-19 00:44:56

Setting a new milestone for this ticket based on a cursory review.
