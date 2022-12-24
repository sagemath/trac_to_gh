# Issue 8427: notebook fortran mode does not work with blank first line (or subroutine starting on first line)

archive/issues_008427.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  jkantor @mwhansen @williamstein\n\nThis example does not work from the tutorial http://www.sagemath.org/doc/numerical_sage/f2py.html:\n\n\n```\n%fortran\n\n        Subroutine Rescale(a,b,n)\n        Implicit none\n        Integer n,i,j\n        Real*8 a(n,n), b\nCf2py intent(in,out) a\n        do i = 1,n\n           do j=1,n\n             a(i,j)=b*a(i,j)\n           end do\n        end do\n        end\n```\n\n\nThe error is:\n\n\n```\nTraceback (most recent call last):\n  File \"<string>\", line 1, in <module>\n  File \"/usr/local/sage2/local/lib/python2.6/site-packages/numpy/f2py/f2py2e.py\", line 557, in main\n    run_compile()\n  File \"/usr/local/sage2/local/lib/python2.6/site-packages/numpy/f2py/f2py2e.py\", line 543, in run_compile\n    setup(ext_modules = [ext])\n  File \"/usr/local/sage2/local/lib/python2.6/site-packages/numpy/distutils/core.py\", line 184, in setup\n    return old_setup(**new_attr)\n  File \"/usr/local/sage2/local/lib/python/distutils/core.py\", line 152, in setup\n    dist.run_commands()\n  File \"/usr/local/sage2/local/lib/python/distutils/dist.py\", line 975, in run_commands\n    self.run_command(cmd)\n  File \"/usr/local/sage2/local/lib/python/distutils/dist.py\", line 995, in run_command\n    cmd_obj.run()\n  File \"/usr/local/sage2/local/lib/python2.6/site-packages/numpy/distutils/command/build.py\", line 37, in run\n    old_build.run(self)\n  File \"/usr/local/sage2/local/lib/python/distutils/command/build.py\", line 134, in run\n    self.run_command(cmd_name)\n  File \"/usr/local/sage2/local/lib/python/distutils/cmd.py\", line 333, in run_command\n    self.distribution.run_command(command)\n  File \"/usr/local/sage2/local/lib/python/distutils/dist.py\", line 995, in run_command\n    cmd_obj.run()\n  File \"/usr/local/sage2/local/lib/python2.6/site-packages/numpy/distutils/command/build_src.py\", line 130, in run\n    self.build_sources()\n  File \"/usr/local/sage2/local/lib/python2.6/site-packages/numpy/distutils/command/build_src.py\", line 147, in build_sources\n    self.build_extension_sources(ext)\n  File \"/usr/local/sage2/local/lib/python2.6/site-packages/numpy/distutils/command/build_src.py\", line 256, in build_extension_sources\n    sources = self.f2py_sources(sources, ext)\n  File \"/usr/local/sage2/local/lib/python2.6/site-packages/numpy/distutils/command/build_src.py\", line 514, in f2py_sources\n    ['-m',ext_name]+f_sources)\n  File \"/usr/local/sage2/local/lib/python2.6/site-packages/numpy/f2py/f2py2e.py\", line 338, in run_main\n    postlist=callcrackfortran(files,options)\n  File \"/usr/local/sage2/local/lib/python2.6/site-packages/numpy/f2py/f2py2e.py\", line 276, in callcrackfortran\n    postlist=crackfortran.crackfortran(files)\n  File \"/usr/local/sage2/local/lib/python2.6/site-packages/numpy/f2py/crackfortran.py\", line 2683, in crackfortran\n    readfortrancode(files,crackline)\n  File \"/usr/local/sage2/local/lib/python2.6/site-packages/numpy/f2py/crackfortran.py\", line 346, in readfortrancode\n    'this code is in fix form?\\n\\tline=%s' % `l`)\nException: readfortrancode: Found non-(space,digit) char in the first column.\n\tAre you sure that this code is in fix form?\n\tline='Subroutine Rescale(a,b,n)'\n\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"_sage_input_2.py\", line 19, in <module>\n    end''', '/sagenb/sagenb/sage_notebook.sagenb/home/jason3/382/cells/1')\n  File \"/usr/local/sage2/local/lib/python2.6/site-packages/sagenb-0.7.5.1-py2.6.egg/sagenb/misc/support.py\", line 473, in syseval\n    return system.eval(cmd, sage_globals, locals = sage_globals)\n  File \"/usr/local/sage2/local/lib/python2.6/site-packages/sage/misc/inline_fortran.py\", line 92, in eval\n    os.unlink(name + '.so')\nOSError: [Errno 2] No such file or directory: 'fortran_module_0.so'\n\n```\n\n\nI get the same error if I delete the blank line after %fortran.\n\nHowever, if I change the notebook cell to have a comment as the first line, it seems to work just fine:\n\n\n```\n%fortran\nC\n        Subroutine Rescale(a,b,n)\n        Implicit none\n        Integer n,i,j\n        Real*8 a(n,n), b\nCf2py intent(in,out) a\n        do i = 1,n\n           do j=1,n\n             a(i,j)=b*a(i,j)\n           end do\n        end do\n        end\n```\n\n\nThis is on Sage 4.3.3 (sagenb.org)\n\nIssue created by migration from https://trac.sagemath.org/ticket/8427\n\n",
    "created_at": "2010-03-03T05:54:53Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "notebook fortran mode does not work with blank first line (or subroutine starting on first line)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8427",
    "user": "@jasongrout"
}
```
Assignee: @williamstein

CC:  jkantor @mwhansen @williamstein

This example does not work from the tutorial http://www.sagemath.org/doc/numerical_sage/f2py.html:


```
%fortran

        Subroutine Rescale(a,b,n)
        Implicit none
        Integer n,i,j
        Real*8 a(n,n), b
Cf2py intent(in,out) a
        do i = 1,n
           do j=1,n
             a(i,j)=b*a(i,j)
           end do
        end do
        end
```


The error is:


```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/usr/local/sage2/local/lib/python2.6/site-packages/numpy/f2py/f2py2e.py", line 557, in main
    run_compile()
  File "/usr/local/sage2/local/lib/python2.6/site-packages/numpy/f2py/f2py2e.py", line 543, in run_compile
    setup(ext_modules = [ext])
  File "/usr/local/sage2/local/lib/python2.6/site-packages/numpy/distutils/core.py", line 184, in setup
    return old_setup(**new_attr)
  File "/usr/local/sage2/local/lib/python/distutils/core.py", line 152, in setup
    dist.run_commands()
  File "/usr/local/sage2/local/lib/python/distutils/dist.py", line 975, in run_commands
    self.run_command(cmd)
  File "/usr/local/sage2/local/lib/python/distutils/dist.py", line 995, in run_command
    cmd_obj.run()
  File "/usr/local/sage2/local/lib/python2.6/site-packages/numpy/distutils/command/build.py", line 37, in run
    old_build.run(self)
  File "/usr/local/sage2/local/lib/python/distutils/command/build.py", line 134, in run
    self.run_command(cmd_name)
  File "/usr/local/sage2/local/lib/python/distutils/cmd.py", line 333, in run_command
    self.distribution.run_command(command)
  File "/usr/local/sage2/local/lib/python/distutils/dist.py", line 995, in run_command
    cmd_obj.run()
  File "/usr/local/sage2/local/lib/python2.6/site-packages/numpy/distutils/command/build_src.py", line 130, in run
    self.build_sources()
  File "/usr/local/sage2/local/lib/python2.6/site-packages/numpy/distutils/command/build_src.py", line 147, in build_sources
    self.build_extension_sources(ext)
  File "/usr/local/sage2/local/lib/python2.6/site-packages/numpy/distutils/command/build_src.py", line 256, in build_extension_sources
    sources = self.f2py_sources(sources, ext)
  File "/usr/local/sage2/local/lib/python2.6/site-packages/numpy/distutils/command/build_src.py", line 514, in f2py_sources
    ['-m',ext_name]+f_sources)
  File "/usr/local/sage2/local/lib/python2.6/site-packages/numpy/f2py/f2py2e.py", line 338, in run_main
    postlist=callcrackfortran(files,options)
  File "/usr/local/sage2/local/lib/python2.6/site-packages/numpy/f2py/f2py2e.py", line 276, in callcrackfortran
    postlist=crackfortran.crackfortran(files)
  File "/usr/local/sage2/local/lib/python2.6/site-packages/numpy/f2py/crackfortran.py", line 2683, in crackfortran
    readfortrancode(files,crackline)
  File "/usr/local/sage2/local/lib/python2.6/site-packages/numpy/f2py/crackfortran.py", line 346, in readfortrancode
    'this code is in fix form?\n\tline=%s' % `l`)
Exception: readfortrancode: Found non-(space,digit) char in the first column.
	Are you sure that this code is in fix form?
	line='Subroutine Rescale(a,b,n)'

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "_sage_input_2.py", line 19, in <module>
    end''', '/sagenb/sagenb/sage_notebook.sagenb/home/jason3/382/cells/1')
  File "/usr/local/sage2/local/lib/python2.6/site-packages/sagenb-0.7.5.1-py2.6.egg/sagenb/misc/support.py", line 473, in syseval
    return system.eval(cmd, sage_globals, locals = sage_globals)
  File "/usr/local/sage2/local/lib/python2.6/site-packages/sage/misc/inline_fortran.py", line 92, in eval
    os.unlink(name + '.so')
OSError: [Errno 2] No such file or directory: 'fortran_module_0.so'

```


I get the same error if I delete the blank line after %fortran.

However, if I change the notebook cell to have a comment as the first line, it seems to work just fine:


```
%fortran
C
        Subroutine Rescale(a,b,n)
        Implicit none
        Integer n,i,j
        Real*8 a(n,n), b
Cf2py intent(in,out) a
        do i = 1,n
           do j=1,n
             a(i,j)=b*a(i,j)
           end do
        end do
        end
```


This is on Sage 4.3.3 (sagenb.org)

Issue created by migration from https://trac.sagemath.org/ticket/8427





---

archive/issue_comments_075548.json:
```json
{
    "body": "This (and the similar examples) compiles if you throw in a `!f90` (couldn't figure out how to get it into fixed format though I tried the obvious).  Adding a comment works, as the title suggests.  \n\nHowever, I then can't gain access to the function `rescale`, which I can with the fib examples.\n\nSee https://github.com/sagemath/sagenb/issues/288",
    "created_at": "2014-12-09T16:38:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8427#issuecomment-75548",
    "user": "@kcrisman"
}
```

This (and the similar examples) compiles if you throw in a `!f90` (couldn't figure out how to get it into fixed format though I tried the obvious).  Adding a comment works, as the title suggests.  

However, I then can't gain access to the function `rescale`, which I can with the fib examples.

See https://github.com/sagemath/sagenb/issues/288



---

archive/issue_comments_075549.json:
```json
{
    "body": "It works in the command line:\n\n```\nsage: from sage.misc.inline_fortran import InlineFortran\nsage: fortran = InlineFortran(globals())\nsage: fortran.eval(\"\"\"\n\n\n\n        Subroutine Rescale(a,b,n)\n        Implicit none\n        Integer n,i,j\n        Real*8 a(n,n), b\nCf2py intent(in,out) a\n        do i = 1,n\n           do j=1,n\n             a(i,j)=b*a(i,j)\n           end do\n        end do\n        end\n\"\"\")\nsage: import numpy\nsage: a = numpy.array([[1,2],[3,4]], dtype=float)\nsage: rescale(a, 2.0)\narray([[ 2.,  4.],\n       [ 6.,  8.]])\n```\n",
    "created_at": "2014-12-09T18:46:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8427#issuecomment-75549",
    "user": "@jdemeyer"
}
```

It works in the command line:

```
sage: from sage.misc.inline_fortran import InlineFortran
sage: fortran = InlineFortran(globals())
sage: fortran.eval("""



        Subroutine Rescale(a,b,n)
        Implicit none
        Integer n,i,j
        Real*8 a(n,n), b
Cf2py intent(in,out) a
        do i = 1,n
           do j=1,n
             a(i,j)=b*a(i,j)
           end do
        end do
        end
""")
sage: import numpy
sage: a = numpy.array([[1,2],[3,4]], dtype=float)
sage: rescale(a, 2.0)
array([[ 2.,  4.],
       [ 6.,  8.]])
```




---

archive/issue_comments_075550.json:
```json
{
    "body": "I have a fix upstream - not as neat as could be, but clear and it should work fine until we get the other leading whitespace issues figured out.",
    "created_at": "2014-12-10T04:34:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8427#issuecomment-75550",
    "user": "@kcrisman"
}
```

I have a fix upstream - not as neat as could be, but clear and it should work fine until we get the other leading whitespace issues figured out.



---

archive/issue_comments_075551.json:
```json
{
    "body": "This now depends on #10057, as the fix was merged in.",
    "created_at": "2014-12-12T20:27:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8427#issuecomment-75551",
    "user": "@kcrisman"
}
```

This now depends on #10057, as the fix was merged in.



---

archive/issue_comments_075552.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-12-18T02:56:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8427#issuecomment-75552",
    "user": "@kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075553.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-12-24T09:48:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8427#issuecomment-75553",
    "user": "@jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075554.json:
```json
{
    "body": "Fixed by #10057.",
    "created_at": "2014-12-24T09:48:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8427#issuecomment-75554",
    "user": "@jdemeyer"
}
```

Fixed by #10057.



---

archive/issue_comments_075555.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-01-13T01:16:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8427",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8427#issuecomment-75555",
    "user": "@vbraun"
}
```

Resolution: fixed
