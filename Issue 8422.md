# Issue 8422: ChainPoset in broken for small input

archive/issues_008422.json:
```json
{
    "body": "Assignee: sage-combinat\n\nKeywords: ChainPoset\n\nFor n>2 the answer is correct: \n\n```\nsage: Posets.ChainPoset(3).size()\n3\nsage: Posets.ChainPoset(4).size()\n4\nsage: Posets.ChainPoset(5).size()\n5\n```\n\nHowever:\n\n```\nsage: Posets.ChainPoset(2).size()\n1\nsage: Posets.ChainPoset(1).size()\n...\nValueError: not valid poset data.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8422\n\n",
    "created_at": "2010-03-02T17:54:52Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "title": "ChainPoset in broken for small input",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8422",
    "user": "hivert"
}
```
Assignee: sage-combinat

Keywords: ChainPoset

For n>2 the answer is correct: 

```
sage: Posets.ChainPoset(3).size()
3
sage: Posets.ChainPoset(4).size()
4
sage: Posets.ChainPoset(5).size()
5
```

However:

```
sage: Posets.ChainPoset(2).size()
1
sage: Posets.ChainPoset(1).size()
...
ValueError: not valid poset data.
```


Issue created by migration from https://trac.sagemath.org/ticket/8422





---

archive/issue_comments_075488.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-02T18:13:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8422#issuecomment-75488",
    "user": "hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075489.json:
```json
{
    "body": "Attachment [trac_8422-chain_poset_fix-fh.patch](tarball://root/attachments/some-uuid/ticket8422/trac_8422-chain_poset_fix-fh.patch) by hivert created at 2010-03-02 18:13:37",
    "created_at": "2010-03-02T18:13:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8422#issuecomment-75489",
    "user": "hivert"
}
```

Attachment [trac_8422-chain_poset_fix-fh.patch](tarball://root/attachments/some-uuid/ticket8422/trac_8422-chain_poset_fix-fh.patch) by hivert created at 2010-03-02 18:13:37



---

archive/issue_comments_075490.json:
```json
{
    "body": "Changing assignee from sage-combinat to hivert.",
    "created_at": "2010-03-04T21:58:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8422#issuecomment-75490",
    "user": "hivert"
}
```

Changing assignee from sage-combinat to hivert.



---

archive/issue_comments_075491.json:
```json
{
    "body": "patch apply, doctests passed, documentation ok.\n\nPositive review from me.",
    "created_at": "2010-03-04T22:50:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8422#issuecomment-75491",
    "user": "nborie"
}
```

patch apply, doctests passed, documentation ok.

Positive review from me.



---

archive/issue_comments_075492.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-04T22:50:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8422#issuecomment-75492",
    "user": "nborie"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075493.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-06T08:50:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8422#issuecomment-75493",
    "user": "mhansen"
}
```

Resolution: fixed
