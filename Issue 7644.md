# Issue 7644: generic power series reversion

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-12-09 20:20:14

Assignee: AlexGhitza

CC:  fwclarke

Make the following work over any base ring:

```
sage: R.<x> = QQ[[]]
sage: f = 1/(1-x) - 1; f
x + x^2 + x^3 + x^4 + x^5 + x^6 + x^7 + x^8 + x^9 + x^10 + x^11 + x^12
+ x^13 + x^14 + x^15 + x^16 + x^17 + x^18 + x^19 + O(x^20)
sage: g = f.reversion(); g
x - x^2 + x^3 - x^4 + x^5 - x^6 + x^7 - x^8 + x^9 - x^10 + x^11 - x^12
+ x^13 - x^14 + x^15 - x^16 + x^17 - x^18 + x^19 + O(x^20)
sage: f(g)
x + O(x^20)
```


Matt Bainbridge says about power series reversion, which uses pari in some cases, and maybe isn't there in others:

```
Its easy enough to code this in sage.  This seems to work over any
field:


def ps_inverse(f):
   if f.prec() is infinity:
       raise ValueError, "series must have finite precision for
reversion"
   if f.valuation() != 1:
       raise ValueError, "series must have valuation one for
reversion"
   t = parent(f).gen()
   a = 1/f.coefficients()[0]
   g = a*t
   for i in range(2, f.prec()):
       g -=  ps_coefficient((f + O(t^(i+1)))(g),i)*a*t^i
   g += O(t^f.prec())
   return g

def ps_coefficient(f,i):
   if i >= f.prec():
       raise ValueError, "that coefficient is undefined"
   else:
       return f.padded_list(f.prec())[i]
```



---

Comment by fwclarke created at 2009-12-10 10:42:26

Lagrange inversion is significantly faster.  With

```
def ps_inverse_Lagrange(f):
   if f.valuation() != 1:
       raise ValueError, "series must have valuation one for reversion"
   if f.prec() is infinity:
       raise ValueError, "series must have finite precision for reversion"
   t = parent(f).gen()
   h = t/f
   k = 1
   g = 0
   for i in range(1, f.prec()):
       k *= h
       g += (1/i)*ps_coefficient(k, i - 1)*t^i
   g += O(t^f.prec())
   return g
```

I found

```
sage: R.<x> = QQ[[]]
sage: f = exp(x) - 1
sage: timeit('ps_inverse(f)')
5 loops, best of 3: 552 ms per loop
sage: timeit('ps_inverse_Lagrange(f)')
5 loops, best of 3: 74 ms per loop
```



---

Comment by was created at 2009-12-25 18:09:03


```
The code doesn't quite run, since it references some other function
(ps_coefficient); here's an updated version which uses only built-in
functions:

def ps_inverse_Lagrange(f):
  if f.valuation() != 1:
      raise ValueError, "series must have valuation one for
reversion"
  if f.prec() is infinity:
      raise ValueError, "series must have finite precision for
reversion"
  t = parent(f).gen()
  h = t/f
  k = 1
  g = 0
  for i in range(1, f.prec()):
      k *= h
      g += (1/i)*k.padded_list(i)[i - 1]*t^i
  g += O(t^f.prec())
  return g
```



---

Comment by AlexGhitza created at 2010-01-29 11:08:59

What should we do with power series with coefficients in, say, ZZ?  Raise an error, or return a power series over the fraction field?


---

Comment by fwclarke created at 2010-01-30 10:35:26

Replying to [comment:4 AlexGhitza]:
> What should we do with power series with coefficients in, say, ZZ?  Raise an error, or return a power series over the fraction field?

In general, return a power series over the fraction field.  But if the leading coefficient is a unit, then despite the fact that Lagrange inversion involves division, the inverse series has coefficients in the same ring as the original series.  E.g., with the function defined in [comment:3 was],

```
sage: PS.<t> = ZZ[[]]
sage: f = t + t^2 + O(t^10)
sage: ps_inverse_Lagrange(f)
t - t^2 + 2*t^3 - 5*t^4 + 14*t^5 - 42*t^6 + 132*t^7 - 429*t^8 + 1430*t^9 + O(t^10)
```

though

```
sage: ps_inverse_Lagrange(f).parent()
Power Series Ring in t over Rational Field
```

Over a ring of finite characteristic, to use Lagrange inversion, you have to lift to a ring of characteristic zero, invert, and then project down to the original ring.


---

Comment by niles created at 2010-07-08 19:45:18

I've uploaded a patch which implements ps_inverse_Lagrange from above.  For simplicity, I didn't implement over rings of positive characteristic, or in the case that the leading coefficient is not a unit.  Instead, I included examples of changing the base ring and carrying out the reversion there.

Note:  the line

```
g += (1/i)*k....
```

gave me some trouble, since I didn't realize .pyx files use python's integer division; someone who understands the implicit conversions between sage and python might want to check I dealt with that correctly.  It now reads:

```
g += k.padded_list(i)[i - 1]/i*t**i
```

and works fine in all my tests.


---

Comment by niles created at 2010-07-08 19:45:18

Changing status from new to needs_review.


---

Comment by niles created at 2010-08-01 16:22:26

Changing keywords from "" to "lagrange, reversion".


---

Comment by niles created at 2010-08-01 16:22:26

Replying to [comment:2 fwclarke]:

Hi Francis,

You may be interested in reviewing this patch since it's based on your code.  I believe it will be an easy review.

best,
Niles


---

Comment by niles created at 2010-11-30 19:17:50

The latest version of this patch applies cleanly to sage 4.6.1.alpha2 and passes all (-long) doctests.  It also adds `power_series_poly` to the sage documentation, and makes some minor changes so that all documentation builds cleanly.


---

Comment by fwclarke created at 2010-11-30 21:20:52

I've been looking at this.  One concern is that for power series with rational coefficients the existing method using pari is a great deal faster, so that at least in this case the pari method should be retained.  Strangely the existing method fails for integer power series, though pari handles them perfectly ok.

On investigation it turns out that it is the conversion to pari which is failing and that this problem is pointed out in modular/overconvergent/genus0.py, and raised as #4376.  I have produced a short patch (awaiting review) which extends the range of base rings over which pari conversion of a power series is possible.

What I propose then is that a revised patch (depending on the #4376 patch) should try to use pari and that only if this fails should the Lagrange inversion code be used.   

I also think it is sensible to be able to revert infinite precision series, either by specifying the desired precision or by using the parent's default precision.


---

Comment by niles created at 2010-12-01 02:31:45

apply only this patch; tries to use pari first, then falls back to Lagrange inversion


---

Attachment

Replying to [comment:10 fwclarke]:
> I've been looking at this.  

Thanks!

> One concern is that for power series with rational coefficients the existing method using pari is a great deal faster, so that at least in this case the pari method should be retained.  

Yes, especially if there is work in progress to support converting more rings to pari.  I wrote a revised patch which first attempts to convert to pari and do reversion there, and then tries the Lagrange inversion if conversion to pari fails.  I think that implementation means that this patch can be independent of #4376 -- it will simply perform better when that patch is included.


> I also think it is sensible to be able to revert infinite precision series, either by specifying the desired precision or by using the parent's default precision.  

Yes, upon further consideration I agree.  I've made this and two other improvements:

 1. Given a power series with infinite precision and degree `deg`, it's reversion is computed with precision `deg + 1`.
 1. Given a power series whose leading coefficient is not a unit, the code tries to pass to the fraction field of the base ring and compute the reversion there.
 1. Given a power series over a base ring of positive characteristic, the code tries to lift to a characteristic zero base (using `.lift()`), compute the reversion, and then push back down to the positive characteristic base.  This works over finite fields and `Zmod(n)`, but fails over a base ring like `Zmod(n)[x]`.

Each of these is demonstrated with an example.


---

Comment by drkirkby created at 2010-12-01 02:50:07

Is it sensible to remove the first 3 patches - if so, I can do so, as I have admin rights. 

Have all the results been verified by independent means? If so, it would be useful to state how. If not, then I personally don't agree with such "tests", but as a minimum it should be documented if the results have not been verified. 

As for the actual maths, I can't review that - this is well outside my level of maths, since none of my degrees are in maths

Dave


---

Comment by niles created at 2010-12-01 13:23:00

Replying to [comment:12 drkirkby]:
> Is it sensible to remove the first 3 patches - if so, I can do so, as I have admin rights. 

Sure; thanks :)

> 
> Have all the results been verified by independent means? If so, it would be useful to state how. If not, then I personally don't agree with such "tests", but as a minimum it should be documented if the results have not been verified. 

The verifications are performed by checking that `f(g)` and `g(f)` both return `x + O(x^prec)`.  Actually just one of these is necessary to determine the reversion of f, so I view this as two different methods for verifying the answer.

> 
> As for the actual maths, I can't review that - this is well outside my level of maths, since none of my degrees are in maths

Thanks for checking into it :)


---

Comment by fwclarke created at 2010-12-01 21:10:51

Replying to [comment:11 niles]:

> Yes, especially if there is work in progress to support converting more rings to pari.  I wrote a revised patch which first attempts to convert to pari and do reversion there, and then tries the Lagrange inversion if conversion to pari fails.  I think that implementation means that this patch can be independent of #4376 -- it will simply perform better when that patch is included.

A good point (but it would be nice if #4376 could be reviewed; it's very short).

> > I also think it is sensible to be able to revert infinite precision series, either by specifying the desired precision or by using the parent's default precision.
> Yes, upon further consideration I agree.  I've made this and two other improvements:  1. Given a power series with infinite precision and degree `deg`, its reversion is computed with precision `deg + 1`.

I don't see the logic for this.  I would suggest having a keyword `precision` with default `None`, and replacing


```
    if f.prec() is infinity:
        out_prec = f.degree() + 1
        f = f.add_bigoh(out_prec)
    else:
        out_prec = f.prec()
```

with


```
    if f.prec() is infinity and precision is None:
        precision = f.parent().default_prec()
    if precision:
        f = f.add_bigoh(precision)
```

Then one could do (to get some Catalan numbers):


```
sage: R.<x> = QQ[[]]
sage: (x - x^2).reversion()
x + x^2 + 2*x^3 + 5*x^4 + 14*x^5 + 42*x^6 + 132*x^7 + 429*x^8 
+ 1430*x^9 + 4862*x^10 + 16796*x^11 + 58786*x^12 + 208012*x^13 
+ 742900*x^14 + 2674440*x^15 + 9694845*x^16 + 35357670*x^17 
+ 129644790*x^18 + 477638700*x^19 + O(x^20)
```

or


```
sage: (x - x^2).reversion(precision=8)
x + x^2 + 2*x^3 + 5*x^4 + 14*x^5 + 42*x^6 + 132*x^7 + O(x^8)
```

rather than


```
sage: (x - x^2).reversion()
x + x^2 + O(x^3)
```



---

Comment by niles created at 2010-12-02 17:02:52

apply only this patch; choice for default precision improved


---

Attachment

Replying to [comment:14 fwclarke]:
> Replying to [comment:11 niles]:
> 

> A good point (but it would be nice if #4376 could be reviewed; it's very short).

agreed -- I'll add it to my list

> I don't see the logic for this.  I would suggest ...

that's a better idea; it's implemented in the new patch


---

Comment by fwclarke created at 2010-12-02 18:25:52

This is looking good.  Some comments on the docstring:


```
If f has infinite precision, then the precision 
of the reversion defaults to the default precision of 
``f.parent()``. 
```

should say "unless precision is set", or words to that effect.

The remark a few lines later that


```
self must have finite precision (i.e. this cannot be done 
for polynomials).  
```

is no longer appropriate.  Nor is


```
Under the current implementation, the leading 
coefficient must be a unit in the base ring, and the base ring must 
have characteristic zero. 
```

I'm not sure that


```
In positive characteristic, attempt first to lift to characteristic 
zero and perform the reversion there:
```

is in the right place; it's really to do with the algorithm.  Perhaps  better to say here that the function can handle some base rings of non-zero characteristic.


---

Comment by niles created at 2010-12-04 17:21:45

Replying to [comment:16 fwclarke]:
> This is looking good.  Some comments on the docstring:
> 

...

Sorry for not catching these before; fixed now.


---

Comment by fwclarke created at 2010-12-17 09:36:47

Changing status from needs_review to needs_work.


---

Comment by fwclarke created at 2010-12-17 09:36:47

This is fine now, except for one little thing.  In the patch file, the line


```
+        most ``f.prec()).  If f has infinite precision, and the argument
```

should read


```
+        most ``f.prec())``.  If ``f`` has infinite precision, and the argument
```



---

Comment by niles created at 2010-12-17 11:58:45

Thanks for catching that -- fixed now.


---

Comment by niles created at 2010-12-17 11:58:45

Changing status from needs_work to needs_review.


---

Comment by fwclarke created at 2010-12-17 12:11:02

Changing status from needs_review to positive_review.


---

Comment by fwclarke created at 2010-12-17 12:11:02

Now it's perfect. Positive review.


---

Comment by jdemeyer created at 2011-01-13 06:39:38

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2011-01-13 06:39:38

You should change the commit message of the patch (use `hg qrefresh -e` for that).  Make sure you include the ticket number.


---

Comment by niles created at 2011-01-13 12:02:08

apply only this patch


---

Attachment

done.


---

Comment by niles created at 2011-01-13 12:02:45

Changing status from needs_work to needs_review.


---

Comment by fwclarke created at 2011-01-13 13:55:01

Changing status from needs_review to positive_review.


---

Comment by fwclarke created at 2011-01-13 13:55:01

commit message ok now


---

Comment by jdemeyer created at 2011-01-19 01:26:42

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2011-01-19 01:26:42

There are some formatting errors in the docstrings (a `::` should be followed by indented code, there are some places where this is violated).  I can fix these, but later.


---

Comment by niles created at 2011-01-19 12:55:51

My apologies -- I'll upload a fixed version soon.


---

Attachment

apply only this patch


---

Comment by niles created at 2011-01-19 13:27:47

The documentation issue is fixed now -- all documentation builds without warnings.


---

Comment by niles created at 2011-01-19 13:27:47

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2011-01-19 16:43:58

Replying to [comment:27 niles]:
> The documentation issue is fixed now -- all documentation builds without warnings.
Agreed.


---

Comment by jdemeyer created at 2011-01-19 16:43:58

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-01-19 22:19:24

Resolution: fixed
