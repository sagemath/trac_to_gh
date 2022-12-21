# Issue 6850: follow-up to #6531: really add ring.pyx to reference manual

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-08-31 05:44:47

Assignee: tba

CC:  davidloeffler cremona

The patch `trac_6531-restify_generic_ring-rebase.patch` at #6531 was intended to provide documentation and doctests for the module `sage/rings/ring.pyx`. It was also meant to add that module to the reference manual, but doesn't really make any changes to `doc/en/reference/rings.rst` to allow this.


---

Attachment

depends on #6531


---

Comment by mvngu created at 2009-08-31 05:50:37

The patch `trac_6850-add-ring.patch` actually adds the module `sage/rings/ring.pyx` to the reference manual and fixes some typos found in that module. It depends on #6531.


---

Comment by cremona created at 2009-08-31 11:26:23

Sorry, that was my fault -- David's original patch did make the necessary changes to the .rst file but somehow that was carried forward into the patch I made.

The patch applies and builds fine (on top of the new one at #6531).


---

Comment by cremona created at 2009-08-31 11:26:23

Changing keywords from "" to "Rings documentation".


---

Comment by mvngu created at 2009-08-31 11:41:26

Resolution: fixed
