# Issue 1126: building of fplll is broken

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-11-07 19:07:40

Assignee: was


```
> 
> ***
> x86_64-Linux
> ***
> While compiling libfplll-2.1-20071024, I get
> 
> g++ -shared -nostdlib /usr/lib/../lib64/crti.o
> /usr/local/gcc-4.2.2/x86_64-Linux/lib/gcc/x86_64-unknown-linux-gnu/4.2.2/crtbeginS.o
>  .libs/fplll.o  -Wl,--rpath
> -Wl,/usr/local/gcc-4.2.2/x86_64-Linux/lib/../lib64 -Wl,--rpath
> -Wl,/usr/local/gcc-4.2.2/x86_64-Linux/lib/../lib64 -lmpfr -lgmp
> -L/usr/local/gcc-4.2.2/x86_64-Linux/lib/gcc/x86_64-unknown-linux-gnu/4.2.2
> -L/usr/local/gcc-4.2.2/x86_64-Linux/lib/gcc/x86_64-unknown-linux-gnu/4.2.2/../../../../lib64
> -L/lib/../lib64 -L/usr/lib/../lib64
> -L/home/kate/sage/sage-2.8.12-x86_64-Linux/local/lib
> -L/usr/local/gcc-4.2.2/x86_64-Linux/lib/gcc/x86_64-unknown-linux-gnu/4.2.2/../../..
> /usr/local/gcc-4.2.2/x86_64-Linux/lib/../lib64/libstdc++.so -lm -lc
> -lgcc_s /usr/local/gcc-4.2.2/x86_64-Linux/lib/gcc/x86_64-unknown-linux-gnu/4.2.2/crtendS.o
> /usr/lib/../lib64/crtn.o  -Wl,-soname -Wl,libfplll.so.0 -o
> .libs/libfplll.so.0.0.0
> /usr/bin/ld: /usr/lib/../lib64/libmpfr.a(exceptions.o): relocation
> R_X86_64_32 against `a local symbol' can not be used when making a
> shared object; recompile with -fPIC
> /usr/lib/../lib64/libmpfr.a: could not read symbols: Bad value
> 
> Why is Sage trying to use libmpfr.a out of /usr/lib?  Should it not be
> using the version
> in [sage]/local/lib?

I agree.  Note that libfpll is a brand new package in Sage (it does very fast LLL reduction,
so is quite important), but it hasn't been as widely tested as other components of Sage. 
```



---

Comment by mabshoff created at 2007-11-07 23:15:34

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-11-07 23:15:34

Changing assignee from was to mabshoff.


---

Comment by mabshoff created at 2007-11-07 23:15:34

For a potential solutions to this problem please try

http://sage.math.washington.edu/home/mabshoff/libfplll-2.1-20071024.p0.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-08 20:06:18

Ok, got feedback from Kate: It works on her x86-64 box and also builds fine for me on sage.math.

Cheers,

Michael


---

Comment by malb created at 2007-11-17 13:59:33

I've uploaded a new spkg to

http://sage.math.washington.edu/home/malb/pkgs/libfplll-2.1.3-20071117.spkg

which contains a cleaner fix than the package linked above by mabshoff. We shouldn't touch `Makefile.am` of the upstream package with SAGE specific fixes and thus I added that flag to `spkg-install`.


---

Comment by mabshoff created at 2007-11-18 06:19:30

Resolution: fixed


---

Comment by mabshoff created at 2007-11-18 06:19:30

Merged in 2.8.13.alpha0.
