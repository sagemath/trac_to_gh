# Issue 8427: notebook fortran mode does not work with blank first line (or subroutine starting on first line)

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2010-03-03 05:54:53

Assignee: was

CC:  jkantor mhansen was

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


---

Comment by kcrisman created at 2014-12-09 16:38:31

This (and the similar examples) compiles if you throw in a `!f90` (couldn't figure out how to get it into fixed format though I tried the obvious).  Adding a comment works, as the title suggests.  

However, I then can't gain access to the function `rescale`, which I can with the fib examples.

See https://github.com/sagemath/sagenb/issues/288


---

Comment by jdemeyer created at 2014-12-09 18:46:15

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

Comment by kcrisman created at 2014-12-10 04:34:16

I have a fix upstream - not as neat as could be, but clear and it should work fine until we get the other leading whitespace issues figured out.


---

Comment by kcrisman created at 2014-12-12 20:27:43

This now depends on #10057, as the fix was merged in.


---

Comment by kcrisman created at 2014-12-18 02:56:36

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2014-12-24 09:48:44

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2014-12-24 09:48:44

Fixed by #10057.


---

Comment by vbraun created at 2015-01-13 01:16:30

Resolution: fixed
