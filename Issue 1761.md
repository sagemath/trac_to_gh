# Issue 1761: Graphviz output for graphs

Issue created by migration from https://trac.sagemath.org/ticket/1761

Original creator: boothby

Original creation time: 2008-01-12 04:16:39

Assignee: rlm

CC:  ncalexan

Add functionality to use graphviz for graph display.


---

Attachment


---

Comment by ncalexan created at 2008-01-22 07:35:49

This is useful and should be applied.  I would have liked to see the actual function abstracted to a Graph class higher in the hierarchy, if there is one, because it seems like the actual code is the same, just the edge identifier symbols for dot are different.  Also, is '# not tested' the correct tag for doctests to not get run?


---

Comment by jason created at 2008-02-16 11:11:10

I agree with ncalexan:

1. The string functions should be abstracted to the GenericGraph class with the string changing depending on whether the graph is directed or not.  In general, we are trying to consolidate functionality to the GenericGraph class when possible these days.

2. The graphviz function documentation should clearly state that graphviz (and in particular, dot) needs to be installed in the system path.  It would be nice were the option to run the other graphviz programs, like neato, etc.


---

Comment by ncalexan created at 2008-04-06 19:36:23

Changing keywords from "" to "graph visualization dot graphviz".


---

Comment by ncalexan created at 2008-04-06 19:36:23

The attached patch addresses the referee's comments.

It also removes references to the actual graphviz/dot application.  I don't see how this can be made cross-platform and I'm worried about licensing issues, so I'm just ducking the issue.  Open a new ticket if you'd like this functionality.


---

Attachment

The original bundle is not needed; apply only the patch.


---

Comment by boothby created at 2008-04-06 20:07:22

Looks good to me.


---

Comment by mabshoff created at 2008-04-08 15:28:58

Resolution: fixed


---

Comment by mabshoff created at 2008-04-08 15:28:58

Merged in Sage 3.0.alpha3


---

Comment by mabshoff created at 2008-04-08 16:58:14

doctest fix due to bitrot


---

Attachment

create doctest files in SAGE_TESTDIR
