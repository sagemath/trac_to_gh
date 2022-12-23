# Issue 314: raw-input in notebook compatible with command line

Issue created by migration from https://trac.sagemath.org/ticket/314

Original creator: TimothyClemans

Original creation time: 2007-03-10 23:18:05

Assignee: boothby

While this may just simply be impossible, it would be nice if I could create interactive programs in SAGE that worked both in the command line interface and the notebook interface. The purpose of this enhancement would be for games, quizzes, wizards, etc.


---

Comment by was created at 2007-03-21 23:10:04

This is a Python question not a SAGE question -- and yes there are billions of ways
to create interactive Python programs.  From this point of view, SAGE is just a Python
library.


---

Comment by was created at 2007-03-21 23:10:04

Resolution: invalid


---

Comment by schilly created at 2011-03-21 15:27:05

Just a note because it came up on sage-devel: In the notebook, one could use JavaScript's window.prompt() function to trigger input boxes just like Python's raw_input(). To make this working, this would require an round-trip to the client triggered by something in the input program. Therefore, enhancements on the client and server side of the notebook are necessary. I leave it as closed, if somebody has a plan how to do it for real feel free to open it.
