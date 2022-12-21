# Issue 6141: [with patch, needs review] simplicial complexes: change 'facets' from an attribute to a method

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-05-27 22:00:42

Assignee: jhpalmieri

See [this thread](http://groups.google.com/group/sage-devel/browse_frm/thread/b5f9b4e58cce0c6b) from sage-devel.


---

Attachment


---

Comment by dperkinson created at 2009-05-28 05:09:56

The patch makes a simple change.  The attribute self.facet is changed to self._facet in all files in the homology directory, and a facets() method is added.  I checked the new code, ran the doctests in homology, and tried a few examples of my own.  Everything was OK.

I was using Sage Version 4.0.alpha0, Release Date: 2009-05-15 under Fedora 10.


---

Comment by mhansen created at 2009-06-01 01:12:12

While this does represent a backwards incompatible change, I think it is better to resolve it now while the code is newer.

Merged in 4.0.1.alpha0.


---

Comment by mhansen created at 2009-06-01 01:12:12

Resolution: fixed
