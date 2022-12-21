# Issue 4025: Sage 3.1.2.alpha3: benchmark.py runs Maple tests that should be optional

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-08-31 22:43:27

Assignee: mabshoff

CC:  wjp

John Cremona reported:

```
********************************************************************** 
File "/home/jec/sage-3.1.2.alpha3/tmp/benchmark.py", line 624: 
    sage: isinstance(B.maple()[1], float) 
Exception raised: 
    Traceback (most recent call last): 
      File "/home/jec/sage-3.1.2.alpha3/local/lib/python2.5/doctest.py", 
line 1228, in __run 
        compileflags, 1) in test.globs 
      File "<doctest __main__.example_25[4]>", line 1, in <module> 
        isinstance(B.maple()[Integer(1)], float)###line 624: 
    sage: isinstance(B.maple()[1], float) 
      File "/home/jec/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/tests/b enchmark.py", 
line 636, in maple 
        z0 = maple(str(z0)) 
      File "/home/jec/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/interfa ces/expect.py", 
line 963, in __call__ 
        return cls(self, x, name=name) 
      File "/home/jec/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/interfa ces/expect.py", 
line 1261, in __init__ 
        raise TypeError, x 
    TypeError: Unable to start maple because the command 'maple -t' failed. 
    In order to use the Maple interface you need to have Maple installed 
    and have a script in your PATH called "maple" that runs the 
    command-line version of Maple.  Alternatively, you could use a remote 
    connection to a server running Maple; for hints, type 
        print maple._install_hints_ssh() 
      (1) You might have to buy Maple (http://webstore.maplesoft.com/). 
      (2) * LINUX: The maple script comes standard with your Maple install. 
          * APPLE OS X: 
              (a) create a file called maple (in your PATH), with the 
following contents: 
                 #!/bin/sh 
/Library/Frameworks/Maple.framework/Versions/Current/bin/maple $`@` 
              (b) Save the file. 
              (c) Make the file executable. 
                    chmod +x maple 
          * WINDOWS: 
            You must install Maple-for-Linux into the VMware machine 
(sorry, that's 
            the only way at present). 
********************************************************************** 
File "/home/jec/sage-3.1.2.alpha3/tmp/benchmark.py", line 964: 
    sage: isinstance(B.maple()[1], float) 
Exception raised: 
    Traceback (most recent call last): 
      File "/home/jec/sage-3.1.2.alpha3/local/lib/python2.5/doctest.py", 
line 1228, in __run 
        compileflags, 1) in test.globs 
      File "<doctest __main__.example_41[4]>", line 1, in <module> 
        isinstance(B.maple()[Integer(1)], float)###line 964: 
    sage: isinstance(B.maple()[1], float) 
      File "/home/jec/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/tests/b enchmark.py", 
line 968, in maple 
        n = maple('%s^%s'%(self.base,self.__ndigits)) 
      File "/home/jec/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/interfa ces/expect.py", 
line 963, in __call__ 
        return cls(self, x, name=name) 
      File "/home/jec/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/interfa ces/expect.py", 
line 1261, in __init__ 
        raise TypeError, x 
    TypeError: Unable to start maple because the command 'maple -t' failed. 
    In order to use the Maple interface you need to have Maple installed 
    and have a script in your PATH called "maple" that runs the 
    command-line version of Maple.  Alternatively, you could use a remote 
    connection to a server running Maple; for hints, type 
        print maple._install_hints_ssh() 
      (1) You might have to buy Maple (http://webstore.maplesoft.com/). 
      (2) * LINUX: The maple script comes standard with your Maple install. 
          * APPLE OS X: 
              (a) create a file called maple (in your PATH), with the 
following contents: 
                 #!/bin/sh 
/Library/Frameworks/Maple.framework/Versions/Current/bin/maple $`@` 
              (b) Save the file. 
              (c) Make the file executable. 
                    chmod +x maple 
          * WINDOWS: 
            You must install Maple-for-Linux into the VMware machine 
(sorry, that's 
            the only way at present). 
********************************************************************** 
File "/home/jec/sage-3.1.2.alpha3/tmp/benchmark.py", line 1125: 
    sage: isinstance(B.maple()[1], float) 
Exception raised: 
    Traceback (most recent call last): 
      File "/home/jec/sage-3.1.2.alpha3/local/lib/python2.5/doctest.py", 
line 1228, in __run 
        compileflags, 1) in test.globs 
      File "<doctest __main__.example_50[4]>", line 1, in <module> 
        isinstance(B.maple()[Integer(1)], float)###line 1125: 
    sage: isinstance(B.maple()[1], float) 
      File "/home/jec/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/tests/b enchmark.py", 
line 1129, in maple 
        n = maple(self.__n) 
      File "/home/jec/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/interfa ces/expect.py", 
line 965, in __call__ 
        return self._coerce_from_special_method(x) 
      File "/home/jec/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/interfa ces/expect.py", 
line 989, in _coerce_from_special_method 
        return (x.__getattribute__(s))(self) 
      File "sage_object.pyx", line 333, in 
sage.structure.sage_object.SageObject._maple_ 
(sage/structure/sage_object.c:3483) 
      File "sage_object.pyx", line 246, in 
sage.structure.sage_object.SageObject._interface_ 
(sage/structure/sage_object.c:2184) 
      File "/home/jec/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/interfa ces/expect.py", 
line 963, in __call__ 
        return cls(self, x, name=name) 
      File "/home/jec/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/interfa ces/expect.py", 
line 1261, in __init__ 
        raise TypeError, x 
    TypeError: Unable to start maple because the command 'maple -t' failed. 
    In order to use the Maple interface you need to have Maple installed 
    and have a script in your PATH called "maple" that runs the 
    command-line version of Maple.  Alternatively, you could use a remote 
    connection to a server running Maple; for hints, type 
        print maple._install_hints_ssh() 
      (1) You might have to buy Maple (http://webstore.maplesoft.com/). 
      (2) * LINUX: The maple script comes standard with your Maple install. 
          * APPLE OS X: 
              (a) create a file called maple (in your PATH), with the 
following contents: 
                 #!/bin/sh 
/Library/Frameworks/Maple.framework/Versions/Current/bin/maple $`@` 
              (b) Save the file. 
              (c) Make the file executable. 
                    chmod +x maple 
          * WINDOWS: 
            You must install Maple-for-Linux into the VMware machine 
(sorry, that's 
            the only way at present). 
********************************************************************** 
```



---

Comment by mabshoff created at 2008-08-31 22:43:37

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-09-01 01:36:27

Patch is up. Please review.

Cheers,

Michael


---

Attachment


---

Comment by wdj created at 2008-09-01 01:43:47

This did better (the unpatched sage failed 5 tests in benchmark) but still failed for me on amd64, hardy heron:


```

wdj`@`hera:~/sagefiles/sage-3.1.2.alpha3$ ./sage -t  devel/sage/sage/tests/benchmark.py
sage -t  devel/sage/sage/tests/benchmark.py                 **********************************************************************
File "/home/wdj/sagefiles/sage-3.1.2.alpha3/tmp/benchmark.py", line 332:
    sage: isinstance(B.maple()[1], float)
Exception raised:
    Traceback (most recent call last):
      File "/home/wdj/sagefiles/sage-3.1.2.alpha3/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_14[4]>", line 1, in <module>
        isinstance(B.maple()[Integer(1)], float)###line 332:
    sage: isinstance(B.maple()[1], float)
      File "/home/wdj/sagefiles/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/tests/benchmark.py", line 337, in maple
        z = maple(str(sum(R.gens())))
      File "/home/wdj/sagefiles/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 963, in __call__
        return cls(self, x, name=name)
      File "/home/wdj/sagefiles/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1261, in __init__
        raise TypeError, x
    TypeError: Unable to start maple because the command 'maple -t' failed.


    In order to use the Maple interface you need to have Maple installed
    and have a script in your PATH called "maple" that runs the
    command-line version of Maple.  Alternatively, you could use a remote
    connection to a server running Maple; for hints, type
        print maple._install_hints_ssh()

      (1) You might have to buy Maple (http://webstore.maplesoft.com/).

      (2) * LINUX: The maple script comes standard with your Maple install.

          * APPLE OS X:
              (a) create a file called maple (in your PATH), with the following contents:
                 #!/bin/sh
                 /Library/Frameworks/Maple.framework/Versions/Current/bin/maple $`@`
              (b) Save the file.
              (c) Make the file executable.
                    chmod +x maple

          * WINDOWS:
            You must install Maple-for-Linux into the VMware machine (sorry, that's
            the only way at present).

**********************************************************************
File "/home/wdj/sagefiles/sage-3.1.2.alpha3/tmp/benchmark.py", line 429:
    sage: isinstance(B.maple()[1], float)
Exception raised:
    Traceback (most recent call last):
      File "/home/wdj/sagefiles/sage-3.1.2.alpha3/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_18[4]>", line 1, in <module>
        isinstance(B.maple()[Integer(1)], float)###line 429:
    sage: isinstance(B.maple()[1], float)
      File "/home/wdj/sagefiles/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/tests/benchmark.py", line 435, in maple
        z0 = maple(str(sum(R.gens()[:k])))
      File "/home/wdj/sagefiles/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 963, in __call__
        return cls(self, x, name=name)
      File "/home/wdj/sagefiles/sage-3.1.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1261, in __init__
        raise TypeError, x
    TypeError: Unable to start maple because the command 'maple -t' failed.


    In order to use the Maple interface you need to have Maple installed
    and have a script in your PATH called "maple" that runs the
    command-line version of Maple.  Alternatively, you could use a remote
    connection to a server running Maple; for hints, type
        print maple._install_hints_ssh()

      (1) You might have to buy Maple (http://webstore.maplesoft.com/).

      (2) * LINUX: The maple script comes standard with your Maple install.

          * APPLE OS X:
              (a) create a file called maple (in your PATH), with the following contents:
                 #!/bin/sh
                 /Library/Frameworks/Maple.framework/Versions/Current/bin/maple $`@`
              (b) Save the file.
              (c) Make the file executable.
                    chmod +x maple

          * WINDOWS:
            You must install Maple-for-Linux into the VMware machine (sorry, that's
            the only way at present).

**********************************************************************
2 items had failures:
   1 of   5 in __main__.example_14
   1 of   5 in __main__.example_18
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/wdj/sagefiles/sage-3.1.2.alpha3/tmp/.doctest_benchmark.py
         [6.6 s]
exit code: 1024

----------------------------------------------------------------------
The following tests failed:


        sage -t  devel/sage/sage/tests/benchmark.py
Total time for all tests: 6.6 seconds
```



---

Comment by mabshoff created at 2008-09-01 01:51:33

Mike found one issue while testing the patch, so he has updated the patch with an updated version. 

David: can you try again? It seems that the new patch and you testing happened simultaneously :)

Cheers,

Michael


---

Comment by wdj created at 2008-09-01 01:58:35

This second patch worked perfectly.


```
wdj`@`hera:~/sagefiles/sage-3.1.2.alpha3$ ./sage -t  devel/sage/sage/tests/benchmark.py
sage -t  devel/sage/sage/tests/benchmark.py
         [6.8 s]

----------------------------------------------------------------------
All tests passed!
Total time for all tests: 6.8 seconds

```



---

Comment by mabshoff created at 2008-09-01 02:19:14

Merged in Sage 3.1.2.alpha4


---

Comment by mabshoff created at 2008-09-01 02:19:14

Resolution: fixed
