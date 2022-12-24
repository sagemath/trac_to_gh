# Issue 1909: Create a "partition" function like Mathematica has

archive/issues_001909.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  sage-combinat\n\n\n```\nThanks.  I would actually strongly encourage you or somebody to\nsit down and actually write a function that has the _same_ functionality\nas http://reference.wolfram.com/mathematica/ref/Partition.html\nsince that looks like a very useful function, and I think having it\ntrivially available in Sage will be very useful to people used to\nMathematica or people porting Mathematica code to Sage.\nI hope people will implement something with the same interface and\nsubmit a patch.\n\n -- William\n```\n\n\nand \n\n\n```\nLet me be the first of many  ;-)  to say that's maybe more efficient to\nuse a temporary variable for the padding:\n\ndef partition(v,n,pad=0):\n    t=(v+[pad]*(n-len(v)%n))\n    return [t[i:i+n] for i in range(0,len(v),n)]\n\n\n-vgermrk-\n```\n\n\nSee http://groups.google.com/group/sage-devel/browse_thread/thread/64de09db029abe43\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1909\n\n",
    "created_at": "2008-01-24T13:33:36Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Create a \"partition\" function like Mathematica has",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1909",
    "user": "jason"
}
```
Assignee: cwitty

CC:  sage-combinat


```
Thanks.  I would actually strongly encourage you or somebody to
sit down and actually write a function that has the _same_ functionality
as http://reference.wolfram.com/mathematica/ref/Partition.html
since that looks like a very useful function, and I think having it
trivially available in Sage will be very useful to people used to
Mathematica or people porting Mathematica code to Sage.
I hope people will implement something with the same interface and
submit a patch.

 -- William
```


and 


```
Let me be the first of many  ;-)  to say that's maybe more efficient to
use a temporary variable for the padding:

def partition(v,n,pad=0):
    t=(v+[pad]*(n-len(v)%n))
    return [t[i:i+n] for i in range(0,len(v),n)]


-vgermrk-
```


See http://groups.google.com/group/sage-devel/browse_thread/thread/64de09db029abe43



Issue created by migration from https://trac.sagemath.org/ticket/1909





---

archive/issue_comments_012099.json:
```json
{
    "body": "Changing assignee from cwitty to mhansen.",
    "created_at": "2008-03-16T08:10:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1909#issuecomment-12099",
    "user": "mabshoff"
}
```

Changing assignee from cwitty to mhansen.



---

archive/issue_comments_012100.json:
```json
{
    "body": "Changing component from misc to combinatorics.",
    "created_at": "2008-03-16T08:10:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1909#issuecomment-12100",
    "user": "mabshoff"
}
```

Changing component from misc to combinatorics.



---

archive/issue_comments_012101.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-22T18:23:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1909",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1909#issuecomment-12101",
    "user": "AlexGhitza"
}
```

Changing type from defect to enhancement.
