# Issue 469: Integrate the PolyBoRi framework

archive/issues_000469.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @malb\n\nPolyBoRi is a framework for doing computation within the boolean ring, i.e. the ring F_2[x_1,...,x_n]/<x_1<sup>2+x_1,x_n</sup>2+x_n>. From the benchmarks presented in http://www.itwm.fraunhofer.de/zentral/download/berichte/bericht122.pdf it not only features very fast arithmetic in that ring but also a very fast Gr\u00f6bner basis engine. PolyBoRi is GPL'd and should be wrapped for SAGE.\n\nIssue created by migration from https://trac.sagemath.org/ticket/469\n\n",
    "created_at": "2007-08-20T22:01:34Z",
    "labels": [
        "component: packages: standard"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "Integrate the PolyBoRi framework",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/469",
    "user": "https://github.com/malb"
}
```
Assignee: @williamstein

CC:  @malb

PolyBoRi is a framework for doing computation within the boolean ring, i.e. the ring F_2[x_1,...,x_n]/<x_1<sup>2+x_1,x_n</sup>2+x_n>. From the benchmarks presented in http://www.itwm.fraunhofer.de/zentral/download/berichte/bericht122.pdf it not only features very fast arithmetic in that ring but also a very fast Gröbner basis engine. PolyBoRi is GPL'd and should be wrapped for SAGE.

Issue created by migration from https://trac.sagemath.org/ticket/469





---

archive/issue_comments_002322.json:
```json
{
    "body": "Changing assignee from @williamstein to @malb.",
    "created_at": "2007-08-20T22:01:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/469#issuecomment-2322",
    "user": "https://github.com/malb"
}
```

Changing assignee from @williamstein to @malb.



---

archive/issue_comments_002323.json:
```json
{
    "body": "Changing assignee from @malb to @burcin.",
    "created_at": "2007-10-21T22:53:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/469#issuecomment-2323",
    "user": "https://github.com/malb"
}
```

Changing assignee from @malb to @burcin.



---

archive/issue_comments_002324.json:
```json
{
    "body": "Alexander Dreyer did comment on the build time of PolyBoRi:\n\n```\nThe essential part of PolyBoRi (using the built-ininterface) can be\nbuilt in about 3 minutes on a Intel(R) Xeon(R) CPU5148  @ 2.33GHz\n(using one cpu only). I'll try to find the corresponding scons\ncommands for the spkg and the Sage-wrapper and give to to Burcin.\n\nBest regards,\n  Alexander\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2007-12-04T14:21:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/469#issuecomment-2324",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Alexander Dreyer did comment on the build time of PolyBoRi:

```
The essential part of PolyBoRi (using the built-ininterface) can be
built in about 3 minutes on a Intel(R) Xeon(R) CPU5148  @ 2.33GHz
(using one cpu only). I'll try to find the corresponding scons
commands for the spkg and the Sage-wrapper and give to to Burcin.

Best regards,
  Alexander
```


Cheers,

Michael



---

archive/issue_comments_002325.json:
```json
{
    "body": "\n```\nThere is a new PolyBoRi package available at:\n\nhttp://www.risc.uni-linz.ac.at/people/berocal/sage/polybori-0.1-r3.spkg\n\nChanges are:\n        - Alexander's changes to speed up the build process\n        - Update to the latest CVS version\n        - pass on MAKEOPTS to scons to allow parallel builds\n\nBuilding the package takes 4 mins 20 seconds on a single Intel(R)\nPentium (R) D CPU 3.40GHz. Parallel make options (-jn) speed up the\nbuild as expected.\n\nBurcin \n```\n",
    "created_at": "2007-12-04T14:54:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/469#issuecomment-2325",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```


```
There is a new PolyBoRi package available at:

http://www.risc.uni-linz.ac.at/people/berocal/sage/polybori-0.1-r3.spkg

Changes are:
        - Alexander's changes to speed up the build process
        - Update to the latest CVS version
        - pass on MAKEOPTS to scons to allow parallel builds

Building the package takes 4 mins 20 seconds on a single Intel(R)
Pentium (R) D CPU 3.40GHz. Parallel make options (-jn) speed up the
build as expected.

Burcin 
```




---

archive/issue_comments_002326.json:
```json
{
    "body": "Okay, I have stuck \n\nhttp://www.risc.uni-linz.ac.at/people/berocal/sage/polybori-0.1-r3.spkg\n\ninto 2.9.alpha2. Burcin, please send me a patch/bundle against some 2.9 release for the code that does the actual integrations with Sage.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-09T14:18:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/469#issuecomment-2326",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Okay, I have stuck 

http://www.risc.uni-linz.ac.at/people/berocal/sage/polybori-0.1-r3.spkg

into 2.9.alpha2. Burcin, please send me a patch/bundle against some 2.9 release for the code that does the actual integrations with Sage.

Cheers,

Michael



---

archive/issue_comments_002327.json:
```json
{
    "body": "New bundle against 2.9.alpha4:\n\nhttp://www.risc.uni-linz.ac.at/people/berocal/sage/polybori_wrapper-2.9.alpha4-20071204.hg\n\nNew package:\n\nhttp://www.risc.uni-linz.ac.at/people/berocal/sage/polybori-0.1-r5.spkg\n\nChanges to the package:\n\nr4 -> r5\n\n* Make symlinks relative\n\nr3 -> r4\n\n* Remove popd, pushd from spkg-install",
    "created_at": "2007-12-10T17:31:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/469#issuecomment-2327",
    "user": "https://github.com/burcin"
}
```

New bundle against 2.9.alpha4:

http://www.risc.uni-linz.ac.at/people/berocal/sage/polybori_wrapper-2.9.alpha4-20071204.hg

New package:

http://www.risc.uni-linz.ac.at/people/berocal/sage/polybori-0.1-r5.spkg

Changes to the package:

r4 -> r5

* Make symlinks relative

r3 -> r4

* Remove popd, pushd from spkg-install



---

archive/issue_comments_002328.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-10T17:31:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/469#issuecomment-2328",
    "user": "https://github.com/burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002329.json:
```json
{
    "body": "Ok, I updated the spkg as well applied the bundle. I also disabled doctests until you can send in the missing bits.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-10T22:34:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/469#issuecomment-2329",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, I updated the spkg as well applied the bundle. I also disabled doctests until you can send in the missing bits.

Cheers,

Michael



---

archive/issue_comments_002330.json:
```json
{
    "body": "fix doctests in pbori.pyx",
    "created_at": "2007-12-12T13:01:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/469#issuecomment-2330",
    "user": "https://github.com/burcin"
}
```

fix doctests in pbori.pyx



---

archive/issue_comments_002331.json:
```json
{
    "body": "Attachment [fix_pbori_doctests.hg](tarball://root/attachments/some-uuid/ticket469/fix_pbori_doctests.hg) by mabshoff created at 2007-12-12 18:37:38\n\nMerged in 2.9.alpha6. - Finally. Doctests pass.",
    "created_at": "2007-12-12T18:37:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/469#issuecomment-2331",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [fix_pbori_doctests.hg](tarball://root/attachments/some-uuid/ticket469/fix_pbori_doctests.hg) by mabshoff created at 2007-12-12 18:37:38

Merged in 2.9.alpha6. - Finally. Doctests pass.



---

archive/issue_comments_002332.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-12T18:37:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/469#issuecomment-2332",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
