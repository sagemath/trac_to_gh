# Issue 9771: unify doctest commands, especially for 'long' and 'parallel' options

archive/issues_009771.json:
```json
{
    "body": "Assignee: mvngu\n\nMake sure that the commands for doctesting the entire Sage library test the same files, in particular when including `long` and `parallel` options.\n\n\nFrom William, at\n\nhttp://ask.sagemath.org/question/35/does-sage-testall-test-long-doctests\n\nLooking at `SAGE_ROOT/local/bin/sage-sage` we see that `sage -testall` calls the script `sage-maketest` which passes all of its options on to `sage -t`. [and thus cannot handle a parallel option]\n\n\nIf you look in `SAGEROOT/makefile` you'll see that `make test` just calls `sage-maketest`. Note that `make testlong` on the other hand has a specific list of directories it tests, defined in `SAGEROOT/makefile`. Right now they match the list in `SAGE_ROOT/local/bin/sage-maketest`. However, if these ever get out of sync, bad things will happen in that `make test` and `make testlong` would suddenly test different code.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9772\n\n",
    "created_at": "2010-08-20T18:12:45Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "unify doctest commands, especially for 'long' and 'parallel' options",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9771",
    "user": "niles"
}
```
Assignee: mvngu

Make sure that the commands for doctesting the entire Sage library test the same files, in particular when including `long` and `parallel` options.


From William, at

http://ask.sagemath.org/question/35/does-sage-testall-test-long-doctests

Looking at `SAGE_ROOT/local/bin/sage-sage` we see that `sage -testall` calls the script `sage-maketest` which passes all of its options on to `sage -t`. [and thus cannot handle a parallel option]


If you look in `SAGEROOT/makefile` you'll see that `make test` just calls `sage-maketest`. Note that `make testlong` on the other hand has a specific list of directories it tests, defined in `SAGEROOT/makefile`. Right now they match the list in `SAGE_ROOT/local/bin/sage-maketest`. However, if these ever get out of sync, bad things will happen in that `make test` and `make testlong` would suddenly test different code.

Issue created by migration from https://trac.sagemath.org/ticket/9772





---

archive/issue_comments_095760.json:
```json
{
    "body": "In fact, there should be a very easy way to to -ptestall or something.",
    "created_at": "2010-08-24T13:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9771",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9771#issuecomment-95760",
    "user": "kcrisman"
}
```

In fact, there should be a very easy way to to -ptestall or something.



---

archive/issue_comments_095761.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-02-28T16:11:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9771",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9771#issuecomment-95761",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_095762.json:
```json
{
    "body": "Superseded by #12415.",
    "created_at": "2013-02-28T16:11:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9771",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9771#issuecomment-95762",
    "user": "jdemeyer"
}
```

Superseded by #12415.



---

archive/issue_comments_095763.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-02-28T16:11:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9771",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9771#issuecomment-95763",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_095764.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2013-03-07T08:18:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9771",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9771#issuecomment-95764",
    "user": "jdemeyer"
}
```

Resolution: duplicate
