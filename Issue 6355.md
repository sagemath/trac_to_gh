# Issue 6355: [with SPKG, needs review] Cliquer to compute maximum cliques

archive/issues_006355.json:
```json
{
    "body": "Assignee: rlm\n\nKeywords: Clique max, Cliquer\n\nHello everybody ! I hope this is the last step for this patch to compute the maximum cliques in a graph.\nHere is the SPKG file with the source code of Cliquer.\nAs for planarity or other modules, the original source code of cliquer is copied, but in this case it is copied in local/lib/cliquer-1.2, I was told planarity was to be an exception to the rule.\n\nYou can download the SPKG file at this address :\nhttp://www-sop.inria.fr/members/Nathann.Cohen/cliquer-1.2.spkg\n\nIssue created by migration from https://trac.sagemath.org/ticket/6355\n\n",
    "created_at": "2009-06-18T12:57:35Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "title": "[with SPKG, needs review] Cliquer to compute maximum cliques",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6355",
    "user": "ncohen"
}
```
Assignee: rlm

Keywords: Clique max, Cliquer

Hello everybody ! I hope this is the last step for this patch to compute the maximum cliques in a graph.
Here is the SPKG file with the source code of Cliquer.
As for planarity or other modules, the original source code of cliquer is copied, but in this case it is copied in local/lib/cliquer-1.2, I was told planarity was to be an exception to the rule.

You can download the SPKG file at this address :
http://www-sop.inria.fr/members/Nathann.Cohen/cliquer-1.2.spkg

Issue created by migration from https://trac.sagemath.org/ticket/6355





---

archive/issue_comments_050806.json:
```json
{
    "body": "This ticket, plus #5793 and #5669, are all a total mess, IMHO. There are two separate spkg's linked, here and on #5669, and there are two different sets of patches (`11803.patch` is separately 229.4KB and 6.0KB) at #5793 and #5669.\n\n1. Patch names need to be of the form `trac_####-description.patch`.\n2. I don't even know which spkg to review.\n3. #5793 and #5669 are total duplicates.\n\nMy recommendation is to close the other two tickets as duplicates, indicate which spkg to review here, properly format the correct patches to be applied, and post everything here. There's just too much confusion right now.\n\nNathann -- I would really like to see cliquer included in Sage, so if you need any help getting this in, please don't hesitate to contact me directly.",
    "created_at": "2009-06-19T22:34:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6355#issuecomment-50806",
    "user": "rlm"
}
```

This ticket, plus #5793 and #5669, are all a total mess, IMHO. There are two separate spkg's linked, here and on #5669, and there are two different sets of patches (`11803.patch` is separately 229.4KB and 6.0KB) at #5793 and #5669.

1. Patch names need to be of the form `trac_####-description.patch`.
2. I don't even know which spkg to review.
3. #5793 and #5669 are total duplicates.

My recommendation is to close the other two tickets as duplicates, indicate which spkg to review here, properly format the correct patches to be applied, and post everything here. There's just too much confusion right now.

Nathann -- I would really like to see cliquer included in Sage, so if you need any help getting this in, please don't hesitate to contact me directly.



---

archive/issue_comments_050807.json:
```json
{
    "body": "As far as I could tell at Sage Days 16, the next step required for cliquer is: Someone needs to implement a build system for Cliquer, either using autotools or SCons. Given how simple cliquer is, SCons is probably the way to go, since this would be something like the one liner `Library('cliquer', ['foo.c', 'bar.c'])`.",
    "created_at": "2009-07-01T14:56:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6355#issuecomment-50807",
    "user": "rlm"
}
```

As far as I could tell at Sage Days 16, the next step required for cliquer is: Someone needs to implement a build system for Cliquer, either using autotools or SCons. Given how simple cliquer is, SCons is probably the way to go, since this would be something like the one liner `Library('cliquer', ['foo.c', 'bar.c'])`.



---

archive/issue_comments_050808.json:
```json
{
    "body": "I updated the SPKG file for cliquer.. This new one builds a shared library and I do not call any .c file in the cython code anymore !!\n\nThe address is still the same, though ;-)\n\nNathann",
    "created_at": "2009-07-07T13:16:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6355#issuecomment-50808",
    "user": "ncohen"
}
```

I updated the SPKG file for cliquer.. This new one builds a shared library and I do not call any .c file in the cython code anymore !!

The address is still the same, though ;-)

Nathann



---

archive/issue_comments_050809.json:
```json
{
    "body": "Replying to [comment:3 ncohen]:\n> I updated the SPKG file for cliquer.. This new one builds a shared library and I do not call any .c file in the cython code anymore !!\n\nTrue, this builds a shared library, but it doesn't seem very portable. The problem is that the code you've written probably works only on systems very similar to yours. For example, when I try building on OS X (32- or 64-bit), I get:\n\n```\nld: unknown option: -soname\ncollect2: ld returned 1 exit status\ncp: cannot stat `libcliquer.so': No such file or directory\n\nreal\t0m2.000s\nuser\t0m0.465s\nsys\t0m0.190s\nsage: An error occurred while installing cliquer-1.2\n```\n\n\nYou need to use SCons or some form of autotools as I suggested above, for this to ever be a viable SPKG.",
    "created_at": "2009-07-13T18:56:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6355#issuecomment-50809",
    "user": "rlm"
}
```

Replying to [comment:3 ncohen]:
> I updated the SPKG file for cliquer.. This new one builds a shared library and I do not call any .c file in the cython code anymore !!

True, this builds a shared library, but it doesn't seem very portable. The problem is that the code you've written probably works only on systems very similar to yours. For example, when I try building on OS X (32- or 64-bit), I get:

```
ld: unknown option: -soname
collect2: ld returned 1 exit status
cp: cannot stat `libcliquer.so': No such file or directory

real	0m2.000s
user	0m0.465s
sys	0m0.190s
sage: An error occurred while installing cliquer-1.2
```


You need to use SCons or some form of autotools as I suggested above, for this to ever be a viable SPKG.



---

archive/issue_comments_050810.json:
```json
{
    "body": "I just updated the SPKG, which now uses Scons !\n\nNathann",
    "created_at": "2009-07-16T09:56:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6355#issuecomment-50810",
    "user": "ncohen"
}
```

I just updated the SPKG, which now uses Scons !

Nathann



---

archive/issue_comments_050811.json:
```json
{
    "body": "Nathann,\n\nThis is great work! However, you are still hard-coding some Linux-isms in spkg-install:\n\n\n```\nscons && cp Build/libcliquer.so \"$SAGE_LOCAL/lib/\"\n```\n\n\nUnfortunately, on OS X, it is `libcliquer.dylib` that is built by SCons. Why don't you copy `Build/*` over, to include all cases? You should also delete the commented part from spkg-install. While I'm reviewing, you need a Mercurial repository in the base directory of the spkg, and the License section of SPKG.txt needs to be clarified (i.e. GPLv2+).\n\nKeep up the good work!",
    "created_at": "2009-07-16T18:45:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6355#issuecomment-50811",
    "user": "rlm"
}
```

Nathann,

This is great work! However, you are still hard-coding some Linux-isms in spkg-install:


```
scons && cp Build/libcliquer.so "$SAGE_LOCAL/lib/"
```


Unfortunately, on OS X, it is `libcliquer.dylib` that is built by SCons. Why don't you copy `Build/*` over, to include all cases? You should also delete the commented part from spkg-install. While I'm reviewing, you need a Mercurial repository in the base directory of the spkg, and the License section of SPKG.txt needs to be clarified (i.e. GPLv2+).

Keep up the good work!



---

archive/issue_comments_050812.json:
```json
{
    "body": "All has been done according to your wishes ;-)\n\nThe spkg has been updated !",
    "created_at": "2009-07-17T18:18:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6355#issuecomment-50812",
    "user": "ncohen"
}
```

All has been done according to your wishes ;-)

The spkg has been updated !



---

archive/issue_comments_050813.json:
```json
{
    "body": "1. You need to check in your changes to the repo!\n\n2. You should add a line to `spkg-install` which copies header files to the right place, something like `cp src/*.h \"$SAGE_LOCAL/include/cliquer/\"`\n\n3. This is all I can think of, so after this it's a lot of testing on different platforms.",
    "created_at": "2009-07-17T18:28:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6355#issuecomment-50813",
    "user": "rlm"
}
```

1. You need to check in your changes to the repo!

2. You should add a line to `spkg-install` which copies header files to the right place, something like `cp src/*.h "$SAGE_LOCAL/include/cliquer/"`

3. This is all I can think of, so after this it's a lot of testing on different platforms.



---

archive/issue_comments_050814.json:
```json
{
    "body": "done again ! ;-)",
    "created_at": "2009-07-17T18:34:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6355#issuecomment-50814",
    "user": "ncohen"
}
```

done again ! ;-)



---

archive/issue_comments_050815.json:
```json
{
    "body": "Change `cliquer-1.2` to `cliquer` (twice) in `spkg-install`, so that we don't need to keep upgrading code in the Sage library when Cliquer upgrades.\n\nAfter that, I think that this is ready to go! It builds successfully on 32-bit and 64-bit OS X and on sage.math.",
    "created_at": "2009-07-17T18:42:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6355#issuecomment-50815",
    "user": "rlm"
}
```

Change `cliquer-1.2` to `cliquer` (twice) in `spkg-install`, so that we don't need to keep upgrading code in the Sage library when Cliquer upgrades.

After that, I think that this is ready to go! It builds successfully on 32-bit and 64-bit OS X and on sage.math.



---

archive/issue_comments_050816.json:
```json
{
    "body": "Done. I have to change the patch though, as the directory changed.",
    "created_at": "2009-07-17T18:46:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6355#issuecomment-50816",
    "user": "ncohen"
}
```

Done. I have to change the patch though, as the directory changed.



---

archive/issue_comments_050817.json:
```json
{
    "body": "The spkg looks great! Nice work.\n\nNOTE: This will be little useful without also merging #5793, when it is ready.\n\nNathann, shall we continue at #5793?",
    "created_at": "2009-07-17T18:49:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6355#issuecomment-50817",
    "user": "rlm"
}
```

The spkg looks great! Nice work.

NOTE: This will be little useful without also merging #5793, when it is ready.

Nathann, shall we continue at #5793?



---

archive/issue_comments_050818.json:
```json
{
    "body": "A small problem with the creation of a directory, and changes commited to the hg repository.",
    "created_at": "2009-07-17T18:59:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6355#issuecomment-50818",
    "user": "ncohen"
}
```

A small problem with the creation of a directory, and changes commited to the hg repository.



---

archive/issue_comments_050819.json:
```json
{
    "body": "Ah, you beat me to posting the same fix! :-)",
    "created_at": "2009-07-17T19:01:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6355#issuecomment-50819",
    "user": "rlm"
}
```

Ah, you beat me to posting the same fix! :-)



---

archive/issue_comments_050820.json:
```json
{
    "body": "However, there is now a `cliquer-1.2.spkg` inside the spkg!!!",
    "created_at": "2009-07-17T19:06:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6355#issuecomment-50820",
    "user": "rlm"
}
```

However, there is now a `cliquer-1.2.spkg` inside the spkg!!!



---

archive/issue_comments_050821.json:
```json
{
    "body": "It comes from a tar command run in the wrong directory.... fixed ;-)",
    "created_at": "2009-07-17T19:11:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6355#issuecomment-50821",
    "user": "ncohen"
}
```

It comes from a tar command run in the wrong directory.... fixed ;-)



---

archive/issue_comments_050822.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-23T04:41:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6355#issuecomment-50822",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_050823.json:
```json
{
    "body": "The SPKG at\n\nhttp://www-sop.inria.fr/members/Nathann.Cohen/cliquer-1.2.spkg\n\ndoesn't conform to the naming convention for SPKG's. I've renamed it as `cliquer-1.2.p0.spkg` and uploaded the renamed SPKG up at\n\nhttp://sage.math.washington.edu/home/mvngu/patch/cliquer-1.2.p0.spkg\n\nAs far as I understand, this new SPKG doesn't depend on #5793. So I'm merging the SPKG into the standard SPKG repository.",
    "created_at": "2009-07-23T04:41:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6355#issuecomment-50823",
    "user": "mvngu"
}
```

The SPKG at

http://www-sop.inria.fr/members/Nathann.Cohen/cliquer-1.2.spkg

doesn't conform to the naming convention for SPKG's. I've renamed it as `cliquer-1.2.p0.spkg` and uploaded the renamed SPKG up at

http://sage.math.washington.edu/home/mvngu/patch/cliquer-1.2.p0.spkg

As far as I understand, this new SPKG doesn't depend on #5793. So I'm merging the SPKG into the standard SPKG repository.



---

archive/issue_comments_050824.json:
```json
{
    "body": "See #6626 for a follow-up to this ticket.",
    "created_at": "2009-07-26T08:27:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6355#issuecomment-50824",
    "user": "mvngu"
}
```

See #6626 for a follow-up to this ticket.



---

archive/issue_comments_050825.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-07-26T08:30:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6355#issuecomment-50825",
    "user": "mvngu"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_050826.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-07-26T08:30:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6355#issuecomment-50826",
    "user": "mvngu"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_050827.json:
```json
{
    "body": "I'm reopening this ticket until #6626 is fixed.",
    "created_at": "2009-07-26T08:30:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6355#issuecomment-50827",
    "user": "mvngu"
}
```

I'm reopening this ticket until #6626 is fixed.



---

archive/issue_comments_050828.json:
```json
{
    "body": "Are there any code or doctests to test the functionalities provided by this package? Any package that is merged in the standard package repository must be doctested by code in the Sage library.",
    "created_at": "2009-07-31T10:22:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6355#issuecomment-50828",
    "user": "mvngu"
}
```

Are there any code or doctests to test the functionalities provided by this package? Any package that is merged in the standard package repository must be doctested by code in the Sage library.



---

archive/issue_comments_050829.json:
```json
{
    "body": "The code/doctest related to cliquer is to be found in #5793 : almost all the functions of the Graph class related to cliques use it, and if I make no mistake I documented all of them ;-)",
    "created_at": "2009-07-31T10:25:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6355#issuecomment-50829",
    "user": "ncohen"
}
```

The code/doctest related to cliquer is to be found in #5793 : almost all the functions of the Graph class related to cliques use it, and if I make no mistake I documented all of them ;-)



---

archive/issue_comments_050830.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-31T23:30:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6355#issuecomment-50830",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_050831.json:
```json
{
    "body": "Merged in standard package repository.",
    "created_at": "2009-07-31T23:30:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6355",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6355#issuecomment-50831",
    "user": "mvngu"
}
```

Merged in standard package repository.
