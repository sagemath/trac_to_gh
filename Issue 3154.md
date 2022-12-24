# Issue 3154: notebook -- spurious u0027's output

archive/issues_003154.json:
```json
{
    "body": "Assignee: boothby\n\nIn the notebook we have this, caused by _eval_cmd in worksheet.py:\n\n\n```\n%python \n2+2\nprint \"'hi\\'\"\n///\n\n'hi\\u0027\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3154\n\n",
    "created_at": "2008-05-10T22:43:31Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "notebook -- spurious u0027's output",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3154",
    "user": "was"
}
```
Assignee: boothby

In the notebook we have this, caused by _eval_cmd in worksheet.py:


```
%python 
2+2
print "'hi\'"
///

'hi\u0027
```


Issue created by migration from https://trac.sagemath.org/ticket/3154





---

archive/issue_comments_021867.json:
```json
{
    "body": "Attachment [trac_3154-spurious-u0027-output.patch](tarball://root/attachments/some-uuid/ticket3154/trac_3154-spurious-u0027-output.patch) by timdumol created at 2010-01-17 00:30:44\n\nUses base64.b64en/decode instead.",
    "created_at": "2010-01-17T00:30:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3154#issuecomment-21867",
    "user": "timdumol"
}
```

Attachment [trac_3154-spurious-u0027-output.patch](tarball://root/attachments/some-uuid/ticket3154/trac_3154-spurious-u0027-output.patch) by timdumol created at 2010-01-17 00:30:44

Uses base64.b64en/decode instead.



---

archive/issue_comments_021868.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-17T00:31:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3154#issuecomment-21868",
    "user": "timdumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_021869.json:
```json
{
    "body": "I think using %r to handle escaping quotes would be cleaner than using intermediate base64. I'm attaching a new patch that does this.",
    "created_at": "2010-01-17T21:44:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3154#issuecomment-21869",
    "user": "wjp"
}
```

I think using %r to handle escaping quotes would be cleaner than using intermediate base64. I'm attaching a new patch that does this.



---

archive/issue_comments_021870.json:
```json
{
    "body": "Attachment [3154_escaping_quotes.patch](tarball://root/attachments/some-uuid/ticket3154/3154_escaping_quotes.patch) by wjp created at 2010-01-17 21:45:10",
    "created_at": "2010-01-17T21:45:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3154#issuecomment-21870",
    "user": "wjp"
}
```

Attachment [3154_escaping_quotes.patch](tarball://root/attachments/some-uuid/ticket3154/3154_escaping_quotes.patch) by wjp created at 2010-01-17 21:45:10



---

archive/issue_comments_021871.json:
```json
{
    "body": "Can we also use `%r` instead of `base64`-encoding in\n\n* `sage.misc.preparser.load_wrap`\n* `sagenb.misc.support.automatic_name_filter`\n* `worksheet.Worksheet.preparse`\n\n?",
    "created_at": "2010-01-18T09:49:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3154#issuecomment-21871",
    "user": "mpatel"
}
```

Can we also use `%r` instead of `base64`-encoding in

* `sage.misc.preparser.load_wrap`
* `sagenb.misc.support.automatic_name_filter`
* `worksheet.Worksheet.preparse`

?



---

archive/issue_comments_021872.json:
```json
{
    "body": "The second patch causes two SageNB doctest failures:\n\n```python\nFile \"/home/tmp/sagenb-0.5/src/sagenb/sagenb/notebook/worksheet.py\", line 3695:\n    sage: W.check_for_system_switching(c1.cleaned_input_text(), c1)\nExpected:\n    (True, u\"print _support_.syseval(gap, ur'''SymmetricGroup(5)''', '...')\")\nGot:\n    (True, u\"print _support_.syseval(gap, u'SymmetricGroup(5)', '/home/.sage/temp/chopin/5101/dir_2.sagenb/home/sage/0/cells/1')\")\n**********************************************************************\nFile \"/home/tmp/sagenb-0.5/src/sagenb/sagenb/notebook/worksheet.py\", line 3721:\n    sage: W.check_for_system_switching(c1.cleaned_input_text(), c1)\nExpected:\n    (True, u\"print _support_.syseval(gap, ur'''SymmetricGroup(5)''', '...')\")\nGot:\n    (True, \"print _support_.syseval(gap, u'SymmetricGroup(5)', '/home/.sage/temp/chopin/5101/dir_2.sagenb/home/sage/0/cells/1')\")\n\n```\n\nDoes the latter reveal a [minor] problem with #7249?",
    "created_at": "2010-01-18T10:15:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3154#issuecomment-21872",
    "user": "mpatel"
}
```

The second patch causes two SageNB doctest failures:

```python
File "/home/tmp/sagenb-0.5/src/sagenb/sagenb/notebook/worksheet.py", line 3695:
    sage: W.check_for_system_switching(c1.cleaned_input_text(), c1)
Expected:
    (True, u"print _support_.syseval(gap, ur'''SymmetricGroup(5)''', '...')")
Got:
    (True, u"print _support_.syseval(gap, u'SymmetricGroup(5)', '/home/.sage/temp/chopin/5101/dir_2.sagenb/home/sage/0/cells/1')")
**********************************************************************
File "/home/tmp/sagenb-0.5/src/sagenb/sagenb/notebook/worksheet.py", line 3721:
    sage: W.check_for_system_switching(c1.cleaned_input_text(), c1)
Expected:
    (True, u"print _support_.syseval(gap, ur'''SymmetricGroup(5)''', '...')")
Got:
    (True, "print _support_.syseval(gap, u'SymmetricGroup(5)', '/home/.sage/temp/chopin/5101/dir_2.sagenb/home/sage/0/cells/1')")

```

Does the latter reveal a [minor] problem with #7249?



---

archive/issue_comments_021873.json:
```json
{
    "body": "Replying to [comment:3 mpatel]:\n> Can we also use `%r` instead of `base64`-encoding in\n> \n>  * `sage.misc.preparser.load_wrap`\n>  * `sagenb.misc.support.automatic_name_filter`\n>  * `worksheet.Worksheet.preparse`\n> \n> ?\nI believe so. I'd rather that be put in a new ticket though.\n\nThe attached patch should solve the mentioned doctest problems. Can't see how they're related to #7249 though.",
    "created_at": "2010-01-18T11:10:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3154#issuecomment-21873",
    "user": "timdumol"
}
```

Replying to [comment:3 mpatel]:
> Can we also use `%r` instead of `base64`-encoding in
> 
>  * `sage.misc.preparser.load_wrap`
>  * `sagenb.misc.support.automatic_name_filter`
>  * `worksheet.Worksheet.preparse`
> 
> ?
I believe so. I'd rather that be put in a new ticket though.

The attached patch should solve the mentioned doctest problems. Can't see how they're related to #7249 though.



---

archive/issue_comments_021874.json:
```json
{
    "body": "Sorry, I forgot to attach the actual patch.",
    "created_at": "2010-01-18T18:31:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3154#issuecomment-21874",
    "user": "timdumol"
}
```

Sorry, I forgot to attach the actual patch.



---

archive/issue_comments_021875.json:
```json
{
    "body": "Fixes a few doctests and a unicode encoding issue.",
    "created_at": "2010-01-18T18:32:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3154#issuecomment-21875",
    "user": "timdumol"
}
```

Fixes a few doctests and a unicode encoding issue.



---

archive/issue_comments_021876.json:
```json
{
    "body": "Attachment [3154_escaping_quotes.2.patch](tarball://root/attachments/some-uuid/ticket3154/3154_escaping_quotes.2.patch) by mpatel created at 2010-01-20 01:54:58\n\nRebase for minor \"hunk\" failure.  Replaces previous.",
    "created_at": "2010-01-20T01:54:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3154#issuecomment-21876",
    "user": "mpatel"
}
```

Attachment [3154_escaping_quotes.2.patch](tarball://root/attachments/some-uuid/ticket3154/3154_escaping_quotes.2.patch) by mpatel created at 2010-01-20 01:54:58

Rebase for minor "hunk" failure.  Replaces previous.



---

archive/issue_comments_021877.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-20T01:57:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3154#issuecomment-21877",
    "user": "mpatel"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_021878.json:
```json
{
    "body": "Attachment [3154_escaping_quotes.3.patch](tarball://root/attachments/some-uuid/ticket3154/3154_escaping_quotes.3.patch) by mpatel created at 2010-01-20 01:57:40\n\nNice work!  V3 is just a rebase of V2.",
    "created_at": "2010-01-20T01:57:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3154#issuecomment-21878",
    "user": "mpatel"
}
```

Attachment [3154_escaping_quotes.3.patch](tarball://root/attachments/some-uuid/ticket3154/3154_escaping_quotes.3.patch) by mpatel created at 2010-01-20 01:57:40

Nice work!  V3 is just a rebase of V2.



---

archive/issue_comments_021879.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-20T03:45:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3154#issuecomment-21879",
    "user": "timdumol"
}
```

Resolution: fixed



---

archive/issue_comments_021880.json:
```json
{
    "body": "Rebased vs. SageNB 0.7.4.  Replaces previous.",
    "created_at": "2010-02-06T19:00:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3154#issuecomment-21880",
    "user": "mpatel"
}
```

Rebased vs. SageNB 0.7.4.  Replaces previous.



---

archive/issue_comments_021881.json:
```json
{
    "body": "Attachment [3154_escaping_quotes.4.patch](tarball://root/attachments/some-uuid/ticket3154/3154_escaping_quotes.4.patch) by mpatel created at 2010-02-06 19:27:11",
    "created_at": "2010-02-06T19:27:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3154#issuecomment-21881",
    "user": "mpatel"
}
```

Attachment [3154_escaping_quotes.4.patch](tarball://root/attachments/some-uuid/ticket3154/3154_escaping_quotes.4.patch) by mpatel created at 2010-02-06 19:27:11



---

archive/issue_comments_021882.json:
```json
{
    "body": "Changing status from closed to needs_work.",
    "created_at": "2010-02-06T19:27:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3154#issuecomment-21882",
    "user": "mpatel"
}
```

Changing status from closed to needs_work.



---

archive/issue_comments_021883.json:
```json
{
    "body": "V4 is rebased against SageNB 0.7.4 (cf. #8051), but now several doctests fail, at least one of which I can't investigate lucidly right now.  I'll return to this soon.",
    "created_at": "2010-02-06T19:29:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3154#issuecomment-21883",
    "user": "mpatel"
}
```

V4 is rebased against SageNB 0.7.4 (cf. #8051), but now several doctests fail, at least one of which I can't investigate lucidly right now.  I'll return to this soon.



---

archive/issue_comments_021884.json:
```json
{
    "body": "I've reopened this ticket because its **not** in SageNB 0.7 (cf. #8051).   I mistakenly thought, per `hg log`, that I had merged it, but I really merged #4217, whose commit string refers to #3154.",
    "created_at": "2010-02-06T19:47:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3154#issuecomment-21884",
    "user": "mpatel"
}
```

I've reopened this ticket because its **not** in SageNB 0.7 (cf. #8051).   I mistakenly thought, per `hg log`, that I had merged it, but I really merged #4217, whose commit string refers to #3154.



---

archive/issue_comments_021885.json:
```json
{
    "body": "Doctest fixes.  Replaces all previous.",
    "created_at": "2010-02-09T05:18:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3154#issuecomment-21885",
    "user": "mpatel"
}
```

Doctest fixes.  Replaces all previous.



---

archive/issue_comments_021886.json:
```json
{
    "body": "Attachment [3154_escaping_quotes.5.patch](tarball://root/attachments/some-uuid/ticket3154/3154_escaping_quotes.5.patch) by mpatel created at 2010-02-09 05:24:16\n\nV5 is rebased for SageNB 0.7.4 and it includes several new doctest fixes.  Can someone review my changes?",
    "created_at": "2010-02-09T05:24:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3154#issuecomment-21886",
    "user": "mpatel"
}
```

Attachment [3154_escaping_quotes.5.patch](tarball://root/attachments/some-uuid/ticket3154/3154_escaping_quotes.5.patch) by mpatel created at 2010-02-09 05:24:16

V5 is rebased for SageNB 0.7.4 and it includes several new doctest fixes.  Can someone review my changes?



---

archive/issue_comments_021887.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-09T05:24:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3154#issuecomment-21887",
    "user": "mpatel"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_021888.json:
```json
{
    "body": "Doctests pass, no regressions noted.",
    "created_at": "2010-03-19T05:10:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3154#issuecomment-21888",
    "user": "timdumol"
}
```

Doctests pass, no regressions noted.



---

archive/issue_comments_021889.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-19T05:10:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3154",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3154#issuecomment-21889",
    "user": "timdumol"
}
```

Changing status from needs_review to positive_review.
