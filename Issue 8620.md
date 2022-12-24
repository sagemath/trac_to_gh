# Issue 8620: Rogue minus sign in sage.modular.modsym.ambient.diamond_bracket_operator

archive/issues_008620.json:
```json
{
    "body": "Assignee: craigcitro\n\nKeywords: modular symbols\n\nThere is a minus sign in the code for diamond operators which shouldn't be there; what actually gets returned is the diamond operator times the star involution! In particular, ```< 1 >``` really ought to be the identity map. This patch corrects the error and adds a doctest to prove it. (This is needed for some code I wrote with Jared Weinstein at the 2010 Montreal conference, in which it's really vital to work with sign 0 symbols.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/8620\n\n",
    "created_at": "2010-03-28T21:46:38Z",
    "labels": [
        "modular forms",
        "major",
        "bug"
    ],
    "title": "Rogue minus sign in sage.modular.modsym.ambient.diamond_bracket_operator",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8620",
    "user": "davidloeffler"
}
```
Assignee: craigcitro

Keywords: modular symbols

There is a minus sign in the code for diamond operators which shouldn't be there; what actually gets returned is the diamond operator times the star involution! In particular, ```< 1 >``` really ought to be the identity map. This patch corrects the error and adds a doctest to prove it. (This is needed for some code I wrote with Jared Weinstein at the 2010 Montreal conference, in which it's really vital to work with sign 0 symbols.)

Issue created by migration from https://trac.sagemath.org/ticket/8620





---

archive/issue_comments_078113.json:
```json
{
    "body": "patch against 4.3.4",
    "created_at": "2010-03-28T21:53:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8620#issuecomment-78113",
    "user": "davidloeffler"
}
```

patch against 4.3.4



---

archive/issue_comments_078114.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-28T22:02:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8620#issuecomment-78114",
    "user": "davidloeffler"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078115.json:
```json
{
    "body": "Attachment [trac_8620-diamond_operator_bug.patch](tarball://root/attachments/some-uuid/ticket8620/trac_8620-diamond_operator_bug.patch) by davidloeffler created at 2010-03-28 22:02:20",
    "created_at": "2010-03-28T22:02:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8620#issuecomment-78115",
    "user": "davidloeffler"
}
```

Attachment [trac_8620-diamond_operator_bug.patch](tarball://root/attachments/some-uuid/ticket8620/trac_8620-diamond_operator_bug.patch) by davidloeffler created at 2010-03-28 22:02:20



---

archive/issue_comments_078116.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-28T22:07:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8620#issuecomment-78116",
    "user": "was"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078117.json:
```json
{
    "body": "Merged \"trac_8620-diamond_operator_bug.patch\" in 4.4.alpha0.",
    "created_at": "2010-04-16T18:53:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8620#issuecomment-78117",
    "user": "jhpalmieri"
}
```

Merged "trac_8620-diamond_operator_bug.patch" in 4.4.alpha0.



---

archive/issue_comments_078118.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-16T18:53:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8620",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8620#issuecomment-78118",
    "user": "jhpalmieri"
}
```

Resolution: fixed
