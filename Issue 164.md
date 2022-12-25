# Issue 164: doctests dependence thing

archive/issues_000164.json:
```json
{
    "body": "Assignee: @williamstein\n\nIt would be nice if, when one line of a doctest fails, then the doctest doesn't run the rest of that \"example block\". What tends to happen is e.g. one line fails, so then a bunch of variables aren't defined, and then you get tons of garbage in your doctest output, which is hard to sift through. After the first failure, it would be good if it would just stop there, and move onto the next example. (Or at least if there was an option for this behaviour.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/164\n\n",
    "created_at": "2006-10-29T23:07:46Z",
    "labels": [
        "component: user interface",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "doctests dependence thing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/164",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: @williamstein

It would be nice if, when one line of a doctest fails, then the doctest doesn't run the rest of that "example block". What tends to happen is e.g. one line fails, so then a bunch of variables aren't defined, and then you get tons of garbage in your doctest output, which is hard to sift through. After the first failure, it would be good if it would just stop there, and move onto the next example. (Or at least if there was an option for this behaviour.)

Issue created by migration from https://trac.sagemath.org/ticket/164





---

archive/issue_comments_000728.json:
```json
{
    "body": "Doctest is a completely standard Python module.  I didn't write it.  Maybe you\nshould look at the documentation and see if it has the feature you want already.\nIf not, you could propose it to the Python people (e.g., as a PEP).  This \nisn't really a SAGE question.",
    "created_at": "2006-11-06T06:46:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/164#issuecomment-728",
    "user": "https://github.com/williamstein"
}
```

Doctest is a completely standard Python module.  I didn't write it.  Maybe you
should look at the documentation and see if it has the feature you want already.
If not, you could propose it to the Python people (e.g., as a PEP).  This 
isn't really a SAGE question.



---

archive/issue_comments_000729.json:
```json
{
    "body": "Does [nose](http://trac.sagemath.org/sage_trac/ticket/9921) have a better way of handling this (not that we could switch to that anytime soon)?  I thought about, but decided against, making this \"wontfix\" after six years - it WOULD be nice.  Comments?",
    "created_at": "2013-01-29T20:31:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/164#issuecomment-729",
    "user": "https://github.com/kcrisman"
}
```

Does [nose](http://trac.sagemath.org/sage_trac/ticket/9921) have a better way of handling this (not that we could switch to that anytime soon)?  I thought about, but decided against, making this "wontfix" after six years - it WOULD be nice.  Comments?



---

archive/issue_comments_000730.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-06-13T12:20:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/164#issuecomment-730",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_000731.json:
```json
{
    "body": "The new doctest option `sage -t --initial` sort of does this: it shows only the first failure in a doctest block. It's an *option* which needs to be specified explicitly but I think that's sufficient.",
    "created_at": "2013-06-13T12:20:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/164#issuecomment-731",
    "user": "https://github.com/jdemeyer"
}
```

The new doctest option `sage -t --initial` sort of does this: it shows only the first failure in a doctest block. It's an *option* which needs to be specified explicitly but I think that's sufficient.



---

archive/issue_comments_000732.json:
```json
{
    "body": "Changing component from user interface to doctest framework.",
    "created_at": "2013-06-13T12:20:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/164#issuecomment-732",
    "user": "https://github.com/jdemeyer"
}
```

Changing component from user interface to doctest framework.



---

archive/issue_comments_000733.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-06-13T12:20:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/164#issuecomment-733",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_000170.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-06-19T12:21:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/164",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/164#event-170"
}
```



---

archive/issue_comments_000734.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-06-19T12:21:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/164",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/164#issuecomment-734",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: worksforme
