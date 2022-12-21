# Issue 6644: [with patch, needs review] fix doctest error for lazy_attribute and abstract_method

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-07-27 20:15:38

Assignee: jhpalmieri

As reported on [sage-devel](http://groups.google.com/group/sage-devel/browse_frm/thread/e1d0c61c235c4554), there are doctest failures for the files lazy_attribute.py and abstract_method.py.  These are caused by ticket #6505, it seems: the patch there changed banner.py, and those changes caused the failures.  Here's a patch.


---

Attachment


---

Comment by mvngu created at 2009-07-29 10:56:54

Resolution: fixed
