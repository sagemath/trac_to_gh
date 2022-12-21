# Issue 6418: [with patch; needs review] ref manual fixes for 4.1.alpha1

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-06-26 00:28:48

Assignee: jhpalmieri

This fixes most of the warnings for building the html version of the reference manual in Sage 4.1.alpha1.



---

Attachment

I still get about 5 warnings when building the reference manual. That's better than 10 warnings.


---

Comment by jhpalmieri created at 2009-06-26 01:28:15

Replying to [comment:1 mvngu]:
> I still get about 5 warnings when building the reference manual. That's better than 10 warnings.

I only get three warnings: the "favicon" message (ticket #5799), and two warnings in sage.misc.misc which I don't know how to fix:

```
WARNING: /Applications/sage_builds/sage-4.1.alpha1/devel/sage-new/doc/en/reference/sage/misc/misc.rst:6: (WARNING/2) autodoc can't import/find class 'sage.misc.misc.MainClass.NestedClass', it reported error: "No module named MainClass", please check your spelling and sys.path
WARNING: /Applications/sage_builds/sage-4.1.alpha1/devel/sage-new/doc/en/reference/sage/misc/misc.rst:6: (WARNING/2) autodoc can't import/find class 'sage.misc.misc.MainClass.NestedClass.NestedSubClass', it reported error: "No module named MainClass.NestedClass", please check your spelling and sys.path
```



---

Comment by jhpalmieri created at 2009-06-26 02:16:16

See #6419 for a patch to get rid of the sage.misc.misc warnings (rather brutally, but it's the only thing I can figure out).


---

Comment by boothby created at 2009-06-26 17:41:12

Resolution: fixed
