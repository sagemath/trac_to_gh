# Issue 8062: New givaro-3.2.13rc2.p0.spkg works with Open Solaris 64 bit, SAGE64="yes"

archive/issues_008062.json:
```json
{
    "body": "Assignee: drkirkby\n\nLet spkg-install work with SAGE64=\"yes\" on Open Solaris.\n\n[http://boxen.math.washington.edu/home/jsp/ports/givaro-3.2.13rc2.p0.spkg](http://boxen.math.washington.edu/home/jsp/ports/givaro-3.2.13rc2.p0.spkg)\n\nJaap\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8062\n\n",
    "created_at": "2010-01-25T21:23:19Z",
    "labels": [
        "porting",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "New givaro-3.2.13rc2.p0.spkg works with Open Solaris 64 bit, SAGE64=\"yes\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8062",
    "user": "jsp"
}
```
Assignee: drkirkby

Let spkg-install work with SAGE64="yes" on Open Solaris.

[http://boxen.math.washington.edu/home/jsp/ports/givaro-3.2.13rc2.p0.spkg](http://boxen.math.washington.edu/home/jsp/ports/givaro-3.2.13rc2.p0.spkg)

Jaap



Issue created by migration from https://trac.sagemath.org/ticket/8062





---

archive/issue_comments_070662.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-25T21:23:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8062#issuecomment-70662",
    "user": "jsp"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070663.json:
```json
{
    "body": "Attachment [givaro-3.2.13rc2.p0,patch](tarball://root/attachments/some-uuid/ticket8062/givaro-3.2.13rc2.p0,patch) by jsp created at 2010-01-26 20:54:56",
    "created_at": "2010-01-26T20:54:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8062#issuecomment-70663",
    "user": "jsp"
}
```

Attachment [givaro-3.2.13rc2.p0,patch](tarball://root/attachments/some-uuid/ticket8062/givaro-3.2.13rc2.p0,patch) by jsp created at 2010-01-26 20:54:56



---

archive/issue_comments_070664.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-28T08:44:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8062#issuecomment-70664",
    "user": "drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_070665.json:
```json
{
    "body": "Attachment [givaro-3.2.13rc2.p0.patch](tarball://root/attachments/some-uuid/ticket8062/givaro-3.2.13rc2.p0.patch) by drkirkby created at 2010-01-28 08:44:40\n\nThe comment in SPKG.txt is inaccurate, as the patch is not specific to Open Solaris. \n\n\nA more accurate comment would be. \n\nEnsures the compiler flag -m64 is added when the environment variable SAGE64 was set to yes - previously this was only happening on OS X. This should aid building 64-bit on any platform, though it has only been tested on Open Solaris. \n\nAlso, add the trac ticket number #8062 to the comment. \n\nIt's far better to open a ticket for the bug first, before trying to fix it. Then the ticket number can be placed in the comments in SPKG.txt. \n\nYou might want to remove Martin Albrecht as a maintainer, as his name is duplicated.",
    "created_at": "2010-01-28T08:44:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8062#issuecomment-70665",
    "user": "drkirkby"
}
```

Attachment [givaro-3.2.13rc2.p0.patch](tarball://root/attachments/some-uuid/ticket8062/givaro-3.2.13rc2.p0.patch) by drkirkby created at 2010-01-28 08:44:40

The comment in SPKG.txt is inaccurate, as the patch is not specific to Open Solaris. 


A more accurate comment would be. 

Ensures the compiler flag -m64 is added when the environment variable SAGE64 was set to yes - previously this was only happening on OS X. This should aid building 64-bit on any platform, though it has only been tested on Open Solaris. 

Also, add the trac ticket number #8062 to the comment. 

It's far better to open a ticket for the bug first, before trying to fix it. Then the ticket number can be placed in the comments in SPKG.txt. 

You might want to remove Martin Albrecht as a maintainer, as his name is duplicated.



---

archive/issue_comments_070666.json:
```json
{
    "body": "Replying to [comment:2 drkirkby]:\n> The comment in SPKG.txt is inaccurate, as the patch is not specific to Open Solaris. \n> \n> \n> A more accurate comment would be. \n> \n> Ensures the compiler flag -m64 is added when the environment variable SAGE64 was set to yes - previously this was only happening on OS X. This should aid building 64-bit on any platform, though it has only been tested on Open Solaris. \n>\n\nThat maybe better, but rather long for a short comment.\n \n> Also, add the trac ticket number #8062 to the comment. \n> \n> It's far better to open a ticket for the bug first, before trying to fix it. Then the ticket number can be placed in the comments in SPKG.txt. \n>\n\nSure that is a possibility. I've seen a lot of SPKG.txt files without trac numbers.\n\n> You might want to remove Martin Albrecht as a maintainer, as his name is duplicated. \n\nThat is what I did. As you can see in the patch.\n\nJaap",
    "created_at": "2010-01-28T11:42:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8062#issuecomment-70666",
    "user": "jsp"
}
```

Replying to [comment:2 drkirkby]:
> The comment in SPKG.txt is inaccurate, as the patch is not specific to Open Solaris. 
> 
> 
> A more accurate comment would be. 
> 
> Ensures the compiler flag -m64 is added when the environment variable SAGE64 was set to yes - previously this was only happening on OS X. This should aid building 64-bit on any platform, though it has only been tested on Open Solaris. 
>

That maybe better, but rather long for a short comment.
 
> Also, add the trac ticket number #8062 to the comment. 
> 
> It's far better to open a ticket for the bug first, before trying to fix it. Then the ticket number can be placed in the comments in SPKG.txt. 
>

Sure that is a possibility. I've seen a lot of SPKG.txt files without trac numbers.

> You might want to remove Martin Albrecht as a maintainer, as his name is duplicated. 

That is what I did. As you can see in the patch.

Jaap



---

archive/issue_comments_070667.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-28T13:11:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8062#issuecomment-70667",
    "user": "jsp"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_070668.json:
```json
{
    "body": "Attachment [givaro-3.2.13rc2.p0+.patch](tarball://root/attachments/some-uuid/ticket8062/givaro-3.2.13rc2.p0+.patch) by jsp created at 2010-01-28 13:11:48\n\nUpdated SPKG.txt\n\nLeft patch level p0.\n\nLink is still\n[http://boxen.math.washington.edu/home/jsp/ports/givaro-3.2.13rc2.p0.spkg](http://boxen.math.washington.edu/home/jsp/ports/givaro-3.2.13rc2.p0.spkg)\n\n\nJaap",
    "created_at": "2010-01-28T13:11:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8062#issuecomment-70668",
    "user": "jsp"
}
```

Attachment [givaro-3.2.13rc2.p0+.patch](tarball://root/attachments/some-uuid/ticket8062/givaro-3.2.13rc2.p0+.patch) by jsp created at 2010-01-28 13:11:48

Updated SPKG.txt

Left patch level p0.

Link is still
[http://boxen.math.washington.edu/home/jsp/ports/givaro-3.2.13rc2.p0.spkg](http://boxen.math.washington.edu/home/jsp/ports/givaro-3.2.13rc2.p0.spkg)


Jaap



---

archive/issue_comments_070669.json:
```json
{
    "body": "Positive review. All dynamic libraries are 64-bit. I don't know how one can determine this with static libraries, as 'ldd' does not indicate anything about them. But I assume they are probably ok\n\n\n```\ndrkirkby@hawk:~/sage-4.3.1$ file local/lib/libgivaro*\nlocal/lib/libgivaro.a:\tcurrent ar archive, not a dynamic executable or shared object\nlocal/lib/libgivaro.la:\tcommands text\nlocal/lib/libgivaro.so:\tELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped\nlocal/lib/libgivaro.so.0:\tELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped\nlocal/lib/libgivaro.so.0.0.2:\tELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped\n```\n\n\nIt would be worth trying to find out a way of confirming the exact type of static libraries, but I think the fact the shared libraries are ok, this patch is fine. \n\nDave",
    "created_at": "2010-01-28T13:39:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8062#issuecomment-70669",
    "user": "drkirkby"
}
```

Positive review. All dynamic libraries are 64-bit. I don't know how one can determine this with static libraries, as 'ldd' does not indicate anything about them. But I assume they are probably ok


```
drkirkby@hawk:~/sage-4.3.1$ file local/lib/libgivaro*
local/lib/libgivaro.a:	current ar archive, not a dynamic executable or shared object
local/lib/libgivaro.la:	commands text
local/lib/libgivaro.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
local/lib/libgivaro.so.0:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
local/lib/libgivaro.so.0.0.2:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
```


It would be worth trying to find out a way of confirming the exact type of static libraries, but I think the fact the shared libraries are ok, this patch is fine. 

Dave



---

archive/issue_comments_070670.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-28T13:39:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8062#issuecomment-70670",
    "user": "drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070671.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T15:16:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8062",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8062#issuecomment-70671",
    "user": "mpatel"
}
```

Resolution: fixed
