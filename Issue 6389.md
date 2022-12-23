# Issue 6389: expose building documentation for user modules not in the Sage library

Issue created by migration from https://trac.sagemath.org/ticket/6389

Original creator: malb

Original creation time: 2009-06-23 14:34:27

Assignee: tba

CC:  mkoeppe jdemeyer vbraun chapoton was dimpase nthiery fhivert embray

Keywords: documentation, sphinx

It would be neat to be able to do:

`sage -docbuild foo.py`

for a single file not in the library


---

Comment by chapoton created at 2016-07-15 11:14:01

This used to work, but no longer

```
sage -docbuild file=my_own_code.py html
```



---

Comment by jhpalmieri created at 2016-08-01 02:16:59

The line

```
    assert app.outdir.startswith(SAGE_DOC)
```

in `src/sage_setup/docbuild/ext/multidocs.py` raises an error. I think we should disable this assertion when using the `file=...` argument to `sage --docbuild`.


---

Comment by mkoeppe created at 2016-08-03 19:35:00

Replying to [comment:3 jhpalmieri]:
> The line
> {{{
>     assert app.outdir.startswith(SAGE_DOC)
> }}}
> in `src/sage_setup/docbuild/ext/multidocs.py` raises an error. I think we should disable this assertion when using the `file=...` argument to `sage --docbuild`.

This assert is in `citation_dir`. 
How should single-file docbuilds handle citations?


---

Comment by jhpalmieri created at 2016-08-03 20:00:55

Replying to [comment:5 mkoeppe]:
> Replying to [comment:3 jhpalmieri]:
> > The line
> > {{{
> >     assert app.outdir.startswith(SAGE_DOC)
> > }}}
> > in `src/sage_setup/docbuild/ext/multidocs.py` raises an error. I think we should disable this assertion when using the `file=...` argument to `sage --docbuild`.
> 
> This assert is in `citation_dir`. 
> How should single-file docbuilds handle citations?

Ignore them? Or at least ignore references to citations in the Sage library: I think it should treat the single file as being unconnected to the Sage library.


---

Comment by mkoeppe created at 2016-08-03 20:26:59

Cc'ing people who are currently working on the documentation infrastructure (#20080, #20893, #20577).


---

Comment by embray created at 2016-11-10 11:54:54

See also #21841 -- per that ticket, I think that if Sage's docbuild facilities are made available to third-party code (as I think it should be) then either it should be moved into the sage library itself (i.e. `sage.docbuild`) or its own package (`sage_docbuild`)--`sage_setup` is not otherwise a good place for it.


---

Comment by embray created at 2016-11-10 11:56:38

I don't fully understand how citations are handled, but would it not be desirable for third-party docs to either have their own citation list, or to be able to point to citations in Sage's docs (if available)?
