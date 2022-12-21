# Issue 4865: dvipng optional spkg fails to build on sage.math (our main devel machine)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-12-24 05:18:46

Assignee: mabshoff

CC:  dimpase


```
sage: install_package('dvipng-1.8')
...
gcc -I/usr/local/sage/local/include/freetype2 -I/usr/local/sage/local/include -I/usr/local/sage/local/include -Wall -I.  -c -o vf.o vf.c
gcc -I/usr/local/sage/local/include/freetype2 -I/usr/local/sage/local/include -I/usr/local/sage/local/include -Wall -I.  -c -o ft.o ft.c
gcc -I/usr/local/sage/local/include/freetype2 -I/usr/local/sage/local/include -I/usr/local/sage/local/include -Wall -I.  -c -o enc.o enc.c
gcc -I/usr/local/sage/local/include/freetype2 -I/usr/local/sage/local/include -I/usr/local/sage/local/include -Wall -I.  -c -o fontmap.o fontmap.c
gcc -I/usr/local/sage/local/include/freetype2 -I/usr/local/sage/local/include -I/usr/local/sage/local/include -Wall -I.  -c -o tfm.o tfm.c
gcc -L/usr/local/sage/local/lib dvipng.o color.o draw.o dvi.o font.o misc.o pk.o set.o special.o papersiz.o ppagelist.o vf.o  ft.o enc.o fontmap.o tfm.o -o dvipng -L/usr/local/sage/local/lib -Wl,--rpath -Wl,/usr/local/sage/local/lib -lfreetype -lkpathsea -lgd -lpng -lz -lm  
special.o: In function `SetSpecial':
special.c:(.text+0x13ac): undefined reference to `gdImageCreateFromJpeg'
collect2: ld returned 1 exit status
make: *** [dvipng] Error 1
Error building dvipng.

real	0m5.119s
user	0m2.720s
sys	0m2.300s
sage: An error occurred while installing dvipng-1.8
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /usr/local/sage/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/usr/local/sage/spkg/build/dvipng-1.8 and type 'make'.
Instead type "/usr/local/sage/sage -sh"
in order to set all environment variables correctly, then cd to
/usr/local/sage/spkg/build/dvipng-1.8
(When you are done debugging, you can type "exit" to leave the
subshell.)
```


I installed  libkpathsea-dev in order to get as far as the above:

```
root`@`sage:/usr/local/sage# apt-get install libkpathsea-dev
```



---

Comment by mabshoff created at 2009-01-12 02:28:54

Is this still relevant since we removed the dvipng spkg?

Cheers,

Michael


---

Comment by mkoeppe created at 2020-08-17 16:38:58

Outdated spkg or build system ticket, should be closed


---

Comment by mkoeppe created at 2020-08-17 16:38:58

Changing status from new to needs_review.


---

Comment by slelievre created at 2020-08-22 07:12:15

Resolution: invalid
