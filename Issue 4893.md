# Issue 4893: srange docstring is misleading

archive/issues_004893.json:
```json
{
    "body": "Assignee: cwitty\n\nKeywords: range\n\nI reported\n\n```\nThe docstring for srange() says:\n\n   Return list of numbers \\code{a, a+step, ..., a+k*step},\n   where \\code{a+k*step < b} and \\code{a+(k+1)*step > b}.\n\n   This is the best way to get an iterator over Sage integers as\n   opposed to Python int's.  It also allows you to specify step sizes\n   to iterate.  It is potentially much slower than the Python range\n   statement, depending on your application.\n\nThe second paragraph suggests that what you get is an iterator, but in\nfact you get a list.  Is there any good reason why srange does not\nreturn an iterator?  Surely that would be more efficient in most\ncases, and the user can turn the iterator into a list if needed.\n```\n\nand William replied\n\n```\nsrange's docstring is wrong and should be fixed.  Please post a patch.\n\nThe function sxrange gives a proper python iterator.  The\ndocumentation for srange should contain a remark that sxrange gives\nthe iterator version, and if it doesn't add that too :-)\n\nBut don't change srange to be a python iterator -- that would be like\nmaking range a python iterator, which is a bad idea since sometimes\npeople use ranges not as iterators.\n```\n\nso I will post a suitable patch,\n\nIssue created by migration from https://trac.sagemath.org/ticket/4893\n\n",
    "created_at": "2008-12-30T20:28:37Z",
    "labels": [
        "misc",
        "minor",
        "bug"
    ],
    "title": "srange docstring is misleading",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4893",
    "user": "cremona"
}
```
Assignee: cwitty

Keywords: range

I reported

```
The docstring for srange() says:

   Return list of numbers \code{a, a+step, ..., a+k*step},
   where \code{a+k*step < b} and \code{a+(k+1)*step > b}.

   This is the best way to get an iterator over Sage integers as
   opposed to Python int's.  It also allows you to specify step sizes
   to iterate.  It is potentially much slower than the Python range
   statement, depending on your application.

The second paragraph suggests that what you get is an iterator, but in
fact you get a list.  Is there any good reason why srange does not
return an iterator?  Surely that would be more efficient in most
cases, and the user can turn the iterator into a list if needed.
```

and William replied

```
srange's docstring is wrong and should be fixed.  Please post a patch.

The function sxrange gives a proper python iterator.  The
documentation for srange should contain a remark that sxrange gives
the iterator version, and if it doesn't add that too :-)

But don't change srange to be a python iterator -- that would be like
making range a python iterator, which is a bad idea since sometimes
people use ranges not as iterators.
```

so I will post a suitable patch,

Issue created by migration from https://trac.sagemath.org/ticket/4893





---

archive/issue_comments_037105.json:
```json
{
    "body": "Attachment [trac_4893.patch](tarball://root/attachments/some-uuid/ticket4893/trac_4893.patch) by cremona created at 2008-12-30 23:01:43",
    "created_at": "2008-12-30T23:01:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4893",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4893#issuecomment-37105",
    "user": "cremona"
}
```

Attachment [trac_4893.patch](tarball://root/attachments/some-uuid/ticket4893/trac_4893.patch) by cremona created at 2008-12-30 23:01:43



---

archive/issue_comments_037106.json:
```json
{
    "body": "Patch attached, based on 3.2.2.  It only changes the (second paragraph of the) docstring for srange() so should not cause any problems.",
    "created_at": "2008-12-30T23:02:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4893",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4893#issuecomment-37106",
    "user": "cremona"
}
```

Patch attached, based on 3.2.2.  It only changes the (second paragraph of the) docstring for srange() so should not cause any problems.



---

archive/issue_comments_037107.json:
```json
{
    "body": "Looks good.",
    "created_at": "2008-12-31T08:09:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4893",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4893#issuecomment-37107",
    "user": "AlexGhitza"
}
```

Looks good.



---

archive/issue_comments_037108.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-12T02:17:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4893",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4893#issuecomment-37108",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_037109.json:
```json
{
    "body": "Merged in Sage 3.3.alpha0",
    "created_at": "2009-01-12T02:17:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4893",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4893#issuecomment-37109",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha0
