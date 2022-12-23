# Issue 7663: notebook -- synchronization code surprises printing of certain characters

archive/issues_007663.json:
```json
{
    "body": "Assignee: was\n\n\n``` \nThis is weird. Occassionaly, in the SAGE notebook, version 4.2.1, the\nlast characters of output after evaluating a cell are supressed. I've\ntried all of string.printable: the only characters supressed are \"S\",\n\"A\", \"G\", \"E\" and \"_\". No kidding.\n Just try:\n\nprint \"ASAVFDBAAGGG___EEESS\"\n///\nASAVFDB\n\n\nprint \"ASAVFDBAAGGG___EEESS.\"\n///\nASAVFDBAAGGG___EEESS.\n\n Is this a private joke or an amazing coincidence?\n\n Regards\nPablo\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7663\n\n",
    "created_at": "2009-12-11T15:13:24Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "notebook -- synchronization code surprises printing of certain characters",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7663",
    "user": "was"
}
```
Assignee: was


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

archive/issue_comments_065617.json:
```json
{
    "body": "For what it's worth, I don't see this problem with the latest at #6855.  I *may* have inadvertently fixed it.",
    "created_at": "2009-12-11T15:58:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7663#issuecomment-65617",
    "user": "mpatel"
}
```

For what it's worth, I don't see this problem with the latest at #6855.  I *may* have inadvertently fixed it.



---

archive/issue_comments_065618.json:
```json
{
    "body": "Possibly related: #7410.  #7666 *may* fix both.",
    "created_at": "2009-12-14T17:45:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7663#issuecomment-65618",
    "user": "mpatel"
}
```

Possibly related: #7410.  #7666 *may* fix both.



---

archive/issue_comments_065619.json:
```json
{
    "body": "Actually, see #7924.  In particular,\n\n```python\nsage: from sagenb.interfaces.expect import WorksheetProcess_ExpectImplementation\nsage: wp = WorksheetProcess_ExpectImplementation() \nsage: wp.execute('print \"ASAVFDBAAGGG___EEESS\"')\nsage: wp.output_status()\nOutput Status:\n        output: 'ASAVFDB'\n        filenames: []\n        done: True\nsage: wp.execute('print \"ASAVFDBAAGGG___EEESS.\"')\nsage: wp.output_status()\nOutput Status:\n        output: 'ASAVFDBAAGGG___EEESS.'\n        filenames: []\n        done: True\n```\n",
    "created_at": "2010-01-15T22:41:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7663#issuecomment-65619",
    "user": "mpatel"
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

archive/issue_comments_065620.json:
```json
{
    "body": "Don't use rstrip on internal prompt.  sagenb repo.",
    "created_at": "2010-01-15T23:07:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7663#issuecomment-65620",
    "user": "mpatel"
}
```

Don't use rstrip on internal prompt.  sagenb repo.



---

archive/issue_comments_065621.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-01-15T23:07:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7663#issuecomment-65621",
    "user": "mpatel"
}
```

Attachment



---

archive/issue_comments_065622.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-15T23:07:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7663#issuecomment-65622",
    "user": "mpatel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065623.json:
```json
{
    "body": "The patch here clashes with that at #7648, but it should be easy to reconcile them.",
    "created_at": "2010-01-15T23:09:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7663#issuecomment-65623",
    "user": "mpatel"
}
```

The patch here clashes with that at #7648, but it should be easy to reconcile them.



---

archive/issue_comments_065624.json:
```json
{
    "body": "Rebased on #7648.",
    "created_at": "2010-01-17T18:31:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7663#issuecomment-65624",
    "user": "timdumol"
}
```

Rebased on #7648.



---

archive/issue_comments_065625.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-17T18:31:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7663#issuecomment-65625",
    "user": "timdumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065626.json:
```json
{
    "body": "Attachment\n\nLGTM.",
    "created_at": "2010-01-17T18:31:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7663#issuecomment-65626",
    "user": "timdumol"
}
```

Attachment

LGTM.



---

archive/issue_comments_065627.json:
```json
{
    "body": "Attachment\n\nRemove extra line to fix #7648.  Replaces previous.",
    "created_at": "2010-01-18T08:41:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7663#issuecomment-65627",
    "user": "mpatel"
}
```

Attachment

Remove extra line to fix #7648.  Replaces previous.



---

archive/issue_comments_065628.json:
```json
{
    "body": "V3 drops `s = s.strip()`, to maintain #7648.",
    "created_at": "2010-01-18T08:44:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7663#issuecomment-65628",
    "user": "mpatel"
}
```

V3 drops `s = s.strip()`, to maintain #7648.



---

archive/issue_comments_065629.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T03:28:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7663",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7663#issuecomment-65629",
    "user": "timdumol"
}
```

Resolution: fixed
