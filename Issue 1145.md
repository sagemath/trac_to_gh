# Issue 1145: high-level strategy for integer factorization

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2007-11-11 13:26:17

Assignee: was

CC:  jdemeyer jpflori

I propose the following strategy for factor(integer):

1) do trial division by all primes up to say 1000. This can be done efficiently by a single
   gcd with the product of all those primes.
2) use GMP-ECM, starting from say B1=100, and increasing B1 by sqrt(B1) at each step, until
   one reaches the _recommended_B1_list value which corresponds to 1/3 of the size of the
   number to be factored. Thus for a 90-digit input, one will stop at B1=250000.
3) try GMP-ECM P-1 and P+1 with respectively 9*B1 and 3*B1 where B1 is the last value tried
   for ECM. The corresponding cost of those runs will be approximately the same as the last
   ECM curve, thus this will not slow down the average computation, and might find a few factors.
4) run MPQS or GNFS. You might want to issue a warning to the user (if called from toplevel) at
   that time.


---

Comment by was created at 2007-11-12 12:24:53

Comments from some experts:

```

On 12/11/2007, Robert Bradshaw <robertwb`@`math.washington.edu> wrote:
> I don't have much expertise in the area, but it looks like a sound
> proposal to me. The trial division bound seems a bit low (and perhaps
> should be adjusted for the size of the input). Is this similar to
> what Pari does? Would it make sense to parallelize ECM/QS by default
> on a multi-core system?
>
> - Robert
>
Bill Hart <goodwillhart`@`googlemail.com>
	
	
This proposal is absolutely correct. It is *exactly* what I would do,
with one exception. I would not issue a warning that MPQS is going to
start, unless the factorisation is over say 70 digits (~90s).

Bill.
```



---

Comment by wbhart created at 2007-11-12 14:05:02

I've just discussed this with Paul Zimmerman and here is what we should do (eventually):

1) Trial factoring for primes up to ~1000
2) SQUFOF for numbers up to ~32-40 bits (use the fast implementation in FLINT - it's 4x faster than anything else)
3) Pollard Rho if we have an efficient implementation
4) tinyQS in FLINT *if* the number of digits is small enough, i.e. if that is going to be faster than GMP-ECM (we have to profile this to determine the cutoff)
5) GMP-ECM with bound up to n^(1/3)
6) p-1 and p+1 with large bound (it works rarely, but saves MPQS if it happens to work - the runtime compared to MPQS is *tiny*)
7) MPQS up to ~90 digits if large prime variant, ~100 digits if double large prime variant or ~130 digits if triple large prime variant QS
8) GNFS 
9) You are the NSA, so you know what to do.


---

Comment by zimmerma created at 2007-12-17 12:18:33

Steps 2) and 3) of my original proposal might be easily implemented using the "finer ECM interface" proposed in #1421.


---

Comment by davidloeffler created at 2009-07-20 19:58:27

Changing assignee from was to tbd.


---

Comment by davidloeffler created at 2009-07-20 19:58:27

Changing component from number theory to factorization.


---

Comment by zimmerma created at 2010-02-05 20:44:31

Resolution: wontfix


---

Comment by zimmerma created at 2010-02-05 20:44:31

since no progress was done in 2 years, I close that ticket.


---

Comment by mvngu created at 2010-02-05 21:15:05

Make sure you understand the procedure for closing tickets. See [this section](http://www.sagemath.org/doc/developer/trac.html#closing-tickets) of the Developer's Guide for more information.


---

Comment by robertwb created at 2010-02-05 21:53:13

Changing status from closed to new.


---

Comment by robertwb created at 2010-02-05 21:53:13

This is still an issue--I have code that I need to clean up and post here (though probably won't get around to it 'till this summer).


---

Comment by robertwb created at 2010-02-05 21:53:13

Resolution changed from wontfix to 


---

Comment by zimmerma created at 2010-02-07 21:18:02

> Make sure you understand the procedure for closing tickets. 

sorry, I wasn't aware of that.


---

Comment by aapitzsch created at 2010-11-17 16:19:45

Changing assignee from tbd to aapitzsch.


---

Comment by aapitzsch created at 2010-11-19 15:18:02

Changing status from new to needs_review.


---

Attachment

Apply first: #5945, #5310

Patch makes use of SQUFOF, ecmfactor, cunningham_table and sympy.factorint.

To pass all tests cunningham database should become a standard package or the warning in cunningham_tables.py should be removed.

To evalutate run attachment:evaluate_1145.sage

This should also fix #9463.


---

Comment by jdemeyer created at 2010-11-19 22:09:12

I have personally been considering moving all the integer factorisation code to a new module.  I think it makes sense because a lot of new code is being added and `sage/rings/integer.pyx` is already large enough.

What do you think?


---

Comment by robertwb created at 2010-11-19 23:45:10

+1 to moving all the code to a new factor module. I've just very briefly looked at your code. Also, in terms of code structure, there's no need for all the functions to start with an underscore, and it's probably worth making them cpdef functions for ease of testing. (There's no overhead for module-level methods, as they can't be overridden, so the cdef portion is just as fast.) How does sympy.factorint compare to, say, pari's sieves? What about the quadratic sieve from flint?


---

Comment by aapitzsch created at 2010-11-20 09:16:59

Okay, I will move the code to a new module. How should it be called? Should it stay in `sage/rings`?

sympy.factorint becomes slow very fast but it can handle perfect powers better than other functions.

quadratic sieve from flint is currently not installed, so I couldn't use it.


---

Comment by jdemeyer created at 2010-11-20 09:20:40

Replying to [comment:16 aapitzsch]:
> Okay, I will move the code to a new module. How should it be called? Should it stay in `sage/rings`?
> 
> sympy.factorint becomes slow very fast but it can handle perfect powers better than other functions.

Personally, I wouldn't care that much about huge perfect powers.  I agree with the PARI people that this is essentially a non-issue.


---

Comment by jdemeyer created at 2010-11-20 09:23:58

Replying to [comment:16 aapitzsch]:
> Okay, I will move the code to a new module. How should it be called? Should it stay in `sage/rings`?

I would call it `sage/rings/factorint.pyx` or so.  It would be nice if you would move *all* the integer factoring code there, not only the newly added code.

I would love to help with this ticket, but I'm already involved in too many tickets...


---

Comment by aapitzsch created at 2010-11-20 09:42:35

Perfect power checking doesn't cost that much but it improves considerably the speed if it's a perfect power.


---

Comment by jdemeyer created at 2010-11-20 09:45:39

Replying to [comment:19 aapitzsch]:
> Perfect power checking doesn't cost that much but it improves considerably the speed if it's a perfect power.

Trial division doesn't cost that much but it improves considerably the speed if it has lots of small factors.

Now guess which is more likely for a random number...


---

Comment by jdemeyer created at 2010-11-20 09:47:01

Besides, if you want to check for a power, just check for a perfect power.  No need to call sympy.factorint() for that.


---

Comment by aapitzsch created at 2010-11-20 09:55:08

That's what I do.

```
if n.is_power(): 
    from sympy import factorint 
    return [(Integer(p),e) for p,e in factorint(n).items()]
```



---

Comment by jdemeyer created at 2010-11-20 10:03:23

That doesn't look good.  If `n` is a power, you should write `n` as `b^k` and then factor `b` and multiply all exponents by `k` instead of using the slower `sympy.factorint()`.


---

Comment by robertwb created at 2010-11-20 22:37:57

Replying to [comment:16 aapitzsch]:
> Okay, I will move the code to a new module. How should it be called? Should it stay in `sage/rings`?

Yes, that'd be a fine place for it. 

> sympy.factorint becomes slow very fast but it can handle perfect powers better than other functions.

Then -1 from moving away from Pari. We can check for perfect powers very quickly using gmp/mpir first. 

> quadratic sieve from flint is currently not installed, so I couldn't use it.

Well, expect some followup patches then :). 

- Robert


---

Comment by aapitzsch created at 2010-11-22 16:15:45

I moved the integer factorization code to factorint.pyx. The patch is attached to #5945 because adding _factor_using_flint_ is a minor change than this one, so review should be easier.

Currently `arith.factor` links to `factorint.factor`. We can create a ticket to get rid of it after fixing #5945. But for now it would be to much I think.


---

Comment by aapitzsch created at 2010-12-03 09:23:18

Changing status from needs_review to needs_work.


---

Attachment


---

Comment by aapitzsch created at 2010-12-07 16:09:33

I changed the things mentioned above.


---

Comment by aapitzsch created at 2010-12-07 16:09:33

Changing status from needs_work to needs_review.


---

Comment by zimmerma created at 2010-12-10 12:59:23

if somebody wants to add GNFS to the list of algorithms available from Sage,
CADO-NFS 1.0 was just released: http://cado-nfs.gforge.inria.fr/


---

Comment by robertwb created at 2010-12-17 22:23:31

Depends on #5310 and #5945

Apply trac_1145_integer_factorization.patch and trac_1145_cunningham_warning.patch


---

Attachment

Yafu (http://sourceforge.net/projects/yafu/) might be an interesting software to include,
although I have difficulties finding its license. It includes a multi-thread implementation
of SIQS, which might be interesting in the 70-100 digit range.

Paul Zimmermann


---

Comment by roed created at 2012-01-05 10:48:08

Changing status from needs_review to needs_work.


---

Comment by roed created at 2012-01-05 10:48:08

I know that it's waiting on #5310, but your patch is doubled: you exported to a file that already contained the patch.  Also, we should figure out how to merge these factoring improvements with those in #12125 and #12133; it shouldn't be too hard.

A couple other comments: you should use the `perfect_power` method of Integers rather than writing your own base_exponent, and you should pass on the `use_pollard` parameter when you recurse.


---

Comment by mstreng created at 2013-07-25 11:57:49

See also #14970
