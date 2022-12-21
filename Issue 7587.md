# Issue 7587: improve multi_polynomial_libsingular exponent method

Issue created by migration from Trac.

Original creator: ylchapuy

Original creation time: 2009-12-02 22:11:10

Assignee: AlexGhitza

CC:  simonking

The returned result is a list of ETuples, but for people interested in maximum speed it would be useful to provide an option to return plain tuples.


---

Attachment

based on 4.3.alpha0


---

Comment by ylchapuy created at 2009-12-02 22:19:33

For the record:


```
sage: R = PolynomialRing(QQ,100,'x') 
sage: p = R.random_element(degree=50,terms=50)
sage: timeit('p.exponents()')
625 loops, best of 3: 1.02 ms per loop
sage: timeit('p.exponents(as_ETuples=False)')
625 loops, best of 3: 110 µs per loop
```



---

Comment by ylchapuy created at 2009-12-02 22:19:33

Changing status from new to needs_review.


---

Comment by SimonKing created at 2009-12-03 14:21:16

Changing status from needs_review to positive_review.


---

Comment by SimonKing created at 2009-12-03 14:21:16

Hi Yann!

First good new: The patch cleanly applies to sage-4.3.alpha0.

Second good news: Using regular expressions (as explained [here](http://groups.google.com/group/sage-devel/browse_thread/thread/20e0fc8f5c5be582)) seem to still be faster in my applications:

```
sage: Vars = ['x_'+str(n) for n in range(50)]+['y'+str(n) for n in range(50)]
sage: R = PolynomialRing(QQ,Vars)
sage: RE = re.compile('([a-zA-Z0-9]+)_([0-9]+)\^?([0-9]*)')
sage: p = R.random_element()
sage: p *= R.random_element()
sage: p *= R.random_element()
sage: p *= R.random_element()
sage: p *= R.random_element()
sage: p *= R.random_element()
sage: L = [(Vars[i],e) for i,e in enumerate(p.lm().exponents(as_ETuples=False)[0][:50]) if e]
sage: L
[('x_0', 1),
 ('x_2', 1),
 ('x_4', 1),
 ('x_5', 2),
 ('x_10', 1),
 ('x_42', 1),
 ('x_47', 1)]
sage: RE.findall(str(p.lm()))
[('x', '0', ''),
 ('x', '2', ''),
 ('x', '4', ''),
 ('x', '5', '2'),
 ('x', '10', ''),
 ('x', '42', ''),
 ('x', '47', '')]
sage: timeit('L = RE.findall(str(p.lm()))')
625 loops, best of 3: 25.1 µs per loop
sage: timeit('L = [(Vars[i],e) for i,e in enumerate(p.lm().exponents(as_ETuples=False)[0][:50]) if e] ')
625 loops, best of 3: 11.2 µs per loop
```


I can also confirm that the computation time with the `as_ETuples=False` option is reduced by 90%. So, I can give it a positive review.


---

Comment by ylchapuy created at 2009-12-03 14:37:07

Thanks for the review.

I don't understand why 25.1 µs is better than 11.2 µs though, but I might miss something.


---

Comment by SimonKing created at 2009-12-03 15:03:36

Replying to [comment:3 ylchapuy]:
> Thanks for the review.
> 
> I don't understand why 25.1 µs is better than 11.2 µs though, but I might miss something.

The 25.1 µs is for using regular expressions, the 11.2 µs is for using `exponents()`. 11.2 µs is certainly better than 25.1 µs!

In other words: With your patch, I can finally avoid the use of regular expressions!

Cheers,
Simon


---

Comment by SimonKing created at 2009-12-03 21:43:58

Replying to [comment:3 ylchapuy]:
> I don't understand why 25.1 µs is better than 11.2 µs though, but I might miss something.

After reading what I wrote in comment 2, I see that I must apologize. I started to write the comment when I had just used exponents _without_ the `as_ETuples=False` option --- which was still slower than the regular expression. When I repeated it _with_ the option, it was finally beating the regular expression --- but I forgot to edit the sentence on top of the example.

Sorry for the noise...


---

Comment by mhansen created at 2009-12-04 05:40:25

Resolution: fixed
