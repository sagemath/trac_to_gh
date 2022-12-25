# Issue 7663: notebook -- synchronization code surprises printing of certain characters

archive/issues_007663.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n``` \nThis is weird. Occassionaly, in the SAGE notebook, version 4.2.1, the\nlast characters of output after evaluating a cell are supressed. I've\ntried all of string.printable: the only characters supressed are \"S\",\n\"A\", \"G\", \"E\" and \"_\". No kidding.\n Just try:\n\nprint \"ASAVFDBAAGGG___EEESS\"\n///\nASAVFDB\n\n\nprint \"ASAVFDBAAGGG___EEESS.\"\n///\nASAVFDBAAGGG___EEESS.\n\n Is this a private joke or an amazing coincidence?\n\n Regards\nPablo\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7663\n\n",
    "created_at": "2009-12-11T15:13:24Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "notebook -- synchronization code surprises printing of certain characters",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7663",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


``` 
This is weird. Occassionaly, in the SAGE notebook, version 4.2.1, the
last characters of output after evaluating a cell are supressed. I've
tried all of string.printable: the only characters supressed are "S",
"A", "G", "E" and "_". No kidding.
 Just try:

print "ASAVFDBAAGGG___EEESS"
///
ASAVFDB


print "ASAVFDBAAGGG___EEESS."
///
ASAVFDBAAGGG___EEESS.

 Is this a private joke or an amazing coincidence?

 Regards
Pablo
```


Issue created by migration from https://trac.sagemath.org/ticket/7663





---

archive/issue_comments_065501.json:
```json
{
    "body": "For what it's worth, I don't see this problem with the latest at #6855.  I *may* have inadvertently fixed it.",
    "created_at": "2009-12-11T15:58:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7663#issuecomment-65501",
    "user": "https://github.com/qed777"
}
```

For what it's worth, I don't see this problem with the latest at #6855.  I *may* have inadvertently fixed it.



---

archive/issue_comments_065502.json:
```json
{
    "body": "Possibly related: #7410.  #7666 *may* fix both.",
    "created_at": "2009-12-14T17:45:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7663#issuecomment-65502",
    "user": "https://github.com/qed777"
}
```

Possibly related: #7410.  #7666 *may* fix both.



---

archive/issue_comments_065503.json:
```json
{
    "body": "Actually, see #7924.  In particular,\n\n```python\nsage: from sagenb.interfaces.expect import WorksheetProcess_ExpectImplementation\nsage: wp = WorksheetProcess_ExpectImplementation() \nsage: wp.execute('print \"ASAVFDBAAGGG___EEESS\"')\nsage: wp.output_status()\nOutput Status:\n        output: 'ASAVFDB'\n        filenames: []\n        done: True\nsage: wp.execute('print \"ASAVFDBAAGGG___EEESS.\"')\nsage: wp.output_status()\nOutput Status:\n        output: 'ASAVFDBAAGGG___EEESS.'\n        filenames: []\n        done: True\n```\n",
    "created_at": "2010-01-15T22:41:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7663#issuecomment-65503",
    "user": "https://github.com/qed777"
}
```

Actually, see #7924.  In particular,

```python
sage: from sagenb.interfaces.expect import WorksheetProcess_ExpectImplementation
sage: wp = WorksheetProcess_ExpectImplementation() 
sage: wp.execute('print "ASAVFDBAAGGG___EEESS"')
sage: wp.output_status()
Output Status:
        output: 'ASAVFDB'
        filenames: []
        done: True
sage: wp.execute('print "ASAVFDBAAGGG___EEESS."')
sage: wp.output_status()
Output Status:
        output: 'ASAVFDBAAGGG___EEESS.'
        filenames: []
        done: True
```




---

archive/issue_comments_065504.json:
```json
{
    "body": "Don't use rstrip on internal prompt.  sagenb repo.",
    "created_at": "2010-01-15T23:07:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7663#issuecomment-65504",
    "user": "https://github.com/qed777"
}
```

Don't use rstrip on internal prompt.  sagenb repo.



---

archive/issue_comments_065505.json:
```json
{
    "body": "Attachment [trac_7663-rstrip_prompt.patch](tarball://root/attachments/some-uuid/ticket7663/trac_7663-rstrip_prompt.patch) by @qed777 created at 2010-01-15 23:07:30",
    "created_at": "2010-01-15T23:07:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7663#issuecomment-65505",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7663-rstrip_prompt.patch](tarball://root/attachments/some-uuid/ticket7663/trac_7663-rstrip_prompt.patch) by @qed777 created at 2010-01-15 23:07:30



---

archive/issue_comments_065506.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-15T23:07:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7663#issuecomment-65506",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065507.json:
```json
{
    "body": "The patch here clashes with that at #7648, but it should be easy to reconcile them.",
    "created_at": "2010-01-15T23:09:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7663#issuecomment-65507",
    "user": "https://github.com/qed777"
}
```

The patch here clashes with that at #7648, but it should be easy to reconcile them.



---

archive/issue_comments_065508.json:
```json
{
    "body": "Rebased on #7648.",
    "created_at": "2010-01-17T18:31:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7663#issuecomment-65508",
    "user": "https://github.com/TimDumol"
}
```

Rebased on #7648.



---

archive/issue_comments_065509.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-17T18:31:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7663#issuecomment-65509",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065510.json:
```json
{
    "body": "Attachment [trac_7663-rstrip_prompt.2.patch](tarball://root/attachments/some-uuid/ticket7663/trac_7663-rstrip_prompt.2.patch) by @TimDumol created at 2010-01-17 18:31:44\n\nLGTM.",
    "created_at": "2010-01-17T18:31:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7663#issuecomment-65510",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_7663-rstrip_prompt.2.patch](tarball://root/attachments/some-uuid/ticket7663/trac_7663-rstrip_prompt.2.patch) by @TimDumol created at 2010-01-17 18:31:44

LGTM.



---

archive/issue_comments_065511.json:
```json
{
    "body": "Attachment [trac_7663-rstrip_prompt.3.patch](tarball://root/attachments/some-uuid/ticket7663/trac_7663-rstrip_prompt.3.patch) by @qed777 created at 2010-01-18 08:41:35\n\nRemove extra line to fix #7648.  Replaces previous.",
    "created_at": "2010-01-18T08:41:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7663#issuecomment-65511",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7663-rstrip_prompt.3.patch](tarball://root/attachments/some-uuid/ticket7663/trac_7663-rstrip_prompt.3.patch) by @qed777 created at 2010-01-18 08:41:35

Remove extra line to fix #7648.  Replaces previous.



---

archive/issue_comments_065512.json:
```json
{
    "body": "V3 drops `s = s.strip()`, to maintain #7648.",
    "created_at": "2010-01-18T08:44:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7663#issuecomment-65512",
    "user": "https://github.com/qed777"
}
```

V3 drops `s = s.strip()`, to maintain #7648.



---

archive/issue_comments_065513.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T03:28:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7663#issuecomment-65513",
    "user": "https://github.com/TimDumol"
}
```

Resolution: fixed



---

archive/issue_events_018260.json:
```json
{
    "actor": "https://github.com/TimDumol",
    "created_at": "2010-01-19T03:28:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7663",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7663#event-18260"
}
```
