# Issue 6970: port R spkg to os x 10.6

Issue created by migration from https://trac.sagemath.org/ticket/6970

Original creator: was

Original creation time: 2009-09-20 22:23:29

Assignee: tbd




---

Comment by was created at 2009-09-20 23:07:21

The error message is:

```
...
stration.o relop.o rlocale.o saveload.o scan.o seq.o serialize.o size.o sort.o source.o split.o sprintf.o startup.o subassign.o subscript.o subset.o summary.o sysutils.o unique.o util.o version.o vfonts.o xxxpr.o   `ls ../appl/*.o ../nmath/*.o ../unix/*.o  2>/dev/null|grep -v /ext-`  -L/Users/wstein/sage/build/64bit/sage-4.1.2.alpha1/local/lib/gcc/i686-apple-darwin8/4.2.3/x86_64 -L/Users/wstein/sage/build/64bit/sage-4.1.2.alpha1/local/lib/gcc/i686-apple-darwin8/4.2.3 -L/Users/wstein/sage/build/64bit/sage-4.1.2.alpha1/local/lib/gcc -L/usr/local/lib -lgfortran -lgcc_s.10.4  ../extra/zlib/libz.a ../extra/bzip2/libbz2.a ../extra/pcre/libpcre.a  ../extra/intl/libintl.a -liconv  -Wl,-framework -Wl,CoreFoundation -lreadline  -lm
ld: symbol dyld_stub_binding_helper not defined (usually in crt1.o/dylib1.o/bundle1.o)
collect2: ld returned 1 exit status
make[5]: *** [libR.dylib] Error 1
make[4]: *** [R] Error 2
make[3]: *** [R] Error 1
make[2]: *** [R] Error 1
Error building R.
```



---

Comment by was created at 2009-09-21 02:00:44

#6972 fixes everything so R works with 10.6


---

Comment by was created at 2009-09-21 02:00:44

Resolution: duplicate
