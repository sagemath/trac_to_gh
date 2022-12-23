# Issue 8066: New libgpg_error-1.6.p3.spkg works with Open Solaris 64 bit

archive/issues_008066.json:
```json
{
    "body": "Assignee: drkirkby\n\nMade the package work with Open Solaris 64 bit SAGE64=\"yes\"\n\nThe package is here:\n[http://boxen.math.washington.edu/home/jsp/ports/libgpg_error-1.6.p3.spkg](http://boxen.math.washington.edu/home/jsp/ports/libgpg_error-1.6.p3.spkg)\n\nJaap\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8066\n\n",
    "created_at": "2010-01-25T22:45:18Z",
    "labels": [
        "porting",
        "major",
        "enhancement"
    ],
    "title": "New libgpg_error-1.6.p3.spkg works with Open Solaris 64 bit",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8066",
    "user": "jsp"
}
```
Assignee: drkirkby

Made the package work with Open Solaris 64 bit SAGE64="yes"

The package is here:
[http://boxen.math.washington.edu/home/jsp/ports/libgpg_error-1.6.p3.spkg](http://boxen.math.washington.edu/home/jsp/ports/libgpg_error-1.6.p3.spkg)

Jaap



Issue created by migration from https://trac.sagemath.org/ticket/8066





---

archive/issue_comments_070685.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-25T22:45:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8066#issuecomment-70685",
    "user": "jsp"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070686.json:
```json
{
    "body": "Attachment\n\nThis package was building 64-bit before, so it's not entirely clear this is 100% necessary. But I agree it is desirable. It should make it more reliable. \n\nBut it is echoing 'Mac Intel' which is incorrect. \n\nDave",
    "created_at": "2010-01-27T13:19:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8066#issuecomment-70686",
    "user": "drkirkby"
}
```

Attachment

This package was building 64-bit before, so it's not entirely clear this is 100% necessary. But I agree it is desirable. It should make it more reliable. 

But it is echoing 'Mac Intel' which is incorrect. 

Dave



---

archive/issue_comments_070687.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-27T13:19:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8066#issuecomment-70687",
    "user": "drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_070688.json:
```json
{
    "body": "I would also put the ticket number you are fixing in SPKG.txt. You should create the ticket for the defect first. Then you have a ticket number which can be put in SPKG.txt.",
    "created_at": "2010-01-27T13:34:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8066#issuecomment-70688",
    "user": "drkirkby"
}
```

I would also put the ticket number you are fixing in SPKG.txt. You should create the ticket for the defect first. Then you have a ticket number which can be put in SPKG.txt.



---

archive/issue_comments_070689.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-01-27T13:37:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8066#issuecomment-70689",
    "user": "jsp"
}
```

Attachment



---

archive/issue_comments_070690.json:
```json
{
    "body": "Done. Didn't raise the patch level.\n\n\n[http://boxen.math.washington.edu/home/jsp/ports/libgpg_error-1.6.p3.spkg](http://boxen.math.washington.edu/home/jsp/ports/libgpg_error-1.6.p3.spkg)\n\n\nJaap",
    "created_at": "2010-01-27T13:42:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8066#issuecomment-70690",
    "user": "jsp"
}
```

Done. Didn't raise the patch level.


[http://boxen.math.washington.edu/home/jsp/ports/libgpg_error-1.6.p3.spkg](http://boxen.math.washington.edu/home/jsp/ports/libgpg_error-1.6.p3.spkg)


Jaap



---

archive/issue_comments_070691.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-27T13:42:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8066#issuecomment-70691",
    "user": "jsp"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_070692.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-27T14:12:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8066#issuecomment-70692",
    "user": "drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070693.json:
```json
{
    "body": "It would have been wiser to overwrite the patch file in this case I think. \n\n\n```\ndrkirkby@hawk:~/sage-4.3.1$ file local/lib/libgpg-error*\nlocal/lib/libgpg-error.a:\tcurrent ar archive, not a dynamic executable or shared object\nlocal/lib/libgpg-error.la:\tcommands text\nlocal/lib/libgpg-error.so:\tELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped\nlocal/lib/libgpg-error.so.0:\tELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped\nlocal/lib/libgpg-error.so.0.4.0:\tELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped\n```\n\n\nLibraries are building 64-bit, so positive review. \n\nIt's probably worth showing the output of the 'file' command, to show the libraries, or executables are building 64-bit. I must admit I've rarely if ever done that, but it will show that the problem is fixed, as not all packages are building properly, even with the -m64 flag added. \n\nDave",
    "created_at": "2010-01-27T14:12:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8066#issuecomment-70693",
    "user": "drkirkby"
}
```

It would have been wiser to overwrite the patch file in this case I think. 


```
drkirkby@hawk:~/sage-4.3.1$ file local/lib/libgpg-error*
local/lib/libgpg-error.a:	current ar archive, not a dynamic executable or shared object
local/lib/libgpg-error.la:	commands text
local/lib/libgpg-error.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
local/lib/libgpg-error.so.0:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
local/lib/libgpg-error.so.0.4.0:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
```


Libraries are building 64-bit, so positive review. 

It's probably worth showing the output of the 'file' command, to show the libraries, or executables are building 64-bit. I must admit I've rarely if ever done that, but it will show that the problem is fixed, as not all packages are building properly, even with the -m64 flag added. 

Dave



---

archive/issue_comments_070694.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T15:17:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8066#issuecomment-70694",
    "user": "mpatel"
}
```

Resolution: fixed
