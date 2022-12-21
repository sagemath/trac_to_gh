# Issue 8768: gnutls-2.2.1.p5 doesn't build on Solaris 10 x86 (fulvia) with GCC-4.5.0

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-04-26 18:09:29

Assignee: drkirkby

CC:  jhpalmieri jsp


```
gcc -std=gnu99 -g -O2 -D_REENTRANT -D_THREAD_SAFE -I/home/wstein/screen/fulvia/sage-4.4/local/include -g -O2 -D_REENTRANT -D_THREAD_SAFE -Wno-pointer-sign -o .libs/gnutls-serv serv-gaa.o serv.o common.o select.o  -L/home/wstein/screen/fulvia/sage-4.4/spkg/build/gnutls-2.2.1.p5/src/lib/.libs ../lib/.libs/libgnutls.so -L/home/wstein/screen/fulvia/sage-4.4/local/lib ../libextra/.libs/libgnutls-extra.so /home/wstein/screen/fulvia/sage-4.4/local/lib/libopencdk.so /home/wstein/screen/fulvia/sage-4.4/spkg/build/gnutls-2.2.1.p5/src/lib/.libs/libgnutls.so -lz ../gl/.libs/libgnu.a /home/wstein/screen/fulvia/sage-4.4/local/lib/libgcrypt.so /home/wstein/screen/fulvia/sage-4.4/local/lib/libgpg-error.so -lsocket  -R/home/wstein/screen/fulvia/sage-4.4/local/lib
serv.o: In function `peer_print_info':
/home/wstein/screen/fulvia/sage-4.4/spkg/build/gnutls-2.2.1.p5/src/src/serv.c:489: undefined reference to `gnutls_x509_crt_print'
common.o: In function `print_x509_info':
/home/wstein/screen/fulvia/sage-4.4/spkg/build/gnutls-2.2.1.p5/src/src/common.c:151: undefined reference to `gnutls_x509_crt_check_hostname'
../libextra/.libs/libgnutls-extra.so: undefined reference to `_gnutls_hostname_compare'
collect2: ld returned 1 exit status
make[5]: *** [gnutls-serv] Error 1
make[5]: Leaving directory `/home/wstein/screen/fulvia/sage-4.4/spkg/build/gnutls-2.2.1.p5/src/src'
make[4]: *** [all-recursive] Error 1
make[4]: Leaving directory `/home/wstein/screen/fulvia/sage-4.4/spkg/build/gnutls-2.2.1.p5/src/src'
make[3]: *** [all-recursive] Error 1
make[3]: Leaving directory `/home/wstein/screen/fulvia/sage-4.4/spkg/build/gnutls-2.2.1.p5/src'
```


More machine details:

```
-bash-3.00$ uname -a
SunOS mark 5.10 Generic_127111-01 sun4u sparc SUNW,Sun-Blade-2500
-bash-3.00$ gcc -v
Using built-in specs.
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/local/gcc-4.5.0/sparc-SunOS-ultrasparc3/libexec/gcc/sparc-sun-solaris2.10/4.5.0/lto-wrapper
Target: sparc-sun-solaris2.10
Configured with: /usr/local/gcc-4.5.0/src/gcc-4.5.0/configure --enable-languages=c,c++,fortran --with-gnu-as --with-as=/usr/local/binutils-2.20.1/sparc-SunOS-ultrasparc3-gcc-4.4.3/bin/as --with-gnu-ld --with-ld=/usr/local/binutils-2.20.1/sparc-SunOS-ultrasparc3-gcc-4.4.3/bin/ld --with-gmp=/usr/local/mpir-1.2.2/sparc-SunOS-ultrasparc3-gcc-4.4.2-abi32 --with-mpfr=/usr/local/mpfr-2.4.2/sparc-SunOS-ultrasparc3-mpir-1.2.2-gcc-4.4.2-abi32 --with-mpc=/usr/local/mpc-0.8.1/sparc-SunOS-ultrasparc3-mpfr-2.4.2-mpir-1.2.2-gcc-4.4.3-abi32 --prefix=/usr/local/gcc-4.5.0/sparc-SunOS-ultrasparc3
Thread model: posix
gcc version 4.5.0 (GCC)
```


}}}


---

Comment by was created at 2010-04-26 20:04:13

Changing priority from major to critical.


---

Comment by was created at 2010-04-26 20:04:13

Note: On SPARC Solaris 10, GNUtls *also* fails to build, with a similar error.  However, the reported undefined symbol that stops the build is different than on x86. Here is what we get on mark:

```
checking whether we are using the GNU Fortran 77 compiler... yes
checking whether gfortran accepts -g... yes
checking the maximum length of command line arguments... rint_x509_info':
/home/wstein/screen/fulvia/sage-4.4/spkg/build/gnutls-2.2.1.p5/src/src/common.c:151: undefined reference to
nutls_x509_crt_check_hostname'
../libextra/.libs/libgnutls-extra.so: undefined reference to gnutls_hostname_compare'
collect2: ld returned 1 exit status
make[5]: *** [gnutls-serv] Error 1
make[5]: Leaving directory home/wstein/screen/fulvia/sage-4.4/spkg/build/gnutls-2.2.1.p5/src/src'
make[4]: *** [all-recursive] Error 1
make[4]: Leaving directory home/wstein/screen/fulvia/sage-4.4/spkg/build/gnutls-2.2.1.p5/src/src'
make[3]: *** [all-recursive] Error 1
make[3]: Leaving directory home/wstein/screen/fulvia/sage-4.4/spkg/build/gnutls-2.2.1.p5/src'
make[2]: *** [all] Error 2
make[2]: Leaving directory home/wstein/screen/fulvia/sage-4.4/spkg/build/gnutls-2.2.1.p5/src'
failed to build GNUTLS

real    2m45.511s
user    0m48.789s
sys     1m1.201s
sage: An error occurred while installing gnutls-2.2.1.p5
q^[^[^[


^Cmake: *** [build] Error 130
-bash-3.00$
-bash-3.00$  gcc -v
Using built-in specs.
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/local/gcc-4.5.0/sparc-SunOS-ultrasparc3/libexec/gcc/sparc-sun-solaris2.10/4.5.0/lto
-wrapper
Target: sparc-sun-solaris2.10
Configured with: /usr/local/gcc-4.5.0/src/gcc-4.5.0/configure --enable-languages=c,c++,fortran --with-gnu-as
 --with-as=/usr/local/binutils-2.20.1/sparc-SunOS-ultrasparc3-gcc-4.4.3/bin/as --with-gnu-ld --with-ld=/usr/
local/binutils-2.20.1/sparc-SunOS-ultrasparc3-gcc-4.4.3/bin/ld --with-gmp=/usr/local/mpir-1.2.2/sparc-SunOS-
ultrasparc3-gcc-4.4.2-abi32 --with-mpfr=/usr/local/mpfr-2.4.2/sparc-SunOS-ultrasparc3-mpir-1.2.2-gcc-4.4.2-a
bi32 --with-mpc=/usr/local/mpc-0.8.1/sparc-SunOS-ultrasparc3-mpfr-2.4.2-mpir-1.2.2-gcc-4.4.3-abi32 --prefix=
/usr/local/gcc-4.5.0/sparc-SunOS-ultrasparc3
Thread model: posix
gcc version 4.5.0 (GCC)
-bash-3.00$ uname -a
SunOS mark 5.10 Generic_127111-01 sun4u sparc SUNW,Sun-Blade-2500
-bash-3.00$ uname -a
SunOS mark 5.10 Generic_127111-01 sun4u sparc SUNW,Sun-Blade-2500
-bash-3.00$ gcc -v
Using built-in specs.
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/local/gcc-4.5.0/sparc-SunOS-ultrasparc3/libexec/gcc/sparc-sun-solaris2.10/4.5.0/lto
-wrapper
Target: sparc-sun-solaris2.10
Configured with: /usr/local/gcc-4.5.0/src/gcc-4.5.0/configure --enable-languages=c,c++,fortran --with-gnu-as
 --with-as=/usr/local/binutils-2.20.1/sparc-SunOS-ultrasparc3-gcc-4.4.3/bin/as --with-gnu-ld --with-ld=/usr/local/binutils-2.20.1/sparc-SunOS-ultrasparc3-gcc-4.4.3/bin/ld --with-gmp=/usr/local/mpir-1.2.2/sparc-SunOS-ultrasparc3-gcc-4.4.2-abi32 --with-mpfr=/usr/local/mpfr-2.4.2/sparc-SunOS-ultrasparc3-mpir-1.2.2-gcc-4.4.2-abi32 --with-mpc=/usr/local/mpc-0.8.1/sparc-SunOS-ultrasparc3-mpfr-2.4.2-mpir-1.2.2-gcc-4.4.3-abi32 --prefix=/usr/local/gcc-4.5.0/sparc-SunOS-ultrasparc3
Thread model: posix
gcc version 4.5.0 (GCC)
-bash-3.00$ hostname
mark
```



---

Comment by was created at 2010-04-26 20:09:17

Changing priority from critical to blocker.


---

Comment by drkirkby created at 2010-05-06 23:02:47

Note, gcc 4.5 is *not* the latest gcc, but gcc 4.4.4 is: See

http://gcc.gnu.org/


```
News

April 29, 2010
    GCC 4.4.4 has been released.
April 14, 2010
    GCC 4.5.0 has been released.
```


Dave


---

Comment by drkirkby created at 2010-05-07 21:17:18

It would probably be better if gcc 4.5 was configured with the Sun linker rather than the GNU linker. On OpenSolaris, best results have been achieved using the GNU assembler and the Sun linker. 

On Solaris 10 (SPARC), both the Sun linker and Sun assembler are used, but that combo does not work too well on OpenSolaris, where the GNU assembler seems to be necessary. 



Dave


---

Comment by drkirkby created at 2010-05-22 08:25:27

I've not tried gcc 4.5, but gcc 4.4.4 configured with the Sun linker and GNU assembler and it builds OK on my Sun Ultra 27 (Xeon processor) running OpenSolaris 06/2009. 

Note the version 4.5 compiler where this problem was observerved was configured with the option



```
--with-ld=/usr/local/binutils-2.20.1/sparc-SunOS-ultrasparc3-gcc-4.4.3/bin/ld
```


which I've personally always found to cause more problems than the Sun linker. I also note that using the Sun linker is recommended by GNU - see http://gcc.gnu.org/install/specific.html#ix86-x-solaris210 

I think it would be better if the gcc on fulvia was configured the way recommended in the GNU documentation. 

Dave


---

Comment by drkirkby created at 2010-05-22 08:27:02

For the record, this is how gcc 4.4.4 was configured by me:


```
drkirkby`@`hawk:~/sage-4.4.2/spkg$ gcc -v
Using built-in specs.
Target: i386-pc-solaris2.11
Configured with: ../gcc-4.4.4/configure --prefix=/usr/local/gcc-4.4.4 --with-as=/usr/local/binutils-2.20/bin/as --with-ld=/usr/ccs/bin/ld --with-gmp=/usr/local --with-mpfr=/usr/local
Thread model: posix
gcc version 4.4.4 (GCC) 
```


using the Sun linker and GNU assembler, as recommended at http://gcc.gnu.org/install/specific.html#ix86-x-solaris210


---

Comment by drkirkby created at 2010-05-22 08:30:08

Oops, I see this was Solaris 10, not OpenSolaris (aka Solaris 11). But the link I provided is for Solaris 10 or later on x86, so the point is still valid, that this version of gcc is probably not configured in the ideal way. 

It looks like a linker problem.

Dave


---

Comment by was created at 2010-06-03 04:07:33

This is not a 4.4.3 blocker.


---

Comment by drkirkby created at 2010-07-31 01:15:21

I'm closing this as invalid. gnutls builds fine on fulvia. I've built it, as has John Palmieri. 

The reason you had trouble was that gcc was mis-configured. I'm of the opinion it is better to use both the Sun linker and Sun assembler on SPARC. Since Mariah provided a gcc configured in this way at:


```
/usr/local/gcc-4.5.0/x86_64-SunOS-core2-sun-ld/bin/gcc
```


the problem has gone away. Note, the default compiler on fulvia is not configured like this. 


```
64 drkirkby`@`fulvia:[~/fulvia/32/sage-4.5.1] $ gcc -v
Using built-in specs.
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/local/gcc-4.5.0/x86_64-SunOS-core2-sun-ld/libexec/gcc/i386-pc-solaris2.10/4.5.0/lto-wrapper
Target: i386-pc-solaris2.10
Configured with: /usr/local/gcc-4.5.0/src/gcc-4.5.0/configure --enable-languages=c,c++,fortran --with-gnu-as --with-as=/usr/local/binutils-2.20.1/x86_64-SunOS-core2-gcc-4.4.3/bin/as --with-ld=/usr/ccs/bin/ld --with-gmp=/usr/local/gmp-5.0.1/x86_64-SunOS-core2-gcc-4.5.0-abi32 --with-mpfr=/usr/local/mpfr-3.0.0/x86_64-SunOS-core2-gmp-5.0.1-gcc-4.5.0-abi32 --with-mpc=/usr/local/mpc-0.8.2/x86_64-SunOS-core2-mpfr-3.0.0-gmp-5.0.1-gcc-4.5.0-abi32 --prefix=/usr/local/gcc-4.5.0/x86_64-SunOS-core2-sun-ld
Thread model: posix
gcc version 4.5.0 (GCC) 
```


An inspection of the log shows gnutls installed OK. 


```
64 drkirkby`@`fulvia:[~/fulvia/32/sage-4.5.1] $ tail -30  spkg/logs/gnutls-2.2.1.p5.log
  for file in Makefile.in.in remove-potcdate.sin quot.sed boldquot.sed en`@`quot.header en`@`boldquot.header insert-header.sin Rules-quot   Makevars.template; do \
    ../build-aux/install-sh -c -m 644 ./$file \
		    /home/drkirkby/fulvia/32/sage-4.5.1/local/share/gettext/po/$file; \
  done; \
  for file in Makevars; do \
    rm -f /home/drkirkby/fulvia/32/sage-4.5.1/local/share/gettext/po/$file; \
  done; \
else \
  : ; \
fi
make[3]: Leaving directory `/home/drkirkby/fulvia/32/sage-4.5.1/spkg/build/gnutls-2.2.1.p5/src/po'
make[3]: Entering directory `/home/drkirkby/fulvia/32/sage-4.5.1/spkg/build/gnutls-2.2.1.p5/src'
make[4]: Entering directory `/home/drkirkby/fulvia/32/sage-4.5.1/spkg/build/gnutls-2.2.1.p5/src'
make[4]: warning: -jN forced in submake: disabling jobserver mode.
make[4]: Nothing to be done for `install-exec-am'.
make[4]: Nothing to be done for `install-data-am'.
make[4]: Leaving directory `/home/drkirkby/fulvia/32/sage-4.5.1/spkg/build/gnutls-2.2.1.p5/src'
make[3]: Leaving directory `/home/drkirkby/fulvia/32/sage-4.5.1/spkg/build/gnutls-2.2.1.p5/src'
make[2]: Leaving directory `/home/drkirkby/fulvia/32/sage-4.5.1/spkg/build/gnutls-2.2.1.p5/src'

real	39m58.479s
user	1m9.593s
sys	1m50.962s
Successfully installed gnutls-2.2.1.p5
Now cleaning up tmp files.
rm: Cannot remove any directory in the path of the current working directory
/home/drkirkby/fulvia/32/sage-4.5.1/spkg/build/gnutls-2.2.1.p5
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing gnutls-2.2.1.p5.spkg
```


Dave


---

Comment by drkirkby created at 2010-07-31 01:15:21

Resolution: invalid


---

Comment by drkirkby created at 2010-07-31 01:19:20

Replying to [comment:9 drkirkby]:

> The reason you had trouble was that gcc was mis-configured. I'm of the opinion it is better to use both the Sun linker and Sun assembler on SPARC. Since Mariah provided a gcc configured in this way at:

Correction, this is not SPARC, but x86. In which case, IMHO, gcc should be configured with the Sun linker and GNU assembler. Since Mariah provided such a gcc at 


```
/usr/local/gcc-4.5.0/x86_64-SunOS-core2-sun-ld/bin/gcc
```


the problem has gone. So this remains invalid.


---

Comment by mpatel created at 2010-09-12 22:56:06

I see the error in the description when I compile 4.5.3 on fulvia.  Perhaps I've misconfigured the environment?  I've sourced `/usr/local/skynet_bash_profile` and I get

```sh
$ gcc -v
Using built-in specs.
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/local/gcc-4.5.1/x86_64-SunOS-core2/libexec/gcc/i386-pc-solaris2.10/4.5.1/lto-wrapper
Target: i386-pc-solaris2.10
Configured with: /usr/local/gcc-4.5.1/src/gcc-4.5.1/configure --enable-languages=c,c++,fortran --with-gnu-as --with-as=/usr/local/binutils-2.20.1/x86_64-SunOS-core2-gcc-4.4.3/bin/as --with-gnu-ld --with-ld=/usr/local/binutils-2.20.1/x86_64-SunOS-core2-gcc-4.4.3/bin/ld --with-gmp=/usr/local/gmp-5.0.1/x86_64-SunOS-core2-gcc-4.5.0-abi32 --with-mpfr=/usr/local/mpfr-3.0.0/x86_64-SunOS-core2-gmp-5.0.1-gcc-4.5.0-abi32 --with-mpc=/usr/local/mpc-0.8.2/x86_64-SunOS-core2-mpfr-3.0.0-gmp-5.0.1-gcc-4.5.0-abi32 --prefix=/usr/local/gcc-4.5.1/x86_64-SunOS-core2
Thread model: posix
gcc version 4.5.1 (GCC) 
```



---

Comment by mpatel created at 2010-09-12 23:42:56

Replying to [comment:12 mpatel]:
> I see the error in the description when I compile 4.5.3 on fulvia.  Perhaps I've misconfigured the environment?  I've sourced `/usr/local/skynet_bash_profile` and I get [...]

Preprending `/usr/local/gcc-4.5.1/x86_64-SunOS-core2-sun-ld/bin` to the `PATH` appears to fix this problem.


---

Comment by jhpalmieri created at 2010-09-13 01:39:06

That's right, the settings in /usr/local/skynet_bash_profile are set up this way, even though Sage won't build with those settings.  See [http://wiki.sagemath.org/skynet](http://wiki.sagemath.org/skynet) for instructions on how to set up fulvia to build Sage.


---

Comment by mpatel created at 2010-09-13 05:51:54

Thanks.  I'll adapt the settings for fulvia and the marks from the wiki page.


---

Comment by drkirkby created at 2010-09-13 10:14:57

Replying to [comment:15 mpatel]:
> Thanks.  I'll adapt the settings for fulvia and the marks from the wiki page.
I've just updated that Wiki (about 10 minutes ago_, as it said Sage would not build on fulvia, but in fact it does. Also, Sage should now build 64-bit on `mark` and `mark2`, though as I remarked there, the build will be unstable. I suggest you re-read the particular section of interest. 

I also added the need to read


```
/usr/local/README.background_jobs
```

