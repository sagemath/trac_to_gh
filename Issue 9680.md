# Issue 9680: Don't greedily replace 'self' with classname in documentation

archive/issues_009680.json:
```json
{
    "body": "Assignee: mvngu\n\nI just found this gem.  Apparently, something replaces \"self\" with the current classname in the documentation.  Amusingly, this almost made something comprehensible by accident.\n\n```\nsage: DLXMatrix?\n...\nThe 0 entry is reserved internally... Blame the original author, or fix it yourDLXMatrix.\n```\n\nwhere it should read \"yourself\" at the end of the sentence.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9680\n\n",
    "created_at": "2010-08-03T23:32:00Z",
    "labels": [
        "component: documentation",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Don't greedily replace 'self' with classname in documentation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9680",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```
Assignee: mvngu

I just found this gem.  Apparently, something replaces "self" with the current classname in the documentation.  Amusingly, this almost made something comprehensible by accident.

```
sage: DLXMatrix?
...
The 0 entry is reserved internally... Blame the original author, or fix it yourDLXMatrix.
```

where it should read "yourself" at the end of the sentence.

Issue created by migration from https://trac.sagemath.org/ticket/9680





---

archive/issue_comments_093951.json:
```json
{
    "body": "I only see this in the notebook.  The cause for the replacement lies in the file sagenb/misc/sageinspect.py, the line\n\n```\n        s = s.replace('self.','%s.'%obj_name)\n```\nin the function sage_getdoc.  There is an identical line in sage/misc/sageinspect.py, so I'm not sure why this doesn't show up in the command line, but I don't remember all the intricacies of how docstrings are produced in the two settings.",
    "created_at": "2010-08-04T00:14:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9680#issuecomment-93951",
    "user": "https://github.com/jhpalmieri"
}
```

I only see this in the notebook.  The cause for the replacement lies in the file sagenb/misc/sageinspect.py, the line

```
        s = s.replace('self.','%s.'%obj_name)
```
in the function sage_getdoc.  There is an identical line in sage/misc/sageinspect.py, so I'm not sure why this doesn't show up in the command line, but I don't remember all the intricacies of how docstrings are produced in the two settings.



---

archive/issue_events_024165.json:
```json
{
    "actor": "https://github.com/mezzarobba",
    "created_at": "2015-04-13T13:11:31Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9680",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9680#event-24165"
}
```



---

archive/issue_comments_093952.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-04-13T13:11:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9680#issuecomment-93952",
    "user": "https://github.com/mezzarobba"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093953.json:
```json
{
    "body": "`DLXMatrix?` now (6.6.rc3) displays\n\n```\n  ...\n   Note: The 0 entry is reserved internally for headers in the\n     sparse representation, so rows and columns begin their indexing\n     with 1. Apologies for any heartache this causes. Blame the\n     original author, or fix it yourself.\n   ...\n```\nas expected.",
    "created_at": "2015-04-13T13:11:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9680#issuecomment-93953",
    "user": "https://github.com/mezzarobba"
}
```

`DLXMatrix?` now (6.6.rc3) displays

```
  ...
   Note: The 0 entry is reserved internally for headers in the
     sparse representation, so rows and columns begin their indexing
     with 1. Apologies for any heartache this causes. Blame the
     original author, or fix it yourself.
   ...
```
as expected.



---

archive/issue_comments_093954.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-04-22T19:26:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9680#issuecomment-93954",
    "user": "https://github.com/videlec"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093955.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2015-04-23T01:45:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9680#issuecomment-93955",
    "user": "https://github.com/vbraun"
}
```

Resolution: wontfix



---

archive/issue_events_024166.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2015-04-23T01:45:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9680",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9680#event-24166"
}
```
