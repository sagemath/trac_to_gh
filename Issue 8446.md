# Issue 8446: avoid 0^0 in Selmer groups of number fields

Issue created by migration from https://trac.sagemath.org/ticket/8446

Original creator: rlm

Original creation time: 2010-03-05 16:28:40

Assignee: davidloeffler

CC:  cremona

In the case of a trivial number field, such as

```
K.<a> = NumberField(polygen(QQ))
```

the Selmer group function doesn't work, since the generator `a` of the number field is 0, and when we're constructing polynomials we use the form `coeff*a**i`. However, if `i==0`, we get an `ArithmeticError` since Sage does not have conventions for `0^0`.


---

Comment by rlm created at 2010-03-05 16:30:27

Changing status from new to needs_review.


---

Attachment


---

Attachment

apply over previous patch


---

Comment by davidloeffler created at 2010-04-20 09:39:38

Looks fine, and all doctests pass. FWIW, I think that there should be a doctest in `_S_class_group_and_units`, not just in `selmer_group`, as that's where the problem actually occurs; and the docstring for `selmer_group` contains the literal string `\t` so it should be a raw string. Hence the tiny second patch. I'm giving this a positive review modulo that, so please set it to positive review if you're happy with the second patch. 

BTW, I tried using this for some some relative extensions and discovered two separate new bugs in the process, #8721 and #8722. Neither of these actually has anything to do with this patch as such, it's preexisting brokenness. I know what's causing #8722; I'll upload a patch shortly -- any chance you could review it for me?


---

Comment by rlm created at 2010-04-20 21:51:26

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-04-20 21:52:34

Re #8722 - I will be happy to review it eventually, but no guarantees at this very moment, since I'm finishing up my dissertation and preparing to defend it next month.


---

Comment by davidloeffler created at 2010-04-20 22:11:25

Understood -- hope it goes well!


---

Comment by jhpalmieri created at 2010-04-23 17:10:33

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-23 17:10:33

Merged into 4.4.alpha2:
 - trac_8446.patch
 - trac_8446_microfix.patch
