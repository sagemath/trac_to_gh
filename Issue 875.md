# Issue 875: further work needed on frast Sage --> PARI int conversion

archive/issues_000875.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\n22:42 < cwitty_> I was looking at #467, and I just crashed SAGE with a PARI stack overflow.\n22:43 < cwitty_> I thought the stack was supposed to resize automatically, or something?  (Or at least\n                 not crash SAGE.)\n22:44 < cwitty_> sage: n = 10^10000000\n22:44 < cwitty_> sage: %time _ = pari(n)\n22:44 < cwitty_>   ***   the PARI stack overflows !\n22:44 < cwitty_>   current stack size: 8000000 (7.629 Mbytes)\n22:44 < cwitty_>   [hint] you can increase GP stack with allocatemem()\n22:44 < cwitty_> /home/cwitty/sage/local/bin/sage-sage: line 205: 25703 Aborted\n                 sage-ipython -c \"$SAGE_STARTUP_COMMAND;\" \"$@\"\n22:44 < cwitty_> (This is after I applied the patch from #467.)\n22:45 < williamstein> weird.\n22:45 < williamstein> it should automatically double *if* the author correctly uses _sig_on/_sig_off\n22:47 < cwitty_> This is the ZZ->Pari fast coercion patch, and I'm pretty sure (from skimming the patch)\n                 that he never touches _sig_on/_sig_off.  So that's probably it.\n```\n\n\n*THE SOLUTION*\n\nNeed to move code for _pari_c to gen.pyx as a method off of the Pari object.\nThen wrap the call to the function in convert.c in _sig_on / _sig_off.\nThe _sig_on / _sig_off macros are specially constructed *only* in gen.pyx \nto automatically double the pari stack if we run out of memory.\n\nIssue created by migration from https://trac.sagemath.org/ticket/875\n\n",
    "created_at": "2007-10-13T06:22:51Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.10",
    "title": "further work needed on frast Sage --> PARI int conversion",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/875",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody


```
22:42 < cwitty_> I was looking at #467, and I just crashed SAGE with a PARI stack overflow.
22:43 < cwitty_> I thought the stack was supposed to resize automatically, or something?  (Or at least
                 not crash SAGE.)
22:44 < cwitty_> sage: n = 10^10000000
22:44 < cwitty_> sage: %time _ = pari(n)
22:44 < cwitty_>   ***   the PARI stack overflows !
22:44 < cwitty_>   current stack size: 8000000 (7.629 Mbytes)
22:44 < cwitty_>   [hint] you can increase GP stack with allocatemem()
22:44 < cwitty_> /home/cwitty/sage/local/bin/sage-sage: line 205: 25703 Aborted
                 sage-ipython -c "$SAGE_STARTUP_COMMAND;" "$@"
22:44 < cwitty_> (This is after I applied the patch from #467.)
22:45 < williamstein> weird.
22:45 < williamstein> it should automatically double *if* the author correctly uses _sig_on/_sig_off
22:47 < cwitty_> This is the ZZ->Pari fast coercion patch, and I'm pretty sure (from skimming the patch)
                 that he never touches _sig_on/_sig_off.  So that's probably it.
```


*THE SOLUTION*

Need to move code for _pari_c to gen.pyx as a method off of the Pari object.
Then wrap the call to the function in convert.c in _sig_on / _sig_off.
The _sig_on / _sig_off macros are specially constructed *only* in gen.pyx 
to automatically double the pari stack if we run out of memory.

Issue created by migration from https://trac.sagemath.org/ticket/875





---

archive/issue_comments_005394.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-13T15:20:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/875#issuecomment-5394",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005395.json:
```json
{
    "body": "Changing assignee from somebody to @craigcitro.",
    "created_at": "2007-10-13T15:20:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/875#issuecomment-5395",
    "user": "https://github.com/craigcitro"
}
```

Changing assignee from somebody to @craigcitro.



---

archive/issue_comments_005396.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2007-10-20T22:15:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/875#issuecomment-5396",
    "user": "https://github.com/williamstein"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_005397.json:
```json
{
    "body": "This patch fixes the problem above, and adds a doctest about it. It took a bit of fiddling to get this to work -- the point is that you need to load the Integer type in order to make this work in gen.pyx, but you can't do that at compile time (it would be a circular dependency). This is further compounded by the fact that the code in gen.pyx actually gets *used* in the process of loading other parts of the Sage library -- that is, you create and use Sage's PariInstance in the process of loading various modules, so things had to be touched up in a few places to get things to load.\n\nAlso, re: William's note above about \"hacking the Python/C API\" -- that's not for this patch, that's for the upcoming patch on ticket 864. That might have to wait until 2.9 at the rate our new versions are coming these days, though. ;)",
    "created_at": "2007-10-27T08:07:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/875#issuecomment-5397",
    "user": "https://github.com/craigcitro"
}
```

This patch fixes the problem above, and adds a doctest about it. It took a bit of fiddling to get this to work -- the point is that you need to load the Integer type in order to make this work in gen.pyx, but you can't do that at compile time (it would be a circular dependency). This is further compounded by the fact that the code in gen.pyx actually gets *used* in the process of loading other parts of the Sage library -- that is, you create and use Sage's PariInstance in the process of loading various modules, so things had to be touched up in a few places to get things to load.

Also, re: William's note above about "hacking the Python/C API" -- that's not for this patch, that's for the upcoming patch on ticket 864. That might have to wait until 2.9 at the rate our new versions are coming these days, though. ;)



---

archive/issue_comments_005398.json:
```json
{
    "body": "Attachment [trac_875.hg](tarball://root/attachments/some-uuid/ticket875/trac_875.hg) by cwitty created at 2007-10-27 19:45:45",
    "created_at": "2007-10-27T19:45:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/875#issuecomment-5398",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [trac_875.hg](tarball://root/attachments/some-uuid/ticket875/trac_875.hg) by cwitty created at 2007-10-27 19:45:45



---

archive/issue_comments_005399.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-27T19:45:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/875",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/875#issuecomment-5399",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Resolution: fixed
