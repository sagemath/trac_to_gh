# Issue 3091: help() should give Sage help, not Python

Issue created by migration from https://trac.sagemath.org/ticket/3091

Original creator: gnprice

Original creation time: 2008-05-03 07:32:46

Assignee: was

CC:  jhpalmieri

When I fired up Sage having never used it before, the first thing I tried after '1+1' and 'f(x) = x + x' followed by 'f(2)' was 'help'.  I was disappointed to see that it gave the Python help system.  I know Python, and I suspect even most Sage users who don't are more likely to want Sage help than Python help when they start out.


```
sage: help
Type help() for interactive help, or help(object) for help about object.
sage: help()

Welcome to Python 2.5!  This is the online help utility.

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at http://www.python.org/doc/tut/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, or topics, type "modules",
"keywords", or "topics".  Each module also comes with a one-line summary
of what it does; to list the modules whose summaries contain a given word
such as "spam", type "modules spam".

help> 
```


I wound up using 'locals()' to see what was around -- a Python trick -- then 'help' on individual values that looked interesting.  I still don't know how to find introductory, overview help on Sage from the interactive prompt, or a list of functions without using tricks from a Python background.  I'm sure there's documentation on the web, but it's nice to be able to get to it while at the prompt.

Of course the native Python 'help' function is invaluable for printing and paging through docstrings, once one knows the name of something.  I'm referring to its behavior with no arguments -- it should begin to give a clue about syntax, what's available, and where to look on the web, for Sage rather than for Python.

Thanks!



---

Comment by gnprice created at 2008-05-07 01:52:00

I just watched another first-time Sage user try typing 'help()' at the prompt. =)

Greg


---

Comment by mpatel created at 2009-11-14 19:13:44

I think we can close this ticket.


---

Comment by mpatel created at 2010-01-16 19:49:56

With #6820 merged, should we close this ticket?


---

Comment by mpatel created at 2010-01-16 19:49:56

Changing status from new to needs_info.


---

Comment by jhpalmieri created at 2010-01-16 20:18:16

Resolution: duplicate
