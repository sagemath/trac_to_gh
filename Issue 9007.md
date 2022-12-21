# Issue 9007: iconv not building properly on OpenSolaris

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-05-21 12:37:18

Assignee: drkirkby

CC:  jsp

The following problem is observed with Sage 4.4.2


```
/bin/sh ../libtool --mode=link gcc  -m64 -fvisibility=hidden -o libiconv.la -rpath /export/home/drkirkby/sage-4.4.2/local/lib -version-info 7:0:5 -no-undefined iconv.lo localcharset.lo relocatable.lo  
libtool: link: gcc -shared -Wl,-z -Wl,text -Wl,-h -Wl,libiconv.so.2 -o .libs/libiconv.so.2.5.0  .libs/iconv.o .libs/localcharset.o .libs/relocatable.o   -lc  -m64  
Text relocation remains                 	referenced
    against symbol		    offset	in file
aliases_lookup                      0x1b818   	.libs/iconv.o
aliases_lookup                      0x1b9be   	.libs/iconv.o
aliases_lookup                      0x1bec7   	.libs/iconv.o
aliases_lookup                      0x1c06d   	.libs/iconv.o
aliases_lookup                      0x1c932   	.libs/iconv.o
ld: fatal: relocations remain against allocatable but non-writable sections
collect2: ld returned 1 exit status
make[3]: *** [libiconv.la] Error 1
make[3]: Leaving directory `/export/home/drkirkby/sage-4.4.2/spkg/build/iconv-1.13.1.p2/src/lib'
make[2]: *** [all] Error 2
make[2]: Leaving directory `/export/home/drkirkby/sage-4.4.2/spkg/build/iconv-1.13.1.p2/src'
Error making iconv

real	0m11.098s
user	0m5.345s
sys	0m4.733s
sage: An error occurred while installing iconv-1.13.1.p2
```


I've tried building the source outside of Sage, both 32 and 64-bit, and neither work. A Google shows using the GNU linker will probably solve it, but that is not an acceptable solution, as the GNU linker will create its own set of problems in other packages. It is better that the issue is resolved properly. 


---

Comment by drkirkby created at 2010-05-22 08:05:24

This appears to be a bug in gcc 4.3.4. At the suggestion of the iconv developers, I used another version of gcc. I used 4.4.4 which seems to build this ok. 

This ticket can be closed.


---

Comment by dimpase created at 2010-05-22 08:34:20

Resolution: wontfix
