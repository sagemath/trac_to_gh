# Issue 3492: [with patch, needs review] listing finite field embeddings

Issue created by migration from Trac.

Original creator: fwclarke

Original creation time: 2008-06-22 22:44:09

Assignee: tbd

Keywords: finite field homomorphism

The attached patch adapts `sage/rings/number_field/morphism.py` so that the syntax for homorphisms of number fields also works for finite fields.  Thus

```
sage: End(GF(125, 'a')).list()

[
Ring endomorphism of Finite Field in a of size 5^3
  Defn: a |--> a,
Ring endomorphism of Finite Field in a of size 5^3
  Defn: a |--> 3*a^2 + 1,
Ring endomorphism of Finite Field in a of size 5^3
  Defn: a |--> 2*a^2 + 4*a + 4
]
```



---

Attachment


---

Comment by dmharvey created at 2008-06-24 01:12:37

This is a nice patch. Some issues still to address:

 * More doctests please! Still a lot of functions don't have doctests.
 * There's some irrelevant stuff that got copied from the number field case, like the "H = Hom(ZZ, QQ)" test, which should be deleted
 * I want to see doctests showing the list of embeddings from a finite field into a larger finite field
 * I want to see doctests showing that there are no embeddings when the characteristics are unequal
 * I want to see doctests showing how to *apply* the homomorphisms to elements of the domain
 * I want to see doctests covering the degenerate case where the domain is the prime field
 * the patch filename is confusing, it has the wrong ticket number :-)


---

Attachment

I've  added several doctests covering the points made by dmharvey.  And 
I've introduced an index function; if you can do `End(GF(27, 'a'))[0]`, 
then it should also be possible to do the opposite.

All this is now included in a replacement for the previous patch.  (It has a more appropriate 
name!)


---

Comment by dmharvey created at 2008-06-25 11:11:31

Hi,

I am in the middle of moving apartments so I won't get back to this for at least a week. If someone else wants to take over in the meantime, please go ahead.


---

Comment by dmharvey created at 2008-07-02 21:15:17

Excellent.


---

Comment by mabshoff created at 2008-07-03 02:15:31

Resolution: fixed


---

Comment by mabshoff created at 2008-07-03 02:15:31

Merged sage-3492-replacement.patch in Sage 3.0.4.alpha2
