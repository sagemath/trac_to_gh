# Issue 4719: [with patch, positive review] Doctests report mysterious errors instead of ordinary failures

archive/issues_004719.json:
```json
{
    "body": "Assignee: @garyfurnish\n\nCC:  @garyfurnish\n\nKeywords: doctests\n\nThe doctest module in 3.2.2.alpha0 seems to report *all* failed doctests as \"A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.\" This occurs even when the failure is a very simple one:\n\n```\ndef bad_docstring():\n        r\"\"\" A function with a bogus docstring.\n\n        EXAMPLES:\n                sage: 2\n                1\n        \"\"\"\n        pass\n```\n\nRunning \"sage -t\" on a file containing only the above code returns a \"mysterious error\", both on 32-bit SuSE (upgraded from 3.2.1) and on the sage.math binary. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4719\n\n",
    "closed_at": "2008-12-06T05:08:23Z",
    "created_at": "2008-12-05T21:00:20Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "[with patch, positive review] Doctests report mysterious errors instead of ordinary failures",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4719",
    "user": "https://github.com/loefflerd"
}
```
Assignee: @garyfurnish

CC:  @garyfurnish

Keywords: doctests

The doctest module in 3.2.2.alpha0 seems to report *all* failed doctests as "A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest." This occurs even when the failure is a very simple one:

```
def bad_docstring():
        r""" A function with a bogus docstring.

        EXAMPLES:
                sage: 2
                1
        """
        pass
```

Running "sage -t" on a file containing only the above code returns a "mysterious error", both on 32-bit SuSE (upgraded from 3.2.1) and on the sage.math binary. 

Issue created by migration from https://trac.sagemath.org/ticket/4719





---

archive/issue_comments_035526.json:
```json
{
    "body": "The issue has been more than likely introduced by #717. My guess is that the output from the doctest run is not passed back and the logic \"no output -> mysterious error\" kicks in. \n\nCheers,\n\nMichael",
    "created_at": "2008-12-05T21:03:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4719#issuecomment-35526",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The issue has been more than likely introduced by #717. My guess is that the output from the doctest run is not passed back and the logic "no output -> mysterious error" kicks in. 

Cheers,

Michael



---

archive/issue_comments_035527.json:
```json
{
    "body": "Attachment [trac_4719_bin.patch](tarball://root/attachments/some-uuid/ticket4719/trac_4719_bin.patch) by @garyfurnish created at 2008-12-06 03:23:09\n\nFailing doctests should now fail correctly.",
    "created_at": "2008-12-06T03:23:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4719#issuecomment-35527",
    "user": "https://github.com/garyfurnish"
}
```

Attachment [trac_4719_bin.patch](tarball://root/attachments/some-uuid/ticket4719/trac_4719_bin.patch) by @garyfurnish created at 2008-12-06 03:23:09

Failing doctests should now fail correctly.



---

archive/issue_comments_035528.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-06T03:23:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4719#issuecomment-35528",
    "user": "https://github.com/garyfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_035529.json:
```json
{
    "body": "Changing assignee from mabshoff to @garyfurnish.",
    "created_at": "2008-12-06T03:23:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4719#issuecomment-35529",
    "user": "https://github.com/garyfurnish"
}
```

Changing assignee from mabshoff to @garyfurnish.



---

archive/issue_comments_035530.json:
```json
{
    "body": "Nice work. The problem cases now pass correctly. \n\nCheers,\n\nMichael",
    "created_at": "2008-12-06T05:08:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4719#issuecomment-35530",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Nice work. The problem cases now pass correctly. 

Cheers,

Michael



---

archive/issue_comments_035531.json:
```json
{
    "body": "Merged in Sage 3.2.2.alpha1",
    "created_at": "2008-12-06T05:08:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4719#issuecomment-35531",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.2.alpha1



---

archive/issue_events_010783.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-06T05:08:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4719",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4719#event-10783"
}
```



---

archive/issue_comments_035532.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-06T05:08:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4719#issuecomment-35532",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
