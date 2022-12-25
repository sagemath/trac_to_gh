# Issue 4706: fix race condition between doctest creation and running

archive/issues_004706.json:
```json
{
    "body": "Assignee: mabshoff\n\nWith high -tp numbers (i.e. 16) on sage.math one will see similar issues to the one below:\n\n```\nsage -t -long devel/sage/sage/libs/symmetrica/symmetrica.pyx\n  File \"/scratch/mabshoff/release-cycle/sage-3.2.alpha0/tmp/.doctest_symmetrica.py\", line 29\n    >>> test_integer(Integer(1))###line 539:_sage_    >>> test_integer(1)\n    ^\nIndentationError: unexpected indent\n```\n\n\nThis is likely a race condition between creating the file running the doctest. The issue is not specific to -tp. \n\nA potential solution might be to create all .doctest_$FOO files and then start running them. This might also fix the problem with \n\n```\nsage -t -long devel/sage/sage/symbolic/constants.pyx\n\t [0.1 s]\n```\n\nin Sage 3.2.1+ which is caused by no doctests being executed since (a) either there are no doctests in that file or (b) we are running optional doctests only.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4706\n\n",
    "created_at": "2008-12-05T01:37:01Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "fix race condition between doctest creation and running",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4706",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

With high -tp numbers (i.e. 16) on sage.math one will see similar issues to the one below:

```
sage -t -long devel/sage/sage/libs/symmetrica/symmetrica.pyx
  File "/scratch/mabshoff/release-cycle/sage-3.2.alpha0/tmp/.doctest_symmetrica.py", line 29
    >>> test_integer(Integer(1))###line 539:_sage_    >>> test_integer(1)
    ^
IndentationError: unexpected indent
```


This is likely a race condition between creating the file running the doctest. The issue is not specific to -tp. 

A potential solution might be to create all .doctest_$FOO files and then start running them. This might also fix the problem with 

```
sage -t -long devel/sage/sage/symbolic/constants.pyx
	 [0.1 s]
```

in Sage 3.2.1+ which is caused by no doctests being executed since (a) either there are no doctests in that file or (b) we are running optional doctests only.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4706





---

archive/issue_comments_035426.json:
```json
{
    "body": "Attachment [trac_4706-scripts-repo.patch](tarball://root/attachments/some-uuid/ticket4706/trac_4706-scripts-repo.patch) by @koffie created at 2011-08-23 21:09:08\n\nI think this is an old ticket which can be closed and has been fixed in the mean time. At least during the parralel builds I did (and I did quite a few this sage days already) I never saw this message.",
    "created_at": "2011-08-23T21:09:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4706#issuecomment-35426",
    "user": "https://github.com/koffie"
}
```

Attachment [trac_4706-scripts-repo.patch](tarball://root/attachments/some-uuid/ticket4706/trac_4706-scripts-repo.patch) by @koffie created at 2011-08-23 21:09:08

I think this is an old ticket which can be closed and has been fixed in the mean time. At least during the parralel builds I did (and I did quite a few this sage days already) I never saw this message.



---

archive/issue_comments_035427.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-08-23T21:09:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4706#issuecomment-35427",
    "user": "https://github.com/koffie"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_035428.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2011-12-17T20:46:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4706#issuecomment-35428",
    "user": "https://github.com/mwhansen"
}
```

Resolution: invalid



---

archive/issue_events_004951.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2011-12-17T20:46:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4706",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4706#event-4951"
}
```



---

archive/issue_comments_035429.json:
```json
{
    "body": "I tihnk this can be closed as well.",
    "created_at": "2011-12-17T20:46:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4706",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4706#issuecomment-35429",
    "user": "https://github.com/mwhansen"
}
```

I tihnk this can be closed as well.
