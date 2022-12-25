# Issue 9307: delete GHMM standard spkg from Sage

archive/issues_009307.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  @rlmill\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9307\n\n",
    "created_at": "2010-06-22T13:18:21Z",
    "labels": [
        "component: build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "delete GHMM standard spkg from Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9307",
    "user": "https://github.com/williamstein"
}
```
Assignee: GeorgSWeber

CC:  @rlmill



Issue created by migration from https://trac.sagemath.org/ticket/9307





---

archive/issue_comments_087513.json:
```json
{
    "body": "I think we can resolve this as \"fixed.\"  For 4.4.4, 4.5.alpha0, and 4.5.alpha1, I get\n\n```sh\n$ cd SAGE_ROOT\n$ grep -i ghmm spkg/install spkg/standard/deps\n$ find | grep -i ghmm\n$\n```\n",
    "created_at": "2010-06-29T21:27:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9307#issuecomment-87513",
    "user": "https://github.com/qed777"
}
```

I think we can resolve this as "fixed."  For 4.4.4, 4.5.alpha0, and 4.5.alpha1, I get

```sh
$ cd SAGE_ROOT
$ grep -i ghmm spkg/install spkg/standard/deps
$ find | grep -i ghmm
$
```




---

archive/issue_comments_087514.json:
```json
{
    "body": "William did this a while ago without closing the ticket. We should figure out what the right milestone is.",
    "created_at": "2010-07-01T17:10:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9307#issuecomment-87514",
    "user": "https://github.com/rlmill"
}
```

William did this a while ago without closing the ticket. We should figure out what the right milestone is.



---

archive/issue_comments_087515.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-01T17:10:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9307",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9307#issuecomment-87515",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
