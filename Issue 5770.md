# Issue 5770: [with patch, needs review] Bring doctests of modular/modsym/p1list.py up to 100%

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2009-04-12 17:25:24

Assignee: craigcitro

CC:  davidloeffler

Keywords: modular form documentation

The attached patch completes all docstrings and doctests for the file modular/modsym/p1list.py.  I also checked that the html and pdf output in the reference manual look good.


---

Attachment

Based on 3.4.1.rc2


---

Comment by davidloeffler created at 2009-04-13 12:32:19

Patch applies fine to 3.4.1.rc2, all doctests pass, and reference manual builds happily. There is just one tiny typo: in the docstring for "apply_S", it has "[-0,1;1,0]" instead of "[0,-1;1,0]". I have uploaded a patch that corrects this.


---

Comment by davidloeffler created at 2009-04-13 12:32:41

apply over previous patch


---

Attachment

Thanks, David.  Getting the documentation to build & look ok takes a long time!  As you can imagine there was a lot of cutting and pasting.  Much more of the same to com with manin_symbols.py, where there are about 5 classes each of which has a very similar set of methods (but not quite identical).


---

Comment by mabshoff created at 2009-04-13 22:06:08

Merged both patches in Sage 3.4.1.rc3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-13 22:06:08

Resolution: fixed
