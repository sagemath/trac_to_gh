# Issue 6419: [with patch, needs review] fix ref manual warnings for sage.misc.misc

Issue created by migration from https://trac.sagemath.org/ticket/6419

Original creator: jhpalmieri

Original creation time: 2009-06-26 02:14:52

Assignee: jhpalmieri

CC:  mhansen

This patch fixes the warnings

```
WARNING: /Applications/sage_builds/sage-4.1.alpha1/devel/sage-new/doc/en/reference/sage/misc/misc.rst:6: 
(WARNING/2) autodoc can't import/find class 'sage.misc.misc.MainClass.NestedClass', it reported error: 
"No module named MainClass", please check your spelling and sys.path
WARNING: /Applications/sage_builds/sage-4.1.alpha1/devel/sage-new/doc/en/reference/sage/misc/misc.rst:6: 
(WARNING/2) autodoc can't import/find class 'sage.misc.misc.MainClass.NestedClass.NestedSubClass', it 
reported error: "No module named MainClass.NestedClass", please 
check your spelling and sys.path
```

produced by Sphinx when building the html version of the reference manual, by omitting these classes from the documentation.


---

Attachment

Looks good to me. It's a pity that Sphinx can't handle this a bit better, but anyone who needs to know about nested classes is going to be a pretty hardcore Sage hacker who is more than capable of just reading the docs themselves. Positive review.

David


---

Comment by rlm created at 2009-07-04 01:41:48

Resolution: fixed
