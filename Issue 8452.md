# Issue 8452: Code check: Pickling of nested classes

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-03-06 00:43:33

Assignee: tbd

CC:  hivert jhpalmieri nthiery

Florent Hivert has recently devised a nice way to use Sphinx to test that nested classes in Sage are picklable.  Please see [attachment:ticket:7448:trac_7448-nested_class_sphinx-fh.4.patch V4] at #7448.  From #7448's description:

   "I also took the chance to raise a warning if someone forgot to set the metaclass leading to a unpicklable class. Several bug have been found that way. I'll add a ticket for this."

This ticket is about implementing Hivert's idea.


---

Attachment

Add `sage -docbuild` option `--check-nested` to check picklability


---

Comment by mpatel created at 2010-03-06 09:59:57

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-03-06 09:59:57

I've attached a patch that adds an option `--check-nested` to the Sage doc builder.  If the flag is present, Sphinx will check [nested classes for picklability](http://stackoverflow.com/questions/1947904/how-can-i-pickle-a-nested-class-in-python).

I've adapted `sage.misc.nested_class.modify_for_nested_pickle`, so that we can put the check in `conf.py` instead of `sage_autodoc.py`.  We may not need to patch Sphinx.  Please test and let me know if this works.

Note: The patch depends on #7448.


---

Comment by mpatel created at 2010-03-06 09:59:57

Changing priority from major to minor.


---

Comment by hivert created at 2010-03-06 10:56:05

Replying to [comment:1 mpatel]:
> I've adapted `sage.misc.nested_class.modify_for_nested_pickle`, so that we can put the check in `conf.py` instead of `sage_autodoc.py`.  We may not need to patch Sphinx.  Please test and let me know if this works.
> 
> Note: The patch depends on #7448.

Hi Mitesh,

As far as I understand, the goal of this ticket is twofold:
 - make the check optional;
 - put it in a sage plugin of sphinx to avoig patching Sphinx for that. 
So you still relies on sphinx to do this check. As I previously said, a priori, checking for nested class has nothing to do with Sphinx. 

Though I definitely don't know where to do it, if possible, it would even be better to do it in sage eg. during the import of the class... Any idea on this way ? Maybe it's not possible without patching `type` which is exactly what `NestedClassMetaclass` does, at least conceptually.  

By the way, am I allowed to review this patch (there is some code from me in it) ?


---

Comment by mpatel created at 2010-03-06 14:27:34

The patch really just takes advantage of Sphinx's iteration over the contents of the [documented] modules.  Sphinx has a [doctest extension](http://sphinx.pocoo.org/ext/doctest.html), which blurs the "line" between building the documentation and checking the code.  If the patch actually works, we could take it as an immediately available but temporary solution while we consider other possibilities.   But I don't mind at all if we adopt a different approach. 

We could create a new script `SAGE_LOCAL/bin/sage-analyze` with options to run various checks on library source code.  Users would call the script directly or via `sage -analyze --option file ...`.

Instead of starting completely from scratch, we could adapt or extend an existing tool: [PyChecker](http://pychecker.sourceforge.net/), [PyFlakes](http://divmod.org/trac/wiki/DivmodPyflakes), [Pylint](http://www.logilab.org/project/pylint).  From my very limited experience, I think Pylint is the most promising of these, as long as we adjust the settings.

I think we could each review the other's contributions and maybe get an assist from a third reviewer.

I just noticed that I didn't put your name in the Author(s) field.  I apologize for that.


---

Comment by hivert created at 2010-03-06 22:30:02

Replying to [comment:3 mpatel]:
> The patch really just takes advantage of Sphinx's iteration over the contents of the [documented] modules.  Sphinx has a [doctest extension](http://sphinx.pocoo.org/ext/doctest.html), which blurs the "line" between building the documentation and checking the code.  If the patch actually works, we could take it as an immediately available but temporary solution while we consider other possibilities.   But I don't mind at all if we adopt a different approach. 

I'm happy to report that the temporary solution is fully working. Running a docbuild 
I got

```
WARNING: Pickling of nested class 'sage.combinat.words.words.Words_all._python_object_alphabet' is probably broken. Please set __metaclass__ of the parent class to sage.misc.nested_class.NestedClassMetaclass.
```

And indeed:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
Loading Sage library. Current Mercurial branch is: review
sage: sage: W = Words()
sage: sage: A = W._python_object_alphabet()
sage: sage: loads(dumps(A))
---------------------------------------------------------------------------
PicklingError                             Traceback (most recent call last)
...
PicklingError: Can't pickle <class 'sage.combinat.words.words._python_object_alphabet'>: attribute lookup sage.combinat.words.words._python_object_alphabet failed
```

I'll report it to the author and create the ticket tomorrow.
| Sage Version 4.3.4.alpha0, Release Date: 2010-03-03                |
| Type notebook() for the GUI, and license() for information.        |
> We could create a new script `SAGE_LOCAL/bin/sage-analyze` with options to run various checks on library source code.  Users would call the script directly or via `sage -analyze --option file ...`.
> 
> Instead of starting completely from scratch, we could adapt or extend an existing tool: [PyChecker](http://pychecker.sourceforge.net/), [PyFlakes](http://divmod.org/trac/wiki/DivmodPyflakes), [Pylint](http://www.logilab.org/project/pylint).  From my very limited experience, I think Pylint is the most promising of these, as long as we adjust the settings.

I think this is a very good idea. Nicolas advised me to use PyFlakes. It work for what I need but I've no idea how to extend it.

> I think we could each review the other's contributions and maybe get an assist from a third reviewer.
> 
> I just noticed that I didn't put your name in the Author(s) field.  I apologize for that.

No problem. My work is already acknowledged as the author of #7448. Symmetrically, You've done more than a review work on this ticket and didn't add yourself as author... So please do as you consider fair. I don't feel offended either way.


---

Comment by hivert created at 2010-03-08 21:09:38

Replying to [comment:3 mpatel]:
> I think we could each review the other's contributions and maybe get an assist from a third reviewer.

From what's concern me the patch is ready to go. Should we keep the idea of `sage -analyze ...` for another ticket ? 

Florent


---

Comment by mpatel created at 2010-03-09 04:48:30

Sure.  If anyone objects, please let us know.


---

Comment by mpatel created at 2010-03-09 04:48:30

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-03-09 07:46:53

Resolution: fixed
