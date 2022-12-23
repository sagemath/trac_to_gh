# Issue 8134: Escape $s in notebook keybindings docstring, config.py

Issue created by migration from https://trac.sagemath.org/ticket/8134

Original creator: mpatel

Original creation time: 2010-01-31 02:28:33

Assignee: mvngu

Sphinx complains

```
[...]/sagenb/notebook/config.py:docstring of sagenb.notebook.config:26: (WARNING/2) Inline interpreted text or phrase reference start-string without end-string.
```

when building the reference manual.



---

Comment by mpatel created at 2010-01-31 02:36:13

Escape `$`s in `config.py`.  _sagenb_ repo.


---

Comment by mpatel created at 2010-01-31 02:36:47

Changing status from new to needs_review.


---

Attachment

I'm not sure why `sagenb.notebook.config?` doesn't render nicely in the notebook.


---

Comment by mpatel created at 2010-01-31 02:44:27

The patch should apply cleanly to #8051's SageNB 0.7.2.


---

Comment by mpatel created at 2010-02-05 07:10:19

Changing component from documentation to notebook.


---

Comment by jhpalmieri created at 2010-02-05 20:38:54

It fixes the error messages and the output looks good.  Should there be an 'r' before the triple quotes at the top of the file?  I'll give it a positive review either way, so if you want to add that, go ahead.


---

Comment by jhpalmieri created at 2010-02-05 20:38:54

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-06 16:24:54

Make top docstring raw.  Replaces previous.


---

Attachment

Replying to [comment:4 jhpalmieri]:
> It fixes the error messages and the output looks good.  Should there be an 'r' before the triple quotes at the top of the file?  I'll give it a positive review either way, so if you want to add that, go ahead.
Done!


---

Comment by mpatel created at 2010-02-10 18:31:56

Resolution: fixed
