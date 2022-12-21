# Issue 4392: smallest_integer() is broken

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2008-10-30 13:10:27

Assignee: cremona

CC:  m.t.aranes@warwick.ac.uk

Keywords: number field ideal

For number field ideals and fractional ideals, the smallest_integer() function is broken in 2 ways:

```
sage: K.<a>=QuadraticField(-5)
sage: I=K.ideal(7)
sage: I.smallest_integer()
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (237, 0))

---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/masgaj/PLMS/<ipython console> in <module>()

/local/jec/sage-3.2.alpha1/local/lib/python2.5/site-packages/sage/rings/number_field/number_field_ideal.pyc in smallest_integer(self)
    731                         bound /= p
    732                 self.smallest_integer = ZZ(bound)
--> 733                 return self.__smallest_integer
    734             I,d = self.integral_split() ## self = I/d
    735             n = I.smallest_integer()    ## n/d in self

AttributeError: 'NumberFieldFractionalIdeal' object has no attribute '_NumberFieldIdeal__smallest_integer'
sage: I.smallest_integer
1
sage: I.smallest_integer()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/masgaj/PLMS/<ipython console> in <module>()

TypeError: 'sage.rings.integer.Integer' object is not callable
```

First: in line 732 of number_field_ideal.py it has `self.smallest_integer` instead of `self.__smallest_integer`, so instead of caching the computed value we overwrite the function itself!

Second:  the answer is wrong (as the example shows).

I will try to fix this and post a ptach today (Bug Day 2008-10-30).


---

Attachment


---

Attachment

The patch sage-trac4392.patch (based on 3.2.alpha1) fixes this by completely reimplementing the function in a simpler way, using linear algebra instead of factorization.  Several new doctests have been added.  All tests in sage.rings.number_field pass.

The second patch applies after the first and handles the zero ideal properly (with another doctest to prove it!)


---

Attachment


---

Comment by cremona created at 2008-10-31 11:37:08

The third patch sage-trac4392-3.patch adds a new rather useful function coordinates() to the class NumberFieldIdeal which expresses an element of the field as a QQ-linear combination of the integral basis of the ideal.  (This does not work for relative ideals, but then what does?).  This uses a change-of-basis matrix which is cached.  It results in simpler implementations for the _contains_() and is_integral() functions, as well as the smallest_integer() function where this started.

I checked that all doctests in sage/rings/number_field pass.


---

Comment by cremona created at 2008-11-12 21:24:25

Replaces the three earlier patches


---

Attachment

For ease of reviewing, the patch sage-trac4392-new.patch merges and replaces the three previous ones.  It applies to 3.2.alpha3.


---

Comment by davidloeffler created at 2008-11-13 05:48:36

Looks good to me. I tested it against 3.1.4 and 3.2.rc0, and in both it applies cleanly. I've tested it a bit under 3.1.4 and it passes all doctests in sage/rings/number_field, and the smallest_integer() and coordinates() functions both seem to work as expected.


---

Comment by davidloeffler created at 2008-11-13 05:56:02

(On a closer inspection of the docstrings, I've noticed a typo in the docstring for the "coordinates" method -- "amllest" for "smallest". But that's the only "issue" I can find.)


---

Comment by davidloeffler created at 2008-11-13 05:59:38

fixes docstring typo in sage-trac4392-new.patch


---

Attachment

Merged sage-trac4392-new.patch and sage-4392-typo.patch in Sage 3.2.rc1.

John: The folded(?) patch was a diff a not a "proper" mercurial patch, so the credit in the log does not reflect your authorship. Please make sure to export patches.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-13 19:36:08

Merged in Sage 3.2.rc1


---

Comment by mabshoff created at 2008-11-13 19:36:08

Resolution: fixed


---

Comment by cremona created at 2008-11-14 10:02:03

Replying to [comment:6 mabshoff]:
> Merged sage-trac4392-new.patch and sage-4392-typo.patch in Sage 3.2.rc1.
> 
> John: The folded(?) patch was a diff a not a "proper" mercurial patch, so the credit in the log does not reflect your authorship. Please make sure to export patches.

Sorry about that.  I had tried to make it easier, by using mercurial queues to merge my three earlier patches.  But clearly I am not doing it right.  Every time I uses queues I read the entire documentation from beginning to end, and think I understand it, but clearly I don't since every time I mess it up. John

> 
> Cheers,
> 
> Michael


---

Comment by mabshoff created at 2008-11-14 14:47:14

Replying to [comment:8 cremona]:
> Replying to [comment:6 mabshoff]:
> > Merged sage-trac4392-new.patch and sage-4392-typo.patch in Sage 3.2.rc1.
> > 
> > John: The folded(?) patch was a diff a not a "proper" mercurial patch, so the credit in the log does not reflect your authorship. Please make sure to export patches.
> 
> Sorry about that.  I had tried to make it easier, by using mercurial queues to merge my three earlier patches.  But clearly I am not doing it right.  Every time I uses queues I read the entire documentation from beginning to end, and think I understand it, but clearly I don't since every time I mess it up. John

Well, I am more concerned about me getting credit for a patch I did not write. The solution to your problem is to export the que patch.

Cheers,

Michael
