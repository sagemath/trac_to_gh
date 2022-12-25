# Issue 8687: Weak SSL certificates in notebooks

archive/issues_008687.json:
```json
{
    "body": "Assignee: jason, was\n\nTo generate the certificate required for secure (https) notebooks, openssl is called (in Linux, at least). By default, openssl generates 512bit RSA keys, which are far too weak to be used with any degree of confidence.\n\nThe offending code is in the sagenb module, in the run_notebook.py file, line 100. A simple fix is to change the line to:\n\n  cmd = ['openssl genrsa 2048 > %s' % private_pem]\n\nIssue created by migration from https://trac.sagemath.org/ticket/8687\n\n",
    "created_at": "2010-04-14T13:32:34Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Weak SSL certificates in notebooks",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8687",
    "user": "https://trac.sagemath.org/admin/accounts/users/sneves"
}
```
Assignee: jason, was

To generate the certificate required for secure (https) notebooks, openssl is called (in Linux, at least). By default, openssl generates 512bit RSA keys, which are far too weak to be used with any degree of confidence.

The offending code is in the sagenb module, in the run_notebook.py file, line 100. A simple fix is to change the line to:

  cmd = ['openssl genrsa 2048 > %s' % private_pem]

Issue created by migration from https://trac.sagemath.org/ticket/8687





---

archive/issue_comments_079027.json:
```json
{
    "body": "Fixed (for some value of fixed, probably needs to be updated again) in [this long-ago commit](https://github.com/sagemath/sagenb/commit/3cbaaec1fc0362bb0acc40dcf7fe8d8172fad357).   See also https://github.com/sagemath/sagenb/pull/253",
    "created_at": "2014-12-10T21:07:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8687",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8687#issuecomment-79027",
    "user": "https://github.com/kcrisman"
}
```

Fixed (for some value of fixed, probably needs to be updated again) in [this long-ago commit](https://github.com/sagemath/sagenb/commit/3cbaaec1fc0362bb0acc40dcf7fe8d8172fad357).   See also https://github.com/sagemath/sagenb/pull/253



---

archive/issue_comments_079028.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-12-10T21:07:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8687",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8687#issuecomment-79028",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079029.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-12-10T21:07:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8687",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8687#issuecomment-79029",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_079030.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-12-11T18:35:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8687",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8687#issuecomment-79030",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_008861.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-12-11T18:35:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8687",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8687#event-8861"
}
```
