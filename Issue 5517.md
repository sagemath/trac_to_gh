# Issue 5517: cvxopt-0.9.p7: build failure due to missing perl modules

archive/issues_005517.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe error reported by `cvxopt-0.9.p7` is:\n\n```\nCan't locate File/Copy.pm in @INC (@INC contains: /etc/perl /usr/local/lib/perl/5.10.0 /usr/local/share/perl/5.10.0 /usr/lib/perl5 /usr/share/perl5 /usr/lib/perl/5.10 /usr/share/perl/5.10 /usr/local/lib/site_perl .) at ./spkg-install line 2.\nBEGIN failed--compilation aborted at ./spkg-install line 2.\n```\n\nI did have perl installed in the system, but only the `perl-base` package (5.10.0-19, debian/lenny).\n\nHowever, the `File/Copy.pm` module is in `perl-modules` package, which wasn't installed in my system (`perl-base` priority is required, and `perl-modules` priority is standard).\n\nThe workaround was to `apt-get install perl-modules`; maybe this issue with `File/Copy.pm` could be checked in the prereq spkg?\n\nIssue created by migration from https://trac.sagemath.org/ticket/5517\n\n",
    "created_at": "2009-03-14T16:08:06Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "cvxopt-0.9.p7: build failure due to missing perl modules",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5517",
    "user": "@tornaria"
}
```
Assignee: mabshoff

The error reported by `cvxopt-0.9.p7` is:

```
Can't locate File/Copy.pm in @INC (@INC contains: /etc/perl /usr/local/lib/perl/5.10.0 /usr/local/share/perl/5.10.0 /usr/lib/perl5 /usr/share/perl5 /usr/lib/perl/5.10 /usr/share/perl/5.10 /usr/local/lib/site_perl .) at ./spkg-install line 2.
BEGIN failed--compilation aborted at ./spkg-install line 2.
```

I did have perl installed in the system, but only the `perl-base` package (5.10.0-19, debian/lenny).

However, the `File/Copy.pm` module is in `perl-modules` package, which wasn't installed in my system (`perl-base` priority is required, and `perl-modules` priority is standard).

The workaround was to `apt-get install perl-modules`; maybe this issue with `File/Copy.pm` could be checked in the prereq spkg?

Issue created by migration from https://trac.sagemath.org/ticket/5517





---

archive/issue_comments_042880.json:
```json
{
    "body": "The real fix here is to get rid of the dependency since it is introduced by the Fortran library handling code written by Josh Kantor. The spkg-install should just be a shell script instead of a perl script given that we only copy two different setup.py files depending on the Fortran runtime used.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-14T17:03:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5517",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5517#issuecomment-42880",
    "user": "mabshoff"
}
```

The real fix here is to get rid of the dependency since it is introduced by the Fortran library handling code written by Josh Kantor. The spkg-install should just be a shell script instead of a perl script given that we only copy two different setup.py files depending on the Fortran runtime used.

Cheers,

Michael



---

archive/issue_comments_042881.json:
```json
{
    "body": "Attachment [trac_5517.cvxopt.patch](tarball://root/attachments/some-uuid/ticket5517/trac_5517.cvxopt.patch) by @tornaria created at 2009-05-01 21:03:31\n\npatch for cvxopt-0.9.p7.spkg: replace spkg-install perl script by a bash script, eliminating the dependency on perl",
    "created_at": "2009-05-01T21:03:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5517",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5517#issuecomment-42881",
    "user": "@tornaria"
}
```

Attachment [trac_5517.cvxopt.patch](tarball://root/attachments/some-uuid/ticket5517/trac_5517.cvxopt.patch) by @tornaria created at 2009-05-01 21:03:31

patch for cvxopt-0.9.p7.spkg: replace spkg-install perl script by a bash script, eliminating the dependency on perl



---

archive/issue_comments_042882.json:
```json
{
    "body": "Changing assignee from mabshoff to @tornaria.",
    "created_at": "2009-05-01T21:58:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5517",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5517#issuecomment-42882",
    "user": "@tornaria"
}
```

Changing assignee from mabshoff to @tornaria.



---

archive/issue_comments_042883.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-01T21:58:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5517",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5517#issuecomment-42883",
    "user": "@tornaria"
}
```

Changing status from new to assigned.



---

archive/issue_comments_042884.json:
```json
{
    "body": "With the patch above, compilation of 3.4.1 was successful in a minimal debian lenny chroot created with `debootstrap` (minimal install) + `apt-get install make gcc g++ m4` inside the chroot.",
    "created_at": "2009-05-01T21:58:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5517",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5517#issuecomment-42884",
    "user": "@tornaria"
}
```

With the patch above, compilation of 3.4.1 was successful in a minimal debian lenny chroot created with `debootstrap` (minimal install) + `apt-get install make gcc g++ m4` inside the chroot.



---

archive/issue_comments_042885.json:
```json
{
    "body": "See also #5964; it turns out building R documentation also requires perl-modules. Compilation of Sage proceeds without it, but some doctests (which use R documentation) fail. IOW, it seems perl-modules is a requirement for compilation after all...",
    "created_at": "2009-05-17T02:04:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5517",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5517#issuecomment-42885",
    "user": "@tornaria"
}
```

See also #5964; it turns out building R documentation also requires perl-modules. Compilation of Sage proceeds without it, but some doctests (which use R documentation) fail. IOW, it seems perl-modules is a requirement for compilation after all...



---

archive/issue_comments_042886.json:
```json
{
    "body": "Looks good to me.\n\nThe spkg with this patch applied can be found at: http://sage.math.washington.edu/home/mhansen/cvxopt-0.9.p8.spkg",
    "created_at": "2009-06-20T01:27:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5517",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5517#issuecomment-42886",
    "user": "@mwhansen"
}
```

Looks good to me.

The spkg with this patch applied can be found at: http://sage.math.washington.edu/home/mhansen/cvxopt-0.9.p8.spkg



---

archive/issue_comments_042887.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-02T21:41:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5517",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5517#issuecomment-42887",
    "user": "@rlmill"
}
```

Resolution: fixed
