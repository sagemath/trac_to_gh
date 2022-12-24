# Issue 5328: Make the ATLAS rebuild on tolerance incremental (followup to #1641)

archive/issues_005328.json:
```json
{
    "body": "Assignee: mabshoff\n\nMy spkg from #1641 did not work 100% due to a bug in spkg-install that detected the failure. The fix is to delete error* in ATLAS' build directory on restart. \n\nSince on some machines the ATLAS tune can fail hours into the build, i.e. Itanium or Sparc the incremental restart is the better solution IMHO.\n\nNote that #5219 should be taken care of at the same time.\n\nCheers,\n\nMichael \n\nIssue created by migration from https://trac.sagemath.org/ticket/5328\n\n",
    "created_at": "2009-02-21T07:01:14Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Make the ATLAS rebuild on tolerance incremental (followup to #1641)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5328",
    "user": "mabshoff"
}
```
Assignee: mabshoff

My spkg from #1641 did not work 100% due to a bug in spkg-install that detected the failure. The fix is to delete error* in ATLAS' build directory on restart. 

Since on some machines the ATLAS tune can fail hours into the build, i.e. Itanium or Sparc the incremental restart is the better solution IMHO.

Note that #5219 should be taken care of at the same time.

Cheers,

Michael 

Issue created by migration from https://trac.sagemath.org/ticket/5328





---

archive/issue_comments_041012.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-21T07:03:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5328#issuecomment-41012",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_041013.json:
```json
{
    "body": "This info from the ATLAS 3.8 errata page might also be relevant here:\n\n```\nHow do I restart an interrupted install?\n\nIf your ATLAS install was interrupted, and you have fixed the problem, you \ncan usually safely (there are always exceptions; if the install died in the \nmiddle of an ar command, for instance, many systems cannot recover) restart \nthe install by:\n\n(1) Edit your Make.inc and if the INSTFLAGS macro includes the flags -a 1 \nchange them to: -a 0. This tells ATLAS not to recopy the arch defaults \nover your partially completed results.\n\n(2) Issuing \"make\" from your BLDdir directory.\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-02-21T07:33:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5328#issuecomment-41013",
    "user": "mabshoff"
}
```

This info from the ATLAS 3.8 errata page might also be relevant here:

```
How do I restart an interrupted install?

If your ATLAS install was interrupted, and you have fixed the problem, you 
can usually safely (there are always exceptions; if the install died in the 
middle of an ar command, for instance, many systems cannot recover) restart 
the install by:

(1) Edit your Make.inc and if the INSTFLAGS macro includes the flags -a 1 
change them to: -a 0. This tells ATLAS not to recopy the arch defaults 
over your partially completed results.

(2) Issuing "make" from your BLDdir directory.
```


Cheers,

Michael



---

archive/issue_comments_041014.json:
```json
{
    "body": "Better luck in 3.4.1.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-01T02:22:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5328#issuecomment-41014",
    "user": "mabshoff"
}
```

Better luck in 3.4.1.

Cheers,

Michael



---

archive/issue_comments_041015.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2013-05-16T07:52:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5328#issuecomment-41015",
    "user": "jdemeyer"
}
```

Resolution: duplicate



---

archive/issue_comments_041016.json:
```json
{
    "body": "I assume this is obsoleted by #10508.",
    "created_at": "2013-05-16T07:52:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5328",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5328#issuecomment-41016",
    "user": "jdemeyer"
}
```

I assume this is obsoleted by #10508.
