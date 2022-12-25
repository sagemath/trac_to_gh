# Issue 3212: Improving rescaling of matrices

archive/issues_003212.json:
```json
{
    "body": "Assignee: @williamstein\n\nCurrently, rescale_row and rescale_col don't allow you to rescale by something mathematically right but outside the current matrix base ring.  Discussion from sage-devel follows.\n\n> Under the current scaling code, this happens: \n> sage: N.rescale_col(2,i/2) \n> --------------------------------------------------------------------------- \n> <type 'exceptions.TypeError'>             Traceback (most recent call \n> last) \n> <snip> \n> <type 'exceptions.TypeError'>: unable to convert I/2 to a rational \n\n\nYep, this is orthogonal.  You're just suggesting that scale_row \nbe improved. \n> What I am wondering is whether throwing an exception of TypeError \n> under the current code should be replaced by a try statement first \n> attempting N.changering(??) . The problem is I have no idea what to \n> use for ??, because unfortunately i/2 lives in Symbolic Ring, not in \n> CC, so I can't just put in ??=parent(i/2). \n\n\nThe Sequence constructor is the canonical answer to this question. \nGiven any list v of Sage object it will find a canonical place to put \nthem all: \nsage: v = [3, I/2] \nsage: w = Sequence(v) \nsage: w \n[3, I/2] \nsage: w.universe() \nSymbolic Ring\n\nIssue created by migration from https://trac.sagemath.org/ticket/3212\n\n",
    "created_at": "2008-05-15T16:31:37Z",
    "labels": [
        "component: linear algebra",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.3",
    "title": "Improving rescaling of matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3212",
    "user": "https://github.com/kcrisman"
}
```
Assignee: @williamstein

Currently, rescale_row and rescale_col don't allow you to rescale by something mathematically right but outside the current matrix base ring.  Discussion from sage-devel follows.

> Under the current scaling code, this happens: 
> sage: N.rescale_col(2,i/2) 
> --------------------------------------------------------------------------- 
> <type 'exceptions.TypeError'>             Traceback (most recent call 
> last) 
> <snip> 
> <type 'exceptions.TypeError'>: unable to convert I/2 to a rational 


Yep, this is orthogonal.  You're just suggesting that scale_row 
be improved. 
> What I am wondering is whether throwing an exception of TypeError 
> under the current code should be replaced by a try statement first 
> attempting N.changering(??) . The problem is I have no idea what to 
> use for ??, because unfortunately i/2 lives in Symbolic Ring, not in 
> CC, so I can't just put in ??=parent(i/2). 


The Sequence constructor is the canonical answer to this question. 
Given any list v of Sage object it will find a canonical place to put 
them all: 
sage: v = [3, I/2] 
sage: w = Sequence(v) 
sage: w 
[3, I/2] 
sage: w.universe() 
Symbolic Ring

Issue created by migration from https://trac.sagemath.org/ticket/3212





---

archive/issue_comments_022174.json:
```json
{
    "body": "This is a first try at a patch improving documentation and removing the problem.",
    "created_at": "2008-05-16T05:21:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3212#issuecomment-22174",
    "user": "https://github.com/kcrisman"
}
```

This is a first try at a patch improving documentation and removing the problem.



---

archive/issue_comments_022175.json:
```json
{
    "body": "Attachment [8867.patch](tarball://root/attachments/some-uuid/ticket3212/8867.patch) by @kcrisman created at 2008-05-16 05:23:22\n\nI should point out that the above patch does not yet work.  It DOES remove the TypeError problem, but doesn't actually give the correct new matrix.",
    "created_at": "2008-05-16T05:23:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3212#issuecomment-22175",
    "user": "https://github.com/kcrisman"
}
```

Attachment [8867.patch](tarball://root/attachments/some-uuid/ticket3212/8867.patch) by @kcrisman created at 2008-05-16 05:23:22

I should point out that the above patch does not yet work.  It DOES remove the TypeError problem, but doesn't actually give the correct new matrix.



---

archive/issue_comments_022176.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-16T05:23:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3212#issuecomment-22176",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to assigned.



---

archive/issue_comments_022177.json:
```json
{
    "body": "Changing assignee from @williamstein to @kcrisman.",
    "created_at": "2008-05-16T05:23:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3212#issuecomment-22177",
    "user": "https://github.com/kcrisman"
}
```

Changing assignee from @williamstein to @kcrisman.



---

archive/issue_comments_022178.json:
```json
{
    "body": "Attachment [8869.patch](tarball://root/attachments/some-uuid/ticket3212/8869.patch) by @kcrisman created at 2008-05-18 03:33:08\n\nPatch for allowing row mult by non-ring elements",
    "created_at": "2008-05-18T03:33:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3212#issuecomment-22178",
    "user": "https://github.com/kcrisman"
}
```

Attachment [8869.patch](tarball://root/attachments/some-uuid/ticket3212/8869.patch) by @kcrisman created at 2008-05-18 03:33:08

Patch for allowing row mult by non-ring elements



---

archive/issue_comments_022179.json:
```json
{
    "body": "The patch 8869 replaces patch 8867.  \n\nIt allows multiplication of rows/columns of matrices by elements of extensions of the base rings, at the cost of (only in those cases) returning a copy, not changing the original.  \n\nThis also adds extra examples and documentation, as well as a set_col_to_multiple_of_col attribute to match set_row_to_multiple_of_row .",
    "created_at": "2008-05-18T03:39:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3212#issuecomment-22179",
    "user": "https://github.com/kcrisman"
}
```

The patch 8869 replaces patch 8867.  

It allows multiplication of rows/columns of matrices by elements of extensions of the base rings, at the cost of (only in those cases) returning a copy, not changing the original.  

This also adds extra examples and documentation, as well as a set_col_to_multiple_of_col attribute to match set_row_to_multiple_of_row .



---

archive/issue_comments_022180.json:
```json
{
    "body": "It should probably always return a matrix (for consistency), even when copying is not required.",
    "created_at": "2008-05-18T06:04:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3212#issuecomment-22180",
    "user": "https://github.com/robertwb"
}
```

It should probably always return a matrix (for consistency), even when copying is not required.



---

archive/issue_comments_022181.json:
```json
{
    "body": "I have to remove my test function, and also want feedback on Robert's comment.",
    "created_at": "2008-05-20T01:50:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3212#issuecomment-22181",
    "user": "https://github.com/kcrisman"
}
```

I have to remove my test function, and also want feedback on Robert's comment.



---

archive/issue_comments_022182.json:
```json
{
    "body": "Improves documentation and error messages and adds alternate methods for rescaling of matrices",
    "created_at": "2008-06-06T03:06:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3212#issuecomment-22182",
    "user": "https://github.com/kcrisman"
}
```

Improves documentation and error messages and adds alternate methods for rescaling of matrices



---

archive/issue_comments_022183.json:
```json
{
    "body": "Attachment [rescaling.patch](tarball://root/attachments/some-uuid/ticket3212/rescaling.patch) by @kcrisman created at 2008-06-06 03:12:13\n\nUse only rescaling.patch.",
    "created_at": "2008-06-06T03:12:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3212#issuecomment-22183",
    "user": "https://github.com/kcrisman"
}
```

Attachment [rescaling.patch](tarball://root/attachments/some-uuid/ticket3212/rescaling.patch) by @kcrisman created at 2008-06-06 03:12:13

Use only rescaling.patch.



---

archive/issue_comments_022184.json:
```json
{
    "body": "Works well for me. The only comments I have are \n\n- (nitpicky) with_rescale_row -> with_rescaled_row (sounds better to me)\n\n- Do not just print out an error message, actually raise a TypeError (with an explanatory error message, though preferably without line breaks at 58 characters).",
    "created_at": "2008-06-06T16:36:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3212#issuecomment-22184",
    "user": "https://github.com/robertwb"
}
```

Works well for me. The only comments I have are 

- (nitpicky) with_rescale_row -> with_rescaled_row (sounds better to me)

- Do not just print out an error message, actually raise a TypeError (with an explanatory error message, though preferably without line breaks at 58 characters).



---

archive/issue_comments_022185.json:
```json
{
    "body": "Attachment [rescale.patch](tarball://root/attachments/some-uuid/ticket3212/rescale.patch) by @kcrisman created at 2008-06-06 21:04:18\n\nUse only rescale.patch.  This is hopefully the final version.",
    "created_at": "2008-06-06T21:04:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3212#issuecomment-22185",
    "user": "https://github.com/kcrisman"
}
```

Attachment [rescale.patch](tarball://root/attachments/some-uuid/ticket3212/rescale.patch) by @kcrisman created at 2008-06-06 21:04:18

Use only rescale.patch.  This is hopefully the final version.



---

archive/issue_comments_022186.json:
```json
{
    "body": "Thanks. Works great.",
    "created_at": "2008-06-07T00:09:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3212#issuecomment-22186",
    "user": "https://github.com/robertwb"
}
```

Thanks. Works great.



---

archive/issue_comments_022187.json:
```json
{
    "body": "Merged rescale.patch in Sage 3.0.3.alpha2",
    "created_at": "2008-06-09T06:45:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3212#issuecomment-22187",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged rescale.patch in Sage 3.0.3.alpha2



---

archive/issue_comments_022188.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-09T06:45:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3212#issuecomment-22188",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003429.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-06-09T06:45:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3212",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3212#event-3429"
}
```
