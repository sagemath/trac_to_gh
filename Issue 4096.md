# Issue 4096: pari precision interface

Issue created by migration from https://trac.sagemath.org/ticket/4096

Original creator: cremona

Original creation time: 2008-09-10 08:44:01

Assignee: cremona

CC:  alexghitza

This is a follow-up from 4064.  Alex Ghitza and I are doing a big job sorting out the interface with the pari library with respect to (real and complex) precision, where there is currently confusion leading to weird results when word-precision, bit-precision and decimal precision are being confused.


---

Comment by cremona created at 2008-09-11 20:31:05

The story so far:  these apply in succession to 3.1.2.rc2:

    * Patch 1 (John) [originally called 4064-ell_pari_precision-2.patch]
    * Patch 2 (Alex) [..........................................3......]
    * Patch 3 (John) Adjusted previous for 64-bit
    * Patch 4 (John) ... and readjusted for 32-bit

The number of places where we need separate doctest results for 32- and 64-bit is very reduced but not entirely.  The main work remaining is to sort out the constructor pari(K) where K is a number field.  I thought I had sorted out pari(E) to be identical for 32 and 64 but it is not quite there yet (for E an elliptic curve).

There is no reason for the patch names to ahve ell_ in them, this is absolutely not just about elliptic curves!


---

Comment by AlexGhitza created at 2008-09-15 08:30:48

There is a new patch 4096-pari_real_precision.patch which replaces the previous ones, is based on 3.1.2.rc3, and adds more stuff.  Still not quite ready for review, but we're getting there.


---

Comment by cremona created at 2008-09-18 22:17:49

The following should be applied to 3.1.2:

4096-pari_real_precision.patch  [Alex]
4096-pari_real_precision64.patch [John after 64-bit testing]
4096-matrix_real_pari64.patch [Alex PLUS some extra 64-bit stuff from John]
4096-pari_real_precision32.patch [tiny extra from John in number_field]

All tests pass.


---

Comment by AlexGhitza created at 2008-09-19 08:28:19

I've added another tiny patch which removes unnecessarily complicated code from converting to Pari in polynomial_element.pyx.


---

Comment by AlexGhitza created at 2008-09-19 23:36:12

doc patch, apply to 3.1.2


---

Attachment

John and I agree that it is time for this to be reviewed.

To make this easier, I have put everything into one patch 4096-pari_real_precision_all.patch, which applies to 3.1.2.  There is also a small doc patch 4096-doc_const.patch which fixes a related issue in const.tex, and also applies to 3.1.2.

Note to the reviewer: it would be best to start by scrolling down in the main patch until you hit the top of gen.pyx; there we have inserted a doc section called "Guide to real precision and the Pari library", which documents the correct behavior which is implemented by the patch.


---

Comment by mabshoff created at 2008-09-25 00:30:34

Hmm, I don't like the following change:

```
178	 	        s = str(self) 
179	428	        import sage.libs.pari.gen_py 
180	 	        return sage.libs.pari.gen_py.pari, (s,) 
 	429	        return sage.libs.pari.gen_py.pari, (str(self),) 
```

I am not 100% certain, but if s were a C type object the above would cause a leak. I have fixed similar issues over and over again in code all over Sage and I suspect that the reference count for "return str(foo)" might be broken somehow. I have zero prove of this, obviously, but I intent to dig deep one day.

Cheers,

Michael


---

Comment by AlexGhitza created at 2008-09-25 10:57:34

Michael,

I will rebase the patch against 3.1.3.alpha1 very soon and fix the issue that you're pointing out.

Alex


---

Comment by cremona created at 2008-09-25 11:08:15

Replying to [comment:7 AlexGhitza]:
> Michael,
> 
> I will rebase the patch against 3.1.3.alpha1 very soon and fix the issue that you're pointing out.
> 
> Alex

It was fine with alpha0.  Thanks, Alex.


---

Attachment

apply to 3.1.3.alpha1


---

Comment by AlexGhitza created at 2008-09-25 13:31:42

there were a couple of rejects against 3.1.3.alpha1, so i replaced the patch with a rebased one


---

Comment by cremona created at 2008-09-25 15:52:05

Replying to [comment:9 AlexGhitza]:
> there were a couple of rejects against 3.1.3.alpha1, so i replaced the patch with a rebased one

NB the doc/const patch still needs to be applied separately.


---

Comment by mabshoff created at 2008-09-26 03:05:25

4096-pari_real_precision_all.patch is bruising faster than a Georgia peach falling from a tree. I rebased it again against my current 3.1.3.alpha2 treee in two places (one whitespace, the other a printing issue in mpfr_real.pyx) and will attach it shortly. I am testing it right now and am inclined to just merge it since both John and Alex spend considerable time on this. If this patch causes problem you can blame me, but at least that way it is in :). If Craig gets around to review this before 3.1.3.final it would be great it he put patches on top of what I am about to post.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-26 04:03:12

This is the patch that was actually merged in 3.1.3.a2. It is slightly rebased against the previous patch


---

Attachment

I read over the patch and it looks good to me. I am certainly no expert, so this positive review should be taken with a grain of salt. Since the patch did bitrot twice and was written by two experts I merged it into 3.1.3.alpha2. Should anything come up during subsequent review please open a new ticket so we can deal with that problem. The situation with the patch is certainly much improved over the old situation, so I consider this a worthy tradeoff. This patch also fixes #4199 and all doctests pass which is the main reason I merged it.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-26 04:07:01

Resolution: fixed


---

Comment by mabshoff created at 2008-09-26 04:07:01

Merged in Sage 3.1.3.alpha2
