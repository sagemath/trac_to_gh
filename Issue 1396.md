# Issue 1396: Ideal.groebner_basis should accept keyword arguments for strategy parameters

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2007-12-04 15:39:11

Assignee: malb

e.g. Singular supports `redTail` and such. We should provide a somewhat unified interface for those (probably modelled after whatever Singular provides).


---

Comment by malb created at 2008-09-20 15:49:52

Changing status from new to assigned.


---

Comment by malb created at 2009-01-23 02:47:10

Changing assignee from malb to john_perry.


---

Comment by malb created at 2009-01-23 02:47:10

Changing status from assigned to new.


---

Comment by john_perry created at 2009-01-23 09:00:26

Replying to [ticket:1396 malb]:
> e.g. Singular supports `redTail` and such. We should provide a somewhat unified interface for those (probably modelled after whatever Singular provides).

I have a version of this going now, with the behavior similar to what the ticket requests. However, would it be more desirable to allow the user's options to persist through several operations, using an interface such as (say)

* `I.set_singular_option("lazy"); I.groebner_basis()`

rather than add arguments only to the Groebner basis command, such as

* `I.groebner_basis(lazy=True)`


---

Comment by malb created at 2009-01-23 09:06:52

Replying to [comment:3 john_perry]:
> I.set_singular_option("lazy"); I.groebner_basis()

That stuff somewhat works already:


```
sage: singular.option('lazy')
sage: singular.option()
//options: lazy redefine loadLib usage prompt
```


The point of this ticket is that the user can be ignorant of the fact that (s)he is running Singular in the background and can specify options for a particular GB computation.


---

Comment by john_perry created at 2009-01-24 02:20:55

[with patch, needs work] Adds options to groebner_basis for lazy, redTail, redSB, and notSugar -- currently implemented for Singular only


---

Attachment


---

Comment by john_perry created at 2009-01-24 03:00:59

Changing status from new to assigned.


---

Comment by john_perry created at 2009-01-24 03:04:29

Changing assignee from john_perry to malb.


---

Comment by john_perry created at 2009-01-24 03:04:29

Changing status from assigned to new.


---

Comment by SimonKing created at 2010-07-15 20:12:35

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2010-07-15 20:12:35

Changing keywords from "" to "libSingular options".


---

Comment by SimonKing created at 2010-07-15 20:12:35

This patch extends Martin's work on libSingular options. Now, the options `degBound` and `multBound` can be used. A decorator, applied to all relevant methods, ensures that standard options are used unless explicitly requested by setting named arguments -- even if outside the methods other options are set.

The options can be named in Python style (deg_bound) or in Singular style (`degBound`), at the user's choice.

Examples:

1. Degree bound


```
sage: R.<x,y> = QQ[]
sage: I = R*[x^3+y^2,x^2*y+1]
sage: from sage.libs.singular.option import opt
# Use prot and deg_bound
sage: I.groebner_basis(prot=True, deg_bound=2)
std in (0),(x,y),(dp(2),C)
[4294967295:2]3ss
(S:1)-
product criterion:0 chain criterion:0
[x^3 + y^2, x^2*y + 1]

# Set prot and degBound outside the method
sage: opt['prot'] = True
# Singular style name
sage: opt['degBound'] = 2
# ... but inside the method, standard options are used:
sage: I.groebner_basis()
[x^3 + y^2, x^2*y + 1, y^3 - x]
sage: opt['prot']
True
# Python style name
sage: opt['deg_bound']
2

# similarly in Singular, rather than libSingular
sage: I.groebner_basis(algorithm='singular',deg_bound=2)
[x^3 + y^2, x^2*y + 1]
sage: singular.eval('degBound=2')
'degBound=2;'
sage: I.groebner_basis(algorithm='singular')
[x^3 + y^2, x^2*y + 1, y^3 - x]
sage: singular.eval('degBound')
'2'
```


2. Multiplicity bound


```
sage: Rlocal.<x,y,z> = PolynomialRing(QQ, order='ds')
sage: J = [x^7+y^7+z^6,x^6+y^8+z^7,x^7+y^5+z^8, x^2*y^3+y^2*z^3+x^3*z^2,x^3*y^2+y^3*z^2+x^2*z^3]*Rlocal
# prot:
sage: J.groebner_basis(prot=True)
std in basering
[1048575:2]5(4)s(3)s6s7s8s(4)s(5)sH(13)9(3)sH(12)8(4)s(5).s.s9....sH(11)8.10
(S:10)-----------
product criterion:9 chain criterion:30
[x^3*y^2 + y^3*z^2 + x^2*z^3, x^2*y^3 + x^3*z^2 + y^2*z^3, y^5, x^6, x^4*z^2 - y^4*z^2 - x^2*y*z^3 + x*y^2*z^3, z^6, y^4*z^3 - y^3*z^4 - x^2*z^5, x^3*y*z^4 - x^2*y^2*z^4 + x*y^3*z^4, x^3*z^5, x^2*y*z^5 + y^3*z^5, x*y^3*z^5]
# bounding the multiplicity
sage: J.groebner_basis(prot=True,mult_bound=100)
std in basering
[1048575:2]5(4)s(3)s6s7s8s(4)s(5)sH(13)
(S:5)------
product criterion:7 chain criterion:7
[x^3*y^2 + y^3*z^2 + x^2*z^3, x^2*y^3 + x^3*z^2 + y^2*z^3, y^5, x^6 + x*y^4*z^5, x^4*z^2 - y^4*z^2 - x^2*y*z^3 + x*y^2*z^3, z^6 - x*y^4*z^4 - x^3*y*z^5]

# Set the multBound in Singular
sage: singular.eval('multBound=100')
'multBound=100;'
# ... nevertheless, the default multBound=0 is used:
sage: J.groebner_basis(algorithm='singular')
[x^3*y^2 + y^3*z^2 + x^2*z^3, x^2*y^3 + x^3*z^2 + y^2*z^3, y^5, x^6, x^4*z^2 - y^4*z^2 - x^2*y*z^3 + x*y^2*z^3, z^6, y^4*z^3 - y^3*z^4 - x^2*z^5, x^3*y*z^4 - x^2*y^2*z^4 + x*y^3*z^4, x^3*z^5, x^2*y*z^5 + y^3*z^5, x*y^3*z^5]
sage: singular.eval('multBound')
'100'
# ... unless requested otherwise
sage: J.groebner_basis(algorithm='singular',mult_bound=100)
[x^3*y^2 + y^3*z^2 + x^2*z^3, x^2*y^3 + x^3*z^2 + y^2*z^3, y^5, x^6 + x*y^4*z^5, x^4*z^2 - y^4*z^2 - x^2*y*z^3 + x*y^2*z^3, z^6 - x*y^4*z^4 - x^3*y*z^5]
```


I just verified that `sage -testall` passes. So, ready for review!

One remark: It turned out to be impossible to doctest `libSingular's` protocol output. I inserted examples with protocol in the documentation, for illustration, but don't test these. Of course, deg_bound and mult_bound is doctested.


---

Attachment

Replaces the first patch. Full support for all Singular options in both Singular and libSingular


---

Comment by malb created at 2010-07-15 21:26:37

Changing status from needs_review to positive_review.


---

Comment by malb created at 2010-07-15 21:26:37

The patch looks good, is well documented, applies cleanly, doctests pass. My referee patch adds one whitespace character thus I feel I can give it a positive review.


---

Comment by mpatel created at 2010-07-21 01:17:40

Applying [attachment:trac1396-singular_options.patch] to a long queue of other patches I've put together for 4.5.2.alpha0, I get

```
$ hg qpush
applying trac1396-singular_options.patch
patching file sage/libs/singular/singular-cdefs.pxi
Hunk #2 FAILED at 993
1 out of 3 hunks FAILED -- saving rejects to file sage/libs/singular/singular-cdefs.pxi.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac1396-singular_options.patch
```

Earlier tickets in the queue include #6922 and #9499.  Since `sage/libs/singular/singular-cdefs.pxi.rej` contains just

```diff
--- singular-cdefs.pxi
+++ singular-cdefs.pxi
`@``@` -995,8 +994,6 `@``@`
     poly *prCopyR_NoSort(poly *p, ring *r, ring *dest_r)
     poly *prCopyR(poly *p, ring *r, ring *dest_r)
 
-
-
     cdef int LANG_TOP
 
 cdef extern from "stairc.h":
```

I'll ignore the rejects, refresh the patch, and attach the refreshed patch here.  Please let me know if this is a problem.


---

Attachment

Rebased for 4.5.2.alpha0 queue.  See comment 9.  Replaces all previous patches.


---

Comment by mpatel created at 2010-07-21 01:46:37

Resolution: fixed


---

Comment by mpatel created at 2010-07-24 00:18:46

This ticket _might_ be the source of an "Unhandled SIGSEGV" on t2.  Please see #9583, a blocker for Sage 4.5.2.


---

Comment by mpatel created at 2010-07-24 00:21:24

Perhaps I didn't rebase the patch properly?


---

Comment by ddrake created at 2010-07-26 07:54:12

Replying to [comment:11 mpatel]:
> This ticket _might_ be the source of an "Unhandled SIGSEGV" on t2.  Please see #9583, a blocker for Sage 4.5.2.

Backing out the patch does allow Sage to start on t2.math, so for 4.5.2, I'm going to yank this patch, and open another ticket; this patch can go back in, along with the necessary spkg, in the next release. Sorry.

We don't have an "unmerged in:" field, but this patch is getting "unmerged" in 4.5.2.alpha1.


---

Comment by ddrake created at 2010-07-26 08:15:01

The new ticket is #9599.


---

Comment by drkirkby created at 2010-08-02 16:21:12

Replying to [comment:13 ddrake]:
> Replying to [comment:11 mpatel]:
> > This ticket _might_ be the source of an "Unhandled SIGSEGV" on t2.  Please see #9583, a blocker for Sage 4.5.2.
> 
> Backing out the patch does allow Sage to start on t2.math, so for 4.5.2, I'm going to yank this patch, and open another ticket; this patch can go back in, along with the necessary spkg, in the next release. Sorry.
> 
> We don't have an "unmerged in:" field, but this patch is getting "unmerged" in 4.5.2.alpha1.

Should it not be set back to "needs work" then? That seems the most accurate description of the status - more accurate so than "fixed". 

Dave


---

Comment by jhpalmieri created at 2010-08-03 23:57:39

> Should it not be set back to "needs work" then? That seems the most accurate description of the status - more accurate so than "fixed".

I think we should just change focus to #9599, the new ticket for re-merging this patch.


---

Comment by jdemeyer created at 2011-01-23 20:28:04

Resolution changed from fixed to duplicate
