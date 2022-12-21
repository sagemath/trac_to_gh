# Issue 1441: latex(x1) -> x_1 might cause problems

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2007-12-09 21:32:14

Assignee: was

Consider the following:

```
sage: var('x_1,x1');
sage: x_1 - x1
x_1 - x1
sage: latex(x_1 - x1)
x_{1} - x_{1}
```

The automatic rule latex(x1) -> x_1 might thus cause ambiguities if both x1 and x_1 exist as
variables.


---

Comment by was created at 2007-12-15 23:42:33

I can see no possible fix for this.  Suggest something.
I mean, the only option I can think of would be for latex(x1) to be x1, which
isn't even latex for a variable (since that's "x times 1").

Invalid?


---

Comment by zimmerma created at 2007-12-17 12:12:45

Here is what Maple does:

```
> latex(x1);
{\it x1}
> latex(x_1);
{\it x\_1}
```

This seems a reasonable alternative to me.


---

Comment by rlm created at 2007-12-18 18:09:26

Joel Mohler also votes invalid.


---

Comment by robertwb created at 2007-12-19 03:25:15

The translation x1 -> x_1 far outweight the potential ambiguity in my mind. However, perhaps a variable named "x_1" should actually be latexed as "x\_1"


---

Comment by rlm created at 2007-12-19 19:45:02

Resolution: invalid
