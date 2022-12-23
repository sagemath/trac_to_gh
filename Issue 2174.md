# Issue 2174: [bug day?] upgrade -- make upgrade() so that when run in the notebook it is not very verbose

Issue created by migration from https://trac.sagemath.org/ticket/2174

Original creator: was

Original creation time: 2008-02-16 01:31:11

Assignee: mabshoff

CC:  was

Make it so in the notebook the upgrade command is very non-verbose.
In order to make this happen, we'll need to have an option to 
"sage -i" that makes sage-spkg much less verbose, i.e., just display
each package is being built, and whether the install failed or
succeeded. 

Also, upgrade() run in the notebook should autodect that it should
run non-verbosely by checking whether it is run in embedded mode (the
same as is done in plotting). 

 
This is a defect, because right now if one types `upgrade()` into the notebook, because of verbosity of the output it can take 20 HOURS to upgrade, as reported by Jim Morrow. 


---

Comment by mabshoff created at 2008-02-16 01:37:54

This is related to #1439.

Cheers,

Michael


---

Comment by timdumol created at 2010-01-18 00:58:18

Since how notebook runs commands has been massively redone, I believe this is fixed (#1439 is definitely fixed, and this is just an extension of it).


---

Comment by timdumol created at 2010-01-19 03:39:42

Resolution: fixed
