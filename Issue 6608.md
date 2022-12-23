# Issue 6608: [with patch, needs review] nodetex is broken

Issue created by migration from https://trac.sagemath.org/ticket/6608

Original creator: jhpalmieri

Original creation time: 2009-07-24 00:26:13

Assignee: jhpalmieri

If you type (at the command line)

```
latex.blackboard_bold?
```

you get the docstring for this, but it is missing all of the backslashes.  This is because the docstring is being processed by the `detex` function, but it's not supposed to be: the docstring contains a "nodetex" directive.  (You can see the backslashes and the "nodetex" directive if you type `latex.blackboard_bold??`.)

The attached patch makes this work again.  Test with the above, or with `view?` or with `sage.misc.sagedoc.detex?`, for instance.


---

Attachment


---

Comment by awebb created at 2009-07-26 12:55:24

Looks good to me. I tried to create a new doctest for this but it was a) too big and ugly and/or b) too fragile to be useful. Adam


---

Comment by mvngu created at 2009-07-27 07:57:13

Resolution: fixed
