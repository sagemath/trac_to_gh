# Issue 572: in sage-env make sure we do not append ":"  LD_WHATEVER

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-09-02 18:29:57

Assignee: mabshoff

Hello,

The optinal gcc spkg doesn't like trailing ":" in environment variables:

```
[20:06] <mabshoff> Another thing:
[20:06] <mabshoff> *** LIBRARY_PATH shouldn't contain the current directory when
[20:06] <mabshoff> *** building gcc. Please change the environment variable
[20:06] <mabshoff> *** and run configure again.
<SNIP>
[20:10] <mabshoff> Problem might be that "LIBRARY_PATH=/tmp/Work2/sage-2.8.3.rc3/local/lib/:" has the trailing ":"
[20:10] <sage> ah. you could change that too
[20:10] <mabshoff> If LD_WHATEVER is empty skip the $LD_WHATEVER on export :
[20:10] <mabshoff> .
[20:11] <mabshoff> Removing the trailing ":" makes configure work.
```

Cheers,

Michael


---

Comment by mabshoff created at 2007-09-02 18:30:05

Changing status from new to assigned.


---

Comment by was created at 2007-09-02 20:11:48

Resolution: fixed
