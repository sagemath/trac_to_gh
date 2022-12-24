# Issue 5927: [with patch; needs review] singular prompt problem on solaris sparc

archive/issues_005927.json:
```json
{
    "body": "Assignee: mabshoff\n\nCredit to William Stein, Mike Hansen, and Michael Abshoff?\n\nIssue created by migration from https://trac.sagemath.org/ticket/5927\n\n",
    "created_at": "2009-04-29T01:36:52Z",
    "labels": [
        "porting",
        "blocker",
        "bug"
    ],
    "title": "[with patch; needs review] singular prompt problem on solaris sparc",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5927",
    "user": "was"
}
```
Assignee: mabshoff

Credit to William Stein, Mike Hansen, and Michael Abshoff?

Issue created by migration from https://trac.sagemath.org/ticket/5927





---

archive/issue_comments_046857.json:
```json
{
    "body": "I tested it, and it works.",
    "created_at": "2009-04-29T01:40:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5927#issuecomment-46857",
    "user": "was"
}
```

I tested it, and it works.



---

archive/issue_comments_046858.json:
```json
{
    "body": "Oops, there are three doctest failures with this patch applied:\n\n```\n        sage -t -long devel/sage/sage/interfaces/expect.py # 1 doctests failed\n        sage -t -long devel/sage/doc/en/developer/coding_in_other.rst # 2 doctests failed\n        sage -t -long devel/sage/doc/en/constructions/algebraic_geometry.rst # 4 doctests failed\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-04-29T23:00:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5927#issuecomment-46858",
    "user": "mabshoff"
}
```

Oops, there are three doctest failures with this patch applied:

```
        sage -t -long devel/sage/sage/interfaces/expect.py # 1 doctests failed
        sage -t -long devel/sage/doc/en/developer/coding_in_other.rst # 2 doctests failed
        sage -t -long devel/sage/doc/en/constructions/algebraic_geometry.rst # 4 doctests failed
```


Cheers,

Michael



---

archive/issue_comments_046859.json:
```json
{
    "body": "This is a 4.0 blocker. \n\nMike: Any comments?\n\nCheers,\n\nMichael",
    "created_at": "2009-05-15T14:33:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5927#issuecomment-46859",
    "user": "mabshoff"
}
```

This is a 4.0 blocker. 

Mike: Any comments?

Cheers,

Michael



---

archive/issue_comments_046860.json:
```json
{
    "body": "Attachment [trac_5927.patch](tarball://root/attachments/some-uuid/ticket5927/trac_5927.patch) by mhansen created at 2009-05-21 17:54:09",
    "created_at": "2009-05-21T17:54:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5927#issuecomment-46860",
    "user": "mhansen"
}
```

Attachment [trac_5927.patch](tarball://root/attachments/some-uuid/ticket5927/trac_5927.patch) by mhansen created at 2009-05-21 17:54:09



---

archive/issue_comments_046861.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-21T17:56:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5927#issuecomment-46861",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_046862.json:
```json
{
    "body": "All of the failures are harmless.  I've attached a new patch which fixes the doctests.",
    "created_at": "2009-05-21T17:56:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5927#issuecomment-46862",
    "user": "mhansen"
}
```

All of the failures are harmless.  I've attached a new patch which fixes the doctests.



---

archive/issue_comments_046863.json:
```json
{
    "body": "Changing assignee from mabshoff to mhansen.",
    "created_at": "2009-05-21T17:56:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5927#issuecomment-46863",
    "user": "mhansen"
}
```

Changing assignee from mabshoff to mhansen.



---

archive/issue_comments_046864.json:
```json
{
    "body": "Hmm, I am not so sure the patch does fix every problem:\nWithout the patch:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: singular.eval(\"intvec G = 4,4,4,0,0,0;\")\n''\n```\n\nWith the patch applied:\n\n```\nmabshoff@sage:/scratch/mabshoff/sage-4.0.rc1$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: singular.eval(\"intvec G = 4,4,4,0,0,0;\")\n'intvec G = 4,4,4,0,0,0;'\nsage: \n```\n\n| Sage Version 4.0.rc0, Release Date: 2009-05-21                     |\n| Type notebook() for the GUI, and license() for information.        |\n| Sage Version 4.0.rc0, Release Date: 2009-05-21                     |\n| Type notebook() for the GUI, and license() for information.        |\nIf you look at the attached patch here it seems that we sometimes get the echo of the command and some times not. It might be consistent, i.e. the doctests pass on all platforms (I hope), but something still seems fishy.\n\nI am not saying we shouldn't apply the patch since it fixes a much more severe bug, I just think that there is more to the story. Anyway, doctests do pass, so I will open a followup ticket and merge this patch.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-22T12:49:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5927#issuecomment-46864",
    "user": "mabshoff"
}
```

Hmm, I am not so sure the patch does fix every problem:
Without the patch:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: singular.eval("intvec G = 4,4,4,0,0,0;")
''
```

With the patch applied:

```
mabshoff@sage:/scratch/mabshoff/sage-4.0.rc1$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: singular.eval("intvec G = 4,4,4,0,0,0;")
'intvec G = 4,4,4,0,0,0;'
sage: 
```

| Sage Version 4.0.rc0, Release Date: 2009-05-21                     |
| Type notebook() for the GUI, and license() for information.        |
| Sage Version 4.0.rc0, Release Date: 2009-05-21                     |
| Type notebook() for the GUI, and license() for information.        |
If you look at the attached patch here it seems that we sometimes get the echo of the command and some times not. It might be consistent, i.e. the doctests pass on all platforms (I hope), but something still seems fishy.

I am not saying we shouldn't apply the patch since it fixes a much more severe bug, I just think that there is more to the story. Anyway, doctests do pass, so I will open a followup ticket and merge this patch.

Cheers,

Michael



---

archive/issue_comments_046865.json:
```json
{
    "body": "Merged in Sage 4.0.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-22T13:17:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5927#issuecomment-46865",
    "user": "mabshoff"
}
```

Merged in Sage 4.0.rc1.

Cheers,

Michael



---

archive/issue_comments_046866.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-22T13:17:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5927",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5927#issuecomment-46866",
    "user": "mabshoff"
}
```

Resolution: fixed
