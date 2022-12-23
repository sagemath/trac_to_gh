# Issue 9191: Running pyx files from the command line doesn't work anymore

Issue created by migration from https://trac.sagemath.org/ticket/9191

Original creator: was

Original creation time: 2010-06-09 02:02:52

Assignee: jason

Create a file like this:

```
flat:tmp wstein$ cat a.spyx
print "hello"
```


We have:

```
flat:tmp wstein$ sage a.spyx
Traceback (most recent call last):
  File "/Users/wstein/sage/build/sage/local/bin/sage-sagex", line 5, in <module>
    from sage.misc.interpreter import load_sagex
ImportError: cannot import name load_sagex
```


Note that .pyx files work fine:


```
flat:x wstein$ cp a.spyx a.pyx
flat:x wstein$ sage a.pyx
hello
```



---

Comment by kcrisman created at 2012-09-25 19:57:19

Well, no surprise!

```
sage: sage.misc.interpreter.loa[tab]
sage.misc.interpreter.load_a_file
sage.misc.interpreter.load_cython
sage.misc.interpreter.load_startup_file
sage.misc.interpreter.load_wrap
```

This is a very easy fix, as it turns out.  I haven't got a clue how to doctest it, though.


---

Comment by kcrisman created at 2012-09-25 19:58:14


```
GC04855:sage-5.4.beta1-again $ ./sage a.spyx 
Compiling a.spyx...
hello
```

It works.  Needs review.


---

Comment by kcrisman created at 2012-09-25 20:17:09

Changing status from new to needs_review.


---

Attachment

I expanded on your patch, added a doctest, renamed `sage-sagex` to `sage-run-cython`.


---

Comment by kcrisman created at 2012-09-27 15:57:08

Wow, nice work!  Very minor concerns below.

----

I'm a little concerned about why .pyx files worked before anyway.  Did it just make it to the 

```
os.execv(os.path.join(binpath, 'sage-python'), ['sage-python', fn] + opts)
```

line and `sage -python` (which is all `sage-python` is) just knew what to do with it?  And this is better for some reason for pyx files, right?

Also, any reason for making the messages print to stderr when they aren't errors?  As well as for changing things to the 'new' print statements?  I guess you did the work so I shouldn't complain :) but it always means I worry about missing some small detail.

Finally, if you're going to add pyx files to those which this command does, you should probably add a testing part to the doctest patch for that as well...


---

Comment by jdemeyer created at 2012-09-27 16:23:06

Replying to [comment:6 kcrisman]:
> I'm a little concerned about why .pyx files worked before anyway.
They worked only because they were treated as plain Python files.  No Cython was involved.  Treating them like `.spyx` files is the logical thing to do.

> Also, any reason for making the messages print to stderr when they aren't errors?
These kind of diagnostic messages are often printed to `stderr` in Unix-land.  For example, `gcc -v` will output what it's doing to `stderr`.  This makes it much easier to use the output of the script non-interactively: if I want to run a `.spyx` file in a shell script, I have to manually remove the "Compiling..." line if its output to `stdout`.

I'm happy with simply removing the "Compiling..." line also.

> As well as for changing things to the 'new' print statements?
I really dislike the

```
print >>file
```

syntax in Python 2.  Besides, it doesn't hurt to be more compatible with Python 3.

> Finally, if you're going to add pyx files to those which this command does, you should probably add a testing part to the doctest patch for that as well...
I'm not sure, because running `.pyx` files from the command line is not documented.  The documentation suggests using `.spyx` files, not `.pyx` files.


---

Comment by kcrisman created at 2012-09-27 16:29:25

Okay, that's all good enough for me.  I'll test it sometime later but it all makes sense and looks nice.


---

Comment by kcrisman created at 2012-09-28 17:56:46

I confirmed that nontrivial .pyx files did fail before - nice catch.

Somewhat ironically, the second patch doesn't apply to Sage 5.4.beta2.  Does this depend on the patch which does or does not remove gcc optional from Sage?


---

Comment by kcrisman created at 2012-09-28 18:26:22

In fact, I guess this patch *must* be based on this assumption, given that all the spyx doctest in cmdline.py has no optional gcc!  Modulo that issue, this is fine, so putting positive review and sage-pending.

----

On a separate issue, I'm now convinced that gcc doctests shouldn't be optional - reporting further at #12446 where at least one of these showed up.


---

Comment by kcrisman created at 2012-09-28 18:26:22

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2012-09-28 18:59:06

Or, if #13540 comes in, then I guess we could use the other patch.  I'm putting a probably illegal dependency listing now.


---

Comment by jdemeyer created at 2012-09-28 20:33:54

Replying to [comment:10 kcrisman]:
> Somewhat ironically, the second patch doesn't apply to Sage 5.4.beta2.  Does this depend on the patch which does or does not remove gcc optional from Sage?
You're right, I developed it on top of #13533.


---

Comment by jdemeyer created at 2012-10-13 10:21:36

This will need to be rebased to #13579.


---

Attachment


---

Comment by jdemeyer created at 2012-11-06 19:56:58

Rebased to sage-5.4.rc4.  I assume the positive_review still stands.


---

Comment by jdemeyer created at 2012-11-12 21:57:03

Resolution: fixed
