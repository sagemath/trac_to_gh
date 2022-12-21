# Issue 8463: Test failure of sage/homology/delta_complex.py

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-03-06 23:23:12

Assignee: tbd

CC:  jhpalmieri

I'm getting lots of failures on a patched version of 4.3.4.alpha0 for many files related to homology:


```
        sage -t  -long "devel/sage/sage/homology/delta_complex.py"
        sage -t  -long "devel/sage/sage/homology/cubical_complex.py"
        sage -t  -long "devel/sage/sage/homology/examples.py"
        sage -t  -long "devel/sage/sage/homology/cell_complex.py"
        sage -t  -long "devel/sage/sage/homology/chain_complex.py"
        sage -t  -long "devel/sage/sage/homology/simplicial_complex.py"
```


The ones involving simplicial_complex.py all report 


```
OSError: [Errno 2] No such file or directory
```


See below for me detailed information. I think John deals with this sort of thing, but I don't even know what to classify it as, so I've stuck it on _doctest_.  


```

sage -t  -long "devel/sage/sage/homology/delta_complex.py"
**********************************************************************
File "/export/home/drkirkby/32/sage-4.3.4.alpha0/devel/sage/sage/homology/delta_complex.py", line 114:
    sage: S5.homology()
Exception raised:
    Traceback (most recent call last):
      File "/export/home/drkirkby/32/sage-4.3.4.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/drkirkby/32/sage-4.3.4.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/drkirkby/32/sage-4.3.4.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[5]>", line 1, in <module>
        S5.homology()###line 114:
    sage: S5.homology()
      File "/export/home/drkirkby/32/sage-4.3.4.alpha0/local/lib/python/site-packages/sage/homology/cell_complex.py", line 555, in homology
        answer = C.homology(**kwds)
      File "/export/home/drkirkby/32/sage-4.3.4.alpha0/local/lib/python/site-packages/sage/homology/chain_complex.py", line 721, in homology
        H = homchain(self, **kwds)
      File "/export/home/drkirkby/32/sage-4.3.4.alpha0/local/lib/python/site-packages/sage/interfaces/chomp.py", line 584, in homchain
        return CHomP()('homchain', complex, **kwds)
      File "/export/home/drkirkby/32/sage-4.3.4.alpha0/local/lib/python/site-packages/sage/interfaces/chomp.py", line 250, in __call__
        output = Popen(cmd, stdout=PIPE).communicate()[0]
      File "/export/home/drkirkby/32/sage-4.3.4.alpha0/local/lib/python2.6/subprocess.py", line 621, in __init__
        errread, errwrite)
      File "/export/home/drkirkby/32/sage-4.3.4.alpha0/local/lib/python2.6/subprocess.py", line 1126, in _execute_child
        raise child_exception
    OSError: [Errno 2] No such file or directory
**********************************************************************
File "/export/home/drkirkby/32/sage-4.3.4.alpha0/devel/sage/sage/homology/delta_complex.py", line 186:
    sage: P.homology(1)
Exception raised:
    Traceback (most recent call last):
      File "/export/home/drkirkby/32/sage-4.3.4.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/drkirkby/32/sage-4.3.4.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/drkirkby/32/sage-4.3.4.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[12]>", line 1, in <module>
        P.homology(Integer(1))###line 186:
    sage: P.homology(1)
      File "/export/home/drkirkby/32/sage-4.3.4.alpha0/local/lib/python/site-packages/sage/homology/cell_complex.py", line 555, in homology
        answer = C.homology(**kwds)
      File "/export/home/drkirkby/32/sage-4.3.4.alpha0/local/lib/python/site-packages/sage/homology/chain_complex.py", line 721, in homology
        H = homchain(self, **kwds)
      File "/export/home/drkirkby/32/sage-4.3.4.alpha0/local/lib/python/site-packages/sage/interfaces/chomp.py", line 584, in homchain
        return CHomP()('homchain', complex, **kwds)
      File "/export/home/drkirkby/32/sage-4.3.4.alpha0/local/lib/python/site-packages/sage/interfaces/chomp.py", line 250, in __call__
        output = Popen(cmd, stdout=PIPE).communicate()[0]
      File "/export/home/drkirkby/32/sage-4.3.4.alpha0/local/lib/python2.6/subprocess.py", line 621, in __init__
        errread, errwrite)
      File "/export/home/drkirkby/32/sage-4.3.4.alpha0/local/lib/python2.6/subprocess.py", line 1126, in _execute_child
        raise child_exception
    OSError: [Errno 2] No such file or directory
```




---

Comment by jhpalmieri created at 2010-03-07 05:18:27

I believe this should be fixed by the patch at #8474, which gets to the heart of the matter.


---

Comment by drkirkby created at 2010-03-07 14:47:02

As I commented on #8474, I not so convinced this is true at least now.


---

Comment by drkirkby created at 2010-03-09 03:18:20

This can now be closed, as #8474, does solve this.


---

Comment by drkirkby created at 2010-03-09 03:18:20

Changing assignee from tbd to drkirkby.


---

Comment by mvngu created at 2010-03-11 04:53:10

Close as fixed by #8474.


---

Comment by mvngu created at 2010-03-11 04:53:10

Resolution: fixed
