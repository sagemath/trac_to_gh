# Issue 7000: Move Sphinx-ify on-the-fly code to another module

archive/issues_007000.json:
```json
{
    "body": "Assignee: tba\n\nCC:  jhpalmieri\n\nThe code for running docstrings through Sphinx on-demand could be useful in other contexts:\n\n* Command-line (cf. 6820).\n* Notebook reST editor (cf. [The List](http://wiki.sagemath.org/SageUsability)).\n\nCurrently, the code lives in `cell.py`, but it would be easier to mantain and extend in `sage.misc`, say.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7000\n\n",
    "created_at": "2009-09-23T09:25:49Z",
    "labels": [
        "documentation",
        "minor",
        "enhancement"
    ],
    "title": "Move Sphinx-ify on-the-fly code to another module",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7000",
    "user": "mpatel"
}
```
Assignee: tba

CC:  jhpalmieri

The code for running docstrings through Sphinx on-demand could be useful in other contexts:

* Command-line (cf. 6820).
* Notebook reST editor (cf. [The List](http://wiki.sagemath.org/SageUsability)).

Currently, the code lives in `cell.py`, but it would be easier to mantain and extend in `sage.misc`, say.

Issue created by migration from https://trac.sagemath.org/ticket/7000





---

archive/issue_comments_057879.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-30T08:16:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7000#issuecomment-57879",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_057880.json:
```json
{
    "body": "This is now down as part of the notebook refactoring.  It's in sagenb.misc.sphinxify.",
    "created_at": "2009-09-30T08:16:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7000#issuecomment-57880",
    "user": "was"
}
```

This is now down as part of the notebook refactoring.  It's in sagenb.misc.sphinxify.
