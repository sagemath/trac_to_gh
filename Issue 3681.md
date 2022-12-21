# Issue 3681: modulus() randomly broken for gf2e fields

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-07-19 14:03:56

Assignee: tbd


```
wdj`@`hera:~/sagefiles/sage-3.0.4.rc0$ ./sage -t  devel/sage/sage/rings/finite_field_ntl_gf2e.pyx
sage -t  devel/sage/sage/rings/finite_field_ntl_gf2e.pyx    **********************************************************************
File "/home/wdj/sagefiles/sage-3.0.4.rc0/tmp/finite_field_ntl_gf2e.py", line 170:
    sage: k.modulus()
Expected:
    x^17 + x^16 + x^15 + x^10 + x^8 + x^6 + x^4 + x^3 + x^2 + x + 1
Got:
    x^17
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_2
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/wdj/sagefiles/sage-3.0.4.rc0/tmp/.doctest_finite_field_ntl_gf2e.py
         [2.9 s]
exit code: 1024

----------------------------------------------------------------------
The following tests failed:


        sage -t  devel/sage/sage/rings/finite_field_ntl_gf2e.pyx
Total time for all tests: 2.9 seconds
```



---

Comment by was created at 2008-07-20 13:54:17

Hi,

The attached two patches make the bug stop, though I'm not completely happy.  Here's what happens.

Patch 1: This is a patch for a completely different bug that I noticed -- namely that the finite field is cached even if modulus='random', which is very stupid:

```
sage: k.<a> = GF(2^17,modulus='random')
sage: k.modulus()
x^17 + x^16 + x^15 + x^14 + x^13 + x^12 + x^11 + x^8 + x^6 + x^4 + x^2 + x + 1
sage: n.<a> = GF(2^17,modulus='random')
sage: n.modulus()
x^17 + x^16 + x^15 + x^14 + x^13 + x^12 + x^11 + x^8 + x^6 + x^4 + x^2 + x + 1
sage: n is k
True
```


Much to my surprise fixing the above caching bug -- i.e., not doing caching, makes
the bug that is the subject of this ticket just go away.  Weird!!!

Patch 2: Looking at the code in finite_field_ntl_gf2e.pyx I saw that GF2X_construct
is used inconsistently.  It is used on ntl_m but *not* on ntl_tmp.  So one or the
other is wrong.  Digging deeper it seems that using GF2X_construct on ntl_m is
totally wrong, since it is only supposed to be used on pointers that are allocated
using malloc/new not on C++ classes that are created by just declaring them.  So patch
2 gets rid of this use of GF2X_construct.   I think this call to GF2X_construct would
possibly have been a small memory leak (mabshoff?). 

NOTE: Applying *only* patch 2 does not fix the bug.  Only patch 1 makes the bug stop happening.

Thus I do not understand the bug.  It must somehow be triggered by Python weakrefs and caching
in a very unusual situation that we just happen to hit with this doctest.    Another remark is
that putting 

```
print ""
```

in the source code of finite_field_ntl_gf2e.pyx right before the random modulus is computed also causes the bug to stop happening.  

William


---

Attachment


---

Comment by mabshoff created at 2008-07-21 08:07:14

Nitpicks:

 * There is a spelling error in sage/rings/finite_field_ntl_gf2e.pyx: "# called at least once before any arithmetic is perfored. "
 * Could we add a doctest (maybe a long one) that verifies that the modulus is really irreducible for some number of fields, i.e. a couple dozen or a hundred?

Other than that I think the patch is good to go.

Cheers,

Michael


---

Comment by cremona created at 2008-07-21 14:24:22

I cannot say that I understand any better, but I'll certainly give the first patch a +1 too.


---

Attachment

patch attached that addresses mabshoff's nitpicks.


---

Comment by cremona created at 2008-07-21 16:57:55

I was puzzled by these lines in finite_field_ntl_gf2e.pyx:

```
            if modulus == "random":
                current_randstate().set_seed_ntl(False)
                GF2X_BuildSparseIrred(ntl_tmp, k)
                GF2X_BuildRandomIrred(ntl_m, ntl_tmp)
```

From looking at NTL's functions, it looks as if we are creating two irreducibles here, one sparse and one random.  Also, the sparse creation function is *not* random for degrees up to 2048 since it just uses a lookup table.

The solution is that `GF2X_BuildRandomIrred` takes as input some monic poly, and (by changing some coefficients at random, I think) changes it into another one which has the same degree and passes the irreducibility test.  So I guess that is random, but it seems a bit of overkill to call the first function (especially for degrees >2048) rather than start with `X^k`, say.


---

Comment by was created at 2008-07-21 17:19:51

John,

I read the ntl source code and what you remark about is true.  Note however that even for k >> 2048 the constructor is very fast and returns a very *non* random poly.  That's why the two calls above are right and do make sense.   It's intriguing but evidently the ntl algorithm to generate a random polynomial is to chose a *random* element of GF(2^k) then compute its minpoly, and return that if it has the right degree.  This might address some issue of distribution.


---

Comment by cremona created at 2008-07-21 17:24:47

That's a clever way of doing it, certainly (OK, so Victor Shoup is clever) -- e.g. if the degree is prime then (almost) any element will do.  I wonder how sparse a random min poly is.

In the old Sage code, before I fixed it,  it was generating random polys over GF(2) and testing them for irreducibility.  This was bad on two counts:  (a) it took many tries before an irreducible was hit; (b) the polys used had 50% of their coefficients =1, so were slow to deal with (and the field arithmetic was also then slow).

I cannot actually think of a situation where I would want to have a random generator...

By the way, do we need any more reviewing before this one gets the go-ahead?


---

Comment by mabshoff created at 2008-07-21 17:28:40

Replying to [comment:7 cremona]:
> That's a clever way of doing it, certainly (OK, so Victor Shoup is clever) -- e.g. if the degree is prime then (almost) any element will do.  I wonder how sparse a random min poly is.

I am sure Victor should "ain't no dummy" :)

> In the old Sage code, before I fixed it,  it was generating random polys over GF(2) and testing them for irreducibility.  This was bad on two counts:  (a) it took many tries before an irreducible was hit; (b) the polys used had 50% of their coefficients =1, so were slow to deal with (and the field arithmetic was also then slow).
> 
> I cannot actually think of a situation where I would want to have a random generator...
> 
> By the way, do we need any more reviewing before this one gets the go-ahead?

No, I consider what you and William wrote a positive review. This has been a Heisenbug and it has been fixed by the patch on the box we did hit the problem on. Should it resurface we will deal with it.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-21 17:54:02

Resolution: fixed


---

Comment by mabshoff created at 2008-07-21 17:54:02

Merged in Sage 3.0.6.rc0
