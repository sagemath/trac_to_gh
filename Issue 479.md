# Issue 479: linbox-20070814.spkg abuses [CPP|CXX|C]FLAGS in spkg-install

Issue created by migration from https://trac.sagemath.org/ticket/479

Original creator: mabshoff

Original creation time: 2007-08-22 19:36:34

Assignee: mabshoff

CC:  cpernet drkirkby

Keywords: LinBox

Hello,

The current LinBox package in Sage 2.8.2 has the following assignments in spkg-install


```
CFLAGS="$CFLAGS -fPIC -I\"$SAGE_LOCAL/include\" -I\"$SAGE_LOCAL/include/linbox\"-L\"$SAGE_LOCAL/lib\""
CXXFLAGS="$CXXFLAGS -fPIC -I\"$SAGE_LOCAL/include\" -I\"$SAGE_LOCAL/include/linbox\"  -L\"$SAGE_LOCAL/lib\""
CPPFLAGS="$CPPFLAGS  -I\"$SAGE_LOCAL/include/linbox\" -I\"$SAGE_LOCAL\"/include"
```

but uses the configure with the following options:

```
./configure --prefix="$SAGE_LOCAL" --with-givaro="$SAGE_LOCAL" --with-gmp="$SAGE_LOCAL" --with-ntl="$SAGE_LOCAL" $OPS --with-blas="$LINBOX_BLAS"
```

This is due to a bug in LinBox where for exmaple GMP_CFLAGS is not propagated down into the Makefiles (via Makefile.am). I have fixed this for the GMP and I assume that it is the same fix for NTL and Givaro. The GMP fix already made it into LinBox-20070814.spkg and I did verify on my systems that the right gmp selected during configure is also linked against. Once I have made the fixes for NTL and Givaro I will push those fixes toward LinBox upstream.

Cheers,

Michael

I 


---

Comment by mabshoff created at 2007-08-22 19:36:56

Changing status from new to assigned.


---

Comment by malb created at 2008-08-17 00:04:40

Just to confirm that this bug is still around, CCing Clément :-)


---

Comment by mabshoff created at 2008-09-26 09:06:03

Well, this should be trivial to fix. Any takers?

Cheers,

Michael


---

Comment by kcrisman created at 2009-12-30 04:40:45

Has this one been addressed in the meantime, due to Kirkby's many helpful flag comments?


---

Comment by drkirkby created at 2009-12-30 16:06:02

linbox appears to have several errors. 

 * #7058 
 * -m64  (a GNUism in itself) hard coded on only OS X, so it will not build 64-bit with Solaris. 
 * The issues you mention here. 
 * The fact -fPIC is a GNU specific flag. 

I'm a bit reluctant to go around editing any more spkg-install files, until we have in place a better system for dealing with the 64-bit issues which is not dependent on a particular platform or compiler. This spkg-install makes the assumption the only compiler is gcc (not true) and the only operating system on which one might want to force a 64-bit build is OS X (again not true). It was rather short-sighted the way this SAGE64 issue was handled. 

Once there is a way of handling this better, I'll revise this. #7505 is needing review and will allow the compiler to be determined. Later I will add an updated version of sage-env, which will set the flags globally. But it needs #7505 to be integrated first. 

Dave


---

Comment by mmezzarobba created at 2015-04-13 14:15:37

Changing status from new to needs_review.


---

Comment by mmezzarobba created at 2015-04-13 14:15:37

Fixed in #12762?


---

Comment by aapitzsch created at 2015-05-19 18:01:16

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-06-19 08:37:53

Resolution: fixed
