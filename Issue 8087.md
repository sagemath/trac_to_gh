# Issue 8087: jinja2 fails to build on Open Solaris x64 (

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-01-27 03:49:35

Assignee: drkirkby

CC:  jas mhansen

## Build environment
 * Sun Ultra 27 3.33 GHz Intel W3580 Xeon. Quad core. 8 threads. 12 GB RAM
 * OpenSolaris 2009.06 snv_111b X86
 * Sage 4.3.1.alpha1 (with a few packages hacked to work on 64-bit)
 * gcc 4.3.4 configured with Sun linker and GNU assembler from binutils version 2.20.
 * 64-bit build. SAGE64 was set to yes, plus various other tricks to get -m64 into packages. 
## The problem
It looks as though this might be a 32/64 bit issue
due to the following line:


```
In file included from /export/home/drkirkby/sage-4.3.1/local/include/python2.6/Python.h:58,
                 from jinja2/_speedups.c:15:
/export/home/drkirkby/sage-4.3.1/local/include/python2.6/pyport.h:685:2: error: #error "LONG_BIT definition appears wrong for platform (bad gcc/glibc config?)."
error: command 'gcc' failed with exit status 1
Error building Jinja2: 'Error installing Jinja2'

```

here's the full log. 

```
jinja2-2.1.1.p0/src/TODO
Finished extraction
****************************************************
Host system
uname -a:
SunOS hawk 5.11 snv_111b i86pc i386 i86pc
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: i386-pc-solaris2.11
Configured with: ../gcc-4.3.4/configure --prefix=/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker --with-as=/usr/local/binutils-2.20/bin/as --with-ld=/usr/ccs/bin/ld --with-gmp=/usr/local --with-mpfr=/usr/local
Thread model: posix
gcc version 4.3.4 (GCC) 
****************************************************
running install
running bdist_egg
running egg_info
writing requirements to Jinja2.egg-info/requires.txt
writing Jinja2.egg-info/PKG-INFO
writing top-level names to Jinja2.egg-info/top_level.txt
writing dependency_links to Jinja2.egg-info/dependency_links.txt
writing entry points to Jinja2.egg-info/entry_points.txt
reading manifest file 'Jinja2.egg-info/SOURCES.txt'
reading manifest template 'MANIFEST.in'
warning: no files found matching 'Makefile'
warning: no files found matching 'ez_setup.py'
warning: no previously-included files matching '*' found under directory 'docs/_build/doctrees'
writing manifest file 'Jinja2.egg-info/SOURCES.txt'
installing library code to build/bdist.solaris-2.11-i86pc/egg
running install_lib
running build_py
creating build
creating build/lib.solaris-2.11-i86pc-2.6
creating build/lib.solaris-2.11-i86pc-2.6/jinja2
copying jinja2/optimizer.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2
copying jinja2/constants.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2
copying jinja2/lexer.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2
copying jinja2/loaders.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2
copying jinja2/tests.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2
copying jinja2/ext.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2
copying jinja2/_ipysupport.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2
copying jinja2/bccache.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2
copying jinja2/utils.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2
copying jinja2/nodes.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2
copying jinja2/runtime.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2
copying jinja2/sandbox.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2
copying jinja2/debug.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2
copying jinja2/environment.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2
copying jinja2/parser.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2
copying jinja2/compiler.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2
copying jinja2/__init__.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2
copying jinja2/filters.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2
copying jinja2/exceptions.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2
copying jinja2/defaults.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2
copying jinja2/visitor.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2
running build_ext
building 'jinja2._speedups' extension
creating build/temp.solaris-2.11-i86pc-2.6
creating build/temp.solaris-2.11-i86pc-2.6/jinja2
gcc -fno-strict-aliasing -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -fPIC -I/export/home/drkirkby/sage-4.3.1/local/include/python2.6 -c jinja2/_speedups.c -o build/temp.solaris-2.11-i86pc-2.6/jinja2/_speedups.o
In file included from /export/home/drkirkby/sage-4.3.1/local/include/python2.6/Python.h:58,
                 from jinja2/_speedups.c:15:
/export/home/drkirkby/sage-4.3.1/local/include/python2.6/pyport.h:685:2: error: #error "LONG_BIT definition appears wrong for platform (bad gcc/glibc config?)."
error: command 'gcc' failed with exit status 1
Error building Jinja2: 'Error installing Jinja2'

real	0m0.211s
user	0m0.136s
sys	0m0.071s
sage: An error occurred while installing jinja2-2.1.1.p0
```




---

Comment by jsp created at 2010-01-27 11:24:00

The spkg-install contains

python setup.py install

no flags set.

export CFLAGS=-m64 will do, I suppose.

Jaap


---

Comment by jsp created at 2010-02-02 12:19:00

All you need is a python that is built well. Then python will set the flags for you.

This is the case for all spkg-install files with python setup.py install



```
cvxopt
cython
docutils
ghmm
ipython
jinja
jinja2
matplotlib
mercurial
moin
mpmath
networx
numpy
pexpect
pil
pycrypto
pygments
pyprocessing
python-gnutils
sagenb
scipy
scipy_sandbox
scons
setuptools
sphinx
sqlalchemy
twisted
weave
zodb3
```


So I think this ticket can be closed.

Jaap


---

Comment by drkirkby created at 2010-02-02 12:46:06

I do not believe it should be closed until we have a Python in Sage which is working fully on Open Solaris. We do not currently have that. However, your deduction of the reason for this is of course very useful. 

I just run _configure --help_ in the python source, and see this. Note the 3rd option. I wonder if we should be using "--with-universal-archs=64-bit" on 64-bit builds. That might help out with other 64-bit issues related to python. 



```
Optional Packages:
  --with-PACKAGE[=ARG]    use PACKAGE [ARG=yes]
  --without-PACKAGE       do not use PACKAGE (same as --with-PACKAGE=no)
  --with-universal-archs=ARCH
                          select architectures for universal build ("32-bit",
                          "64-bit" or "all")
```


Dave


---

Comment by jsp created at 2010-02-02 15:07:48

Replying to [comment:4 drkirkby]:
> I do not believe it should be closed until we have a Python in Sage which is working fully on Open Solaris. We do not currently have that. However, your deduction of the reason for this is of course very useful. 
>

I know how to build one :)!

Jaap


---

Comment by jsp created at 2010-02-24 20:21:49

If #7761 gets in this ticket can be closed.

Jaap


---

Comment by mpatel created at 2010-03-05 00:47:39

Should we now close this ticket?


---

Comment by mhansen created at 2010-03-05 00:50:38

Resolution: invalid


---

Comment by mhansen created at 2010-03-05 00:50:38

Seems reasonable.
