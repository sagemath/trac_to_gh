# Issue 5841: reenable interface/lisp.py doctests

archive/issues_005841.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  mvngu mhansen jdemeyer\n\n#5662 introduced a problem when using old clisp builds which we need to use on RHEL5/Itanium since any more current clisp is hopelessly broken there. But since Gonzalo's patch fixes a real issue in the clisp interface I don't want to change any of that patch.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5841\n\n",
    "created_at": "2009-04-21T06:26:48Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "title": "reenable interface/lisp.py doctests",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5841",
    "user": "mabshoff"
}
```
Assignee: mabshoff

CC:  mvngu mhansen jdemeyer

#5662 introduced a problem when using old clisp builds which we need to use on RHEL5/Itanium since any more current clisp is hopelessly broken there. But since Gonzalo's patch fixes a real issue in the clisp interface I don't want to change any of that patch.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5841





---

archive/issue_comments_045924.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-04-21T06:29:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5841#issuecomment-45924",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_045925.json:
```json
{
    "body": "Changing priority from blocker to critical.",
    "created_at": "2009-06-15T23:26:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5841#issuecomment-45925",
    "user": "was"
}
```

Changing priority from blocker to critical.



---

archive/issue_comments_045926.json:
```json
{
    "body": "If we've released for 2 months without fixing this, it doesn't make sense to keep it as a blocker. Note that the lisp interface is in fact 100% completely broken right now.",
    "created_at": "2009-06-15T23:26:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5841#issuecomment-45926",
    "user": "was"
}
```

If we've released for 2 months without fixing this, it doesn't make sense to keep it as a blocker. Note that the lisp interface is in fact 100% completely broken right now.



---

archive/issue_comments_045927.json:
```json
{
    "body": "As far as I can tell, this is all no longer true.\n\n```\n./sage -t devel/sage/sage/interfaces/lisp.py\nsage -t  \"devel/sage/sage/interfaces/lisp.py\"               \n\t [5.7 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 5.7 seconds\n```\n\nRandom tests that seem to be working fine:\n\n```\nsage:  lisp._equality_symbol()\n---------------------------------------------------------------------------\n<snip>\nNotImplementedError: We should never reach here in the Lisp interface. Please report this as a bug.\nsage: lisp.function_call('sin', ['2'])\n0.90929741\nsage: lisp.sin(2)\n0.90929741\n```\n\nI figure this should be closed...",
    "created_at": "2010-05-26T21:05:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5841#issuecomment-45927",
    "user": "kcrisman"
}
```

As far as I can tell, this is all no longer true.

```
./sage -t devel/sage/sage/interfaces/lisp.py
sage -t  "devel/sage/sage/interfaces/lisp.py"               
	 [5.7 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 5.7 seconds
```

Random tests that seem to be working fine:

```
sage:  lisp._equality_symbol()
---------------------------------------------------------------------------
<snip>
NotImplementedError: We should never reach here in the Lisp interface. Please report this as a bug.
sage: lisp.function_call('sin', ['2'])
0.90929741
sage: lisp.sin(2)
0.90929741
```

I figure this should be closed...



---

archive/issue_comments_045928.json:
```json
{
    "body": "To release manager: I believe this should be closed. It's not even clear what doctests were ever disabled unless you look around a bit.  \n\nIn fact, #6294 seems to have cleared this up.  I suggest it be closed.",
    "created_at": "2011-01-19T21:11:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5841#issuecomment-45928",
    "user": "kcrisman"
}
```

To release manager: I believe this should be closed. It's not even clear what doctests were ever disabled unless you look around a bit.  

In fact, #6294 seems to have cleared this up.  I suggest it be closed.



---

archive/issue_comments_045929.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-01-19T21:11:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5841#issuecomment-45929",
    "user": "kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_045930.json:
```json
{
    "body": "I really don't think this is 'positive review', but if this gets the release manager's attention to close the ticket, I guess I'll do it ;-)",
    "created_at": "2011-03-12T03:45:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5841#issuecomment-45930",
    "user": "kcrisman"
}
```

I really don't think this is 'positive review', but if this gets the release manager's attention to close the ticket, I guess I'll do it ;-)



---

archive/issue_comments_045931.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-03-12T03:45:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5841#issuecomment-45931",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_045932.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2011-03-17T09:47:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5841#issuecomment-45932",
    "user": "jdemeyer"
}
```

Resolution: invalid
