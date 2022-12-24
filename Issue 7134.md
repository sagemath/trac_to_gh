# Issue 7134: ntl 5.4.2.p9 always builds 32-bit libraries on Solaris.

archive/issues_007134.json:
```json
{
    "body": "Assignee: tbd\n\nsing\n\n* A Sun Blade 2000 running Solaris 10 update 7\n* Sage 4.1.2.rc0\n* gcc 4.4.1\n* SAGE64 exported to \"yes\" \n\nWe can see that *ntl* is building 32-bit libraries, despite the fact SAGE64 was set to \"yes\"\n\n```\ndrkirkby@swan:[~/sage/gcc64-sage-4.1.2.rc0/local/lib] $ file *ntl*\nlibntl-5.4.2.so:        ELF 32-bit MSB dynamic lib SPARC32PLUS Version 1, V8+ Required, dynamically linked, not stripped\nlibntl.a:       current ar archive, not a dynamic executable or shared object\nlibntl.so:      ELF 32-bit MSB dynamic lib SPARC32PLUS Version 1, V8+ Required, dynamically linked, not stripped\ndrkirkby@swan:[~/sage/gcc64-sage-4.1.2.rc0/local/lib] $\n```\n\n\n\nOther packages building 32-bit libraries, even when SAGE64 is set to \"yes\" include, but are probably not limited to:\n\n* zlib #7128\n* libgpg_error #7129\n* libpng #7130\n* libcliquer #7131 \n* pari #7133\n\nmpir currently mixes 32 and 64-bit objects, so do not build at all #7132.\n\nI will sort this package out after creating a new sage-env, which exports all the variables properly, including the flag for building 64-bit code, which is not always -m64.\n\nAlthough there is no support for AIX or HP-UX in Sage yet, we could potentially add it - I personally own machines running AIX and HP-UX.\n\nIBM's compiler on AIX uses -q64, and HP's on HP-UX uses +DD64.\n\nThe sensible way to resolve this is to add the correct flag on every platform.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7134\n\n",
    "created_at": "2009-10-06T00:32:47Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "ntl 5.4.2.p9 always builds 32-bit libraries on Solaris.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7134",
    "user": "drkirkby"
}
```
Assignee: tbd

sing

* A Sun Blade 2000 running Solaris 10 update 7
* Sage 4.1.2.rc0
* gcc 4.4.1
* SAGE64 exported to "yes" 

We can see that *ntl* is building 32-bit libraries, despite the fact SAGE64 was set to "yes"

```
drkirkby@swan:[~/sage/gcc64-sage-4.1.2.rc0/local/lib] $ file *ntl*
libntl-5.4.2.so:        ELF 32-bit MSB dynamic lib SPARC32PLUS Version 1, V8+ Required, dynamically linked, not stripped
libntl.a:       current ar archive, not a dynamic executable or shared object
libntl.so:      ELF 32-bit MSB dynamic lib SPARC32PLUS Version 1, V8+ Required, dynamically linked, not stripped
drkirkby@swan:[~/sage/gcc64-sage-4.1.2.rc0/local/lib] $
```



Other packages building 32-bit libraries, even when SAGE64 is set to "yes" include, but are probably not limited to:

* zlib #7128
* libgpg_error #7129
* libpng #7130
* libcliquer #7131 
* pari #7133

mpir currently mixes 32 and 64-bit objects, so do not build at all #7132.

I will sort this package out after creating a new sage-env, which exports all the variables properly, including the flag for building 64-bit code, which is not always -m64.

Although there is no support for AIX or HP-UX in Sage yet, we could potentially add it - I personally own machines running AIX and HP-UX.

IBM's compiler on AIX uses -q64, and HP's on HP-UX uses +DD64.

The sensible way to resolve this is to add the correct flag on every platform.

Issue created by migration from https://trac.sagemath.org/ticket/7134





---

archive/issue_comments_059151.json:
```json
{
    "body": "Changing component from algebra to solaris.",
    "created_at": "2009-10-06T00:33:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7134#issuecomment-59151",
    "user": "drkirkby"
}
```

Changing component from algebra to solaris.



---

archive/issue_comments_059152.json:
```json
{
    "body": "This can be closed as fixed, as the issue was resolved in sage-4.3.3.alpha0 #8101. \n\nDave",
    "created_at": "2011-04-02T13:15:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7134#issuecomment-59152",
    "user": "drkirkby"
}
```

This can be closed as fixed, as the issue was resolved in sage-4.3.3.alpha0 #8101. 

Dave



---

archive/issue_comments_059153.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-04-05T15:51:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7134",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7134#issuecomment-59153",
    "user": "@jdemeyer"
}
```

Resolution: duplicate
