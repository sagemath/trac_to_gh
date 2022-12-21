# Issue 7776: Implements sage.misc.misc.inject_variable(name, value)

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2009-12-27 22:27:38

Assignee: was

CC:  sage-combinat

From the doc:

    inject a variable into the main global namespace

    INPUT:
     - name  - a string
     - value - anything

    EXAMPLES::

        sage: from sage.misc.misc import inject_variable
        sage: inject_variable("a", 314)
        sage: a
        314

This will be used in the upcoming "inject_shorthands" patch for symmetric functions, and could be used in the various inject_variable code instead of manipulating directly globals() (which could be incorrect if not called directly from the interpreter/notebook.


---

Comment by nthiery created at 2009-12-27 22:34:49

Changing status from new to needs_review.


---

Comment by nthiery created at 2009-12-27 22:35:34

(note: patch prepared and tested on 4.2 not 4.3)


---

Comment by robertwb created at 2009-12-30 09:13:11

I'd rather it looked for `__name__ == '__main__'` than `wiki_create_instance`.


---

Attachment


---

Comment by nthiery created at 2010-01-03 16:17:14

Replying to [comment:3 robertwb]:
> I'd rather it looked for `__name__ == '__main__'` than `wiki_create_instance`.

Ah, excellent, that sure is the right way for doing this. I had missed this __name__ thing. 

Thanks for the suggestion! Patch updated.


---

Comment by mhansen created at 2010-01-13 23:51:38

This looks good to me.


---

Comment by mhansen created at 2010-01-13 23:51:38

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-01-13 23:54:58

If I do

```
sage: inject_variable(3, 34)  # pass a non-string to inject_variable, which I probably shouldn't do
```

then tab-completion is broken.  This is odd, and a little alarming.  Since this function isn't meant for casual users, maybe this isn't a big deal, but otherwise, perhaps we should check that the first argument is a string.

Here's another question:

```
sage: from sage.misc.misc import inject_variable
sage: inject_variable('a', 23)
sage: inject_variable('a', 26)
/Applications/sage/local/bin/sage-ipython:1: RuntimeWarning: redefining global value `a`
  #!/usr/bin/env python
sage: inject_variable('a', 29)
sage: inject_variable('a', 33)
```

Why is the warning only printed the first time?  Is that just the nature of these warnings?


---

Comment by rlm created at 2010-01-14 01:34:18

Resolution: fixed


---

Comment by nthiery created at 2010-01-14 08:57:15

Replying to [comment:6 jhpalmieri]:
> If I do
> {{{
> sage: inject_variable(3, 34)  # pass a non-string to inject_variable, which I probably shouldn't do
> }}}
> then tab-completion is broken.  This is odd, and a little alarming.  Since this function isn't meant for casual users, maybe this isn't a big deal, but otherwise, perhaps we should check that the first argument is a string.

Thanks for catching this. Please review the trivial #7928 follow up!

> Here's another question:
> {{{
> sage: from sage.misc.misc import inject_variable
> sage: inject_variable('a', 23)
> sage: inject_variable('a', 26)
> /Applications/sage/local/bin/sage-ipython:1: RuntimeWarning: redefining global value `a`
>   #!/usr/bin/env python
> sage: inject_variable('a', 29)
> sage: inject_variable('a', 33)
> }}}
> Why is the warning only printed the first time?  Is that just the nature of these warnings?

Ah, I had not noticed this. It seems to be a feature of warn. I added a comment in #7928.
