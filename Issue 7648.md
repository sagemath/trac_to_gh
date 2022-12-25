# Issue 7648: notebook: issue with indentation of first line being wrong

archive/issues_007648.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nOn 11/27/2009 05:47 AM, Minh Nguyen wrote:\n> On Fri, Nov 27, 2009 at 9:10 PM, Yotam Avital <> wrote:\n>> for i in range (1,5):\n>>     print '%6s %6s %6s'%(i, i^2, i^3)\n\nI think *part* of the problem could be line 294 of sagenb.interfaces.expect:\n\n       s = s.strip().rstrip(self._prompt)\n\n\nReplacing this with\n\n       s = s.rstrip(self._prompt)\n\nappears to restore the expected spacing.  But quitting and reopening the\nworksheet puts\n\n1      1      1\n    2      4      8\n    3      9     27\n    4     16     64\n\nin the output cell.  I think the problem here is line 910 (or so) of\nsagenb.notebook.cell:\n\n           out = '///\\n' + out.strip()\n\n\nReplacing this with\n\n           out = '///\\n' + out.strip('\\n')\n\nseems to solve this problem.  It also makes the text representation of\nthe worksheet more compact.\n\nNote: I haven't tested these changes extensively.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7648\n\n",
    "created_at": "2009-12-10T01:19:32Z",
    "labels": [
        "component: notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "notebook: issue with indentation of first line being wrong",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7648",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


```
On 11/27/2009 05:47 AM, Minh Nguyen wrote:
> On Fri, Nov 27, 2009 at 9:10 PM, Yotam Avital <> wrote:
>> for i in range (1,5):
>>     print '%6s %6s %6s'%(i, i^2, i^3)

I think *part* of the problem could be line 294 of sagenb.interfaces.expect:

       s = s.strip().rstrip(self._prompt)


Replacing this with

       s = s.rstrip(self._prompt)

appears to restore the expected spacing.  But quitting and reopening the
worksheet puts

1      1      1
    2      4      8
    3      9     27
    4     16     64

in the output cell.  I think the problem here is line 910 (or so) of
sagenb.notebook.cell:

           out = '///\n' + out.strip()


Replacing this with

           out = '///\n' + out.strip('\n')

seems to solve this problem.  It also makes the text representation of
the worksheet more compact.

Note: I haven't tested these changes extensively.
```


Issue created by migration from https://trac.sagemath.org/ticket/7648





---

archive/issue_comments_065265.json:
```json
{
    "body": "Attachment [trac_7648-missing_indent.patch](tarball://root/attachments/some-uuid/ticket7648/trac_7648-missing_indent.patch) by @qed777 created at 2009-12-10 02:22:30\n\nMake the changes in the ticket description.  sagenb repo.",
    "created_at": "2009-12-10T02:22:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7648#issuecomment-65265",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7648-missing_indent.patch](tarball://root/attachments/some-uuid/ticket7648/trac_7648-missing_indent.patch) by @qed777 created at 2009-12-10 02:22:30

Make the changes in the ticket description.  sagenb repo.



---

archive/issue_comments_065266.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-10T03:13:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7648#issuecomment-65266",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065267.json:
```json
{
    "body": "The Se tests pass.  Unfortunately, `sage -t sagenb/notebook` yields several\n\n```\nA mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.\n```\n\nPlease see #7650.",
    "created_at": "2009-12-10T03:13:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7648#issuecomment-65267",
    "user": "https://github.com/qed777"
}
```

The Se tests pass.  Unfortunately, `sage -t sagenb/notebook` yields several

```
A mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.
```

Please see #7650.



---

archive/issue_comments_065268.json:
```json
{
    "body": "The patch for #7663 (and #7924) clashes with [attachment:trac_7648-missing_indent.patch this one].  Reconciling them should be easy.",
    "created_at": "2010-01-15T23:03:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7648#issuecomment-65268",
    "user": "https://github.com/qed777"
}
```

The patch for #7663 (and #7924) clashes with [attachment:trac_7648-missing_indent.patch this one].  Reconciling them should be easy.



---

archive/issue_comments_065269.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-17T18:26:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7648#issuecomment-65269",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065270.json:
```json
{
    "body": "Good job.",
    "created_at": "2010-01-17T18:26:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7648#issuecomment-65270",
    "user": "https://github.com/TimDumol"
}
```

Good job.



---

archive/issue_comments_065271.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T03:27:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7648",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7648#issuecomment-65271",
    "user": "https://github.com/TimDumol"
}
```

Resolution: fixed



---

archive/issue_events_018191.json:
```json
{
    "actor": "https://github.com/TimDumol",
    "created_at": "2010-01-19T03:27:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7648",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7648#event-18191"
}
```
