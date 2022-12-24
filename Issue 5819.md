# Issue 5819: make sage -coverage require a loads/dumps test for each class defined in a file

archive/issues_005819.json:
```json
{
    "body": "Assignee: mabshoff\n\nKeywords: coverage loads dumps\n\nAt the moment, `sage -coverage file.py` complains if `file.py` has no doctests of the form `s == loads(dumps(s))`.  However, it says nothing if there is only one such doctest in `file.py`, independent of how many different classes are defined in that file.\n\nIdeally, we would have a doctest `s == loads(dumps(s))` for every single class.  Thus, we should change `sage -coverage` to detect if there are classes without such doctests and complain about it.\n\nSee also the thread at\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/bc99d36058aff638\n\nIssue created by migration from https://trac.sagemath.org/ticket/5819\n\n",
    "created_at": "2009-04-19T02:51:45Z",
    "labels": [
        "doctest coverage",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "make sage -coverage require a loads/dumps test for each class defined in a file",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5819",
    "user": "AlexGhitza"
}
```
Assignee: mabshoff

Keywords: coverage loads dumps

At the moment, `sage -coverage file.py` complains if `file.py` has no doctests of the form `s == loads(dumps(s))`.  However, it says nothing if there is only one such doctest in `file.py`, independent of how many different classes are defined in that file.

Ideally, we would have a doctest `s == loads(dumps(s))` for every single class.  Thus, we should change `sage -coverage` to detect if there are classes without such doctests and complain about it.

See also the thread at
http://groups.google.com/group/sage-devel/browse_thread/thread/bc99d36058aff638

Issue created by migration from https://trac.sagemath.org/ticket/5819





---

archive/issue_comments_045737.json:
```json
{
    "body": "This should now be a test of the form TestSuite(s).run() (see also #7209).",
    "created_at": "2009-10-19T20:42:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5819#issuecomment-45737",
    "user": "nthiery"
}
```

This should now be a test of the form TestSuite(s).run() (see also #7209).
