# Issue 6482: multivariate polynomial substitution has a design flaw

Issue created by migration from https://trac.sagemath.org/ticket/6482

Original creator: was

Original creation time: 2009-07-08 13:08:58

Assignee: malb


```
On Wed, Jul 8, 2009 at 1:28 AM, Kwankyu<...> wrote:
>
> Hi,
>
> I was surprised to see
>
> sage: R.<x,y>=QQ[]
> sage: g=x+y
> sage: g.subs({x:x+1,y:x*y})
> x*y + x + y + 1
>
> So the order of substitution matters...unfortunately.
>
> sage: g.subs({x:x+1}).subs({y:x*y})
> x*y + x + 1
> sage: g.subs({y:x*y}).subs({x:x+1})
> x*y + x + y + 1
>
> So the order seems to be from right to left. This seems to me
> unnatural. Anyway this is undocumented. 

Actually, i guess it is documented.  However, I consider it a serious design flaw.
Many thanks for pointing this out!!

I consider this a serious design flaw for the following reasons:

 (1) it is too hard to understand the above behavior, since it depends on the hash values symbolic variables, which might possibly be system-dependent.

 (2) it is totally inconsistent with the behavior for symbolic expressions, where things are done right.

 (3) it is totally inconsistent with the behavior of *homomorphisms*, where things are also done right.

Here is a session to illustrate the above points:

# BAD
sage: R.<x,y>=QQ[]
sage: g=x+y
sage: g.subs({x:x+1,y:x*y})
x*y + x + y + 1

# BAD
sage: R.<x,y>=QQ[]
sage: g=x+y
sage: g.subs(x=x+1,y=x*y)
x*y + x + y + 1

# GOOD
sage: R.<x,y>=QQ[]
sage: phi = R.hom([x+1,x*y])
sage: g=x+y
sage: phi(g)
x*y + x + 1

# GOOD
sage: var('x,y')
sage: g = x+y
sage: g.subs({x:x+1,y:x*y})
x*y + x + 1

# GOOD
sage: var('x,y')
sage: g = x+y
sage: g.subs(x=x+1,y=x*y)
x*y + x + 1
        

> What should be done to this?

1. I suggest that for now you use Hom, as illustrated above, as a workaround.  

2. I think subs should be reimplemented using Hom ASAP.  Note that this could break existing code, so will have to be done carefully.    We can leave the old behavior in for speed, but as a non-default option.

3. Come up with a fast way to implement the new behavior. 

```



---

Comment by malb created at 2009-07-08 13:56:42

the main use-case for which I wrote it is (which **must** be fast):


```
sage: R.<x,y>=QQ[]
sage: g=x+y
sage: %timeit g.subs({x:2,y:1})
10000 loops, best of 3: 62.9 µs per loop
```


The performance for elements in R is:


```
sage: %timeit g.subs({x:x+1,y:x*y})
10000 loops, best of 3: 153 µs per loop
```


However, to my surprise `hom` is faster:


```
sage: R.<x,y>=QQ[]
sage: phi = R.hom([x+1,x*y])
sage: g=x+y
sage: %timeit phi(g)
10000 loops, best of 3: 45.8 µs per loop
```



Is it because it caches or is really just better code?


---

Comment by was created at 2009-07-08 21:43:05

> Is it because it caches or is really just better code? 

Hom is implemented by Singular when the base ring is a singular ring. 

```
sage: R.<x,y>=GF(next_prime(10^9))[]
sage: phi = R.hom([x+1,x*y])
sage: g=x+y
sage: print type(g)
sage: timeit('phi(g)')
<type 'sage.rings.polynomial.multi_polynomial_libsingular.MPolynomial_libsingular'>
625 loops, best of 3: 39.7 µs per loop
sage: R.<x,y>=GF(next_prime(10^10))[]
sage: phi = R.hom([x+1,x*y])
sage: g=x+y
sage: print type(g)
sage: timeit('phi(g)')
<class 'sage.rings.polynomial.multi_polynomial_element.MPolynomial_polydict'>
625 loops, best of 3: 305 µs per loop     
```



---

Comment by malb created at 2009-07-08 22:23:14

So it is `_im_gens_` in `MPolynomial_libsingular` then (sorry for not checking myself earlier). 

It seems the most straight-forward implementation possible including the comment `#TODO: very slow` in `_im_gens_` wins for small examples, but for bigger ones we get:


```
sage: P.<a,b,c,d,e> = PolynomialRing(QQ)
sage: f = P.random_element(degree=3,terms=50)
sage: g = {a:b,b:c,c:d,d:e,e:a}
sage: %timeit f.subs(g)
10000 loops, best of 3: 138 µs per loop
```



```
sage: phi = P.hom([b,c,d,e,a])
sage: %timeit phi(f)
1000 loops, best of 3: 893 µs per loop
```



---

Attachment

*Performance*


```python
sage: P.<a,b,c,d,e> = PolynomialRing(QQ)
sage: f = P.random_element(degree=3,terms=50)
sage: g = {a:b,b:c,c:d,d:e,e:a}
sage: %timeit f.subs(g)
1000 loops, best of 3: 271 µs per loop
```



```python
sage: phi = P.hom([b,c,d,e,a])
sage: %timeit phi(f)
1000 loops, best of 3: 939 µs per loop
```



```python
sage: phi(f)
-a^2*b - 11/2*b^3 - 8*a^2*c + 1/51*b*c^2 + 1/2*c^3 - a^2*d + 1/3*a*b*d - 2/11*a*c*d + 195*b*c*d + 1/3*a*d^2 + 2*b*d^2 - c*d^2 - 2/3*a^2*e + 1/2*a*b*e - 203*b^2*e + 1/4*a*c*e + b*c*e - 5*c^2*e + 6*a*e^2 + b*e^2 - 1/3*c*e^2 - 5*d*e^2 + 3*e^3 + 1/3*a^2 - a*b - 7/48*a*c - 2*b*c - 53/2*c^2 - 1/3*a*d - 1/2*b*d + c*d - d^2 - a*e - 4*b*e - d*e + 13*e^2 - 2*a - 1/2*b - c + 9/2*d - 1/2
sage: f.sub
f.sub_m_mul_q  f.subs         f.substitute
sage: f.subs(g)
-a^2*b - 11/2*b^3 - 8*a^2*c + 1/51*b*c^2 + 1/2*c^3 - a^2*d + 1/3*a*b*d - 2/11*a*c*d + 195*b*c*d + 1/3*a*d^2 + 2*b*d^2 - c*d^2 - 2/3*a^2*e + 1/2*a*b*e - 203*b^2*e + 1/4*a*c*e + b*c*e - 5*c^2*e + 6*a*e^2 + b*e^2 - 1/3*c*e^2 - 5*d*e^2 + 3*e^3 + 1/3*a^2 - a*b - 7/48*a*c - 2*b*c - 53/2*c^2 - 1/3*a*d - 1/2*b*d + c*d - d^2 - a*e - 4*b*e - d*e + 13*e^2 - 2*a - 1/2*b - c + 9/2*d - 1/2
```



---

Comment by jason created at 2009-09-19 02:34:48

Note that since dictionaries do not preserve order, in python, there is no way to distinguish between ` {x:x+1,y:x*y} ` and ` {y:x*y, x:x+1} `.  There are classes out there that implement ordered dictionaries, but if the feature request depends on looping through a standard dictionary in the order that the dictionary was specified, that seems pretty impossible.

Note that this also means that there is no distinction between these calls: ` g(x=3, y=x) ` and ` g(y=x, x=3) `.


---

Comment by jason created at 2009-09-19 02:41:59

To emphasize the point, here is the result after applying the patch:


```
sage: R.<x,y>=QQ[] 
sage: g=x+y 
sage: g.subs({x:x+1,y:x*y}) 
x*y + x + 1
sage: g.subs({y:x*y, x:x+1})
x*y + x + 1
```


Note that things are *not* in order in the second example.

I think this is probably hopeless as stated.  If the substitutions were given as a list of tuples, then you could depend on the order.  In other words, if you had something like `g.subs([(y,x*y), (x,x+1)])` then you could say something about doing the substitutions in order.  Or even if you did something like `g.subs((y,x*y), (x,x+1))` you could do something in order, since *args is a list that preserves the order of the arguments.


---

Comment by malb created at 2009-09-19 10:36:05

It never even occurred to me that one could want to substitute in the order of the dictionary, so this is not what I tried to provide. 'ordered' to me only means 'by variables'. To me, the second example is in order but it might be a good idea to add a note to the docstring to clarify the behaviour.


---

Comment by mhansen created at 2009-10-05 07:50:07

I think that this patch should get a positive review.  The behavior after the patch is the correct behavior and is consistent with the rest of Sage.

I think Jason just misinterpreted what the ticket was for.


---

Comment by mhansen created at 2009-10-15 05:19:01

Resolution: fixed
