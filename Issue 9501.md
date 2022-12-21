# Issue 9501: Make an @fork decorator

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-07-14 22:32:17

Assignee: jason

CC:  mvngu

Simon King mentioned that sometimes his code crashes/leaks/etc.  So make it so one can do:

```
`@`fork
def f(x,y,z,...):
    ...
```

and then f gets computed in a blocking forked process, and the result is returned via pickling. This is 100% to thwart mem leaks, segfaults, and guaranteed timeout possibility.   This could be basically just a light wrapper around `@`parallel(1).  Also, make a global flag to turn this off, so `@`fork does nothing.


---

Comment by was created at 2010-07-14 23:05:55

Keep in mind #8410, though this doesn't depend on that.

See http://sagenb.org/home/pub/2248/ for a demo.


---

Comment by was created at 2010-07-15 18:31:20

The code is a little longer than necessary, since:


   * I improved the documentation and doctesting to get coverage to 100% (it wasn't really before).

   * I implemented an option to not kill the interfaces, but it's not used.  It could be useful for some users.


---

Comment by was created at 2010-07-15 18:31:20

Changing status from new to needs_review.


---

Comment by malb created at 2010-07-15 18:56:44


```
File "/mnt/usb1/scratch/malb/sage-4.4/devel/sage/sage/parallel/decorate.py", line 292:

    sage: g()

Expected:

    '10'

Got:

    [Errno 16] Device or resource busy: '/home/malb/.sage/temp/sage.math.washington.edu/29514/dir_0/.nfs000000000482d3cd00028d9f'

    '10'

**********************************************************************

File "/mnt/usb1/scratch/malb/sage-4.4/devel/sage/sage/parallel/decorate.py", line 303:

    sage: g()

Expected:

    'a'

Got:

    [Errno 16] Device or resource busy: '/home/malb/.sage/temp/sage.math.washington.edu/29514/dir_1/.nfs000000000482d3d300028da0'

    'a'


```



---

Comment by malb created at 2010-07-15 18:58:50

* the timeout documentation should mention that 0 means Infinity
 * the fork decorator talks about parallel subprocesses (copy 'n' paste oversight)
 * I don't know whether the above failures are a real issue or not

If these are addressed I'm happy to give this a positive review.


---

Comment by malb created at 2010-07-15 19:14:39

William and I discussed the doctest failure and tried it again: we couldn't reproduce it so we assume it's okay for now, the machine (disk?) was just quite busy.


---

Comment by malb created at 2010-07-15 19:20:40

Changing status from needs_review to positive_review.


---

Comment by SimonKing created at 2010-07-15 19:30:11

William, you just mentioned that you have not added a doctest illustrating that a segmentation fault is no disaster when one uses the fork decorator. But in the worksheet you link at, there is a segfaulting example. So, why not add such thing as a doctest?


---

Comment by was created at 2010-07-15 23:53:52

SimonKing -- that's a good idea.  I've refreshed the patch with this example.


---

Attachment


---

Comment by was created at 2010-07-15 23:54:39

Changing status from positive_review to needs_work.


---

Comment by was created at 2010-07-15 23:54:46

Changing status from needs_work to needs_review.


---

Comment by malb created at 2010-07-16 08:30:19

Changing status from needs_review to positive_review.


---

Comment by malb created at 2010-07-16 08:30:19

Patch looks good, tests passed.


---

Comment by kcrisman created at 2010-07-16 14:12:13

I think the 'warning' sections need to be in proper REsT format, which I *think* (but won't guarantee) should look more like

```
.. warning::
```

or something like that.  I'm cc:ing mvngu since he will know :)


---

Comment by kcrisman created at 2010-07-16 14:12:13

Changing status from positive_review to needs_work.


---

Comment by mvngu created at 2010-07-17 02:23:50

Replying to [comment:12 kcrisman]:
> I think the 'warning' sections need to be in proper REsT format, which I *think* (but won't guarantee) should look more like

```
.. warning::
```

> or something like that.

That's right. See [this section](http://sphinx.pocoo.org/markup/para.html#dir-warning) of the Sphinx reference manual.


---

Attachment

new version with fixed warnings.


---

Comment by was created at 2010-07-17 12:53:39

Changing status from needs_work to needs_review.


---

Comment by malb created at 2010-07-18 14:20:18

Looks good, but the file doesn't seem to be included in the reference manual anyway.


---

Comment by malb created at 2010-07-21 12:39:54

Changing status from needs_review to positive_review.


---

Comment by ddrake created at 2010-07-22 08:32:08

Resolution: fixed


---

Comment by ddrake created at 2010-07-22 08:32:08

Merged trac_9501.2.patch in 4.5.2.alpha1.


---

Comment by mpatel created at 2010-08-08 22:09:17

This ticket was backed out at #9616.  The new ticket for merging this is #9631.
