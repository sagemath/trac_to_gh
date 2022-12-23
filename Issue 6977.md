# Issue 6977: Implement __len__ to add support for MuPAD objects as Python containers

Issue created by migration from https://trac.sagemath.org/ticket/6977

Original creator: nthiery

Original creation time: 2009-09-21 13:43:23

Assignee: was

CC:  mhansen@gmail.com sage-combinat

Keywords: MuPAD len

The title says it all; after the patch, one can do:

            sage: len(mupad([1,2,3]))
            3
            sage: map(ZZ, list(mupad([1,2,3])))
            [1, 2, 3]




---

Comment by nthiery created at 2009-09-21 19:35:02

Changing status from new to assigned.


---

Comment by nthiery created at 2009-09-21 19:35:02

Changing assignee from was to nthiery.


---

Comment by mhansen created at 2009-09-26 03:44:40

Looks good to me.  There should be double colons after EXAMPLES, but since the rest of the file hasn't been converted over, we can wait to fix it then.


---

Comment by mvngu created at 2009-09-26 08:40:08

Any doctest involving MuPAD must be tagged as optional, otherwise one would get doctest failures. For example, for the patch `trac_6977_mupad_len.patch` the test

```
sage: len(mupad([1,2,3])) # indirect doctest
```

depends on having MuPAD one's local machine, so it should be written as

```
sage: len(mupad([1,2,3])) # optional indirect doctest
```

After applying the patch, I got these doctest failures:

```
sage -t -long devel/sage/sage/interfaces/mupad.py
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha2/devel/sage-main/sage/interfaces/mupad.py", line 599:
    sage: len(mupad([1,2,3])) # indirect doctest
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_34[2]>", line 1, in <module>
        len(mupad([Integer(1),Integer(2),Integer(3)])) # indirect doctest###line 599:
    sage: len(mupad([1,2,3])) # indirect doctest
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python/site-packages/sage/interfaces/expect.py", line 1044, in __call__
        raise TypeError, msg
    TypeError: Unable to start MuPAD because the command 'mupkern -P e -U SAGE=TRUE' failed.

    In order to use the MuPAD interface you need to have MuPAD installed
    and have a script in your PATH called "mupkern" that runs the
    command-line version of MuPAD. 

      (1) You might have to buy MuPAD.
          
      (2) * LINUX: The mupkern script comes standard with your Mupad install.
            
          * APPLE OS X:
             ???

**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha2/devel/sage-main/sage/interfaces/mupad.py", line 601:
    sage: type(len(mupad([1,2,3])))
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_34[3]>", line 1, in <module>
        type(len(mupad([Integer(1),Integer(2),Integer(3)])))###line 601:
    sage: type(len(mupad([1,2,3])))
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python/site-packages/sage/interfaces/expect.py", line 1044, in __call__
        raise TypeError, msg
    TypeError: Unable to start MuPAD because the command 'mupkern -P e -U SAGE=TRUE' failed.

    In order to use the MuPAD interface you need to have MuPAD installed
    and have a script in your PATH called "mupkern" that runs the
    command-line version of MuPAD. 

      (1) You might have to buy MuPAD.
          
      (2) * LINUX: The mupkern script comes standard with your Mupad install.
            
          * APPLE OS X:
             ???

**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha2/devel/sage-main/sage/interfaces/mupad.py", line 604:
    sage: len(mupad(4))
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_34[4]>", line 1, in <module>
        len(mupad(Integer(4)))###line 604:
    sage: len(mupad(4))
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python/site-packages/sage/interfaces/expect.py", line 1033, in __call__
        return self._coerce_from_special_method(x)
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python/site-packages/sage/interfaces/expect.py", line 1059, in _coerce_from_special_method
        return self(x._interface_init_())
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python/site-packages/sage/interfaces/expect.py", line 1031, in __call__
        return cls(self, x, name=name)
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python/site-packages/sage/interfaces/expect.py", line 1447, in __init__
        raise TypeError, x
    TypeError: Unable to start MuPAD because the command 'mupkern -P e -U SAGE=TRUE' failed.

    In order to use the MuPAD interface you need to have MuPAD installed
    and have a script in your PATH called "mupkern" that runs the
    command-line version of MuPAD. 

      (1) You might have to buy MuPAD.
          
      (2) * LINUX: The mupkern script comes standard with your Mupad install.
            
          * APPLE OS X:
             ???

**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha2/devel/sage-main/sage/interfaces/mupad.py", line 610:
    sage: map(ZZ, list(mupad([1,2,3])))
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_34[5]>", line 1, in <module>
        map(ZZ, list(mupad([Integer(1),Integer(2),Integer(3)])))###line 610:
    sage: map(ZZ, list(mupad([1,2,3])))
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python/site-packages/sage/interfaces/expect.py", line 1044, in __call__
        raise TypeError, msg
    TypeError: Unable to start MuPAD because the command 'mupkern -P e -U SAGE=TRUE' failed.

    In order to use the MuPAD interface you need to have MuPAD installed
    and have a script in your PATH called "mupkern" that runs the
    command-line version of MuPAD. 

      (1) You might have to buy MuPAD.
          
      (2) * LINUX: The mupkern script comes standard with your Mupad install.
            
          * APPLE OS X:
             ???

**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha2/devel/sage-main/sage/interfaces/mupad.py", line 613:
    sage: [int(x) for x in mupad([1,2,3]) ]
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_34[6]>", line 1, in <module>
        [int(x) for x in mupad([Integer(1),Integer(2),Integer(3)]) ]###line 613:
    sage: [int(x) for x in mupad([1,2,3]) ]
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python/site-packages/sage/interfaces/expect.py", line 1044, in __call__
        raise TypeError, msg
    TypeError: Unable to start MuPAD because the command 'mupkern -P e -U SAGE=TRUE' failed.

    In order to use the MuPAD interface you need to have MuPAD installed
    and have a script in your PATH called "mupkern" that runs the
    command-line version of MuPAD. 

      (1) You might have to buy MuPAD.
          
      (2) * LINUX: The mupkern script comes standard with your Mupad install.
            
          * APPLE OS X:
             ???

**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha2/devel/sage-main/sage/interfaces/mupad.py", line 616:
    sage: [int(x) for x in mupad("{1,2,3,5}") ]
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_34[7]>", line 1, in <module>
        [int(x) for x in mupad("{1,2,3,5}") ]###line 616:
    sage: [int(x) for x in mupad("{1,2,3,5}") ]
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python/site-packages/sage/interfaces/expect.py", line 1031, in __call__
        return cls(self, x, name=name)
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python/site-packages/sage/interfaces/expect.py", line 1447, in __init__
        raise TypeError, x
    TypeError: Unable to start MuPAD because the command 'mupkern -P e -U SAGE=TRUE' failed.

    In order to use the MuPAD interface you need to have MuPAD installed
    and have a script in your PATH called "mupkern" that runs the
    command-line version of MuPAD. 

      (1) You might have to buy MuPAD.
          
      (2) * LINUX: The mupkern script comes standard with your Mupad install.
            
          * APPLE OS X:
             ???

**********************************************************************
1 items had failures:
   6 of   8 in __main__.example_34
***Test Failed*** 6 failures.
For whitespace errors, see the file /home/mvngu/.sage//tmp/.doctest_mupad.py
	 [2.0 s]
```



---

Attachment


---

Comment by nthiery created at 2009-09-30 10:23:39

The updated version adds
 - The missing #optional flags, the missing '::' (Oops, thanks Minh & Mike for the review and spotting those)
 - Fixes the implementation of len (bigger Oops: with MuPAD-Combinat, l := [1,2,3]; l::nops gives FAIL!!!!)
 - Add a comment about another failing test

Now: should this be seen as a bug fix or enhancement ? I.e. go through the feature freeze for 4.1.2? It does not risk to break much anyway.


---

Comment by mhansen created at 2009-10-05 07:34:16

Looks good.


---

Comment by mhansen created at 2009-10-15 08:53:27

Resolution: fixed
