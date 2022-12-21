# Issue 7982: sage_fortran on Open Solaris 64 bit is the wrong thing

Issue created by migration from Trac.

Original creator: jsp

Original creation time: 2010-01-18 19:14:43

Assignee: drkirkby

CC:  drkirkby

The fortran-20071120.p9.spkg does not build well on Open Solaris 64 bit. It defaults to 32 bit.

What is the way to go?

1) try to build g95 from src

or 

2) export SAGE_FORTRAN='path to gfortran'
   export SAGE_FORTAN_LIB='path to lib/amd64/libfortran.so

I all cases there must be a way to inserting the compiler option -m64
in sage_fortran.

For now I went for 2) and edited the file by hand.


```
jaap`@`opensolaris:~/Downloads/sage-4.3.1.rc0$ cat local/bin/sage_fortran 
#!/bin/sh 

/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/bin/gfortran -m64 -fPIC $`@`

```



Jaap


---

Comment by drkirkby created at 2010-01-18 19:34:12

I tried that approach, but it did not work for all packages - I forget what one it is, but at least one will not accept the shell script. 

The way to go is to get into the spkg, and edit that to include $CFLAG64. That will then be set to -m64 (for 64 bit builds with gcc), unset for 32-bit builds with gcc, and whatever else is neeeded for 64-bit builds with other compilers. 

Either use a modified version of sage-env, or simply set CFLAG64 to -m64 for now. 

Ultimately, the packages need to be fixed - not the compiler. 

Dave


---

Comment by drkirkby created at 2010-01-19 01:04:37

Also, be aware -m64 is not universally used to support the building of 64-bit binaries. It is better to use $CFLAG64, where CFLAG64 will be set in sage-env. 

It is difficult enough porting Sage to Solaris. Let's not make life any more difficult for someone that wants to port it to something else. Hard-coding flags will certainly do that. 

Dave


---

Comment by jsp created at 2010-01-21 15:06:45

Changing status from new to needs_review.


---

Comment by jsp created at 2010-01-21 15:06:45

The new fortran-20100118.spkg made it easy #7485 (g95 is gone) just use gfortran.

Setting SAGE_FORTRAN and SAGE_FORTRAN_LIB to the right files, e.g.
export SAGE_FORTAN_LIB='path to lib/amd64/libgfortran.so

The patched spkg can be found here:
[http://boxen.math.washington.edu/home/jsp/ports/fortran-20100118.p0.spkg](http://boxen.math.washington.edu/home/jsp/ports/fortran-20100118.p0.spkg)

Jaap


---

Comment by drkirkby created at 2010-01-27 16:59:53

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-01-27 16:59:53

This is not working correctly. It is copying a 32-bit version of the Fortran libary to SAGE_ROOT/local/lib 

First, I delete any library, and set SAGE_FORTRAN_LIB correctly:


```
drkirkby`@`hawk:~/sage-4.3.1$ rm local/lib/libgfortran.so
rm: local/lib/libgfortran.so: No such file or directory
drkirkby`@`hawk:~/sage-4.3.1$ export SAGE_FORTRAN_LIB=/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/amd64/libgfortran.so
```


Now install the package

```
drkirkby`@`hawk:~/sage-4.3.1$ ./sage -f fortran-20100118.p0
Force installing fortran-20100118.p0
Calling sage-spkg on fortran-20100118.p0
<SNIP>
Successfully installed fortran-20100118.p0
Now cleaning up tmp files.
rm: Cannot remove any directory in the path of the current working directory
/export/home/drkirkby/sage-4.3.1/spkg/build/fortran-20100118.p0
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing fortran-20100118.p0.spkg
```


It claims to have built, yet there is still a 32-bit library copied. 


```
drkirkby`@`hawk:~/sage-4.3.1$ file local/lib/libgfortran.so
local/lib/libgfortran.so:	ELF 32-bit LSB dynamic lib 80386 Version 1, dynamically linked, not stripped
```

There is no 64-bit version in any of the subdirectories either, though it needs to be put in local/lib. 


```
drkirkby`@`hawk:~/sage-4.3.1$ file local/lib/64/libgfortran.so
local/lib/64/libgfortran.so:	cannot open: No such file or directory
drkirkby`@`hawk:~/sage-4.3.1$ file local/lib/amd64/libgfortran.so
local/lib/amd64/libgfortran.so:	cannot open: No such file or directory
drkirkby`@`hawk:~/sage-4.3.1$ 
```


I forget what the command is, but I send it to you the other day, which will allow the correct directory to be determined. It will return one of sparcv9 or amd64, though I would suggest not hard-coding them, as that might change in future. In particular on SPARC. 

PS, when you fix this, update SPKG.txt to have the correct trac number (#7982) against the entry. 
Dave


---

Comment by jsp created at 2010-02-22 23:11:31

Replacement with the same name


---

Comment by jsp created at 2010-02-22 23:23:30

Changing status from needs_work to needs_review.


---

Attachment

Made a new spkg:

[http://boxen.math.washington.edu/home/jsp/ports/fortran-20100118.p0.patch](http://boxen.math.washington.edu/home/jsp/ports/fortran-20100118.p0.patch)



```
jaap`@`opensolaris:~/Downloads/sage-4.3.3.alpha1$ cat local/bin/sage_fortran 
#!/bin/sh 

/usr/local/gcc-4.4.2/bin/gfortran -m64 -fPIC $`@`

```


And on hawk:


```
-bash-3.2$ file local/lib/*fortran*
local/lib/libgfortran.so:       ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
-bash-3.2$ 

```


Jaap


---

Comment by jsp created at 2010-02-22 23:25:45

Sorry the spkg is here:

[http://boxen.math.washington.edu/home/jsp/ports/fortran-20100118.p0.spkg](http://boxen.math.washington.edu/home/jsp/ports/fortran-20100118.p0.spkg)

Jaap


---

Comment by drkirkby created at 2010-05-23 17:04:55

Your package works fine, so I would give it positive review. However, since you produced this, sage_fortran has been updated, so I created a new .spkg and put it here


http://boxen.math.washington.edu/home/kirkby/patches/fortran-20100523.spkg


---

Comment by jsp created at 2010-06-07 16:33:11

Replying to [comment:8 drkirkby]:
> Your package works fine, so I would give it positive review. However, since you produced this, sage_fortran has been updated, so I created a new .spkg and put it here
> 
> 
> http://boxen.math.washington.edu/home/kirkby/patches/fortran-20100523.spkg
> 

Ok, as we are both mentioned as author, we need to find a reviewer :)

Jaap


---

Comment by jsp created at 2010-06-12 16:07:50

Dave,

The best way out seems to be: you review my part and I review your changes.

As you gave my package a positive review, I give your spkg a positive review.

I'll do this right now!

Jaap


---

Comment by jsp created at 2010-06-12 16:07:50

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-06-12 16:18:59

That does seem quite logical in this case. 

 * You made the change, which I checked and agreed with. 
 * I just rebased it, in light of another package. 
 * You have checked my changes. 

So all done!

dave


---

Comment by rlm created at 2010-06-25 15:47:50

Resolution: fixed


---

Comment by mpatel created at 2010-06-26 07:22:10

I noticed a problem with the updated `spkg-install` on t2.  If `SAGE64` is not set to `"yes"`, I get

```sh
$ cat local/bin/sage_fortran
#!/bin/sh 


```



---

Comment by mpatel created at 2010-06-26 07:30:17

The following seems to work

```python
    if OS == "sunos" and os.environ.get("SAGE64") == "yes":
            f.write("%s -m64 -fPIC $`@`"%name)
    else:
        f.write("%s -fPIC $`@`"%name)

```

but I have not tested it with `SAGE64="yes"`.


---

Comment by drkirkby created at 2010-06-26 09:25:31

That does work with SAGE64=yes. 

drkirkby`@`hawk:~/2/sage-4.5.alpha0$ cat local/bin/sage_fortran

{{{#!/bin/sh 

/usr/local/gcc-4.4.4-multilib/bin/gfortran -m64 -fPIC $`@`
```


After that, if I try to build lapack, the object files it creates are 64-bit

./spkg/build/lapack-20071123.p1/src/SRC/shseqr.o:	ELF 64-bit LSB relocatable AMD64 Version 1


---

Comment by drkirkby created at 2010-06-26 18:09:31

Replying to [comment:14 mpatel]:
> I noticed a problem with the updated `spkg-install` on t2.  If `SAGE64` is not set to `"yes"`, I get
> {{{
> #!sh
> $ cat local/bin/sage_fortran
> #!/bin/sh 
> 
> 
> }}}

I've created #9346 to address this issue, which is quite serious as it totally breaks Sage on Solaris. 

Do you want to create the patch and I review it? If you don't have time, I can create it and get someone else to review it. 

Dave


---

Comment by jhpalmieri created at 2010-06-26 22:43:34

I posted a new spkg at #9346 using mpatel's suggestion.
