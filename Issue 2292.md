# Issue 2292: segfault in AbelianGroups

archive/issues_002292.json:
```json
{
    "body": "Assignee: joyner\n\nwdj`@`wooster:~/wdj/sagefiles/sage-2.10.2.rc0$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.10.2, Release Date: 2008-02-22                      |\n| Type notebook() for the GUI, and license() for information.        |\nsage: G.<a,b> = AbelianGroup(2)\nsage: a/b\n/home/wdj/wdj/sagefiles/sage-2.10.2.rc0/local/bin/sage-sage: line 212: 31402 Segmentation fault      (core dumped) sage-ipython -c \"$SAGE_STARTUP_COMMAND;\" \"$`@`\"\n\nOn the other hand, this seems to be okay in perm_groups_named:\n\nwdj`@`wooster:~/wdj/sagefiles/sage-2.10.2.rc0$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.10.2, Release Date: 2008-02-22                      |\n| Type notebook() for the GUI, and license() for information.        |\nsage: G = SymmetricGroup(5)\nsage: G.gens()\n((1,2,3,4,5), (1,2))\nsage: a,b = G.gens()\nsage: a/b\n(2,3,4,5)\n\nIssue created by migration from https://trac.sagemath.org/ticket/2292\n\n",
    "created_at": "2008-02-24T15:16:16Z",
    "labels": [
        "group theory",
        "critical",
        "bug"
    ],
    "title": "segfault in AbelianGroups",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2292",
    "user": "wdj"
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

archive/issue_comments_015204.json:
```json
{
    "body": "This is a more readable version:\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.10.2, Release Date: 2008-02-22                      |\n| Type notebook() for the GUI, and license() for information.        |\nsage: G.<a,b> = AbelianGroup(2)\nsage: a/b\n/home/wdj/wdj/sagefiles/sage-2.10.2.rc0/local/bin/sage-sage: line 212: 31402 Segmentation fault      (core dumped) sage-ipyt on -c \"$SAGE_STARTUP_COMMAND;\" \"$@\"\n```\n\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.10.2, Release Date: 2008-02-22                      |\n| Type notebook() for the GUI, and license() for information.        |\nsage: G = SymmetricGroup(5)\nsage: G.gens()\n((1,2,3,4,5), (1,2))\nsage: a,b = G.gens()\nsage: a/b\n(2,3,4,5)\nsage:\n```\n",
    "created_at": "2008-02-24T15:18:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2292#issuecomment-15204",
    "user": "wdj"
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

archive/issue_comments_015205.json:
```json
{
    "body": "I think I can fix this. I'm running tests on the patch now. The patch will hopefully also fix\nhttp://trac.sagemath.org/sage_trac/ticket/2293",
    "created_at": "2008-02-24T18:15:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2292#issuecomment-15205",
    "user": "wdj"
}
```

I think I can fix this. I'm running tests on the patch now. The patch will hopefully also fix
http://trac.sagemath.org/sage_trac/ticket/2293



---

archive/issue_comments_015206.json:
```json
{
    "body": "Attachment [8681.patch](tarball://root/attachments/some-uuid/ticket2292/8681.patch) by wdj created at 2008-02-24 18:38:48",
    "created_at": "2008-02-24T18:38:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2292#issuecomment-15206",
    "user": "wdj"
}
```

Attachment [8681.patch](tarball://root/attachments/some-uuid/ticket2292/8681.patch) by wdj created at 2008-02-24 18:38:48



---

archive/issue_comments_015207.json:
```json
{
    "body": "Attachment [abelian_groupl_24-02-2008.hg](tarball://root/attachments/some-uuid/ticket2292/abelian_groupl_24-02-2008.hg) by wdj created at 2008-02-24 18:41:21\n\nI attached the patch and the bundle, so the reviewer can use either one. Passed the tests and fixes\nhttp://trac.sagemath.org/sage_trac/ticket/2293",
    "created_at": "2008-02-24T18:41:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2292#issuecomment-15207",
    "user": "wdj"
}
```

Attachment [abelian_groupl_24-02-2008.hg](tarball://root/attachments/some-uuid/ticket2292/abelian_groupl_24-02-2008.hg) by wdj created at 2008-02-24 18:41:21

I attached the patch and the bundle, so the reviewer can use either one. Passed the tests and fixes
http://trac.sagemath.org/sage_trac/ticket/2293



---

archive/issue_comments_015208.json:
```json
{
    "body": "Works for me in 2.10.3.alpha0.",
    "created_at": "2008-02-27T22:19:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2292#issuecomment-15208",
    "user": "mhansen"
}
```

Works for me in 2.10.3.alpha0.



---

archive/issue_comments_015209.json:
```json
{
    "body": "David: Please add the issue that caused the bug as a doctest, especially in case of segfaults. mhansen is adding a doctest in this case.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-27T23:07:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2292#issuecomment-15209",
    "user": "mabshoff"
}
```

David: Please add the issue that caused the bug as a doctest, especially in case of segfaults. mhansen is adding a doctest in this case.

Cheers,

Michael



---

archive/issue_comments_015210.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-27T23:07:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2292#issuecomment-15210",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_015211.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc0",
    "created_at": "2008-02-27T23:07:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2292#issuecomment-15211",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.3.rc0



---

archive/issue_comments_015212.json:
```json
{
    "body": "Attachment [2292-doctest.patch](tarball://root/attachments/some-uuid/ticket2292/2292-doctest.patch) by mabshoff created at 2008-02-27 23:14:45\n\nMerged 2292-doctest.patch (due to unknown parent via GNU patch), but credited to mhansen via hg commit",
    "created_at": "2008-02-27T23:14:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2292",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2292#issuecomment-15212",
    "user": "mabshoff"
}
```

Attachment [2292-doctest.patch](tarball://root/attachments/some-uuid/ticket2292/2292-doctest.patch) by mabshoff created at 2008-02-27 23:14:45

Merged 2292-doctest.patch (due to unknown parent via GNU patch), but credited to mhansen via hg commit
