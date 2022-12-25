# Issue 5129: numerical noise in roots calculus/calculus.py

archive/issues_005129.json:
```json
{
    "body": "Assignee: @burcin\n\n```\n[jaap@peace sage-3.3.alpha0]$ ./sage -t \"devel/sage/sage/calculus/calculus.py\"\nsage -t  \"devel/sage/sage/calculus/calculus.py\"\n**********************************************************************\nFile \"/home/jaap/Download/sage-3.3.alpha0/devel/sage/sage/calculus/calculus.py\",\nline 3206:\n    sage: f.roots(ring=CC)\nExpected:\n    [(-0.0588115223184495, 1), (1.36050567903502 + 1.51880872209965*I,\n1), (-1.33109991787579 + 1.52241655183732*I, 1), (1.36050567903502 -\n1.51880872209965*I, 1), (-1.33109991787580 - 1.52241655183732*I, 1)]\nGot:\n    [(-0.0588115223184495, 1), (1.36050567903502 + 1.51880872209965*I,\n1), (-1.33109991787580 + 1.52241655183732*I, 1), (1.36050567903502 -\n1.51880872209965*I, 1), (-1.33109991787580 - 1.52241655183732*I, 1)]\n**********************************************************************\nFile \"/home/jaap/Download/sage-3.3.alpha0/devel/sage/sage/calculus/calculus.py\",\nline 3208:\n    sage: (2.5*f).roots(ring=RR)\nExpected:\n    [(-0.0588115223184494, 1)]\nGot:\n    [(-0.0588115223184495, 1)]\n**********************************************************************\nFile \"/home/jaap/Download/sage-3.3.alpha0/devel/sage/sage/calculus/calculus.py\",\nline 3210:\n    sage: f.roots(ring=CC, multiplicities=False)\nExpected:\n    [-0.0588115223184495, 1.36050567903502 + 1.51880872209965*I,\n-1.33109991787579 + 1.52241655183732*I, 1.36050567903502 -\n1.51880872209965*I, -1.33109991787580 - 1.52241655183732*I]\nGot:\n    [-0.0588115223184495, 1.36050567903502 + 1.51880872209965*I,\n-1.33109991787580 + 1.52241655183732*I, 1.36050567903502 -\n1.51880872209965*I, -1.33109991787580 - 1.52241655183732*I]\n**********************************************************************\n1 items had failures:\n   3 of  29 in __main__.example_81\n***Test Failed*** 3 failures.\nFor whitespace errors, see the file\n/home/jaap/Download/sage-3.3.alpha0/tmp/.doctest_calculus.py\n\t [243.9 s]\nexit code: 1024\n\n------------------------------\n\n```\n\nThis is on Fedora 10, 32 bits.\n\nJaap\n\nIssue created by migration from https://trac.sagemath.org/ticket/5129\n\n",
    "created_at": "2009-01-29T19:55:22Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "numerical noise in roots calculus/calculus.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5129",
    "user": "https://github.com/jaapspies"
}
```
Assignee: @burcin

```
[jaap@peace sage-3.3.alpha0]$ ./sage -t "devel/sage/sage/calculus/calculus.py"
sage -t  "devel/sage/sage/calculus/calculus.py"
**********************************************************************
File "/home/jaap/Download/sage-3.3.alpha0/devel/sage/sage/calculus/calculus.py",
line 3206:
    sage: f.roots(ring=CC)
Expected:
    [(-0.0588115223184495, 1), (1.36050567903502 + 1.51880872209965*I,
1), (-1.33109991787579 + 1.52241655183732*I, 1), (1.36050567903502 -
1.51880872209965*I, 1), (-1.33109991787580 - 1.52241655183732*I, 1)]
Got:
    [(-0.0588115223184495, 1), (1.36050567903502 + 1.51880872209965*I,
1), (-1.33109991787580 + 1.52241655183732*I, 1), (1.36050567903502 -
1.51880872209965*I, 1), (-1.33109991787580 - 1.52241655183732*I, 1)]
**********************************************************************
File "/home/jaap/Download/sage-3.3.alpha0/devel/sage/sage/calculus/calculus.py",
line 3208:
    sage: (2.5*f).roots(ring=RR)
Expected:
    [(-0.0588115223184494, 1)]
Got:
    [(-0.0588115223184495, 1)]
**********************************************************************
File "/home/jaap/Download/sage-3.3.alpha0/devel/sage/sage/calculus/calculus.py",
line 3210:
    sage: f.roots(ring=CC, multiplicities=False)
Expected:
    [-0.0588115223184495, 1.36050567903502 + 1.51880872209965*I,
-1.33109991787579 + 1.52241655183732*I, 1.36050567903502 -
1.51880872209965*I, -1.33109991787580 - 1.52241655183732*I]
Got:
    [-0.0588115223184495, 1.36050567903502 + 1.51880872209965*I,
-1.33109991787580 + 1.52241655183732*I, 1.36050567903502 -
1.51880872209965*I, -1.33109991787580 - 1.52241655183732*I]
**********************************************************************
1 items had failures:
   3 of  29 in __main__.example_81
***Test Failed*** 3 failures.
For whitespace errors, see the file
/home/jaap/Download/sage-3.3.alpha0/tmp/.doctest_calculus.py
	 [243.9 s]
exit code: 1024

------------------------------

```

This is on Fedora 10, 32 bits.

Jaap

Issue created by migration from https://trac.sagemath.org/ticket/5129





---

archive/issue_comments_039126.json:
```json
{
    "body": "This is a blocker!\n\nCheers,\n\nMichael",
    "created_at": "2009-02-03T17:37:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5129",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5129#issuecomment-39126",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is a blocker!

Cheers,

Michael



---

archive/issue_comments_039127.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-03T17:37:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5129",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5129#issuecomment-39127",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_039128.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2009-02-03T17:37:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5129",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5129#issuecomment-39128",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_039129.json:
```json
{
    "body": "Changing assignee from @burcin to mabshoff.",
    "created_at": "2009-02-03T17:37:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5129",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5129#issuecomment-39129",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from @burcin to mabshoff.



---

archive/issue_comments_039130.json:
```json
{
    "body": "Attachment [trac_5129.patch](tarball://root/attachments/some-uuid/ticket5129/trac_5129.patch) by mabshoff created at 2009-02-03 18:24:56",
    "created_at": "2009-02-03T18:24:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5129",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5129#issuecomment-39130",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_5129.patch](tarball://root/attachments/some-uuid/ticket5129/trac_5129.patch) by mabshoff created at 2009-02-03 18:24:56



---

archive/issue_comments_039131.json:
```json
{
    "body": "Patch is up.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-03T18:25:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5129",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5129#issuecomment-39131",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch is up.

Cheers,

Michael



---

archive/issue_comments_039132.json:
```json
{
    "body": "On Fedora 9, 32 bits:\n\n```\n[jaap@paix sage-3.3.alpha3]$ ./sage -t \"devel/sage/sage/calculus/calculus.py\"\nsage -t  \"devel/sage/sage/calculus/calculus.py\"             \n\t [171.4 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 171.4 seconds\n\n```\n\nLooks good to me!\n\nJaap",
    "created_at": "2009-02-03T18:36:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5129",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5129#issuecomment-39132",
    "user": "https://github.com/jaapspies"
}
```

On Fedora 9, 32 bits:

```
[jaap@paix sage-3.3.alpha3]$ ./sage -t "devel/sage/sage/calculus/calculus.py"
sage -t  "devel/sage/sage/calculus/calculus.py"             
	 [171.4 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 171.4 seconds

```

Looks good to me!

Jaap



---

archive/issue_comments_039133.json:
```json
{
    "body": "Merged in Sage 3.3.alpha5.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-03T18:51:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5129",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5129#issuecomment-39133",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha5.

Cheers,

Michael



---

archive/issue_events_011888.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-03T18:51:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5129",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5129#event-11888"
}
```



---

archive/issue_comments_039134.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-03T18:51:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5129",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5129#issuecomment-39134",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
