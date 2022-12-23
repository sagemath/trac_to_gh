# Issue 8769: linbox fails on Fedora Core 12 x86_64 with gcc-4.5.0, due to "Givaro not good enough" error.

Issue created by migration from https://trac.sagemath.org/ticket/8769

Original creator: was

Original creation time: 2010-04-26 19:59:58

Assignee: GeorgSWeber


```
checking for NTL >= 5.0... found
checking for GIVARO >= 3.2.10... problem
Sorry, your GIVARO version is too old. Disabling.
*******************************************************************************
 ERROR: GIVARO not found!

 GIVARO version 3.2.10 or greater is required for this library to compile.
 Please make sure GIVARO is installed and specify its location with the
 option --with-givaro=<prefix> when running configure.
*******************************************************************************
Error configuring linbox

real    0m10.872s
user    0m4.506s
sys     0m4.882s
sage: An error occurred while installing linbox-1.1.6.p3
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /home/wstein/screen/flavius/sage-4.4/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem yourself, *don't* just cd to
/home/wstein/screen/flavius/sage-4.4/spkg/build/linbox-1.1.6.p3 and type 'make check' or whatever is appropriate.
Instead, the following commands setup all environment variables
correctly and load a subshell for you to debug the error:
(cd '/home/wstein/screen/flavius/sage-4.4/spkg/build/linbox-1.1.6.p3' && '/home/wstein/screen/flavius/sage-4.4/sage' -sh)
When you are done debugging, you can type "exit" to leave the
subshell.
make[1]: *** [installed/linbox-1.1.6.p3] Error 1
make[1]: Leaving directory `/home/wstein/screen/flavius/sage-4.4/spkg'

real    0m13.018s
user    0m5.586s
sys     0m5.119s
Error building Sage.
./sage -docbuild all html  2>&1 | tee -a dochtml.log
python: can't open file '/home/wstein/screen/flavius/sage-4.4/devel/sage/doc/common/builder.py': [Errno 2] No such file or directory
./sage -b
There is no directory '/home/wstein/screen/flavius/sage-4.4/devel/sage'

real    0m0.026s
user    0m0.011s
sys     0m0.017s
make: *** [testlong] Error 1
[wstein@flavius flavius]$ eer_print_info':
> /home/wstein/screen/fulvia/sage-4.4/spkg/build/gnutls-2.2.1.p5/src/src/serv.c:489: undefined reference to nutls_x509_crt_print'
-bash: eer_print_info:
/home/wstein/screen/fulvia/sage-4.4/spkg/build/gnutls-2.2.1.p5/src/src/serv.c:489: undefined reference to nutls_x509_crt_print: No such file or directory
[wstein@flavius flavius]$ uname -a
Linux flavius 2.6.31.12-174.2.19.fc12.x86_64 #1 SMP Thu Feb 11 07:07:16 UTC 2010 x86_64 x86_64 x86_64 GNU/Linux
[wstein@flavius flavius]$ cat /etc/issue
Fedora release 12 (Constantine)
Kernel \r on an \m (\l)

[wstein@flavius flavius]$ gcc -v
Using built-in specs.
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/local/gcc-4.5.0/x86_64-Linux-k8-fc/libexec/gcc/x86_64-unknown-linux-gnu/4.5.0/lto-wrapper
Target: x86_64-unknown-linux-gnu
Configured with: /usr/local/gcc-4.5.0/src/gcc-4.5.0/configure --enable-languages=c,c++,fortran --with-gnu-as --with-as=/usr/local/binutils-2.20.1/x86_64-Linux-k8-fc-gcc-4.4.3/bin/as --with-gnu-ld --with-ld=/usr/local/binutils-2.20.1/x86_64-Linux-k8-fc-gcc-4.4.3/bin/ld --with-gmp=/usr/local/mpir-1.2.2/x86_64-Linux-k8-gcc-4.2.2 --with-mpfr=/usr/local/mpfr-2.4.2/x86_64-Linux-k8-fc-mpir-1.2.2-gcc-4.4.2 --with-mpc=/usr/local/mpc-0.8.1/x86_64-Linux-k8-fc-mpfr-2.4.2-mpir-1.2.2-gcc-4.4.3 --prefix=/usr/local/gcc-4.5.0/x86_64-Linux-k8-fc
Thread model: posix
gcc version 4.5.0 (GCC)
[wstein@flavius flavius]$     

YET Givaro is installed!

[wstein@flavius sage-4.4]$ ls spkg/installed/givaro-3.2.13rc2.p0
spkg/installed/givaro-3.2.13rc2.p0

```



---

Comment by was created at 2010-04-26 20:01:28

Machines where this can be easily replicated (on skynet):

   * flavius

   * taurus


---

Comment by was created at 2010-04-26 21:17:41

* This turned out to be a bug in the system-wide LD_LIBRARY_PATH on flavius. 

 * On taurus there was also an LD_LIBRARY_PATH mistake.

So not a sage issue; case closed.


---

Comment by was created at 2010-04-26 21:17:41

Resolution: fixed


---

Comment by mvngu created at 2010-04-29 15:05:22

Resolution changed from fixed to invalid
