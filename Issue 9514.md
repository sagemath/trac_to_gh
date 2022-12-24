# Issue 9514: sage/symbolic/random_tests.py wrongly depends on order of dict.values()

archive/issues_009514.json:
```json
{
    "body": "Assignee: cwitty\n\nThe variable sage.symbolic.random_tests.full_functions is ordered in the same order as the .values() method on a dict, which is not necessarily reproducible.  (I'm a little curious as to why the order in fact does seem to be reproducible, across multiple platforms, etc., but changes with the addition of seemingly unrelated code -- but not curious enough to investigate.)\n\nAnyway, the current code is clearly wrong.  I'll have a fix in a few minutes.\n\nThis should fix the strange random_tests.py doctest issue from #8988, and possibly reduce the churn in the random_tests doctest results.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9514\n\n",
    "created_at": "2010-07-16T03:36:32Z",
    "labels": [
        "symbolics",
        "major",
        "bug"
    ],
    "title": "sage/symbolic/random_tests.py wrongly depends on order of dict.values()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9514",
    "user": "cwitty"
}
```
Assignee: cwitty

The variable sage.symbolic.random_tests.full_functions is ordered in the same order as the .values() method on a dict, which is not necessarily reproducible.  (I'm a little curious as to why the order in fact does seem to be reproducible, across multiple platforms, etc., but changes with the addition of seemingly unrelated code -- but not curious enough to investigate.)

Anyway, the current code is clearly wrong.  I'll have a fix in a few minutes.

This should fix the strange random_tests.py doctest issue from #8988, and possibly reduce the churn in the random_tests doctest results.

Issue created by migration from https://trac.sagemath.org/ticket/9514





---

archive/issue_comments_091475.json:
```json
{
    "body": "Attachment [trac_9514-random-tests-sort-functions.patch](tarball://root/attachments/some-uuid/ticket9514/trac_9514-random-tests-sort-functions.patch) by cwitty created at 2010-07-16 04:32:34\n\nThis patch fixes the problem, and also seems to fix the random_tests.py problem with #8988 (as expected).",
    "created_at": "2010-07-16T04:32:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9514#issuecomment-91475",
    "user": "cwitty"
}
```

Attachment [trac_9514-random-tests-sort-functions.patch](tarball://root/attachments/some-uuid/ticket9514/trac_9514-random-tests-sort-functions.patch) by cwitty created at 2010-07-16 04:32:34

This patch fixes the problem, and also seems to fix the random_tests.py problem with #8988 (as expected).



---

archive/issue_comments_091476.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-16T04:32:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9514#issuecomment-91476",
    "user": "cwitty"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_091477.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-16T15:26:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9514#issuecomment-91477",
    "user": "novoselt"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091478.json:
```json
{
    "body": "Works for me and removes the necessity of interfering in #8988.",
    "created_at": "2010-07-16T15:26:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9514#issuecomment-91478",
    "user": "novoselt"
}
```

Works for me and removes the necessity of interfering in #8988.



---

archive/issue_comments_091479.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T08:46:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9514#issuecomment-91479",
    "user": "mpatel"
}
```

Resolution: fixed
