# Issue 1014: there should be an Integer.number_of_digits() function

Issue created by migration from https://trac.sagemath.org/ticket/1014

Original creator: bober

Original creation time: 2007-10-27 23:06:26

Assignee: bober

Both `log(x,10)` and `len(str(x))` are bad ways to calculate the number of digits of an integer, but there doesn't appear to be a better way to do it right now in sage.

Probably, it would be nice if there were a number_of_digits() (or maybe there is a better name) function in `sage.rings.integer.Integer` that wraps the relevant gmp function to return the number of digits of the integer.


---

Comment by malb created at 2007-10-28 16:53:08

It should be called ndigits() just as ngens() et al.


---

Comment by dmharvey created at 2007-11-16 01:22:09

This should wrap GMP's `sizeinbase()` function. See

http://gmplib.org/manual/Miscellaneous-Integer-Functions.html#Miscellaneous-Integer-Functions


---

Comment by dmharvey created at 2007-11-16 01:24:54

Sorry, my previous comment is wrong. The sizeinbase() function only returns an exact answer if the base is a power of two. Otherwise it can return one digit too much. The problem is that determining the exact number of digits is not a linear time algorithm; I think it's probably around O(n log<sup>2</sup>(n)). I did write an `exact_log()` function at some point which might be relevant, but from memory it wasn't too efficient.


---

Comment by AlexGhitza created at 2008-01-27 07:48:07

I spent a few hours trying to come up with a smart way of doing this, and then I decided to see exactly how bad it is to do log(x,10).  The upshot is that I couldn't come up with an integer large enough that taking the log isn't practically instantaneous.  Hence the patch.

Here's an example:

```
sage: time n=100000000000000000**10000000+1
CPU times: user 53.12 s, sys: 0.52 s, total: 53.65 s
Wall time: 53.76
sage: time n.ndigits()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00
170000001
```


Note that it takes significantly longer to actually compute n than to get the number of digits.


---

Comment by cwitty created at 2008-01-27 08:04:44

If this is supposed to give the exact number of digits... it doesn't.

The algorithm correctly says that the first number has 1001 digits; but the next two numbers actually have 1000 digits and the algorithm says 1001.


```
sage: RR(10^1000).abs().log(10).floor() + 1
1001
sage: RR(10^1000 - 1).abs().log(10).floor() + 1
1001
sage: RR(10^1000 - 10^900).abs().log(10).floor() + 1
1001
```



---

Attachment

revised patch


---

Comment by AlexGhitza created at 2008-01-27 23:32:07

Carl: thanks a lot for catching this.  I love this refereeing thing!

I've put up a new patch, hopefully correct this time.

Here's the (again, simple) idea:  Since my one-liner gave the same result as GMP's sizeinbase function, I ditched my earlier try and just called sizeinbase, which gives me a number guess, which is either the correct number of digits, or 1+ that.  To figure out which one is which, we simply need to compare our integer with the integer base**(guess-1).

That's what the patch does.  I've played around with this for very large numbers and the running time seems to be dominated by computing base**(guess-1); sizeinbase and the comparison are practically instantaneous.  So ndigits() now has roughly the same running time as creating n itself (which, I would guess, is linear in the size of n).  Here are some examples:


```
sage: time n=10^1000
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00
sage: time n.ndigits()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00
1001
sage: time n=10^1000-1
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00
sage: time n.ndigits()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00
1000
sage: time n=10^1000-10^900
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00
sage: time n.ndigits()
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00
1000
sage: time n=100000000000000000^10000000-1
CPU times: user 29.66 s, sys: 0.42 s, total: 30.08 s
Wall time: 30.07
sage: time n.ndigits()
CPU times: user 29.64 s, sys: 0.40 s, total: 30.03 s
Wall time: 30.03
170000000
```



---

Comment by dmharvey created at 2008-01-27 23:42:15

This is very similar to the `Integer.exact_log` function. Can we perhaps merge the functionality here?

Also, I know nobody has time for this, but an even better algorithm would be:
 * as alex suggests, estimate the exponent using mpz_sizeinbase
 * instead of computing the whole power, just estimate the top couple of digits using MPFR (much much much faster than computing the whole power)
 * keep increasing precision until we can distinguish the input from the power.

Maybe this would be easiest to implement using interval arithmetic.

The point is, for uniform random input, the top couple of digits will almost always give you the right answer straightaway. It's very rare that you need to compute everything. I wish I had more time to think about this, it sounds like a fun problem.


---

Attachment


---

Comment by AlexGhitza created at 2008-01-29 04:25:03

Apply *only* the new patch.  It modifies exact_log and makes ndigits wrap it.  Also fixes a couple of typos.

See the discussion at
http://groups.google.com/group/sage-devel/browse_thread/thread/a17bdc227206638f


---

Comment by ncalexan created at 2008-02-15 05:13:37

Looks good, I say apply.


---

Comment by mabshoff created at 2008-02-15 05:17:39

Resolution: fixed


---

Comment by mabshoff created at 2008-02-15 05:17:39

Merged 1014-ndigits-and-exact_log.patch in Sage 2.10.2.alpha0
