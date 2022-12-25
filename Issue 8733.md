# Issue 8733: clean up documentation of c_graph.pyx

archive/issues_008733.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nAs the subject says. The goal here is to make the documentation of the module `c_graph.pyx` consistent and also to better document the module itself.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8733\n\n",
    "created_at": "2010-04-21T04:57:50Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.1",
    "title": "clean up documentation of c_graph.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8733",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: jason, ncohen, rlm

As the subject says. The goal here is to make the documentation of the module `c_graph.pyx` consistent and also to better document the module itself.

Issue created by migration from https://trac.sagemath.org/ticket/8733





---

archive/issue_comments_079691.json:
```json
{
    "body": "The method `degree()` in the class `CGraphBackend` of the module `c_graph.pyx` has a bug in its implementation. This issue is tracked at #8395.",
    "created_at": "2010-04-23T02:41:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8733#issuecomment-79691",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The method `degree()` in the class `CGraphBackend` of the module `c_graph.pyx` has a bug in its implementation. This issue is tracked at #8395.



---

archive/issue_comments_079692.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-23T02:41:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8733#issuecomment-79692",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079693.json:
```json
{
    "body": "Attachment [trac_8733-cgraph-cleanup.patch](tarball://root/attachments/some-uuid/ticket8733/trac_8733-cgraph-cleanup.patch) by mvngu created at 2010-04-23 02:57:28",
    "created_at": "2010-04-23T02:57:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8733#issuecomment-79693",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_8733-cgraph-cleanup.patch](tarball://root/attachments/some-uuid/ticket8733/trac_8733-cgraph-cleanup.patch) by mvngu created at 2010-04-23 02:57:28



---

archive/issue_comments_079694.json:
```json
{
    "body": "Changes proposed by the patch include:\n\n* Remove trailing white spaces.\n* Don't go over 79 characters wherever possible.\n* Cross link methods and classes.\n* Add more documentation to methods.\n* Stylistic clean-ups in accordance with [PEP 8](http://www.python.org/dev/peps/pep-0008/).\n* Use \"in\" instead of \"has_key()\" for dictionaries.",
    "created_at": "2010-04-23T02:59:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8733#issuecomment-79694",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changes proposed by the patch include:

* Remove trailing white spaces.
* Don't go over 79 characters wherever possible.
* Cross link methods and classes.
* Add more documentation to methods.
* Stylistic clean-ups in accordance with [PEP 8](http://www.python.org/dev/peps/pep-0008/).
* Use "in" instead of "has_key()" for dictionaries.



---

archive/issue_comments_079695.json:
```json
{
    "body": "Well.. What can I say besides \"good work\" ? :-)\n\nDefinitely cleaner, still passes all tests, the documentation is clearly improved, and I was responsible for some of the mistakes you corrected (the dictionaries, for examples) :-)\n\nPositive review, and thank you very muuuuuuuuch !\n\nNathann",
    "created_at": "2010-04-24T15:02:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8733#issuecomment-79695",
    "user": "https://github.com/nathanncohen"
}
```

Well.. What can I say besides "good work" ? :-)

Definitely cleaner, still passes all tests, the documentation is clearly improved, and I was responsible for some of the mistakes you corrected (the dictionaries, for examples) :-)

Positive review, and thank you very muuuuuuuuch !

Nathann



---

archive/issue_comments_079696.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-24T15:02:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8733#issuecomment-79696",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_079697.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-29T05:40:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8733",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8733#issuecomment-79697",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
