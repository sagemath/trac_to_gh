# Issue 5453: [with patch, needs review] Create a ring for working with polynomials in countably infinitely many variables

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2009-03-07 19:12:56

Assignee: malb

CC:  simonking




---

Attachment


---

Comment by SimonKing created at 2009-03-07 21:02:36

Dear Mike,

Cool! Thank you that you started an implementation!

Certainly from your patch I learn a lot about how to create a (unique) parent structure. 

I don't quite understand how the method `stretch` works, but I'll try to figure out. However, I think a more useful thing to implement would be the action by permutation of variables. I.e., 

```
sage: X.<x,y> = InfinitePolynomialRing(QQ) 
sage: P = Permutation(((0,1),(2,3,4)))
sage: a = x[3] + y[2] + x[0]*y[1]
sage: a^P
x1*y0 + x4 + y3
```

That's to say, `x[i]` is mapped by `P` to `x[P(i)]`.

However I am not sure whether it is a good idea to implement things on top of usual finitely generated polynomial algebras. After all, they are parent structures and are thus cached -- and my successively fill up memory. 

What happens if you do the following?

```
sage: X.<x> = InfinitePolynomialRing(QQ) 
sage: p = x[0]
sage: while(1):
....:     p = p.stretch(2)
....:     print p
```


Does it soon fill up the whole memory with huge (but finite) polynomial rings? And is much time being spent with creating these rings?

Sorry that I can't test the example myself (will only be possible next week). But perhaps you can tell me what happens.

Cheers,
     Simon


---

Comment by SimonKing created at 2009-03-07 21:06:10

Replying to [comment:1 SimonKing]:
Oops, I had a typo in this example:

> What happens if you do the following?
> {{{
> sage: X.<x> = InfinitePolynomialRing(QQ) 
> sage: p = x[0]
> sage: while(1):
> ....:     p = p.stretch(2)
> ....:     print p
> }}}

It should be `p = x[1]`, to that in the loop `p` becomes `x[2]`, `x[4]`, `x[8]`, ...


---

Comment by mhansen created at 2009-03-07 21:14:32

Changing assignee from malb to mhansen.


---

Comment by mhansen created at 2009-03-07 21:14:32

Replying to [comment:1 SimonKing]:
> Cool! Thank you that you started an implementation!

Actually, it's code that I've had on the combinat patch server for awhile since I have code that makes use of these things.
 
> I don't quite understand how the method `stretch` works, but I'll try to figure out. 

Stretch is actually something that I needed.

> However, I think a more useful thing to implement would be the action by permutation of variables. I.e., 
> {{{
> sage: X.<x,y> = InfinitePolynomialRing(QQ) 
> sage: P = Permutation(((0,1),(2,3,4)))
> sage: a = x[3] + y[2] + x[0]*y[1]
> sage: a^P
> x1*y0 + x4 + y3
> }}}
> That's to say, `x[i]` is mapped by `P` to `x[P(i)]`.

Sure.

> However I am not sure whether it is a good idea to implement things on top of usual finitely generated polynomial algebras. After all, they are parent structures and are thus cached -- and my successively fill up memory. 
> What happens if you do the following?
> ...
> Does it soon fill up the whole memory with huge (but finite) polynomial rings? And is much time being spent with creating these rings?

Yep (that's what you can with infinite loops :-)  For my application, doing the arithmetic will the primary bottleneck.

Like I said, this was a very basic implementation that I wrote because it does what I need and I was able to write it relatively quickly.  I used the existing finite polynomial rings because they already do fast arithmetic that I (personally) have no desire to duplicate.


---

Comment by mhansen created at 2009-03-07 21:14:32

Changing status from new to assigned.


---

Comment by SimonKing created at 2009-03-07 22:01:39

Hi Mike,

Replying to [comment:3 mhansen]:
> Stretch is actually something that I needed.

Of course, this is why one implements things. My aim is to have the Gröbner basis theory of Aschenbrenner and Hillar implemented in Sage, and actually I have potential applications to 3-dimensional topology in the background. 

And for this, the permutation actions are essential. 

But independent from this, I think the implementation should be more sparse.

> Yep (that's what you can with infinite loops :-)  For my application, doing the arithmetic will the primary bottleneck.

For me, arithmetic will certainly be a bottleneck, too. I mean, it is about computing Gröbner bases, and if this is done then there still remains to compute normal forms for really _really_ huge polynomials.

> I used the existing finite polynomial rings because they already do fast arithmetic that I (personally) have no desire to duplicate.

Yep. It is very reasonable to try and avoid duplication! 

But how? Perhaps it would be better if the f.g. polynomial rings were more hidden. For example, the elements of an infinite polynomial ring could be described not simply as a polynomial (say, `x100*x101+x90`) but as a pair formed by a polynomial in a smaller ring and an offset, say `(90,x10*x11+x0)`, or perhaps by an even smaller polynomial and a permutation, say `(((0,90),(1,100),(2,101)), x1*x2+x0)`.

I think a compromise between speed and size makes sense. Or perhaps even concurrent models, similar to dense vs. sparse matrices.

Since I am rather tired, I don't know if all this makes sense, though...


---

Comment by mhansen created at 2009-03-07 22:08:38

Replying to [comment:4 SimonKing]:

> But how? Perhaps it would be better if the f.g. polynomial rings were more hidden. For example, the elements of an infinite polynomial ring could be described not simply as a polynomial (say, `x100*x101+x90`) but as a pair formed by a polynomial in a smaller ring and an offset, say `(90,x10*x11+x0)`, or perhaps by an even smaller polynomial and a permutation, say `(((0,90),(1,100),(2,101)), x1*x2+x0)`.
> 
> I think a compromise between speed and size makes sense. Or perhaps even concurrent models, similar to dense vs. sparse matrices.

Yes, I even mention this in the documentation that the current implementation is definitely tailored to what I needed and that it would be a good project to have different backends.

The primary problem will be doing the arithmetic efficiently.  This is not my area of expertise though.


---

Comment by SimonKing created at 2009-03-08 16:00:50

Sorry, the patch failed to apply. It says

```
unable to find 'doc/en/reference/polynomial_rings.rst' for patching
1 out of 1 hunks FAILED -- saving rejects to file doc/en/reference/polynomial_rings.rst.rej
abort: patch failed to apply
```


What went wrong?


---

Comment by mhansen created at 2009-03-08 18:07:55

Are you running a Sage 3.4 release?  If not, that is the problem because the patch touches the new documentation.


---

Comment by SimonKing created at 2009-03-09 07:37:38

Replying to [comment:7 mhansen]:
> Are you running a Sage 3.4 release?  If not, that is the problem because the patch touches the new documentation.

No, I only have Sage 3.3. Is Sage 3.4 already out? I'll upgrade, or get the 3.4-sources.

Cheers
      Simon


---

Comment by SimonKing created at 2009-03-09 09:05:40

Replying to [comment:8 SimonKing]:
> No, I only have Sage 3.3. Is Sage 3.4 already out? I'll upgrade, or get the 3.4-sources.

I made it differently: I removed the .rst-part from the patch; after removing ReST, the rest worked in Sage 3.3...

Anyway. I think the whole story should be made more sparse. 

I suggest to use the method `change_ring()` of polynomial rings in the background. Then, `stretch()` could be implemented along these lines:

```
sage: R.<x1,y1>=QQ[]
sage: p=R.random_element()
sage: p
-x1^2 - 1/4*y1^2 - 1/2*y1 - 1
sage: S=R.change_ring(names=['x2','y2'])
sage: p=S(p)
sage: p
-x2^2 - 1/4*y2^2 - 1/2*y2 - 1
sage: S=S.change_ring(names=['x4','y4'])
sage: p=S(p)
sage: p
-x4^2 - 1/4*y4^2 - 1/2*y4 - 1
```


In that way, one could keep the underlying ring small.

Problem though: How to add things, if the underlying polynomial rings are different? Probably you know much more about coercion than I do. But I guess it should be possible to automatically find a common parent for the summands as follows:

```
sage: q=R.random_element()
sage: q
1/3*x1^2 + 1/12*x1*y1 - 3/10*y1^2 + x1
sage: Varnames=set([str(X) for X in p.variables()]+[str(X) for X in q.variables()])
sage: T=PolynomialRing(QQ,list(Varnames))
sage: T(p)+T(q)
-3/10*y1^2 + 1/12*y1*x1 + 1/3*x1^2 - 1/4*y4^2 - x4^2 + x1 - 1/2*y4 - 1
```


This could be done behind the scenes.

In the example above, I did not take care about the monomial order, though. This needs to be dealt with in a proper implementation.

Cheers,
    Simon


---

Comment by SimonKing created at 2009-03-09 11:55:04

Replying to [comment:9 SimonKing]:
> I suggest to use the method `change_ring()` of polynomial rings in the background. Then, `stretch()` could be implemented along these lines:
...

It seems that indeed the `while` loop that I gave above is both faster and goes further when using my suggestion:

```
sage: R.<x1,y1>=QQ[]
sage: p=x1
sage: S=R.change_ring(names=['x2','y2'])
sage: n=2
sage: while(1):
....:     p=S(p)
....:     n=2*n
....:     S=S.change_ring(names=['x%d'%(n),'y%d'%(n)])
....:     print p
....:
x2
x4
x8
x16
x32
x64
x128
x256
x512
x1024
x2048
x4096
x8192
x16384
x32768
x65536
x131072
x262144
x524288
x1048576
x2097152
x4194304
x8388608
x16777216
x33554432
x67108864
x134217728
x268435456
x536870912
x1073741824
x2147483648
x4294967296
x8589934592
x17179869184
x34359738368
x68719476736
x137438953472
x274877906944
x549755813888
x1099511627776
x2199023255552
x4398046511104
x8796093022208
x17592186044416
x35184372088832
x70368744177664
x140737488355328
x281474976710656
x562949953421312
x1125899906842624
x2251799813685248
x4503599627370496
x9007199254740992
x18014398509481984
x36028797018963968
x72057594037927936
x144115188075855872
x288230376151711744
x576460752303423488
x1152921504606846976
x2305843009213693952
```


Only at that point was a type error, because the next number is not an `int` anymore.

So, my suggestions are: 
 * An `InfinitePolynomialRing` should _not_ have an underlying polynomial ring by itself.
 * Only the _elements_ of an `InfinitePolynomialRing` should have an underlying polynomial ring.

The advantage of my suggestion is that the rings become much smaller.

Cheers,
     Simon


---

Comment by SimonKing created at 2009-03-09 16:32:09

I think I will be able to provide an alternative (=sparse) implementation soon. I think for `stretch` and the to-be-implemented permutation action, the sparse version is more convenient, while arithmetic might be faster in the dense version. However, I can only start the work on Wednesday.

Can you tell me what (coercion?) methods are needed to provide in order to have a smooth transition from sparse to dense and from dense to sparse?

And then I think there should also be a `subs` method, based on which it would be easy to implement a permutation action.


---

Comment by SimonKing created at 2009-03-12 09:08:18

Hi Mike!

Now, being back at work, I try an alternative implementation.

I wondered why you define `_coerce_map_from_` to return False whenever the second argument is an infinite polynomial ring (different from self, of course).

What do you think:
 * Should there be a coercion between two infinite polynomial rings that have the same variables in different order, such as 

```
sage: X.<x,y> = InfinitePolynomialRing(QQ)
sage: Y.<y,x> = InfinitePolynomialRing(QQ)
```

 I believe it should, because one also has 

```
sage: X.<x,y> = PolynomialRing(QQ)
sage: Y.<y,x> = PolynomialRing(QQ)
sage: X.has_coerce_map_from(Y)
True
```



---

Comment by SimonKing created at 2009-03-12 12:11:23

Hi Mike,

I found a point that I think requires more work:

```
sage: X.<x,y> = InfinitePolynomialRing(QQ)
sage: x[1]/y[2]
x1/y2
sage: _.parent()
Infinite polynomial ring in x, y over Rational Field
```


Hence, suddenly one has fractions, but they still belong to a *polynomial* ring. And:

```
sage: (x[1]/y[2]).parent().polynomial_ring()
Multivariate Polynomial Ring in x0, y0, x1, y1, x2, y2 over Rational Field
sage: (x[1]/y[2])._p.parent()
Fraction Field of Multivariate Polynomial Ring in x0, y0, x1, y1, x2, y2 over Rational Field
```


So, the parent of `x[1]/y[1]` expressed as a finite polynomial is a fraction field and is different from the underlying ring of the parent of `x[1]/y[1]`.

Do you agree that this should be sorted out?


---

Comment by SimonKing created at 2009-03-13 10:41:06

Meanwhile I implemented my approach to infinite polynomial rings. For the moment, I call them "symmetric polynomials", since Aschenbrenner and Hillar use the notion "symmetric ideals" (and implementing the algorithms of Aschenbrenner and Hillar is my aim).

Mike, since I took your implementation as a template, I named both you and me in the copyright notes.

I provide essentially the same methods than you. Main changes, compared with your implementation:
 * The `__pow__` method now also provides a permutation action.
 * The stretch method is *much* faster than in your implementation.
 * In order to have a sparse implementation, I probably had to take a compromise speed-wise. Can you please look whether the arithmetic in `SymmetricPolynomialRing` is sufficient for your purposes?
 * I allow coercions whenever variable names match (i.e., I coerce R into S if the generator names of R form a subset of the generator names of S, regardless of the order). Is this acceptable behaviour?

I took care about term orders. We have x[m]<y[n] iff
 * x appears before y in the list of generators, or
 * x=y and m<n

One technical question: I marked the `_coerce_map_from_` method as `@`cached. Is this allowed (probably yes, since we talk about parent structures, and they can be used in dictionaries)? Is this not necessary (perhaps the existence of coercions is cached anyway?)?

Here some examples:

```
sage: X.<x,y> = SymmetricPolynomialRing(QQ)
sage: p=x[10]*y[2]^3+2*x[1]*y[3]
sage: P=Permutation(((1,2),(3,4,5)))
sage: p^P
y1^3*x10 + 2*y4*x2
sage: x[5]<y[3]
True
sage: y[5]<y[3]
False
sage: p(x1=x[3],x10=y[1])
y2^3*y1 + 2*y3*x3
```


I could imagine to have both implementations in Sage, in particular if it turns out that there is a big speed difference in arithmetic. Please test!

To be continued (probably on a different ticket): Implement symmetric ideals (= ideals in an infinite polynomial ring that are set-wise invariant under variable permutations).


---

Comment by SimonKing created at 2009-03-13 10:42:18

This patch removes some print commands that I forgot to remove after debugging. To be applied after the other two patches


---

Attachment

I forgot one change w.r.t. your implementation: Division is not implemented except for scalar divisors.

Continuing the example from above:

```
sage: p/X(3)
1/3*y2^3*x10 + 2/3*y3*x1
sage: p/p
NotImplementedError                       Traceback (most recent call last)
...
NotImplementedError: Fraction Fields of Symmetric Polynomial Rings are not implemented
```


Cheers,
    Simon


---

Comment by SimonKing created at 2009-03-13 10:50:33

Sorry. I just realized that it works when I _attach_ `symmetric_polynomial.py` (this is how I obtained my examples above), but when I apply the patches and do ` sage -b` then sage fails on start-up, apparently when my file tries to import `Permutation_class`.

Can you explain this? I have to return home right now, but perhaps you know how to fix it.

Cheers,
   Simon


---

Attachment

To be applied after mhansen's patch. Replaces the other 'symmetric polynomial' patches


---

Comment by SimonKing created at 2009-03-13 20:28:54

(Concerning the patches: Please first apply `trac_5453.patch` and then `symmetric_polynomial.patch`. The third patch is now obsolete.)

I sorted the above mentioned import problem out (import of `Permutation_class`). Instead of importing this class and doing `is_instance`, I now test the presence of the attribute {{{to_cycles()}.

And, to my surprise, the arithmetics is faster than the "dense" implementation. I don't know the reason. 
Here, I make some very basic timings for `InfinitePolynomialRing` versus `SymmetricPolynomialRing`:

```
sage: X.<x,y> = SymmetricPolynomialRing(QQ)
sage: Y.<a,b> = InfinitePolynomialRing(QQ)
sage: p=x[10]*y[2]^3+2*x[1]*y[3]
sage: p2=x[100]*y[20]^3+2*x[10]*y[30]
sage: q=a[10]*b[2]^3+2*a[1]*b[3]
sage: q2=a[100]*b[20]^3+2*a[10]*b[30]
sage: timeit('r=p*p2')
625 loops, best of 3: 1.15 ms per loop
sage: timeit('r=q*q2')
125 loops, best of 3: 3.68 ms per loop
sage: timeit('r=p+p2')
625 loops, best of 3: 1.14 ms per loop
sage: timeit('r=q+q2')
125 loops, best of 3: 3.69 ms per loop
```


Cheers,
  Simon


---

Comment by SimonKing created at 2009-03-14 10:20:51

Recall that the starting point of my implementation was that the stretch method of the dense implementation requires too many resources in some cases.

However, my stretch implementation is _slower_ than yours, as long as the stretch factor is small and as long as one uses `timeit` and not `time`. 

The reason is: The critical part of the dense stretch method is the creation of a large polynomial ring. Once this is done, the ring is re-used, and it is very fast. In contrast, the sparse stretch method only creates a small ring (faster), but this has to be repeated over and over again.

Therefore one has:

```
sage: X.<x,y> = SymmetricPolynomialRing(QQ)
sage: Y.<a,b> = InfinitePolynomialRing(QQ)
sage: timeit('t=x[10].stretch(10)')
625 loops, best of 3: 194 Âµs per loop
sage: timeit('t=a[10].stretch(10)')
625 loops, best of 3: 92.8 Âµs per loop
sage: timeit('t=(x[10]*y[5]+x[100]*y[83]).stretch(500)')
125 loops, best of 3: 2.29 ms per loop
sage: time t=(a[10]*b[5]+a[100]*b[83]).stretch(500) # fails after 2:30 minutes:
------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```


So again, this is an argument to include _both_ implementation into Sage. That way, one can pick the method that is better for the respective application.

But who will review our patches? I guess neither of us. Should we ping malb?


---

Comment by malb created at 2009-03-16 11:25:33

From the outstanding discussion it seems this needs work rather than review already.


---

Comment by SimonKing created at 2009-03-16 12:26:51

Replying to [comment:19 malb]:
> From the outstanding discussion it seems this needs work rather than review already.

Yes, I think you are right. 

At least I would like to work a lot more on my implementation. But perhaps you think that Mike's patch is ready for inclusion? I wouldn't mind to let Mike's patch being merged and open a different ticket for my patch.


---

Comment by malb created at 2009-03-16 12:36:13

I think at least the interface should be agreed upon first. 


```
sage: X.<x,y> = SymmetricPolynomialRing(QQ)
sage: Y.<a,b> = InfinitePolynomialRing(QQ)
```


should be one name only and a parameters `dense`/`sparse` just like matrices.


---

Comment by SimonKing created at 2009-03-16 12:56:19

Replying to [comment:21 malb]:
> I think at least the interface should be agreed upon first. 
> 
> {{{
> sage: X.<x,y> = SymmetricPolynomialRing(QQ)
> sage: Y.<a,b> = InfinitePolynomialRing(QQ)
> }}}
> 
> should be one name only and a parameters `dense`/`sparse` just like matrices.

Makes sense.

I vote for the name `SymmetricPolynomialRing`, since Aschenbrenner and Hillar use the notion "Symmetric Ideals", e.g. in  arXiv:math/0411514 ("Finite generation of symmetric ideals"). Of course, when choosing this name, a permutation action should be implemented. But this can be easily done for Mike's approach as well.

But then, we should also agree on monomial orderings. Meanwhile, I am implementing support for different orderings (lex, deglex, degrevlex). But in either case, I have
  X.gen(i)[m] < X.gen(j)[n] iff i<j or (i==j and m<n)

Is this acceptable for you, Mike and Martin?


---

Comment by SimonKing created at 2009-03-19 15:34:24

I think it makes more sense to develop the _sparse_ approach on a different ticket -- see [#5566].
Hence, one should disregard my attachments, as everything is now at [#5566]...

And, concerning a common interface, I think it would be almost trivial to change the whole thing so that `SymmetricPolynomialRing(QQ,['x'],implementation='dense')` returns the same as `InfinitePolynomialRing(QQ,['x'])`

Can we agree to split the tickets, so that Mike's original ticket is now 'with patch, needs review'?


---

Comment by malb created at 2009-03-19 15:49:24

Replying to [comment:23 SimonKing]:
> And, concerning a common interface, I think it would be almost trivial to change the whole thing so that `SymmetricPolynomialRing(QQ,['x'],implementation='dense')` returns the same as `InfinitePolynomialRing(QQ,['x'])`

At least some agreement on the name should be reached.


---

Comment by SimonKing created at 2009-03-20 20:11:57

Replying to [comment:24 malb]:
> At least some agreement on the name should be reached.

I sketched my opinion already: 
 * If the aim is an implementation of the algorithm of Aschenbrenner and Hillar, we should use the word ``Symmetric``, since they do.
 * If it is just about having a convenient way to provide an unbounded number of variables, than ``InfinitePolynomialRing`` is fine as well. 
 * Since i think that the most ambitious part of the implementation is in fact the Gröbner basis computation, I vote for 'Symmetric'.

But what do you think?


---

Comment by hivert created at 2009-03-28 19:18:31

Let me add my two cents: It seems to me that the if something is called "the ring of symmetric polynomials" this is *not* what you implement under the name `SymetricPolynomialRing` so that I'm against such a name. 

Another argument is that it is extremely likely that some people working in combinatorics will need "the ring of symmetric polynomials" (in a finite number of variable). We already have a the ring of "symmetric functions" that is the case of an infinite number of variables. Note that, whether they are polynomials or not is always subject to discussion: they have an infinite number of monomials but they have a finite degree. We (combinatorician) choose the name functions for those finite degree series in an infinite number of variables.

Anyway, going back to your case, what about `PolynomialRingWithSymmetry` ?

Cheers,

Florent


---

Comment by SimonKing created at 2009-03-28 20:56:01

Dear Florent,

thank you very much for the input!

Replying to [comment:26 hivert]:
> Let me add my two cents: It seems to me that the if something is called "the ring of symmetric polynomials" this is *not* what you implement under the name `SymetricPolynomialRing` so that I'm against such a name. 

It is correct that the _polynomials_ are not symmetric. But the ring has an action of an infinite symmetric group, and the (or at least _my_) motivation was an implementation of Symmetric Ideals (they do deserve the attribute 'symmetric') and their Gröbner bases (see ticket #5566). So, it is not the 'ring of symmetric polynomials' but a 'symmetric ring of polynomials'.

> Another argument is that it is extremely likely that some people working in combinatorics will need "the ring of symmetric polynomials" (in a finite number of variable). 

That's half right. Aren't these called 'invariant rings' rather than 'symmetric rings'?

> We already have a the ring of "symmetric functions" that is the case of an infinite number of variables. Note that, whether they are polynomials or not is always subject to discussion: they have an infinite number of monomials but they have a finite degree. We (combinatorician) choose the name functions for those finite degree series in an infinite number of variables.

Here we clearly talk about polynomials: The elements of the 'infinite' or 'symmetric' polynomial ring are _finite_ sums of monomials. While the number of variables in the ring is infinite, the number of variables occuring in one polynomial is finite.


---

Comment by SimonKing created at 2009-03-28 22:16:46

Dear Florent,

Replying to [comment:27 SimonKing]:
> It is correct that the _polynomials_ are not symmetric. But the ring has an action of an infinite symmetric group, and the (or at least _my_) motivation was an implementation of Symmetric Ideals (they do deserve the attribute 'symmetric') and their Gröbner bases (see ticket #5566). So, it is not the 'ring of symmetric polynomials' but a 'symmetric ring of polynomials'.

I think my suggestion "symmetric polynomial ring" is partially due to the fact that in German it is "symmetrischer Polynomring" -- hence, clearly it is a polynomial ring that has a symmetry, and not a ring of symmetric polynomials ("Ring symmetrischer Polynome" in German). 

Perhaps native english speakers can help here:

Is your suggestion "polynomial ring with symmetry" the shortest way to express "symmetrischer Polynomring" in English? 

Is the natural English understanding "((symmetric polynomial) ring)" or "(symmetric (polynomial ring))"?

Best regards,
     Simon


---

Comment by SimonKing created at 2009-03-29 00:06:20

Hi!

I just had a look at the abstract of Aschenbrenner's and Hillar's articles. The title of one article is "An Algorithm for Finding Symmetric Gröbner Bases in Infinite Dimensional Rings". They talk about "symmetric ideals", but again they say "infinite dimensional polynomial ring", not "symmetric polynomial ring".

This convinces me that Mike's InfinitePolynomialRing is better than SymmetricPolynomialRing, and that the word "symmetric" should be reserved to the ideals and Gröbner bases of that ring.

Here some thoughts about a unification:
   Both in Mike's and my implementation, an element p of the ring R essentially has an attribute _p, which is a 'usual' polynomial: p._p gives the value of p. 
   In Mike's implementation, the ring R has and attribute P (a polynomial ring) so that p._p is guaranteed to be coercible into P, for any `p \in R`. This allows for usual arithmetic.
   In my implementation, it is possible that coercion does not provide arithmetic for p._p and q._p, for p and q in R. _Only_ if it does not, then i explicitly construct a common parent for p._p and q._p. So, Mike's arithmetic is a special case of mine.

Do we agree on the following technical details of a potential unification?
 * Compared with SymmetricPolynomialRing_class, InfinitePolynomialRing_class has one additional attribute `P`, and the arithmetic of InfinitePolynomial is just a special case of the arithmetic of SymmetricPolynomial. So, the init method might have an optional parameter `implementation`, and if this is 'dense' then the ring is initialized together with an attribute `P`. Otherwise, it is without `P`.
 * In the methods of InfinitePolynomial and SymmetricIdeal, we could test whether the underlying infinite ring has an attribute P. If it has (dense implementation), the methods choose your algorithm, otherwise they choose mine. 

In the end, we would have a dense and a sparse implementation, and the computation of symmetric Gröbner bases would be possible in _both_ cases.

Do you think it works? How should the work be organised? Here? #5566? New ticket?

Cheers
     Simon


---

Comment by SimonKing created at 2009-03-30 11:51:44

Meanwhile i can provide a uniform interface for the dense and the sparse approach. In both approaches, one can compute symmetric Gröbner bases. And: Dense seems indeed to be faster.

Since i am owner for #5566, i've put my patch there. Hope you are not upset.

The name of the rings is now InfinitePolynomialRing, and they can be created in dense or sparse implementation.

Due to differences in the interface of uni- and multivariate polynomials, a bug occured in the reduce method; i need to fix this, thus #5566 currently is 'needs work'. But perhaps you can already have a look if the implementation makes sense.


---

Comment by mhansen created at 2009-06-04 18:14:34

Resolution: fixed


---

Comment by mhansen created at 2009-06-04 18:14:34

This was fixed due to #5556.
