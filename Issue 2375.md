# Issue 2375: Sage 2.10.3.rc1: graph_isom.py doctest failure in PermutationGroup

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-03-03 16:45:04

Assignee: rlm


```
File ".doctest_graph_isom.py", line 614, in __main__.example_8
Failed example:
    PermutationGroup([perm_group_elt(aa) for aa in gens]).order() # long time###line 1208:_sage_    >>> PermutationGroup([perm_group_elt(aa) for aa in gens]).order() # long time
Expected:
    46080
Got:
    16492674416640
**********************************************************************
1 items had failures:
   1 of 115 in __main__.example_8
***Test Failed*** 1 failures.

A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.
         [30.6 s]
exit code: 256

----------------------------------------------------------------------
The following tests failed:
```

Some comments from IRC:

```

[17:16] <jason-> hi everyone.
[17:16] <mabshoff> Hi jason
[17:16] <mabshoff> Hi jason-
[17:16] <jason-> mabshoff: did you get the long doctest resolved?
[17:16] <wstein> hi
[17:17] <jason-> sorry we didn't check those doctests.
[17:17] <jason-> oh, so it wasn't really a problem?
[17:17] <mabshoff> jason-: Ahh, you read the log.
[17:17] <jason-> :)
[17:17] <mabshoff> But the problem is still open.
[17:17] <mabshoff> I am about to open tickets for all rc1 issues that I see and release a rc1 tarball 
[17:17] <mabshoff> and binary dist for sage.math in about an hour or two.
[17:17] <jason-> okay, I'll read that then.
[17:17] <jason-> great.
[17:18] <mabshoff> Give me a sec, I can point you to the failure then.
[17:18] <mabshoff> I didn't happen before merging Robert's patch, so it isn't in rc0.
[17:18] <mabshoff> But it is PermutationGroup related, i.e. 
[17:18] <mabshoff>     PermutationGroup([perm_group_elt(aa) for aa in gens]).order() # long time###line 1208:_sage_    >>> PermutationGroup([perm_group_elt(aa) for aa in gens]).order() # long time
[17:18] <mabshoff> Expected:
[17:18] <mabshoff>     46080
[17:18] <mabshoff> Got:
[17:18] <mabshoff>     16492674416640
[17:19] <jason-> wow, that's a big difference.
[17:19] <mabshoff> Yep. It makes me a little queasy.
[17:19] <jason-> i hope it's not a sign issue.
[17:19] <mabshoff> I think wdj and mhansen worked in that area a while back, so the doctest might 
[17:19] <jason-> (i.e., -46000 interpreted as an unsigned number)
[17:19] <mabshoff> Ok, that makes sense.
[17:20] <jason-> when I see numbers jump like that, that's what I think of.
[17:20] <cwitty> sage: (16492674416640).str(base=16)
[17:20] <cwitty> 'f0000000000'
[17:20] <mabshoff> A wrapping issue would explain it.
[17:20] <mabshoff> Let me run valgrind on it.
[17:20] <mabshoff> Maybe it is in initialization issue.
[17:20] <jason-> yeah, that hex string looks awfully suspicious :)
[17:21] <jason-> and that's a cool function too.  I'm going to have to remember that.
```



---

Comment by jason created at 2008-03-03 17:11:12

I took a pristine 2.10.2, applied the patch from #2326, and ran the doctest in question and it gave the expected answer (46080).  This was on 32-bit Ubuntu 7.10


---

Attachment


---

Comment by rlm created at 2008-03-03 22:33:17

apply after 2375-fix.patch


---

Attachment

looks good to me.


---

Comment by mabshoff created at 2008-03-04 00:02:28

Resolution: fixed


---

Comment by mabshoff created at 2008-03-04 00:02:28

Merged in Sage 2.10.3.rc1
