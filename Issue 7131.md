# Issue 7131: libcliquer always builds 32-bit libraries on Solaris.

archive/issues_007131.json:
```json
{
    "body": "Assignee: tbd\n\nUsing\n\n* A Sun Blade 2000 running Solaris 10 update 7\n* Sage 4.1.2.rc0\n* gcc 4.4.1\n* SAGE64 exported to \"yes\" \n\nWe can see that libcliquer is building 32-bit libraries, despite other packages are building 64-bit libraries. \n\nlibcliquer.so:  ELF 32-bit MSB dynamic lib SPARC32PLUS Version 1, V8+ Required, dynamically linked, not stripped\nlibhistory.so:  ELF 64-bit MSB dynamic lib SPARCV9 Version 1, dynamically linked, not stripped\nlibhistory.so.6:        ELF 64-bit MSB dynamic lib SPARCV9 Version 1, dynamically linked, not stripped\n\nOther packages building 32-bit libraries, even when SAGE64 is set to \"yes\" include, but are probably not limited to:\n\n* zlib #7128\n* libgpg_error #7129 \n* libpng #7130\n\nI will sort this package out after creating a new sage-env, which exports all the variables properly, including the flag for building 64-bit code, which is not always -m64.\n\nAlthough there is no support for AIX or HP-UX in Sage yet, we could potentially add it - I personally own machines running AIX and HP-UX.\n\nIBM's compiler on AIX uses -q64, and HP's on HP-UX uses +DD64.\n\nThe sensible way to resolve this is to add the correct flag on every platform.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7131\n\n",
    "created_at": "2009-10-05T23:38:20Z",
    "labels": [
        "porting: Solaris",
        "major",
        "bug"
    ],
    "title": "libcliquer always builds 32-bit libraries on Solaris.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7131",
    "user": "drkirkby"
}
```
Assignee: tbd

Using

* A Sun Blade 2000 running Solaris 10 update 7
* Sage 4.1.2.rc0
* gcc 4.4.1
* SAGE64 exported to "yes" 

We can see that libcliquer is building 32-bit libraries, despite other packages are building 64-bit libraries. 

libcliquer.so:  ELF 32-bit MSB dynamic lib SPARC32PLUS Version 1, V8+ Required, dynamically linked, not stripped
libhistory.so:  ELF 64-bit MSB dynamic lib SPARCV9 Version 1, dynamically linked, not stripped
libhistory.so.6:        ELF 64-bit MSB dynamic lib SPARCV9 Version 1, dynamically linked, not stripped

Other packages building 32-bit libraries, even when SAGE64 is set to "yes" include, but are probably not limited to:

* zlib #7128
* libgpg_error #7129 
* libpng #7130

I will sort this package out after creating a new sage-env, which exports all the variables properly, including the flag for building 64-bit code, which is not always -m64.

Although there is no support for AIX or HP-UX in Sage yet, we could potentially add it - I personally own machines running AIX and HP-UX.

IBM's compiler on AIX uses -q64, and HP's on HP-UX uses +DD64.

The sensible way to resolve this is to add the correct flag on every platform.

Issue created by migration from https://trac.sagemath.org/ticket/7131





---

archive/issue_comments_059144.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-17T07:48:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7131#issuecomment-59144",
    "user": "drkirkby"
}
```

Resolution: fixed



---

archive/issue_comments_059145.json:
```json
{
    "body": "At some point this must have been fixed:\n\n\n```\ndrkirkby@hawk:~/sage-4.4.4.alpha0$ find . -name 'libcl*'\n./local/lib/libcliquer.so\ndrkirkby@hawk:~/sage-4.4.4.alpha0$ file ./local/lib/libcliquer.so\n./local/lib/libcliquer.so:      ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped\n```\n",
    "created_at": "2010-06-17T07:48:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7131",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7131#issuecomment-59145",
    "user": "drkirkby"
}
```

At some point this must have been fixed:


```
drkirkby@hawk:~/sage-4.4.4.alpha0$ find . -name 'libcl*'
./local/lib/libcliquer.so
drkirkby@hawk:~/sage-4.4.4.alpha0$ file ./local/lib/libcliquer.so
./local/lib/libcliquer.so:      ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
```

