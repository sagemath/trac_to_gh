# Issue 1399: Problems with arithmetic

Issue created by migration from Trac.

Original creator: ljpk

Original creation time: 2007-12-04 22:49:22

Assignee: somebody

There are some operations which are either unimplemented or give (what I would consider to be) wrong answers:

N=-7

N.is_prime()
>>false

I believe that this should give the answer "true".

Also, if one tries
`ZZ.ideal(N).is_prime()`

one gets a NotImplementedError.


---

Comment by mhansen created at 2007-12-06 04:46:56

Apply this patch after #1398 .


---

Comment by mhansen created at 2007-12-06 04:46:56

Changing assignee from somebody to mhansen.


---

Comment by mhansen created at 2007-12-06 04:46:56

Changing status from new to assigned.


---

Attachment


---

Comment by was created at 2007-12-13 23:10:19

NO!!!!!!

The change to ideal.py is fine, but making is_prime(-7) return True is *wrong*.

Justification:

```
sage: gp.eval('isprime(-7)')
'0'
sage: prime_range(-10,10)
[2, 3, 5, 7]
```

and in Wikipedia it says:
 
"In mathematics, a prime number (or a prime) is a natural number which has exactly two distinct natural number divisors: 1 and itself."

and more importantly it says the same thing in my elementary number theory book.

So NO.

However, the change to ideal.py is fine.


---

Comment by was created at 2007-12-13 23:11:21

Oh, I should add that  Magma defines -7 to be Prime


```
sage: magma.eval('IsPrime(-7)')
'true'
```



---

Comment by rlm created at 2007-12-13 23:25:56

Note:

```
sage: I = ZZ.ideal(-7)
sage: I.gens()
(-7,)
```

If the change to integer.pyx isn't accepted, then the change to ideal.py needs to account for -1.


---

Attachment

Revised patch by John Cremona


---

Comment by cremona created at 2008-02-16 18:33:42

Replacement patch handles these issues as follows:

   * for Integers the method is_prime() only returns True for _positive_ primes, as agreed.
   * Integers have a new method is_irreducible() which is True for +p and -p where p is prime
   * the is_prime() method for ideals in a PID is almost as in mhansen's patch, but it tests if the generator is_irreducible() rather than is_prime().  So not only does it work properly for integer ideals, it also now works for ideals in polynomial rings (in one variable) over a field -- see doctests.
   * All relevant doctests have been updated
   * I changed IntegerModRing(n) to work for negative n (it just uses -n instead) which makes sense to me.


---

Comment by cremona created at 2008-02-16 18:54:06

to be applied after 1399new.patch


---

Attachment

Small addendum to previous:  I forgot to return True for the zero ideal (which is prime in a PID!)
Both patches 1399new.patch and 1399newextra.patch shold be applied.


---

Comment by dmharvey created at 2008-02-23 13:01:22

Very nice. Code looks good to me, all doctests pass after applying 1399new.patch and 1399newextra.patch to 2.10.1.


---

Attachment


---

Comment by was created at 2008-02-24 21:08:29

Apply the last three patches in order.


---

Comment by mabshoff created at 2008-02-24 21:19:03

Resolution: fixed


---

Comment by mabshoff created at 2008-02-24 21:19:03

Merged 1399new.patch, 1399newextra.patch and sage-1399-3_of_3.patch in Sage 2.10.3.alpha0
