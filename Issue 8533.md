# Issue 8533: browse thematic tutorials from command line and within notebook

Issue created by migration from https://trac.sagemath.org/ticket/8533

Original creator: mvngu

Original creation time: 2010-03-14 00:01:21

Assignee: mvngu

CC:  wdj rlm ncohen rbeezer sage-combinat bump jhpalmieri

Ticket #8470 adds a collection of thematic tutorials to the Sage standard documentation. We should be able to browse such tutorials from the Sage command line or within the Sage notebook.


---

Attachment

based on Sage 4.3.4.alpha1; depends on #8442


---

Comment by mvngu created at 2010-03-14 00:07:19

Changing status from new to needs_review.


---

Comment by mvngu created at 2010-03-14 00:07:19

The attachment should allow you to do these things from the Sage command line and within the Sage notebook:

 1. browse the FAQ
 1. browse the index of thematic tutorials
 1. browse any of the following thematic tutorials at #8465, #8469, #8468, #8442.


---

Comment by mvngu created at 2010-03-14 00:43:07

From IRC:

```
16:33 < mhansen> I don't think things like group_theory_tutorial should be at 
                 the top-level.
16:34 < mvngu> mhansen: Another way is: browse_sage_doc("group_theory_tutorial")
16:34 < mvngu> The original goal was to able to do sage.groups.tutorial()
16:35 < mvngu> But I can't figure out how to put the group theory tutorial 
               within the Sage library, and to also list it within the thematic 
               tutorials page.
16:40 < palmieri> Put this in sage/groups/__init__.py:  from sage.misc.sagedoc 
                  import browse_sage_doc
16:40 < palmieri> tutorial = browse_sage_doc.group_theory_tutorial
16:40 < mvngu> OK. Let try...
16:40 < palmieri> Put those two lines in sage/groups/__init__.py
16:41 < palmieri> Or maybe "from sage.misc.sagedoc import groups_tutorial as 
                  tutorial"
16:41 < mvngu> The last syntax looks better.
```



---

Comment by mvngu created at 2010-03-14 00:43:07

Changing status from needs_review to needs_work.


---

Comment by mvngu created at 2010-03-14 01:17:20

Changing status from needs_work to needs_review.


---

Comment by mvngu created at 2010-03-14 01:17:20

The attachment [trac_8533-browse-doc-take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8533/trac_8533-browse-doc-take2.patch) is another implementation different from the one in [trac_8533-browse-doc.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8533/trac_8533-browse-doc.patch). With [trac_8533-browse-doc-take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8533/trac_8533-browse-doc-take2.patch), you can do these:

 * `sage.groups.tutorial()`
 * `sage.combinat.lie_tutorial()`
 * `sage.crypto.rsa_tutorial()`

That is, the above three tutorials are no longer available from the global name space. The above is closer to the original goal of being able to do "sage.groups.tutorial()" to get the group theory tutorial, etc. However, the FAQ and the index of thematic tutorials are still available in the global name space:

 * `faq()`
 * `thematic_tutorials()`

To see a list of tutorials that you could browse, use "browse_sage_doc.<tab>". Nevertheless, we still have the problem of listing thematic tutorials in the index of thematic tutorials. Could the second patch be seen as a compromise?


---

Comment by mvngu created at 2010-03-19 01:23:43

based on Sage 4.3.4.alpha1; depends on #8442


---

Attachment

The latest version [trac_8533-browse-doc-take2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8533/trac_8533-browse-doc-take2.patch) now allows you to do these:

 * `sage.groups.tutorial()`
 * `sage.combinat.tutorial()`
 * `sage.crypto.tutorial()`

That is, there is only one tutorial for each Sage top level module.


---

Comment by jhpalmieri created at 2010-06-23 17:32:04

In addition to #8442, does this also depend on #8465 and #8469?  Without those, commands like `browse_sage_doc.funcprogramming_tutorial` (available via tab completion) don't work and give a message 

```
OSError: The document 'thematic_tutorials/functional_programming' does not exist.  Please build it
with 'sage -docbuild thematic_tutorials/functional_programming html --jsmath' and try again.
```

which is misleading, since that command won't succeed.

I have no idea if there is any good way to doctest functions like 

```
    def faq(self):
        """
        The Sage FAQ. A collection of frequently asked questions, together
        with answers to those questions.
        """
        self._open("faq")
```

It would be nice to not lower our coverage by including functions like this.  Here's an idea: replace the function by

```
faq = lambda self: self._open('faq')
```

Or is that cheating? This belongs on another ticket, in any case.

Given my understanding of the dependencies, this gets a positive review.


---

Comment by jhpalmieri created at 2010-06-23 17:32:04

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-08-07 05:47:08

Is it possible to move the dependent code here to #8442 and #8469?  Then I could merge this ticket into 4.5.3.x.


---

Comment by mvngu created at 2010-08-07 07:26:36

based on Sage 4.5.2.rc1


---

Comment by mvngu created at 2010-08-07 07:38:28

Changing status from positive_review to needs_work.


---

Attachment

The new patch [attachment:trac_8533-browse-doc-take3.patch] does the same thing as the previous two. But here are the changes in this new patch:

 * Remove dependency on #8442 and #8469.
 * Use John's idea of invoking a document using `lambda`.
 * Allow for browsing the following documents from the command line: FAQ and all the thematic tutorials in the standard documentation so far.
 * Doctesting the `lambda` functions that are used for browsing the FAQ and the thematic tutorials.
 
John's idea of invoking a document using `lambda` is not cheating at all. I implemented that for the FAQ and the extant thematic tutorials, and have provided doctests.



With [attachment:trac_8533-browse-doc-take3.patch] offering a completely new implementation, it renders John's previous positive review ineffective. Sorry, but I have to move this ticket to "needs review" again.


---

Comment by mvngu created at 2010-08-07 07:38:38

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2010-08-11 21:08:09

On my mac: when I run doctests on sagedoc.py, my browser opens up several different windows.  I don't think this is a good idea.     Maybe the lines

```
    sage: faq() 
    sage: thematic_tutorials() 
    sage: funcprogramming_tutorial() 
    sage: sage.groups.tutorial() 
```

should be labeled `# not tested` instead?  Also, do we need to have `funcprogramming_tutorial()` as a top-level command, or is it good enough to have `thematic_tutorials()`?  (This is a genuine question: I don't know which way is better.)


---

Comment by jhpalmieri created at 2010-08-11 21:08:09

Changing status from needs_review to needs_work.


---

Comment by vdelecroix created at 2014-08-29 18:43:53

Replying to [comment:11 jhpalmieri]:
> Also, do we need to have `funcprogramming_tutorial()` as a top-level command, or is it good enough to have `thematic_tutorials()`?  (This is a genuine question: I don't know which way is better.)

Or `thematic_tutorials.funcprogramming_tutorial()` which would be useful in conjunction with `thematic_tutorials.<tab>`. Only one entry point for all thematic tutorials seem more reasonable.

Vincent


---

Comment by klee created at 2022-02-09 01:46:47

I think this ticket didn't get enough momentum, perhaps because we don't want to clutter the global namespace with names of not much use.

Time to close?


---

Comment by klee created at 2022-02-09 01:46:47

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2022-02-09 06:14:35

Yes, I agree.


---

Comment by jhpalmieri created at 2022-02-09 06:14:35

Changing status from needs_review to positive_review.


---

Comment by mkoeppe created at 2022-02-12 18:02:50

Resolution: invalid
