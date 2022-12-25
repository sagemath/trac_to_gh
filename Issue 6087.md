# Issue 6087: graph automorphism group segfaults on invalid input

archive/issues_006087.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  @rlmill @orlitzky\n\nEven though the input is invalid (the partition isn't a valid partition), I think segfaulting is considered a bug:\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: g=graphs.CubeGraph(3)\nsage: \nsage: g.relabel()\nsage: g.automorphism_group(partition=[[0,1,2],[3,4,5]])\n| Sage Version 3.4.1.rc2, Release Date: 2009-04-10                   |\n| Type notebook() for the GUI, and license() for information.        |\n\n------------------------------------------------------------\nUnhandled SIGSEGV: A segmentation fault occured in SAGE.\nThis probably occured because a *compiled* component\nof SAGE has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run SAGE under gdb with 'sage -gdb' to debug this.\nSAGE will now terminate (sorry).\n------------------------------------------------------------\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6087\n\n",
    "created_at": "2009-05-19T21:38:06Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.8",
    "title": "graph automorphism group segfaults on invalid input",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6087",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @rlmill

CC:  @rlmill @orlitzky

Even though the input is invalid (the partition isn't a valid partition), I think segfaulting is considered a bug:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: g=graphs.CubeGraph(3)
sage: 
sage: g.relabel()
sage: g.automorphism_group(partition=[[0,1,2],[3,4,5]])
| Sage Version 3.4.1.rc2, Release Date: 2009-04-10                   |
| Type notebook() for the GUI, and license() for information.        |

------------------------------------------------------------
Unhandled SIGSEGV: A segmentation fault occured in SAGE.
This probably occured because a *compiled* component
of SAGE has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run SAGE under gdb with 'sage -gdb' to debug this.
SAGE will now terminate (sorry).
------------------------------------------------------------
```



Issue created by migration from https://trac.sagemath.org/ticket/6087





---

archive/issue_comments_048404.json:
```json
{
    "body": "Attachment [sage-trac_6087.patch](tarball://root/attachments/some-uuid/ticket6087/sage-trac_6087.patch) by @orlitzky created at 2011-12-15 15:09:47\n\nPatch adding a doctest for the correct behavior",
    "created_at": "2011-12-15T15:09:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6087",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6087#issuecomment-48404",
    "user": "https://github.com/orlitzky"
}
```

Attachment [sage-trac_6087.patch](tarball://root/attachments/some-uuid/ticket6087/sage-trac_6087.patch) by @orlitzky created at 2011-12-15 15:09:47

Patch adding a doctest for the correct behavior



---

archive/issue_comments_048405.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-12-15T15:10:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6087",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6087#issuecomment-48405",
    "user": "https://github.com/orlitzky"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_048406.json:
```json
{
    "body": "This is fixed now, so I've added a doctest for it.",
    "created_at": "2011-12-15T15:10:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6087",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6087#issuecomment-48406",
    "user": "https://github.com/orlitzky"
}
```

This is fixed now, so I've added a doctest for it.



---

archive/issue_comments_048407.json:
```json
{
    "body": "Looks great; passes tests on the file.  Thanks!",
    "created_at": "2011-12-16T16:26:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6087",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6087#issuecomment-48407",
    "user": "https://github.com/jasongrout"
}
```

Looks great; passes tests on the file.  Thanks!



---

archive/issue_comments_048408.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-12-16T16:26:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6087",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6087#issuecomment-48408",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_048409.json:
```json
{
    "body": "Can you add your name to the Author field?",
    "created_at": "2011-12-16T16:27:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6087",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6087#issuecomment-48409",
    "user": "https://github.com/jasongrout"
}
```

Can you add your name to the Author field?



---

archive/issue_comments_048410.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-12-17T09:12:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6087",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6087#issuecomment-48410",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_014300.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-12-17T09:12:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6087",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6087#event-14300"
}
```
