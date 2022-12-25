# Issue 7118: [close as fixed] remove quaddouble from sage

archive/issues_007118.json:
```json
{
    "body": "Assignee: tbd\n\nSince quaddouble was deprecated a year ago, and voted out, we should finally actually remove it.  This is motivated also by us getting numerous build failure reports that involve quaddouble lately.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7118\n\n",
    "closed_at": "2009-10-31T16:39:12Z",
    "created_at": "2009-10-04T22:56:48Z",
    "labels": [
        "component: build",
        "blocker"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[close as fixed] remove quaddouble from sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7118",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

Since quaddouble was deprecated a year ago, and voted out, we should finally actually remove it.  This is motivated also by us getting numerous build failure reports that involve quaddouble lately.

Issue created by migration from https://trac.sagemath.org/ticket/7118





---

archive/issue_comments_058876.json:
```json
{
    "body": "Attachment [trac_7118.patch](tarball://root/attachments/some-uuid/ticket7118/trac_7118.patch) by @williamstein created at 2009-10-04 23:12:23",
    "created_at": "2009-10-04T23:12:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7118#issuecomment-58876",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_7118.patch](tarball://root/attachments/some-uuid/ticket7118/trac_7118.patch) by @williamstein created at 2009-10-04 23:12:23



---

archive/issue_comments_058877.json:
```json
{
    "body": "Attachment [trac_7118-part2.patch](tarball://root/attachments/some-uuid/ticket7118/trac_7118-part2.patch) by @williamstein created at 2009-10-05 02:54:18",
    "created_at": "2009-10-05T02:54:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7118#issuecomment-58877",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_7118-part2.patch](tarball://root/attachments/some-uuid/ticket7118/trac_7118-part2.patch) by @williamstein created at 2009-10-05 02:54:18



---

archive/issue_comments_058878.json:
```json
{
    "body": "I also removed the rqdf objects from the pickle jar test, since they obviously no longer unpickle.  People using RQDF have been warned not to for a year now.",
    "created_at": "2009-10-05T02:54:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7118#issuecomment-58878",
    "user": "https://github.com/williamstein"
}
```

I also removed the rqdf objects from the pickle jar test, since they obviously no longer unpickle.  People using RQDF have been warned not to for a year now.



---

archive/issue_comments_058879.json:
```json
{
    "body": "I did a clean build test of sage with these patches, plus the appropriate changes to spkg/standard/deps and spkg/install (which can't be expressed as patches right now), and it all works perfectly.",
    "created_at": "2009-10-05T02:55:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7118#issuecomment-58879",
    "user": "https://github.com/williamstein"
}
```

I did a clean build test of sage with these patches, plus the appropriate changes to spkg/standard/deps and spkg/install (which can't be expressed as patches right now), and it all works perfectly.



---

archive/issue_comments_058880.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2009-10-05T02:56:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7118#issuecomment-58880",
    "user": "https://github.com/williamstein"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_058881.json:
```json
{
    "body": "Applied patches in this order to Sage 4.1.2.rc0:\n\n1. `trac_7118.patch`\n2. `trac_7118-part2.patch`\n \nDoctesting resulted in the following failure:\n\n```\nsage -t -long \"devel/sage-main/sage/structure/sage_object.pyx\"\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.2.rc0/devel/sage-main/sage/structure/sage_object.pyx\", line 931:\n    sage: sage.structure.sage_object.unpickle_all(std)\nExpected:\n    doctest...\n    Successfully unpickled 571 objects.\n    Failed to unpickle 0 objects.\nGot:\n    doctest:1: DeprecationWarning: Your word object is saved in an old file format since FiniteWord_over_OrderedAlphabet is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing \"word.save(filename)\" to ensure that it will load in future versions of Sage.\n    doctest:1: DeprecationWarning: Your word object is saved in an old file format since AbstractWord is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing \"word.save(filename)\" to ensure that it will load in future versions of Sage.\n    doctest:1: DeprecationWarning: Your word object is saved in an old file format since Word_over_Alphabet is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing \"word.save(filename)\" to ensure that it will load in future versions of Sage.\n    doctest:1: DeprecationWarning: Your word object is saved in an old file format since Word_over_OrderedAlphabet is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing \"word.save(filename)\" to ensure that it will load in future versions of Sage.\n    doctest:1: DeprecationWarning: ChristoffelWord_Lower is deprecated, use LowerChristoffelWord instead\n    doctest:1172: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.\n    Successfully unpickled 572 objects.\n    Failed to unpickle 0 objects.\n**********************************************************************\n1 items had failures:\n   1 of   7 in __main__.example_21\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/mvngu/.sage//tmp/.doctest_sage_object.py\n\t [6.0 s]\n```",
    "created_at": "2009-10-10T21:05:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7118#issuecomment-58881",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Applied patches in this order to Sage 4.1.2.rc0:

1. `trac_7118.patch`
2. `trac_7118-part2.patch`
 
Doctesting resulted in the following failure:

```
sage -t -long "devel/sage-main/sage/structure/sage_object.pyx"
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.rc0/devel/sage-main/sage/structure/sage_object.pyx", line 931:
    sage: sage.structure.sage_object.unpickle_all(std)
Expected:
    doctest...
    Successfully unpickled 571 objects.
    Failed to unpickle 0 objects.
Got:
    doctest:1: DeprecationWarning: Your word object is saved in an old file format since FiniteWord_over_OrderedAlphabet is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing "word.save(filename)" to ensure that it will load in future versions of Sage.
    doctest:1: DeprecationWarning: Your word object is saved in an old file format since AbstractWord is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing "word.save(filename)" to ensure that it will load in future versions of Sage.
    doctest:1: DeprecationWarning: Your word object is saved in an old file format since Word_over_Alphabet is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing "word.save(filename)" to ensure that it will load in future versions of Sage.
    doctest:1: DeprecationWarning: Your word object is saved in an old file format since Word_over_OrderedAlphabet is deprecated and will be deleted in a future version of Sage (you can use FiniteWord_list instead). You can re-save your word by typing "word.save(filename)" to ensure that it will load in future versions of Sage.
    doctest:1: DeprecationWarning: ChristoffelWord_Lower is deprecated, use LowerChristoffelWord instead
    doctest:1172: DeprecationWarning: RQDF is deprecated; use RealField(212) instead.
    Successfully unpickled 572 objects.
    Failed to unpickle 0 objects.
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_21
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/mvngu/.sage//tmp/.doctest_sage_object.py
	 [6.0 s]
```



---

archive/issue_comments_058882.json:
```json
{
    "body": "```\noh, your own failure is in the pickle jar.\n[2:06pm] williamstein:\nThat requires manually removing a pickle from the pickle jar.\n[2:07pm] williamstein:\nThere is a quaddouble pickle in there.\n[2:07pm] williamstein:\nNotice that the doctest failure is in the message about how many pickles there are.\n[2:07pm] williamstein:\nso that's fine.\n[2:07pm] williamstein:\nIn my tree i've removed that.\n[2:07pm] williamstein:\nthat = 1 pickle\n```",
    "created_at": "2009-10-10T21:07:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7118#issuecomment-58882",
    "user": "https://github.com/williamstein"
}
```

```
oh, your own failure is in the pickle jar.
[2:06pm] williamstein:
That requires manually removing a pickle from the pickle jar.
[2:07pm] williamstein:
There is a quaddouble pickle in there.
[2:07pm] williamstein:
Notice that the doctest failure is in the message about how many pickles there are.
[2:07pm] williamstein:
so that's fine.
[2:07pm] williamstein:
In my tree i've removed that.
[2:07pm] williamstein:
that = 1 pickle
```



---

archive/issue_comments_058883.json:
```json
{
    "body": "```\n14:08 < mvngu> williamstein: Which file(s) exactly must be removed?\n14:08 < mvngu> williamstein: Can you give me the path to those files to remove?\n14:09 < williamstein> you have to remove a file from the tarball in\n                      data/extcode/pickle_jar\n14:09 < williamstein> it's the one with \"rqdf\" in its name, I think.\n14:09 < williamstein> then you remake the tarball.\n14:10 < mvngu> williamstein: OK. Thank you.\n```",
    "created_at": "2009-10-10T21:14:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7118#issuecomment-58883",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

```
14:08 < mvngu> williamstein: Which file(s) exactly must be removed?
14:08 < mvngu> williamstein: Can you give me the path to those files to remove?
14:09 < williamstein> you have to remove a file from the tarball in
                      data/extcode/pickle_jar
14:09 < williamstein> it's the one with "rqdf" in its name, I think.
14:09 < williamstein> then you remake the tarball.
14:10 < mvngu> williamstein: OK. Thank you.
```



---

archive/issue_comments_058884.json:
```json
{
    "body": "install log on sage.math",
    "created_at": "2009-10-11T02:05:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7118#issuecomment-58884",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

install log on sage.math



---

archive/issue_comments_058885.json:
```json
{
    "body": "Attachment [install-7118-quaddouble.log.bz2](tarball://root/attachments/some-uuid/ticket7118/install-7118-quaddouble.log.bz2) by mvngu created at 2009-10-11 02:05:30\n\nApplied patches in this order to Sage 4.1.2.rc0:\n\n1. `trac_7118.patch`\n2. `trac_7118-part2.patch`\n \nThen uncompressed the file `SAGE_ROOT/data/extcode/pickle_jar/pickle_jar.tar.bz2` and removed the following files from the directory `SAGE_ROOT/data/extcode/pickle_jar/pickle_jar`:\n\n1. `_type__sage_rings_real_rqdf_QuadDoubleElement__.sobj`\n2. `_type__sage_rings_real_rqdf_QuadDoubleElement__.txt`\n \nWith these files removed, the directory `SAGE_ROOT/data/extcode/pickle_jar/pickle_jar` is compressed into a tarball again and replaced the previous version of the same tarball. From Mercurial's point of view, this would result in a change to a file it tracks, i.e. the pickle_jar.tar.bz2 has changed and all changes should be checked in. Now edit the file `SAGE_ROOT/spkg/install` to comment out the line related to quaddouble. The commented lines should be:\n\n```\n# See ticket #7118: remove quaddouble from sage                                 \n# QUADDOUBLE=`$newest quaddouble`                                               \n# export QUADDOUBLE\n```\nThe file `SAGE_ROOT/spkg/install` is not tracked by Mercurial, so no need to check in changes. Also, edit the file `SAGE_ROOT/spkg/standard/deps` to comment out all lines related to quaddouble. The commented lines should be:\n\n```\n# See ticket #7118: remove quaddouble from sage\n# $(INST)/$(QUADDOUBLE): $(BASE) $(INST)/$(MPIR) $(INST)/$(MPFR)\n#       $(SAGE_SPKG) $(QUADDOUBLE) 2>&1\n\n<SNIP>\n\n                  # See ticket #7118: remove quaddouble from sage\n                  # $(INST)/$(QUADDOUBLE) \\\n```\nThis file is also not tracked by Mercurial, so no need to check in changes. Finally, remove the package quaddouble-2.2.p9.spkg from the directory `SAGE_ROOT/spkg/standard` of standard Sage packages. With these changes, I made a new source tarball called \"sage-4.1.2.rc1-7118-quaddouble\". After unpacking that tarball and compiling from scratch, I got the following error. The full install log is attached.\n\n```\ng++ -o libcsage.so -shared src/convert.os src/interrupt.os src/mpn_pylong.os src/mpz_pylong.os src/mpz_longlong.os src/stdsage.os src/gmp_globals.os src/ZZ_pylong.os src/ntl_wrap.os -L/scratch/mvngu/release/sandbox/sage-4.1.2.rc1-7118-quaddouble/local/lib -lntl -lgmp -lpari\n*** TOUCHING ALL CYTHON (.pyx) FILES ***\nscons: `install' is up to date.\n\n----------------------------------------------------------\nsage: Building and installing modified Sage library files.\n\n\nInstalling c_lib\nscons: `install' is up to date.\nTraceback (most recent call last):\n  File \"setup.py\", line 16, in <module>\n    from module_list import ext_modules\n  File \"/scratch/mvngu/release/sandbox/sage-4.1.2.rc1-7118-quaddouble/devel/sage-main/module_list.py\", line 84, in <module>\n    for line in open(SAGE_LOCAL + \"/share/polybori/flags.conf\"):\nIOError: [Errno 2] No such file or directory: '/scratch/mvngu/release/sandbox/sage-4.1.2.rc1-7118-quaddouble/local//share/polybori/flags.conf'\nsage: There was an error installing modified sage library code.\n\nERROR installing SAGE\n\nreal    0m4.375s\nuser    0m3.050s\nsys     0m1.290s\nsage: An error occurred while installing sage-4.1.2.rc1-7118-quaddouble\nPlease email sage-devel http://groups.google.com/group/sage-devel\nexplaining the problem and send the relevant part of\nof /scratch/mvngu/release/sandbox/sage-4.1.2.rc1-7118-quaddouble/install.log.  Describe your computer, operating system, etc.\nIf you want to try to fix the problem yourself, *don't* just cd to\n/scratch/mvngu/release/sandbox/sage-4.1.2.rc1-7118-quaddouble/spkg/build/sage-4.1.2.rc1-7118-quaddouble and type 'make'.\nInstead type \"/scratch/mvngu/release/sandbox/sage-4.1.2.rc1-7118-quaddouble/sage -sh\"\nin order to set all environment variables correctly, then cd to\n/scratch/mvngu/release/sandbox/sage-4.1.2.rc1-7118-quaddouble/spkg/build/sage-4.1.2.rc1-7118-quaddouble\n(When you are done debugging, you can type \"exit\" to leave the\nsubshell.)\nmake[1]: *** [installed/sage-4.1.2.rc1-7118-quaddouble] Error 1\nmake[1]: Leaving directory `/scratch/mvngu/release/sandbox/sage-4.1.2.rc1-7118-quaddouble/spkg'\n\nreal    50m13.360s\nuser    42m20.520s\nsys     7m27.370s\nError building Sage.\n```",
    "created_at": "2009-10-11T02:05:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7118#issuecomment-58885",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [install-7118-quaddouble.log.bz2](tarball://root/attachments/some-uuid/ticket7118/install-7118-quaddouble.log.bz2) by mvngu created at 2009-10-11 02:05:30

Applied patches in this order to Sage 4.1.2.rc0:

1. `trac_7118.patch`
2. `trac_7118-part2.patch`
 
Then uncompressed the file `SAGE_ROOT/data/extcode/pickle_jar/pickle_jar.tar.bz2` and removed the following files from the directory `SAGE_ROOT/data/extcode/pickle_jar/pickle_jar`:

1. `_type__sage_rings_real_rqdf_QuadDoubleElement__.sobj`
2. `_type__sage_rings_real_rqdf_QuadDoubleElement__.txt`
 
With these files removed, the directory `SAGE_ROOT/data/extcode/pickle_jar/pickle_jar` is compressed into a tarball again and replaced the previous version of the same tarball. From Mercurial's point of view, this would result in a change to a file it tracks, i.e. the pickle_jar.tar.bz2 has changed and all changes should be checked in. Now edit the file `SAGE_ROOT/spkg/install` to comment out the line related to quaddouble. The commented lines should be:

```
# See ticket #7118: remove quaddouble from sage                                 
# QUADDOUBLE=`$newest quaddouble`                                               
# export QUADDOUBLE
```
The file `SAGE_ROOT/spkg/install` is not tracked by Mercurial, so no need to check in changes. Also, edit the file `SAGE_ROOT/spkg/standard/deps` to comment out all lines related to quaddouble. The commented lines should be:

```
# See ticket #7118: remove quaddouble from sage
# $(INST)/$(QUADDOUBLE): $(BASE) $(INST)/$(MPIR) $(INST)/$(MPFR)
#       $(SAGE_SPKG) $(QUADDOUBLE) 2>&1

<SNIP>

                  # See ticket #7118: remove quaddouble from sage
                  # $(INST)/$(QUADDOUBLE) \
```
This file is also not tracked by Mercurial, so no need to check in changes. Finally, remove the package quaddouble-2.2.p9.spkg from the directory `SAGE_ROOT/spkg/standard` of standard Sage packages. With these changes, I made a new source tarball called "sage-4.1.2.rc1-7118-quaddouble". After unpacking that tarball and compiling from scratch, I got the following error. The full install log is attached.

```
g++ -o libcsage.so -shared src/convert.os src/interrupt.os src/mpn_pylong.os src/mpz_pylong.os src/mpz_longlong.os src/stdsage.os src/gmp_globals.os src/ZZ_pylong.os src/ntl_wrap.os -L/scratch/mvngu/release/sandbox/sage-4.1.2.rc1-7118-quaddouble/local/lib -lntl -lgmp -lpari
*** TOUCHING ALL CYTHON (.pyx) FILES ***
scons: `install' is up to date.

----------------------------------------------------------
sage: Building and installing modified Sage library files.


Installing c_lib
scons: `install' is up to date.
Traceback (most recent call last):
  File "setup.py", line 16, in <module>
    from module_list import ext_modules
  File "/scratch/mvngu/release/sandbox/sage-4.1.2.rc1-7118-quaddouble/devel/sage-main/module_list.py", line 84, in <module>
    for line in open(SAGE_LOCAL + "/share/polybori/flags.conf"):
IOError: [Errno 2] No such file or directory: '/scratch/mvngu/release/sandbox/sage-4.1.2.rc1-7118-quaddouble/local//share/polybori/flags.conf'
sage: There was an error installing modified sage library code.

ERROR installing SAGE

real    0m4.375s
user    0m3.050s
sys     0m1.290s
sage: An error occurred while installing sage-4.1.2.rc1-7118-quaddouble
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /scratch/mvngu/release/sandbox/sage-4.1.2.rc1-7118-quaddouble/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem yourself, *don't* just cd to
/scratch/mvngu/release/sandbox/sage-4.1.2.rc1-7118-quaddouble/spkg/build/sage-4.1.2.rc1-7118-quaddouble and type 'make'.
Instead type "/scratch/mvngu/release/sandbox/sage-4.1.2.rc1-7118-quaddouble/sage -sh"
in order to set all environment variables correctly, then cd to
/scratch/mvngu/release/sandbox/sage-4.1.2.rc1-7118-quaddouble/spkg/build/sage-4.1.2.rc1-7118-quaddouble
(When you are done debugging, you can type "exit" to leave the
subshell.)
make[1]: *** [installed/sage-4.1.2.rc1-7118-quaddouble] Error 1
make[1]: Leaving directory `/scratch/mvngu/release/sandbox/sage-4.1.2.rc1-7118-quaddouble/spkg'

real    50m13.360s
user    42m20.520s
sys     7m27.370s
Error building Sage.
```



---

archive/issue_comments_058886.json:
```json
{
    "body": "The error you get suggests a messed up deps file.  Here's mine, which worked (I think):\n\nhttp://sage.math.washington.edu/home/wstein/patches/7118/deps",
    "created_at": "2009-10-11T06:44:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7118#issuecomment-58886",
    "user": "https://github.com/williamstein"
}
```

The error you get suggests a messed up deps file.  Here's mine, which worked (I think):

http://sage.math.washington.edu/home/wstein/patches/7118/deps



---

archive/issue_comments_058887.json:
```json
{
    "body": "```\n23:35 < mvngu> williamstein: Any ideas about the error I reported at #7118 (remove quaddouble)?\n23:40 < williamstein> wow, I can't belive the pickle jar is under revision control -- that's stupid.\n23:41 < williamstein> but that is orthogonal.\n23:41 < williamstein> maybe you made a typo when editing module_list.py?\n23:42 < williamstein> wait, that was my patch.\n23:42 < mvngu> williamstein: I didn't touch module_list.py\n23:42 < williamstein> hmm.\n23:42 < williamstein> i'll post my deps file.\n23:42 < williamstein> maybe there is a typo ther.e\n23:43 < williamstein> the error you get suggests a messed up deps file.\n23:44 < williamstein> http://sage.math.washington.edu/home/wstein/patches/7118/deps\n23:45 < williamstein> my wife just decided to stay overnight at her friends house, since they are having so much fun... so\n23:45 < williamstein> sounds like a good night for a Sage all nighter for me!\n23:46 < williamstein> 3 new sagenb users in the last few minutes...\n23:47 < williamstein> mvngu -- thanks again for looking at the #7118!\n23:49 < mvngu> williamstein: A diff of the original deps vs. your changed deps... this suggests that I should really delete lines relating to quaddouble, instead of commenting them out.\n23:49 < williamstein> You should try that.\n23:50 < mvngu> trying now...\n```",
    "created_at": "2009-10-11T10:14:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7118#issuecomment-58887",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

```
23:35 < mvngu> williamstein: Any ideas about the error I reported at #7118 (remove quaddouble)?
23:40 < williamstein> wow, I can't belive the pickle jar is under revision control -- that's stupid.
23:41 < williamstein> but that is orthogonal.
23:41 < williamstein> maybe you made a typo when editing module_list.py?
23:42 < williamstein> wait, that was my patch.
23:42 < mvngu> williamstein: I didn't touch module_list.py
23:42 < williamstein> hmm.
23:42 < williamstein> i'll post my deps file.
23:42 < williamstein> maybe there is a typo ther.e
23:43 < williamstein> the error you get suggests a messed up deps file.
23:44 < williamstein> http://sage.math.washington.edu/home/wstein/patches/7118/deps
23:45 < williamstein> my wife just decided to stay overnight at her friends house, since they are having so much fun... so
23:45 < williamstein> sounds like a good night for a Sage all nighter for me!
23:46 < williamstein> 3 new sagenb users in the last few minutes...
23:47 < williamstein> mvngu -- thanks again for looking at the #7118!
23:49 < mvngu> williamstein: A diff of the original deps vs. your changed deps... this suggests that I should really delete lines relating to quaddouble, instead of commenting them out.
23:49 < williamstein> You should try that.
23:50 < mvngu> trying now...
```



---

archive/issue_comments_058888.json:
```json
{
    "body": "doctest on bsd.math",
    "created_at": "2009-10-12T03:19:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7118#issuecomment-58888",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

doctest on bsd.math



---

archive/issue_comments_058889.json:
```json
{
    "body": "Attachment [doctest-cicero.log](tarball://root/attachments/some-uuid/ticket7118/doctest-cicero.log) by mvngu created at 2009-10-12 03:24:29\n\ndoctest on cicero on SkyNet",
    "created_at": "2009-10-12T03:24:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7118#issuecomment-58889",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [doctest-cicero.log](tarball://root/attachments/some-uuid/ticket7118/doctest-cicero.log) by mvngu created at 2009-10-12 03:24:29

doctest on cicero on SkyNet



---

archive/issue_comments_058890.json:
```json
{
    "body": "doctest on eno on SkyNet",
    "created_at": "2009-10-12T03:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7118#issuecomment-58890",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

doctest on eno on SkyNet



---

archive/issue_comments_058891.json:
```json
{
    "body": "Attachment [doctest-eno.log](tarball://root/attachments/some-uuid/ticket7118/doctest-eno.log) by mvngu created at 2009-10-12 03:41:01\n\ndoctest on mandriva2009-64 on boxen.math",
    "created_at": "2009-10-12T03:41:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7118#issuecomment-58891",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [doctest-eno.log](tarball://root/attachments/some-uuid/ticket7118/doctest-eno.log) by mvngu created at 2009-10-12 03:41:01

doctest on mandriva2009-64 on boxen.math



---

archive/issue_comments_058892.json:
```json
{
    "body": "Attachment [doctest-cento53-64-boxen.log](tarball://root/attachments/some-uuid/ticket7118/doctest-cento53-64-boxen.log) by mvngu created at 2009-10-12 03:46:23\n\ndoctest on cento53-64 on boxen.math",
    "created_at": "2009-10-12T03:46:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7118#issuecomment-58892",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [doctest-cento53-64-boxen.log](tarball://root/attachments/some-uuid/ticket7118/doctest-cento53-64-boxen.log) by mvngu created at 2009-10-12 03:46:23

doctest on cento53-64 on boxen.math



---

archive/issue_comments_058893.json:
```json
{
    "body": "Attachment [doctest-opensuse32-boxen.log](tarball://root/attachments/some-uuid/ticket7118/doctest-opensuse32-boxen.log) by mvngu created at 2009-10-12 03:51:33\n\ndoctest on opensuse32 on boxen.math",
    "created_at": "2009-10-12T03:51:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7118#issuecomment-58893",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [doctest-opensuse32-boxen.log](tarball://root/attachments/some-uuid/ticket7118/doctest-opensuse32-boxen.log) by mvngu created at 2009-10-12 03:51:33

doctest on opensuse32 on boxen.math



---

archive/issue_comments_058894.json:
```json
{
    "body": "doctest on opensuse64 on boxen.math",
    "created_at": "2009-10-12T03:56:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7118#issuecomment-58894",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

doctest on opensuse64 on boxen.math



---

archive/issue_comments_058895.json:
```json
{
    "body": "Attachment [doctest-opensuse64-boxen.log](tarball://root/attachments/some-uuid/ticket7118/doctest-opensuse64-boxen.log) by mvngu created at 2009-10-12 05:17:10\n\nThis time, I really deleted the following lines from the file `SAGE_ROOT/spkg/standard/deps`:\n\n```\n$(INST)/$(QUADDOUBLE): $(BASE) $(INST)/$(MPIR) $(INST)/$(MPFR)\n      $(SAGE_SPKG) $(QUADDOUBLE) 2>&1\n\n<SNIP>\n\n                  See ticket #7118: remove quaddouble from sage\n                  $(INST)/$(QUADDOUBLE) \\\n```\nI made a new source tarball called \"sage-4.1.2.rc1-7118-quaddouble\" that incorporates the cliquer spkg at #6681. The new source tarball was tested on the following platforms:\n\n* sage.math: 64-bit Ubuntu 8.04.3 LTS, GCC 4.2.4 --- compile OK; all doctests pass.\n* rosemary.math: 64-bit Red Hat Enterprise Linux Server 5.4, GCC 4.1.2 --- compile OK; all doctests pass.\n* bsd.math: Mac OS X 10.6.1, GCC 4.2.1 --- compile OK; some doctest failures:\n {{{\nsage -t -long \"rc1-7118-6681/devel/sage/sage/calculus/calculus.py\"\nsage -t -long \"rc1-7118-6681/devel/sage/sage/calculus/tests.py\"\nsage -t -long \"rc1-7118-6681/devel/sage/sage/calculus/wester.py\"\nsage -t -long \"rc1-7118-6681/devel/sage/sage/ext/fast_eval.pyx\"\nsage -t -long \"rc1-7118-6681/devel/sage/sage/functions/hyperbolic.py\"\nsage -t -long \"rc1-7118-6681/devel/sage/sage/functions/other.py\"\nsage -t -long \"rc1-7118-6681/devel/sage/sage/functions/trig.py\"\nsage -t -long \"rc1-7118-6681/devel/sage/sage/gsl/interpolation.pyx\"\nsage -t -long \"rc1-7118-6681/devel/sage/sage/matrix/matrix_symbolic_dense.pyx\"\nsage -t -long \"rc1-7118-6681/devel/sage/sage/rings/polynomial/pbori.pyx\"\nsage -t -long \"rc1-7118-6681/devel/sage/sage/symbolic/constants.py\"\nsage -t -long \"rc1-7118-6681/devel/sage/sage/symbolic/expression.pyx\"\nsage -t -long \"rc1-7118-6681/devel/sage/sage/symbolic/function.pyx\"\n }}}\n Full doctest log is attached; see the attachment `doctest-bsd.math.log`.\n* cicero on SkyNet: 32-bit Fedora 9, GCC 4.4.1 --- compile OK; some doctest failures:\n {{{\nsage -t -long \"devel/sage/sage/misc/randstate.pyx\"\nsage -t -long \"devel/sage/sage/interfaces/expect.py\"\nsage -t -long \"devel/sage/sage/interfaces/sage0.py\"\nsage -t -long \"devel/sage/sage/server/simple/twist.py\"\n }}}\n Full doctest log is attached; see the attachment `doctest-cicero.log`.\n* eno on SkyNet: 64-bit Fedora 9, GCC 4.4.1 --- compile OK; some doctest failures:\n {{{\nsage -t -long \"devel/sage/sage/rings/fast_arith.pyx\"\nsage -t -long \"devel/sage/sage/rings/tests.py\"\n }}}\n Full doctest log is attached; see the attachment `doctest-eno.log`.\n* lena on SkyNet: 64-bit Red Hat Enterprise Linux Server 5.3, GCC 4.4.1 --- compile OK; all doctests pass.\n* menas on SkyNet: 64-bit openSUSE 11.1, GCC 4.4.1 --- compile OK; all doctests pass.\n* cento53-64 on boxen.math: 64-bit CentOS 5.3, GCC 4.1.2 --- compile OK; one doctest failure:\n {{{\nsage -t -long \"devel/sage/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx\"\n }}}\n Full doctest log is attached; see the attachment `doctest-cento53-64-boxen.log`.\n* debian5-32 on boxen.math: 32-bit Debian 5.0, GCC 4.3.2 --- compile OK; all doctests pass.\n* debian5-64 on boxen.math: 64-bit Debian 5.0, GCC 4.3.2 --- compile OK; all doctests pass.\n* mandriva2009.1-32 on boxen.math: 32-bit Mandriva Linux 2009.1, GCC 4.3.2 --- compile OK; all doctests pass.\n* mandriva2009.1-64 on boxen.math: 64-bit Mandriva Linux 2009.1, GCC 4.3.2 --- compile OK; one doctest failure:\n {{{\nsage -t -long \"devel/sage/sage/server/simple/twist.py\"\n }}}\n Full doctest log is attached; see the attachment `doctest-mandriva2009-64.boxen.log`.\n* opensuse-11.1-32 on boxen.math: 32-bit openSUSE 11.1, GCC 4.3.2 --- compile OK; one doctest failure:\n {{{\nsage -t -long \"devel/sage/sage/server/simple/twist.py\"\n }}}\n Full doctest log is attached; see the attachment `doctest-opensuse32-boxen.log`.\n* opensuse-11.1-64 on boxen.math: 64-bit openSUSE 11.1, GCC 4.3.2 --- compile OK; one doctest failure:\n {{{\nsage -t -long \"devel/sage/sage/graphs/graph_plot.py\"\n }}}\n Full doctest log is attached; see the attachment `doctest-opensuse64-boxen.log`.\n* ubuntu9.04-32: 32-bit Ubuntu 9.04, GCC 4.3.3 --- compile OK; all doctests pass.\n* ubuntu9.04-64: 64-bit Ubuntu 9.04, GCC 4.3.3 --- compile OK; all doctests pass.",
    "created_at": "2009-10-12T05:17:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7118#issuecomment-58895",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [doctest-opensuse64-boxen.log](tarball://root/attachments/some-uuid/ticket7118/doctest-opensuse64-boxen.log) by mvngu created at 2009-10-12 05:17:10

This time, I really deleted the following lines from the file `SAGE_ROOT/spkg/standard/deps`:

```
$(INST)/$(QUADDOUBLE): $(BASE) $(INST)/$(MPIR) $(INST)/$(MPFR)
      $(SAGE_SPKG) $(QUADDOUBLE) 2>&1

<SNIP>

                  See ticket #7118: remove quaddouble from sage
                  $(INST)/$(QUADDOUBLE) \
```
I made a new source tarball called "sage-4.1.2.rc1-7118-quaddouble" that incorporates the cliquer spkg at #6681. The new source tarball was tested on the following platforms:

* sage.math: 64-bit Ubuntu 8.04.3 LTS, GCC 4.2.4 --- compile OK; all doctests pass.
* rosemary.math: 64-bit Red Hat Enterprise Linux Server 5.4, GCC 4.1.2 --- compile OK; all doctests pass.
* bsd.math: Mac OS X 10.6.1, GCC 4.2.1 --- compile OK; some doctest failures:
 {{{
sage -t -long "rc1-7118-6681/devel/sage/sage/calculus/calculus.py"
sage -t -long "rc1-7118-6681/devel/sage/sage/calculus/tests.py"
sage -t -long "rc1-7118-6681/devel/sage/sage/calculus/wester.py"
sage -t -long "rc1-7118-6681/devel/sage/sage/ext/fast_eval.pyx"
sage -t -long "rc1-7118-6681/devel/sage/sage/functions/hyperbolic.py"
sage -t -long "rc1-7118-6681/devel/sage/sage/functions/other.py"
sage -t -long "rc1-7118-6681/devel/sage/sage/functions/trig.py"
sage -t -long "rc1-7118-6681/devel/sage/sage/gsl/interpolation.pyx"
sage -t -long "rc1-7118-6681/devel/sage/sage/matrix/matrix_symbolic_dense.pyx"
sage -t -long "rc1-7118-6681/devel/sage/sage/rings/polynomial/pbori.pyx"
sage -t -long "rc1-7118-6681/devel/sage/sage/symbolic/constants.py"
sage -t -long "rc1-7118-6681/devel/sage/sage/symbolic/expression.pyx"
sage -t -long "rc1-7118-6681/devel/sage/sage/symbolic/function.pyx"
 }}}
 Full doctest log is attached; see the attachment `doctest-bsd.math.log`.
* cicero on SkyNet: 32-bit Fedora 9, GCC 4.4.1 --- compile OK; some doctest failures:
 {{{
sage -t -long "devel/sage/sage/misc/randstate.pyx"
sage -t -long "devel/sage/sage/interfaces/expect.py"
sage -t -long "devel/sage/sage/interfaces/sage0.py"
sage -t -long "devel/sage/sage/server/simple/twist.py"
 }}}
 Full doctest log is attached; see the attachment `doctest-cicero.log`.
* eno on SkyNet: 64-bit Fedora 9, GCC 4.4.1 --- compile OK; some doctest failures:
 {{{
sage -t -long "devel/sage/sage/rings/fast_arith.pyx"
sage -t -long "devel/sage/sage/rings/tests.py"
 }}}
 Full doctest log is attached; see the attachment `doctest-eno.log`.
* lena on SkyNet: 64-bit Red Hat Enterprise Linux Server 5.3, GCC 4.4.1 --- compile OK; all doctests pass.
* menas on SkyNet: 64-bit openSUSE 11.1, GCC 4.4.1 --- compile OK; all doctests pass.
* cento53-64 on boxen.math: 64-bit CentOS 5.3, GCC 4.1.2 --- compile OK; one doctest failure:
 {{{
sage -t -long "devel/sage/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx"
 }}}
 Full doctest log is attached; see the attachment `doctest-cento53-64-boxen.log`.
* debian5-32 on boxen.math: 32-bit Debian 5.0, GCC 4.3.2 --- compile OK; all doctests pass.
* debian5-64 on boxen.math: 64-bit Debian 5.0, GCC 4.3.2 --- compile OK; all doctests pass.
* mandriva2009.1-32 on boxen.math: 32-bit Mandriva Linux 2009.1, GCC 4.3.2 --- compile OK; all doctests pass.
* mandriva2009.1-64 on boxen.math: 64-bit Mandriva Linux 2009.1, GCC 4.3.2 --- compile OK; one doctest failure:
 {{{
sage -t -long "devel/sage/sage/server/simple/twist.py"
 }}}
 Full doctest log is attached; see the attachment `doctest-mandriva2009-64.boxen.log`.
* opensuse-11.1-32 on boxen.math: 32-bit openSUSE 11.1, GCC 4.3.2 --- compile OK; one doctest failure:
 {{{
sage -t -long "devel/sage/sage/server/simple/twist.py"
 }}}
 Full doctest log is attached; see the attachment `doctest-opensuse32-boxen.log`.
* opensuse-11.1-64 on boxen.math: 64-bit openSUSE 11.1, GCC 4.3.2 --- compile OK; one doctest failure:
 {{{
sage -t -long "devel/sage/sage/graphs/graph_plot.py"
 }}}
 Full doctest log is attached; see the attachment `doctest-opensuse64-boxen.log`.
* ubuntu9.04-32: 32-bit Ubuntu 9.04, GCC 4.3.3 --- compile OK; all doctests pass.
* ubuntu9.04-64: 64-bit Ubuntu 9.04, GCC 4.3.3 --- compile OK; all doctests pass.



---

archive/issue_comments_058896.json:
```json
{
    "body": "This is \"needs review\", but it looks like these patches have been merged -- changesets 13089:ab082b3c94fe and 13090:06b7dd9afde9. Perhaps having released 4.1.2 and 4.2, with plenty of people reporting all doctests passing, counts as a sort of positive review?",
    "created_at": "2009-10-30T00:06:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7118#issuecomment-58896",
    "user": "https://github.com/dandrake"
}
```

This is "needs review", but it looks like these patches have been merged -- changesets 13089:ab082b3c94fe and 13090:06b7dd9afde9. Perhaps having released 4.1.2 and 4.2, with plenty of people reporting all doctests passing, counts as a sort of positive review?



---

archive/issue_comments_058897.json:
```json
{
    "body": "Replying to [comment:12 ddrake]:\n> This is \"needs review\", but it looks like these patches have been merged -- changesets 13089:ab082b3c94fe and 13090:06b7dd9afde9. Perhaps having released 4.1.2 and 4.2, with plenty of people reporting all doctests passing, counts as a sort of positive review?\n\n\nI wanted to give the ticket a positive after writing up my test results on various platforms. But my mind at the time was more focused on my thesis, so I didn't actually change the status to \"positive review\". I apologize for the confusion. Now the status is positive review, and the ticket can be closed as fixed.",
    "created_at": "2009-10-30T05:09:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7118#issuecomment-58897",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:12 ddrake]:
> This is "needs review", but it looks like these patches have been merged -- changesets 13089:ab082b3c94fe and 13090:06b7dd9afde9. Perhaps having released 4.1.2 and 4.2, with plenty of people reporting all doctests passing, counts as a sort of positive review?


I wanted to give the ticket a positive after writing up my test results on various platforms. But my mind at the time was more focused on my thesis, so I didn't actually change the status to "positive review". I apologize for the confusion. Now the status is positive review, and the ticket can be closed as fixed.



---

archive/issue_comments_058898.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-30T05:09:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7118#issuecomment-58898",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_016823.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-10-30T05:10:40Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7118",
    "milestone": "sage-4.1.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7118#event-16823"
}
```



---

archive/issue_events_016824.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-10-31T16:39:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7118",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7118#event-16824"
}
```



---

archive/issue_comments_058899.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-31T16:39:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7118",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7118#issuecomment-58899",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
