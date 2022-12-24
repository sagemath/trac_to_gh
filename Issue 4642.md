# Issue 4642: Limit sage-flags.txt to vector math flags

archive/issues_004642.json:
```json
{
    "body": "Assignee: mabshoff\n\nJeffrey reported:\n\n```\nI've just downloaded and launched Sage on an Ubuntu 8.10 box.  I \nunzipped the file and ran ./sage and got this: \n  WARNING!  This Sage install was built on a machine that supports \n  instructions that are not available on this computer.  Sage will \n  likely fail with ILLEGAL INSTRUCTION errors! The following processor \n  flags were on the build machine but are not on this computer: \n  nx up \nI downloaded this image of Sage: \n  sage-3.2-ubuntu32bit-intel-i686-Linux.tar.gz \nIs there anything I can do? \nThanks in advance \nJeffrey \n```\n\n\nThe problem is that nx for example is a no execute flag and has zero impact on compatibility for binaries. We should only trac sse, sse2 and see3 flags (and potentially others, but I will do some research here.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4642\n\n",
    "created_at": "2008-11-28T07:41:37Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "title": "Limit sage-flags.txt to vector math flags",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4642",
    "user": "mabshoff"
}
```
Assignee: mabshoff

Jeffrey reported:

```
I've just downloaded and launched Sage on an Ubuntu 8.10 box.  I 
unzipped the file and ran ./sage and got this: 
  WARNING!  This Sage install was built on a machine that supports 
  instructions that are not available on this computer.  Sage will 
  likely fail with ILLEGAL INSTRUCTION errors! The following processor 
  flags were on the build machine but are not on this computer: 
  nx up 
I downloaded this image of Sage: 
  sage-3.2-ubuntu32bit-intel-i686-Linux.tar.gz 
Is there anything I can do? 
Thanks in advance 
Jeffrey 
```


The problem is that nx for example is a no execute flag and has zero impact on compatibility for binaries. We should only trac sse, sse2 and see3 flags (and potentially others, but I will do some research here.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4642





---

archive/issue_comments_034941.json:
```json
{
    "body": "Can somebody please post a list of flags to be ignored here.  Obviously up and nx are on it.  Anything else?",
    "created_at": "2008-11-28T15:42:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4642#issuecomment-34941",
    "user": "was"
}
```

Can somebody please post a list of flags to be ignored here.  Obviously up and nx are on it.  Anything else?



---

archive/issue_comments_034942.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-11-28T15:42:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4642#issuecomment-34942",
    "user": "was"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_034943.json:
```json
{
    "body": "Replying to [comment:1 was]:\n> Can somebody please post a list of flags to be ignored here.  Obviously up and nx are on it.  Anything else?\n\nWhy don't we do it the other way around, i.e. only consider flags we know cause trouble: sse, sse2, sse4 and maybe three or four more. These flags are vectorization flags and are the only ones I am aware of that need consideration. All the other flags are CPU properties that aren't related to instruction sets.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-28T18:28:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4642#issuecomment-34943",
    "user": "mabshoff"
}
```

Replying to [comment:1 was]:
> Can somebody please post a list of flags to be ignored here.  Obviously up and nx are on it.  Anything else?

Why don't we do it the other way around, i.e. only consider flags we know cause trouble: sse, sse2, sse4 and maybe three or four more. These flags are vectorization flags and are the only ones I am aware of that need consideration. All the other flags are CPU properties that aren't related to instruction sets.

Cheers,

Michael



---

archive/issue_comments_034944.json:
```json
{
    "body": "Attachment [trac_4642_sage.patch](tarball://root/attachments/some-uuid/ticket4642/trac_4642_sage.patch) by was created at 2008-11-28 21:08:34\n\nI named the patch trac_4642_sage.patch but it should be trac_4642_scripts.patch",
    "created_at": "2008-11-28T21:08:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4642#issuecomment-34944",
    "user": "was"
}
```

Attachment [trac_4642_sage.patch](tarball://root/attachments/some-uuid/ticket4642/trac_4642_sage.patch) by was created at 2008-11-28 21:08:34

I named the patch trac_4642_sage.patch but it should be trac_4642_scripts.patch



---

archive/issue_comments_034945.json:
```json
{
    "body": "This is a true blocker for 3.2.1. Positive review, but I will do some more testing.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-28T21:32:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4642#issuecomment-34945",
    "user": "mabshoff"
}
```

This is a true blocker for 3.2.1. Positive review, but I will do some more testing.

Cheers,

Michael



---

archive/issue_comments_034946.json:
```json
{
    "body": "Two more flags I would consider:\n\n* pni - prescott new instructions\n* cmov - an older instruction present on Pentiums or higher - that might be pushing it, but you never know :)\n\nCheers,\n\nMichael",
    "created_at": "2008-11-29T00:13:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4642#issuecomment-34946",
    "user": "mabshoff"
}
```

Two more flags I would consider:

* pni - prescott new instructions
* cmov - an older instruction present on Pentiums or higher - that might be pushing it, but you never know :)

Cheers,

Michael



---

archive/issue_comments_034947.json:
```json
{
    "body": "I did some more testing and the patch works as expected. One problem is when one does a -bdist from a 3.2 install with the old flags then the new binary complains about all the lfags that are now omitted, but since one generally does not -bdist repeatedly from the same install that seems fine by me.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-29T00:25:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4642#issuecomment-34947",
    "user": "mabshoff"
}
```

I did some more testing and the patch works as expected. One problem is when one does a -bdist from a 3.2 install with the old flags then the new binary complains about all the lfags that are now omitted, but since one generally does not -bdist repeatedly from the same install that seems fine by me.

Cheers,

Michael



---

archive/issue_comments_034948.json:
```json
{
    "body": "Updated version of William's patch with cmov and pni flags added",
    "created_at": "2008-11-29T04:28:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4642#issuecomment-34948",
    "user": "mabshoff"
}
```

Updated version of William's patch with cmov and pni flags added



---

archive/issue_comments_034949.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-29T04:28:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4642#issuecomment-34949",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_034950.json:
```json
{
    "body": "Attachment [trac_4642_sage.2.patch](tarball://root/attachments/some-uuid/ticket4642/trac_4642_sage.2.patch) by mabshoff created at 2008-11-29 04:28:57\n\nMerged in Sage 3.2.1.rc0",
    "created_at": "2008-11-29T04:28:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4642#issuecomment-34950",
    "user": "mabshoff"
}
```

Attachment [trac_4642_sage.2.patch](tarball://root/attachments/some-uuid/ticket4642/trac_4642_sage.2.patch) by mabshoff created at 2008-11-29 04:28:57

Merged in Sage 3.2.1.rc0



---

archive/issue_comments_034951.json:
```json
{
    "body": "For the record: trac_4642_sage.2.patch was merged.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-29T04:29:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4642#issuecomment-34951",
    "user": "mabshoff"
}
```

For the record: trac_4642_sage.2.patch was merged.

Cheers,

Michael
