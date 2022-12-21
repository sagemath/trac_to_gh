# Issue 6739: warning when importing sage within the sage build directory

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-08-12 14:02:49

Assignee: was

In numpy one has:

```
bash-3.2$ python
Python 2.6.2 (r262:71600, Aug 11 2009, 10:59:28) 
[GCC 4.3.2 20080827 (beta) 2] on cygwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "numpy/__init__.py", line 121, in <module>
    raise ImportError(msg)
ImportError: Error importing numpy: you should not try to import numpy from
        its source directory; please exit the numpy source tree, and relaunch
        your python intepreter from there.
>>> 
```


We should have the same with sage.  Instead we get a confusing error:

```

GOOD:

flat:sage wstein$ cd
flat:~ wstein$ sage -python
Python 2.6.2 (r262:71600, Jul  8 2009, 17:42:25) 
[GCC 4.0.1 (Apple Inc. build 5465)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import sage.all
>>> 

BAD:

flat:sage wstein$ sage -python
Python 2.6.2 (r262:71600, Jul  8 2009, 17:42:25) 
[GCC 4.0.1 (Apple Inc. build 5465)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import sage.all
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/wstein/sage/build/64bit/sage/local/lib/python2.6/site-packages/sage/all.py", line 64, in <module>
    from sage.misc.all       import *         # takes a while
  File "/Users/wstein/sage/build/64bit/sage/local/lib/python2.6/site-packages/sage/misc/all.py", line 16, in <module>
    from sage_timeit_class import timeit
  File "sage_timeit_class.pyx", line 3, in sage.misc.sage_timeit_class (sage/misc/sage_timeit_class.c:764)
  File "/Users/wstein/sage/build/64bit/sage/local/lib/python2.6/site-packages/sage/misc/sage_timeit.py", line 12, in <module>
    import timeit as timeit_, time, math, preparser, interpreter
  File "/Users/wstein/sage/build/64bit/sage/local/lib/python2.6/site-packages/sage/misc/interpreter.py", line 95, in <module>
    import IPython.ipapi
  File "/Users/wstein/sage/build/64bit/sage/local/lib/python2.6/site-packages/IPython/__init__.py", line 58, in <module>
    __import__(name,glob,loc,[])
  File "/Users/wstein/sage/build/64bit/sage/local/lib/python2.6/site-packages/IPython/Shell.py", line 45, in <module>
    from IPython.iplib import InteractiveShell
  File "/Users/wstein/sage/build/64bit/sage/local/lib/python2.6/site-packages/IPython/iplib.py", line 59, in <module>
    from sets import Set
ImportError: cannot import name Set
```

