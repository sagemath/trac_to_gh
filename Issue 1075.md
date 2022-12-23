# Issue 1075: [with patch] sync'ing hashes for fraction fields and rings

Issue created by migration from https://trac.sagemath.org/ticket/1075

Original creator: jbmohler

Original creation time: 2007-11-03 12:42:09

Assignee: somebody

The attached patch provides a custom __hash__ function for fraction field elements so that fractions with a denominator of 1 hash the same as the hash of the numerator as an element in the ring.  A charming side effect is that __hash__ is *much* faster now for fraction field elements of MPoly's over QQ.

This fixes some bugs (IMO) in the subs method of ParentWithGens when passing a dictionary.

I don't think there is any problems with hash's changing from one version to the next -- I guess there might be something I'm missing here.


---

Attachment


---

Comment by jbmohler created at 2007-11-15 22:08:44

Resolution: invalid


---

Comment by jbmohler created at 2007-11-15 22:08:44

I'm closing this because the patch I'm going to attached to #1181 is much better and much broader.
