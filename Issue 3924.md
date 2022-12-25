# Issue 3924: making sage on os x build, when python is built as a framework

archive/issues_003924.json:
```json
{
    "body": "Assignee: jkantor\n\nCC:  dphilp prabhu @cswiercz\n\nKeywords: framework\n\nI'm trying to build sage on mac with a shareable python library.  The current version, being built without the --enable-framework option, cannot be linked to other libraries because of the environ variable.  I think getting this working would be useful, and I would like eventually to see it the default build on OS X.\n\nThe following recipe works, though it is clearly a defective approach:\n\n1. build vanilla sage from source \n\n2. edit the spkg/standard/python-2.5....spkg/spkg-install file to include the --enable-framework=SAGE_ROOT/local/Frameworks\n\n3. rebuild sage.  This creates SAGE_ROOT/Frameworks/Python.framework\n\n4. all doctests pass, and I can link to libpython from boost python\n\nIdeally, the following steps would work:\n\n1. edit the spkg/standard/python-2.5....spkg/spkg-install file to include the --enable-framework= SAGE_ROOT/local/Frameworks\n\n2. build sage.\n\nIt doesn't work so simply.  I've managed to help it along a few steps, but am stuck with cvxopt\n\n1. The build of mercurial crashes.  When it crashes, create two symlinks:\n\n2a. local/lib/python2.5 \n---> local/Frameworks/Python.framework/Versions/Current/lib/python2.5/\n\n1b. local/include/python2.5 \n---> local/Frameworks/Python.framework/Versions/Current/include/python2.5/\n\n1c. Restart make\n\n2. The build of the sage package crashes, with a similar error.  \n\n2a. Delete the busted symlink at \nlocal/Frameworks/Python.framework/Versions/Current/lib/python2.5/site-packages/sage\n\n2b. Create a symlink:\nlocal/Frameworks/Python.framework/Versions/Current/lib/python2.5/site-packages/sage\n--->devel/sage/build/sage\n\n2c. Delete half-built files, restart make.\n\n3. The build of cvxopt crashes, with a duplicate symbol error.  I'm not in a position to debug this one.\n\nAny attention appreciated!  For my part, I can muddle along with the duplicate builds but I would like to get this working.\n\nD\n\nIssue created by migration from https://trac.sagemath.org/ticket/3924\n\n",
    "created_at": "2008-08-22T01:38:43Z",
    "labels": [
        "component: build",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "making sage on os x build, when python is built as a framework",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3924",
    "user": "https://trac.sagemath.org/admin/accounts/users/dphilp"
}
```
Assignee: jkantor

CC:  dphilp prabhu @cswiercz

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

2a. local/lib/python2.5 
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

Issue created by migration from https://trac.sagemath.org/ticket/3924





---

archive/issue_comments_028020.json:
```json
{
    "body": "The duplicate symbol error is this:\nld: duplicate symbol _matrix_tp in build/temp.macosx-10.3-i386-2.5/C/dense.o and build/temp.macosx-10.3-i386-2.5/C/base.o\n\nIt is the first error, until then, gcc happily chugs along.",
    "created_at": "2008-08-25T02:02:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3924#issuecomment-28020",
    "user": "https://trac.sagemath.org/admin/accounts/users/dphilp"
}
```

The duplicate symbol error is this:
ld: duplicate symbol _matrix_tp in build/temp.macosx-10.3-i386-2.5/C/dense.o and build/temp.macosx-10.3-i386-2.5/C/base.o

It is the first error, until then, gcc happily chugs along.



---

archive/issue_comments_028021.json:
```json
{
    "body": "This is the command that pruduced the error.\n\ngcc -bundle -undefined dynamic_lookup build/temp.macosx-10.3-i386-2.5/C/base.o build/temp.macosx-10.3-i386-2.5/C/dense.o build/temp.macosx-10.3-i386-2.5/C/sparse.o -L/Users/dphilp/sage-3.0.3fo/local/lib -L/Users/dphilp/sage-3.0.3fo/local/lib/gcc-lib/i386-apple-darwin8.10.3/4.0.3/ -lm -llapack -lblas -lf95 -o build/lib.macosx-10.3-i386-2.5/cvxopt/base.so",
    "created_at": "2008-08-25T02:18:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3924#issuecomment-28021",
    "user": "https://trac.sagemath.org/admin/accounts/users/dphilp"
}
```

This is the command that pruduced the error.

gcc -bundle -undefined dynamic_lookup build/temp.macosx-10.3-i386-2.5/C/base.o build/temp.macosx-10.3-i386-2.5/C/dense.o build/temp.macosx-10.3-i386-2.5/C/sparse.o -L/Users/dphilp/sage-3.0.3fo/local/lib -L/Users/dphilp/sage-3.0.3fo/local/lib/gcc-lib/i386-apple-darwin8.10.3/4.0.3/ -lm -llapack -lblas -lf95 -o build/lib.macosx-10.3-i386-2.5/cvxopt/base.so



---

archive/issue_comments_028022.json:
```json
{
    "body": "Can crash tthrough the cvxopt errors by adding extern declarations in some of the source files.\n\nI think this is a complete list:\n\nin src/C/base.c, \n\n```\nPyTypeObject matrix_tp ;\nPyTypeObject spmatrix_tp ;\n```\n \nboth get an extern.\n\nIn dense.c, `PyTypeObject spmatrix_tp ;` gets an extern.\n\nIn dense.c and sparse.c, `PyObject *base_mod;` gets an extern.",
    "created_at": "2008-08-25T03:00:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3924#issuecomment-28022",
    "user": "https://trac.sagemath.org/admin/accounts/users/dphilp"
}
```

Can crash tthrough the cvxopt errors by adding extern declarations in some of the source files.

I think this is a complete list:

in src/C/base.c, 

```
PyTypeObject matrix_tp ;
PyTypeObject spmatrix_tp ;
```
 
both get an extern.

In dense.c, `PyTypeObject spmatrix_tp ;` gets an extern.

In dense.c and sparse.c, `PyObject *base_mod;` gets an extern.



---

archive/issue_comments_028023.json:
```json
{
    "body": "It builds and sage works with two warnings and some dsage badness:\n\n```\nWARNING: Readline services not available on this platform.\nWARNING: The auto-indent feature requires the readline library\n```\n\n\nfailed doctests:\n\n```\nsage -t  devel/sage/sage/dsage/tests/testdoc.py             \n**********************************************************************\nFile \"/Users/dphilp/sage-3.0.3fo/tmp/testdoc.py\", line 14:\n    sage: a\nExpected:\n    5\nGot:\n    No output.\n**********************************************************************\nFile \"/Users/dphilp/sage-3.0.3fo/tmp/testdoc.py\", line 33:\n    sage: j\nExpected:\n    10\nGot:\n    No output.\n**********************************************************************\n```\n",
    "created_at": "2008-08-25T04:33:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3924#issuecomment-28023",
    "user": "https://trac.sagemath.org/admin/accounts/users/dphilp"
}
```

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

archive/issue_comments_028024.json:
```json
{
    "body": "Readline fix.  Python's spkg needs a couple of lines:\n\n```\nLDFLAGS=\"-L/Users/dphilp/sage-3.0.3fo/local/lib $LDFLAGS\"\nexport LDFLAGS\n\nCPPFLAGS=\"-I/Users/dphilp/sage-3.0.3fo/local/include $CPPFLAGS\"\nexport CPPFLAGS\n```\n",
    "created_at": "2008-08-25T06:55:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3924#issuecomment-28024",
    "user": "https://trac.sagemath.org/admin/accounts/users/dphilp"
}
```

Readline fix.  Python's spkg needs a couple of lines:

```
LDFLAGS="-L/Users/dphilp/sage-3.0.3fo/local/lib $LDFLAGS"
export LDFLAGS

CPPFLAGS="-I/Users/dphilp/sage-3.0.3fo/local/include $CPPFLAGS"
export CPPFLAGS
```




---

archive/issue_comments_028025.json:
```json
{
    "body": "The last has been committed as a general fix to python's build by mabshoff.",
    "created_at": "2008-08-25T07:13:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3924#issuecomment-28025",
    "user": "https://trac.sagemath.org/admin/accounts/users/dphilp"
}
```

The last has been committed as a general fix to python's build by mabshoff.



---

archive/issue_comments_028026.json:
```json
{
    "body": "And that also fixes dsage's doctest trouble.",
    "created_at": "2008-08-25T07:15:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3924#issuecomment-28026",
    "user": "https://trac.sagemath.org/admin/accounts/users/dphilp"
}
```

And that also fixes dsage's doctest trouble.



---

archive/issue_comments_028027.json:
```json
{
    "body": "Patches required to get this working.  (Sorry I don't know how to do the pretty red/green bizzo.)\n## python.spkg/spkg-install:\n\n```\n49a50,56\n> # (OS X only)  If SAGE_PYTHON_FRAMEWORK is set, compile sage as a framework\n> if [ `uname` = \"Darwin\" -a $SAGE_PYTHON_FRAMEWORK ] ; then\n>     echo \"Building python as a framework with --enable-framework=$SAGE_LOCAL/Frameworks\"\n>     FRAMEWORK_BUILD_OPTION=\"--enable-framework=$SAGE_LOCAL/Frameworks\"\n> fi\n> \n> \n74c81,82\n<         --with-gcc=\"gcc -m64\" --disable-toolbox-glue\n---\n>         --with-gcc=\"gcc -m64\" --disable-toolbox-glue \\\n>         $FRAMEWORK_BUILD_OPTION\n80c88,89\n<         ./configure $EXTRAFLAGS --prefix=\"$SAGE_LOCAL\" --without-libpng --enable-unicode=ucs4\n---\n>         ./configure $EXTRAFLAGS --prefix=\"$SAGE_LOCAL\" --without-libpng --enable-unicode=ucs4 \\\n>         $FRAMEWORK_BUILD_OPTION\n109a119,132\n> # (OS X only)  If SAGE_PYTHON_FRAMEWORK the symlink created above will be left dangling\n> if [ $SAGE_PYTHON_FRAMEWORK ] ; then\n>     ln -s python2.5 ../Frameworks/Python.framework/Versions/Current/lib/python2.5\n> fi\n> \n> \n> cd $SAGE_LOCAL/include\n> \n> # (OS X only)  If SAGE_PYTHON_FRAMEWORK, we need to point to the framework headers\n> if [ $SAGE_PYTHON_FRAMEWORK ] ; then\n>     ln -s python2.5 ../Frameworks/Python.framework/Versions/Current/include/python2.5\n> fi\n> \n```\n\n\n## sage.spkg/sagebuild.py:\n\n```\n509c509,514\n<     safesymlink('../../../../devel/sage/build/sage','local/lib/python/site-packages/sage')\n---\n>     if env.options['SAGE_PYTHON_FRAMEWORK'] != 'yes' :\n>         safesymlink('../../../../devel/sage/build/sage','local/lib/python/site-packages/sage')\n>     else:\n>         safesymlink(\n>             '../../../../../../devel/sage/build/sage',\n>             'local/Frameworks/Python.framework/Versions/Current/lib/python/site-packages/sage')\n```\n\n\nAnd a bunch of edits to cvxopt, which are apparently fixed in version 1.0.",
    "created_at": "2008-08-25T12:33:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3924#issuecomment-28027",
    "user": "https://trac.sagemath.org/admin/accounts/users/dphilp"
}
```

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

archive/issue_comments_028028.json:
```json
{
    "body": "Slightly better in python.spkg/spkg-install:\n\n```\n> # (OS X only)  If SAGE_PYTHON_FRAMEWORK is set, compile sage as a framework\n> if [ `uname` = \"Darwin\" -a \"$SAGE_PYTHON_FRAMEWORK\" = \"yes\" ] ; then\n>     echo \"Building python as a framework with --enable-framework=$SAGE_LOCAL/Frameworks\"\n>     FRAMEWORK_BUILD_OPTION=\"--enable-framework=$SAGE_LOCAL/Frameworks\"\n> fi\n```\n",
    "created_at": "2008-08-26T01:23:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3924#issuecomment-28028",
    "user": "https://trac.sagemath.org/admin/accounts/users/dphilp"
}
```

Slightly better in python.spkg/spkg-install:

```
> # (OS X only)  If SAGE_PYTHON_FRAMEWORK is set, compile sage as a framework
> if [ `uname` = "Darwin" -a "$SAGE_PYTHON_FRAMEWORK" = "yes" ] ; then
>     echo "Building python as a framework with --enable-framework=$SAGE_LOCAL/Frameworks"
>     FRAMEWORK_BUILD_OPTION="--enable-framework=$SAGE_LOCAL/Frameworks"
> fi
```




---

archive/issue_comments_028029.json:
```json
{
    "body": "` if [ \"$SAGE_PYTHON_FRAMEWORK\" = \"yes\" ] ; then ` throughout",
    "created_at": "2008-08-26T02:00:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3924#issuecomment-28029",
    "user": "https://trac.sagemath.org/admin/accounts/users/dphilp"
}
```

` if [ "$SAGE_PYTHON_FRAMEWORK" = "yes" ] ; then ` throughout



---

archive/issue_comments_028030.json:
```json
{
    "body": "correction to: ` sage.spkg/sagebuild.py `\n\n```\n>     if os.environ.get('SAGE_PYTHON_FRAMEWORK') != 'yes' :\n>         safesymlink('../../../../devel/sage/build/sage','local/lib/python/site-packages/sage')\n>     else:\n>         safesymlink(\n>             '../../../../../../devel/sage/build/sage',\n>             'local/Frameworks/Python.framework/Versions/Current/lib/python/site-packages/sage')\n```\n",
    "created_at": "2008-08-26T04:27:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3924#issuecomment-28030",
    "user": "https://trac.sagemath.org/admin/accounts/users/dphilp"
}
```

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

archive/issue_comments_028031.json:
```json
{
    "body": "I suck.  ` python.spkg/spkg-install `\n\n\n```\n> # (OS X only)  If SAGE_PYTHON_FRAMEWORK the symlink created above will be left dangling\n> if [ $SAGE_PYTHON_FRAMEWORK ] ; then\n>     ln -s python2.5 ../Frameworks/Python.framework/Versions/Current/lib/python2.5\n> fi\n> \n> \n> cd $SAGE_LOCAL/include\n> \n> # (OS X only)  If SAGE_PYTHON_FRAMEWORK, we need to point to the framework headers\n> if [ $SAGE_PYTHON_FRAMEWORK ] ; then\n>     ln -s python2.5 ../Frameworks/Python.framework/Versions/Current/include/python2.5\n> fi\n```\n",
    "created_at": "2008-08-26T05:06:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3924#issuecomment-28031",
    "user": "https://trac.sagemath.org/admin/accounts/users/dphilp"
}
```

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

archive/issue_comments_028032.json:
```json
{
    "body": "Attachment [trac_sage_3924.patch](tarball://root/attachments/some-uuid/ticket3924/trac_sage_3924.patch) by dphilp created at 2008-08-27 03:52:43",
    "created_at": "2008-08-27T03:52:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3924#issuecomment-28032",
    "user": "https://trac.sagemath.org/admin/accounts/users/dphilp"
}
```

Attachment [trac_sage_3924.patch](tarball://root/attachments/some-uuid/ticket3924/trac_sage_3924.patch) by dphilp created at 2008-08-27 03:52:43



---

archive/issue_comments_028033.json:
```json
{
    "body": "Attachment [trac_python_3924.patch](tarball://root/attachments/some-uuid/ticket3924/trac_python_3924.patch) by @williamstein created at 2009-07-09 20:25:10\n\nThis was the original mess of a ticket description:\n\nI'm trying to build sage on mac with a shareable python library.  The current version, being built without the --enable-framework option, cannot be linked to other libraries because of the environ variable.  I think getting this working would be useful, and I would like eventually to see it the default build on OS X.\n\nThe following recipe works, though it is clearly a defective approach:\n\n1. build vanilla sage from source \n\n2. edit the spkg/standard/python-2.5....spkg/spkg-install file to include the --enable-framework=SAGE_ROOT/local/Frameworks\n\n3. rebuild sage.  This creates SAGE_ROOT/Frameworks/Python.framework\n\n4. all doctests pass, and I can link to libpython from boost python\n\nIdeally, the following steps would work:\n\n1. edit the spkg/standard/python-2.5....spkg/spkg-install file to include the --enable-framework= SAGE_ROOT/local/Frameworks\n\n2. build sage.\n\nIt doesn't work so simply.  I've managed to help it along a few steps, but am stuck with cvxopt\n\n1. The build of mercurial crashes.  When it crashes, create two symlinks:\n\n2a. local/lib/python2.5 \n---> local/Frameworks/Python.framework/Versions/Current/lib/python2.5/\n\n1b. local/include/python2.5 \n---> local/Frameworks/Python.framework/Versions/Current/include/python2.5/\n\n1c. Restart make\n\n2. The build of the sage package crashes, with a similar error.  \n\n2a. Delete the busted symlink at \nlocal/Frameworks/Python.framework/Versions/Current/lib/python2.5/site-packages/sage\n\n2b. Create a symlink:\nlocal/Frameworks/Python.framework/Versions/Current/lib/python2.5/site-packages/sage\n--->devel/sage/build/sage\n\n2c. Delete half-built files, restart make.\n\n3. The build of cvxopt crashes, with a duplicate symbol error.  I'm not in a position to debug this one.\n\nAny attention appreciated!  For my part, I can muddle along with the duplicate builds but I would like to get this working.\n\nD",
    "created_at": "2009-07-09T20:25:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3924#issuecomment-28033",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_python_3924.patch](tarball://root/attachments/some-uuid/ticket3924/trac_python_3924.patch) by @williamstein created at 2009-07-09 20:25:10

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

2a. local/lib/python2.5 
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

archive/issue_comments_028034.json:
```json
{
    "body": "Since we have upgraded to python-2.6, I think this needs to be rebased at least.  I am interested in testing an updated version.",
    "created_at": "2009-10-29T19:11:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3924#issuecomment-28034",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Since we have upgraded to python-2.6, I think this needs to be rebased at least.  I am interested in testing an updated version.



---

archive/issue_comments_028035.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-10-29T19:11:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3924#issuecomment-28035",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_028036.json:
```json
{
    "body": "[\u0432\u043e\u0441\u0442\u043e\u0447\u043d\u044b\u0435 \u0442\u0430\u043d\u0446\u044b](http://art-dance.com.ua/)",
    "created_at": "2010-05-26T08:41:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3924#issuecomment-28036",
    "user": "https://trac.sagemath.org/admin/accounts/users/bascorp2"
}
```

[восточные танцы](http://art-dance.com.ua/)
