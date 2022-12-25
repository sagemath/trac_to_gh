# Issue 6757: libgcrypt in Sage is GPL 3

archive/issues_006757.json:
```json
{
    "body": "Assignee: somebody\n\nSage has libgcrypt version 1.4.3 in spkg/standard.\n\nBut:\n\nhttp://directory.fsf.org/project/libgcrypt/\n\nclearly shows:\n\n1.4.3\n\n* Released: 21 Nov, 2008\n* Code Maturity: Stable\n* Source Archive: http://www.gnupg.org/download/index.en.html#lib...\n* Licenses: GPLv3\n* Interfaces: Command Line\n\nThe file SPKG.txt says:\n\n## License\n\n* LGPL V2.1 or later (1.4 release)\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6757\n\n",
    "created_at": "2009-08-16T03:42:29Z",
    "labels": [
        "component: cryptography",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "libgcrypt in Sage is GPL 3",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6757",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: somebody

Sage has libgcrypt version 1.4.3 in spkg/standard.

But:

http://directory.fsf.org/project/libgcrypt/

clearly shows:

1.4.3

* Released: 21 Nov, 2008
* Code Maturity: Stable
* Source Archive: http://www.gnupg.org/download/index.en.html#lib...
* Licenses: GPLv3
* Interfaces: Command Line

The file SPKG.txt says:

## License

* LGPL V2.1 or later (1.4 release)


Issue created by migration from https://trac.sagemath.org/ticket/6757





---

archive/issue_comments_055525.json:
```json
{
    "body": "See also http://trac.sagemath.org/sage_trac/ticket/1627\nWhen I download libcrypt-1.4.4 from http://www.gnupg.org/download/index.en.html#libgcrypt\nthe COPYING file indicates GPLv2 and the COPYING.LIB file indicates LGPLv2.1.\n\nI don't see 1.4.3 there.",
    "created_at": "2009-08-16T10:33:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6757",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6757#issuecomment-55525",
    "user": "https://github.com/wdjoyner"
}
```

See also http://trac.sagemath.org/sage_trac/ticket/1627
When I download libcrypt-1.4.4 from http://www.gnupg.org/download/index.en.html#libgcrypt
the COPYING file indicates GPLv2 and the COPYING.LIB file indicates LGPLv2.1.

I don't see 1.4.3 there.



---

archive/issue_comments_055526.json:
```json
{
    "body": "The name of the .spkg file in Sage 4.1.1 is libgcrypt-1.4.3.p1.spkg I've made a libgcrypt-1.4.3.p2.spkg\n\n\n```\n\ndrkirkby@smudge:[~/sage/suncc/sage-4.1.1/spkg/standard] $ ls -ld libgcrypt* \n-rw-r--r--   1 drkirkby other    2036701 Jul 31 22:45 libgcrypt-1.4.3.p1.spkg\n-rw-r--r--   1 drkirkby other    2115840 Aug 16 12:34 libgcrypt-1.4.3.p2.spkg\ndrkirkby@smudge:[~/sage/suncc/sage-4.1.1/spkg/standard] $ pwd\n/export/home/drkirkby/sage/suncc/sage-4.1.1/spkg/standard\ndrkirkby@smudge:[~/sage/suncc/sage-4.1.1/spkg/standard] $\n\n\n```\n",
    "created_at": "2009-08-16T12:29:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6757",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6757#issuecomment-55526",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

The name of the .spkg file in Sage 4.1.1 is libgcrypt-1.4.3.p1.spkg I've made a libgcrypt-1.4.3.p2.spkg


```

drkirkby@smudge:[~/sage/suncc/sage-4.1.1/spkg/standard] $ ls -ld libgcrypt* 
-rw-r--r--   1 drkirkby other    2036701 Jul 31 22:45 libgcrypt-1.4.3.p1.spkg
-rw-r--r--   1 drkirkby other    2115840 Aug 16 12:34 libgcrypt-1.4.3.p2.spkg
drkirkby@smudge:[~/sage/suncc/sage-4.1.1/spkg/standard] $ pwd
/export/home/drkirkby/sage/suncc/sage-4.1.1/spkg/standard
drkirkby@smudge:[~/sage/suncc/sage-4.1.1/spkg/standard] $


```




---

archive/issue_comments_055527.json:
```json
{
    "body": "I guess we should go by the COPYING file. The website and the actual code disagree. I assume the code is more authorative. \n\nI suspect this should be closed in that case.",
    "created_at": "2009-09-15T21:32:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6757",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6757#issuecomment-55527",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I guess we should go by the COPYING file. The website and the actual code disagree. I assume the code is more authorative. 

I suspect this should be closed in that case.



---

archive/issue_events_006987.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-28T01:34:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6757",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6757#event-6987"
}
```



---

archive/issue_comments_055528.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-09-28T01:34:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6757",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6757#issuecomment-55528",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: invalid



---

archive/issue_comments_055529.json:
```json
{
    "body": "I think the file COPYING in the source tarball is the authority here. So close this ticket as invalid.",
    "created_at": "2009-09-28T01:34:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6757",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6757#issuecomment-55529",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

I think the file COPYING in the source tarball is the authority here. So close this ticket as invalid.
