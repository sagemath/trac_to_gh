# Issue 8842: sage notebook interacts: format exceptions nicely

Issue created by migration from https://trac.sagemath.org/ticket/8842

Original creator: was

Original creation time: 2010-05-02 20:20:35

Assignee: jason, was

CC:  chapoton


```
If I write a function in a cell of a notebook like:

@interact
def foo(a = input_box(default=0, type=Integer)):
    # do something here
    pass

And the user enters something that cannot be coerced to Integer, then
I get a verbose (and rather unhelpful) exception, which, as far as I
can see, can't be caught inside of foo.  So, I would suggest that if a
type is specified in input_box, and the coercion fails that a nicer
looking message be given (perhaps next to the box that a specifies).

Victor
```



---

Comment by mkoeppe created at 2020-08-18 00:36:52

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Changing status from new to needs_review.


---

Comment by chapoton created at 2020-09-09 09:39:46

Resolution: invalid
