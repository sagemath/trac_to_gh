# Issue 7016: Bizarre results when taking the mod of a p-adic number

Issue created by migration from https://trac.sagemath.org/ticket/7016

Original creator: jonhanke

Original creation time: 2009-09-26 01:54:51

Assignee: tbd

CC:  wstein mabshoff roed

Keywords: padic, mod, %

The operation x % n for p-adic numbers x and integers n currently depends on the creation method of the p-adic number (not just it's equality).  It also does not seem to return meaningful results!


---

Comment by jonhanke created at 2009-09-26 01:59:51


```
## Create a p-adic number in two ways
sage: e = 1 + O(2^20)  ## Explicit creation
sage: e
1 + O(2^20)
sage: c = Qp(2)(1)     ## By coercion
sage: c
1 + O(2^20)
sage: e == c
True

## Check their types
sage: type(e)
<type 'sage.rings.padics.padic_capped_relative_element.pAdicCappedRelativeElement'>
sage: type(c)
<type 'sage.rings.padics.padic_capped_relative_element.pAdicCappedRelativeElement'>

## Use the mod operation, with inconsistent results: (I expected the integer 1 in both cases)
sage: e % 8
1 + O(2^20)
sage: c % 8
0
sage: e % 8 == c % 8
False

## Check the mod types
sage: type(e % 8)
<type 'sage.rings.padics.padic_capped_relative_element.pAdicCappedRelativeElement'>
sage: type(c % 8)
<type 'sage.rings.padics.padic_capped_relative_element.pAdicCappedRelativeElement'>


## Check their lifts
sage: e.lift()
1
sage: c.lift()
1
sage: c.lift() == e.lift()
True
sage: c.lift() % 8 == e.lift() % 8
True


```




Suggestions:


1) x % M returns an integer when x is a p-adic number (in Qp) and M is
   an integer or raises an error if either the modulus is not a power
   of p or is larger than the known precision of the number allows.
   This syntax will return an error for any (non-trivial) extensions
   of Qp.

2) Add a more general syntax x.reduce_mod_prime() returns an element
   of FiniteField(q) whenever x is an element of an unramified
   extension Qq of Qp.

3) It might also be nice to have an x.reduce_mod_prime_power(n) which
   would return an element in the associated finite quotient ring
   Q_q/((pi)**n), but this may not be worth the effort right now.


---

Comment by roed created at 2009-09-26 05:54:03

This is a consequence of the fact that those two elements have different parents: 

```
sage: parent(1+O(2^20))
2-adic Ring with capped relative precision 20
sage: parent(Qp(2)(1))
2-adic Field with capped relative precision 20
```


Most rings in sage return an element of the same ring when applying the operation %.  The function you want is residue.


```
sage: a = Zp(2)(1); b = Qp(2)(1)
sage: a.residue(3), b.residue(3)
(1, 1)
sage: a.residue(3).parent(), b.residue(3).parent()
(Ring of integers modulo 8, Ring of integers modulo 8)
sage: c = Qp(2)(1/2)
sage: c.residue(3)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

ValueError: Element must have non-negative valuation in order to compute residue.
```


There are some tricky questions for % and // and how they relate.  A similar issue bit William this past spring, so maybe we should have a design discussion about how to solve it.  I'm probably not going to be working on the p-adics this fall though: my advisor wants me to work on my thesis.  ;-)


---

Comment by roed created at 2010-12-26 21:33:06

Changing priority from critical to major.


---

Comment by roed created at 2010-12-26 21:33:06

I was just glancing through tickets and found this one.  If anyone has suggestions for making % and // less confusing, please let me know.  There's documentation, but it's hidden in double underscore methods, so often doesn't get seen.


---

Comment by roed created at 2010-12-26 21:33:06

Changing component from algebra to padics.


---

Comment by rozenszt created at 2016-03-21 17:19:33

New commits:


---

Comment by rozenszt created at 2016-03-21 17:19:33

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2016-03-21 17:33:29

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2016-03-21 17:33:29

Personally, I don't think that the sentence "This is different from the mod function `%` which returns an element with the same parent." really clarifies anything.


---

Comment by jdemeyer created at 2016-03-21 17:46:10

Replying to [comment:3 roed]:
> This is a consequence of the fact that those two elements have different parents: 
> 
> Most rings in sage return an element of the same ring when applying the operation `%`.  The function you want is residue.
> 
> There are some tricky questions for `%` and `//` and how they relate.

That may be, but it's still a poor excuse for having "bizarre" results for `%`. If `%` makes no sense, better disallow it completely.


---

Comment by rozenszt created at 2016-03-22 06:49:19

Replying to [comment:12 jdemeyer]:
> Personally, I don't think that the sentence "This is different from the mod function `%` which returns an element with the same parent." really clarifies anything.

Actually there is already a detailled explanation of how the mod function works in its documentation, so the point of the note is mostly to direct people to the approriate documentation.


---

Comment by git created at 2016-11-17 22:24:45

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by saraedum created at 2016-11-17 22:26:27

Changing status from needs_work to needs_review.


---

Comment by git created at 2016-11-17 22:55:47

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2016-11-17 23:06:47

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by roed created at 2016-11-17 23:19:36

Looks good.


---

Comment by roed created at 2016-11-17 23:19:36

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2016-11-19 22:10:07

Resolution: fixed
