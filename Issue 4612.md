# Issue 4612: [with patch, needs review] is_perfect_power for rationals

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-11-25 07:21:25

Assignee: somebody




---

Comment by craigcitro created at 2008-11-27 07:50:18

The code looks good, but doesn't handle negatives correctly:


```
sage: (-1/25).is_perfect_power()
True
```


Fix is pretty obvious (call `mpz_sgn` on the numerator, make sure we don't get -1), so I'm adding a patch that fixes it.


---

Comment by craigcitro created at 2008-11-27 08:05:16

Actually, I retract my review above. This patch is completely wrong! In particular, look at this:


```
sage: (4/27).is_perfect_power()
True
```


That's absolutely not a perfect power! This code is too naive. If both the numerator and denominator are perfect powers, we need to see what powers they are, and make sure that one of the powers divides the other. Here's a battery of tests that needs to pass:


```
 sage: (2/27).is_perfect_power()
 False
 sage: (4/27).is_perfect_power()
 False
 sage: (-1/25).is_perfect_power()
 False
 sage: (-1/27).is_perfect_power()
 True
```


One might want even more doctests ...


---

Comment by robertwb created at 2008-11-28 08:18:00

Oops... Yeah, that's totally wrong. I'll fix this.


---

Comment by cremona created at 2008-12-19 20:35:23

It won't be trivial to fix since the gmp function only returns whether or not the argument is a perfect power, not what the root or exponents are.

I suggest that we implement something involving the factorizations.  Assuming that both numerator and denonimator are perfect powers, compute (where the input is r = +-n/d)

```
gcd(gcd([e for p,e in n.factor()]), gcd([e for p,e in d.factor()]))
```

If that is 1 return 1.  If it is e>1 then return e if r is positive or if e is odd and r is negative, otherwise (e even, r<0) return e.prime_to_m_part(2), i.e. the odd part of e.  This will return the largest e such that r is an e'th power.

I don't see what else we can do unless gmp has a better function.


---

Comment by robertwb created at 2008-12-19 21:04:55

Factoring the numerator/denominator completely may be prohibitively expensive. It would probably be cheaper to compute the nth root and see if it is exact for n in from 2 to lg(n).


---

Comment by robertwb created at 2008-12-19 21:24:58

I just looked at the gmp source, it does trial division for all three-digit primes, aborting if it finds any inconsistency. If small factors were found, it can bound the nth roots it needs to test on the remainder (if any), otherwise it tries taking nth roots for primes up to lg(2). 

It does not compute the largest exponent for which it is an nth root, only a divisor of it. I wonder if MPIR will would be willing to provide such a function. 

However, I believe there is an easier solution. Noting that the numerator and denominator are relatively prime, one only needs to check if the product is a perfect power, and if it is their ratio will be as well. (It is unclear however whether or not it would be a time savings to do the (cheaper) test on the smallest of the numerator/denominator first.)


---

Comment by cremona created at 2008-12-19 23:08:30

Replying to [comment:6 robertwb]:
> I just looked at the gmp source, it does trial division for all three-digit primes, aborting if it finds any inconsistency. If small factors were found, it can bound the nth roots it needs to test on the remainder (if any), otherwise it tries taking nth roots for primes up to lg(2). 

ok -- I had not thought of checking the p-valuation for small primes but that's a good idea.  Otherwise it's the textbook method, which would not be hard to adapt to provide the exponent.

> 
> It does not compute the largest exponent for which it is an nth root, only a divisor of it. I wonder if MPIR will would be willing to provide such a function. 

That would be good.  All we have to do is ask!

> 
> However, I believe there is an easier solution. Noting that the numerator and denominator are relatively prime, one only needs to check if the product is a perfect power, and if it is their ratio will be as well. (It is unclear however whether or not it would be a time savings to do the (cheaper) test on the smallest of the numerator/denominator first.)

Certainly it's clear that you can replace n/d by n*d, but we already know what to do if know the numerator is an e'th power and the denom is an f'th power (answer = gcd(e,f), or the odd part of that if the number was negative), which would be more efficient.  So as long as we can solve the problem (with the exponent) for integers then it will be easy to do it for rationals.


---

Attachment


---

Comment by robertwb created at 2008-12-19 23:23:43

A new patch is up. If n/d is a not perfect power, it is usually cheaper to check min(n,d) for being a perfect power first, but that is redundant if n/d is in fact a perfect power. I added an extra parameter to handle that, let me know if you think it's a good idea or excessive. 

It is more work to figure out the maximal exponent a number can be expressed with than it is to detect whether it can be expressed with any exponent. For example, consider $p^(2r) / q^(2s)$. It is easy to detect that both are perfect squares, but finding r and s is more work. 

Clearly, the optimal solution would look something like gmp's mpz_perfect_power_p done in parallel on the numerator and denominator.


---

Comment by cremona created at 2008-12-20 21:18:47

Something is wrong:

```
sage: a=(-1/20)^3
sage: a.is_perfect_power()
False
```

but then so is this:

```
sage: a=(-20)^3
sage: a.is_perfect_power()
False
```

which does not call the new function but the old one (with integers).  Is this a bug in gmp?  If so it should be reported.


---

Comment by robertwb created at 2008-12-20 21:41:29

Integer.is_perfect_power is a direct call to mpz_perfect_power_p. Looks like a bug in gmp to me. That's really bad.


---

Comment by cremona created at 2008-12-21 12:04:57

Replying to [comment:10 robertwb]:
> Integer.is_perfect_power is a direct call to mpz_perfect_power_p. Looks like a bug in gmp to me. That's really bad. 

```
sage: len([a for a in srange(100) if not (-a^3).is_perfect_power()])
24
```

Experiment shows that it gives the wrong answer for `-a^3` whenever a is not square-free.


---

Comment by mabshoff created at 2008-12-23 00:10:51

I did ping the eMPIRe list - see http://groups.google.com/group/mpir-devel/t/dc3682208383afc7

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-04 01:28:38

The upcoming eMPIRe will fix the issue that we are currently seeing in gmp:

```
sage: len([a for a in srange(10**6) if not (-a^3).is_perfect_power()]) 
0 
```

This is mpir-svn1523 and we are planning to switch in Sage 3.4, so this will happen around SD12.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-04 02:35:12

Note that with the old gmp as well as the new eMPIRe this operation leaks like a sieve:

```
sage: get_memory_usage()
798.4765625
sage: time len([a for a in srange(10**6) if not (-a^3).is_perfect_power()])
CPU times: user 2.84 s, sys: 0.27 s, total: 3.12 s
Wall time: 3.12 s
241224
sage: get_memory_usage()
868.921875
```


I have made this #4935 since it is seemingly unrelated to the correctness issue.

Cheers,

Michael


---

Comment by craigcitro created at 2009-01-11 08:30:05

Alright, I've coded up a new version of the above patch that we should use until we merge either a new GMP or eMPIRe with the fix included. This patch works around the GMP bug for both integers and rationals.

Assuming that this gets a positive review, I'll open another ticket to say "remove ugly workaround" once we merge a new arithmetic package with a fix.

(Credit also goes to Rob Bradshaw for code, and John Cremona for refereeing.)


---

Comment by craigcitro created at 2009-01-11 08:30:05

Changing assignee from somebody to craigcitro.


---

Comment by craigcitro created at 2009-01-11 08:30:05

Changing status from new to assigned.


---

Attachment

Note: apply *only* `trac-4612-v2.patch`, i.e. don't apply it on top of Robert's patch.


---

Comment by cremona created at 2009-01-13 21:52:08

Patch applies cleanly to 3.2.3, code looks good, tests pass.  Pass!


---

Comment by mabshoff created at 2009-01-13 21:54:53

Replying to [comment:17 cremona]:
> Patch applies cleanly to 3.2.3, code looks good, tests pass.  Pass!

We are switching to eMPIRe in 3.3.alpha0, so I am not sure how much of the workaround in this patch ought to be removed. It might be a good idea to rebase this patch for 3.3.alpha0 and hold on for now.

Cheers,

Michael


---

Comment by craigcitro created at 2009-01-13 22:17:31

Ah, I wrote this before I knew eMRIPe was so close. I agree, once it's merged, I'll make a new patch with that alpha or rc.


---

Comment by cremona created at 2009-01-13 22:45:42

Fair enough.  I just hope that the empire versions pass these doctests....


---

Comment by mabshoff created at 2009-01-18 14:13:52

Replying to [comment:19 craigcitro]:
> Ah, I wrote this before I knew eMRIPe was so close. I agree, once it's merged, I'll make a new patch with that alpha or rc.

This is going in as is for now even though eMPIRe will be in 3.3.alpha0. I will open a followup ticket to deal with using the eMPIRe function directly again, but since this adds doctests it will be merged.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-18 14:45:15

Merged trac-4612-v2.patch in Sage 3.3.alpha0


---

Comment by mabshoff created at 2009-01-18 14:45:15

Resolution: fixed
