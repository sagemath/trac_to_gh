# Issue 8787: upgrade the openssl optional spkg to version 1.0

archive/issues_008787.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  schilly\n\nAmazingly, openssl released version *1.0*! Let's upgrade to this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8787\n\n",
    "created_at": "2010-04-27T23:02:19Z",
    "labels": [
        "packages: optional",
        "major",
        "enhancement"
    ],
    "title": "upgrade the openssl optional spkg to version 1.0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8787",
    "user": "was"
}
```
Assignee: tbd

CC:  schilly

Amazingly, openssl released version *1.0*! Let's upgrade to this.

Issue created by migration from https://trac.sagemath.org/ticket/8787





---

archive/issue_comments_080454.json:
```json
{
    "body": "Here is the spkg:\n\nhttp://wstein.org/home/wstein/patches/openssl-1.0.0.spkg\n\nI fixed things to be \"modern\" and up to snuff -- a formatted SPKG.txt file, a .hg directory, error messages not all messed up in spkg-install, a src/ directory, etc.",
    "created_at": "2010-04-27T23:14:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8787#issuecomment-80454",
    "user": "was"
}
```

Here is the spkg:

http://wstein.org/home/wstein/patches/openssl-1.0.0.spkg

I fixed things to be "modern" and up to snuff -- a formatted SPKG.txt file, a .hg directory, error messages not all messed up in spkg-install, a src/ directory, etc.



---

archive/issue_comments_080455.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-27T23:14:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8787#issuecomment-80455",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080456.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-05T15:32:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8787#issuecomment-80456",
    "user": "mariah"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_080457.json:
```json
{
    "body": "Sadly, building sage-4.3.5 with gcc-4.4.3 and openssl-1.0.0.spkg \ndid NOT work on one of my company's computers (not connected to\nthe Internet).  The machine is similar hardware to Skynet/taurus, \nbut running Red Hat Enterprise Linux Server.\n\nFirst I installed openssl-1.0.0.spkg.  Then I did 'make testlong'.\nThe build failed while trying to build python-2.6.4.p7 with the\nmessage\n  \n  import _md5\nImport Error: No module named _md5\nhashlib module failed to import",
    "created_at": "2010-05-05T15:32:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8787#issuecomment-80457",
    "user": "mariah"
}
```

Sadly, building sage-4.3.5 with gcc-4.4.3 and openssl-1.0.0.spkg 
did NOT work on one of my company's computers (not connected to
the Internet).  The machine is similar hardware to Skynet/taurus, 
but running Red Hat Enterprise Linux Server.

First I installed openssl-1.0.0.spkg.  Then I did 'make testlong'.
The build failed while trying to build python-2.6.4.p7 with the
message
  
  import _md5
Import Error: No module named _md5
hashlib module failed to import



---

archive/issue_comments_080458.json:
```json
{
    "body": "Replying to [comment:3 mariah]:\n> Sadly, building sage-4.3.5 with gcc-4.4.3 and openssl-1.0.0.spkg \n> did NOT work on one of my company's computers (not connected to\n> the Internet).  The machine is similar hardware to Skynet/taurus, \n> but running Red Hat Enterprise Linux Server.\n> \n> First I installed openssl-1.0.0.spkg.  Then I did 'make testlong'.\n> The build failed while trying to build python-2.6.4.p7 with the\n> message\n\nCan you post the log that results from doing\n\n  sage -f openssl-1.0.0\n\nand also the log that results from building python, e.g.,\n\n  sage -f python-2.6.4.p7\n\n\nAlso, did you get this failure on taurus?  If so, I can just test there.",
    "created_at": "2010-05-05T15:42:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8787#issuecomment-80458",
    "user": "was"
}
```

Replying to [comment:3 mariah]:
> Sadly, building sage-4.3.5 with gcc-4.4.3 and openssl-1.0.0.spkg 
> did NOT work on one of my company's computers (not connected to
> the Internet).  The machine is similar hardware to Skynet/taurus, 
> but running Red Hat Enterprise Linux Server.
> 
> First I installed openssl-1.0.0.spkg.  Then I did 'make testlong'.
> The build failed while trying to build python-2.6.4.p7 with the
> message

Can you post the log that results from doing

  sage -f openssl-1.0.0

and also the log that results from building python, e.g.,

  sage -f python-2.6.4.p7


Also, did you get this failure on taurus?  If so, I can just test there.



---

archive/issue_comments_080459.json:
```json
{
    "body": "> Can you post the log that results from doing\n> \n>   sage -f openssl-1.0.0\n> \n> and also the log that results from building python, e.g.,\n> \n>   sage -f python-2.6.4.p7\n\nI do not believe I am allowed to export the logs.\nThis problem is happening on one of our internal \ncompany machines.\n\n> Also, did you get this failure on taurus?  If so, I can just test there.\n\nI tried to reproduce the problem on taurus, but sadly the \nproblem does NOT seem to be reproducible on taurus.",
    "created_at": "2010-05-05T15:56:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8787#issuecomment-80459",
    "user": "mariah"
}
```

> Can you post the log that results from doing
> 
>   sage -f openssl-1.0.0
> 
> and also the log that results from building python, e.g.,
> 
>   sage -f python-2.6.4.p7

I do not believe I am allowed to export the logs.
This problem is happening on one of our internal 
company machines.

> Also, did you get this failure on taurus?  If so, I can just test there.

I tried to reproduce the problem on taurus, but sadly the 
problem does NOT seem to be reproducible on taurus.



---

archive/issue_comments_080460.json:
```json
{
    "body": "\n```\nI have investigated the problem and found that \nthe reason for the failure is that openssl-1.0.0\nputs libraries in $SAGE_ROOT/local/lib64 on 64-bit \nmachines. Sage does not add $SAGE_ROOT/local/lib64\nto the LD_LIBRARY_PATH.\n\nIf you add\n\n  --libdir=lib\n\nto the ./config line in spkg-install, then sage\nbuilds with openssl-1.0.0 and all tests pass.\n```\n",
    "created_at": "2010-05-27T14:23:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8787#issuecomment-80460",
    "user": "mariah"
}
```


```
I have investigated the problem and found that 
the reason for the failure is that openssl-1.0.0
puts libraries in $SAGE_ROOT/local/lib64 on 64-bit 
machines. Sage does not add $SAGE_ROOT/local/lib64
to the LD_LIBRARY_PATH.

If you add

  --libdir=lib

to the ./config line in spkg-install, then sage
builds with openssl-1.0.0 and all tests pass.
```




---

archive/issue_comments_080461.json:
```json
{
    "body": "I've posted a new spkg with the fix you suggest here:\n\n   http://wstein.org/home/wstein/patches/openssl-1.0.0.p0.spkg",
    "created_at": "2010-06-04T05:29:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8787#issuecomment-80461",
    "user": "was"
}
```

I've posted a new spkg with the fix you suggest here:

   http://wstein.org/home/wstein/patches/openssl-1.0.0.p0.spkg



---

archive/issue_comments_080462.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-06-04T05:29:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8787#issuecomment-80462",
    "user": "was"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_080463.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-09T14:23:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8787#issuecomment-80463",
    "user": "mariah"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080464.json:
```json
{
    "body": "On the machine where I previously was having problems, \nopenssl-1.0.0.p0.spkg builds and 'make testlong' on\nsage-4.4.3 passes all tests.\n\nThus I give this package a positive review!",
    "created_at": "2010-06-09T14:23:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8787#issuecomment-80464",
    "user": "mariah"
}
```

On the machine where I previously was having problems, 
openssl-1.0.0.p0.spkg builds and 'make testlong' on
sage-4.4.3 passes all tests.

Thus I give this package a positive review!



---

archive/issue_comments_080465.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-08T18:57:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8787",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8787#issuecomment-80465",
    "user": "rlm"
}
```

Resolution: fixed
