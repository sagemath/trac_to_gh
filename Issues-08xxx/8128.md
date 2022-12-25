# Issue 8128: UnicodeDecodeError with %latex

archive/issues_008128.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @jhpalmieri @robert-marik mvngu\n\nWith the SageNB spkg at #8051, evaluating a cell\n\n```\n%latex\n\u010d\n```\nraises\n\n```python\n[...]\n  File \"/opt/sage-4.3.1/local/lib/python2.6/site-packages/sage/misc/latex.py\", line 786, in eval\n    O.write(x.encode('utf-8'))\nUnicodeDecodeError: 'ascii' codec can't decode byte 0xc4 in position 0: ordinal not in range(128) \n```\n\nSee [sage-notebook](http://groups.google.com/group/sage-notebook/browse_thread/thread/44c237cc11e9b422).\n\nIssue created by migration from https://trac.sagemath.org/ticket/8128\n\n",
    "closed_at": "2010-02-11T14:38:59Z",
    "created_at": "2010-01-30T02:47:31Z",
    "labels": [
        "component: notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "UnicodeDecodeError with %latex",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8128",
    "user": "https://github.com/qed777"
}
```
Assignee: @williamstein

CC:  @jhpalmieri @robert-marik mvngu

With the SageNB spkg at #8051, evaluating a cell

```
%latex
č
```
raises

```python
[...]
  File "/opt/sage-4.3.1/local/lib/python2.6/site-packages/sage/misc/latex.py", line 786, in eval
    O.write(x.encode('utf-8'))
UnicodeDecodeError: 'ascii' codec can't decode byte 0xc4 in position 0: ordinal not in range(128) 
```

See [sage-notebook](http://groups.google.com/group/sage-notebook/browse_thread/thread/44c237cc11e9b422).

Issue created by migration from https://trac.sagemath.org/ticket/8128





---

archive/issue_comments_071344.json:
```json
{
    "body": "Encode just once, if it's necessary.  Apply to **sage** repository.",
    "created_at": "2010-01-30T02:57:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8128#issuecomment-71344",
    "user": "https://github.com/qed777"
}
```

Encode just once, if it's necessary.  Apply to **sage** repository.



---

archive/issue_comments_071345.json:
```json
{
    "body": "Attachment [trac_8128-latex_cell_unicode.patch](tarball://root/attachments/some-uuid/ticket8128/trac_8128-latex_cell_unicode.patch) by @qed777 created at 2010-01-30 03:00:55\n\nThe patch uses the recently added (cf. #7249, #8051) `sagenb.misc.encoded_str` to avoid attempting to re-encode encoded strings.\n\nI haven't tested this extensively, but it appears to fix the problem above.",
    "created_at": "2010-01-30T03:00:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8128#issuecomment-71345",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_8128-latex_cell_unicode.patch](tarball://root/attachments/some-uuid/ticket8128/trac_8128-latex_cell_unicode.patch) by @qed777 created at 2010-01-30 03:00:55

The patch uses the recently added (cf. #7249, #8051) `sagenb.misc.encoded_str` to avoid attempting to re-encode encoded strings.

I haven't tested this extensively, but it appears to fix the problem above.



---

archive/issue_comments_071346.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-30T03:00:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8128#issuecomment-71346",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071347.json:
```json
{
    "body": "From `sagenb.misc.misc`:\n\n```python\ndef encoded_str(obj, encoding='utf-8'):\n    if isinstance(obj, unicode):\n        return obj.encode(encoding, 'ignore')\n    return str(obj)\n\ndef unicode_str(obj, encoding='utf-8'):\n    if isinstance(obj, str):\n        return obj.decode(encoding, 'ignore')\n    elif isinstance(obj, unicode):\n        return obj\n    return unicode(obj)\n```",
    "created_at": "2010-01-30T03:41:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8128#issuecomment-71347",
    "user": "https://github.com/qed777"
}
```

From `sagenb.misc.misc`:

```python
def encoded_str(obj, encoding='utf-8'):
    if isinstance(obj, unicode):
        return obj.encode(encoding, 'ignore')
    return str(obj)

def unicode_str(obj, encoding='utf-8'):
    if isinstance(obj, str):
        return obj.decode(encoding, 'ignore')
    elif isinstance(obj, unicode):
        return obj
    return unicode(obj)
```



---

archive/issue_comments_071348.json:
```json
{
    "body": "I haven't tested it extensively either, but it looks okay. See #8083 for a related notebook issue and #8130 for a related command-line issue.",
    "created_at": "2010-01-30T04:53:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8128#issuecomment-71348",
    "user": "https://github.com/jhpalmieri"
}
```

I haven't tested it extensively either, but it looks okay. See #8083 for a related notebook issue and #8130 for a related command-line issue.



---

archive/issue_comments_071349.json:
```json
{
    "body": "Seems good, works for me. Tested on the top of #8051",
    "created_at": "2010-01-31T00:46:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8128#issuecomment-71349",
    "user": "https://github.com/robert-marik"
}
```

Seems good, works for me. Tested on the top of #8051



---

archive/issue_comments_071350.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-31T00:46:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8128#issuecomment-71350",
    "user": "https://github.com/robert-marik"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071351.json:
```json
{
    "body": "Just a quick note: This is for the sage repository.",
    "created_at": "2010-02-05T00:35:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8128#issuecomment-71351",
    "user": "https://github.com/qed777"
}
```

Just a quick note: This is for the sage repository.



---

archive/issue_events_019466.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-02-11T14:38:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8128",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8128#event-19466"
}
```



---

archive/issue_comments_071352.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T14:38:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8128",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8128#issuecomment-71352",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
