# Issue 3325: [with patch, needs review] small error in argument to dvipng in latex.py

Issue created by migration from https://trac.sagemath.org/ticket/3325

Original creator: jhpalmieri

Original creation time: 2008-05-28 19:50:11

Assignee: somebody

Keywords: %latex, dvipng

%latex calls dvipng if it is available.  Its arguments include '-q*', and my shell tries to expand the *, thus causing %latex to bomb whenever I use it.  In fact, the argument should just be '-q'.  (See the dvipng man page: at one point it says

```
-q* Run quietly.  Don't chatter about pages converted, etc. to standard output;
    report no warnings (only errors) to standard error.
```

But earlier it says

```
Many of the parameterless options listed here can be turned off by suffixing the
option with a zero (0); for instance, to turn off page reversal, use -r0.  Such
options are marked with a trailing *.
```

So the * is not actually part of the argument.)


---

Comment by jhpalmieri created at 2008-05-28 19:50:53

remove extraneous * in argument to dvipng


---

Attachment

Patch looks good to me. Positive review. 

Nice catch John.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-29 01:10:25

Resolution: fixed


---

Comment by mabshoff created at 2008-05-29 01:10:25

Merged in Sage 3.0.3.alpha1
