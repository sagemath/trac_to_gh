# Issue 3476: [with patch, needs review] save timeit information with sage -t -timeit

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2008-06-19 21:53:02

Assignee: failure

Keywords: testing doctest timing timeit profile regression

There are several parts to this patch.

The first is an update to `sage.misc.sage_timeit` that generalizes the interface to return an object that prints itself as a timing string rather than the string itself.  The advantage is that the information does not need to be parsed from the string later.  This patch is a requirement of the later ones but is conceptually independent.

The second adds a file `ncadoctest.py` to *scripts* that is a slightly modified version of Python's `doctest.py` file.  It is easier to subclass the various classes with this version.

The third uses `ncadoctest.py` to subclass the doctest architecture and updates `sage-doctest` to use these updated classes.


---

Attachment


---

Attachment

The attachments came in the wrong order -- the one with `sage-scripts` applies to sage/local/bin.


---

Attachment

`diff-python-doctest-to-ncadoctest` records the changes from upstream Python `doctest.py` to `ncadoctest.py` for future reference.


---

Comment by mabshoff created at 2008-07-06 10:56:48

Changing keywords from "testing doctest timing timeit profile regression" to "testing doctest timing timeit profile regression, editor_mabshoff".


---

Comment by gfurnish created at 2008-08-14 03:09:53

Changing keywords from "testing doctest timing timeit profile regression, editor_mabshoff" to "testing doctest timing timeit profile regression, editor_mabshoff, editor_gfurnish".


---

Comment by rlm created at 2008-08-28 23:34:40

This should be applied after #3982.


---

Comment by rlm created at 2008-08-28 23:44:54

Changing keywords from "testing doctest timing timeit profile regression, editor_mabshoff, editor_gfurnish" to "testing doctest timing timeit profile regression, editor_mhansen".


---

Comment by mhansen created at 2008-09-04 03:49:37

Since my one main concern at #3982 is taken care of, I think this can go in.


---

Comment by mabshoff created at 2008-09-04 23:37:40

There is a reject apllying Nick's first patch:

```
--- sage-doctest
+++ sage-doctest
`@``@` -218,8 +241,8 `@``@` def extract_doc(file_name, module):
             doc = doc_preparse(F[i:j+3])
         except SyntaxError:
             doc = F[i:j+3]
-        if len(doc):
-            doc = '""">>> set_random_seed(0L)\n\n' + doc[3:]
+#         if len(doc):
+#             doc = '""">>> print "YYY"; print random() # ; set_random_seed(0L)\n\n' + doc[3:]
         s += "\tr"+ doc + "\n\n"
         F = F[j+3:]
```

I am attempting to merge this manually.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-04 23:43:41

Ok, the reject seems to happen due to merging the warning patch into sage-doctest.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-05 00:06:44

If I merge the patch without the troublesome hunk I see 4 doctests related to the random framework and timeit itself fail:

```
	sage -t -long devel/sage/sage/misc/sage_timeit_class.pyx # 7 doctests failed
	sage -t -long devel/sage/sage/misc/sage_timeit.py # 2 doctests failed
	sage -t -long devel/sage/sage/misc/prandom.py # 2 doctests failed
	sage -t -long devel/sage/sage/misc/randstate.pyx # 6 doctests failed
```


Oh well, life sucks :)

Cheers,

Michael


---

Attachment


---

Comment by mhansen created at 2008-11-08 05:07:39

I've added two updated patches which fix the issue.  The problem was that the 'timeit' in test.globs was set to "False" from the options in sage-doctest instead of being the actual timeit function from Sage.  Thus, you'd only hit the problem with doctests that used timeit.


---

Comment by mabshoff created at 2008-11-08 08:00:52

For "sage -sdist" to work we need to copy ncadoctest.py, sagedoctest.py in sage-make_devel_packages after 

```
  cp -p $SAGE_ROOT/local/bin/SbuildHack.pm $SCRIPTS/
```

I will take care of this once the patch passes doctests.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-08 17:22:53

Hi Mike,

there is one tiny easy to fix doctest issue left:

```
sage -t -long devel/sage/sage/misc/sage_timeit.py           
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.rc0/devel/sage/sage/misc/sage_timeit.py", line 48:
    sage: sage_timeit("a = 2\nb=131\nfactor(a^b-1)", globals(), number=10)
Expected:
    '10 loops, best of 3: ... per loop'
Got:
    10 loops, best of 3: 18.4 ms per loop
**********************************************************************
```

I will fix this via a followup patch.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-08 20:11:23

Resolution: fixed


---

Comment by mabshoff created at 2008-11-08 20:11:23

Merged in Sage 3.2.rc0
