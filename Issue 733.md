# Issue 733: generating docs

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2007-09-21 19:18:07

Assignee: tba

I updated the reference manual tex files by doing:

cd sage/devel/doc/ref/
./update
cd ..
make pdf

However, it claimed that there was nothing to be done, since everything was up to date.  I had to make clobber before it would build the documentation again.

Is there a way to have the ./update command touch a file which was then a dependency for the make pdf/html/etc commands?  That way, running ./update would force make to rerun the pdf/html/etc generation.



---

Comment by mabshoff created at 2008-03-11 01:16:51

I think this has been fixed. 

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-22 05:58:36

`rebuild` works, so I am closing this. If anything comes up again please open a more specific  ticket with an actual example.


---

Comment by mabshoff created at 2008-03-22 05:58:36

Resolution: worksforme
