# Issue 4275: [with patch, needs review] improved doctest for elliptic curves (part 2)

Issue created by migration from https://trac.sagemath.org/ticket/4275

Original creator: zimmerma

Original creation time: 2008-10-13 15:58:25

Assignee: was

CC:  cremona

This patch adds missing doctests to ell_modular_symbols.py, ell_number_field.py and
ell_padic_field.py. The conversion to Pari in ell_padic_field.py was broken, and still
fails in some cases (see example in file), but I don't know if this is a bug in Pari, or
an invalid input.

I also removed some unused functions in ell_modular_symbols.py, it would be good to check they
are not needed elsewhere.

Note that some internal functions could not be tested, thus the coverage is not 100%.

```
bash-3.00$ sage -coverage ell_modular_symbols.py ell_number_field.py ell_padic_field.py
----------------------------------------------------------------------
ell_modular_symbols.py
SCORE ell_modular_symbols.py: 100% (6 of 6)
----------------------------------------------------------------------

----------------------------------------------------------------------
ell_number_field.py
SCORE ell_number_field.py: 90% (19 of 21)

Missing documentation:
         * _proot(x, e):
         * _pquadroots (a, b, c):

----------------------------------------------------------------------

----------------------------------------------------------------------
ell_padic_field.py
SCORE ell_padic_field.py: 80% (4 of 5)

Missing documentation:
         * _frob(P):
```



---

Attachment

Paul, can you say which version (exactly) your patch should apply to?  I failed to apply it to 3.1.3.alpha3, and suspect that some of the changes I made between 3.1.2 and that one conflict with yours.  (For example, I thought I had already converted some "internal functions" to lambda functions!)  It is a habit of mine that when I work on a file I try to improve its doctest coverage at the same time, so this is not so surprising!  John


---

Comment by zimmerma created at 2008-10-13 19:40:25

John, my patch should apply to 3.1.2 (I always use the latest release).
In the meantime, I have worked on ell_point.py, I hope this will be no duplicate work,
I will submit it soon.


---

Attachment

The second patch (to be applied after the first one) adds some documentation and one test for the
Pari conversion (thanks Karim Belabas).


---

Attachment

The 3rd patch (to be applied after the first 2) re-enable two methods that were unused in
ell_modular_symbols.py, but one was used elsewhere, and the other one might be useful.


---

Attachment

Replaces the three earlier patches


---

Comment by cremona created at 2008-10-18 08:55:38

The new patch sage-trac4275.patch merges the three previous ones and rebases them on 3.1.4.  Essentially the same as Paul's 3.  I am happy with these being merged.


---

Comment by zimmerma created at 2008-10-18 09:26:40

Thanks John. A quick summary of my (unfinished) doctest work on elliptic curves:

#4271 -> merged in 3.1.3

#4275 (this one): needs review

#4277 positive review, ready to merge

#4281 needs review

#4287 needs review + fix loads/dump problem

I put you in cc to be sure you get this. Feel free to remove yourself.


---

Comment by zimmerma created at 2008-10-18 09:29:20

Sorry, one should read #4275 (this one): positive review, ready to merge instead of what I wrote
above.


---

Comment by mabshoff created at 2008-10-18 19:48:29

Merged in Sage 3.2.alpha0


---

Comment by mabshoff created at 2008-10-18 19:48:29

Resolution: fixed
