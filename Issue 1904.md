# Issue 1904: elliptic curves -- many period lattice functions just don't work

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-24 02:46:27

Assignee: was

CC:  davidloeffler


```
sage: E = EllipticCurve('37a1')
sage: Lambda = E.period_lattice()
sage: OE = Lambda.omega(); OE
5.986917292463919259664019958905016355595167582740265970681046757126500713973
sage: Lambda.matrix()
Traceback (most recent call last):
...
TypeError: Unable to coerce 2.451389381986790060854224831866525225349617289144796614656471406129152899999*I (<type 'sage.rings.complex_number.ComplexNumber'>) to Rational
sage: Lambda.gram_matrix()
Traceback (most recent call last):
...
AttributeError: 'PeriodLattice_ell' object has no attribute 'ambient_vector_space'
sage: Lambda.basis()
(2.993458646231959629832009979452508177797583791370132985340523378563250356987, 2.451389381986790060854224831866525225349617289144796614656471406129152899999*I)
sage: Lambda.basis_matrix()
Traceback (most recent call last):
...
TypeError: Unable to coerce 2.451389381986790060854224831866525225349617289144796614656471406129152899999*I (<type 'sage.rings.complex_number.ComplexNumber'>) to Rational
s
```


The root cause of this is that Period lattices actually derive from the abstract free module type, but they don't implement all the functionality that type requires. 


---

Comment by cremona created at 2008-09-09 14:22:07

Just to confirm that none of this has changed yet despite a lot of (mainly precision-related) work on period lattices leading up to 3.1.2.

I'm not sure what benefits, if any, the class PeriodLattice_ell gains from being derived from FreeModule_generic_pid (via class PeriodLattice), but it means that len(dir(L)) is 210 so there's a lot of work to do implementing possibly trivial and possibly irrelevant things.

The issue is that a FreeModule_generic_pid seems to think that it's a submodule of some concrete module like `ZZ^n`, rather than being an abstract module;  functions like basis_matrix() make no sense in general.

If anyone can point out a method of FreeModule_generic_pid which PeriodLattice_ell should implement but does not, I would be happy to implement it.


---

Comment by davidloeffler created at 2008-11-04 11:59:43

Just for the record: ticket #4388 goes some way towards fixing this by providing a basis_matrix() method for period lattices. This fixes all of the problems reported by was above, but several issues remain: for example, I can't seem to create any nonzero element of a period lattice -- the return values of basis() are plain complex numbers, not elements of the lattice, and attempting to coerce them back into the lattice fails.


---

Comment by cremona created at 2008-11-04 12:06:04

You are right, David.  For me this class is just a sort of place-holder to hold the data needed for when you ask an elliptic curve about its periods and related things.  I never thought about it as a lattice in any precise sense.  (I did not create the class, by the way, but I have added to it -- for example, support for real embeddings of number fields, not just Q).

Feel free to let it behave more sensibly for what you need by adding stuff!  John


---

Comment by AlexGhitza created at 2009-01-23 07:06:33

Changing type from defect to enhancement.


---

Comment by davidloeffler created at 2009-07-20 19:47:23

Changing assignee from was to davidloeffler.


---

Comment by davidloeffler created at 2009-07-20 19:47:23

Assigned to new "elliptic curves" component.


---

Comment by davidloeffler created at 2009-07-20 19:47:23

Changing component from number theory to elliptic curves.


---

Comment by davidloeffler created at 2009-10-09 09:12:51

Remove assignee davidloeffler.


---

Comment by zimmerma created at 2011-09-16 13:11:33

Changing keywords from "" to "ecc2011".


---

Comment by zimmerma created at 2011-09-16 13:11:33

Changing status from new to needs_info.


---

Comment by zimmerma created at 2011-09-16 13:11:33

the examples in the description work with Sage 4.7.1:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: 9322
sage: E = EllipticCurve('37a1')
sage: Lambda = E.period_lattice()
sage: OE = Lambda.omega(); OE
5.98691729246392
sage: Lambda.matrix()
[ 2.99345864623196 0.000000000000000]
[0.000000000000000  2.45138938198679]
sage: Lambda.gram_matrix()
[ 8.96079466670088 0.000000000000000]
[0.000000000000000  6.00930990211758]
sage: Lambda.basis()
(2.99345864623196, 2.45138938198679*I)
sage: Lambda.basis_matrix()
[ 2.99345864623196 0.000000000000000]
[0.000000000000000  2.45138938198679]
```

Should this ticket be closed?
| Sage Version 4.7.1, Release Date: 2011-08-11                       |
| Type notebook() for the GUI, and license() for information.        |
Paul


---

Comment by cremona created at 2011-09-16 13:34:20

Replying to [comment:7 zimmerma]:

> Should this ticket be closed?
> 
> Paul

In my opinion, yes, but see the comments above by David Loeffler.


---

Comment by davidloeffler created at 2011-09-16 13:48:15

Changing status from needs_info to needs_review.


---

Comment by davidloeffler created at 2011-09-16 13:48:15

I concur with the vote to close. Setting this to "positive review" to bring it to the notice of someone who has the authority to do so. -- David


---

Comment by davidloeffler created at 2011-09-16 13:48:30

Changing status from needs_review to positive_review.


---

Comment by leif created at 2011-09-17 05:47:22

Resolution: fixed
