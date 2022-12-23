# Issue 8142: Unexpected notebook behavior when readline init file is non empty

Issue created by migration from https://trac.sagemath.org/ticket/8142

Original creator: mmeulien

Original creation time: 2010-02-01 08:01:43

Assignee: was

Keywords: notebook readline .inputrc

To reproduce the problem

===============

1. Create the file ~/.inputrc with the following content:



$if Python

# Pair insertion

"\(": "\C-q()\C-b"

$endif



This will automaticaly insert a closing brace after the cursor when an opening brace is inserted when the application name is Python.


2. Start Sage


3. In command line, everything seems ok; closing braces get inserted automaticaly.


4. In notebook, closing braces aren't inserted automaticaly AND computations never end!


Possible workarounds

=============

From Bash documentation (Command Line Editing>Readline Init File>Conditional Init Constructs), "Each program using the Readline library sets the APPLICATION NAME". The "$if" constructs in the .inputrc file uses this variable for application-specific settings.


Sage should set that variable to its own value. Better it should change its value when the notebook is started/stopped.


---

Comment by mkoeppe created at 2021-12-02 01:04:49

outdated, should close


---

Comment by mkoeppe created at 2021-12-02 01:04:49

Changing status from new to needs_review.


---

Comment by dimpase created at 2021-12-02 23:39:46

Changing status from needs_review to positive_review.


---

Comment by mkoeppe created at 2021-12-03 18:41:01

Resolution: invalid
