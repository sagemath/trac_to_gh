# Issue 5066: [with patch, needs review] break out relative number fields into separate file

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2009-01-23 08:59:32

Assignee: was

Keywords: relative number fields files

This has been some time coming, but let's separate relative number fields from generic/absolute number fields now, while I'm looking at them.


---

Attachment

Fails a doctest, to be addressed by patches to #1357 (which will depend on this)


---

Comment by roed created at 2009-01-24 09:47:53

Looks good, assuming that the other patch you mentioned (which isn't #1357) gets in at the same time.  The only change that needs to be made is in sage.rings.polynomials.polynomial_quotient_ring_element, changing number_field to number_field_rel a couple places.


---

Comment by ncalexan created at 2009-01-24 10:00:36

Patch should be at #1367, sorry.  With #5066 and #1367, all doctests pass on sage.math.


---

Comment by mabshoff created at 2009-01-29 05:38:41

Merged in Sage 3.3.alpha3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-29 05:38:41

Resolution: fixed
