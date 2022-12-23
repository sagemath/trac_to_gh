# Issue 5910: move logic module boolopt.py to another enhancement ticket

Issue created by migration from https://trac.sagemath.org/ticket/5910

Original creator: mvngu

Original creation time: 2009-04-27 11:53:41

Assignee: somebody

Keywords: Quine-McCluskey, logic

This is a followup to #545. As discussed at #545, the module `boolopt.py` is moved to this enhancement ticket. So basically, #545 no longer requires boolopt.py to reach 100% doctest coverage in order to be merged into Sage. Thus the only work needed to be done here is to bring coverage of boolopt.py to 100%.


---

Attachment

Restore the method simplify() and its doctests


---

Comment by mabshoff created at 2009-04-30 03:30:11

Please make sure to convert the newlines to standard Unix convention since it seems that some newlines are in Windows format. It would also be good to get all this restified, get the coverage of logic.py up and get the code into the reference manual post ReST conversion - not that this all has to happen on this ticket. I am just glad we are done wioth #545 :)

Cheers,

Michael


---

Comment by mvngu created at 2009-05-05 06:24:08

with Unix newline


---

Attachment


---

Comment by AlexGhitza created at 2010-01-02 03:18:33

Changing component from basic arithmetic to misc.


---

Comment by mhansen created at 2013-07-23 14:55:02

Resolution: invalid


---

Comment by mhansen created at 2013-07-23 14:55:02

Given http://comments.gmane.org/gmane.comp.mathematics.sage.devel/67430 , I think we can close this.  The file is still here for reference if we ever need it.
