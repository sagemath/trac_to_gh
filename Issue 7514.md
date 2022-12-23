# Issue 7514: rewrite load and attach

Issue created by migration from https://trac.sagemath.org/ticket/7514

Original creator: was

Original creation time: 2009-11-22 08:12:38

Assignee: tbd

CC:  slabbe robertwb ddrake




---

Attachment

apply to the core sage library


---

Attachment


---

Comment by was created at 2009-11-22 08:16:59

Changing status from new to needs_review.


---

Comment by slabbe created at 2009-11-23 10:30:16

Reading the summary of this ticket made me remember a problem I was having with the attach command : Can we attach a file already in the sage tree that we are editing? I already tried, but I stopped using it because sometimes the changes in the file were not considered and I have been stopping sage and running sage -br ever since then.

Maybe I was doing something bad or maybe this ticket solves the problem or maybe it is not possible at all to do this...??

Sébastien


---

Comment by was created at 2009-11-23 15:11:14

> Can we attach a file already in the sage tree that we are editing?

> I stopped using it because sometimes the changes in the file were not
>  considered and I have been stopping sage and running sage -br ever since then. 

You probably don't understand what attach does.  All it does is execfile the file that you attached.  There are situations where this happening might be perceived as "the file were not considered".  E.g., if you create an install F of a class Foo defined in a file a.py, then a.py is reloaded, the object F is *not* somehow magically modified in memory to be an instance of a the new Foo that was defined in the file a.py.    That's not how Python works, and it would be weird and confusing overall if things did work that way.


---

Attachment


---

Comment by was created at 2009-12-08 21:16:43

Changing status from needs_review to needs_work.


---

Comment by was created at 2009-12-08 21:16:43

Replying to [comment:2 slabbe]:
> Reading the summary of this ticket made me remember a problem I was having with the attach command : Can we attach a file already in the sage tree that we are editing? I already tried, but I stopped using it because sometimes the changes in the file were not considered and I have been stopping sage and running sage -br ever since then.
> 
> Maybe I was doing something bad or maybe this ticket solves the problem or maybe it is not possible at all to do this...??
> 

You just have to *understand* what attach does.  It reloads the file via execfile into the global namespace when the file changes.  You can attach any file, in the tree or not.  But imagine this:   In the sage tree there is a file foo.py.  There is another file bar.py that does "import foo" and uses some code in foo.  If you attach foo.py (which results in exec'ing it in the global interpreter namespaces), then that will have no impact at all on bar.py.  

Thus for some problems attach works very nicely for library code, and for others it doesn't.  Which is which is clearer if you know what attach does.


---

Attachment

Combined _sage_ repo patch.  Depends on 4.3.alpha1, SageNB 0.4.6 (#7625), #7483, #7482.


---

Comment by mpatel created at 2009-12-10 01:48:20

I've attached a combined "sagelib" patch.  It depends on 4.3.alpha1, SageNB 0.4.6 (#7625), #7483, and #7482.

Out of curiosity:  What if we "overload" `import` by keeping a stack of all imported modules.  When a watched file changes, we reload it and all modules loaded since the watched file was first loaded?  Would this be useful in some situations?


---

Comment by mpatel created at 2009-12-10 02:00:01

With 4.3.alpha1 + #7625 + #7483 + #7482 + this ticket, several doctests failed:

```
        sage -t  devel/sage/sage/misc/sageinspect.py # 3 doctests failed
        sage -t  devel/sage/sage/misc/preparser.py # 10 doctests failed
        sage -t  devel/sage/sage/misc/reset.pyx # 2 doctests failed
        sage -t  devel/sage/sage/misc/session.pyx # 1 doctests failed
```

Should we stop doctesting most (all?) of `sage/server`?


---

Comment by mpatel created at 2009-12-10 12:37:21

Replying to [comment:8 mpatel]:
> With 4.3.alpha1 + #7625 + #7483 + #7482 + this ticket, several doctests failed:

Three tests fail in `sagenb.misc.sageinpect`.  Please see #7650.

> Should we stop doctesting most (all?) of `sage/server`?

Please see #7534.


---

Comment by mpatel created at 2009-12-28 13:56:11

I noticed

```python
sage: f = 1
sage: save(f, 'f')
sage: attach('f.sobj')
Traceback (most recent call last)
...
ValueError: argument (='f.sobj') to load or attach must have extension py, sage, or pyx                             
sage: attached_files()
['f.sobj']
```


Questions about loading/attaching Cython files:

 * Can they only be loaded once, if they haven't changed?  For example: If `zzz.pyx` contains `print 'Zzz!'`, I see

```python
sage: load('zzz.pyx')
Compiling zzz.pyx...
Zzz!
sage: load('zzz.pyx')
sage: load('zzz.pyx')
sage: # Now I edit zzz.pyx
sage: load('zzz.pyx')
Compiling zzz.pyx...
Awake!
```


 * Can they access existing objects?  For example: If I put

```python
try:
    b += 1
except:
    b = 10
print b
```


    in a .pyx file, loading the file always sets `b` to 10, even if it's already defined.

Disclaimer:  I'm still quite ignorant about Cython.


---

Attachment

Fixed doctest failures.  Replaces previous.


---

Comment by mpatel created at 2009-12-28 17:12:32

Fixed doctest failures.  Depends on Sage 4.3, #7483, #7482.  Replaces previous.


---

Attachment

The latest patches should fix the doctests and the `attached_files` problem mentioned above.  I changed `attach t` to `attach(t)`, since the doctesting framework appears to use a Python interpreter, i.e., _not_ IPython, to run the examples.  I also weakened [somewhat] the tests for `preparser.modified_attached_files`.  Is there an IPython doctesting mode?

I'm not sure about the Cython file reload problem.  Should we set `use_cache=True` when loading .pyx files explicitly?

On globals:  I see that a Cython file `foo.pyx` is compiled to a module and loaded via `from foo import *`.

Can someone else please help to review this ticket?


---

Comment by mpatel created at 2009-12-28 18:22:45

Changing status from needs_work to needs_review.


---

Comment by mpatel created at 2009-12-28 21:38:46

Fix(?) loading of .spyx files.  Add preparser.py to reference manual.  Replaces previous.


---

Attachment


---

Attachment

rebased against sagenb-0.4.8 + trac #7483.


---

Comment by was created at 2009-12-31 19:34:17

trac 7514 sagenb-part2: proper tracebacks; make source code introspection of functions defined in \ the notebook finally work in the notebook; properly cleanup worksheet files when notebook server is killed.


---

Attachment

Right now the files that one must apply are:


```
To Sage Library:
 sagelib-7514_combined.3.patch 

To Notebook:
 sagenb-7514-rebase.patch  
 sagenb-7514-rebase-part2.patch
```



---

Comment by was created at 2009-12-31 19:36:47

The file sagenb-7514-rebase-part2.patch fixes some serious issues.  In particular, it makes it so we get proper tracebacks on errors, which was broken without this patch by the new architecture (of doing everything in the worksheet process, etc.).  Also, source code introspection now works again for functions defined in the notebook, which many users wanted.  Finally, there was a little bug where pressing control-c to stop the notebook server didn't result in quitting all worksheet processes, hence they left junk around.


---

Comment by mpatel created at 2010-01-01 03:51:22

* When I load/attach a .(s)pyx file in the notebook, `___code__.py` appears in the cell's output HTML.

 * Minor: Should we make `attached_files()` in the notebook report, e.g.,

```
[DATA+'foo.py']
```

   instead of

```
['/full/path/to/foo.py']
```


 * Typing `f??<TAB>` for a function `f` defined in the notebook shows its docstring but not its source code.  Is this related to ?? not working for Cython functions defined in cells or attached `DATA` files?

 * Should we make it possible to edit attached .pyx files, just as we can edit .py, .sage, .spyx, and .txt files?

 * Minor: `save_notebook` appears to be called twice on shutdown.  Is this a fail-safe behavior?


---

Comment by was created at 2010-01-01 04:53:06

> When I load/attach a .(s)pyx file in the notebook, ___code__.py appears in 
> the cell's output HTML. 

That's a bug.  I'll fix it soon. 

> Minor: Should we make attached_files() in the notebook report

I'm not sure.  But I think this should be a separate ticket, since it would be a new feature. 

>     * Typing f??<TAB> for a function f defined in the notebook shows its docstring but > not its source code. 

That's really weird, because it is one of the problems that this patch definitely fixes.  Are you sure?   Did you define a function f in one input cell, then do f?? in another, and it didn't show the source code?    Were you using a clean sagenb-0.4.8 install for testing?  Maybe I messed up posting the patch. 

> Minor: save_notebook appears to be called twice on shutdown. Is this a fail-safe behavior?

This has been the case forever.  It is not caused by this patch.  I don't think it is desirable.  Please do open a ticket. 

OK, so I'm going to fix the ___code___.py issue you reported above, triple check that f?? works, and if not, figure out what went wrong, then mark this as "needs review" again.


---

Comment by was created at 2010-01-01 04:53:06

Changing status from needs_review to needs_work.


---

Comment by mpatel created at 2010-01-01 05:18:03

Replying to [comment:16 was]:
> >     * Typing f??<TAB> for a function f defined in the notebook shows its docstring but > not its source code. 
> 
> That's really weird, because it is one of the problems that this patch definitely fixes.  Are you sure?   Did you define a function f in one input cell, then do f?? in another, and it didn't show the source code?    Were you using a clean sagenb-0.4.8 install for testing?  Maybe I messed up posting the patch. 

It seems that just the last line of code is omitted.  The source displayed is the preparsed source, but I don't know if this is a problem.


---

Comment by was created at 2010-01-01 05:35:49

Changing status from needs_work to needs_review.


---

Comment by was created at 2010-01-01 05:35:49

The attached patch (sagenb-7514-rebase-part3.patch) should:

1. Fixed this: "When I load/attach a .(s)pyx file in the notebook, _code.py appears in the cell's output HTML."

2. Fixed this: "Typing f??<TAB> for a function f defined in the notebook shows its docstring but not its source code."  Actually, this wasn't exactly broken... the last line of the docstring was missing.  I've added a newline to the end of the input file, and now the problem is gone.  This isn't a hack, since I think files are *supposed* to end with a newline, according to "IEEE Standard 1003.1 (aka POSIX)".   Note that this patch *only* adds support for f?? for functions specifically entered in input normal cells (not cython, not load/attached).  That's another issue.


---

Attachment


---

Attachment

Trivial docstring tweaks.  Replaces previous.


---

Comment by mpatel created at 2010-01-01 06:17:59

Positive review.

If it's OK, I'll fix (e.g., INPUT/OUTPUT blocks) a few docstrings of functions affected by the sagelib patch.


---

Comment by mpatel created at 2010-01-01 06:46:08

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-01-01 06:46:08

Replying to [comment:19 mpatel]:
> Positive review.
> 
> If it's OK, I'll fix (e.g., INPUT/OUTPUT blocks) a few docstrings of functions affected by the sagelib patch.

I'll make a separate ticket instead.  We should include `load` and `attach` in the reference manual.


---

Comment by timdumol created at 2010-01-03 19:18:02

The preparsing function introduced in #7483 lacks a "# -*- coding: utf-8 -*-" header that prevents the notebook from evaluating any string that contains unicode. This is addressed in #7835.


---

Comment by mhansen created at 2010-01-03 22:32:59

I've merged sagelib-7514_combined.patch in sage-4.3.1.alpha0.


---

Comment by was created at 2010-01-04 06:41:38

I merged the sagenb patches into sagenb-0.4.8.


---

Comment by was created at 2010-01-04 06:41:38

Resolution: fixed


---

Comment by mvngu created at 2010-01-28 16:33:43

The attachment [sagelib-7514_combined.3.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7514/sagelib-7514_combined.3.patch) in the Sage library.
