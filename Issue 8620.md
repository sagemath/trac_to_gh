# Issue 8620: Rogue minus sign in sage.modular.modsym.ambient.diamond_bracket_operator

archive/issues_008620.json:
```json
{
    "body": "Assignee: @craigcitro\n\nKeywords: modular symbols\n\nThere is a minus sign in the code for diamond operators which shouldn't be there; what actually gets returned is the diamond operator times the star involution! In particular, ```< 1 >``` really ought to be the identity map. This patch corrects the error and adds a doctest to prove it. (This is needed for some code I wrote with Jared Weinstein at the 2010 Montreal conference, in which it's really vital to work with sign 0 symbols.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/8620\n\n",
    "created_at": "2010-03-28T21:46:38Z",
    "labels": [
        "component: modular forms",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "Rogue minus sign in sage.modular.modsym.ambient.diamond_bracket_operator",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8620",
    "user": "https://github.com/loefflerd"
}
```
Assignee: @craigcitro

Keywords: modular symbols

There is a minus sign in the code for diamond operators which shouldn't be there; what actually gets returned is the diamond operator times the star involution! In particular, ```< 1 >``` really ought to be the identity map. This patch corrects the error and adds a doctest to prove it. (This is needed for some code I wrote with Jared Weinstein at the 2010 Montreal conference, in which it's really vital to work with sign 0 symbols.)

Issue created by migration from https://trac.sagemath.org/ticket/8620





---

archive/issue_comments_077985.json:
```json
{
    "body": "patch against 4.3.4",
    "created_at": "2010-03-28T21:53:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8620#issuecomment-77985",
    "user": "https://github.com/loefflerd"
}
```

patch against 4.3.4



---

archive/issue_comments_077986.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-28T22:02:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8620#issuecomment-77986",
    "user": "https://github.com/loefflerd"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077987.json:
```json
{
    "body": "Attachment [trac_8620-diamond_operator_bug.patch](tarball://root/attachments/some-uuid/ticket8620/trac_8620-diamond_operator_bug.patch) by @loefflerd created at 2010-03-28 22:02:20",
    "created_at": "2010-03-28T22:02:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8620#issuecomment-77987",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_8620-diamond_operator_bug.patch](tarball://root/attachments/some-uuid/ticket8620/trac_8620-diamond_operator_bug.patch) by @loefflerd created at 2010-03-28 22:02:20



---

archive/issue_comments_077988.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-28T22:07:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8620#issuecomment-77988",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077989.json:
```json
{
    "body": "Merged \"trac_8620-diamond_operator_bug.patch\" in 4.4.alpha0.",
    "created_at": "2010-04-16T18:53:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8620#issuecomment-77989",
    "user": "https://github.com/jhpalmieri"
}
```

Merged "trac_8620-diamond_operator_bug.patch" in 4.4.alpha0.



---

archive/issue_comments_077990.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-16T18:53:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8620#issuecomment-77990",
    "user": "https://github.com/jhpalmieri"
}
```

Resolution: fixed
