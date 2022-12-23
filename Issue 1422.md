# Issue 1422: add bibtex function to get the bibtex code for citing the sage components

Issue created by migration from https://trac.sagemath.org/ticket/1422

Original creator: mhansen

Original creation time: 2007-12-07 21:42:23

Assignee: tba

CC:  burcin ranosch

6.3 how do i reference sage?
If you write a paper using SAGE, please reference computations done with
SAGE by including
[SAGE], SAGE Mathematical Software, Version 2.6, http://www.sagemath.org
<sup>^</sup>
How about a function bibtex() similar to latex() which gives a bibtex
entry? Coudl default to bibtex(sage) but could also provide
bibtex(pari), bibtex(gp), bibtex(Singular), etc.


---

Comment by was created at 2008-01-14 05:53:43

This is an excellent idea.    The output should probably be both the bibtex
database entry *and* the result of running it through bibtex, so it can be directly included in a paper (without having to use bibtex).

 -- William
