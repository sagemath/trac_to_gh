# Issue 6974: cygwin port: make all the crypto ssl-ish spkg's into dummy packages on Cygwin (where we can use the system openssl instead)

Issue created by migration from https://trac.sagemath.org/ticket/6974

Original creator: was

Original creation time: 2009-09-21 02:23:39

Assignee: tbd

The packages are:

   *


---

Comment by certik created at 2009-09-21 02:32:43

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

Comment by certik created at 2009-09-21 02:51:58

now it looks good, +1 from me


---

Comment by certik created at 2009-09-21 03:15:04

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

Comment by certik created at 2009-09-21 03:16:38

libgcrypt-1.4.3.p2.spkg and opencdk-0.6.6.p1.spkg are ok. 

Packages that I "oked" all fail for me with:


```
Detected Cygwin -- checking for openssl development headers, since we use openssl instead.
On Cygwin you *must* install Cygwin's openssl-devel development package (using Cygwin's setup.exe program).
```


which I think is ok.


---

Comment by certik created at 2009-09-21 03:32:14

Now even the python_gnutls-1.1.4.p5.spkg fails with: 


```
Detected Cygwin -- checking for openssl development headers, since we use openssl instead.
On Cygwin you *must* install Cygwin's openssl-devel development package (using Cygwin's setup.exe program).
```


so all packages +1.


---

Comment by was created at 2009-09-21 06:38:12

Changing priority from major to blocker.


---

Comment by mvngu created at 2009-09-27 00:21:45

New gnutls package up at

http://sage.math.washington.edu/home/mvngu/release/spkg/standard/gnutls-2.2.1.p4.spkg

The only change from .p3 is checking in all existing changes in wstein's name.


---

Comment by mvngu created at 2009-09-27 00:27:09

See ticket #6758 about libgcrypt-1.4.3.p2.spkg being seriously messed up.


---

Comment by mvngu created at 2009-09-27 00:47:08

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

Comment by mvngu created at 2009-09-27 02:58:25

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 02:58:25

See palmieri's and my reports at #6849.


---

Comment by mvngu created at 2009-09-27 10:59:34

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
