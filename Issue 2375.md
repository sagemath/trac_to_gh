# Issue 2375: Sage 2.10.3.rc1: graph_isom.py doctest failure in PermutationGroup

archive/issues_002375.json:
```json
{
    "body": "Assignee: rlm\n\n\n```\nFile \".doctest_graph_isom.py\", line 614, in __main__.example_8\nFailed example:\n    PermutationGroup([perm_group_elt(aa) for aa in gens]).order() # long time###line 1208:_sage_    >>> PermutationGroup([perm_group_elt(aa) for aa in gens]).order() # long time\nExpected:\n    46080\nGot:\n    16492674416640\n**********************************************************************\n1 items had failures:\n   1 of 115 in __main__.example_8\n***Test Failed*** 1 failures.\n\nA mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.\n         [30.6 s]\nexit code: 256\n\n----------------------------------------------------------------------\nThe following tests failed:\n```\n\nSome comments from IRC:\n\n```\n\n[17:16] <jason-> hi everyone.\n[17:16] <mabshoff> Hi jason\n[17:16] <mabshoff> Hi jason-\n[17:16] <jason-> mabshoff: did you get the long doctest resolved?\n[17:16] <wstein> hi\n[17:17] <jason-> sorry we didn't check those doctests.\n[17:17] <jason-> oh, so it wasn't really a problem?\n[17:17] <mabshoff> jason-: Ahh, you read the log.\n[17:17] <jason-> :)\n[17:17] <mabshoff> But the problem is still open.\n[17:17] <mabshoff> I am about to open tickets for all rc1 issues that I see and release a rc1 tarball \n[17:17] <mabshoff> and binary dist for sage.math in about an hour or two.\n[17:17] <jason-> okay, I'll read that then.\n[17:17] <jason-> great.\n[17:18] <mabshoff> Give me a sec, I can point you to the failure then.\n[17:18] <mabshoff> I didn't happen before merging Robert's patch, so it isn't in rc0.\n[17:18] <mabshoff> But it is PermutationGroup related, i.e. \n[17:18] <mabshoff>     PermutationGroup([perm_group_elt(aa) for aa in gens]).order() # long time###line 1208:_sage_    >>> PermutationGroup([perm_group_elt(aa) for aa in gens]).order() # long time\n[17:18] <mabshoff> Expected:\n[17:18] <mabshoff>     46080\n[17:18] <mabshoff> Got:\n[17:18] <mabshoff>     16492674416640\n[17:19] <jason-> wow, that's a big difference.\n[17:19] <mabshoff> Yep. It makes me a little queasy.\n[17:19] <jason-> i hope it's not a sign issue.\n[17:19] <mabshoff> I think wdj and mhansen worked in that area a while back, so the doctest might \n[17:19] <jason-> (i.e., -46000 interpreted as an unsigned number)\n[17:19] <mabshoff> Ok, that makes sense.\n[17:20] <jason-> when I see numbers jump like that, that's what I think of.\n[17:20] <cwitty> sage: (16492674416640).str(base=16)\n[17:20] <cwitty> 'f0000000000'\n[17:20] <mabshoff> A wrapping issue would explain it.\n[17:20] <mabshoff> Let me run valgrind on it.\n[17:20] <mabshoff> Maybe it is in initialization issue.\n[17:20] <jason-> yeah, that hex string looks awfully suspicious :)\n[17:21] <jason-> and that's a cool function too.  I'm going to have to remember that.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2375\n\n",
    "created_at": "2008-03-03T16:45:04Z",
    "labels": [
        "graph theory",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "Sage 2.10.3.rc1: graph_isom.py doctest failure in PermutationGroup",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2375",
    "user": "mabshoff"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/2375





---

archive/issue_comments_016024.json:
```json
{
    "body": "I took a pristine 2.10.2, applied the patch from #2326, and ran the doctest in question and it gave the expected answer (46080).  This was on 32-bit Ubuntu 7.10",
    "created_at": "2008-03-03T17:11:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2375#issuecomment-16024",
    "user": "jason"
}
```

I took a pristine 2.10.2, applied the patch from #2326, and ran the doctest in question and it gave the expected answer (46080).  This was on 32-bit Ubuntu 7.10



---

archive/issue_comments_016025.json:
```json
{
    "body": "Attachment [2375-fix.patch](tarball://root/attachments/some-uuid/ticket2375/2375-fix.patch) by rlm created at 2008-03-03 21:36:52",
    "created_at": "2008-03-03T21:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2375#issuecomment-16025",
    "user": "rlm"
}
```

Attachment [2375-fix.patch](tarball://root/attachments/some-uuid/ticket2375/2375-fix.patch) by rlm created at 2008-03-03 21:36:52



---

archive/issue_comments_016026.json:
```json
{
    "body": "apply after 2375-fix.patch",
    "created_at": "2008-03-03T22:33:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2375#issuecomment-16026",
    "user": "rlm"
}
```

apply after 2375-fix.patch



---

archive/issue_comments_016027.json:
```json
{
    "body": "Attachment [2375-fix2.patch](tarball://root/attachments/some-uuid/ticket2375/2375-fix2.patch) by jason created at 2008-03-03 23:02:42\n\nlooks good to me.",
    "created_at": "2008-03-03T23:02:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2375#issuecomment-16027",
    "user": "jason"
}
```

Attachment [2375-fix2.patch](tarball://root/attachments/some-uuid/ticket2375/2375-fix2.patch) by jason created at 2008-03-03 23:02:42

looks good to me.



---

archive/issue_comments_016028.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-04T00:02:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2375#issuecomment-16028",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016029.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc1",
    "created_at": "2008-03-04T00:02:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2375#issuecomment-16029",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.3.rc1
