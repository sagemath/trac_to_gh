# Issue 819: linenumbers in python inspect are 0-based

Issue created by migration from https://trac.sagemath.org/ticket/819

Original creator: nbruin

Original creation time: 2007-10-04 03:06:52

Assignee: robertwb

python's inspect.findsource returns a line number that is 0-based, because the source
file is considered to be a list of lines. sage.misc.sageinspect._extract_embedded_position tries to return similar data, but does so 1-based. We should probably be consistent about how line numbers are handled.

Line numbers *SHOULD* be 1-based, of course, but we cannot change python's library. 

At the same time, python's "inspect" does not have a routine to just give back a line number. It always gives the source itself as well.

Perhaps the solution is to include into sageinspect a routine that gives back file name and line number? The routine "fileandline" included in patch #768 tries to do this. Perhaps it should be included in sageinspect and thus hide the discrepancy between 0- and 1-based line numbers that currently becomes visible because functionality has to be borrowed from both "inspect" and "sageinspect"?


---

Comment by mmezzarobba created at 2015-04-13 16:10:24

I doubt we want to change the convention at this point.


---

Comment by mmezzarobba created at 2015-04-13 16:10:24

Changing status from new to needs_review.


---

Comment by vdelecroix created at 2015-04-14 09:39:57

Replying to [comment:5 mmezzarobba]:
> I doubt we want to change the convention at this point.

why?


---

Comment by mmezzarobba created at 2015-04-14 09:49:30

Replying to [comment:6 vdelecroix]:
> Replying to [comment:5 mmezzarobba]:
> > I doubt we want to change the convention at this point.
> 
> why?

I misread the description and thought the idea was to make `sageinspect` return 0-based line numbers. Sorry for the noise.


---

Comment by mmezzarobba created at 2015-04-14 09:49:30

Changing status from needs_review to needs_work.
