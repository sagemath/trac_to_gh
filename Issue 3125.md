# Issue 3125: chromatic_polynomial incorrectly blocks control-c

archive/issues_003125.json:
```json
{
    "body": "Assignee: mhansen\n\nTry this:\n\n```\nsage: graphs.CubeGraph(5).chromatic_polynomial()\n[control-c]\n```\n\n\ncontrol-c is ignored.  Probably somebody doesn't understand _sig_on/_sig_off!\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3125\n\n",
    "created_at": "2008-05-07T16:14:33Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.2",
    "title": "chromatic_polynomial incorrectly blocks control-c",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3125",
    "user": "was"
}
```
Assignee: mhansen

Try this:

```
sage: graphs.CubeGraph(5).chromatic_polynomial()
[control-c]
```


control-c is ignored.  Probably somebody doesn't understand _sig_on/_sig_off!




Issue created by migration from https://trac.sagemath.org/ticket/3125





---

archive/issue_comments_021655.json:
```json
{
    "body": "Changing assignee from mhansen to rlm.",
    "created_at": "2008-05-07T17:46:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3125#issuecomment-21655",
    "user": "rlm"
}
```

Changing assignee from mhansen to rlm.



---

archive/issue_comments_021656.json:
```json
{
    "body": "Attachment [trac3125-chrompoly_sig.patch](tarball://root/attachments/some-uuid/ticket3125/trac3125-chrompoly_sig.patch) by rlm created at 2008-05-07 23:22:01\n\nAfter attached patch:\n\n```\nsage: graphs.CubeGraph(5).chromatic_polynomial()\n^C---------------------------------------------------------------------------\n<type 'exceptions.KeyboardInterrupt'>     Traceback (most recent call last)\n\n/Users/rlmill/sage-3.0.1/<ipython console> in <module>()\n\n/Users/rlmill/sage-3.0.1/local/lib/python/site-packages/sage/graphs/graph.py in chromatic_polynomial(self)\n   7099         \"\"\"\n   7100         from sage.graphs.chrompoly import chromatic_polynomial\n-> 7101         return chromatic_polynomial(self)\n   7102 \n   7103     def chromatic_number(self):\n\n<type 'exceptions.KeyboardInterrupt'>: \n```\n",
    "created_at": "2008-05-07T23:22:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3125#issuecomment-21656",
    "user": "rlm"
}
```

Attachment [trac3125-chrompoly_sig.patch](tarball://root/attachments/some-uuid/ticket3125/trac3125-chrompoly_sig.patch) by rlm created at 2008-05-07 23:22:01

After attached patch:

```
sage: graphs.CubeGraph(5).chromatic_polynomial()
^C---------------------------------------------------------------------------
<type 'exceptions.KeyboardInterrupt'>     Traceback (most recent call last)

/Users/rlmill/sage-3.0.1/<ipython console> in <module>()

/Users/rlmill/sage-3.0.1/local/lib/python/site-packages/sage/graphs/graph.py in chromatic_polynomial(self)
   7099         """
   7100         from sage.graphs.chrompoly import chromatic_polynomial
-> 7101         return chromatic_polynomial(self)
   7102 
   7103     def chromatic_number(self):

<type 'exceptions.KeyboardInterrupt'>: 
```




---

archive/issue_comments_021657.json:
```json
{
    "body": "Patch is good.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-11T10:41:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3125#issuecomment-21657",
    "user": "mabshoff"
}
```

Patch is good.

Cheers,

Michael



---

archive/issue_comments_021658.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-11T10:43:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3125#issuecomment-21658",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_021659.json:
```json
{
    "body": "Merged in Sage 3.0.2.alpha0",
    "created_at": "2008-05-11T10:43:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3125#issuecomment-21659",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.2.alpha0
