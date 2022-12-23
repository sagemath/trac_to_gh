# Issue 7982: sage_fortran on Open Solaris 64 bit is the wrong thing

archive/issues_007982.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  drkirkby\n\nThe fortran-20071120.p9.spkg does not build well on Open Solaris 64 bit. It defaults to 32 bit.\n\nWhat is the way to go?\n\n1) try to build g95 from src\n\nor \n\n2) export SAGE_FORTRAN='path to gfortran'\n   export SAGE_FORTAN_LIB='path to lib/amd64/libfortran.so\n\nI all cases there must be a way to inserting the compiler option -m64\nin sage_fortran.\n\nFor now I went for 2) and edited the file by hand.\n\n\n```\njaap@opensolaris:~/Downloads/sage-4.3.1.rc0$ cat local/bin/sage_fortran \n#!/bin/sh \n\n/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/bin/gfortran -m64 -fPIC $@\n\n```\n\n\n\nJaap\n\nIssue created by migration from https://trac.sagemath.org/ticket/7982\n\n",
    "created_at": "2010-01-18T19:14:43Z",
    "labels": [
        "porting",
        "major",
        "bug"
    ],
    "title": "sage_fortran on Open Solaris 64 bit is the wrong thing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7982",
    "user": "jsp"
}
```
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
jaap@opensolaris:~/Downloads/sage-4.3.1.rc0$ cat local/bin/sage_fortran 
#!/bin/sh 

/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/bin/gfortran -m64 -fPIC $@

```



Jaap

Issue created by migration from https://trac.sagemath.org/ticket/7982





---

archive/issue_comments_069682.json:
```json
{
    "body": "I tried that approach, but it did not work for all packages - I forget what one it is, but at least one will not accept the shell script. \n\nThe way to go is to get into the spkg, and edit that to include $CFLAG64. That will then be set to -m64 (for 64 bit builds with gcc), unset for 32-bit builds with gcc, and whatever else is neeeded for 64-bit builds with other compilers. \n\nEither use a modified version of sage-env, or simply set CFLAG64 to -m64 for now. \n\nUltimately, the packages need to be fixed - not the compiler. \n\nDave",
    "created_at": "2010-01-18T19:34:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7982#issuecomment-69682",
    "user": "drkirkby"
}
```

I tried that approach, but it did not work for all packages - I forget what one it is, but at least one will not accept the shell script. 

The way to go is to get into the spkg, and edit that to include $CFLAG64. That will then be set to -m64 (for 64 bit builds with gcc), unset for 32-bit builds with gcc, and whatever else is neeeded for 64-bit builds with other compilers. 

Either use a modified version of sage-env, or simply set CFLAG64 to -m64 for now. 

Ultimately, the packages need to be fixed - not the compiler. 

Dave



---

archive/issue_comments_069683.json:
```json
{
    "body": "Also, be aware -m64 is not universally used to support the building of 64-bit binaries. It is better to use $CFLAG64, where CFLAG64 will be set in sage-env. \n\nIt is difficult enough porting Sage to Solaris. Let's not make life any more difficult for someone that wants to port it to something else. Hard-coding flags will certainly do that. \n\nDave",
    "created_at": "2010-01-19T01:04:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7982#issuecomment-69683",
    "user": "drkirkby"
}
```

Also, be aware -m64 is not universally used to support the building of 64-bit binaries. It is better to use $CFLAG64, where CFLAG64 will be set in sage-env. 

It is difficult enough porting Sage to Solaris. Let's not make life any more difficult for someone that wants to port it to something else. Hard-coding flags will certainly do that. 

Dave



---

archive/issue_comments_069684.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-21T15:06:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7982#issuecomment-69684",
    "user": "jsp"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_069685.json:
```json
{
    "body": "The new fortran-20100118.spkg made it easy #7485 (g95 is gone) just use gfortran.\n\nSetting SAGE_FORTRAN and SAGE_FORTRAN_LIB to the right files, e.g.\nexport SAGE_FORTAN_LIB='path to lib/amd64/libgfortran.so\n\nThe patched spkg can be found here:\n[http://boxen.math.washington.edu/home/jsp/ports/fortran-20100118.p0.spkg](http://boxen.math.washington.edu/home/jsp/ports/fortran-20100118.p0.spkg)\n\nJaap",
    "created_at": "2010-01-21T15:06:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7982#issuecomment-69685",
    "user": "jsp"
}
```

The new fortran-20100118.spkg made it easy #7485 (g95 is gone) just use gfortran.

Setting SAGE_FORTRAN and SAGE_FORTRAN_LIB to the right files, e.g.
export SAGE_FORTAN_LIB='path to lib/amd64/libgfortran.so

The patched spkg can be found here:
[http://boxen.math.washington.edu/home/jsp/ports/fortran-20100118.p0.spkg](http://boxen.math.washington.edu/home/jsp/ports/fortran-20100118.p0.spkg)

Jaap



---

archive/issue_comments_069686.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-27T16:59:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7982#issuecomment-69686",
    "user": "drkirkby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_069687.json:
```json
{
    "body": "This is not working correctly. It is copying a 32-bit version of the Fortran libary to SAGE_ROOT/local/lib \n\nFirst, I delete any library, and set SAGE_FORTRAN_LIB correctly:\n\n\n```\ndrkirkby@hawk:~/sage-4.3.1$ rm local/lib/libgfortran.so\nrm: local/lib/libgfortran.so: No such file or directory\ndrkirkby@hawk:~/sage-4.3.1$ export SAGE_FORTRAN_LIB=/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/amd64/libgfortran.so\n```\n\n\nNow install the package\n\n```\ndrkirkby@hawk:~/sage-4.3.1$ ./sage -f fortran-20100118.p0\nForce installing fortran-20100118.p0\nCalling sage-spkg on fortran-20100118.p0\n<SNIP>\nSuccessfully installed fortran-20100118.p0\nNow cleaning up tmp files.\nrm: Cannot remove any directory in the path of the current working directory\n/export/home/drkirkby/sage-4.3.1/spkg/build/fortran-20100118.p0\nMaking Sage/Python scripts relocatable...\nMaking script relocatable\nFinished installing fortran-20100118.p0.spkg\n```\n\n\nIt claims to have built, yet there is still a 32-bit library copied. \n\n\n```\ndrkirkby@hawk:~/sage-4.3.1$ file local/lib/libgfortran.so\nlocal/lib/libgfortran.so:\tELF 32-bit LSB dynamic lib 80386 Version 1, dynamically linked, not stripped\n```\n\nThere is no 64-bit version in any of the subdirectories either, though it needs to be put in local/lib. \n\n\n```\ndrkirkby@hawk:~/sage-4.3.1$ file local/lib/64/libgfortran.so\nlocal/lib/64/libgfortran.so:\tcannot open: No such file or directory\ndrkirkby@hawk:~/sage-4.3.1$ file local/lib/amd64/libgfortran.so\nlocal/lib/amd64/libgfortran.so:\tcannot open: No such file or directory\ndrkirkby@hawk:~/sage-4.3.1$ \n```\n\n\nI forget what the command is, but I send it to you the other day, which will allow the correct directory to be determined. It will return one of sparcv9 or amd64, though I would suggest not hard-coding them, as that might change in future. In particular on SPARC. \n\nPS, when you fix this, update SPKG.txt to have the correct trac number (#7982) against the entry. \nDave",
    "created_at": "2010-01-27T16:59:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7982#issuecomment-69687",
    "user": "drkirkby"
}
```

This is not working correctly. It is copying a 32-bit version of the Fortran libary to SAGE_ROOT/local/lib 

First, I delete any library, and set SAGE_FORTRAN_LIB correctly:


```
drkirkby@hawk:~/sage-4.3.1$ rm local/lib/libgfortran.so
rm: local/lib/libgfortran.so: No such file or directory
drkirkby@hawk:~/sage-4.3.1$ export SAGE_FORTRAN_LIB=/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker/lib/amd64/libgfortran.so
```


Now install the package

```
drkirkby@hawk:~/sage-4.3.1$ ./sage -f fortran-20100118.p0
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
drkirkby@hawk:~/sage-4.3.1$ file local/lib/libgfortran.so
local/lib/libgfortran.so:	ELF 32-bit LSB dynamic lib 80386 Version 1, dynamically linked, not stripped
```

There is no 64-bit version in any of the subdirectories either, though it needs to be put in local/lib. 


```
drkirkby@hawk:~/sage-4.3.1$ file local/lib/64/libgfortran.so
local/lib/64/libgfortran.so:	cannot open: No such file or directory
drkirkby@hawk:~/sage-4.3.1$ file local/lib/amd64/libgfortran.so
local/lib/amd64/libgfortran.so:	cannot open: No such file or directory
drkirkby@hawk:~/sage-4.3.1$ 
```


I forget what the command is, but I send it to you the other day, which will allow the correct directory to be determined. It will return one of sparcv9 or amd64, though I would suggest not hard-coding them, as that might change in future. In particular on SPARC. 

PS, when you fix this, update SPKG.txt to have the correct trac number (#7982) against the entry. 
Dave



---

archive/issue_comments_069688.json:
```json
{
    "body": "Replacement with the same name",
    "created_at": "2010-02-22T23:11:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7982#issuecomment-69688",
    "user": "jsp"
}
```

Replacement with the same name



---

archive/issue_comments_069689.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-22T23:23:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7982#issuecomment-69689",
    "user": "jsp"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_069690.json:
```json
{
    "body": "Attachment\n\nMade a new spkg:\n\n[http://boxen.math.washington.edu/home/jsp/ports/fortran-20100118.p0.patch](http://boxen.math.washington.edu/home/jsp/ports/fortran-20100118.p0.patch)\n\n\n\n```\njaap@opensolaris:~/Downloads/sage-4.3.3.alpha1$ cat local/bin/sage_fortran \n#!/bin/sh \n\n/usr/local/gcc-4.4.2/bin/gfortran -m64 -fPIC $@\n\n```\n\n\nAnd on hawk:\n\n\n```\n-bash-3.2$ file local/lib/*fortran*\nlocal/lib/libgfortran.so:       ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped\n-bash-3.2$ \n\n```\n\n\nJaap",
    "created_at": "2010-02-22T23:23:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7982#issuecomment-69690",
    "user": "jsp"
}
```

Attachment

Made a new spkg:

[http://boxen.math.washington.edu/home/jsp/ports/fortran-20100118.p0.patch](http://boxen.math.washington.edu/home/jsp/ports/fortran-20100118.p0.patch)



```
jaap@opensolaris:~/Downloads/sage-4.3.3.alpha1$ cat local/bin/sage_fortran 
#!/bin/sh 

/usr/local/gcc-4.4.2/bin/gfortran -m64 -fPIC $@

```


And on hawk:


```
-bash-3.2$ file local/lib/*fortran*
local/lib/libgfortran.so:       ELF 64-bit LSB dynamic lib AMD64 Version 1, dynamically linked, not stripped
-bash-3.2$ 

```


Jaap



---

archive/issue_comments_069691.json:
```json
{
    "body": "Sorry the spkg is here:\n\n[http://boxen.math.washington.edu/home/jsp/ports/fortran-20100118.p0.spkg](http://boxen.math.washington.edu/home/jsp/ports/fortran-20100118.p0.spkg)\n\nJaap",
    "created_at": "2010-02-22T23:25:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7982#issuecomment-69691",
    "user": "jsp"
}
```

Sorry the spkg is here:

[http://boxen.math.washington.edu/home/jsp/ports/fortran-20100118.p0.spkg](http://boxen.math.washington.edu/home/jsp/ports/fortran-20100118.p0.spkg)

Jaap



---

archive/issue_comments_069692.json:
```json
{
    "body": "Your package works fine, so I would give it positive review. However, since you produced this, sage_fortran has been updated, so I created a new .spkg and put it here\n\n\nhttp://boxen.math.washington.edu/home/kirkby/patches/fortran-20100523.spkg",
    "created_at": "2010-05-23T17:04:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7982#issuecomment-69692",
    "user": "drkirkby"
}
```

Your package works fine, so I would give it positive review. However, since you produced this, sage_fortran has been updated, so I created a new .spkg and put it here


http://boxen.math.washington.edu/home/kirkby/patches/fortran-20100523.spkg



---

archive/issue_comments_069693.json:
```json
{
    "body": "Replying to [comment:8 drkirkby]:\n> Your package works fine, so I would give it positive review. However, since you produced this, sage_fortran has been updated, so I created a new .spkg and put it here\n> \n> \n> http://boxen.math.washington.edu/home/kirkby/patches/fortran-20100523.spkg\n> \n\nOk, as we are both mentioned as author, we need to find a reviewer :)\n\nJaap",
    "created_at": "2010-06-07T16:33:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7982#issuecomment-69693",
    "user": "jsp"
}
```

Replying to [comment:8 drkirkby]:
> Your package works fine, so I would give it positive review. However, since you produced this, sage_fortran has been updated, so I created a new .spkg and put it here
> 
> 
> http://boxen.math.washington.edu/home/kirkby/patches/fortran-20100523.spkg
> 

Ok, as we are both mentioned as author, we need to find a reviewer :)

Jaap



---

archive/issue_comments_069694.json:
```json
{
    "body": "Dave,\n\nThe best way out seems to be: you review my part and I review your changes.\n\nAs you gave my package a positive review, I give your spkg a positive review.\n\nI'll do this right now!\n\nJaap",
    "created_at": "2010-06-12T16:07:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7982#issuecomment-69694",
    "user": "jsp"
}
```

Dave,

The best way out seems to be: you review my part and I review your changes.

As you gave my package a positive review, I give your spkg a positive review.

I'll do this right now!

Jaap



---

archive/issue_comments_069695.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-12T16:07:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7982#issuecomment-69695",
    "user": "jsp"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_069696.json:
```json
{
    "body": "That does seem quite logical in this case. \n\n* You made the change, which I checked and agreed with. \n* I just rebased it, in light of another package. \n* You have checked my changes. \n\nSo all done!\n\ndave",
    "created_at": "2010-06-12T16:18:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7982#issuecomment-69696",
    "user": "drkirkby"
}
```

That does seem quite logical in this case. 

* You made the change, which I checked and agreed with. 
* I just rebased it, in light of another package. 
* You have checked my changes. 

So all done!

dave



---

archive/issue_comments_069697.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-25T15:47:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7982#issuecomment-69697",
    "user": "rlm"
}
```

Resolution: fixed



---

archive/issue_comments_069698.json:
```json
{
    "body": "I noticed a problem with the updated `spkg-install` on t2.  If `SAGE64` is not set to `\"yes\"`, I get\n\n```sh\n$ cat local/bin/sage_fortran\n#!/bin/sh \n\n\n```\n",
    "created_at": "2010-06-26T07:22:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7982#issuecomment-69698",
    "user": "mpatel"
}
```

I noticed a problem with the updated `spkg-install` on t2.  If `SAGE64` is not set to `"yes"`, I get

```sh
$ cat local/bin/sage_fortran
#!/bin/sh 


```




---

archive/issue_comments_069699.json:
```json
{
    "body": "The following seems to work\n\n```python\n    if OS == \"sunos\" and os.environ.get(\"SAGE64\") == \"yes\":\n            f.write(\"%s -m64 -fPIC $@\"%name)\n    else:\n        f.write(\"%s -fPIC $@\"%name)\n\n```\n\nbut I have not tested it with `SAGE64=\"yes\"`.",
    "created_at": "2010-06-26T07:30:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7982#issuecomment-69699",
    "user": "mpatel"
}
```

The following seems to work

```python
    if OS == "sunos" and os.environ.get("SAGE64") == "yes":
            f.write("%s -m64 -fPIC $@"%name)
    else:
        f.write("%s -fPIC $@"%name)

```

but I have not tested it with `SAGE64="yes"`.



---

archive/issue_comments_069700.json:
```json
{
    "body": "That does work with SAGE64=yes. \n\ndrkirkby`@`hawk:~/2/sage-4.5.alpha0$ cat local/bin/sage_fortran\n\n\n```/bin/sh \n\n/usr/local/gcc-4.4.4-multilib/bin/gfortran -m64 -fPIC $@\n```\n\n\nAfter that, if I try to build lapack, the object files it creates are 64-bit\n\n./spkg/build/lapack-20071123.p1/src/SRC/shseqr.o:\tELF 64-bit LSB relocatable AMD64 Version 1",
    "created_at": "2010-06-26T09:25:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7982#issuecomment-69700",
    "user": "drkirkby"
}
```

That does work with SAGE64=yes. 

drkirkby`@`hawk:~/2/sage-4.5.alpha0$ cat local/bin/sage_fortran


```/bin/sh 

/usr/local/gcc-4.4.4-multilib/bin/gfortran -m64 -fPIC $@
```


After that, if I try to build lapack, the object files it creates are 64-bit

./spkg/build/lapack-20071123.p1/src/SRC/shseqr.o:	ELF 64-bit LSB relocatable AMD64 Version 1



---

archive/issue_comments_069701.json:
```json
{
    "body": "Replying to [comment:14 mpatel]:\n> I noticed a problem with the updated `spkg-install` on t2.  If `SAGE64` is not set to `\"yes\"`, I get\n> {{{\n> #!sh\n> $ cat local/bin/sage_fortran\n> #!/bin/sh \n> \n> \n> }}}\n\nI've created #9346 to address this issue, which is quite serious as it totally breaks Sage on Solaris. \n\nDo you want to create the patch and I review it? If you don't have time, I can create it and get someone else to review it. \n\nDave",
    "created_at": "2010-06-26T18:09:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7982#issuecomment-69701",
    "user": "drkirkby"
}
```

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

archive/issue_comments_069702.json:
```json
{
    "body": "I posted a new spkg at #9346 using mpatel's suggestion.",
    "created_at": "2010-06-26T22:43:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7982",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7982#issuecomment-69702",
    "user": "jhpalmieri"
}
```

I posted a new spkg at #9346 using mpatel's suggestion.
