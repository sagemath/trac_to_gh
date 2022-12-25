# Issue 6974: cygwin port: make all the crypto ssl-ish spkg's into dummy packages on Cygwin (where we can use the system openssl instead)

archive/issues_006974.json:
```json
{
    "body": "Assignee: tbd\n\nThe packages are:\n\n   *\n\nIssue created by migration from https://trac.sagemath.org/ticket/6974\n\n",
    "created_at": "2009-09-21T02:23:39Z",
    "labels": [
        "component: porting"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "cygwin port: make all the crypto ssl-ish spkg's into dummy packages on Cygwin (where we can use the system openssl instead)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6974",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

The packages are:

   *

Issue created by migration from https://trac.sagemath.org/ticket/6974





---

archive/issue_comments_057573.json:
```json
{
    "body": "The package works on linux. in cygwin I got:\n\ngcc version 4.3.2 20080827 (beta) 2 (GCC) \n****************************************************\nDetected Cygwin -- checking for OPENssl development headers, since we use openssl instead.\n\nreal\t0m0.078s\nuser\t0m0.015s\nsys\t0m0.015s\nsage: An error occurred while installing libgpg_error-1.6.p2\n\n\nit should print information what has to be installed if it fails",
    "created_at": "2009-09-21T02:32:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6974#issuecomment-57573",
    "user": "https://github.com/certik"
}
```

The package works on linux. in cygwin I got:

gcc version 4.3.2 20080827 (beta) 2 (GCC) 
****************************************************
Detected Cygwin -- checking for OPENssl development headers, since we use openssl instead.

real	0m0.078s
user	0m0.015s
sys	0m0.015s
sage: An error occurred while installing libgpg_error-1.6.p2


it should print information what has to be installed if it fails



---

archive/issue_comments_057574.json:
```json
{
    "body": "now it looks good, +1 from me",
    "created_at": "2009-09-21T02:51:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6974#issuecomment-57574",
    "user": "https://github.com/certik"
}
```

now it looks good, +1 from me



---

archive/issue_comments_057575.json:
```json
{
    "body": "gnutls-2.2.1.p3.spkg is ok\n\npython_gnutls-1.1.4.p5.spkg fails with:\n\n```\ngcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/home/ondrej/tmp/sage-4.1-cygwin-i686-CYGWIN_NT-5.1/local/include/ -I/home/ondrej/tmp/sage-4.1-cygwin-i686-CYGWIN_NT-5.1/local/include/python2.6 -c gnutls/library/_gnutls_init.c -o build/temp.cygwin-1.5.25-i686-2.6/gnutls/library/_gnutls_init.o\ngnutls/library/_gnutls_init.c:11:27: error: gnutls/gnutls.h: No such file or directory\ngnutls/library/_gnutls_init.c:12:26: error: gnutls/extra.h: No such file or directory\ngnutls/library/_gnutls_init.c:13:20: error: gcrypt.h: No such file or directory\ngnutls/library/_gnutls_init.c:18: warning: data definition has no type or storage class\ngnutls/library/_gnutls_init.c:18: warning: type defaults to 'int' in declaration of 'GCRY_THREAD_OPTION_PTHREAD_IMPL'\ngnutls/library/_gnutls_init.c: In function 'init_gnutls_init':\ngnutls/library/_gnutls_init.c:42: warning: implicit declaration of function 'gcry_control'\ngnutls/library/_gnutls_init.c:42: error: 'GCRYCTL_SET_THREAD_CBS' undeclared (first use in this function)\ngnutls/library/_gnutls_init.c:42: error: (Each undeclared identifier is reported only once\ngnutls/library/_gnutls_init.c:42: error: for each function it appears in.)\ngnutls/library/_gnutls_init.c:42: error: 'gcry_threads_pthread' undeclared (first use in this function)\ngnutls/library/_gnutls_init.c:44: warning: implicit declaration of function 'gnutls_global_init'\ngnutls/library/_gnutls_init.c:45: warning: implicit declaration of function 'gnutls_global_init_extra'\nerror: command 'gcc' failed with exit status 1\n```\n",
    "created_at": "2009-09-21T03:15:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6974#issuecomment-57575",
    "user": "https://github.com/certik"
}
```

gnutls-2.2.1.p3.spkg is ok

python_gnutls-1.1.4.p5.spkg fails with:

```
gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/home/ondrej/tmp/sage-4.1-cygwin-i686-CYGWIN_NT-5.1/local/include/ -I/home/ondrej/tmp/sage-4.1-cygwin-i686-CYGWIN_NT-5.1/local/include/python2.6 -c gnutls/library/_gnutls_init.c -o build/temp.cygwin-1.5.25-i686-2.6/gnutls/library/_gnutls_init.o
gnutls/library/_gnutls_init.c:11:27: error: gnutls/gnutls.h: No such file or directory
gnutls/library/_gnutls_init.c:12:26: error: gnutls/extra.h: No such file or directory
gnutls/library/_gnutls_init.c:13:20: error: gcrypt.h: No such file or directory
gnutls/library/_gnutls_init.c:18: warning: data definition has no type or storage class
gnutls/library/_gnutls_init.c:18: warning: type defaults to 'int' in declaration of 'GCRY_THREAD_OPTION_PTHREAD_IMPL'
gnutls/library/_gnutls_init.c: In function 'init_gnutls_init':
gnutls/library/_gnutls_init.c:42: warning: implicit declaration of function 'gcry_control'
gnutls/library/_gnutls_init.c:42: error: 'GCRYCTL_SET_THREAD_CBS' undeclared (first use in this function)
gnutls/library/_gnutls_init.c:42: error: (Each undeclared identifier is reported only once
gnutls/library/_gnutls_init.c:42: error: for each function it appears in.)
gnutls/library/_gnutls_init.c:42: error: 'gcry_threads_pthread' undeclared (first use in this function)
gnutls/library/_gnutls_init.c:44: warning: implicit declaration of function 'gnutls_global_init'
gnutls/library/_gnutls_init.c:45: warning: implicit declaration of function 'gnutls_global_init_extra'
error: command 'gcc' failed with exit status 1
```




---

archive/issue_comments_057576.json:
```json
{
    "body": "libgcrypt-1.4.3.p2.spkg and opencdk-0.6.6.p1.spkg are ok. \n\nPackages that I \"oked\" all fail for me with:\n\n\n```\nDetected Cygwin -- checking for openssl development headers, since we use openssl instead.\nOn Cygwin you *must* install Cygwin's openssl-devel development package (using Cygwin's setup.exe program).\n```\n\n\nwhich I think is ok.",
    "created_at": "2009-09-21T03:16:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6974#issuecomment-57576",
    "user": "https://github.com/certik"
}
```

libgcrypt-1.4.3.p2.spkg and opencdk-0.6.6.p1.spkg are ok. 

Packages that I "oked" all fail for me with:


```
Detected Cygwin -- checking for openssl development headers, since we use openssl instead.
On Cygwin you *must* install Cygwin's openssl-devel development package (using Cygwin's setup.exe program).
```


which I think is ok.



---

archive/issue_comments_057577.json:
```json
{
    "body": "Now even the python_gnutls-1.1.4.p5.spkg fails with: \n\n\n```\nDetected Cygwin -- checking for openssl development headers, since we use openssl instead.\nOn Cygwin you *must* install Cygwin's openssl-devel development package (using Cygwin's setup.exe program).\n```\n\n\nso all packages +1.",
    "created_at": "2009-09-21T03:32:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6974#issuecomment-57577",
    "user": "https://github.com/certik"
}
```

Now even the python_gnutls-1.1.4.p5.spkg fails with: 


```
Detected Cygwin -- checking for openssl development headers, since we use openssl instead.
On Cygwin you *must* install Cygwin's openssl-devel development package (using Cygwin's setup.exe program).
```


so all packages +1.



---

archive/issue_comments_057578.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2009-09-21T06:38:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6974#issuecomment-57578",
    "user": "https://github.com/williamstein"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_057579.json:
```json
{
    "body": "New gnutls package up at\n\nhttp://sage.math.washington.edu/home/mvngu/release/spkg/standard/gnutls-2.2.1.p4.spkg\n\nThe only change from .p3 is checking in all existing changes in wstein's name.",
    "created_at": "2009-09-27T00:21:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6974#issuecomment-57579",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

New gnutls package up at

http://sage.math.washington.edu/home/mvngu/release/spkg/standard/gnutls-2.2.1.p4.spkg

The only change from .p3 is checking in all existing changes in wstein's name.



---

archive/issue_comments_057580.json:
```json
{
    "body": "See ticket #6758 about libgcrypt-1.4.3.p2.spkg being seriously messed up.",
    "created_at": "2009-09-27T00:27:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6974#issuecomment-57580",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

See ticket #6758 about libgcrypt-1.4.3.p2.spkg being seriously messed up.



---

archive/issue_comments_057581.json:
```json
{
    "body": "New opencdk package up at\n\nhttp://sage.math.washington.edu/home/mvngu/release/spkg/standard/opencdk-0.6.6.p2.spkg\n\nThe only change from .p1 is to add the following standard check to `spkg-install`:\n\n```\nif [ \"$SAGE_LOCAL\" = \"\" ]; then\n   echo \"SAGE_LOCAL undefined ... exiting\";\n   echo \"Maybe run 'sage -sh'?\"\n   exit 1\nfi\n```\n",
    "created_at": "2009-09-27T00:47:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6974#issuecomment-57581",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

New opencdk package up at

http://sage.math.washington.edu/home/mvngu/release/spkg/standard/opencdk-0.6.6.p2.spkg

The only change from .p1 is to add the following standard check to `spkg-install`:

```
if [ "$SAGE_LOCAL" = "" ]; then
   echo "SAGE_LOCAL undefined ... exiting";
   echo "Maybe run 'sage -sh'?"
   exit 1
fi
```




---

archive/issue_events_007196.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-27T02:58:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6974",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6974#event-7196"
}
```



---

archive/issue_comments_057582.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-27T02:58:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6974#issuecomment-57582",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_057583.json:
```json
{
    "body": "See palmieri's and my reports at #6849.",
    "created_at": "2009-09-27T02:58:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6974#issuecomment-57583",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

See palmieri's and my reports at #6849.



---

archive/issue_comments_057584.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T10:59:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6974",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6974#issuecomment-57584",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
