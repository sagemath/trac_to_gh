# Issue 405: add setting of rows or columns to a matrix

archive/issues_000405.json:
```json
{
    "body": "Assignee: was\n\n\n```\nOn 7/26/07, David Joyner <wdjoyner@gmail.com> wrote:\n> On 7/26/07, mak <mak@math.uvic.ca> wrote:\n> > 1.  How do I change the entire row or column of a matrix at once?  In\n> > pari, I could do e.g. a=[1,2,3;4,5,6], and then put a[1,]=[0,0,0],\n> > which would give a=[0,0,0;4,5,6].  What's the sage equivalent?\n\nThere is no SAGE equivalent yet.  David's example might be helpful\nbelow though.  The best you could in SAGE is set each entry\none at a time right now.  I should add something.  \n\ndef set_row(A, r, v):\n    for i in range(A.ncols()):\n         A[r, i] = v[i]\n\nI'm not sure how we forgot to ever do this. \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/405\n\n",
    "created_at": "2007-07-26T15:23:45Z",
    "labels": [
        "algebraic geometry",
        "major",
        "enhancement"
    ],
    "title": "add setting of rows or columns to a matrix",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/405",
    "user": "was"
}
```
Assignee: was


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

archive/issue_comments_001987.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2007-07-26T15:23:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/405#issuecomment-1987",
    "user": "was"
}
```

Changing priority from major to minor.



---

archive/issue_comments_001988.json:
```json
{
    "body": "Changing component from algebraic geometry to linear algebra.",
    "created_at": "2007-07-26T15:23:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/405#issuecomment-1988",
    "user": "was"
}
```

Changing component from algebraic geometry to linear algebra.



---

archive/issue_comments_001989.json:
```json
{
    "body": "Attachment [405.patch](tarball://root/attachments/some-uuid/ticket405/405.patch) by mhansen created at 2007-12-22 17:10:22",
    "created_at": "2007-12-22T17:10:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/405#issuecomment-1989",
    "user": "mhansen"
}
```

Attachment [405.patch](tarball://root/attachments/some-uuid/ticket405/405.patch) by mhansen created at 2007-12-22 17:10:22



---

archive/issue_comments_001990.json:
```json
{
    "body": "Changing assignee from was to mhansen.",
    "created_at": "2007-12-22T17:10:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/405#issuecomment-1990",
    "user": "mhansen"
}
```

Changing assignee from was to mhansen.



---

archive/issue_comments_001991.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-22T17:10:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/405#issuecomment-1991",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_001992.json:
```json
{
    "body": "merged in 2.9.1 rc0",
    "created_at": "2007-12-22T18:00:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/405#issuecomment-1992",
    "user": "rlm"
}
```

merged in 2.9.1 rc0



---

archive/issue_comments_001993.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-22T18:00:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/405",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/405#issuecomment-1993",
    "user": "rlm"
}
```

Resolution: fixed
