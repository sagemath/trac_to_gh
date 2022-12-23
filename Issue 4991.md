# Issue 4991: GDB is broken on OSX due to ipython's readline detection

Issue created by migration from https://trac.sagemath.org/ticket/4991

Original creator: mabshoff

Original creation time: 2009-01-17 15:28:37

Assignee: mabshoff

Running Sage under gdb is broken on OSX at the moment:

```
(gdb) r
Starting program: /Users/michaelabshoff/Desktop/sage-3.2.3-64bit/local/bin/python /Users/michaelabshoff/Desktop/sage-3.2.3-64bit/tmp/.doctest_ell_finite_field.py
warning: posix_spawn failed, trying execvp, error: 86
Traceback (most recent call last):
  File "/Users/michaelabshoff/Desktop/sage-3.2.3-64bit/tmp/.doctest_ell_finite_field.py", line 2, in <module>
    from sage.all_cmdline import *; 
  File "/Users/michaelabshoff/Desktop/sage-3.2.3-64bit/local/lib/python2.5/site-packages/sage/all_cmdline.py", line 14, in <module>
    from sage.all import *
  File "/Users/michaelabshoff/Desktop/sage-3.2.3-64bit/local/lib/python2.5/site-packages/sage/all.py", line 64, in <module>
    from sage.misc.all       import *         # takes a while
  File "/Users/michaelabshoff/Desktop/sage-3.2.3-64bit/local/lib/python2.5/site-packages/sage/misc/all.py", line 16, in <module>
    from sage_timeit_class import timeit
  File "sage_timeit_class.pyx", line 3, in sage.misc.sage_timeit_class (sage/misc/sage_timeit_class.c:603)
  File "/Users/michaelabshoff/Desktop/sage-3.2.3-64bit/local/lib/python2.5/site-packages/sage/misc/sage_timeit.py", line 12, in <module>
    import timeit as timeit_, time, math, preparser, interpreter
  File "/Users/michaelabshoff/Desktop/sage-3.2.3-64bit/local/lib/python2.5/site-packages/sage/misc/interpreter.py", line 95, in <module>
    import IPython.ipapi
  File "/Users/michaelabshoff/Desktop/sage-3.2.3-64bit/local/lib/python2.5/site-packages/IPython/__init__.py", line 57, in <module>
    __import__(name,glob,loc,[])
  File "/Users/michaelabshoff/Desktop/sage-3.2.3-64bit/local/lib/python2.5/site-packages/IPython/ipstruct.py", line 22, in <module>
    from IPython.genutils import list2dict2
  File "/Users/michaelabshoff/Desktop/sage-3.2.3-64bit/local/lib/python2.5/site-packages/IPython/genutils.py", line 118, in <module>
    import IPython.rlineimpl as readline
  File "/Users/michaelabshoff/Desktop/sage-3.2.3-64bit/local/lib/python2.5/site-packages/IPython/rlineimpl.py", line 37, in <module>
    (status, result) = commands.getstatusoutput( "otool -L %s | grep libedit" % _rl.__file__ )
  File "/Users/michaelabshoff/Desktop/sage-3.2.3-64bit/local/lib/python2.5/commands.py", line 54, in getstatusoutput
    text = pipe.read()
IOError: [Errno 4] Interrupted system call

Program exited with code 01.
```

The above problem is caused by the IPython import. The problem goes away if we disable the following libedit import test in rlineimpl.py

```
uses_libedit = False
if sys.platform == 'darwin' and have_readline:
    import commands
    (status, result) = commands.getstatusoutput( "otool -L %s | grep libedit" % _rl.__file__ )
    if status == 0 and len(result) > 0:
        # we are bound to libedit - new in Leopard
        _rl.parse_and_bind("bind ^I rl_complete")
        print "Leopard libedit detected."
        uses_libedit = True
```

This can be done without side effects since we link against the real readline. The issue has been reported to the IPython mailing list.

spkg is coming up.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-17 15:28:45

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-01-18 16:31:57

The spkg is at

http://sage.math.washington.edu/home/mabshoff/spkgs/ipython-0.8.4.p1.spkg

Cheers,

Michael


---

Comment by was created at 2009-01-18 20:42:56

I took a clean Sage install, installed your spkg, then started sage -gdb and get

```
...
. done
Reading symbols for shared libraries warning: Could not find object file "/Users/wstein/sage-3.2.3/devel/sage-main/build/temp.macosx-10.3-i386-2.5/sage/ext/interactive_constructors_c.o" - no debug information available for "sage/ext/interactive_constructors_c.c".

. done
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/Users/wstein/sage/local/lib/python2.5/site-packages/IPython/ipmaker.pyc in force_import(modname)
     64         reload(sys.modules[modname])
     65     else:
---> 66         __import__(modname)
     67 
     68 

/Users/wstein/ipy_profile_sage.py in <module>()
     14     from sage.misc.interpreter import attached_files
     15 
---> 16     branch = sage.misc.misc.branch_current_hg_notice(sage.misc.misc.branch_current_hg())
     17     if branch:
     18         print branch

/Users/wstein/sage/local/lib/python2.5/site-packages/sage/misc/misc.pyc in branch_current_hg()
   1502     i = s.rfind('->')
   1503     if i == -1:
-> 1504         raise RuntimeError, "unable to determine branch?!"
   1505     s = s[i+2:]
   1506     i = s.find('-')

RuntimeError: unable to determine branch?!
Error importing ipy_profile_sage - perhaps you should run %upgrade?
WARNING: Loading of ipy_profile_sage failed.

sage: 
```


That said, it gets farther and is running into a different error than before.  Also, the patch you did include looks good and is done right.  Thus this ticket gets a positive review since it's summary specifically says it's only supposed to fix a readline detection issue, not a branch detection issue. 

Please create another ticket though with the branch detection issue (just paste the above log).


---

Comment by mabshoff created at 2009-01-19 02:05:56

I have made the above issue with branches #5019

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-19 02:07:11

Resolution: fixed


---

Comment by mabshoff created at 2009-01-19 02:07:11

Merged in Sage 3.3.alpha0
