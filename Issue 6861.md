# Issue 6861: allow users to test Sage script using system-wide Sage installation

Issue created by migration from https://trac.sagemath.org/ticket/6861

Original creator: mvngu

Original creation time: 2009-09-02 04:47:07

Assignee: tbd

At least in Sage 4.1.1, a regular user cannot run tests on their own Sage scripts using a system-wide installation of Sage. Doing so would result in a permission error:

```
[mvngu@mod mvngu]$ cat demo.sage 
print 2
[mvngu@mod mvngu]$ sage -t demo.sage 
Traceback (most recent call last):
  File "/usr/local/sage/local/bin/sage-test", line 49, in <module>
    os.makedirs(TMP)
  File "/usr/local/sage/local/lib/python/os.py", line 157, in makedirs
    mkdir(name, mode)
OSError: [Errno 13] Permission denied: '/usr/local/sage/tmp/tmp'
```

That is due to the testing script writing temporary data to a temporary directory under the system-wide Sage installation. A work around is to have one's own local installation of Sage under one's home directory. But it would be nice if the test script would write temporary data to the user's `DOT_SAGE` directory, i.e. `$HOME/.sage`. This problem was reported at this [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/af6d95445f76cbe9) thread.


---

Attachment


---

Attachment

The two files above are identical.  One can be deleted.


---

Comment by fwclarke created at 2009-09-03 07:27:29

Replying to [comment:1 jason]:

In addition to the change made by the patch, some corresponding changes need making in `sage-test` and `sage-doctest`.  Moreover, testing of one's own Sage scripts won't work until the changes in #6668 are also implemented (most particularly the change to line 408 of `sage-doctest`).


---

Comment by jason created at 2009-09-03 07:50:24

Replying to [comment:2 fwclarke]:
> Replying to [comment:1 jason]:
> 
> In addition to the change made by the patch, some corresponding changes need making in `sage-test` and `sage-doctest`.  Moreover, testing of one's own Sage scripts won't work until the changes in #6668 are also implemented (most particularly the change to line 408 of `sage-doctest`). 


You sound like you know what needs to be done.  Please, please post a patch.


---

Comment by fwclarke created at 2009-09-03 07:58:58

Replying to [comment:3 jason]:
> You sound like you know what needs to be done.  Please, please post a patch.

Will do, but not immediately; there are a few things I don't quite understand, and I'm off to the day-job now.


---

Comment by fwclarke created at 2009-09-05 18:41:01

Replying to [comment:4 fwclarke]:
 
> There are a few things I don't quite understand ...

It seems to me that if (because of the changed definition of `SAGE_TESTDIR`) the directory `~/.sage/tmp` is to be used for testing system files, then logically it should also be used for testing users' own files.  This requires a few more changes.    

It also seems worthwhile to active the function `delete_tmpfiles` in `sage-doctest`; at present this function does nothing.  The obvious things is for it to get called if the doctest succeeds without any failures, but at present the method of counting the number of failures is defective.

I have implemented these ideas and am testing the code.  A patch will follow soon.


---

Comment by fwclarke created at 2009-09-05 22:43:31

The new patch, which incorporates the change in the earlier patch, also includes the changes made in the patch at #6668.


---

Comment by fwclarke created at 2009-09-05 22:44:43

replaces earlier patches


---

Attachment

I have added an extra patch (to be applied after trac_6861_new.patch) which deals with a problem in testing files specified by their full path name, as [discussed](http://groups.google.com/group/sage-devel/browse_thread/thread/6295a62c30f5edca) in sage-devel.


---

Attachment

apply after trac_6861_new.patch


---

Comment by timdumol created at 2009-09-23 12:52:32

Patches work perfectly, and I've run several dozen doctests without any problems. Temporary files are deleted as promised. Nice job guys. Positive review.


---

Comment by mvngu created at 2009-09-24 11:02:02

Merged in the script repository.


---

Comment by mvngu created at 2009-09-24 11:02:02

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 10:20:51

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.


---

Comment by mvngu created at 2009-09-30 07:17:50

See #7079 for a case where the current ticket breaks parallel doctesting.
