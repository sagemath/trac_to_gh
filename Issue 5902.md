# Issue 5902: [with patch, needs review] Try SAGE_ROOT as base of argument to "sage -t"

archive/issues_005902.json:
```json
{
    "body": "Assignee: mabshoff\n\nRunning\n\n```\nsage -t devel/sage/sage/rings/polynomial/pbori.pyx\n```\n\nseems to not work for me sometimes when the current working directory is not SAGE_ROOT.  I don't really understand what is going wrong here, since there is a \"cd\" in $SAGE_ROOT/sage, but I've heard other people complain about issues with this.\n\nThe attached patch caused the problems to go away for me.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5902\n\n",
    "created_at": "2009-04-26T05:51:28Z",
    "labels": [
        "doctest coverage",
        "minor",
        "enhancement"
    ],
    "title": "[with patch, needs review] Try SAGE_ROOT as base of argument to \"sage -t\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5902",
    "user": "tabbott"
}
```
Assignee: mabshoff

Running

```
sage -t devel/sage/sage/rings/polynomial/pbori.pyx
```

seems to not work for me sometimes when the current working directory is not SAGE_ROOT.  I don't really understand what is going wrong here, since there is a "cd" in $SAGE_ROOT/sage, but I've heard other people complain about issues with this.

The attached patch caused the problems to go away for me.

Issue created by migration from https://trac.sagemath.org/ticket/5902





---

archive/issue_comments_046651.json:
```json
{
    "body": "Changing assignee from mabshoff to mhansen.",
    "created_at": "2009-06-20T01:57:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5902#issuecomment-46651",
    "user": "mhansen"
}
```

Changing assignee from mabshoff to mhansen.



---

archive/issue_comments_046652.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-20T01:57:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5902#issuecomment-46652",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_046653.json:
```json
{
    "body": "Attachment\n\nLooks good to me!",
    "created_at": "2009-06-20T01:57:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5902#issuecomment-46653",
    "user": "mhansen"
}
```

Attachment

Looks good to me!



---

archive/issue_comments_046654.json:
```json
{
    "body": "> Running\n>\n> sage -t devel/sage/sage/rings/polynomial/pbori.pyx\n>\n> seems to not work for me sometimes when the current working directory is not SAGE_ROOT.\n\nIt should not work.  \"sage -t\" is supposed to take the path to a file.  If you're not in SAGE_ROOT, then devel/sage/sage/rings/polynomial/pbori.pyx is not a file.  It's like with any other unix command.  E.g., you wouldn't expect \n\n```\ncat devel/sage/sage/rings/polynomial/pbori.pyx\n```\n\nto magically work if you're not in SAGE_ROOT.\n\nNote that Mike Hansen just gave this a positive review.  I strongly disagree.",
    "created_at": "2009-06-20T14:44:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5902#issuecomment-46654",
    "user": "was"
}
```

> Running
>
> sage -t devel/sage/sage/rings/polynomial/pbori.pyx
>
> seems to not work for me sometimes when the current working directory is not SAGE_ROOT.

It should not work.  "sage -t" is supposed to take the path to a file.  If you're not in SAGE_ROOT, then devel/sage/sage/rings/polynomial/pbori.pyx is not a file.  It's like with any other unix command.  E.g., you wouldn't expect 

```
cat devel/sage/sage/rings/polynomial/pbori.pyx
```

to magically work if you're not in SAGE_ROOT.

Note that Mike Hansen just gave this a positive review.  I strongly disagree.



---

archive/issue_comments_046655.json:
```json
{
    "body": "Hi William,\n\nMy motivation for this change was that when you run \"sage -testall\", for each test it prints out what it is running as \n\nsage -t devel/sage/sage/rings/polynomial/pbori.py\n\nsince $SAGE_ROOT/sage changes directory to SAGE_ROOT before proceeding.\n\nSo that if you copy-and-paste that output from \"sage -testall\" to run the test a second time, it doesn't work.",
    "created_at": "2009-06-20T15:33:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5902#issuecomment-46655",
    "user": "tabbott"
}
```

Hi William,

My motivation for this change was that when you run "sage -testall", for each test it prints out what it is running as 

sage -t devel/sage/sage/rings/polynomial/pbori.py

since $SAGE_ROOT/sage changes directory to SAGE_ROOT before proceeding.

So that if you copy-and-paste that output from "sage -testall" to run the test a second time, it doesn't work.



---

archive/issue_comments_046656.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-26T17:46:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5902",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5902#issuecomment-46656",
    "user": "boothby"
}
```

Resolution: fixed
