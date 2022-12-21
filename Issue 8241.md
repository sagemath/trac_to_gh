# Issue 8241: p-adic fields should have Witt Frobenius

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2010-02-11 19:54:03

Assignee: roed

If K is an unramified extension of Qp, there should be a function that computes the canonical Witt p-Frobenius:


```
sage: K.<a> = Qp(25)
sage: a.witt_frobenius()
???
```



---

Comment by dmharvey created at 2010-02-11 19:54:29

(oops the Qp above should be Qq)


---

Comment by roed created at 2010-11-22 09:51:23

I called the function `frobenius` rather than `witt_frobenius`.


---

Comment by roed created at 2010-11-22 09:51:23

Changing status from new to needs_review.


---

Comment by roed created at 2010-12-03 13:52:52

Fixed a small problem revealed by the test-bot.


---

Comment by kedlaya created at 2011-06-17 15:43:00

For consistency, these methods should also apply to Qp, with Frobenius acting as the identity map. For instance, the following should not raise an exception:

```
sage: Qp(7)(2).frobenius()
```



---

Comment by kedlaya created at 2011-06-17 15:43:14

Changing status from needs_review to needs_work.


---

Comment by roed created at 2011-06-21 19:44:21

There's now a frobenius method for p-adic base rings and fields.


---

Comment by roed created at 2011-06-21 19:44:21

Changing status from needs_work to needs_review.


---

Comment by roed created at 2011-06-22 07:53:33

I have no idea why adding a method to Qp causes a test in sage/libs/fplll/fplll.py to fail.


---

Comment by jdemeyer created at 2011-08-24 22:02:31

Replying to [comment:7 roed]:
> I have no idea why adding a method to Qp causes a test in sage/libs/fplll/fplll.py to fail.

See #10195.


---

Comment by leif created at 2011-09-16 17:20:02

Ping. (#11586, which has positive review, depends on this one.)


---

Attachment

As Sebastian Pancratz noted in his talk, it would be great if someone wrote a better implementation of this.


---

Comment by davidloeffler created at 2012-03-10 17:25:32

The patchbot finds some Sphinx formatting errors in the docstrings:


```
docstring of sage.rings.padics.padic_ZZ_pX_CA_element.pAdicZZpXCAElement.teichmuller_list:4: WARNING: Inline interpreted text or phrase reference start-string without end-string.
docstring of sage.rings.padics.padic_ZZ_pX_CA_element:2: WARNING: Block quote ends without a blank line; unexpected unindent.
docstring of sage.rings.padics.padic_ZZ_pX_CR_element.pAdicZZpXCRElement.teichmuller_list:4: WARNING: Inline interpreted text or phrase reference start-string without end-string.
docstring of sage.rings.padics.padic_ZZ_pX_CR_element:2: WARNING: Block quote ends without a blank line; unexpected unindent.
docstring of sage.rings.padics.padic_ext_element.pAdicExtElement.frobenius:6: WARNING: Inline interpreted text or phrase reference start-string without end-string.
```


It's also harping on about trailing whitespace (which is apparently now a Bad Thing, although Sage has been tolerating it cheerfully for years).


---

Comment by davidloeffler created at 2012-03-12 18:54:04

Here's a new patch with the docstrings straightened out and trailing whitespace removed. I've also added a doctest to show that an error is raised when "frobenius" is called on an element of a ramified extension. I'm happy with the rest of the code, so if David's happy with my changes we can call this that's a positive review.


---

Comment by roed created at 2012-03-12 19:41:00

Changing status from needs_review to positive_review.


---

Comment by roed created at 2012-03-12 19:41:00

Looks good to me.  I've created #12657: write a more efficient implementation of Frobenius.


---

Attachment

Apply only this patch. Patch against 5.0.beta7


---

Comment by davidloeffler created at 2012-03-12 19:48:08

Patchbot's grumbling about trailing whitespace again, so I removed one single space character and re-uploaded the patch.


---

Comment by jdemeyer created at 2012-03-21 22:03:40

Resolution: fixed
