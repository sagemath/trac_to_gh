# Issue 9277: Flint's spkg-check file does not work on 64-bit (SAGE64 only works on OS X)

archive/issues_009277.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @jaapspies\n\nJust when I thought I'd got rid of all the junk like this from spkg-install files:\n\nIssue created by migration from https://trac.sagemath.org/ticket/9277\n\n",
    "created_at": "2010-06-19T21:38:52Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5",
    "title": "Flint's spkg-check file does not work on 64-bit (SAGE64 only works on OS X)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9277",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: @aghitza

CC:  @jaapspies

Just when I thought I'd got rid of all the junk like this from spkg-install files:

Issue created by migration from https://trac.sagemath.org/ticket/9277





---

archive/issue_comments_087241.json:
```json
{
    "body": "Changing component from algebra to build.",
    "created_at": "2010-06-19T21:44:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9277#issuecomment-87241",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing component from algebra to build.



---

archive/issue_comments_087242.json:
```json
{
    "body": "Changing assignee from @aghitza to GeorgSWeber.",
    "created_at": "2010-06-19T21:44:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9277#issuecomment-87242",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing assignee from @aghitza to GeorgSWeber.



---

archive/issue_comments_087243.json:
```json
{
    "body": "Here's an updated package\n\nhttp://boxen.math.washington.edu/home/kirkby/patches/flint-1.5.0.p5.spkg\n\nwhich has a trivial fix to remove the OS X restriction. \n\nIt was also desirable to remove these 3 lines from spkg-install, since if SAGE_CHECK was set to yes, the test suite got executed twice, which just wastes time. \n\n```\nif [ \"$SAGE_CHECK\" = \"yes\" ]; then\n    cd ..; ./spkg-check\nfi\n```\n\nAfter that change, on my Sun Ultra 27 running OpenSolaris x64, the test suite builds, runs once, and passes all the tests. \n\n\n```\nTesting zmod_poly_factor()... Cpu = 2060 ms  Wall = 2061 ms ... ok\nTesting zmod_poly_2x2_mat_mul_classical_strassen()... Cpu = 330 ms  Wall = 326 ms ... ok\nTesting zmod_poly_2x2_mat_mul()... Cpu = 1070 ms  Wall = 1073 ms ... ok\n\nAll tests passed\nTesting zmod_mat_row_reduce_gauss()... Cpu = 470 ms  Wall = 473 ms ... ok\n\nAll tests passed\nTesting ZZ_to_fmpz()... Cpu = 530 ms  Wall = 536 ms ... ok\nTesting ZZ_to_F_mpz()... Cpu = 460 ms  Wall = 457 ms ... ok\nTesting ZZX_to_fmpz_poly()... Cpu = 1710 ms  Wall = 1710 ms ... ok\n\nAll tests passed\nNow cleaning up tmp files.\nrm: Cannot remove any directory in the path of the current working directory\n/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/flint-1.5.0.p5\nMaking Sage/Python scripts relocatable...\nMaking script relocatable\nFinished installing flint-1.5.0.p5.spkg\n```",
    "created_at": "2010-06-19T23:57:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9277#issuecomment-87243",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Here's an updated package

http://boxen.math.washington.edu/home/kirkby/patches/flint-1.5.0.p5.spkg

which has a trivial fix to remove the OS X restriction. 

It was also desirable to remove these 3 lines from spkg-install, since if SAGE_CHECK was set to yes, the test suite got executed twice, which just wastes time. 

```
if [ "$SAGE_CHECK" = "yes" ]; then
    cd ..; ./spkg-check
fi
```

After that change, on my Sun Ultra 27 running OpenSolaris x64, the test suite builds, runs once, and passes all the tests. 


```
Testing zmod_poly_factor()... Cpu = 2060 ms  Wall = 2061 ms ... ok
Testing zmod_poly_2x2_mat_mul_classical_strassen()... Cpu = 330 ms  Wall = 326 ms ... ok
Testing zmod_poly_2x2_mat_mul()... Cpu = 1070 ms  Wall = 1073 ms ... ok

All tests passed
Testing zmod_mat_row_reduce_gauss()... Cpu = 470 ms  Wall = 473 ms ... ok

All tests passed
Testing ZZ_to_fmpz()... Cpu = 530 ms  Wall = 536 ms ... ok
Testing ZZ_to_F_mpz()... Cpu = 460 ms  Wall = 457 ms ... ok
Testing ZZX_to_fmpz_poly()... Cpu = 1710 ms  Wall = 1710 ms ... ok

All tests passed
Now cleaning up tmp files.
rm: Cannot remove any directory in the path of the current working directory
/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/flint-1.5.0.p5
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing flint-1.5.0.p5.spkg
```



---

archive/issue_comments_087244.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-19T23:57:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9277#issuecomment-87244",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_events_022854.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/drkirkby",
    "created_at": "2010-06-19T23:57:10Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9277",
    "milestone": "sage-4.4.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9277#event-22854"
}
```



---

archive/issue_comments_087245.json:
```json
{
    "body": "Attachment [9277.patch](tarball://root/attachments/some-uuid/ticket9277/9277.patch) by drkirkby created at 2010-06-19 23:58:59\n\nMercurial patch which permits a 64-bit build of test suite and ensures tests dont run twice",
    "created_at": "2010-06-19T23:58:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9277#issuecomment-87245",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [9277.patch](tarball://root/attachments/some-uuid/ticket9277/9277.patch) by drkirkby created at 2010-06-19 23:58:59

Mercurial patch which permits a 64-bit build of test suite and ensures tests dont run twice



---

archive/issue_comments_087246.json:
```json
{
    "body": "Looks good to me.\n\nPositive review.\n\nJaap",
    "created_at": "2010-06-20T10:21:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9277#issuecomment-87246",
    "user": "https://github.com/jaapspies"
}
```

Looks good to me.

Positive review.

Jaap



---

archive/issue_comments_087247.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-20T10:21:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9277#issuecomment-87247",
    "user": "https://github.com/jaapspies"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_022855.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-06-25T15:42:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9277",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9277#event-22855"
}
```



---

archive/issue_comments_087248.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-25T15:42:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9277",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9277#issuecomment-87248",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
