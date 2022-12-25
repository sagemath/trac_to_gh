# Issue 3528: test_gcc_version.pl claims that gcc 4.3 is not a valid compiler to build FLINT

archive/issues_003528.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nhexagon1001: [gcc -v result.]\n[02:14am] hexagon1001: Using built-in specs.\n[02:14am] hexagon1001: Target: i586-suse-linux\n[02:14am] hexagon1001: Configured with: ../configure --prefix=/usr \n--with-local-prefix=/usr/local --infodir=/usr/share/info \n--mandir=/usr/share/man --libdir=/usr/lib --libexecdir=/usr/lib \n--enable-languages=c,c++,objc,fortran,obj-c++,java,ada \n--enable-checking=release --with-gxx-include-dir=/usr/include/c++/4.3 \n\\--enable-ssp --disable-libssp --with-bugurl=http://bugs.opensuse.org/ \n--with-pkgversion='SUSE Linux' --disable-libgcj --with-slibdir=/lib \n--with-system-zlib --ena\n[02:14am] hexagon1001: Thread model: posix\n[02:14am] hexagon1001: gcc version 4.3.1 20080507 (prerelease) [gcc-4_3-branch revision 135036] (SUSE Linux)\n[02:15am] mabshoff: ok, but gcc -dumpversion  says \"4.3\" ?\n```\n\n\nThis is OpenSuSE 11, so those SuSE people need to get a life since they have been shipping odd compilers for way too many years. The fix in test_gcc_version.pl is to check also for only major and minor version.\n\nThe check should also happen before we start building Sage and should black list a bunch of known broken compilers.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3528\n\n",
    "created_at": "2008-06-28T09:36:05Z",
    "labels": [
        "component: build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "test_gcc_version.pl claims that gcc 4.3 is not a valid compiler to build FLINT",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3528",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff


```
hexagon1001: [gcc -v result.]
[02:14am] hexagon1001: Using built-in specs.
[02:14am] hexagon1001: Target: i586-suse-linux
[02:14am] hexagon1001: Configured with: ../configure --prefix=/usr 
--with-local-prefix=/usr/local --infodir=/usr/share/info 
--mandir=/usr/share/man --libdir=/usr/lib --libexecdir=/usr/lib 
--enable-languages=c,c++,objc,fortran,obj-c++,java,ada 
--enable-checking=release --with-gxx-include-dir=/usr/include/c++/4.3 
\--enable-ssp --disable-libssp --with-bugurl=http://bugs.opensuse.org/ 
--with-pkgversion='SUSE Linux' --disable-libgcj --with-slibdir=/lib 
--with-system-zlib --ena
[02:14am] hexagon1001: Thread model: posix
[02:14am] hexagon1001: gcc version 4.3.1 20080507 (prerelease) [gcc-4_3-branch revision 135036] (SUSE Linux)
[02:15am] mabshoff: ok, but gcc -dumpversion  says "4.3" ?
```


This is OpenSuSE 11, so those SuSE people need to get a life since they have been shipping odd compilers for way too many years. The fix in test_gcc_version.pl is to check also for only major and minor version.

The check should also happen before we start building Sage and should black list a bunch of known broken compilers.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3528





---

archive/issue_comments_024837.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-06-28T09:36:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3528#issuecomment-24837",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_024838.json:
```json
{
    "body": "The spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.4/alpha2/flint-1.010.p0.spkg\n\nonly tests major and minor version of gcc and not tiny. It is also somewhat more verbose than the old script. \n\nCheers,\n\nMichael",
    "created_at": "2008-07-07T05:43:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3528#issuecomment-24838",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.4/alpha2/flint-1.010.p0.spkg

only tests major and minor version of gcc and not tiny. It is also somewhat more verbose than the old script. 

Cheers,

Michael



---

archive/issue_comments_024839.json:
```json
{
    "body": "Look relatively harmless.",
    "created_at": "2008-07-07T05:55:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3528#issuecomment-24839",
    "user": "https://github.com/williamstein"
}
```

Look relatively harmless.



---

archive/issue_comments_024840.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-07T05:56:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3528#issuecomment-24840",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_024841.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha2",
    "created_at": "2008-07-07T05:56:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3528",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3528#issuecomment-24841",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.4.alpha2



---

archive/issue_events_003747.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-07-07T05:56:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3528",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3528#event-3747"
}
```
