# Issue 9029: sympow is buiding 32-bit on OpenSolaris x64 even when SAGE64 is set to "yes"

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-05-24 07:34:13

Assignee: drkirkby

CC:  jsp was

When building 'sympow' on OpenSolaris, with SAGE64 set to yes, I see: 



```
**ATTENTION** If you wish build SYMPOW, please ensure beforehand
that the various licenses of your C compiler, linker, assembler, etc.
allow you to create a derived work based on SYMPOW and your C libraries
gcc -O3   -c -o analrank.o analrank.c
gcc -O3   -c -o analytic.o analytic.c
gcc -O3   -c -o compute.o compute.c
gcc -O3   -c -o compute2.o compute2.c
gcc -O3   -c -o fpu.o fpu.c
gcc -O3   -c -o help.o help.c
gcc -O3   -c -o conductors.o conductors.c
gcc -O3   -c -o disk.o disk.c
gcc -O3   -c -o ec_ap.o ec_ap.c
gcc -O3   -c -o ec_ap_bsgs.o ec_ap_bsgs.c
gcc -O3   -c -o ec_ap_large.o ec_ap_large.c
gcc -O3   -c -o eulerfactors.o eulerfactors.c
gcc -O3   -c -o factor.o factor.c
gcc -O3   -c -o generate.o generate.c
gcc -O3   -c -o init_curve.o init_curve.c
gcc -O3   -c -o main.o main.c
gcc -O3   -c -o moddeg.o moddeg.c
gcc -O3   -c -o periods.o periods.c
gcc -O3   -c -o prepare.o prepare.c
gcc -O3   -c -o QD.o QD.c
gcc -O3   -c -o rootno.o rootno.c
gcc -O3   -c -o util.o util.c
mkdir -p datafiles
touch datafiles/param_data
gcc -O3  -o sympow  analrank.o analytic.o compute.o compute2.o fpu.o help.o conductors.o disk.o ec_ap.o ec_ap_bsgs.o ec_ap_large.o eulerfactors.o factor.o generate.o init_curve.o main.o moddeg.o periods.o prepare.o QD.o rootno.o util.o 
```


Then checking one of the generated files, 


```
drkirkby`@`hawk:~/sage-4.4.2$ file ./local/lib/sympow/sympow
./local/lib/sympow/sympow:	ELF 32-bit LSB executable 80386 Version 1 [FPU], dynamically linked, not stripped
```


we see it is indeed a 32-bit file. 

Looking at sympow-1.018.1.p6 source code, I can't see anything that would attempt to build 64-bit on any platform, so I doubt sympow ever built 64-bit on OS X versions where 32-bit was the default. 

Dave


---

Comment by drkirkby created at 2010-05-24 18:22:07

For other OpenSolaris issues, see #9026


---

Comment by drkirkby created at 2010-05-25 02:57:13

Mercurial patch to build 64-bit if SAGE64 is set to "yes"


---

Comment by drkirkby created at 2010-05-25 03:03:10

Changing status from new to needs_review.


---

Attachment

With the attached patch and

http://boxen.math.washington.edu/home/kirkby/patches/sympow-1.018.1.p7.spkg

this now builds 64-bit. 


```
gcc -O3  -m64  -c -o rootno.o rootno.c
gcc -O3  -m64  -c -o util.o util.c
mkdir -p datafiles
touch datafiles/param_data
gcc -O3  -m64 -o sympow  analrank.o analytic.o compute.o compute2.o fpu.o help.o conductors.o disk.o ec_ap.o ec_ap_bsgs.o ec_ap_large.o eulerfactors.o factor.o generate.o init_curve.o main.o moddeg.o periods.o prepare.o QD.o rootno.o util.o 

real	0m4.465s
user	0m4.101s
sys	0m0.301s
Successfully installed sympow-1.018.1.p7
Now cleaning up tmp files.
rm: Cannot remove any directory in the path of the current working directory
/export/home/drkirkby/sage-4.4.2/spkg/build/sympow-1.018.1.p7
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing sympow-1.018.1.p7.spkg
drkirkby`@`hawk:~/sage-4.4.2$ file ./local/lib/sympow/sympow
./local/lib/sympow/sympow:	ELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped, no debugging information available
```


The binary is now 64-bit, not 32-bit as before. 


```
drkirkby`@`hawk:~/sage-4.4.2$ file ./local/lib/sympow/sympow
./local/lib/sympow/sympow:	ELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped, no debugging information available
```



---

Comment by jsp created at 2010-06-10 16:08:22

Changing status from needs_review to positive_review.


---

Comment by jsp created at 2010-06-10 16:08:22

Looks ok for me on Open Solaris:



```
-bash-4.0$ file local/lib/sympow/sympow 
local/lib/sympow/sympow:        ELF 64-bit LSB executable AMD64 Version 1, dynamically linked, not stripped, no debugging information available
-bash-4.0$ 

```


Positive review.

Jaap


---

Comment by mhansen created at 2010-06-11 21:05:42

Resolution: fixed
