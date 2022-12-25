# Issue 8070: New  pycrypto-2.0.1.p5.spkg works with Open Solaris 64 bit

archive/issues_008070.json:
```json
{
    "body": "Assignee: drkirkby\n\nLet SAGE64=\"yes\" work with Open Solaris 64 bit too.\n\nThe spkg is here:\n[http://boxen.math.washington.edu/home/jsp/ports/pycrypto-2.0.1.p5.spkg](http://boxen.math.washington.edu/home/jsp/ports/pycrypto-2.0.1.p5.spkg)\n\n\n\n```\nbyte-compiling /export/home/jaap/Downloads/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/__init__.py to __init__.pyc\nrunning install_egg_info\nWriting /export/home/jaap/Downloads/sage-4.3.1/local/lib/python2.6/site-packages/pycrypto-2.0.1-py2.6.egg-info\n\nreal\t0m5.851s\nuser\t0m4.285s\nsys\t0m0.920s\nSuccessfully installed pycrypto-2.0.1.p5\nYou can safely delete the temporary build directory\n/export/home/jaap/Downloads/sage-4.3.1/spkg/build/pycrypto-2.0.1.p5\nMaking Sage/Python scripts relocatable...\nMaking script relocatable\nFinished installing pycrypto-2.0.1.p5.spkg\njaap@opensolaris:~/Downloads/sage-4.3.1$ \n\n```\n\n\n\nJaap\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8070\n\n",
    "created_at": "2010-01-26T00:27:10Z",
    "labels": [
        "component: porting"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "New  pycrypto-2.0.1.p5.spkg works with Open Solaris 64 bit",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8070",
    "user": "https://github.com/jaapspies"
}
```
Assignee: drkirkby

Let SAGE64="yes" work with Open Solaris 64 bit too.

The spkg is here:
[http://boxen.math.washington.edu/home/jsp/ports/pycrypto-2.0.1.p5.spkg](http://boxen.math.washington.edu/home/jsp/ports/pycrypto-2.0.1.p5.spkg)



```
byte-compiling /export/home/jaap/Downloads/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/__init__.py to __init__.pyc
running install_egg_info
Writing /export/home/jaap/Downloads/sage-4.3.1/local/lib/python2.6/site-packages/pycrypto-2.0.1-py2.6.egg-info

real	0m5.851s
user	0m4.285s
sys	0m0.920s
Successfully installed pycrypto-2.0.1.p5
You can safely delete the temporary build directory
/export/home/jaap/Downloads/sage-4.3.1/spkg/build/pycrypto-2.0.1.p5
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing pycrypto-2.0.1.p5.spkg
jaap@opensolaris:~/Downloads/sage-4.3.1$ 

```



Jaap



Issue created by migration from https://trac.sagemath.org/ticket/8070





---

archive/issue_comments_070600.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-26T00:27:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8070#issuecomment-70600",
    "user": "https://github.com/jaapspies"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_070601.json:
```json
{
    "body": "Attachment [pycrypto-2.0.1.p5.patch](tarball://root/attachments/some-uuid/ticket8070/pycrypto-2.0.1.p5.patch) by @jaapspies created at 2010-01-26 19:00:17",
    "created_at": "2010-01-26T19:00:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8070#issuecomment-70601",
    "user": "https://github.com/jaapspies"
}
```

Attachment [pycrypto-2.0.1.p5.patch](tarball://root/attachments/some-uuid/ticket8070/pycrypto-2.0.1.p5.patch) by @jaapspies created at 2010-01-26 19:00:17



---

archive/issue_comments_070602.json:
```json
{
    "body": "It has 'echo \"64 bit MacIntel\" which is not correct.",
    "created_at": "2010-01-27T12:25:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8070#issuecomment-70602",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

It has 'echo "64 bit MacIntel" which is not correct.



---

archive/issue_comments_070603.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-27T12:25:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8070#issuecomment-70603",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_070604.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-27T14:07:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8070#issuecomment-70604",
    "user": "https://github.com/jaapspies"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_070605.json:
```json
{
    "body": "Attachment [pycrypto-2.0.1.p5+.patch](tarball://root/attachments/some-uuid/ticket8070/pycrypto-2.0.1.p5+.patch) by @jaapspies created at 2010-01-27 14:07:55\n\nDone.\n\nJaap",
    "created_at": "2010-01-27T14:07:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8070#issuecomment-70605",
    "user": "https://github.com/jaapspies"
}
```

Attachment [pycrypto-2.0.1.p5+.patch](tarball://root/attachments/some-uuid/ticket8070/pycrypto-2.0.1.p5+.patch) by @jaapspies created at 2010-01-27 14:07:55

Done.

Jaap



---

archive/issue_comments_070606.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-27T16:39:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8070#issuecomment-70606",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_070607.json:
```json
{
    "body": "That's fine. In future, it would be helpful if you could show evidence that the package is building ok, as \n\n\n```\nSuccessfully installed pycrypto-2.0.1.p5\n```\n\n\ndoes not prove very much. Plenty of packages claim to 'sucessfully' install in Open Solaris, yet in practice they do not. In this case, we can see:\n\n\n```\ncopying build/lib.solaris-2.11-i86pc-2.6/Crypto/Cipher/AES.so -> /export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher\ncopying build/lib.solaris-2.11-i86pc-2.6/Crypto/Cipher/DES3.so -> /export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher\ncopying build/lib.solaris-2.11-i86pc-2.6/Crypto/Cipher/DES.so -> /export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher\n```\n\n\nand using 'file' in the directory, I can indeed see the binaries are now 64-bit. \n\n\n```\ndrkirkby@hawk:~/sage-4.3.1$ file /export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/*\n/export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/AES.so:\tELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped\n/export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/ARC2.so:\tELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped\n/export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/ARC4.so:\tELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped\n/export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/Blowfish.so:\tELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped\n/export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/CAST.so:\tELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped\n/export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/DES3.so:\tELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped\n/export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/DES.so:\tELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped\n/export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/IDEA.so:\tELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped\n/export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/__init__.py:\tEnglish text\n/export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/__init__.pyc:\tdata\n/export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/RC5.so:\tELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped\n/export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/XOR.so:\tELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped\ndrkirkby@hawk:~/sage-4.3.1$ \n```\n\n\nSo a positive review from me. \n\nSorry to sometimes ask for extra things, but it is easier for the reviewer if he can see evidence this fixes the bug. As I've done many of these Solaris fixes, and see some from  you, I can see ways of improving some things. \n\nDave",
    "created_at": "2010-01-27T16:39:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8070#issuecomment-70607",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

That's fine. In future, it would be helpful if you could show evidence that the package is building ok, as 


```
Successfully installed pycrypto-2.0.1.p5
```


does not prove very much. Plenty of packages claim to 'sucessfully' install in Open Solaris, yet in practice they do not. In this case, we can see:


```
copying build/lib.solaris-2.11-i86pc-2.6/Crypto/Cipher/AES.so -> /export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher
copying build/lib.solaris-2.11-i86pc-2.6/Crypto/Cipher/DES3.so -> /export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher
copying build/lib.solaris-2.11-i86pc-2.6/Crypto/Cipher/DES.so -> /export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher
```


and using 'file' in the directory, I can indeed see the binaries are now 64-bit. 


```
drkirkby@hawk:~/sage-4.3.1$ file /export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/*
/export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/AES.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
/export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/ARC2.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
/export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/ARC4.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
/export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/Blowfish.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
/export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/CAST.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
/export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/DES3.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
/export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/DES.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
/export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/IDEA.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
/export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/__init__.py:	English text
/export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/__init__.pyc:	data
/export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/RC5.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
/export/home/drkirkby/sage-4.3.1/local/lib/python2.6/site-packages/Crypto/Cipher/XOR.so:	ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
drkirkby@hawk:~/sage-4.3.1$ 
```


So a positive review from me. 

Sorry to sometimes ask for extra things, but it is easier for the reviewer if he can see evidence this fixes the bug. As I've done many of these Solaris fixes, and see some from  you, I can see ways of improving some things. 

Dave



---

archive/issue_events_008278.json:
```json
{
    "actor": "@qed777",
    "created_at": "2010-02-11T15:17:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8070",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8070#event-8278"
}
```



---

archive/issue_comments_070608.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T15:17:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8070",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8070#issuecomment-70608",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
