# Issue 8834: make R png graphics doctests optional

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-05-01 06:14:29

Assignee: jason, was


```
Hi,

Continuing this thread, I think that building Sage shouldn't require X11.  E.g., on t2, the new R png tests fail:

File "/scratch/wstein/build/sage-4.4.1.alpha2/devel/sage/sage/interfaces/r.py", line 993:
    sage: r.png(filename='"%s"'%filename) # filename not needed in notebook, used for doctesting
Exception raised:
...
    sage: r.png(filename='"%s"'%filename) # filename not needed in notebook, used for doctesting
      File "/scratch/wstein/build/sage-4.4.1.alpha2/local/lib/python/site-packages/sage/interfaces/r.py
", line 356, in png
        raise RuntimeError, "R was not compiled with PNG support"
    RuntimeError: R was not compiled with PNG support
*******************************************************************

---

Unfortunately, this really means that those tests should all be changed to be 

   # optional -- x11

They won't get tested by "make test".  However, doing 

  ./sage -t -only_optional=x11 devel/sage/sage/

will test them.  The release manager checklist will suggest to do this check. 

I've opened a ticket for this:

```



---

Comment by drkirkby created at 2010-05-01 10:25:46

PNG libraries do exist on Solaris. Whether they are sufficiently new I don't know.


---

Comment by was created at 2010-05-01 18:58:52

Changing status from new to needs_review.


---

Comment by was created at 2010-05-01 18:58:52

There are *many* platforms -- even the latest OS X -- where our copy of R gets built without any graphics support (png or aqua or whatever). 

Having these tests exist, but get clearly marked #optional, will remind users that they are usually broken, and that we know this, at least until we fix this major issue.


---

Attachment


---

Comment by was created at 2010-05-01 19:01:39

How to test:

```
wstein`@`sage:~/build/release/4.4.1/sage-4.4.1.rc0$ ./sage -t devel/sage/sage/interfaces/r.py 
sage -t  "devel/sage/sage/interfaces/r.py"                  
         [4.2 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 4.2 seconds
wstein`@`sage:~/build/release/4.4.1/sage-4.4.1.rc0$ ./sage -t --only_optional=rgraphics devel/sage/sage/interfaces/r.py 
sage -t --only_optional=rgraphics "devel/sage/sage/interfaces/r.py"
         [3.3 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 3.3 seconds
wstein`@`sage:~/build/release/4.4.1/sage-4.4.1.rc0$ 
```



---

Comment by mvngu created at 2010-05-02 23:49:38

Resolution: fixed


---

Comment by mvngu created at 2010-05-02 23:49:38

Doctests pass on bsd.math (Mac OS X 10.6) with the option:

```
[mvngu`@`bsd sage-4.4.1.rc0]$ ./sage -t -long devel/sage-main/sage/interfaces/r.py
```

But doctests would fail with:

```
sage -t -long --only_optional=rgraphics "devel/sage-main/sage/interfaces/r.py"
**********************************************************************
File "/Users/mvngu/sandbox/sage-4.4.1.rc0/devel/sage-main/sage/interfaces/r.py", line 338:
    sage: r.png(filename='"%s"'%filename)             # optional -- rgraphics
Exception raised:
    Traceback (most recent call last):
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[3]>", line 1, in <module>
        r.png(filename='"%s"'%filename)             # optional -- rgraphics###line 338:
    sage: r.png(filename='"%s"'%filename)             # optional -- rgraphics
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/lib/python/site-packages/sage/interfaces/r.py", line 359, in png
        raise RuntimeError, "R was not compiled with PNG support"
    RuntimeError: R was not compiled with PNG support
**********************************************************************
File "/Users/mvngu/sandbox/sage-4.4.1.rc0/devel/sage-main/sage/interfaces/r.py", line 342:
    sage: r.plot(x,y) # This saves to filename, but is not viewable from command line; optional -- rgraphics
Expected:
    null device
              1
Got:
    Error: object 'sage8' not found
**********************************************************************
File "/Users/mvngu/sandbox/sage-4.4.1.rc0/devel/sage-main/sage/interfaces/r.py", line 345:
    sage: import os; os.unlink(filename) # We remove the file for doctesting; optional -- rgraphics
Exception raised:
    Traceback (most recent call last):
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[7]>", line 1, in <module>
        import os; os.unlink(filename) # We remove the file for doctesting; optional -- rgraphics###line 345:
    sage: import os; os.unlink(filename) # We remove the file for doctesting; optional -- rgraphics
    OSError: [Errno 2] No such file or directory: '/Users/mvngu/.sage//temp/bsd.local/96132//tmp_0.png'
**********************************************************************
File "/Users/mvngu/sandbox/sage-4.4.1.rc0/devel/sage-main/sage/interfaces/r.py", line 352:
    sage: "TRUE" in s+t                      # optional -- rgraphics
Expected:
    True
Got:
    False
**********************************************************************
File "/Users/mvngu/sandbox/sage-4.4.1.rc0/devel/sage-main/sage/interfaces/r.py", line 961:
    sage: r.plot("1:10")                # optional -- rgraphics
Expected:
    null device
              1
Got:
    [1] 4
**********************************************************************
File "/Users/mvngu/sandbox/sage-4.4.1.rc0/devel/sage-main/sage/interfaces/r.py", line 970:
    sage: r.png(filename='"%s"'%filename) # Note the double quotes in single quotes!; optional -- rgraphics
Exception raised:
    Traceback (most recent call last):
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[5]>", line 1, in <module>
        r.png(filename='"%s"'%filename) # Note the double quotes in single quotes!; optional -- rgraphics###line 970:
    sage: r.png(filename='"%s"'%filename) # Note the double quotes in single quotes!; optional -- rgraphics
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/lib/python/site-packages/sage/interfaces/r.py", line 359, in png
        raise RuntimeError, "R was not compiled with PNG support"
    RuntimeError: R was not compiled with PNG support
**********************************************************************
File "/Users/mvngu/sandbox/sage-4.4.1.rc0/devel/sage-main/sage/interfaces/r.py", line 974:
    sage: r.plot(x,y)         # optional -- rgraphics
Expected:
    null device
              1
Got:
    Error: object 'sage10' not found
**********************************************************************
File "/Users/mvngu/sandbox/sage-4.4.1.rc0/devel/sage-main/sage/interfaces/r.py", line 977:
    sage: import os; os.unlink(filename) # For doctesting, we remove the file; optional -- rgraphics
Exception raised:
    Traceback (most recent call last):
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[9]>", line 1, in <module>
        import os; os.unlink(filename) # For doctesting, we remove the file; optional -- rgraphics###line 977:
    sage: import os; os.unlink(filename) # For doctesting, we remove the file; optional -- rgraphics
    OSError: [Errno 2] No such file or directory: '/Users/mvngu/.sage//temp/bsd.local/96132//tmp_1.png'
**********************************************************************
File "/Users/mvngu/sandbox/sage-4.4.1.rc0/devel/sage-main/sage/interfaces/r.py", line 997:
    sage: r.png(filename='"%s"'%filename) # filename not needed in notebook, used for doctesting; optional -- rgraphics
Exception raised:
    Traceback (most recent call last):
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[11]>", line 1, in <module>
        r.png(filename='"%s"'%filename) # filename not needed in notebook, used for doctesting; optional -- rgraphics###line 997:
    sage: r.png(filename='"%s"'%filename) # filename not needed in notebook, used for doctesting; optional -- rgraphics
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/lib/python/site-packages/sage/interfaces/r.py", line 359, in png
        raise RuntimeError, "R was not compiled with PNG support"
    RuntimeError: R was not compiled with PNG support
**********************************************************************
File "/Users/mvngu/sandbox/sage-4.4.1.rc0/devel/sage-main/sage/interfaces/r.py", line 1000:
    sage: r("print(histogram(~wt | cyl, data=mtcars))") # plot should appear; optional -- rgraphics
Expected nothing
Got:
    [1] 4
**********************************************************************
File "/Users/mvngu/sandbox/sage-4.4.1.rc0/devel/sage-main/sage/interfaces/r.py", line 1001:
    sage: import os; os.unlink(filename) # We remove the file for doctesting, not needed in notebook;  optional -- rgraphics
Exception raised:
    Traceback (most recent call last):
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/mvngu/sandbox/sage-4.4.1.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[14]>", line 1, in <module>
        import os; os.unlink(filename) # We remove the file for doctesting, not needed in notebook;  optional -- rgraphics###line 1001:
    sage: import os; os.unlink(filename) # We remove the file for doctesting, not needed in notebook;  optional -- rgraphics
    OSError: [Errno 2] No such file or directory: '/Users/mvngu/.sage//temp/bsd.local/96132//tmp_2.png'
**********************************************************************
2 items had failures:
   4 of  11 in __main__.example_0
   7 of  15 in __main__.example_1
***Test Failed*** 11 failures.
For whitespace errors, see the file /Users/mvngu/.sage//tmp/.doctest_r.py
	 [3.0 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -long --only_optional=rgraphics "devel/sage-main/sage/interfaces/r.py"
Total time for all tests: 3.0 seconds
```

Making the specified doctests optional mean we're postponing a fix for the failure for a later time. Note that the above doctest failure is specific to Mac OS X as far as I can tell.


---

Comment by was created at 2010-05-03 03:31:50

> Making the specified doctests optional mean we're postponing a fix for the failure for a later time. 

I'm not so sure.  I'm still not convinced R can do any graphics on a system without X11 dev packages, which will not be a dependency for building Sage.   R graphics might always be optional on Linux.   I really hope I'm wrong!

> Note that the above doctest failure is specific to Mac OS X as far as I can tell.

They also happen on some Linux and Solaris boxes.


---

Comment by kcrisman created at 2010-05-03 14:50:43

Replying to [comment:6 was]:
> > Making the specified doctests optional mean we're postponing a fix for the failure for a later time. 
> 
> I'm not so sure.  I'm still not convinced R can do any graphics on a system without X11 dev packages, which will not be a dependency for building Sage.   R graphics might always be optional on Linux.   I really hope I'm wrong!

I am sure you are, having seen some workarounds on the internet.  But how to deal with this is something we need an R build expert for, I think.

Thanks to Minh for dealing with this - I was not able to deal with any Sage-devel related material this weekend.

> There are *many* platforms -- even the latest OS X -- where our copy of R gets built without any graphics support (png or aqua or whatever).
You mean OS X 10.6?  That's odd - that's where I did the main work for testing the new R spkg which should compile with aqua support whenever the system is 'Darwin'.


---

Comment by kcrisman created at 2010-05-03 14:52:12

Replying to [comment:7 kcrisman]:
> Replying to [comment:6 was]:
> > > Making the specified doctests optional mean we're postponing a fix for the failure for a later time. 
> > 
> > I'm not so sure.  I'm still not convinced R can do any graphics on a system without X11 dev packages, which will not be a dependency for building Sage.   R graphics might always be optional on Linux.   I really hope I'm wrong!
> 
> I am sure you are, having seen some workarounds on the internet.  But how to deal with this is something we need an R build expert for, I think.

Sorry, I mean wrong in the sense that R can do graphics in other ways, apparently.  I don't know whether it will allow capabilities() to return png support True without them, which is what I meant to say.


---

Comment by kcrisman created at 2010-05-03 19:11:59

Just putting things here because there isn't anywhere else convenient...  R install guide says:

```
Unless you do not want to view graphs on-screen you need ‘X11’ installed, including its headers and client libraries. For recent Fedora distributions it means (at least) ‘libX11’, ‘libX11-devel’, ‘libXt’ and ‘libXt-devel’. On Debian we recommend the meta-package ‘xorg-dev’. If you really do not want these you will need to explicitly configure R without X11, using --with-x=no.
```



---

Comment by kcrisman created at 2010-05-04 15:21:29

This continues at #8868.
