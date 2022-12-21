# Issue 3779: inconsistency for variables method, leads to errors in differentiation

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2008-08-06 04:29:22

Assignee: gfurnish


```

Hi William:

I was running Sage 3.0.2 on Linux when the error occurred.  Just now i
upgraded to 'sage-3.0.6-i686-Linux-debian-intel' without problems, ran
the same code (in a notebook and on the command line), and got the
same error.  Hmm, i don't understand why Sage can do 'diff(f*SR(2),x)'
but not 'diff(f*SR(1),x)'.

Alex
```


This boils down to the fact that some symbolic objects take an extra argument in their `variables` method. It is unclear what the meaning of this argument is (couldn't find any examples) and if it should be removed, or added, to make things consistent. (I'd guess removed, but I don't want to break things.) 


---

Comment by gfurnish created at 2008-08-06 06:30:33

The argument doesn't exist in symbolics, so I'm in favor of removal (and I have no idea what it does either)


---

Comment by mhansen created at 2008-08-06 20:09:08

Changing assignee from gfurnish to mhansen.


---

Comment by mhansen created at 2008-08-06 20:09:08

The argument was used to pass in additional variables to the variables method which would then be subsequently returned.  This functionality was never used, and I can't / couldn't think of a case where it would be needed.  So, I do think the correct fix is to remove it.  I've attached a patch which does that and passes tests.


---

Comment by mhansen created at 2008-08-06 20:09:08

Changing status from new to assigned.


---

Attachment

Looks good to me, and fixes the bug. The only question I had is why you wrote tuple([]) rather than (), but I'm OK with that.


---

Comment by mhansen created at 2008-08-07 02:12:33

There's no real reason -- it's just what I happened to type :-)


---

Attachment


---

Comment by mabshoff created at 2008-08-10 06:33:25

Resolution: fixed


---

Comment by mabshoff created at 2008-08-10 06:33:25

Merged both patches in Sage 3.1.alpha1
