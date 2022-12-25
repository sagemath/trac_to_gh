# Issue 4374: Numerical noise doctest failure in sage/tests/book_stein_ent.py

archive/issues_004374.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @craigcitro\n\n\n```\nsage -t  devel/sage/sage/tests/book_stein_ent.py \n********************************************************************** \nFile \"/local/jec/sage-3.1.4/tmp/book_stein_ent.py\", line 5056: \n    : g2.complex_embedding() \nExpected: \n    -2.2360679775 + 3.33066907388e-16*I \nGot: \n    -2.2360679775 + 3.83970199386e-16*I \n********************************************************************** \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4374\n\n",
    "created_at": "2008-10-27T17:12:43Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "Numerical noise doctest failure in sage/tests/book_stein_ent.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4374",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

CC:  @craigcitro


```
sage -t  devel/sage/sage/tests/book_stein_ent.py 
********************************************************************** 
File "/local/jec/sage-3.1.4/tmp/book_stein_ent.py", line 5056: 
    : g2.complex_embedding() 
Expected: 
    -2.2360679775 + 3.33066907388e-16*I 
Got: 
    -2.2360679775 + 3.83970199386e-16*I 
********************************************************************** 
```


Issue created by migration from https://trac.sagemath.org/ticket/4374





---

archive/issue_comments_032101.json:
```json
{
    "body": "On an Itanium I am seeing the following numerical results:\n\n```\nsage -t  devel/sage/sage/tests/book_stein_ent.py            \n**********************************************************************\nFile \"/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-cleo/tmp/book_stein_ent.py\", line 5056:\n    : g2.complex_embedding()\nExpected:\n    -2.2360679775 + 3.33066907388e-16*I\nGot:\n    -2.2360679775 + 5.38810057558e-16*I\n**********************************************************************\n```\n",
    "created_at": "2008-10-27T17:15:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4374#issuecomment-32101",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

On an Itanium I am seeing the following numerical results:

```
sage -t  devel/sage/sage/tests/book_stein_ent.py            
**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-cleo/tmp/book_stein_ent.py", line 5056:
    : g2.complex_embedding()
Expected:
    -2.2360679775 + 3.33066907388e-16*I
Got:
    -2.2360679775 + 5.38810057558e-16*I
**********************************************************************
```




---

archive/issue_comments_032102.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-27T17:15:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4374#issuecomment-32102",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_032103.json:
```json
{
    "body": "And from a G5 running OSX 10.4:\n\n```\nsage -t  devel/sage/sage/tests/book_stein_ent.py            \n**********************************************************************\nFile \"/Users/mabshoff/sage-3.2.alpha1/tmp/book_stein_ent.py\", line 5056:\n    : g2.complex_embedding()\nExpected:\n    -2.2360679775 + 3.33066907388e-16*I\nGot:\n    -2.2360679775 + 5.38810057558e-16*I\n**********************************************************************\n```\n",
    "created_at": "2008-10-27T18:07:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4374#issuecomment-32103",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

And from a G5 running OSX 10.4:

```
sage -t  devel/sage/sage/tests/book_stein_ent.py            
**********************************************************************
File "/Users/mabshoff/sage-3.2.alpha1/tmp/book_stein_ent.py", line 5056:
    : g2.complex_embedding()
Expected:
    -2.2360679775 + 3.33066907388e-16*I
Got:
    -2.2360679775 + 5.38810057558e-16*I
**********************************************************************
```




---

archive/issue_comments_032104.json:
```json
{
    "body": "Craig,\n\nsince William mentioned you were cleaning up those files feel free to take ownership here.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-27T18:14:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4374#issuecomment-32104",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Craig,

since William mentioned you were cleaning up those files feel free to take ownership here.

Cheers,

Michael



---

archive/issue_comments_032105.json:
```json
{
    "body": "Changing assignee from mabshoff to @craigcitro.",
    "created_at": "2008-10-27T19:47:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4374#issuecomment-32105",
    "user": "https://github.com/craigcitro"
}
```

Changing assignee from mabshoff to @craigcitro.



---

archive/issue_comments_032106.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2008-10-27T19:47:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4374#issuecomment-32106",
    "user": "https://github.com/craigcitro"
}
```

Changing status from assigned to new.



---

archive/issue_comments_032107.json:
```json
{
    "body": "Attachment [trac-4374.patch](tarball://root/attachments/some-uuid/ticket4374/trac-4374.patch) by @craigcitro created at 2008-10-27 19:47:28\n\nThe attached patch fixes the above issues, as well as cleaning up the files `book_stein_ent.py` and `book_stein_modform.py`. I'll keep an eye out for any new numerical noise that pops up during testing ...",
    "created_at": "2008-10-27T19:47:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4374#issuecomment-32107",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-4374.patch](tarball://root/attachments/some-uuid/ticket4374/trac-4374.patch) by @craigcitro created at 2008-10-27 19:47:28

The attached patch fixes the above issues, as well as cleaning up the files `book_stein_ent.py` and `book_stein_modform.py`. I'll keep an eye out for any new numerical noise that pops up during testing ...



---

archive/issue_comments_032108.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-27T19:47:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4374#issuecomment-32108",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_032109.json:
```json
{
    "body": "Positive review. Tests pass on Itanium and the G5. All the other changes look good, too, and also take care of the coverage problem.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-27T20:04:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4374#issuecomment-32109",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review. Tests pass on Itanium and the G5. All the other changes look good, too, and also take care of the coverage problem.

Cheers,

Michael



---

archive/issue_events_004619.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-10-27T20:05:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4374",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4374#event-4619"
}
```



---

archive/issue_comments_032110.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-27T20:05:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4374#issuecomment-32110",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_032111.json:
```json
{
    "body": "Merged in Sage 3.2.alpha2",
    "created_at": "2008-10-27T20:05:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4374#issuecomment-32111",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.alpha2
