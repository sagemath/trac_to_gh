# Issue 4411: phc breaks on one-variable problems

Issue created by migration from Trac.

Original creator: mhampton

Original creation time: 2008-10-31 12:54:55

Assignee: mhampton

Keywords: phc, phcpack, numerical, polynomial

phcpack uses a different method and different output for 1-variable problems, which breaks a lot of the assumptions in the interface.  I will ask Jan Verschelde if it is possible to harmonize the output, otherwise I will add some special-casing code to the interface.


---

Comment by mhampton created at 2008-10-31 12:55:08

Changing status from new to assigned.


---

Comment by mhampton created at 2011-01-11 23:08:38

Fixes 1-variable problems with phc


---

Comment by mhampton created at 2011-01-11 23:09:22

Changing status from new to needs_review.


---

Attachment

Here's an example for testing:

```
R1.<t> = PolynomialRing(QQ)
start_sys1 = [t^15-t-1]             
sol = phc.blackbox(start_sys1, R1, verbose=False)        
len(sol.solutions())
```

should give 15.


---

Comment by mhampton created at 2011-01-12 00:01:37

Oops, for the above snippet you need to first import phc:

```
from sage.interfaces.phc import phc
```


and have the phc optional spkg installed.


---

Comment by mhampton created at 2011-01-12 00:54:07

Changing component from interfaces to optional packages.


---

Comment by dimpase created at 2011-01-12 20:45:45

current spkg does not work on MacOSX 10.6. Will need an update...


---

Comment by dimpase created at 2011-01-13 19:09:59

Changing status from needs_review to needs_work.


---

Comment by dimpase created at 2011-01-13 19:09:59

Replying to [comment:6 dimpase]:
> current spkg does not work on MacOSX 10.6. Will need an update...

The new spkg (Marshall, could you post a link to it?) breaks parts of the current code, as some outputs(?) did change.


---

Comment by mhampton created at 2011-03-26 16:45:20

Changing status from needs_work to needs_review.


---

Comment by mhampton created at 2011-03-26 16:47:06

For this patch, the optional spkg from ticket #10607 should be used.  

[http://sage.math.washington.edu/home/mhampton/phc-2.3.60.spkg](http://sage.math.washington.edu/home/mhampton/phc-2.3.60.spkg)


---

Comment by mhampton created at 2011-03-26 16:55:48

Tested so far on OS X 10.6 and linux (64-bit).


---

Comment by mhampton created at 2011-03-27 01:52:37

This (and 10607) also work on Solaris (tested on mark on skynet) in addition to OS X 10.6 and linux.


---

Comment by jhpalmieri created at 2011-07-15 02:28:29

A few comments: the variable `real_tol` needs to be documented.  Also, the examples should probably be marked "optional: phc" instead of just "optional".

In the documentation it says "A dictionary of lists if dictionaries of solutions, classified by type.".  Should the word "if" be "of"?

You've changed the functions `get_solution_dicts` and `get_classified_solution_dicts`; can you add some doctests to illustrate and test the changes?


---

Attachment

updated patch for both 4411 and 10607


---

Comment by mhampton created at 2011-08-05 03:04:03

I think I've addressed all of your comments.  The changes to get_solution_dicts and get_classified_solution_dicts are mostly trivial, just to handle to minor differences in output of phcpack for the 1-variable case.


---

Comment by vbraun created at 2012-05-17 22:35:15

patch doesn't apply to sage-5.0, I get a rejected hunk.


---

Attachment

rebased cumulative patch for #4411 and #10607, for sage-5.0


---

Comment by mhampton created at 2012-05-28 20:21:26

Replying to [comment:16 vbraun]:
> patch doesn't apply to sage-5.0, I get a rejected hunk.

Okay, I fixed that and updated the description to point to a more recent phcpack spkg.  Please try again!  It would be depressing for this to rot again.


---

Comment by jhpalmieri created at 2012-06-12 21:08:30

I just posted a new spkg to #10607, since the old one wasn't building on my OS X Lion machine. I don't know what this package is doing, but all optional tests pass for me with the patch here and the spkg from #10607.


---

Comment by vbraun created at 2012-10-23 19:34:24

Looks good to me!


---

Comment by vbraun created at 2012-10-23 19:34:24

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2012-10-23 19:59:48

I get the following doctest error on Sage-5.4.rc1, perhaps it has something to do with #13579?

```
[vbraun`@`volker-desktop hg]$ sage -t -only-optional=phc --verbose devel/sage-main/sage/interfaces/phc.py
sage -t -only-optional=phc --verbose "devel/sage-main/sage/interfaces/phc.py"
Trying:
    set_random_seed(0L)
Expecting nothing
ok
Trying:
    change_warning_output(sys.stdout)
Expecting nothing
ok
Trying:
    from sage.interfaces.phc import *         #optional: phc###line 56:_sage_    >>> from sage.interfaces.phc import *         #optional: phc
Expecting nothing
ok
Trying:
    R2 = PolynomialRing(QQ,Integer(2), names=('x1', 'x2',)); (x1, x2,) = R2._first_ngens(2)#optional: phc###line 57:_sage_    >>> R2.<x1,x2> = PolynomialRing(QQ,2)         #optional: phc
Expecting nothing
ok
Trying:
    test_sys = [(x1-Integer(1))**Integer(5)-x2, (x2-Integer(1))**Integer(5)-Integer(1)] #optional: phc###line 58:_sage_    >>> test_sys = [(x1-1)^5-x2, (x2-1)^5-1] #optional: phc
Expecting nothing
ok
Trying:
    sol = phc.blackbox(test_sys, R2)          #optional: phc###line 59:_sage_    >>> sol = phc.blackbox(test_sys, R2)          #optional: phc
Expecting nothing

There exists already a file named /home/vbraun/.sage/temp/volker_desktop.stp.dias.ie/21208/tmp_filename-SmhVtI
Do you want to destroy this file ? (y/n) y
```



---

Comment by vbraun created at 2012-10-23 19:59:48

Changing status from positive_review to needs_work.


---

Comment by jhpalmieri created at 2012-10-25 20:27:18

Yes, I guess that since `tmp_filename` now creates the file in addition to returning its path, it causes the problem. Here's a patch. (There are other things which could be cleaned up, for example `log_filename` is never used, but I'm not going to bother.)


---

Comment by jhpalmieri created at 2012-10-25 20:27:18

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by mhampton created at 2012-12-21 14:45:48

That does solve this new filename problem. This ticket should have been closed with 10607, but wasn't, so now I guess it can serve this new purpose of fixing the tmp file problem.


---

Comment by mhampton created at 2012-12-21 14:46:18

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-12-26 16:18:45

Changing component from optional packages to interfaces.


---

Comment by jdemeyer created at 2012-12-27 10:24:36

Resolution: fixed
