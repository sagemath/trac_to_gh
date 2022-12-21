# Issue 5289: gdmodule fails to build on Linux/Solaris systems without a system wide libpng

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-02-17 02:16:24

Assignee: mabshoff

This is fallout from the libpng -> libpng12 transition and trivial to fix:

```
gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -DHAVE_LIBGD -DHAVE_LIBZ -DHAVE_LIBFREETYPE -DHAVE_LIBPNG -I/home/mabshoff/build-3.3.rc1/sage-3.3.rc1-cicero-gcc-433/local/include -I/usr/include -I/home/mabshoff/build-3.3.rc1/sage-3.3.rc1-cicero-gcc-433/local/include/python2.5 -c _gdmodule.c -o build/temp.linux-i686-2.5/_gdmodule.o
_gdmodule.c:152: warning: function declaration isn’t a prototype
_gdmodule.c:169: warning: function declaration isn’t a prototype
_gdmodule.c: In function ‘image_string’:
_gdmodule.c:993: warning: pointer targets in passing argument 5 of ‘gdImageString’ differ in signedness
_gdmodule.c: In function ‘image_string16’:
_gdmodule.c:1008: warning: passing argument 5 of ‘gdImageString16’ from incompatible pointer type
_gdmodule.c: In function ‘image_stringup’:
_gdmodule.c:1022: warning: pointer targets in passing argument 5 of ‘gdImageStringUp’ differ in signedness
_gdmodule.c: In function ‘image_stringup16’:
_gdmodule.c:1037: warning: passing argument 5 of ‘gdImageStringUp16’ from incompatible pointer type
gcc -pthread -shared build/temp.linux-i686-2.5/_gdmodule.o -L/home/mabshoff/build-3.3.rc1/sage-3.3.rc1-cicero-gcc-433/local/lib -L/usr/lib -lgd -lz -lfreetype -lpng -o build/lib.linux-i686-2.5/_gd.so
/usr/local/binutils-2.19.1/x86-Linux-fc-gcc-4.3.3/bin/ld: cannot find -lpng
collect2: ld returned 1 exit status
error: command 'gcc' failed with exit status 1
Failure to build gdmodule
```



---

Comment by mabshoff created at 2009-02-17 02:16:34

Changing status from new to assigned.


---

Attachment

This is the fix I am applying inside the spkg - it will make it easier for the reviewer


---

Comment by mabshoff created at 2009-02-17 07:24:44

The spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.3/rc2/gdmodule-0.56.p5.spkg

Fixes the issue and also cleans it up a great deal.

Cheers,

Michael


---

Comment by mhansen created at 2009-02-17 13:56:15

Seems reasonable to me.


---

Comment by mabshoff created at 2009-02-17 18:52:02

Resolution: fixed


---

Comment by mabshoff created at 2009-02-17 18:52:02

Merged in Sage 3.3.rc2.

Cheers,

Michael
