# Issue 2292: segfault in AbelianGroups

archive/issues_002292.json:
```json
{
    "body": "Assignee: joyner\n\nwdj`@`wooster:~/wdj/sagefiles/sage-2.10.2.rc0$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.10.2, Release Date: 2008-02-22                      |\n| Type notebook() for the GUI, and license() for information.        |\nsage: G.<a,b> = AbelianGroup(2)\nsage: a/b\n/home/wdj/wdj/sagefiles/sage-2.10.2.rc0/local/bin/sage-sage: line 212: 31402 Segmentation fault      (core dumped) sage-ipython -c \"$SAGE_STARTUP_COMMAND;\" \"$`@`\"\n\nOn the other hand, this seems to be okay in perm_groups_named:\n\nwdj`@`wooster:~/wdj/sagefiles/sage-2.10.2.rc0$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.10.2, Release Date: 2008-02-22                      |\n| Type notebook() for the GUI, and license() for information.        |\nsage: G = SymmetricGroup(5)\nsage: G.gens()\n((1,2,3,4,5), (1,2))\nsage: a,b = G.gens()\nsage: a/b\n(2,3,4,5)\n\nIssue created by migration from https://trac.sagemath.org/ticket/2292\n\n",
    "created_at": "2008-02-24T15:16:16Z",
    "labels": [
        "component: group theory",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "segfault in AbelianGroups",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2292",
    "user": "https://github.com/wdjoyner"
}
```
Assignee: joyner

wdj`@`wooster:~/wdj/sagefiles/sage-2.10.2.rc0$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.10.2, Release Date: 2008-02-22                      |
| Type notebook() for the GUI, and license() for information.        |
sage: G.<a,b> = AbelianGroup(2)
sage: a/b
/home/wdj/wdj/sagefiles/sage-2.10.2.rc0/local/bin/sage-sage: line 212: 31402 Segmentation fault      (core dumped) sage-ipython -c "$SAGE_STARTUP_COMMAND;" "$`@`"

On the other hand, this seems to be okay in perm_groups_named:

wdj`@`wooster:~/wdj/sagefiles/sage-2.10.2.rc0$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.10.2, Release Date: 2008-02-22                      |
| Type notebook() for the GUI, and license() for information.        |
sage: G = SymmetricGroup(5)
sage: G.gens()
((1,2,3,4,5), (1,2))
sage: a,b = G.gens()
sage: a/b
(2,3,4,5)

Issue created by migration from https://trac.sagemath.org/ticket/2292





---

archive/issue_comments_015171.json:
```json
{
    "body": "This is a more readable version:\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.10.2, Release Date: 2008-02-22                      |\n| Type notebook() for the GUI, and license() for information.        |\nsage: G.<a,b> = AbelianGroup(2)\nsage: a/b\n/home/wdj/wdj/sagefiles/sage-2.10.2.rc0/local/bin/sage-sage: line 212: 31402 Segmentation fault      (core dumped) sage-ipyt on -c \"$SAGE_STARTUP_COMMAND;\" \"$@\"\n```\n\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.10.2, Release Date: 2008-02-22                      |\n| Type notebook() for the GUI, and license() for information.        |\nsage: G = SymmetricGroup(5)\nsage: G.gens()\n((1,2,3,4,5), (1,2))\nsage: a,b = G.gens()\nsage: a/b\n(2,3,4,5)\nsage:\n```\n",
    "created_at": "2008-02-24T15:18:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2292#issuecomment-15171",
    "user": "https://github.com/wdjoyner"
}
```

This is a more readable version:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.10.2, Release Date: 2008-02-22                      |
| Type notebook() for the GUI, and license() for information.        |
sage: G.<a,b> = AbelianGroup(2)
sage: a/b
/home/wdj/wdj/sagefiles/sage-2.10.2.rc0/local/bin/sage-sage: line 212: 31402 Segmentation fault      (core dumped) sage-ipyt on -c "$SAGE_STARTUP_COMMAND;" "$@"
```



```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.10.2, Release Date: 2008-02-22                      |
| Type notebook() for the GUI, and license() for information.        |
sage: G = SymmetricGroup(5)
sage: G.gens()
((1,2,3,4,5), (1,2))
sage: a,b = G.gens()
sage: a/b
(2,3,4,5)
sage:
```




---

archive/issue_comments_015172.json:
```json
{
    "body": "I think I can fix this. I'm running tests on the patch now. The patch will hopefully also fix\nhttp://trac.sagemath.org/sage_trac/ticket/2293",
    "created_at": "2008-02-24T18:15:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2292#issuecomment-15172",
    "user": "https://github.com/wdjoyner"
}
```

I think I can fix this. I'm running tests on the patch now. The patch will hopefully also fix
http://trac.sagemath.org/sage_trac/ticket/2293



---

archive/issue_comments_015173.json:
```json
{
    "body": "Attachment [8681.patch](tarball://root/attachments/some-uuid/ticket2292/8681.patch) by @wdjoyner created at 2008-02-24 18:38:48",
    "created_at": "2008-02-24T18:38:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2292#issuecomment-15173",
    "user": "https://github.com/wdjoyner"
}
```

Attachment [8681.patch](tarball://root/attachments/some-uuid/ticket2292/8681.patch) by @wdjoyner created at 2008-02-24 18:38:48



---

archive/issue_comments_015174.json:
```json
{
    "body": "Attachment [abelian_groupl_24-02-2008.hg](tarball://root/attachments/some-uuid/ticket2292/abelian_groupl_24-02-2008.hg) by @wdjoyner created at 2008-02-24 18:41:21\n\nI attached the patch and the bundle, so the reviewer can use either one. Passed the tests and fixes\nhttp://trac.sagemath.org/sage_trac/ticket/2293",
    "created_at": "2008-02-24T18:41:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2292#issuecomment-15174",
    "user": "https://github.com/wdjoyner"
}
```

Attachment [abelian_groupl_24-02-2008.hg](tarball://root/attachments/some-uuid/ticket2292/abelian_groupl_24-02-2008.hg) by @wdjoyner created at 2008-02-24 18:41:21

I attached the patch and the bundle, so the reviewer can use either one. Passed the tests and fixes
http://trac.sagemath.org/sage_trac/ticket/2293



---

archive/issue_comments_015175.json:
```json
{
    "body": "Works for me in 2.10.3.alpha0.",
    "created_at": "2008-02-27T22:19:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2292#issuecomment-15175",
    "user": "https://github.com/mwhansen"
}
```

Works for me in 2.10.3.alpha0.



---

archive/issue_comments_015176.json:
```json
{
    "body": "David: Please add the issue that caused the bug as a doctest, especially in case of segfaults. mhansen is adding a doctest in this case.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-27T23:07:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2292#issuecomment-15176",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

David: Please add the issue that caused the bug as a doctest, especially in case of segfaults. mhansen is adding a doctest in this case.

Cheers,

Michael



---

archive/issue_comments_015177.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-27T23:07:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2292#issuecomment-15177",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_002467.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-27T23:07:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2292",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2292#event-2467"
}
```



---

archive/issue_comments_015178.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc0",
    "created_at": "2008-02-27T23:07:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2292#issuecomment-15178",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.3.rc0



---

archive/issue_comments_015179.json:
```json
{
    "body": "Attachment [2292-doctest.patch](tarball://root/attachments/some-uuid/ticket2292/2292-doctest.patch) by mabshoff created at 2008-02-27 23:14:45\n\nMerged 2292-doctest.patch (due to unknown parent via GNU patch), but credited to mhansen via hg commit",
    "created_at": "2008-02-27T23:14:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2292#issuecomment-15179",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [2292-doctest.patch](tarball://root/attachments/some-uuid/ticket2292/2292-doctest.patch) by mabshoff created at 2008-02-27 23:14:45

Merged 2292-doctest.patch (due to unknown parent via GNU patch), but credited to mhansen via hg commit
