# Issue 5761: Bring doctests of sage/misc/latex.py to 100%

Issue created by migration from Trac.

Original creator: rbeezer

Original creation time: 2009-04-11 19:56:35

Assignee: mabshoff




---

Comment by rbeezer created at 2009-04-12 01:00:59

I'm partway through this, but still need to do much more, and will be away from it for a few days.


---

Comment by rbeezer created at 2009-04-12 01:00:59

Changing assignee from mabshoff to rbeezer.


---

Comment by mabshoff created at 2009-04-13 03:40:25

Bouncing to 3.4.2.

Cheers,

Michael


---

Comment by tscrim created at 2013-02-01 16:15:46

I've gone through an brought the documentation for `latex.py` to full coverage and up to current standards. I've also removed the ~2 year old deprecated method `pdflatex()`.


---

Comment by tscrim created at 2013-02-01 16:15:46

Changing status from new to needs_review.


---

Comment by tscrim created at 2013-02-01 16:15:46

Changing keywords from "" to "documentation, coverage, latex".


---

Comment by aapitzsch created at 2013-02-02 16:08:52

Changing status from needs_review to needs_work.


---

Comment by aapitzsch created at 2013-02-02 16:08:52

There are some `True, False` and `None` not surrounded by ````.

After

```
"\\ZZ[x]
```

in

```
EXAMPLES::

    # sage: latex.eval("\\ZZ[x], locals(), filename="test") # This would generate a file named "test.png"
    # ''
    # sage: latex.eval("\\ZZ[x], locals(), filename="/path/to/test") # This would generate a file named "/path/to/test.png"
    # ''
```

a " is missing, otherwise the command will fail. You can use _# not tested_ at the end of the line instead of commenting out the examples.

Everything else looks good to me.


---

Comment by tscrim created at 2013-02-05 02:21:18

Changing status from needs_work to needs_review.


---

Comment by tscrim created at 2013-02-05 02:21:18

I believe I caught them all; let me know where if I missed any others.

Thanks for the review,

Travis


---

Comment by aapitzsch created at 2013-02-05 22:24:53

Could you add an additional patch to fix the trac reference in `repr_lincomb()`:

```
Verify that a certain corner case works (see trac 5707 and 5766)::
```

and in `latex_varify()`:

```
if "is_fname" flag is True or False.
```



---

Comment by tscrim created at 2013-02-05 23:16:39

Fixed. I've also made the patchbot offending test optional.

-----

For patchbot:

Apply only: trac_5791-latex_docstrings-ts.patch


---

Comment by aapitzsch created at 2013-02-06 18:03:14

You added one trailing whitespace after "An error"

```
sage: latex.eval("\ThisIsAnInvalidCommand", {}) # optional - requires 'convert'
An error
```

But I think it's no problem. So I'm giving this a positive review. Let's hope the release manager does not complain about the wrong number in the filename. ;)


---

Comment by aapitzsch created at 2013-02-06 18:03:14

Changing status from needs_review to positive_review.


---

Attachment

Fixed trailing whitespace and matched ticket number


---

Comment by tscrim created at 2013-02-06 18:31:34

Fixed. Thank you.

For patchbot:

Apply only: trac_5761-latex_docstrings-ts.patch


---

Comment by jdemeyer created at 2013-02-09 12:13:02

Resolution: fixed
