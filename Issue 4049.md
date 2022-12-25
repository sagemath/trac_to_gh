# Issue 4049: Don't use the -i option to tar as it does not exist on most BSDs

archive/issues_004049.json:
```json
{
    "body": "Assignee: cwitty\n\nWhile trying to compile sage under OpenBSD, the first problem I encountered was that it could not extract the spkgs because it passes the -i option to tar which is not recognized.  \n\nAfter reading the description of the meaning of that option on a linux man page:\n\n `--ignore-zeros'\n `-i'\n      With this option, `tar' will ignore zeroed blocks in the archive,\n      which normally signals EOF. \n\nAnd additional information about what is a zero block:\n\n Normally, `tar' stops reading when it encounters a block of zeros\n between file entries (which usually indicates the end of the archive).\n `--ignore-zeros' (`-i') allows `tar' to completely read an archive\n which contains a block of zeros before the end (i.e. a damaged archive,\n or one which was created by concatenating several archives together).\n\nI concluded that unless some spkgs are created by concatenating several tar archives together this option can be safely removed.\n\nIf there is a consensus to keep the option, I could always make a new patch \n\nIssue created by migration from https://trac.sagemath.org/ticket/4049\n\n",
    "created_at": "2008-09-03T17:59:15Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "Don't use the -i option to tar as it does not exist on most BSDs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4049",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```
Assignee: cwitty

While trying to compile sage under OpenBSD, the first problem I encountered was that it could not extract the spkgs because it passes the -i option to tar which is not recognized.  

After reading the description of the meaning of that option on a linux man page:

 `--ignore-zeros'
 `-i'
      With this option, `tar' will ignore zeroed blocks in the archive,
      which normally signals EOF. 

And additional information about what is a zero block:

 Normally, `tar' stops reading when it encounters a block of zeros
 between file entries (which usually indicates the end of the archive).
 `--ignore-zeros' (`-i') allows `tar' to completely read an archive
 which contains a block of zeros before the end (i.e. a damaged archive,
 or one which was created by concatenating several archives together).

I concluded that unless some spkgs are created by concatenating several tar archives together this option can be safely removed.

If there is a consensus to keep the option, I could always make a new patch 

Issue created by migration from https://trac.sagemath.org/ticket/4049





---

archive/issue_comments_029137.json:
```json
{
    "body": "About the new patch, I meant a new patch that only removes the option on systems where it is not supported.",
    "created_at": "2008-09-03T18:03:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4049#issuecomment-29137",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```

About the new patch, I meant a new patch that only removes the option on systems where it is not supported.



---

archive/issue_events_009249.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-03T18:10:25Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4049",
    "milestone": "sage-3.1.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4049#event-9249"
}
```



---

archive/issue_comments_029138.json:
```json
{
    "body": "Changing assignee from cwitty to anakha.",
    "created_at": "2008-09-03T18:10:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4049#issuecomment-29138",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from cwitty to anakha.



---

archive/issue_comments_029139.json:
```json
{
    "body": "Attachment [trac_4049.patch](tarball://root/attachments/some-uuid/ticket4049/trac_4049.patch) by mabshoff created at 2008-09-03 18:10:25\n\nPatch looks good to me. Positive review.\n\nOne general problem with Sage is that we depend on gnumake and gtar in a couple places. The shell scripts we use also assume GNUisms in a couple places, but I would be more than happy to get those wiped out.\n\nFor now I would suggest copying gmake into $SAGE_LOCAL/bin and rename it make. You should also treat gld and gas the same way for now.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-03T18:10:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4049#issuecomment-29139",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_4049.patch](tarball://root/attachments/some-uuid/ticket4049/trac_4049.patch) by mabshoff created at 2008-09-03 18:10:25

Patch looks good to me. Positive review.

One general problem with Sage is that we depend on gnumake and gtar in a couple places. The shell scripts we use also assume GNUisms in a couple places, but I would be more than happy to get those wiped out.

For now I would suggest copying gmake into $SAGE_LOCAL/bin and rename it make. You should also treat gld and gas the same way for now.

Cheers,

Michael



---

archive/issue_comments_029140.json:
```json
{
    "body": "Until now, the regular make has not given me any errors.  I had to install bash though.  I will try to use the native system binaries as much as possible and only revert to the gnu ones if it fails too much.\n\nOtherwise, expect more reports like this one to remove GNUisms where it makes sense.",
    "created_at": "2008-09-03T18:21:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4049#issuecomment-29140",
    "user": "https://trac.sagemath.org/admin/accounts/users/anakha"
}
```

Until now, the regular make has not given me any errors.  I had to install bash though.  I will try to use the native system binaries as much as possible and only revert to the gnu ones if it fails too much.

Otherwise, expect more reports like this one to remove GNUisms where it makes sense.



---

archive/issue_comments_029141.json:
```json
{
    "body": "Replying to [comment:3 anakha]:\n> Until now, the regular make has not given me any errors.  I had to install bash though.  I will try to use the native system binaries as much as possible and only revert to the gnu ones if it fails too much.\n> \n> Otherwise, expect more reports like this one to remove GNUisms where it makes sense.\n\nfreetype and eclib for now require gmake. We use bash for now and do not really plan to switch to a pure sh env since sh on Solaris is pretty broken. At least on FreeBSD the default location of bash is in /usr/local/bin and all shebangs of the scripts should not hard code the /bin/bash location.\n\nWe should continue this discussion on sage-devel though :)\n\nCheers,\n\nMichael",
    "created_at": "2008-09-03T18:26:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4049#issuecomment-29141",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:3 anakha]:
> Until now, the regular make has not given me any errors.  I had to install bash though.  I will try to use the native system binaries as much as possible and only revert to the gnu ones if it fails too much.
> 
> Otherwise, expect more reports like this one to remove GNUisms where it makes sense.

freetype and eclib for now require gmake. We use bash for now and do not really plan to switch to a pure sh env since sh on Solaris is pretty broken. At least on FreeBSD the default location of bash is in /usr/local/bin and all shebangs of the scripts should not hard code the /bin/bash location.

We should continue this discussion on sage-devel though :)

Cheers,

Michael



---

archive/issue_events_009250.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-04T00:31:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4049",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4049#event-9250"
}
```



---

archive/issue_comments_029142.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc0 - and I merged the patch into both repos, i.e. spkg/base, too.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-04T00:31:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4049#issuecomment-29142",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.rc0 - and I merged the patch into both repos, i.e. spkg/base, too.

Cheers,

Michael



---

archive/issue_comments_029143.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-04T00:31:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4049",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4049#issuecomment-29143",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
