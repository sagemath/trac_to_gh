# Issue 5372: [with patch, needs review] Fix mwrank doctest in 3.4.alpha0

Issue created by migration from https://trac.sagemath.org/ticket/5372

Original creator: mhansen

Original creation time: 2009-02-25 18:28:43

Assignee: mabshoff


```
sage -t -long "devel/sage/sage/libs/mwrank/all.py"
**********************************************************************
File "/Applications/sage_builds/sage-3.4.alpha0-upgrade/devel/sage/
sage/libs/mwrank/all.py", line 26:
   sage: file= Sage_TMP + '/PRIMES'
Exception raised:
   Traceback (most recent call last):
     File "/Applications/sage_builds/sage-3.4.alpha0-upgrade/local/
bin/ncadoctest.py", line 1231, in run_one_test
       self.run_one_example(test, example, filename, compileflags)
     File "/Applications/sage_builds/sage-3.3.rc1/local/bin/
sagedoctest.py", line 38, in run_one_example
       OrigDocTestRunner.run_one_example(self, test, example,
filename, compileflags)
     File "/Applications/sage_builds/sage-3.4.alpha0-upgrade/local/
bin/ncadoctest.py", line 1172, in run_one_example
       compileflags, 1) in test.globs
     File "<doctest __main__.example_1[2]>", line 1, in <module>
       file= Sage_TMP + '/PRIMES'###line 26:
   sage: file= Sage_TMP + '/PRIMES'
   NameError: name 'Sage_TMP' is not defined
**********************************************************************
File "/Applications/sage_builds/sage-3.4.alpha0-upgrade/devel/sage/
sage/libs/mwrank/all.py", line 27:
   sage: open(file,'w').write(' '.join([str(p) for p in prime_range
(10^6)]))
Exception raised:
   Traceback (most recent call last):
     File "/Applications/sage_builds/sage-3.4.alpha0-upgrade/local/
bin/ncadoctest.py", line 1231, in run_one_test
       self.run_one_example(test, example, filename, compileflags)
     File "/Applications/sage_builds/sage-3.3.rc1/local/bin/
sagedoctest.py", line 38, in run_one_example
       OrigDocTestRunner.run_one_example(self, test, example,
filename, compileflags)
     File "/Applications/sage_builds/sage-3.4.alpha0-upgrade/local/
bin/ncadoctest.py", line 1172, in run_one_example
       compileflags, 1) in test.globs
     File "<doctest __main__.example_1[3]>", line 1, in <module>
       open(file,'w').write(' '.join([str(p) for p in prime_range
(Integer(10)**Integer(6))]))###line 27:
   sage: open(file,'w').write(' '.join([str(p) for p in prime_range
(10^6)]))
   TypeError: coercing to Unicode: need string or buffer, type found
**********************************************************************
File "/Applications/sage_builds/sage-3.4.alpha0-upgrade/devel/sage/
sage/libs/mwrank/all.py", line 28:
   sage: mwrank_initprimes(file, verb=False)
Exception raised:
   Traceback (most recent call last):
     File "/Applications/sage_builds/sage-3.4.alpha0-upgrade/local/
bin/ncadoctest.py", line 1231, in run_one_test
       self.run_one_example(test, example, filename, compileflags)
     File "/Applications/sage_builds/sage-3.3.rc1/local/bin/
sagedoctest.py", line 38, in run_one_example
       OrigDocTestRunner.run_one_example(self, test, example,
filename, compileflags)
     File "/Applications/sage_builds/sage-3.4.alpha0-upgrade/local/
bin/ncadoctest.py", line 1172, in run_one_example
       compileflags, 1) in test.globs
     File "<doctest __main__.example_1[4]>", line 1, in <module>
       mwrank_initprimes(file, verb=False)###line 28:
   sage: mwrank_initprimes(file, verb=False)
     File "/Applications/sage_builds/sage-3.4.alpha0-upgrade/local/
lib/python2.5/site-packages/sage/libs/mwrank/all.py", line 31, in
mwrank_initprimes
       return mwrank_initprimes(filename, verb)
     File "mwrank.pyx", line 119, in
sage.libs.mwrank.mwrank.initprimes (sage/libs/mwrank/mwrank.c:630)
     File "/Applications/sage_builds/sage-3.4.alpha0-upgrade/local/
lib/python2.5/posixpath.py", line 171, in exists
       st = os.stat(path)
   TypeError: coercing to Unicode: need string or buffer, type found
```



---

Attachment


---

Comment by mhansen created at 2009-02-25 18:45:24

Changing status from new to assigned.


---

Comment by mhansen created at 2009-02-25 18:45:24

Changing assignee from mabshoff to mhansen.


---

Comment by jsp created at 2009-02-26 14:31:35

After applying the patch:



```
sage -t -long "devel/sage/sage/libs/mwrank/all.py"          
	 [7.5 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 7.5 seconds

```


So a positive review.

Jaap


---

Comment by mabshoff created at 2009-02-28 16:22:40

Merged in Sage 3.4.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-28 16:22:40

Resolution: fixed
