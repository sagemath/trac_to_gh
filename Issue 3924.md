# Issue 3924: making sage on os x build, when python is built as a framework

Issue created by migration from https://trac.sagemath.org/ticket/3924

Original creator: dphilp

Original creation time: 2008-08-22 01:38:43

Assignee: jkantor

CC:  dphilp prabhu cswiercz

Keywords: framework

I'm trying to build sage on mac with a shareable python library.  The current version, being built without the --enable-framework option, cannot be linked to other libraries because of the environ variable.  I think getting this working would be useful, and I would like eventually to see it the default build on OS X.

The following recipe works, though it is clearly a defective approach:

1. build vanilla sage from source 

2. edit the spkg/standard/python-2.5....spkg/spkg-install file to include the --enable-framework=SAGE_ROOT/local/Frameworks

3. rebuild sage.  This creates SAGE_ROOT/Frameworks/Python.framework

4. all doctests pass, and I can link to libpython from boost python

Ideally, the following steps would work:

1. edit the spkg/standard/python-2.5....spkg/spkg-install file to include the --enable-framework= SAGE_ROOT/local/Frameworks

2. build sage.

It doesn't work so simply.  I've managed to help it along a few steps, but am stuck with cvxopt

1. The build of mercurial crashes.  When it crashes, create two symlinks:

1a. local/lib/python2.5 
---> local/Frameworks/Python.framework/Versions/Current/lib/python2.5/

1b. local/include/python2.5 
---> local/Frameworks/Python.framework/Versions/Current/include/python2.5/

1c. Restart make

2. The build of the sage package crashes, with a similar error.  

2a. Delete the busted symlink at 
local/Frameworks/Python.framework/Versions/Current/lib/python2.5/site-packages/sage

2b. Create a symlink:
local/Frameworks/Python.framework/Versions/Current/lib/python2.5/site-packages/sage
--->devel/sage/build/sage

2c. Delete half-built files, restart make.

3. The build of cvxopt crashes, with a duplicate symbol error.  I'm not in a position to debug this one.

Any attention appreciated!  For my part, I can muddle along with the duplicate builds but I would like to get this working.

D


---

Comment by dphilp created at 2008-08-25 02:02:05

The duplicate symbol error is this:
ld: duplicate symbol _matrix_tp in build/temp.macosx-10.3-i386-2.5/C/dense.o and build/temp.macosx-10.3-i386-2.5/C/base.o

It is the first error, until then, gcc happily chugs along.


---

Comment by dphilp created at 2008-08-25 02:18:21

This is the command that pruduced the error.

gcc -bundle -undefined dynamic_lookup build/temp.macosx-10.3-i386-2.5/C/base.o build/temp.macosx-10.3-i386-2.5/C/dense.o build/temp.macosx-10.3-i386-2.5/C/sparse.o -L/Users/dphilp/sage-3.0.3fo/local/lib -L/Users/dphilp/sage-3.0.3fo/local/lib/gcc-lib/i386-apple-darwin8.10.3/4.0.3/ -lm -llapack -lblas -lf95 -o build/lib.macosx-10.3-i386-2.5/cvxopt/base.so


---

Comment by dphilp created at 2008-08-25 03:00:40

Can crash tthrough the cvxopt errors by adding extern declarations in some of the source files.

I think this is a complete list:

in src/C/base.c, 

```
PyTypeObject matrix_tp ;
PyTypeObject spmatrix_tp ;
}}} 
both get an extern.

In dense.c, `PyTypeObject spmatrix_tp ;` gets an extern.

In dense.c and sparse.c, `PyObject *base_mod;` gets an extern.


---

Comment by dphilp created at 2008-08-25 04:33:50

It builds and sage works with two warnings and some dsage badness:

```
WARNING: Readline services not available on this platform.
WARNING: The auto-indent feature requires the readline library
```


failed doctests:

```
sage -t  devel/sage/sage/dsage/tests/testdoc.py             
**********************************************************************
File "/Users/dphilp/sage-3.0.3fo/tmp/testdoc.py", line 14:
    sage: a
Expected:
    5
Got:
    No output.
**********************************************************************
File "/Users/dphilp/sage-3.0.3fo/tmp/testdoc.py", line 33:
    sage: j
Expected:
    10
Got:
    No output.
**********************************************************************
```



---

Comment by dphilp created at 2008-08-25 06:55:48

Readline fix.  Python's spkg needs a couple of lines:

```
LDFLAGS="-L/Users/dphilp/sage-3.0.3fo/local/lib $LDFLAGS"
export LDFLAGS

CPPFLAGS="-I/Users/dphilp/sage-3.0.3fo/local/include $CPPFLAGS"
export CPPFLAGS
```



---

Comment by dphilp created at 2008-08-25 07:13:52

The last has been committed as a general fix to python's build by mabshoff.


---

Comment by dphilp created at 2008-08-25 07:15:05

And that also fixes dsage's doctest trouble.


---

Comment by dphilp created at 2008-08-25 12:33:54

Patches required to get this working.  (Sorry I don't know how to do the pretty red/green bizzo.)
## python.spkg/spkg-install:

```
49a50,56
> # (OS X only)  If SAGE_PYTHON_FRAMEWORK is set, compile sage as a framework
> if [ `uname` = "Darwin" -a $SAGE_PYTHON_FRAMEWORK ] ; then
>     echo "Building python as a framework with --enable-framework=$SAGE_LOCAL/Frameworks"
>     FRAMEWORK_BUILD_OPTION="--enable-framework=$SAGE_LOCAL/Frameworks"
> fi
> 
> 
74c81,82
<         --with-gcc="gcc -m64" --disable-toolbox-glue
---
>         --with-gcc="gcc -m64" --disable-toolbox-glue \
>         $FRAMEWORK_BUILD_OPTION
80c88,89
<         ./configure $EXTRAFLAGS --prefix="$SAGE_LOCAL" --without-libpng --enable-unicode=ucs4
---
>         ./configure $EXTRAFLAGS --prefix="$SAGE_LOCAL" --without-libpng --enable-unicode=ucs4 \
>         $FRAMEWORK_BUILD_OPTION
109a119,132
> # (OS X only)  If SAGE_PYTHON_FRAMEWORK the symlink created above will be left dangling
> if [ $SAGE_PYTHON_FRAMEWORK ] ; then
>     ln -s python2.5 ../Frameworks/Python.framework/Versions/Current/lib/python2.5
> fi
> 
> 
> cd $SAGE_LOCAL/include
> 
> # (OS X only)  If SAGE_PYTHON_FRAMEWORK, we need to point to the framework headers
> if [ $SAGE_PYTHON_FRAMEWORK ] ; then
>     ln -s python2.5 ../Frameworks/Python.framework/Versions/Current/include/python2.5
> fi
> 
```


## sage.spkg/sagebuild.py:

```
509c509,514
<     safesymlink('../../../../devel/sage/build/sage','local/lib/python/site-packages/sage')
---
>     if env.options['SAGE_PYTHON_FRAMEWORK'] != 'yes' :
>         safesymlink('../../../../devel/sage/build/sage','local/lib/python/site-packages/sage')
>     else:
>         safesymlink(
>             '../../../../../../devel/sage/build/sage',
>             'local/Frameworks/Python.framework/Versions/Current/lib/python/site-packages/sage')
```


And a bunch of edits to cvxopt, which are apparently fixed in version 1.0.


---

Comment by dphilp created at 2008-08-26 01:23:21

Slightly better in python.spkg/spkg-install:

```
> # (OS X only)  If SAGE_PYTHON_FRAMEWORK is set, compile sage as a framework
> if [ `uname` = "Darwin" -a "$SAGE_PYTHON_FRAMEWORK" = "yes" ] ; then
>     echo "Building python as a framework with --enable-framework=$SAGE_LOCAL/Frameworks"
>     FRAMEWORK_BUILD_OPTION="--enable-framework=$SAGE_LOCAL/Frameworks"
> fi
```



---

Comment by dphilp created at 2008-08-26 02:00:06

` if [ "$SAGE_PYTHON_FRAMEWORK" = "yes" ] ; then ` throughout


---

Comment by dphilp created at 2008-08-26 04:27:54

correction to: ` sage.spkg/sagebuild.py `

```
>     if os.environ.get('SAGE_PYTHON_FRAMEWORK') != 'yes' :
>         safesymlink('../../../../devel/sage/build/sage','local/lib/python/site-packages/sage')
>     else:
>         safesymlink(
>             '../../../../../../devel/sage/build/sage',
>             'local/Frameworks/Python.framework/Versions/Current/lib/python/site-packages/sage')
```



---

Comment by dphilp created at 2008-08-26 05:06:05

I suck.  ` python.spkg/spkg-install `


```
> # (OS X only)  If SAGE_PYTHON_FRAMEWORK the symlink created above will be left dangling
> if [ $SAGE_PYTHON_FRAMEWORK ] ; then
>     ln -s python2.5 ../Frameworks/Python.framework/Versions/Current/lib/python2.5
> fi
> 
> 
> cd $SAGE_LOCAL/include
> 
> # (OS X only)  If SAGE_PYTHON_FRAMEWORK, we need to point to the framework headers
> if [ $SAGE_PYTHON_FRAMEWORK ] ; then
>     ln -s python2.5 ../Frameworks/Python.framework/Versions/Current/include/python2.5
> fi
```



---

Attachment


---

Attachment

This was the original mess of a ticket description:

I'm trying to build sage on mac with a shareable python library.  The current version, being built without the --enable-framework option, cannot be linked to other libraries because of the environ variable.  I think getting this working would be useful, and I would like eventually to see it the default build on OS X.

The following recipe works, though it is clearly a defective approach:

1. build vanilla sage from source 

2. edit the spkg/standard/python-2.5....spkg/spkg-install file to include the --enable-framework=SAGE_ROOT/local/Frameworks

3. rebuild sage.  This creates SAGE_ROOT/Frameworks/Python.framework

4. all doctests pass, and I can link to libpython from boost python

Ideally, the following steps would work:

1. edit the spkg/standard/python-2.5....spkg/spkg-install file to include the --enable-framework= SAGE_ROOT/local/Frameworks

2. build sage.

It doesn't work so simply.  I've managed to help it along a few steps, but am stuck with cvxopt

1. The build of mercurial crashes.  When it crashes, create two symlinks:

1a. local/lib/python2.5 
---> local/Frameworks/Python.framework/Versions/Current/lib/python2.5/

1b. local/include/python2.5 
---> local/Frameworks/Python.framework/Versions/Current/include/python2.5/

1c. Restart make

2. The build of the sage package crashes, with a similar error.  

2a. Delete the busted symlink at 
local/Frameworks/Python.framework/Versions/Current/lib/python2.5/site-packages/sage

2b. Create a symlink:
local/Frameworks/Python.framework/Versions/Current/lib/python2.5/site-packages/sage
--->devel/sage/build/sage

2c. Delete half-built files, restart make.

3. The build of cvxopt crashes, with a duplicate symbol error.  I'm not in a position to debug this one.

Any attention appreciated!  For my part, I can muddle along with the duplicate builds but I would like to get this working.

D


---

Comment by mhampton created at 2009-10-29 19:11:55

Since we have upgraded to python-2.6, I think this needs to be rebased at least.  I am interested in testing an updated version.


---

Comment by mhampton created at 2009-10-29 19:11:55

Changing status from needs_review to needs_work.


---

Comment by bascorp2 created at 2010-05-26 08:41:30

[восточные танцы](http://art-dance.com.ua/)
