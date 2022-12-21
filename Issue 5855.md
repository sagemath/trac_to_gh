# Issue 5855: [with patch, needs review] implement squarefree_divisors function

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2009-04-22 15:30:53

Assignee: somebody

e.g.

```
sage: list(squarefree_divisors(12))
[1, 2, 3, 6, -1, -2, -3, -6]
```



---

Comment by dmharvey created at 2009-04-25 01:07:37

Hmmm, is this supposed to work only for integers? If so, shouldn't it be a method on Integer? You might run into trouble if you apply it to an element of a ring of integers where there are more units than +1 and -1.


---

Comment by kcrisman created at 2009-04-26 02:51:59

Isn't there a lot of stuff in this file (arith.py) like that, though?  I'm not saying dmharvey is wrong, just that there is probably a lot of work to be done with figuring out where all these arithmetic functions go, since a lot of the ones here (e.g. is_prime_power) really are assuming we are working over the standard ring of integers, even though they are top-level in the rings directory.  So it would seem reasonable to add the functionality and then have someone make a new ticket asking for arith.py to be somehow refactored (yet still globally imported).


---

Comment by was created at 2009-04-26 05:38:13

Note that is_prime_power explicitly coerces its input to ZZ first, whereas squarefree_divisors doesn't.  

Also, just because some code wasn't written in a certain way in arith.py long ago, doesn't mean we should continue in that direction now.   You might as well argue that lots of code has no doctests, so "it would seem reasonable to write lots more code with no doctests and then have someone make a new ticket to add doctests".  It's the same argument you make above, but with "doctests" instead of "making sense over more general rings". 

Regarding the actual patch, David says "Hmmm, is this supposed to work only for integers?".  Note that the first sentence of the docstring says "Iterator over the squarefree divisors of the integer N."

The only reasonable options seem to be:

  1. This should be a method of integers, or

  2. The input should be coerced to ZZ, or

  3. The function is modified so it works over more general rings, and it is stated in the docs that it is "squarefree up to units", and works for any ring where the prime_divisors function works.   Note that prime_divisors works for *any* ring where factor works. 


I like 3 the best.


---

Comment by dmharvey created at 2009-04-26 11:59:03

I agree, I prefer (3). Although I'm not sure I completely believe that `prime_divisors` really does the right thing over arbitrary rings, it also seems to have a bias regarding -1.

I also don't like that the `divisors` function returns only positive divisors, but the proposed `squarefree_divisors` returns negative ones as well. I imagine the user would typically want only the positive ones, and they can easily add the negative ones if that's what they want.


---

Attachment


---

Comment by cremona created at 2009-04-28 17:53:22

I'm a bit late to this discussion.  I see that the new funtcion applies, for example, tp ZZ[x], but gives the wrong results because factor() is wrong for that ring:

```
sage: R.<x> = ZZ[]
sage: f = 30*x
sage: f.factor()
30 * x
```

which should return 2*3*5*x, if we mean the factors to be irreducibles in th parent ring.  Unless we make a deliberate design decision not to (since then factorization obviously becomes as hard as in ZZ).


---

Comment by dmharvey created at 2009-04-28 19:03:52

Thumbs up.

John, I agree the results are wrong for ZZ[x], but that should be on a different ticket. (My 2c on that: I think the return value should be 2*3*5*x in your example, because algebraically that makes the most sense. The user should be aware that integer factorisation is hard, and they always have the option to remove the content manually if that suits their application.)


---

Comment by cremona created at 2009-04-28 19:50:43

OK for this patch.  FOr the wider issues, here's what I think we should do.  There are several divisor-related functions (including divisors(), square-free-divisors(), and some more) all of which are trivial get from a Factorization object such as is returned by factor() on a large variety of things (not just rings: think of ideal factorizations in number fields, for example).

So I think the Factorization class should implement all these.  By default they should ignore unit factors (if users know that there are finitely many users they can have a separate iterator over those and multiply).

Then for the most general kind of ring where factorization makes sense (should be a UFD mathematicall) we put in a factor() function which is a placeholder (NotImplemented) together with a few one-line functions which return for example divisors() by just doing self.factor().divisors().  Then for any subsidiary classes which actuall implement factor(), these associated functions are automatically available.

Does any of that make sense?


---

Comment by cremona created at 2009-04-28 20:05:44

See #5921 for improved handling of the content in integer poly factorization.  I may not have done the correct cythonic things.


---

Comment by mabshoff created at 2009-04-30 05:51:51

Merged in Sage 3.4.2.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-30 05:51:51

Resolution: fixed
