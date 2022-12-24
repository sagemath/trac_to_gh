# Issue 7941: sage -tp N should store times when some files fail

archive/issues_007941.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nline 364 of `$SAGE_LOCAL/bin/sage-ptest` is where to start looking:\n\n```\n    if len(failed) == 0:\n        if interrupt == False:\n            print \"All tests passed!\"\n        else:\n            print \"Keyboard Interrupt: All tests that ran passed.\"\n        #Only update timings if we are doing something standard\n        if opts==\"-long\" or len(opts)==0:\n            with open(time_file_name,\"w\") as time_file:\n                pickle.dump(time_dict, time_file)\n                print \"Timings have been updated.\"\n    else:\n        if interrupt:\n            print \"Keyboard Interrupt, not all tests ran\"\n        print \"\\nThe following tests failed:\\n\"\n        for i in range(len(failed)):\n               print \"\\t\", failed[i]\n        print \"-\"*int(70)\n```\n\n\nThe reason I want this is that if you're making lots of changes and testing frequently, and you never get a completely clean run, all the good files still run in a random order, which is inefficient.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7941\n\n",
    "created_at": "2010-01-16T03:21:55Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "sage -tp N should store times when some files fail",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7941",
    "user": "rlm"
}
```
Assignee: AlexGhitza

line 364 of `$SAGE_LOCAL/bin/sage-ptest` is where to start looking:

```
    if len(failed) == 0:
        if interrupt == False:
            print "All tests passed!"
        else:
            print "Keyboard Interrupt: All tests that ran passed."
        #Only update timings if we are doing something standard
        if opts=="-long" or len(opts)==0:
            with open(time_file_name,"w") as time_file:
                pickle.dump(time_dict, time_file)
                print "Timings have been updated."
    else:
        if interrupt:
            print "Keyboard Interrupt, not all tests ran"
        print "\nThe following tests failed:\n"
        for i in range(len(failed)):
               print "\t", failed[i]
        print "-"*int(70)
```


The reason I want this is that if you're making lots of changes and testing frequently, and you never get a completely clean run, all the good files still run in a random order, which is inefficient.

Issue created by migration from https://trac.sagemath.org/ticket/7941





---

archive/issue_comments_069274.json:
```json
{
    "body": "Changing assignee from AlexGhitza to tbd.",
    "created_at": "2010-01-17T22:23:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7941#issuecomment-69274",
    "user": "AlexGhitza"
}
```

Changing assignee from AlexGhitza to tbd.



---

archive/issue_comments_069275.json:
```json
{
    "body": "Changing component from algebra to doctest.",
    "created_at": "2010-01-17T22:23:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7941#issuecomment-69275",
    "user": "AlexGhitza"
}
```

Changing component from algebra to doctest.



---

archive/issue_comments_069276.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-18T18:39:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7941#issuecomment-69276",
    "user": "rlm"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069277.json:
```json
{
    "body": "Attachment [trac_7941.patch](tarball://root/attachments/some-uuid/ticket7941/trac_7941.patch) by rlm created at 2010-01-19 03:40:40\n\napply to scripts repo",
    "created_at": "2010-01-19T03:40:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7941#issuecomment-69277",
    "user": "rlm"
}
```

Attachment [trac_7941.patch](tarball://root/attachments/some-uuid/ticket7941/trac_7941.patch) by rlm created at 2010-01-19 03:40:40

apply to scripts repo



---

archive/issue_comments_069278.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-19T04:15:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7941#issuecomment-69278",
    "user": "rbeezer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069279.json:
```json
{
    "body": "Works as expected.  Removed timings, introduced a doctest that would fail.\n\nRan `sage  -tp 2  -long devel/sage/sage/graphs/`\n\ntwice, and repeated experiment without -long argument.\n\nIn both cases, second run obviously employed timings.\n\nPositive review.",
    "created_at": "2010-01-19T04:15:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7941#issuecomment-69279",
    "user": "rbeezer"
}
```

Works as expected.  Removed timings, introduced a doctest that would fail.

Ran `sage  -tp 2  -long devel/sage/sage/graphs/`

twice, and repeated experiment without -long argument.

In both cases, second run obviously employed timings.

Positive review.



---

archive/issue_comments_069280.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T04:28:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7941#issuecomment-69280",
    "user": "rlm"
}
```

Resolution: fixed
