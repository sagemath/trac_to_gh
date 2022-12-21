# Issue 677: add doctest option to check if result and expected result are numerically close

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-09-17 01:12:00

Assignee: mhansen

Keywords: doctest, numerical noise


```
[02:48] <mhansen_> Regarding testing with small numerical differences, that would still be something that'd need to be handled in within the doctest code since nose provides a "wrapper" around doctest.
[02:48] <mabshoff> ok
[02:48] <williamstein> The point would only be about what options there might be for doing it.
[02:49] <williamstein> It might still have to go via preparsing.
[02:49] <williamstein> E.g., a special comment
[02:49] <williamstein> sage: foo(2.1)      # random low order bits
[02:49] <williamstein> could mean that the output should be checked except the last 3 bits discarded
[02:49] <williamstein> Another possibility would be to rewrite the doctests like this:
[02:49] <williamstein> sage: foo(2.1)
[02:50] <williamstein> 1.239930820384...
[02:50] <williamstein> Then the doctest framework just ignored everythign starting at the ...'s.
[02:50] <williamstein> But everything before will be checked to make sure it is the same.
[02:50] <mabshoff> That sounds like a good solution with the "..."
[02:50] <williamstein> That actually might be a good approach, since it will work in more complicated cases:
[02:50] <williamstein> [foo(2.1), foo(2.2)]
[02:50] <williamstein> [1.20919..., 2.233....]
[02:50] <williamstein> You could try it with that doctest just now.
```



---

Comment by mabshoff created at 2007-09-17 01:24:43

Changing component from packages to doctest.


---

Comment by mabshoff created at 2007-11-26 22:20:29

Ok, this works in python's doctests, so no need to implement this. Maybe it still needs to be added to the manual.

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-26 22:20:29

Resolution: fixed
