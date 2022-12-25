# Issue 4794: Update pari to 2.3.4svb

archive/issues_004794.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @ncalexan boothby @craigcitro\n\nThe following spkgs depend on pari and need to be bumped:\n\n```\n * genus2reduction\n * lcalc \n * eclib\n```\n\nThe Sage library also depends on pari, but is linked dynamically. Note that once this ticket is solved we should also fix #1891. For update to lcalc see #4793, for eclib see #3358.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4794\n\n",
    "created_at": "2008-12-14T07:45:53Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Update pari to 2.3.4svb",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4794",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

CC:  @ncalexan boothby @craigcitro

The following spkgs depend on pari and need to be bumped:

```
 * genus2reduction
 * lcalc 
 * eclib
```

The Sage library also depends on pari, but is linked dynamically. Note that once this ticket is solved we should also fix #1891. For update to lcalc see #4793, for eclib see #3358.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4794





---

archive/issue_comments_036273.json:
```json
{
    "body": "Ok, due to various people like Nick and Tom running into numerous problems with the current pari we will update this in Sage 3.4. This will require changes on top of the ReST patches. \n\nI should post an spkg in the next 24 hours.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-09T05:50:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4794#issuecomment-36273",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, due to various people like Nick and Tom running into numerous problems with the current pari we will update this in Sage 3.4. This will require changes on top of the ReST patches. 

I should post an spkg in the next 24 hours.

Cheers,

Michael



---

archive/issue_comments_036274.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-09T05:50:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4794#issuecomment-36274",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_036275.json:
```json
{
    "body": "The spkg at\n\n  http://sage.math.washington.edu/home/mabshoff/spkgs/pari-2.4.3-svn11590.spkg\n\ncontains today's development snapshot. Unfortunately gen.pyx does not build at the moment:\n\n```\ngcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -I/scratch/mabshoff/gp/sage-3.3.alpha6-pari2.4.3-special/local//include -I/scratch/mabshoff/gp/sage-3.3.alpha6-pari2.4.3-special/local//include/csage -I/scratch/mabshoff/gp/sage-3.3.alpha6-pari2.4.3-special/devel//sage/sage/ext -I/scratch/mabshoff/gp/sage-3.3.alpha6-pari2.4.3-special/local/include/python2.5 -c sage/libs/pari/gen.c -o build/temp.linux-x86_64-2.5/sage/libs/pari/gen.o -w\nsage/libs/pari/gen.c: In function \u2018__pyx_pf_4sage_4libs_4pari_3gen_3gen___hex__\u2019:\nsage/libs/pari/gen.c:7100: error: \u2018BYTES_IN_LONG\u2019 undeclared (first use in this function)\nsage/libs/pari/gen.c:7100: error: (Each undeclared identifier is reported only once\nsage/libs/pari/gen.c:7100: error: for each function it appears in.)\nsage/libs/pari/gen.c: In function \u2018__pyx_pf_4sage_4libs_4pari_3gen_3gen_idealred\u2019:\nsage/libs/pari/gen.c:21573: error: too many arguments to function \u2018idealred0\u2019\nsage/libs/pari/gen.c: In function \u2018__pyx_pf_4sage_4libs_4pari_3gen_3gen_idealmul\u2019:\nsage/libs/pari/gen.c:22203: error: too many arguments to function \u2018idealmulred\u2019\nsage/libs/pari/gen.c:23069:361: error: macro \"nfdiscf0\" passed 3 arguments, but takes just 1\nsage/libs/pari/gen.c: In function \u2018__pyx_pf_4sage_4libs_4pari_3gen_3gen_nfdisc\u2019:\nsage/libs/pari/gen.c:23069: error: \u2018nfdiscf0\u2019 undeclared (first use in this function)\nsage/libs/pari/gen.c: In function \u2018__pyx_pf_4sage_4libs_4pari_3gen_3gen_qflll\u2019:\nsage/libs/pari/gen.c:27453: error: too many arguments to function \u2018qflll0\u2019\nsage/libs/pari/gen.c: In function \u2018__pyx_pf_4sage_4libs_4pari_3gen_3gen_qflllgram\u2019:\nsage/libs/pari/gen.c:27554: error: too many arguments to function \u2018qflllgram0\u2019\nsage/libs/pari/gen.c: In function \u2018__pyx_pf_4sage_4libs_4pari_3gen_3gen_algdep\u2019:\nsage/libs/pari/gen.c:30284: error: too many arguments to function \u2018algdep0\u2019\nsage/libs/pari/gen.c: In function \u2018__pyx_pf_4sage_4libs_4pari_3gen_3gen_lindep\u2019:\nsage/libs/pari/gen.c:30417: error: too many arguments to function \u2018lindep0\u2019\nsage/libs/pari/gen.c: In function \u2018__pyx_pf_4sage_4libs_4pari_3gen_12PariInstance_listcreate\u2019:\nsage/libs/pari/gen.c:35975: error: too many arguments to function \u2018listcreate\u2019\nsage/libs/pari/gen.c: In function \u2018__pyx_f_4sage_4libs_4pari_3gen_fix_size\u2019:\nsage/libs/pari/gen.c:37409: error: \u2018BYTES_IN_LONG\u2019 undeclared (first use in this function)\nerror: command 'gcc' failed with exit status 1\nsage: There was an error installing modified sage library code.\n```\n\nIronically the doctests for gen.pyx pass:\n\n```\nmabshoff@sage:/scratch/mabshoff/gp/sage-3.3.alpha6-pari2.4.3-special$ ./sage -t devel/sage/sage/libs/pari/gen.pyx \nsage -t  \"devel/sage/sage/libs/pari/gen.pyx\"                \n\t [2.4 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 2.4 seconds\n```\n\nAnd we are linking against the correct development snapshot:\n\n```\nsage-3.3.alpha6-pari2.4.3-special$ ldd devel/sage/build/sage/libs/pari/gen.so\n\tlinux-vdso.so.1 =>  (0x00007fff01ffe000)\n\tlibcsage.so => /scratch/mabshoff/gp/sage-3.3.alpha6-pari2.4.3-special/local/lib/libcsage.so (0x00007f4af99f2000)\n\tlibpari-gmp.so.2 => /scratch/mabshoff/gp/sage-3.3.alpha6-pari2.4.3-special/local/lib/libpari-gmp.so.2 (0x00007f4af94ad000)\n\tlibgmp.so.3 => /scratch/mabshoff/gp/sage-3.3.alpha6-pari2.4.3-special/local/lib/libgmp.so.3 (0x00007f4af925c000)\n\tlibstdc++.so.6 => /usr/lib/libstdc++.so.6 (0x00007f4af8f40000)\n\tlibntl-5.4.2.so => /scratch/mabshoff/gp/sage-3.3.alpha6-pari2.4.3-special/local/lib/libntl-5.4.2.so (0x00007f4af8b61000)\n\tlibpthread.so.0 => /lib/libpthread.so.0 (0x00007f4af8945000)\n\tlibc.so.6 => /lib/libc.so.6 (0x00007f4af85e3000)\n\tlibpari-gmp-2.4.so.3 => /scratch/mabshoff/gp/sage-3.3.alpha6-pari2.4.3-special/local/lib/libpari-gmp-2.4.so.3 (0x00007f4af7f62000)\n\tlibm.so.6 => /lib/libm.so.6 (0x00007f4af7ce1000)\n\tlibgcc_s.so.1 => /lib/libgcc_s.so.1 (0x00007f4af7ad3000)\n\tlibdl.so.2 => /lib/libdl.so.2 (0x00007f4af78ce000)\n\t/lib64/ld-linux-x86-64.so.2 (0x00007f4af9ece000)\n```\n",
    "created_at": "2009-02-11T06:17:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4794#issuecomment-36275",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The spkg at

  http://sage.math.washington.edu/home/mabshoff/spkgs/pari-2.4.3-svn11590.spkg

contains today's development snapshot. Unfortunately gen.pyx does not build at the moment:

```
gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -I/scratch/mabshoff/gp/sage-3.3.alpha6-pari2.4.3-special/local//include -I/scratch/mabshoff/gp/sage-3.3.alpha6-pari2.4.3-special/local//include/csage -I/scratch/mabshoff/gp/sage-3.3.alpha6-pari2.4.3-special/devel//sage/sage/ext -I/scratch/mabshoff/gp/sage-3.3.alpha6-pari2.4.3-special/local/include/python2.5 -c sage/libs/pari/gen.c -o build/temp.linux-x86_64-2.5/sage/libs/pari/gen.o -w
sage/libs/pari/gen.c: In function ‘__pyx_pf_4sage_4libs_4pari_3gen_3gen___hex__’:
sage/libs/pari/gen.c:7100: error: ‘BYTES_IN_LONG’ undeclared (first use in this function)
sage/libs/pari/gen.c:7100: error: (Each undeclared identifier is reported only once
sage/libs/pari/gen.c:7100: error: for each function it appears in.)
sage/libs/pari/gen.c: In function ‘__pyx_pf_4sage_4libs_4pari_3gen_3gen_idealred’:
sage/libs/pari/gen.c:21573: error: too many arguments to function ‘idealred0’
sage/libs/pari/gen.c: In function ‘__pyx_pf_4sage_4libs_4pari_3gen_3gen_idealmul’:
sage/libs/pari/gen.c:22203: error: too many arguments to function ‘idealmulred’
sage/libs/pari/gen.c:23069:361: error: macro "nfdiscf0" passed 3 arguments, but takes just 1
sage/libs/pari/gen.c: In function ‘__pyx_pf_4sage_4libs_4pari_3gen_3gen_nfdisc’:
sage/libs/pari/gen.c:23069: error: ‘nfdiscf0’ undeclared (first use in this function)
sage/libs/pari/gen.c: In function ‘__pyx_pf_4sage_4libs_4pari_3gen_3gen_qflll’:
sage/libs/pari/gen.c:27453: error: too many arguments to function ‘qflll0’
sage/libs/pari/gen.c: In function ‘__pyx_pf_4sage_4libs_4pari_3gen_3gen_qflllgram’:
sage/libs/pari/gen.c:27554: error: too many arguments to function ‘qflllgram0’
sage/libs/pari/gen.c: In function ‘__pyx_pf_4sage_4libs_4pari_3gen_3gen_algdep’:
sage/libs/pari/gen.c:30284: error: too many arguments to function ‘algdep0’
sage/libs/pari/gen.c: In function ‘__pyx_pf_4sage_4libs_4pari_3gen_3gen_lindep’:
sage/libs/pari/gen.c:30417: error: too many arguments to function ‘lindep0’
sage/libs/pari/gen.c: In function ‘__pyx_pf_4sage_4libs_4pari_3gen_12PariInstance_listcreate’:
sage/libs/pari/gen.c:35975: error: too many arguments to function ‘listcreate’
sage/libs/pari/gen.c: In function ‘__pyx_f_4sage_4libs_4pari_3gen_fix_size’:
sage/libs/pari/gen.c:37409: error: ‘BYTES_IN_LONG’ undeclared (first use in this function)
error: command 'gcc' failed with exit status 1
sage: There was an error installing modified sage library code.
```

Ironically the doctests for gen.pyx pass:

```
mabshoff@sage:/scratch/mabshoff/gp/sage-3.3.alpha6-pari2.4.3-special$ ./sage -t devel/sage/sage/libs/pari/gen.pyx 
sage -t  "devel/sage/sage/libs/pari/gen.pyx"                
	 [2.4 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 2.4 seconds
```

And we are linking against the correct development snapshot:

```
sage-3.3.alpha6-pari2.4.3-special$ ldd devel/sage/build/sage/libs/pari/gen.so
	linux-vdso.so.1 =>  (0x00007fff01ffe000)
	libcsage.so => /scratch/mabshoff/gp/sage-3.3.alpha6-pari2.4.3-special/local/lib/libcsage.so (0x00007f4af99f2000)
	libpari-gmp.so.2 => /scratch/mabshoff/gp/sage-3.3.alpha6-pari2.4.3-special/local/lib/libpari-gmp.so.2 (0x00007f4af94ad000)
	libgmp.so.3 => /scratch/mabshoff/gp/sage-3.3.alpha6-pari2.4.3-special/local/lib/libgmp.so.3 (0x00007f4af925c000)
	libstdc++.so.6 => /usr/lib/libstdc++.so.6 (0x00007f4af8f40000)
	libntl-5.4.2.so => /scratch/mabshoff/gp/sage-3.3.alpha6-pari2.4.3-special/local/lib/libntl-5.4.2.so (0x00007f4af8b61000)
	libpthread.so.0 => /lib/libpthread.so.0 (0x00007f4af8945000)
	libc.so.6 => /lib/libc.so.6 (0x00007f4af85e3000)
	libpari-gmp-2.4.so.3 => /scratch/mabshoff/gp/sage-3.3.alpha6-pari2.4.3-special/local/lib/libpari-gmp-2.4.so.3 (0x00007f4af7f62000)
	libm.so.6 => /lib/libm.so.6 (0x00007f4af7ce1000)
	libgcc_s.so.1 => /lib/libgcc_s.so.1 (0x00007f4af7ad3000)
	libdl.so.2 => /lib/libdl.so.2 (0x00007f4af78ce000)
	/lib64/ld-linux-x86-64.so.2 (0x00007f4af9ece000)
```




---

archive/issue_comments_036276.json:
```json
{
    "body": "Remember to turn on relative number field in the ring tester once this spkg has made it - see #4779.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T08:29:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4794#issuecomment-36276",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Remember to turn on relative number field in the ring tester once this spkg has made it - see #4779.

Cheers,

Michael



---

archive/issue_comments_036277.json:
```json
{
    "body": "What's the latest on this?  We have code which uses the pari library and will not work until a pari bug fix (in their current svn)  is in Sage too.\n\nIsn't Alex Ghitza working on this?  He is not on the CC list for this ticket though.",
    "created_at": "2009-03-19T12:45:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4794#issuecomment-36277",
    "user": "https://github.com/JohnCremona"
}
```

What's the latest on this?  We have code which uses the pari library and will not work until a pari bug fix (in their current svn)  is in Sage too.

Isn't Alex Ghitza working on this?  He is not on the CC list for this ticket though.



---

archive/issue_comments_036278.json:
```json
{
    "body": "See #9343 instead.",
    "created_at": "2010-08-01T16:01:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4794#issuecomment-36278",
    "user": "https://github.com/jdemeyer"
}
```

See #9343 instead.



---

archive/issue_comments_036279.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-09-08T18:11:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4794#issuecomment-36279",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_036280.json:
```json
{
    "body": "Please close this ticket",
    "created_at": "2010-09-08T18:11:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4794#issuecomment-36280",
    "user": "https://github.com/jdemeyer"
}
```

Please close this ticket



---

archive/issue_events_005037.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-10T10:50:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4794",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4794#event-5037"
}
```



---

archive/issue_comments_036281.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-09-10T10:50:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4794",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4794#issuecomment-36281",
    "user": "https://github.com/qed777"
}
```

Resolution: duplicate
