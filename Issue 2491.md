# Issue 2491: Showing source from sloane_functions

archive/issues_002491.json:
```json
{
    "body": "Assignee: mhansen\n\nCC:  sage-combinat\n\nFrom IRC #sage-devel\n\n\n```\n<mhansen> jaap: There's a difference between sloane.A000001?? and sage.combinat.sloane_functions.A000001??\n<jaap> mhansen sage: sloane.A000001??\n<jaap> Error getting source: arg is not a module, class, method, function, traceback, frame, or code object\n<mhansen> jaap: A bit earlier I had said that  sloane.A000001?? doesn't work because of the way the sloane object works.\n<jaap> ok, but how about the OEIS user who wants to see how things work?\n<mhansen> If it's a bug, then it should be reported.\n<jaap> I think so\n```\n\n\n\n\n\n```\nsage: sloane.A000045\n Fibonacci numbers with index n >= 0\n\nsage: sloane.A000045?\n\nsage: sloane.A000045??\nError getting source: arg is not a module, class, method, function, traceback, frame, or code object\n\nsage: sage.combinat.sloane_functions.A000045??\n\nworks ok.\n\n\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2491\n\n",
    "created_at": "2008-03-12T14:13:50Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "title": "Showing source from sloane_functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2491",
    "user": "jsp"
}
```
Assignee: mhansen

CC:  sage-combinat

From IRC #sage-devel


```
<mhansen> jaap: There's a difference between sloane.A000001?? and sage.combinat.sloane_functions.A000001??
<jaap> mhansen sage: sloane.A000001??
<jaap> Error getting source: arg is not a module, class, method, function, traceback, frame, or code object
<mhansen> jaap: A bit earlier I had said that  sloane.A000001?? doesn't work because of the way the sloane object works.
<jaap> ok, but how about the OEIS user who wants to see how things work?
<mhansen> If it's a bug, then it should be reported.
<jaap> I think so
```





```
sage: sloane.A000045
 Fibonacci numbers with index n >= 0

sage: sloane.A000045?

sage: sloane.A000045??
Error getting source: arg is not a module, class, method, function, traceback, frame, or code object

sage: sage.combinat.sloane_functions.A000045??

works ok.


```



Issue created by migration from https://trac.sagemath.org/ticket/2491





---

archive/issue_comments_016879.json:
```json
{
    "body": "> sage: sloane.A000045??\n> Error getting source: arg is not a module, class, method, function, traceback, frame, or code object\n\nThat this doesn't work should be considered a bug.   The actual introspection is simply some python code I wrote, so it's fixable.  Nick also knows something about it.",
    "created_at": "2008-03-12T15:36:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2491#issuecomment-16879",
    "user": "was"
}
```

> sage: sloane.A000045??
> Error getting source: arg is not a module, class, method, function, traceback, frame, or code object

That this doesn't work should be considered a bug.   The actual introspection is simply some python code I wrote, so it's fixable.  Nick also knows something about it.



---

archive/issue_comments_016880.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-08-27T01:56:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2491#issuecomment-16880",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_016881.json:
```json
{
    "body": "Positive review. Works for me.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-27T01:57:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2491#issuecomment-16881",
    "user": "mabshoff"
}
```

Positive review. Works for me.

Cheers,

Michael



---

archive/issue_comments_016882.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-27T02:17:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2491#issuecomment-16882",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016883.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha1",
    "created_at": "2008-08-27T02:17:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2491#issuecomment-16883",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.alpha1
