# Issue 1469: sage-doctest should import the namespace of the file

Issue created by migration from https://trac.sagemath.org/ticket/1469

Original creator: burcin

Original creation time: 2007-12-12 08:56:24

Assignee: burcin

The doctest script sage-doctest should try to import the namespace of the file being tested. It is not very convenient to add


```
from sage.foo import bar
```


at the beginning of every doctest in a file.

This would simplify some of the doctests in ~100 files, removing ~450 lines.

Importing the module might have an impact on the speed of the doctests. 


---

Comment by burcin created at 2007-12-12 12:17:39


```
<craigcitro> let's say the user types foo?
<craigcitro> and gets the docstring for some function
<craigcitro> then since they don't see this import that you've added
<craigcitro> they can't actually run those doctests
<craigcitro> they have to modify them by adding the sage.path.to.file at the beginning
<craigcitro> which would be confusing if you've never run into it before
```



---

Comment by burcin created at 2007-12-12 12:17:39

Resolution: wontfix
