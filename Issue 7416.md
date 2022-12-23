# Issue 7416: Create a 'man page'

archive/issues_007416.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  david.kirkby@onetel.net\n\nThe title says it all really. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7416\n\n",
    "created_at": "2009-11-09T13:26:38Z",
    "labels": [
        "documentation",
        "minor",
        "enhancement"
    ],
    "title": "Create a 'man page'",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7416",
    "user": "drkirkby"
}
```
Assignee: mvngu

CC:  david.kirkby@onetel.net

The title says it all really. 

Issue created by migration from https://trac.sagemath.org/ticket/7416





---

archive/issue_comments_062405.json:
```json
{
    "body": "IMO this man page should be written in reStructuredText for maintainability. `make` should generate the man page file using `rst2man.py` from Python's docutils, and `make install` should copy it to the appropriate place to register it into the system's man page database.",
    "created_at": "2013-07-15T19:59:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7416",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7416#issuecomment-62405",
    "user": "kini"
}
```

IMO this man page should be written in reStructuredText for maintainability. `make` should generate the man page file using `rst2man.py` from Python's docutils, and `make install` should copy it to the appropriate place to register it into the system's man page database.
