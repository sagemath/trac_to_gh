# Issue 6675: doctest failure in sage/sage/misc/sagedoc.py

archive/issues_006675.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: sagedoc.py\n\n```\nBuilt from scratch on\n\nLinux cartan 2.6.28-15-generic #48-Ubuntu SMP Wed Jul 29 08:53:35 UTC\n2009 x86_64 GNU/Linux\n\n(MacBook running 64-bit Ubuntu).\n\nRunning make test gave one failing doctest, which is repeatable:\n\n[ghitza@cartan sage-4.1.1.rc1]$ ./sage -t devel/sage/sage/misc/sagedoc.py\nsage -t  \"devel/sage/sage/misc/sagedoc.py\"\n**********************************************************************\nFile \"/opt/sage-4.1.1.rc1/devel/sage/sage/misc/sagedoc.py\", line 360:\n   sage: 'abvar/homology' in _search_src_or_doc('doc', 'homology',\n'variety', interact=False)\nExpected:\n   True\nGot:\n   False\n**********************************************************************\n1 items had failures:\n  1 of   6 in __main__.example_5\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /opt/sage-4.1.1.rc1/tmp/.doctest_sagedoc.py\n        [5.6 s]\nexit code: 1024\n\n----------------------------------------------------------------------\nThe following tests failed:\n\n\n       sage -t  \"devel/sage/sage/misc/sagedoc.py\"\nTotal time for all tests: 5.6 seconds\n```\nThis was reported in [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/37d851338ed69c6a/289094b891882b2e).\n\nIssue created by migration from https://trac.sagemath.org/ticket/6675\n\n",
    "created_at": "2009-08-05T12:32:47Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "doctest failure in sage/sage/misc/sagedoc.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6675",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: tbd

Keywords: sagedoc.py

```
Built from scratch on

Linux cartan 2.6.28-15-generic #48-Ubuntu SMP Wed Jul 29 08:53:35 UTC
2009 x86_64 GNU/Linux

(MacBook running 64-bit Ubuntu).

Running make test gave one failing doctest, which is repeatable:

[ghitza@cartan sage-4.1.1.rc1]$ ./sage -t devel/sage/sage/misc/sagedoc.py
sage -t  "devel/sage/sage/misc/sagedoc.py"
**********************************************************************
File "/opt/sage-4.1.1.rc1/devel/sage/sage/misc/sagedoc.py", line 360:
   sage: 'abvar/homology' in _search_src_or_doc('doc', 'homology',
'variety', interact=False)
Expected:
   True
Got:
   False
**********************************************************************
1 items had failures:
  1 of   6 in __main__.example_5
***Test Failed*** 1 failures.
For whitespace errors, see the file /opt/sage-4.1.1.rc1/tmp/.doctest_sagedoc.py
        [5.6 s]
exit code: 1024

----------------------------------------------------------------------
The following tests failed:


       sage -t  "devel/sage/sage/misc/sagedoc.py"
Total time for all tests: 5.6 seconds
```
This was reported in [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/37d851338ed69c6a/289094b891882b2e).

Issue created by migration from https://trac.sagemath.org/ticket/6675





---

archive/issue_comments_054766.json:
```json
{
    "body": "The same problem occurs on \n\n```\nLinux artin 2.6.30-ARCH #1 SMP PREEMPT Fri Jul 31 18:10:38 UTC 2009 i686 Intel(R) Core(TM)2 Duo CPU T9300 @ 2.50GHz GenuineIntel GNU/Linux\n```\n\na Dell laptop running 32-bit Archlinux.",
    "created_at": "2009-08-05T12:36:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6675#issuecomment-54766",
    "user": "https://github.com/aghitza"
}
```

The same problem occurs on 

```
Linux artin 2.6.30-ARCH #1 SMP PREEMPT Fri Jul 31 18:10:38 UTC 2009 i686 Intel(R) Core(TM)2 Duo CPU T9300 @ 2.50GHz GenuineIntel GNU/Linux
```

a Dell laptop running 32-bit Archlinux.



---

archive/issue_comments_054767.json:
```json
{
    "body": "I believe that this is fixed by #6674.  That is, the failure here is because the reference manual didn't build during the 'make' process, and it didn't build because of the issue discussed and solved at #6674.  Since the reference manual didn't build, searching the docs produced no results, hence the doctest failure here.  If someone can confirm this, I think we can close this ticket.",
    "created_at": "2009-08-05T21:37:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6675#issuecomment-54767",
    "user": "https://github.com/jhpalmieri"
}
```

I believe that this is fixed by #6674.  That is, the failure here is because the reference manual didn't build during the 'make' process, and it didn't build because of the issue discussed and solved at #6674.  Since the reference manual didn't build, searching the docs produced no results, hence the doctest failure here.  If someone can confirm this, I think we can close this ticket.



---

archive/issue_events_015748.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-08-12T15:40:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6675",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6675#event-15748"
}
```



---

archive/issue_comments_054768.json:
```json
{
    "body": "This has been fixed by #6674.",
    "created_at": "2009-08-12T15:40:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6675#issuecomment-54768",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

This has been fixed by #6674.



---

archive/issue_comments_054769.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-12T15:40:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6675#issuecomment-54769",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
