# Issue 9839: link-editor thinks ECL library contains non-pic code on *all* 64-bit Solaris/OpenSolaris releases

archive/issues_009839.json:
```json
{
    "body": "Assignee: drkirkby\n\nAs noted at #9099, Maxima fails to build properly on OpenSolaris x64. The ticket then went onto discuss specific doctest failures on 32-bit Solaris n x86. \n\nHowever, the reason Maxima was not working on OpenSolaris is totally unrelated and  **much** wider. It has nothing to do with Maxima, but is almost certainly an issue with ECL. \n\nHence it seemed wise to open a ticket specific for this. \n\nThe problem is that the link-editor thinks the ecl shared library contains text relocations, which is why there was an error like \n\n\n\n```\nld.so.1: ecl: fatal: relocation error: R_AMD64_PC32: file /export/home/drkirkby/sage-4.4.2/local/lib//libecl.so: symbol main: value 0x22800097de04 does not fit\n```\n\n\nThere's a command given on this Sun blog\n\nhttp://blogs.sun.com/rie/entry/my_relocations_don_t_fit\n\nwhich will show libraries with this problem. \n\n == OpenSolaris on x64 ==\n\nI built the latest ECL snapshot outside of Sage, and run the suggested command on the ECL library. Note, this a different version of ECL built at a later date. \n\n\n```\ndrkirkby@hawk:/tmp/ecl$ ./configure \ndrkirkby@hawk:/tmp/ecl$ make\n```\n\n\nthen the all important: \n\n\n```\ndrkirkby@hawk:/tmp/ecl$ elfdump -d ./build/libecl.so |  fgrep TEXTREL\n      [23]  TEXTREL           0\n      [31]  FLAGS             0x4                 [ TEXTREL ]\n\n```\n\nwhich indicates a problem - there should be no output from that. \n\nIt's also suggested to compile with some debugging information:\n\n\n```\n$ export LD_OPTIONS=-Dreloc,detail \n$ unset MAKE\n$ make\n```\n\n\nA full log is attached of that.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9840\n\n",
    "created_at": "2010-08-30T12:11:30Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "link-editor thinks ECL library contains non-pic code on *all* 64-bit Solaris/OpenSolaris releases",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9839",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

As noted at #9099, Maxima fails to build properly on OpenSolaris x64. The ticket then went onto discuss specific doctest failures on 32-bit Solaris n x86. 

However, the reason Maxima was not working on OpenSolaris is totally unrelated and  **much** wider. It has nothing to do with Maxima, but is almost certainly an issue with ECL. 

Hence it seemed wise to open a ticket specific for this. 

The problem is that the link-editor thinks the ecl shared library contains text relocations, which is why there was an error like 



```
ld.so.1: ecl: fatal: relocation error: R_AMD64_PC32: file /export/home/drkirkby/sage-4.4.2/local/lib//libecl.so: symbol main: value 0x22800097de04 does not fit
```


There's a command given on this Sun blog

http://blogs.sun.com/rie/entry/my_relocations_don_t_fit

which will show libraries with this problem. 

 == OpenSolaris on x64 ==

I built the latest ECL snapshot outside of Sage, and run the suggested command on the ECL library. Note, this a different version of ECL built at a later date. 


```
drkirkby@hawk:/tmp/ecl$ ./configure 
drkirkby@hawk:/tmp/ecl$ make
```


then the all important: 


```
drkirkby@hawk:/tmp/ecl$ elfdump -d ./build/libecl.so |  fgrep TEXTREL
      [23]  TEXTREL           0
      [31]  FLAGS             0x4                 [ TEXTREL ]

```

which indicates a problem - there should be no output from that. 

It's also suggested to compile with some debugging information:


```
$ export LD_OPTIONS=-Dreloc,detail 
$ unset MAKE
$ make
```


A full log is attached of that.

Issue created by migration from https://trac.sagemath.org/ticket/9840





---

archive/issue_comments_096959.json:
```json
{
    "body": "Attachment [complete-log-of-OpenSolaris-86-built.txt.gz](tarball://root/attachments/some-uuid/ticket9840/complete-log-of-OpenSolaris-86-built.txt.gz) by drkirkby created at 2010-08-30 12:13:45\n\nBuild log on OpenSolaris, when using debugging options to show text relocations.",
    "created_at": "2010-08-30T12:13:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9839#issuecomment-96959",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Attachment [complete-log-of-OpenSolaris-86-built.txt.gz](tarball://root/attachments/some-uuid/ticket9840/complete-log-of-OpenSolaris-86-built.txt.gz) by drkirkby created at 2010-08-30 12:13:45

Build log on OpenSolaris, when using debugging options to show text relocations.



---

archive/issue_comments_096960.json:
```json
{
    "body": "It should be noted this problem exists on every combination of Solaris/OpenSolaris system tested\n\n* 32-bit Solaris 10 on SPARC\n* 64-bit Solaris 10 on SPARC\n* 32-bit Solaris 10 on x86\n* 64-bit Solaris 10 on x86\n* 32-bit OpenSolaris on x86\n* 64-bit OpenSolaris on x86\n\nHowever, on 32-bit builds, the text relocation issues are not actually causing any problems, so we can live with that. On 64-bit builds, it completely screws things up. \n\nSimilar issues with text relocation has been observed with: \n\n* Cliquer - solved with a change of compiler flags (#9871)\n* PolyBoRi - solved in the latest upstream release (#9872)\n* R - unsolved (#9040)\n\nSo it's only R and ECL which have this problem outstanding. \n\nDave",
    "created_at": "2010-09-16T10:03:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9839#issuecomment-96960",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

It should be noted this problem exists on every combination of Solaris/OpenSolaris system tested

* 32-bit Solaris 10 on SPARC
* 64-bit Solaris 10 on SPARC
* 32-bit Solaris 10 on x86
* 64-bit Solaris 10 on x86
* 32-bit OpenSolaris on x86
* 64-bit OpenSolaris on x86

However, on 32-bit builds, the text relocation issues are not actually causing any problems, so we can live with that. On 64-bit builds, it completely screws things up. 

Similar issues with text relocation has been observed with: 

* Cliquer - solved with a change of compiler flags (#9871)
* PolyBoRi - solved in the latest upstream release (#9872)
* R - unsolved (#9040)

So it's only R and ECL which have this problem outstanding. 

Dave



---

archive/issue_comments_096961.json:
```json
{
    "body": "This has ben fixed upstream, and is the result of using a GCC extension (computed gotos), which don't seem to work properly on Solaris. As yet, I am unaware what the fix is, though I've been told its been fixed. \n\nDave",
    "created_at": "2010-11-09T09:18:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9839#issuecomment-96961",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

This has ben fixed upstream, and is the result of using a GCC extension (computed gotos), which don't seem to work properly on Solaris. As yet, I am unaware what the fix is, though I've been told its been fixed. 

Dave



---

archive/issue_comments_096962.json:
```json
{
    "body": "This problem was fixed by #10766, so can be closed as fixed in sage-4.7.alpha1",
    "created_at": "2011-04-02T12:30:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9839#issuecomment-96962",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

This problem was fixed by #10766, so can be closed as fixed in sage-4.7.alpha1



---

archive/issue_events_024773.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-04-05T15:55:34Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9839",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9839#event-24773"
}
```



---

archive/issue_comments_096963.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-04-05T15:55:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9839",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9839#issuecomment-96963",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate



---

archive/issue_events_024774.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-04-05T15:55:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9839",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9839#event-24774"
}
```
