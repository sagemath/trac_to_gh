# Issue 8087: jinja2 fails to build on Open Solaris x64 (

archive/issues_008087.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  jas @mwhansen\n\n## Build environment\n* Sun Ultra 27 3.33 GHz Intel W3580 Xeon. Quad core. 8 threads. 12 GB RAM\n* OpenSolaris 2009.06 snv_111b X86\n* Sage 4.3.1.alpha1 (with a few packages hacked to work on 64-bit)\n* gcc 4.3.4 configured with Sun linker and GNU assembler from binutils version 2.20.\n* 64-bit build. SAGE64 was set to yes, plus various other tricks to get -m64 into packages. \n## The problem\nIt looks as though this might be a 32/64 bit issue\ndue to the following line:\n\n\n```\nIn file included from /export/home/drkirkby/sage-4.3.1/local/include/python2.6/Python.h:58,\n                 from jinja2/_speedups.c:15:\n/export/home/drkirkby/sage-4.3.1/local/include/python2.6/pyport.h:685:2: error: #error \"LONG_BIT definition appears wrong for platform (bad gcc/glibc config?).\"\nerror: command 'gcc' failed with exit status 1\nError building Jinja2: 'Error installing Jinja2'\n\n```\n\nhere's the full log. \n\n```\njinja2-2.1.1.p0/src/TODO\nFinished extraction\n****************************************************\nHost system\nuname -a:\nSunOS hawk 5.11 snv_111b i86pc i386 i86pc\n****************************************************\n****************************************************\nCC Version\ngcc -v\nUsing built-in specs.\nTarget: i386-pc-solaris2.11\nConfigured with: ../gcc-4.3.4/configure --prefix=/usr/local/gcc-4.3.4-GNU-assembler-Sun-linker --with-as=/usr/local/binutils-2.20/bin/as --with-ld=/usr/ccs/bin/ld --with-gmp=/usr/local --with-mpfr=/usr/local\nThread model: posix\ngcc version 4.3.4 (GCC) \n****************************************************\nrunning install\nrunning bdist_egg\nrunning egg_info\nwriting requirements to Jinja2.egg-info/requires.txt\nwriting Jinja2.egg-info/PKG-INFO\nwriting top-level names to Jinja2.egg-info/top_level.txt\nwriting dependency_links to Jinja2.egg-info/dependency_links.txt\nwriting entry points to Jinja2.egg-info/entry_points.txt\nreading manifest file 'Jinja2.egg-info/SOURCES.txt'\nreading manifest template 'MANIFEST.in'\nwarning: no files found matching 'Makefile'\nwarning: no files found matching 'ez_setup.py'\nwarning: no previously-included files matching '*' found under directory 'docs/_build/doctrees'\nwriting manifest file 'Jinja2.egg-info/SOURCES.txt'\ninstalling library code to build/bdist.solaris-2.11-i86pc/egg\nrunning install_lib\nrunning build_py\ncreating build\ncreating build/lib.solaris-2.11-i86pc-2.6\ncreating build/lib.solaris-2.11-i86pc-2.6/jinja2\ncopying jinja2/optimizer.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2\ncopying jinja2/constants.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2\ncopying jinja2/lexer.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2\ncopying jinja2/loaders.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2\ncopying jinja2/tests.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2\ncopying jinja2/ext.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2\ncopying jinja2/_ipysupport.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2\ncopying jinja2/bccache.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2\ncopying jinja2/utils.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2\ncopying jinja2/nodes.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2\ncopying jinja2/runtime.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2\ncopying jinja2/sandbox.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2\ncopying jinja2/debug.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2\ncopying jinja2/environment.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2\ncopying jinja2/parser.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2\ncopying jinja2/compiler.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2\ncopying jinja2/__init__.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2\ncopying jinja2/filters.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2\ncopying jinja2/exceptions.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2\ncopying jinja2/defaults.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2\ncopying jinja2/visitor.py -> build/lib.solaris-2.11-i86pc-2.6/jinja2\nrunning build_ext\nbuilding 'jinja2._speedups' extension\ncreating build/temp.solaris-2.11-i86pc-2.6\ncreating build/temp.solaris-2.11-i86pc-2.6/jinja2\ngcc -fno-strict-aliasing -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -fPIC -I/export/home/drkirkby/sage-4.3.1/local/include/python2.6 -c jinja2/_speedups.c -o build/temp.solaris-2.11-i86pc-2.6/jinja2/_speedups.o\nIn file included from /export/home/drkirkby/sage-4.3.1/local/include/python2.6/Python.h:58,\n                 from jinja2/_speedups.c:15:\n/export/home/drkirkby/sage-4.3.1/local/include/python2.6/pyport.h:685:2: error: #error \"LONG_BIT definition appears wrong for platform (bad gcc/glibc config?).\"\nerror: command 'gcc' failed with exit status 1\nError building Jinja2: 'Error installing Jinja2'\n\nreal\t0m0.211s\nuser\t0m0.136s\nsys\t0m0.071s\nsage: An error occurred while installing jinja2-2.1.1.p0\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8087\n\n",
    "created_at": "2010-01-27T03:49:35Z",
    "labels": [
        "component: porting: solaris",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "jinja2 fails to build on Open Solaris x64 (",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8087",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: drkirkby

CC:  jas @mwhansen

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



Issue created by migration from https://trac.sagemath.org/ticket/8087





---

archive/issue_comments_070750.json:
```json
{
    "body": "The spkg-install contains\n\npython setup.py install\n\nno flags set.\n\nexport CFLAGS=-m64 will do, I suppose.\n\nJaap",
    "created_at": "2010-01-27T11:24:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8087",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8087#issuecomment-70750",
    "user": "https://github.com/jaapspies"
}
```

The spkg-install contains

python setup.py install

no flags set.

export CFLAGS=-m64 will do, I suppose.

Jaap



---

archive/issue_comments_070751.json:
```json
{
    "body": "All you need is a python that is built well. Then python will set the flags for you.\n\nThis is the case for all spkg-install files with python setup.py install\n\n\n\n```\ncvxopt\ncython\ndocutils\nghmm\nipython\njinja\njinja2\nmatplotlib\nmercurial\nmoin\nmpmath\nnetworx\nnumpy\npexpect\npil\npycrypto\npygments\npyprocessing\npython-gnutils\nsagenb\nscipy\nscipy_sandbox\nscons\nsetuptools\nsphinx\nsqlalchemy\ntwisted\nweave\nzodb3\n```\n\n\nSo I think this ticket can be closed.\n\nJaap",
    "created_at": "2010-02-02T12:19:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8087",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8087#issuecomment-70751",
    "user": "https://github.com/jaapspies"
}
```

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

archive/issue_comments_070752.json:
```json
{
    "body": "I do not believe it should be closed until we have a Python in Sage which is working fully on Open Solaris. We do not currently have that. However, your deduction of the reason for this is of course very useful. \n\nI just run *configure --help* in the python source, and see this. Note the 3rd option. I wonder if we should be using \"--with-universal-archs=64-bit\" on 64-bit builds. That might help out with other 64-bit issues related to python. \n\n\n\n```\nOptional Packages:\n  --with-PACKAGE[=ARG]    use PACKAGE [ARG=yes]\n  --without-PACKAGE       do not use PACKAGE (same as --with-PACKAGE=no)\n  --with-universal-archs=ARCH\n                          select architectures for universal build (\"32-bit\",\n                          \"64-bit\" or \"all\")\n```\n\n\nDave",
    "created_at": "2010-02-02T12:46:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8087",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8087#issuecomment-70752",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I do not believe it should be closed until we have a Python in Sage which is working fully on Open Solaris. We do not currently have that. However, your deduction of the reason for this is of course very useful. 

I just run *configure --help* in the python source, and see this. Note the 3rd option. I wonder if we should be using "--with-universal-archs=64-bit" on 64-bit builds. That might help out with other 64-bit issues related to python. 



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

archive/issue_comments_070753.json:
```json
{
    "body": "Replying to [comment:4 drkirkby]:\n> I do not believe it should be closed until we have a Python in Sage which is working fully on Open Solaris. We do not currently have that. However, your deduction of the reason for this is of course very useful. \n>\n\nI know how to build one :)!\n\nJaap",
    "created_at": "2010-02-02T15:07:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8087",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8087#issuecomment-70753",
    "user": "https://github.com/jaapspies"
}
```

Replying to [comment:4 drkirkby]:
> I do not believe it should be closed until we have a Python in Sage which is working fully on Open Solaris. We do not currently have that. However, your deduction of the reason for this is of course very useful. 
>

I know how to build one :)!

Jaap



---

archive/issue_comments_070754.json:
```json
{
    "body": "If #7761 gets in this ticket can be closed.\n\nJaap",
    "created_at": "2010-02-24T20:21:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8087",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8087#issuecomment-70754",
    "user": "https://github.com/jaapspies"
}
```

If #7761 gets in this ticket can be closed.

Jaap



---

archive/issue_comments_070755.json:
```json
{
    "body": "Should we now close this ticket?",
    "created_at": "2010-03-05T00:47:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8087",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8087#issuecomment-70755",
    "user": "https://github.com/qed777"
}
```

Should we now close this ticket?



---

archive/issue_comments_070756.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-03-05T00:50:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8087",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8087#issuecomment-70756",
    "user": "https://github.com/mwhansen"
}
```

Resolution: invalid



---

archive/issue_events_008293.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2010-03-05T00:50:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8087",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8087#event-8293"
}
```



---

archive/issue_comments_070757.json:
```json
{
    "body": "Seems reasonable.",
    "created_at": "2010-03-05T00:50:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8087",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8087#issuecomment-70757",
    "user": "https://github.com/mwhansen"
}
```

Seems reasonable.
