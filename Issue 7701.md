# Issue 7701: update the openmpi spkg to the latest version

archive/issues_007701.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @jdemeyer\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7701\n\n",
    "created_at": "2009-12-16T02:03:02Z",
    "labels": [
        "component: packages: optional"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "update the openmpi spkg to the latest version",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7701",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

CC:  @jdemeyer



Issue created by migration from https://trac.sagemath.org/ticket/7701





---

archive/issue_comments_065951.json:
```json
{
    "body": "Spkg in progress here:\n\n    http://sage.math.washington.edu/home/wstein/patches/openmpi-1.4.spkg\n\nThis doesn't work, and fails with this error:\n\n```\n/bin/bash ./libtool --tag=CC   --mode=link gcc  -O3 -DNDEBUG   -fvisibility=hidden -module -avoid-version  -o dlopen.la  dlopen.lo -ldl -ldl -lnsl -lutil  -lm\nlibtool: link: ar cru .libs/dlopen.a .libs/dlopen.o\nlibtool: link: ranlib .libs/dlopen.a\nrm: cannot remove `dlopen.la': No such file or directory\nlibtool: link: ( cd \".libs\" && rm \"dlopen.la\" && ln -s \"../dlopen.la\" \"dlopen.la\" )\nrm: cannot remove `dlopen.la': No such file or directory\nmake[3]: *** [dlopen.la] Error 1\nmake[3]: Leaving directory `/scratch/wstein/build/sage-4.3.rc0/spkg/build/openmpi-1.4/src/opal/libltdl'\nmake[2]: *** [all] Error 2\nmake[2]: Leaving directory `/scratch/wstein/build/sage-4.3.rc0/spkg/build/openmpi-1.4/src/opal/libltdl'\nmake[1]: *** [all-recursive] Error 1\nmake[1]: Leaving directory `/scratch/wstein/build/sage-4.3.rc0/spkg/build/openmpi-1.4/src/opal'\nmake: *** [all-recursive] Error 1\nError building\n```\n",
    "created_at": "2009-12-16T02:13:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7701#issuecomment-65951",
    "user": "https://github.com/williamstein"
}
```

Spkg in progress here:

    http://sage.math.washington.edu/home/wstein/patches/openmpi-1.4.spkg

This doesn't work, and fails with this error:

```
/bin/bash ./libtool --tag=CC   --mode=link gcc  -O3 -DNDEBUG   -fvisibility=hidden -module -avoid-version  -o dlopen.la  dlopen.lo -ldl -ldl -lnsl -lutil  -lm
libtool: link: ar cru .libs/dlopen.a .libs/dlopen.o
libtool: link: ranlib .libs/dlopen.a
rm: cannot remove `dlopen.la': No such file or directory
libtool: link: ( cd ".libs" && rm "dlopen.la" && ln -s "../dlopen.la" "dlopen.la" )
rm: cannot remove `dlopen.la': No such file or directory
make[3]: *** [dlopen.la] Error 1
make[3]: Leaving directory `/scratch/wstein/build/sage-4.3.rc0/spkg/build/openmpi-1.4/src/opal/libltdl'
make[2]: *** [all] Error 2
make[2]: Leaving directory `/scratch/wstein/build/sage-4.3.rc0/spkg/build/openmpi-1.4/src/opal/libltdl'
make[1]: *** [all-recursive] Error 1
make[1]: Leaving directory `/scratch/wstein/build/sage-4.3.rc0/spkg/build/openmpi-1.4/src/opal'
make: *** [all-recursive] Error 1
Error building
```




---

archive/issue_comments_065952.json:
```json
{
    "body": "The reason for this error is that newer versions of libtool break when you define $RM=\"rm\", see http://trac.sagemath.org/sage_trac/ticket/7818#comment:28\n\nTemporary work-around is adding `unset RM` to spkg-install",
    "created_at": "2010-01-25T22:30:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7701#issuecomment-65952",
    "user": "https://github.com/vbraun"
}
```

The reason for this error is that newer versions of libtool break when you define $RM="rm", see http://trac.sagemath.org/sage_trac/ticket/7818#comment:28

Temporary work-around is adding `unset RM` to spkg-install



---

archive/issue_comments_065953.json:
```json
{
    "body": "this ticket should be fixed according to the release notes of sage 4.6.2, right ?\n\n#8537: Stefan Reiterer: Update Open MPI package to latest - Sage version is 3 years old! [Reviewed by Volker Braun]",
    "created_at": "2011-03-02T15:07:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7701#issuecomment-65953",
    "user": "https://trac.sagemath.org/admin/accounts/users/thisch"
}
```

this ticket should be fixed according to the release notes of sage 4.6.2, right ?

#8537: Stefan Reiterer: Update Open MPI package to latest - Sage version is 3 years old! [Reviewed by Volker Braun]



---

archive/issue_comments_065954.json:
```json
{
    "body": "Sage-4.6.2 has openmpi-1.4.3 as optional spkg. \n\nRelease manager: Please close this ticket.",
    "created_at": "2011-03-02T15:09:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7701#issuecomment-65954",
    "user": "https://github.com/vbraun"
}
```

Sage-4.6.2 has openmpi-1.4.3 as optional spkg. 

Release manager: Please close this ticket.



---

archive/issue_comments_065955.json:
```json
{
    "body": "any reason why this ticket is still open?",
    "created_at": "2011-05-28T14:42:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7701#issuecomment-65955",
    "user": "https://trac.sagemath.org/admin/accounts/users/thisch"
}
```

any reason why this ticket is still open?



---

archive/issue_comments_065956.json:
```json
{
    "body": "Replying to [comment:4 vbraun]:\n> Sage-4.6.2 has openmpi-1.4.3 as optional spkg. \n> \n> Release manager: Please close this ticket.",
    "created_at": "2011-05-30T07:38:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7701#issuecomment-65956",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:4 vbraun]:
> Sage-4.6.2 has openmpi-1.4.3 as optional spkg. 
> 
> Release manager: Please close this ticket.



---

archive/issue_comments_065957.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-05-30T07:38:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7701#issuecomment-65957",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065958.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-05-30T07:38:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7701",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7701#issuecomment-65958",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate
