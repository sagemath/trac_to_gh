# Issue 8771: Sage-4.4 + GCC-4.5.0 -- sage fails to startup due to libzn_poly missing symbol issue (ZNP_mpn_mulmid_fallback_thresh)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-04-26 20:53:40

Assignee: GeorgSWeber

The machine

```
[wstein`@`lena sage-4.4]$ uname -a
Linux lena 2.6.31.12-174.2.19.fc12.x86_64 #1 SMP Thu Feb 11 07:07:16 UTC 2010 x86_64 x86_64 x86_64 GNU/Linux
[wstein`@`lena sage-4.4]$ cat /etc/issue
Fedora release 12 (Constantine)
Kernel \r on an \m (\l)

[wstein`@`lena sage-4.4]$ gcc -v
Using built-in specs.
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/local/gcc-4.5.0/x86_64-Linux-k10-fc/libexec/gcc/x86_64-unknown-linux-gnu/4.5.0/lto-wrapper
Target: x86_64-unknown-linux-gnu
Configured with: /usr/local/gcc-4.5.0/src/gcc-4.5.0/configure --enable-languages=c,c++,fortran --with-gnu-as --with-gnu-as=/usr/local/binutils-2.20.1/x86_64-Linux-k10-fc-gcc-4.4.3/bin/as --with-gnu-ld --with-ld=/usr/local/binutils-2.20.1/x86_64-Linux-k10-fc-gcc-4.4.3/bin/ld --with-gmp=/usr/local/mpir-1.2.2/x86_64-Linux-k10-gcc-4.2.2 --with-mpfr=/usr/local/mpfr-2.4.2/x86_64-Linux-k10-fc-mpir-1.2.2-gcc-4.4.2 --with-mpc=/usr/local/mpc-0.8.1/x86_64-Linux-k10-fc-mpfr-2.4.2-mpir-1.2.2-gcc-4.4.3 --prefix=/usr/local/gcc-4.5.0/x86_64-Linux-k10-fc
Thread model: posix
gcc version 4.5.0 (GCC)
```


The error, after building Sage seems to finish fine:

```
./sage 
...
boom!
...
ImportError: /home/wstein/screen/lena/sage-4.4/local/lib/libzn_poly-0.9.so: undefined symbol: ZNP_mpn_mulmid_fallback_thresh
```



---

Comment by was created at 2010-04-26 21:28:51

wjp figured out that this boils down to some tuning program not getting built:

```
sage subshell$ gcc -fPIC -std=c99 -O3 -L. -I/home/wstein/screen/eno/sage-4.4/local/include -I./include -DNDEBUG -o tune/mulmid-tune.o -c tune/mulmid-tune.c
tune/mulmid-tune.c: In function ‘ZNP_tune_mulmid’:
tune/mulmid-tune.c:85:10: error: jump into scope of identifier with variably modified type
tune/mulmid-tune.c:135:7: note: label ‘done’ defined here
tune/mulmid-tune.c:115:14: note: ‘score’ declared here
tune/mulmid-tune.c:85:10: error: jump into scope of identifier with variably modified type
tune/mulmid-tune.c:135:7: note: label ‘done’ defined here
tune/mulmid-tune.c:114:14: note: ‘points’ declared here
tune/mulmid-tune.c:108:10: error: jump into scope of identifier with variably modified type
tune/mulmid-tune.c:135:7: note: label ‘done’ defined here
tune/mulmid-tune.c:115:14: note: ‘score’ declared here
tune/mulmid-tune.c:108:10: error: jump into scope of identifier with variably modified type
tune/mulmid-tune.c:135:7: note: label ‘done’ defined here
tune/mulmid-tune.c:114:14: note: ‘points’ declared here
/home/wstein/screen/eno/sage-4.4
sage subshell$                     
```


For this, 

```
14:26 < wjp> the fix is to move the lines
14:26 < wjp>       const int max_intervals = 20;
14:26 < wjp>       size_t points[max_intervals + 1];
14:26 < wjp>       double score[max_intervals + 1];
14:26 < wjp> up a bit to at least above the goto
```

but... 

```
4:26 < wjp> but after doing that it is now complaining about a missing ZNP_tuning_info when linking 'tune'
```



---

Comment by wjp created at 2010-04-26 21:59:46

I fixed the compile errors by moving the offending "identifiers with variably modified type" to above the goto, and added a check to the `spkg-install` script to see if building this tune program failed.

New spkg at:

http://www.math.leidenuniv.nl/~wpalenst/sage/zn_poly-0.9.p4.spkg


---

Comment by wjp created at 2010-04-26 21:59:46

Changing status from new to needs_review.


---

Comment by was created at 2010-04-26 22:19:56

Even new spkg here (with some slight referee improvements): 

          http://wstein.org/home/wstein/patches/zn_poly-0.9.p4.spkg


---

Comment by was created at 2010-04-26 22:19:56

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-04-26 22:21:16


```
15:21 < wjp> ok, your extra changes look good to me too
```



---

Comment by was created at 2010-04-28 19:17:27

Resolution: fixed


---

Comment by leif created at 2012-04-20 02:46:17

Only the changelog entry references the wrong ticket (#8711); now fixed at #12433...
