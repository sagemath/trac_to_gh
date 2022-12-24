# Issue 4719: Doctests report mysterious errors instead of ordinary failures

archive/issues_004719.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @garyfurnish\n\nKeywords: doctests\n\nThe doctest module in 3.2.2.alpha0 seems to report *all* failed doctests as \"A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.\" This occurs even when the failure is a very simple one:\n\n\n```\ndef bad_docstring():\n        r\"\"\" A function with a bogus docstring.\n\n        EXAMPLES:\n                sage: 2\n                1\n        \"\"\"\n        pass\n```\n\n\nRunning \"sage -t\" on a file containing only the above code returns a \"mysterious error\", both on 32-bit SuSE (upgraded from 3.2.1) and on the sage.math binary. \n\nIssue created by migration from https://trac.sagemath.org/ticket/4719\n\n",
    "created_at": "2008-12-05T21:00:20Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "Doctests report mysterious errors instead of ordinary failures",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4719",
    "user": "@loefflerd"
}
```
Assignee: mabshoff

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

archive/issue_comments_035595.json:
```json
{
    "body": "The issue has been more than likely introduced by #717. My guess is that the output from the doctest run is not passed back and the logic \"no output -> mysterious error\" kicks in. \n\nCheers,\n\nMichael",
    "created_at": "2008-12-05T21:03:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4719#issuecomment-35595",
    "user": "mabshoff"
}
```

The issue has been more than likely introduced by #717. My guess is that the output from the doctest run is not passed back and the logic "no output -> mysterious error" kicks in. 

Cheers,

Michael



---

archive/issue_comments_035596.json:
```json
{
    "body": "Attachment [trac_4719_bin.patch](tarball://root/attachments/some-uuid/ticket4719/trac_4719_bin.patch) by @garyfurnish created at 2008-12-06 03:23:09\n\nFailing doctests should now fail correctly.",
    "created_at": "2008-12-06T03:23:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4719#issuecomment-35596",
    "user": "@garyfurnish"
}
```

Attachment [trac_4719_bin.patch](tarball://root/attachments/some-uuid/ticket4719/trac_4719_bin.patch) by @garyfurnish created at 2008-12-06 03:23:09

Failing doctests should now fail correctly.



---

archive/issue_comments_035597.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-06T03:23:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4719#issuecomment-35597",
    "user": "@garyfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_035598.json:
```json
{
    "body": "Changing assignee from mabshoff to @garyfurnish.",
    "created_at": "2008-12-06T03:23:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4719#issuecomment-35598",
    "user": "@garyfurnish"
}
```

Changing assignee from mabshoff to @garyfurnish.



---

archive/issue_comments_035599.json:
```json
{
    "body": "Nice work. The problem cases now pass correctly. \n\nCheers,\n\nMichael",
    "created_at": "2008-12-06T05:08:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4719#issuecomment-35599",
    "user": "mabshoff"
}
```

Nice work. The problem cases now pass correctly. 

Cheers,

Michael



---

archive/issue_comments_035600.json:
```json
{
    "body": "Merged in Sage 3.2.2.alpha1",
    "created_at": "2008-12-06T05:08:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4719#issuecomment-35600",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.2.alpha1



---

archive/issue_comments_035601.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-06T05:08:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4719#issuecomment-35601",
    "user": "mabshoff"
}
```

Resolution: fixed
