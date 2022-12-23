# Issue 8121: preparsing of "time" special command inconsistent in company of parenthesis

Issue created by migration from https://trac.sagemath.org/ticket/8121

Original creator: was

Original creation time: 2010-01-29 16:29:52

Assignee: was

CC:  chapoton

On the Sage (=IPython) command line:

```
sage: time (2+2)/3
CPU times: user 0.00 s, sys: 0.00 s, total: 0.00 s
Wall time: 0.00 s
4/3
sage: time(2+2)/3
...
NameError: name 'time' is not defined
```


In the notebook

```
sage: time     (2+2)/3
...
NameError: name 'time' is not defined
```


This is happening because in some cases Sage treats "time <foo>" as a function call, and sometimes not.  In the notebook it is always a function, when <foo> starts with a paren, but on the command line it is a function only if there is no space between time and (.   

FIX: Make the notebook work exactly the same was as the command line, in this instance.  That seems like a reasonable solution or compromise. 




---

Comment by mkoeppe created at 2020-08-18 00:36:52

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-08-18 00:36:52

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.


---

Comment by dimpase created at 2020-08-22 08:23:19

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-08-22 08:46:10

Resolution: invalid
