# Issue 7318: SageNB: Sphinxify erases doc/en/introspect

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2009-10-27 03:17:20

Assignee: boothby

CC:  timdumol was

In Sage, `sagenb.misc.sphinxify.sphinxify` does

```python
    shutil.rmtree(confdir, ignore_errors=True)
```

after running Sphinx, but this should happen only if `confdir` is a temporary directory.  Otherwise,

```sh
prompt$> cd $SAGE_ROOT/devel/sage/
prompt$> hg stat
! doc/en/introspect/__init__.py
! doc/en/introspect/conf.py
! doc/en/introspect/static/empty
! doc/en/introspect/templates/layout.html
```




---

Attachment

Preserve doc/en/introspect in sphinxify.  Apply to sagenb repository.


---

Comment by mpatel created at 2009-10-27 03:22:32

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2009-10-27 03:34:35

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2009-10-27 03:34:35

I can confirm that before patching, doc/en/introspect is deleted, and afterwards it isn't.  The patch obviously does the right thing.


---

Comment by was created at 2009-11-11 19:57:07

merged into sagenb-0.4.2 (sage-4.2.1)


---

Comment by was created at 2009-11-11 19:57:07

Resolution: fixed
