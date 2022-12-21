# Issue 6922: Matrix term ordering

Issue created by migration from Trac.

Original creator: klee

Original creation time: 2009-09-11 04:47:10

Assignee: Somebody

CC:  novoselt

Keywords: term order

In Sage, I am trying to construct a polynomial ring with matrix
ordering. 
....
AFAIK, it is not implemented, but I think that some people were
working on it.

It is in fact one of the things that I miss in Sage's polynomial rings
(the other thing are supercommutative rings), so that I need to use
the Singular interface rather than libsingular. 
....
Anyway it will be great that the matrix ordering is included in Sage
natively. 


---

Comment by klee created at 2009-09-11 05:05:37

The patch introduces matrix term ordering, but it does not work yet unfortunately.


```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: local2
sage: R.<x,y>=PolynomialRing(QQ,order="matrix(1,3,1,0)")
sage: r=singular(R)
sage: r
| Sage Version 4.1.1, Release Date: 2009-08-14                       |
| Type notebook() for the GUI, and license() for information.        |
//   characteristic : 0
//   number of vars : 2
//        block   1 : ordering M
//                  : names    x y 
//                  : weights  1 3 
//                  : weights  1 0 
//        block   2 : ordering C
sage: f=x^2+y
sage: f.lt()
x^2
sage: f=x^3+y
sage: f.lt()
x^3
sage: t=R.term_order()
sage: t
matrix(1,3,1,0) term order
```


Please someone who knows better check the patch, and make it work!

Simon says:

Better wait for a proper implementation in libsingular 
(which is beyond my capabilities, I am afraid).

Cheers,
Simon


---

Comment by malb created at 2009-09-11 10:20:32

I don't think we should support the 'matrix()' syntax. The Singular syntax is 'M()' which we should support for compatibility and familiarity. However, adding another string expression does not seem to make sense, because we will be able to simply write `order=A` where A is an integer matrix which is much more python-ic.


---

Comment by klee created at 2009-09-12 01:30:35

I agree partially. Should we follow the Singular syntax exactly? For short syntax, how about just "m(1,3,1,0)"? I personally think the Singular syntax for term ordering is somewhat cryptic.

I think it is better for Sage to support both the string description and `TermOrder` description. Thus for examples,


```
order='m(1,3,1,0)'+'deglex(2)'
```



```
order='m(1,3,1,0),deglex(3)'
```


for a square matrix m,

```
order=TermOrder(m)+TermOrder('deglex',3)
```


are all supported.

Marshall Hampton says:

I agree with John that Simon's example:


```
  sage: M = Matrix(2,2, [1,3,1,0])
  sage: R.<a,b,c,d,e,f> = PolynomialRing(QQ, order=TermOrder(M)
+TermOrder('deglex',3))
```


looks good and reasonably intuitive to me.


---

Comment by malb created at 2009-09-12 09:59:02

Replying to [comment:3 klee]:
> I agree partially. Should we follow the Singular syntax exactly? For short syntax, how about just "m(1,3,1,0)"? I personally think the Singular syntax for term ordering is somewhat cryptic.

Sure, but it would be accepted anyway and passed through to Singular (in an ideal implementation) :)

> I think it is better for Sage to support both the string description and `TermOrder` description. Thus for examples,
> 
> {{{
> order='m(1,3,1,0)'+'deglex(2)'
> }}}
> 
> {{{
> order='m(1,3,1,0),deglex(3)'
> }}}

This description is a mix of Singular syntax and Sage string syntax. I would like to avoid Sage string syntax as much as possible.

> for a square matrix m,
> {{{
> order=TermOrder(m)+TermOrder('deglex',3)
> }}}
> are all supported.

I like this best.
 
> Marshall Hampton says:
> 
> I agree with John that Simon's example:
> 
> {{{
>   sage: M = Matrix(2,2, [1,3,1,0])
>   sage: R.<a,b,c,d,e,f> = PolynomialRing(QQ, order=TermOrder(M)
> +TermOrder('deglex',3))
> }}}
> 
> looks good and reasonably intuitive to me.

Yep, that's what I would be aiming for.


---

Comment by klee created at 2010-05-25 15:05:33

The replaced patch is still in beta stage, due to lack of docstrings. It adds matrix ordering to Sage term order suite, which works fine. It is based on Sage 4.4.2. The reason that I uploaded this premature patch is related with the ticket !#9003


---

Comment by klee created at 2010-05-25 15:05:33

Changing status from new to needs_work.


---

Comment by klee created at 2010-05-27 02:23:47

The replaced patch now works, though only with PolyDict engine.


---

Comment by klee created at 2010-05-27 02:23:47

Changing status from needs_work to needs_review.


---

Comment by malb created at 2010-06-02 18:41:59

Replying to [comment:6 klee]:
> The replaced patch now works, though only with PolyDict engine.

Sorry for being a bit obnoxious about it, but shouldn't this be needs work until it works across the board? At least we should fall back to the `PolyDict` version automatically if a matrix term ordering is selected or something.


---

Comment by klee created at 2010-06-03 00:55:10

Changing status from needs_review to needs_work.


---

Comment by klee created at 2010-06-03 00:55:10

Replying to [comment:9 malb]:

> Sorry for being a bit obnoxious about it, but shouldn't this be needs work until it works across the board? At least we should fall back to the `PolyDict` version automatically if a matrix term ordering is selected or something.   

I am sorry that I cannot understand what you mean. Do you mean that matrix term order should work with Singular version before this patch is merged? Now, if a matrix term ordering is selected, then {{PolyDict}} version is used automatically because Singular version does not support matrix term ordering. If someone implements matrix term ordering with Singular version, then I would be happy. I have been waiting for this to be done. As it is not the case, I thought it's not bad to add matrix term ordering support only with {{PolyDict}} version--Singular version may be added later.


---

Comment by malb created at 2010-06-03 21:29:05

> I am sorry that I cannot understand what you mean. Do you mean that matrix term 
> order should work with Singular version before this patch is merged? Now, if a 
> matrix term ordering is selected, then `PolyDict` version is used 
> automatically because Singular version does not support matrix term ordering. 

Right, I forgot that I implemented to fall back this way :) Okay, my bad then. 

> If someone implements matrix term ordering with Singular version, then I would be 
> happy. 

We all would be happy. All one needs to do btw. is to fix the constructor.

> I have been waiting for this to be done. 

Why not give it a try yourself? I'd love to help but other commitments prevent me from doing so.

> As it is not the case, I thought it's not bad to add matrix term ordering support 
> only with `PolyDict` version--Singular version may be added later. 

You are right, I stand corrected.


---

Comment by malb created at 2010-06-03 21:29:05

Changing status from needs_work to needs_review.


---

Comment by malb created at 2010-06-03 21:30:21

I stand corrected twice. YOU implemented it to fall back not me. I thought the automatic fallback would kick in, but from your patch it looks like it doesn't.


---

Comment by malb created at 2010-06-03 21:41:10

* `NotImplementedError, "Singular engine in Sage cannot handle matrix ordering yet."` should be replaced by `NotImplementedError("Matrix term orderings are not supported by the libSingular interface yet."` or something along those lines. I propose this change to make it clearer that Singular can indeed deal with Matrix term orderings and that it is us who cannot.
 * `TypeError: Cannot use a matrix term order as a block.` shouldn't that be a `NotImplementedError`?
 * I thought the agreement was not to allow 'matrix(0,1,2,3)' but to use Singular's convention instead? It seems you are allowing at and using it internally.


---

Comment by malb created at 2010-06-03 21:52:02

Oh, one more thing, isn't


```python
TermOrder([0,1,2,3])
```


ambiguous since it could be interpreted as a list of weights? I'd vote to not to allow it for matrix term orders.


---

Comment by klee created at 2010-06-04 01:22:54

Replying to [comment:13 malb]:

> * `NotImplementedError, "Singular engine in Sage cannot handle matrix ordering yet."` should be replaced by `NotImplementedError("Matrix term orderings are not supported by the libSingular interface yet."` or something along those lines. I propose this change to make it clearer that Singular can indeed deal with Matrix term orderings and that it is us who cannot. 

I agree.

> * `TypeError: Cannot use a matrix term order as a block.` shouldn't that be a `NotImplementedError`? 

I know Singular allow matrix term orderings in block order. But this feature is not one of the aims of the current patch. That could be included in a future patch that use Singular version.

> * I thought the agreement was not to allow 'matrix(0,1,2,3)' but to use Singular's convention instead? It seems you are allowing at and using it internally.

I did not agree then. :-) Anyway, I will change it to 'm(...)'


---

Comment by klee created at 2010-06-04 01:24:15

Replying to [comment:14 malb]:

> Oh, one more thing, isn't ` #!python TermOrder([0,1,2,3]) ` ambiguous since it could be interpreted as a list of weights? I'd vote to not to allow it for matrix term orders. 

Ok.


---

Attachment

replaced


---

Comment by malb created at 2010-06-24 12:38:56

The patch applies cleanly and doctests pass.

I'm still not happy with the interface:


```python
sage: P.<a,b> = PolynomialRing(GF(32003),order=TermOrder(Matrix([1,2,0,3])))
sage: P.term_order()
m(1,2,0,3) term order
```


This uses the non-standard "m(...)" representation which I would avoid. I'd be happy with either "M()" (Singular notation) or "Matrix term ordering with matrix ..." or so.

Also, the "m()" notation is allowed but shouldn't.


```python
sage: P.<a,b> = PolynomialRing(GF(32003),order='m(1,2,0,3)')
```


I understand that this is a typical paint-the-bike-shed scenario and in particular a question of choice. Still, I think we shouldn't invent more ad-hoc string notation when (a) there is an established notation and (b) we have a much nicer object oriented way of constructing term orderings.

However, since this isn't really that big of a deal, I am okay with being overruled by some other referee who disagrees.

PS: Apologies for taking so long to revisit this ticket.


---

Comment by klee created at 2010-06-25 00:51:05

Changing status from needs_review to needs_work.


---

Comment by klee created at 2010-06-25 00:51:05

Replying to [comment:17 malb]:

I prefer "Matrix term ordering with matrix ...".

both "M(1,2,0,3)" and "m(1,2,0,3)" is allowed, which is not bad. The situation is the same with other orderings like "Lex", which is converted to lower case internally. I don't mind that "M(...)" should be the official string representation of matrix orderings.

I am working to make matrix ordering work with Singular version. I am not really confident whether the code is sound as it is based on a knowledge obtained by a reverse engineering of libSingular Sage interface. 

I will upload a revised patch soon, perhaps within a couple of hours. Then I wish you again to review the patch.


---

Comment by klee created at 2010-06-25 04:56:16

with singular version support


---

Comment by klee created at 2010-06-25 04:58:21

Changing status from needs_work to needs_review.


---

Attachment

The new patch supports also the Singular version.  Now "M(...)" is the official string representation of matrix  orderings.


---

Comment by malb created at 2010-06-25 07:09:04

Replying to [comment:18 klee]:
> The situation is the same with other orderings like "Lex", which is converted to 
> lower case internally.

Good point, I'm convinced.

> I am working to make matrix ordering work with Singular version. I am not really 
> confident whether the code is sound as it is based on a knowledge obtained by a 
> reverse engineering of libSingular Sage interface. 

Great, I'll take a look.


---

Comment by malb created at 2010-06-25 09:06:19

Patch looks good (small issue see below), applies cleanly, doctests pass.

So, this stuff now works, very cool:


```python
sage: P = PolynomialRing(GF(127),2,'x',order=Matrix([1,2,0,3]))
sage: P.term_order()
Matrix term order with matrix
[1 2]
[0 3]
sage: magma(P)
Polynomial ring of rank 2 over GF(127)
Order: Weight [full]
Variables: x0, x1
sage: singular(P)
//   characteristic : 127
//   number of vars : 2
//        block   1 : ordering M
//                  : names    x0 x1
//                  : weights   1  2
//                  : weights   0  3
//        block   2 : ordering C
```


I've attached a small referee patch which Kwankyu or someone else has to sign of. Kwankyu's patch gets a positive review modulo the issue in the referee patch.


---

Attachment

apply after klee's patch


---

Attachment

combined with referee's patch


---

Comment by klee created at 2010-06-25 10:54:19

Changing status from needs_review to positive_review.


---

Comment by klee created at 2010-06-25 10:54:19

Positive review for the referee's patch. Thank you!


---

Comment by mpatel created at 2010-07-20 08:38:47

I'm applying just `trac#6922_final.patch` to 4.5.2.alpha0.  Just let me know if I'm wrong.


---

Comment by mpatel created at 2010-07-20 09:21:03

Resolution: fixed
