# Issue 508: problem with "sage -c"

archive/issues_000508.json:
```json
{
    "body": "Assignee: was\n\nCreate any script, say test.sage.  The following should work but doesn't:\n\n```\n  # sage -c \"load test.sage\"\nTraceback (most recent call last):\n  File \"/home/was/s/local/bin/sage-eval\", line 10, in <module>\n    eval(compile(s,tmp_filename(),'exec'))\n  File \"/home/was/.sage//temp/sage/25215//tmp_0\", line 1\n    load test.sage\n            ^\nSyntaxError: invalid syntax\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/508\n\n",
    "created_at": "2007-08-29T08:19:22Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "problem with \"sage -c\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/508",
    "user": "was"
}
```
Assignee: was

Create any script, say test.sage.  The following should work but doesn't:

```
  # sage -c "load test.sage"
Traceback (most recent call last):
  File "/home/was/s/local/bin/sage-eval", line 10, in <module>
    eval(compile(s,tmp_filename(),'exec'))
  File "/home/was/.sage//temp/sage/25215//tmp_0", line 1
    load test.sage
            ^
SyntaxError: invalid syntax
```


Issue created by migration from https://trac.sagemath.org/ticket/508





---

archive/issue_comments_002543.json:
```json
{
    "body": "Changing component from algebraic geometry to user interface.",
    "created_at": "2007-09-07T05:28:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/508",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/508#issuecomment-2543",
    "user": "craigcitro"
}
```

Changing component from algebraic geometry to user interface.



---

archive/issue_comments_002544.json:
```json
{
    "body": "Why is this supposed to work?\n\nAnyway I did some investigation, and the problem comes from the fact that preparse() doesn't take care of \"load test.sage\" since that is done by ipython magic usually.  \n\nThere is very complicated logic in sage-preparse to deal with those that would be inappropriate to reproduce in sage-eval.\n\nAlso there is a very simple workaround: sage test.sage\n\nSo I vote for 'wontfix' for this bug.",
    "created_at": "2008-10-23T23:02:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/508",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/508#issuecomment-2544",
    "user": "anakha"
}
```

Why is this supposed to work?

Anyway I did some investigation, and the problem comes from the fact that preparse() doesn't take care of "load test.sage" since that is done by ipython magic usually.  

There is very complicated logic in sage-preparse to deal with those that would be inappropriate to reproduce in sage-eval.

Also there is a very simple workaround: sage test.sage

So I vote for 'wontfix' for this bug.



---

archive/issue_comments_002545.json:
```json
{
    "body": "> So I vote for 'wontfix' for this bug.\n\nJust because you couldn't fix it and there is a workaround doesn't mean it isn't a bug.\n\nAnd this is still a bug in sage-3.2:\n\n```\nteragon:tmp wstein$ more a.sage\nprint 2^3\nteragon:tmp wstein$ sage -c \"load a.sage\"\nTraceback (most recent call last):\n  File \"/Users/wstein/sage/local/bin/sage-eval\", line 10, in <module>\n    eval(compile(s,tmp_filename(),'exec'))\n  File \"/Users/wstein/.sage//temp/teragon.local/98089//tmp_0\", line 1\n    load a.sage\n         ^\nSyntaxError: invalid syntax\n\n```\n",
    "created_at": "2008-10-23T23:37:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/508",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/508#issuecomment-2545",
    "user": "was"
}
```

> So I vote for 'wontfix' for this bug.

Just because you couldn't fix it and there is a workaround doesn't mean it isn't a bug.

And this is still a bug in sage-3.2:

```
teragon:tmp wstein$ more a.sage
print 2^3
teragon:tmp wstein$ sage -c "load a.sage"
Traceback (most recent call last):
  File "/Users/wstein/sage/local/bin/sage-eval", line 10, in <module>
    eval(compile(s,tmp_filename(),'exec'))
  File "/Users/wstein/.sage//temp/teragon.local/98089//tmp_0", line 1
    load a.sage
         ^
SyntaxError: invalid syntax

```




---

archive/issue_comments_002546.json:
```json
{
    "body": "Attachment [trac_508.patch](tarball://root/attachments/some-uuid/ticket508/trac_508.patch) by anakha created at 2008-10-24 00:37:26\n\nFixes the problem by emulating load and attach.\n\nIt won't work with files that have spaces in their name because sage, sage-sage, sage-run, and various other are not ready to deal with that, yet.",
    "created_at": "2008-10-24T00:37:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/508",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/508#issuecomment-2546",
    "user": "anakha"
}
```

Attachment [trac_508.patch](tarball://root/attachments/some-uuid/ticket508/trac_508.patch) by anakha created at 2008-10-24 00:37:26

Fixes the problem by emulating load and attach.

It won't work with files that have spaces in their name because sage, sage-sage, sage-run, and various other are not ready to deal with that, yet.



---

archive/issue_comments_002547.json:
```json
{
    "body": "This doesn't work because when sage-eval gets run the working directory is local/bin/, so the file test.sage isn't found.  I bet you tested this patch with test.sage in SAGE_ROOT/local/bin/, which is the only case when this will work:\n\n```\nteragon-2:sage-3.2 wstein$ more test.sage\nprint \"Hi\"\nteragon-2:sage-3.2 wstein$ ./sage -c \"load test.sage\"\n/Users/wstein/sage/build/sage-3.2/local/bin/sage-preparse: File test.sage is missing\npython: can't open file 'test.py': [Errno 2] No such file or directory\nteragon-2:sage-3.2 wstein$ cp test.sage local/bin/\nteragon-2:sage-3.2 wstein$ ./sage -c \"load test.sage\"\nHi\n```\n",
    "created_at": "2008-11-27T07:49:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/508",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/508#issuecomment-2547",
    "user": "was"
}
```

This doesn't work because when sage-eval gets run the working directory is local/bin/, so the file test.sage isn't found.  I bet you tested this patch with test.sage in SAGE_ROOT/local/bin/, which is the only case when this will work:

```
teragon-2:sage-3.2 wstein$ more test.sage
print "Hi"
teragon-2:sage-3.2 wstein$ ./sage -c "load test.sage"
/Users/wstein/sage/build/sage-3.2/local/bin/sage-preparse: File test.sage is missing
python: can't open file 'test.py': [Errno 2] No such file or directory
teragon-2:sage-3.2 wstein$ cp test.sage local/bin/
teragon-2:sage-3.2 wstein$ ./sage -c "load test.sage"
Hi
```




---

archive/issue_comments_002548.json:
```json
{
    "body": "Attachment [trac_508v2.patch](tarball://root/attachments/some-uuid/ticket508/trac_508v2.patch) by abergeron created at 2008-12-24 04:55:20",
    "created_at": "2008-12-24T04:55:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/508",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/508#issuecomment-2548",
    "user": "abergeron"
}
```

Attachment [trac_508v2.patch](tarball://root/attachments/some-uuid/ticket508/trac_508v2.patch) by abergeron created at 2008-12-24 04:55:20



---

archive/issue_comments_002549.json:
```json
{
    "body": "Changing assignee from was to abergeron.",
    "created_at": "2008-12-24T04:57:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/508",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/508#issuecomment-2549",
    "user": "abergeron"
}
```

Changing assignee from was to abergeron.



---

archive/issue_comments_002550.json:
```json
{
    "body": "It did work with 3.1.4 in other directories.  But it doesn't with 3.2 and up as you pointed out.\n\nLast patch fixes this.",
    "created_at": "2008-12-24T04:57:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/508",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/508#issuecomment-2550",
    "user": "abergeron"
}
```

It did work with 3.1.4 in other directories.  But it doesn't with 3.2 and up as you pointed out.

Last patch fixes this.



---

archive/issue_comments_002551.json:
```json
{
    "body": "Target time for the review: January 12th",
    "created_at": "2008-12-29T21:15:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/508",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/508#issuecomment-2551",
    "user": "GeorgSWeber"
}
```

Target time for the review: January 12th



---

archive/issue_comments_002552.json:
```json
{
    "body": "Rescheduled for January 18th",
    "created_at": "2009-01-15T21:40:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/508",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/508#issuecomment-2552",
    "user": "GeorgSWeber"
}
```

Rescheduled for January 18th



---

archive/issue_comments_002553.json:
```json
{
    "body": "Works fine, and looks good to me. (Apply the v2 patch only; tested with Sage 3.2.3)\n\nI adjusted the milestone because this patch does not interfere with the sphinxification.",
    "created_at": "2009-01-18T23:52:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/508",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/508#issuecomment-2553",
    "user": "GeorgSWeber"
}
```

Works fine, and looks good to me. (Apply the v2 patch only; tested with Sage 3.2.3)

I adjusted the milestone because this patch does not interfere with the sphinxification.



---

archive/issue_comments_002554.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-19T06:14:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/508",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/508#issuecomment-2554",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_002555.json:
```json
{
    "body": "Merged in Sage 3.3.alpha0",
    "created_at": "2009-01-19T06:14:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/508",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/508#issuecomment-2555",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha0
