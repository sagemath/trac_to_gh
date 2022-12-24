# Issue 5044: on some systems mwrank dumps core and crashes on exit when run under pexpect

archive/issues_005044.json:
```json
{
    "body": "Assignee: cwitty\n\nA workaround is to add\n\n\n```\ndef quit(self, verbose=False):\n    if self._expect is None: return\n    os.kill(self._expect.pid, 9)\n    self._expect = None\n```\n\nas the last method to interfaces/mwrank.py to override the builtin quit method.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5044\n\n",
    "created_at": "2009-01-21T05:59:52Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "title": "on some systems mwrank dumps core and crashes on exit when run under pexpect",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5044",
    "user": "was"
}
```
Assignee: cwitty

A workaround is to add


```
def quit(self, verbose=False):
    if self._expect is None: return
    os.kill(self._expect.pid, 9)
    self._expect = None
```

as the last method to interfaces/mwrank.py to override the builtin quit method.

Issue created by migration from https://trac.sagemath.org/ticket/5044





---

archive/issue_comments_038419.json:
```json
{
    "body": "Attachment [trac_5044.patch](tarball://root/attachments/some-uuid/ticket5044/trac_5044.patch) by was created at 2009-01-24 07:53:25",
    "created_at": "2009-01-24T07:53:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5044",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5044#issuecomment-38419",
    "user": "was"
}
```

Attachment [trac_5044.patch](tarball://root/attachments/some-uuid/ticket5044/trac_5044.patch) by was created at 2009-01-24 07:53:25



---

archive/issue_comments_038420.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-28T13:07:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5044",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5044#issuecomment-38420",
    "user": "mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_comments_038421.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2009-01-28T13:07:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5044",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5044#issuecomment-38421",
    "user": "mabshoff"
}
```

Changing priority from major to critical.



---

archive/issue_comments_038422.json:
```json
{
    "body": "Merged in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-28T13:48:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5044",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5044#issuecomment-38422",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha3.

Cheers,

Michael



---

archive/issue_comments_038423.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-28T13:48:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5044",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5044#issuecomment-38423",
    "user": "mabshoff"
}
```

Resolution: fixed
