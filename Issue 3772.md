# Issue 3772: Gnuplot.py uses IPython/Python 2.6 keyword with

Issue created by migration from Trac.

Original creator: Jondice

Original creation time: 2008-08-04 01:35:51

Assignee: was

sage: help
Type help() for interactive help, or help(object) for help about object.
sage: help('keywords')

Here is a list of the Python keywords.  Enter any keyword to get more help.

and                 elif                if                  print
as                  else                import              raise
assert              except              in                  return
break               exec                is                  try
class               finally             lambda              while
continue            for                 not                 with
def                 from                or                  yield

Should be simple to fix, by renaming the with argument to something creative like witharg or w


---

Comment by mhansen created at 2009-11-17 11:22:30

This was fixed by the new spkg at #7187


---

Comment by mhansen created at 2009-11-17 11:22:30

Resolution: fixed
