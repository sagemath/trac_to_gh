# Issue 7260: [with patch; needs review] Inverse mod number field ideals: deal with several remaining problems

Issue created by migration from Trac.

Original creator: fwclarke

Original creation time: 2009-10-21 08:54:00

Assignee: davidloeffler

CC:  mtaranes cremona

Keywords: inverse_mod

At present the function `inverse_mod` (which computes the inverse of 
elements of number fields modulo integral ideals) suffers from several 
defects.

1.  It does not work for elements of relative number fields, though it 
does for an element of the rings of integers of such a number field.

2.  The behaviour is different depending whether the element's parent is 
the number field or the maximal order.  Thus with 4.1.2:

```
sage: k.<a> = NumberField(x^3 + 11)
sage: R = k.ring_of_integers()
sage: (a + 13).inverse_mod(k.ideal(a^2))
-3*a - 5
sage: R(a + 13).inverse_mod(k.ideal(a^2))
-123*a^2 + 8*a - 104
```

This is because the field version of the function applies `small_residue` 
to the results of the computation, while the order versions do not.
Moreover

```
sage: R(a + 13).inverse_mod(k.ideal(a^2)).parent() == k
True
```

when it would make more sense if the inverse of an element of R was an 
element of R.

3.  Error messages are inconsistent.

The attached patch deals with these defects and also makes the code run a 
bit faster in some cases.  




---

Attachment


---

Comment by ylchapuy created at 2009-10-31 21:46:49

Changing status from new to needs_review.


---

Comment by cremona created at 2009-11-22 17:26:37

This looks good to me.  It applies fine to 4.3.alpha0 and all tests in rings/number_field pass.  I also tested modular/modsym since p1list_nf.py is one place where this code is used and that was fine too.


---

Comment by cremona created at 2009-11-22 17:26:37

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-29 05:12:13

Resolution: fixed
