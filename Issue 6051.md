# Issue 6051: [with patch, needs some work] Enable Singular's coefficient rings which are not fields

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2009-05-17 01:05:00

Assignee: malb

Singular 3-1-0 supports coefficient rings which are not fields. In particular, it supports ZZ and ZZ/nZZ now. We should support those natively too.



---

Comment by malb created at 2009-05-17 01:05:41

almost works


---

Attachment

The attached patch enables the Singular coefficient rings natively. It passes doctests except: 

```
The following tests failed:

        sage -t  devel/sage/sage/rings/polynomial/toy_d_basis.py # 1 doctests failed
----------------------------------------------------------------------
Total time for all tests: 1049.8 seconds
```

which I reported upstream at 

  http://www.singular.uni-kl.de:8002/trac/ticket/137


---

Comment by kedlaya created at 2009-06-02 16:40:24

I applied this against 4.0 patched by #6034, and it works great. I don't find any other doctest failures.


---

Comment by malb created at 2009-06-03 22:37:02

FYI I pinged upstream again about this blocker.


---

Comment by ncalexan created at 2009-06-10 05:17:34

Against 4.0.1:


```
ncalexan`@`sage:~/releases/sage-4.0.2.alpha0/devel/sage-main/sage$ sage -hg import ~/releases/trac_6051-singular-3_1_0-rings.patch 
applying /home/ncalexan/releases/trac_6051-singular-3_1_0-rings.patch
patching file doc/en/reference/polynomial_rings.rst
Hunk #2 FAILED at 13
1 out of 2 hunks FAILED -- saving rejects to file doc/en/reference/polynomial_rings.rst.rej
patching file sage/rings/polynomial/multi_polynomial_ideal.py
Hunk #14 FAILED at 353
Hunk #52 FAILED at 2195
Hunk #53 FAILED at 2219
Hunk #54 FAILED at 2263
Hunk #55 FAILED at 2271
Hunk #57 FAILED at 2381
6 out of 63 hunks FAILED -- saving rejects to file sage/rings/polynomial/multi_polynomial_ideal.py.rej
patching file sage/rings/polynomial/multi_polynomial_libsingular.pyx
Hunk #16 succeeded at 529 with fuzz 1 (offset 0 lines).
Hunk #17 FAILED at 550
Hunk #87 succeeded at 2650 with fuzz 1 (offset 21 lines).
Hunk #90 succeeded at 2711 with fuzz 1 (offset 23 lines).
1 out of 176 hunks FAILED -- saving rejects to file sage/rings/polynomial/multi_polynomial_libsingular.pyx.rej
abort: patch failed to apply
```



---

Comment by malb created at 2009-06-10 08:40:51

Upstream fixed the issue in:

   ftp://www.mathematik.uni-kl.de/pub/Math/Singular/src/3-1-0/Singular-3-1-0-4.tar.gz


---

Comment by ncalexan created at 2009-06-10 21:20:58

Replying to [comment:5 malb]:
> Upstream fixed the issue in:
> 
>    ftp://www.mathematik.uni-kl.de/pub/Math/Singular/src/3-1-0/Singular-3-1-0-4.tar.gz

I'm release manager for this.  I should update your spkg with this new tree?  Will you do that for me?


---

Comment by malb created at 2009-06-10 22:46:56

> I'm release manager for this.  I should update your spkg with this new tree?  Will you do that for me?

Nick, you don't have to update the SPKG just because you are release manager. In any case, I'll see if I can update it soon-ish.


---

Attachment

I rebased the patch against 4.0.1 (really what will be 4.0.2.alpha0) and it works up to that one failing doctest.  I'd really like to merge this and #6034 for 4.0.2 so if the spkg itself isn't updated to the even newer singular, let's remove the failing doctest.


---

Comment by malb created at 2009-06-11 13:31:01

There are some issue with the new upstream release (computations timing out), which I haven't tracked down yet. I am a bit short on time so I'd suggest not to include this patch in 4.0.2 or to follow the strategy Nick proposed above: just remove the doctest failure.


---

Comment by ncalexan created at 2009-06-12 08:02:22

Resolution: fixed


---

Comment by ncalexan created at 2009-06-12 08:02:22

Docstring #random-ed, follow up ticket at #6265.


---

Comment by mvngu created at 2009-06-12 14:19:50

Is this really merged in 4.0.2.alpha1? Do you mean 4.0.2.alpha0?


---

Comment by ncalexan created at 2009-06-14 21:18:22

This is confusing, and the first part (multivariate rings) behave differently on 32 and 64 bit machines.  Any thoughts, Martin?


```
sage: P.<x,y,z> = Integers(2^32)[]
sage: P(2^32-1)
-1
sage: P.<x> = Integers(2^32)[]
sage: P(2^32-1)
4294967295
```



---

Comment by malb created at 2009-06-15 10:41:32

This looks like an upstream bug to me. I reported it at


  http://www.singular.uni-kl.de:8002/trac/ticket/138

I will provide a workaround and attach it to this ticket.


---

Attachment

The attached patch fixes the issue on sage.math for me.
