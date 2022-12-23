# Issue 8785: avoid subtle interaction between importing multiprocessing and twisted

archive/issues_008785.json:
```json
{
    "body": "Assignee: jason\n\nIt turns out that on some platforms, importing multiprocessing, then twisted, leads to an \"int object is not callable\" TypeError.  This breaks devel/sage/sage/all.py's quit_sage function, causing a big traceback at exit.   This could also cause great confusion for people writing a program that uses `@`parallel('multiprocessing') followed by anything involving twisted. \n\nA simple fix is to import the relevant part of twisted before using multiprocessing in `@`parallel.   The attached patch does this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8785\n\n",
    "created_at": "2010-04-27T20:54:37Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "title": "avoid subtle interaction between importing multiprocessing and twisted",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8785",
    "user": "was"
}
```
Assignee: jason

It turns out that on some platforms, importing multiprocessing, then twisted, leads to an "int object is not callable" TypeError.  This breaks devel/sage/sage/all.py's quit_sage function, causing a big traceback at exit.   This could also cause great confusion for people writing a program that uses `@`parallel('multiprocessing') followed by anything involving twisted. 

A simple fix is to import the relevant part of twisted before using multiprocessing in `@`parallel.   The attached patch does this.

Issue created by migration from https://trac.sagemath.org/ticket/8785





---

archive/issue_comments_080438.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-04-27T20:58:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8785#issuecomment-80438",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_080439.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-27T20:58:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8785#issuecomment-80439",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080440.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-27T22:23:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8785#issuecomment-80440",
    "user": "mariah"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080441.json:
```json
{
    "body": "I tried it and it works!",
    "created_at": "2010-04-27T22:27:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8785#issuecomment-80441",
    "user": "mariah"
}
```

I tried it and it works!



---

archive/issue_comments_080442.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-28T17:36:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8785#issuecomment-80442",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_080443.json:
```json
{
    "body": "Would be more informative to write explicitely on which hardware/OS it failed. \"corporate settings\" is more than vague. Was there any upstream report? This problem might have been solved since then!",
    "created_at": "2016-01-10T23:21:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8785#issuecomment-80443",
    "user": "vdelecroix"
}
```

Would be more informative to write explicitely on which hardware/OS it failed. "corporate settings" is more than vague. Was there any upstream report? This problem might have been solved since then!
