# Issue 5469: sage -clone ...  should copy the sage/doc/output directory

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-03-10 19:00:18

Assignee: tba

Running "sage -clone blah" should copy $SAGE_ROOT/devel/sage/doc/output/...: for one thing, if you clone the repository, you should still have access to all of the local Sage documentation (via the "Help" button in the notebook), and for another, if you want to modify library code, you shouldn't have to wait 20 minutes to see how your changes affect the reference manual.



---

Comment by robertwb created at 2009-03-11 01:09:10

Just a note, it would be nice if the files could be hard linked rather than actually copied.


---

Comment by mabshoff created at 2009-03-11 06:27:26

Resolution: fixed


---

Comment by mabshoff created at 2009-03-11 06:27:26

Fixed via #5414.

Cheers,

Michael
