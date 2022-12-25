# Issue 4750: make it so sage -t foo.sage pulls in the preparsed version of all the code in foo.sage before doctesting foo.py; make it so "sage -t foo.py" has an option to pull in all code from foo.py before doctesting it.

archive/issues_004750.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @dandrake abergeron\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4750\n\n",
    "created_at": "2008-12-10T12:34:53Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "make it so sage -t foo.sage pulls in the preparsed version of all the code in foo.sage before doctesting foo.py; make it so \"sage -t foo.py\" has an option to pull in all code from foo.py before doctesting it.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4750",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

CC:  @dandrake abergeron



Issue created by migration from https://trac.sagemath.org/ticket/4750





---

archive/issue_comments_035877.json:
```json
{
    "body": "I'm not sure if this is a good idea to do by default. We also use the doctests to give examples for the endusers. Enabling this functionality by default makes it possible to write passing doctests which are not working in interactive sage sessions.",
    "created_at": "2011-08-24T16:29:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4750#issuecomment-35877",
    "user": "https://github.com/koffie"
}
```

I'm not sure if this is a good idea to do by default. We also use the doctests to give examples for the endusers. Enabling this functionality by default makes it possible to write passing doctests which are not working in interactive sage sessions.



---

archive/issue_comments_035878.json:
```json
{
    "body": "I don't understand what this ticket is suggesting.  I thought we already imported the classes and functions defined in a .sage file....",
    "created_at": "2012-02-06T05:15:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4750#issuecomment-35878",
    "user": "https://github.com/roed314"
}
```

I don't understand what this ticket is suggesting.  I thought we already imported the classes and functions defined in a .sage file....



---

archive/issue_comments_035879.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-02-28T15:58:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4750#issuecomment-35879",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_035880.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-02-28T15:58:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4750#issuecomment-35880",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_035881.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-03-07T08:12:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4750",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4750#issuecomment-35881",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: worksforme
