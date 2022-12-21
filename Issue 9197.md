# Issue 9197: If latex() causes an error or doesn't work, we should just default to repr

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2010-06-09 16:17:13

Assignee: jason, was

CC:  danaernst

Reported by Dana Ernst - for instance, the cayley_table() of a group doesn't work in the notebook if you click 'Typeset'.  But that's not the only place that's a problem.  If there isn't a good latex() command, it should output repr() or something.  This isn't exactly graphics, but I'll put it in there for now.
