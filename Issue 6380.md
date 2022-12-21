# Issue 6380: [with patch, needs review] Allow NTL to build on Solaris with Sun or GNU linker

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-06-21 21:59:34

Assignee: drkirkby

Keywords: solaris ntl makefile GNUism

Although the ntl-5.4.2.p7 package would build on Solaris 10 with gcc 4.4.0 if the gcc was configured to use the GNU linker from binutils, the package would not build with the gcc if the compiler was configured to use the Sun linker, with the following options:

--with-ld=/usr/ccs/bin/ld --without-gnu-ld 

The part of the makefile executed when building a shared library would fail if the Sun linker was used. The makefile specified the same output filename twice, but in a way the Sun linker would not tolerate. 

This patch simply removes a very small bit of code (just "-Wl,-soname,lib`cat DIRNAME`.so "), which allows NTL to build properly, irrespective of the linker that is being used. 

Please see 

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/ntl/




---

Comment by was created at 2009-06-21 23:00:11

Positive review, though I didn't test it with the Sun linker, it looks very sensible and doesn't break things.  

An spkg with the changes checked into the repo and a typo fixed is now here:

  http://sage.math.washington.edu/home/wstein/patches/ntl-5.4.2.p8.spkg


---

Comment by rlm created at 2009-07-02 23:30:29

Unfortunately, another ticket already got "p8", and the changes here need to be reapplied to that spkg.


---

Comment by rlm created at 2009-07-02 23:31:24

Replying to [comment:2 rlm]:
> Unfortunately, another ticket already got "p8", and the changes here need to be reapplied to that spkg.

That spkg is available here:

http://sage.math.washington.edu/home/rlmill/ntl-5.4.2.p8.spkg


---

Comment by drkirkby created at 2009-07-09 21:44:35

OK, I've made the changes. 

Please see: 

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/ntl-5.4.2.p9/ (different directory to last one)

I created a patchfile which shows the differences from the last copy of 'mfile' otherwise the patch would be huge and uncomprehsible, as mfile has been changed so many times. There is actually a patch in the 'patches' directory. 

I just noticed I probably put the original and new files in the wrong order, as it looks like I've added stuff to the 'mfile' not taken it away. I have in fact just *removed*   -Wl,-soname,libcat DIRNAME.so

Formally the line was:
	$(LINK_CXX) -fPIC -shared -Wl,-soname,lib`cat DIRNAME`.so -o lib`cat DIRNAME`.so $(OBJ) $(GMP_LIBDIR)

now it is 
	$(LINK_CXX) -fPIC -shared -o lib`cat DIRNAME`.so $(OBJ) $(GMP_LIBDIR) $(GMP_LIB)


---

Comment by mvngu created at 2009-07-15 16:57:52

Replying to [comment:4 drkirkby]:
> OK, I've made the changes. 
> 
> Please see: 
> 
> http://sage.math.washington.edu/home/kirkby/Solaris-fixes/ntl-5.4.2.p9/ (different directory to last one)
The NTL spkg above contains some junk and changes were not checked in. I've checked in changes in David Kirkby's name. The updated spkg is available at

http://sage.math.washington.edu/home/mvngu/patch/ntl-5.4.2.p9.spkg


---

Comment by mvngu created at 2009-07-15 17:58:45

After installing the NTL package at

http://sage.math.washington.edu/home/mvngu/patch/ntl-5.4.2.p9.spkg

and running doctests on all of the Sage library, I got this:

```
The following tests failed:

        sage -t -long devel/sage-main/sage/modular/hecke/morphism.py # 0 doctests failed
        sage -t -long devel/sage-main/sage/categories/morphism.pyx # 0 doctests failed
```

The funny thing is that it reports doctest failures, with "0 doctests failed". I reinstalled `ntl-5.4.2.p8.spkg` and ran all doctests again, and they passed. I then installed *ntl-5.4.2.p9.spkg* a second time, ran all doctests, and they now passed without any of those weird "0 doctests failed".


---

Comment by mvngu created at 2009-07-16 10:26:25

Just to let people know, this has been merged in sage-4.1.1-alpha0. I can't close this ticket because I don't have the privilege to do so. Sorry, folks :-(


---

Comment by mvngu created at 2009-07-16 21:27:54

Resolution: fixed
