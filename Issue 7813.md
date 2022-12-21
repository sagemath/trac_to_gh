# Issue 7813: No empty links at docs

Issue created by migration from Trac.

Original creator: slosoi

Original creation time: 2010-01-02 03:42:43

Assignee: schilly

Keywords: docs

To disable at least temporarily the dead links, for instance, at

 1. http://sagemath.org/doc/genindex.html
 2. http://sagemath.org/doc/tutorial/modindex.html
 3. http://sagemath.org/doc/tutorial/genindex.html
 ...


---

Attachment

See lines 156, 159, and 162. `hg qnew -f docs patch` did not work for me this time so I include the whole file.
