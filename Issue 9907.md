# Issue 9907: maxima sum returns hypergeometric function

Issue created by migration from Trac.

Original creator: schilly

Original creation time: 2010-09-14 10:31:28

Assignee: burcin

CC:  eviatarbach

The parsing of Maxima's output is not good enough to handle this:


```
var('n')
sum(((2*I)^n/(n^3+1)*(1/4)^n), n, 0, infinity)
```

gives an exception

```
TypeError: unable to make sense of Maxima expression 'f[4,3]([1,1,-(sqrt(3)*I+1)/2,(sqrt(3)*I-1)/2],[2,-(sqrt(3)*I-1)/2,(sqrt(3)*I+1)/2],I/2)' in Sage
```

which is - i think - a f_43 hypergeometric function.


---

Comment by schilly created at 2010-09-18 11:47:21

one additional example by omologos on irc:

```
var('x n')
f=(-1)^n/((2*n+1)*factorial(2n+1))
sum(f,n,0,oo)
```

but i get this error:

```
TypeError: unable to make sense of Maxima expression 'f[1,2]([1/2],[3/2,3/2],-1/4)' in Sage
```



---

Comment by kcrisman created at 2011-02-17 01:51:30

This should be 

```
var('x n')
f=(-1)^n/((2*n+1)*factorial(2*n+1))
sum(f,n,0,oo)
```

If I'm not mistaken, this might be related to #2516, in the sense that we should be parsing hypergeometric functions correctly and that would be part of that ticket.


---

Comment by eviatarbach created at 2013-06-17 21:01:42

This also causes a similar problem in #4102:


```
sage: f = bessel_J(2, x)
sage: f.integrate(x)
Traceback (most recent call last):
...
TypeError: cannot coerce arguments: no canonical coercion from <type 'list'> to Symbolic Ring
```


In that case, Maxima is returning `hypergeometric([3/2],[5/2,3],-x^2/4)`.


---

Comment by kcrisman created at 2013-10-17 01:01:33

See also http://ask.sagemath.org/question/3091 for another example.


---

Comment by chapoton created at 2014-03-06 17:07:35

Changing keywords from "" to "hypergeometric".


---

Comment by kcrisman created at 2014-04-24 01:15:49

And see [this sage-support thread](https://groups.google.com/forum/#!topic/sage-support/IgC78rcdO7c) for possibly another example.


---

Comment by kcrisman created at 2014-07-08 15:21:11

#2516 has all the examples above in it, with the exception of the ones mentioned in the comments.
* One would want to be able to do

```
b=var('b')
integral(1/(x^b+1),x)
```

  without using W|A; apparently `1/(a^b+1)` would yield `2F1(1,1/a,1+1/a,-a^x)`.
* Apparently 

```
sum(x^(3*k)/factorial(2*k),k,0,oo)
```

  would also be doable with hypergeometrics.


---

Comment by rws created at 2014-07-08 15:54:48

Replying to [comment:11 kcrisman]:
> #2516 has all the examples above in it, with the exception of the ones mentioned in the comments.
What I get with #2516 is

```
sage: integral(1/(x^b+1),x)
integrate(1/(x^b + 1), x)
sage: sum(x^(3*k)/factorial(2*k),k,0,oo)
sqrt(pi)*x^(3/4)*sqrt(1/(pi*x^(3/2)))*cosh(x^(3/2))
```



---

Comment by kcrisman created at 2014-07-08 16:09:48

> What I get with #2516 is
> {{{
> sage: integral(1/(x^b+1),x)
> integrate(1/(x^b + 1), x)
> }}}
Not really worth keeping open, as even Maxima does this.
> {{{
> sage: sum(x^(3*k)/factorial(2*k),k,0,oo)
> sqrt(pi)*x<sup>(3/4)*sqrt(1/(pi*x</sup>(3/2)))*cosh(x^(3/2))
> }}}
Interestingly, this works in vanilla Sage as well.  Maybe there weren't any hg functions to begin with there.  I assume it was fixed with #16224 - earlier it gave yet another (wrong) answer.

So I nominate to close this ticket.


---

Comment by kcrisman created at 2014-07-08 16:09:48

Changing status from new to needs_review.


---

Comment by kcrisman created at 2014-07-08 16:13:37

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2014-07-08 16:13:37

> > {{{
> > sage: sum(x^(3*k)/factorial(2*k),k,0,oo)
> > sqrt(pi)*x<sup>(3/4)*sqrt(1/(pi*x</sup>(3/2)))*cosh(x^(3/2))
> > }}}
> Interestingly, this works in vanilla Sage as well.  Maybe there weren't any hg functions to begin with there.  I assume it was fixed with #16224 - earlier it gave yet another (wrong) answer.
Even more interestingly, this is not as simple as just `cosh(x^(3/2))` (which is correct) but I'm not going to repurpose this one for that.


---

Comment by rws created at 2014-07-08 16:15:42

Practically a duplicate of #2516


---

Comment by vbraun created at 2014-07-08 22:53:22

Resolution: duplicate
