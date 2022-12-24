# Issue 5052: preparser does not respect leading space in front of "load foo.sage"

archive/issues_005052.json:
```json
{
    "body": "Assignee: cwitty\n\nIf you have something like the following in a file:\n\n```\ntry:\n    load foo.sage\nexcept:\n    print 'uh oh'\n```\n\nit gets preparsed to this, and blows up because of the bad indentation:\n\n```\ntry:\nexecfile(\"foo.py\")\nexcept:\n    print 'uh oh'\n```\n\nThe preparser is not honoring the leading space before the `load` statement.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5052\n\n",
    "created_at": "2009-01-22T09:03:25Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "title": "preparser does not respect leading space in front of \"load foo.sage\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5052",
    "user": "ddrake"
}
```
Assignee: cwitty

If you have something like the following in a file:

```
try:
    load foo.sage
except:
    print 'uh oh'
```

it gets preparsed to this, and blows up because of the bad indentation:

```
try:
execfile("foo.py")
except:
    print 'uh oh'
```

The preparser is not honoring the leading space before the `load` statement.

Issue created by migration from https://trac.sagemath.org/ticket/5052





---

archive/issue_comments_038494.json:
```json
{
    "body": "Attachment [trac_5052.patch](tarball://root/attachments/some-uuid/ticket5052/trac_5052.patch) by ddrake created at 2009-01-23 03:54:26",
    "created_at": "2009-01-23T03:54:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5052#issuecomment-38494",
    "user": "ddrake"
}
```

Attachment [trac_5052.patch](tarball://root/attachments/some-uuid/ticket5052/trac_5052.patch) by ddrake created at 2009-01-23 03:54:26



---

archive/issue_comments_038495.json:
```json
{
    "body": "The problem was in sage-preparse; it ran a lstrip() on the line and never took into consideration the indentation.\n\nI wanted to add some doctests, since as we see here, anything not tested is broken -- do the files in `$SAGE_ROOT/local/bin` get doctested?",
    "created_at": "2009-01-23T03:58:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5052#issuecomment-38495",
    "user": "ddrake"
}
```

The problem was in sage-preparse; it ran a lstrip() on the line and never took into consideration the indentation.

I wanted to add some doctests, since as we see here, anything not tested is broken -- do the files in `$SAGE_ROOT/local/bin` get doctested?



---

archive/issue_comments_038496.json:
```json
{
    "body": "works for me",
    "created_at": "2009-01-24T08:02:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5052#issuecomment-38496",
    "user": "boothby"
}
```

works for me



---

archive/issue_comments_038497.json:
```json
{
    "body": "Merged in Sage 3.3.alpha3",
    "created_at": "2009-01-28T12:35:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5052#issuecomment-38497",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha3



---

archive/issue_comments_038498.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-28T12:35:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5052",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5052#issuecomment-38498",
    "user": "mabshoff"
}
```

Resolution: fixed
