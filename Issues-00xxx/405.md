# Issue 405: [with patch, positive referee] add setting of rows or columns to a matrix

archive/issues_000405.json:
```json
{
    "body": "Assignee: @mwhansen\n\n```\nOn 7/26/07, David Joyner <wdjoyner@gmail.com> wrote:\n> On 7/26/07, mak <mak@math.uvic.ca> wrote:\n> > 1.  How do I change the entire row or column of a matrix at once?  In\n> > pari, I could do e.g. a=[1,2,3;4,5,6], and then put a[1,]=[0,0,0],\n> > which would give a=[0,0,0;4,5,6].  What's the sage equivalent?\n\nThere is no SAGE equivalent yet.  David's example might be helpful\nbelow though.  The best you could in SAGE is set each entry\none at a time right now.  I should add something.  \n\ndef set_row(A, r, v):\n    for i in range(A.ncols()):\n         A[r, i] = v[i]\n\nI'm not sure how we forgot to ever do this. \n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/405\n\n",
    "closed_at": "2007-12-22T18:00:46Z",
    "created_at": "2007-07-26T15:23:45Z",
    "labels": [
        "component: linear algebra",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9.1",
    "title": "[with patch, positive referee] add setting of rows or columns to a matrix",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/405",
    "user": "https://github.com/williamstein"
}
```
Assignee: @mwhansen

```
On 7/26/07, David Joyner <wdjoyner@gmail.com> wrote:
> On 7/26/07, mak <mak@math.uvic.ca> wrote:
> > 1.  How do I change the entire row or column of a matrix at once?  In
> > pari, I could do e.g. a=[1,2,3;4,5,6], and then put a[1,]=[0,0,0],
> > which would give a=[0,0,0;4,5,6].  What's the sage equivalent?

There is no SAGE equivalent yet.  David's example might be helpful
below though.  The best you could in SAGE is set each entry
one at a time right now.  I should add something.  

def set_row(A, r, v):
    for i in range(A.ncols()):
         A[r, i] = v[i]

I'm not sure how we forgot to ever do this. 
```

Issue created by migration from https://trac.sagemath.org/ticket/405





---

archive/issue_comments_001978.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2007-07-26T15:23:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/405#issuecomment-1978",
    "user": "https://github.com/williamstein"
}
```

Changing priority from major to minor.



---

archive/issue_comments_001979.json:
```json
{
    "body": "Changing component from algebraic geometry to linear algebra.",
    "created_at": "2007-07-26T15:23:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/405#issuecomment-1979",
    "user": "https://github.com/williamstein"
}
```

Changing component from algebraic geometry to linear algebra.



---

archive/issue_events_000972.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-19T11:06:32Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/405",
    "milestone": "sage-2.9.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/405#event-972"
}
```



---

archive/issue_comments_001980.json:
```json
{
    "body": "Attachment [405.patch](tarball://root/attachments/some-uuid/ticket405/405.patch) by @mwhansen created at 2007-12-22 17:10:22",
    "created_at": "2007-12-22T17:10:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/405#issuecomment-1980",
    "user": "https://github.com/mwhansen"
}
```

Attachment [405.patch](tarball://root/attachments/some-uuid/ticket405/405.patch) by @mwhansen created at 2007-12-22 17:10:22



---

archive/issue_comments_001981.json:
```json
{
    "body": "Changing assignee from @williamstein to @mwhansen.",
    "created_at": "2007-12-22T17:10:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/405#issuecomment-1981",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @williamstein to @mwhansen.



---

archive/issue_comments_001982.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-22T17:10:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/405#issuecomment-1982",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_events_000973.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2007-12-22T18:00:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/405",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/405#event-973"
}
```



---

archive/issue_comments_001983.json:
```json
{
    "body": "merged in 2.9.1 rc0",
    "created_at": "2007-12-22T18:00:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/405#issuecomment-1983",
    "user": "https://github.com/rlmill"
}
```

merged in 2.9.1 rc0



---

archive/issue_comments_001984.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-22T18:00:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/405#issuecomment-1984",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
