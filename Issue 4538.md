# Issue 4538: write a python script that runs a subprocess and kills it after a while

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-11-17 15:13:40

Assignee: cwitty

CC:  gfurnish

Create a script `sage-walltimekill` SAGE_ROOT/local/bin/ that would run
a subprocess, wait a certain amount of time, then killing it.  

```
sage-walltimekill 3600 sage
```

would kill the process it starts after 3600 wall seconds.

This will be useful both for doctesting and the notebook.  It's the sort of
thing ulimit "should" do, but doesn't. 


---

Comment by was created at 2008-11-17 15:13:51

Changing type from defect to enhancement.


---

Comment by mabshoff created at 2008-12-05 05:18:09

Gary,

this is very interesting and would help to make -tp more robust.

Cheers,

Michael


---

Comment by gfurnish created at 2008-12-05 07:11:47

With #717 can we close this as invalid?  Or do you want me to encapsulate the #717 code for some other purpose?


---

Comment by mabshoff created at 2008-12-05 07:21:16

Replying to [comment:3 gfurnish]:
> With #717 can we close this as invalid?  Or do you want me to encapsulate the #717 code for some other purpose?  

This could still come in useful for example for the notebook, so I would leave it open.

William: any thoughts here?

Cheers,

Michael
