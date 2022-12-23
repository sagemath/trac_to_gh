# Issue 1656: make SCons pick the same gcc as `which gcc`

archive/issues_001656.json:
```json
{
    "body": "Assignee: mabshoff\n\nKiran had some build failure with PolyBori because SCons seems to pick the newest gcc in $PATH instead of the first one. In his particular case the newest gcc was a 32 bit target on a 64 bit platform and things didn't go to well from there. See the discussion toward the end of \n\nhttp://groups.google.com/group/sage-support/browse_thread/thread/cdf2ae8087d5637e#\n\nThis affects PolyBori as well as sagelib as far as I can tell.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/1656\n\n",
    "created_at": "2008-01-02T17:01:49Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "make SCons pick the same gcc as `which gcc`",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1656",
    "user": "mabshoff"
}
```
Assignee: mabshoff

Kiran had some build failure with PolyBori because SCons seems to pick the newest gcc in $PATH instead of the first one. In his particular case the newest gcc was a 32 bit target on a 64 bit platform and things didn't go to well from there. See the discussion toward the end of 

http://groups.google.com/group/sage-support/browse_thread/thread/cdf2ae8087d5637e#

This affects PolyBori as well as sagelib as far as I can tell.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/1656





---

archive/issue_comments_010533.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-02T17:02:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1656#issuecomment-10533",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010534.json:
```json
{
    "body": "On my system, unless PATH is forced to be imported from the external environment, SCons somehow decides to try using the path:\n\n```\n/usr/local/bin:/opt/bin:/bin:/usr/bin\n```\n\ndespite the fact that /opt/bin doesn't exist. (This has caused mischief in the past because I had an old version of gcc in /usr/local/bin and a current one in /usr/bin; in my PATH, /usr/bin comes first.) How is this generated?",
    "created_at": "2008-01-02T19:59:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1656#issuecomment-10534",
    "user": "kedlaya"
}
```

On my system, unless PATH is forced to be imported from the external environment, SCons somehow decides to try using the path:

```
/usr/local/bin:/opt/bin:/bin:/usr/bin
```

despite the fact that /opt/bin doesn't exist. (This has caused mischief in the past because I had an old version of gcc in /usr/local/bin and a current one in /usr/bin; in my PATH, /usr/bin comes first.) How is this generated?



---

archive/issue_comments_010535.json:
```json
{
    "body": "This ticket also relates to #1553.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-03T14:39:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1656#issuecomment-10535",
    "user": "mabshoff"
}
```

This ticket also relates to #1553.

Cheers,

Michael



---

archive/issue_comments_010536.json:
```json
{
    "body": "Changing assignee from mabshoff to gfurnish.",
    "created_at": "2008-03-23T18:30:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1656#issuecomment-10536",
    "user": "gfurnish"
}
```

Changing assignee from mabshoff to gfurnish.



---

archive/issue_comments_010537.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2008-03-23T18:30:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1656#issuecomment-10537",
    "user": "gfurnish"
}
```

Changing status from assigned to new.



---

archive/issue_comments_010538.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-23T18:30:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1656#issuecomment-10538",
    "user": "gfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010539.json:
```json
{
    "body": "This has been fixed in PolyBoRi via a custom.py and has been fixed in SageLib for a long, long time.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-25T16:56:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1656#issuecomment-10539",
    "user": "mabshoff"
}
```

This has been fixed in PolyBoRi via a custom.py and has been fixed in SageLib for a long, long time.

Cheers,

Michael



---

archive/issue_comments_010540.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-25T16:56:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1656#issuecomment-10540",
    "user": "mabshoff"
}
```

Resolution: fixed
