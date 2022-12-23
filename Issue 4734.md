# Issue 4734: sage -notebook option now broken

Issue created by migration from https://trac.sagemath.org/ticket/4734

Original creator: was

Original creation time: 2008-12-07 04:49:58

Assignee: boothby


```

Dear Sage-Devels,

Let me again thank you for the excellent work put in building sage.

I've found a bug in the most recent release. Specifically, when
invoked with the -notebook switch, the current release does not
properly quote paths. So, if I execute:

/Applications/sage/sage -notebook "/Users/carson/doc/math/
sage_notebook/"

Sage says:

Traceback (most recent call last):
 File "/Applications/sage/local/bin/sage-notebook", line 14, in
<module>
   exec "notebook(" + ",".join(sys.argv[1:]) + ")"
 File "<string>", line 1
   notebook(/Users/carson/doc/math/sage_notebook/)
            ^
SyntaxError: invalid syntax

If I edit the offending line in local/bin/sage-notebook:

   exec "notebook(" + ",".join(sys.argv[1:]) + ")"

To instead read:

   exec "notebook('" + ",".join(sys.argv[1:]) + "')"

Then the -notebook switch works as expected. Please consider using the
following sage-notebook file to correct this bug:

http://bentham.k2.t.u-tokyo.ac.jp/media/bugs/sage/sage-notebook

Cheers,
```


Makes sense.  This was indeed caused by a patch in the last version of sage.


---

Comment by klee created at 2008-12-07 10:28:45

The -notebook command line option takes the same arguments as the
notebook() sage command. The directory argument to both the command
line option and the sage command should be a python string. So the
proper way to write your code is

/Applications/sage/sage -notebook '"/Users/carson/doc/math/
sage_notebook/"'

Here the outer single quotes ' ' quote the python string "/Users/
carson/doc/math/sage_notebook/". This is a function of your shell.

The most recent release of Sage also accepts for example

/Applications/sage/sage -notebook '"/Users/carson/doc/math/
sage_notebook/"' secure=True open_viewer=False

This did not work for the old release of Sage.


---

Comment by was created at 2008-12-07 19:11:53

Since the first input two notebook has to be a string, if there are no named parameters we should rewrite the code to make the original user's input work.  I.e., This should work no matter what, and I see no reason not to make this work:

```
sage -notebook "/Users/carson/doc/math/sage_notebook/"
```



---

Comment by klee created at 2008-12-08 04:25:45

Then the patch for ticket #4641 applied to Sage 3.2.1 should be abolished, and the original code

notebook(*sys.argv[1:])

should be recovered, until a better solution be found. The original code seems better than the code proposed by the reporter of this bug.


---

Attachment


---

Comment by was created at 2009-01-24 15:51:08

apply the patch to the *SCRIPTS* repo!


---

Comment by mabshoff created at 2009-02-02 04:57:59

Nice, positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-02 04:58:16

Resolution: fixed


---

Comment by mabshoff created at 2009-02-02 04:58:16

Merged in Sage 3.3.alpha4.

Cheers,

Michael
