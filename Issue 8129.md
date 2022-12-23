# Issue 8129: Install jsMath image fonts in a fixed location

Issue created by migration from https://trac.sagemath.org/ticket/8129

Original creator: mpatel

Original creation time: 2010-01-30 04:06:57

Assignee: tbd

CC:  was jason jhpalmieri

Keywords: notebook, jsmath, fonts

Installing the jsMath image fonts in `SAGE_LOCAL/lib/jsmath/fonts`, say, should make it easier to upgrade to new SageNB versions.

Note: Both the notebook and the command-line can use jsMath (e.g., `browse_sage_doc(identity_matrix)`).  We could detect and check the relevant paths and make a symbolic link in `sage.all`.

See [sage-notebook](http://groups.google.com/group/sage-notebook/browse_thread/thread/53157b4e21f4ef86), #7467, #7778.


---

Comment by mpatel created at 2010-01-30 04:14:16

We could detect and check the relevant paths and make a symbolic link in `sage.all`.  We'd have a potential race condition --- two processes could try to make the link at the same time --- but it should be mostly harmless: `OSError: [Errno 17] File exists`.


---

Comment by robert.marik created at 2010-01-30 10:59:13

I have no problem with jsmath image fonts (with latest Sage and #8051).
Could the problem be limited to sagenb.org only?


---

Comment by robert.marik created at 2010-01-30 11:10:01

Replying to [comment:3 robert.marik]:
> I have no problem with jsmath image fonts (with latest Sage and #8051).
> Could the problem be limited to sagenb.org only?

Forgot to write: I tested it on fresh Sage install - this means there are no old directories used by previous versions. Perhaps, the install script from the latest jsmath fonts was confused by previous installs and old jsmath directories on sageng.org? Just guessing, I do not have access there.


---

Comment by mpatel created at 2010-02-05 10:55:43

Look for jsMath fonts in `SAGE_LOCAL/...`.  Depends on #8051.  sagenb repo.


---

Attachment

With the patch, the server does a simple check for jsMath fonts under `SAGE_LOCAL`:

```python
jsmath_fonts_path = os.path.join(os.environ['SAGE_LOCAL'],
                                 'lib', 'jsmath', 'fonts')
if not os.path.exists(jsmath_fonts_path):
    jsmath_fonts_path = os.path.join(javascript_path, 'jsmath', 'fonts')
```


We'll need to add the msbm10 fonts to the fonts spkg.  Instead of putting even more version-checking logic in `jsmath-image-fonts-*.spkg` `spkg-install`, should we give the new spkg a different name, e.g., `jsmath-image-fonts-new-*.spkg`?  Its `spkg-install` would just install the fonts in `SAGE_LOCAL/lib/jsmath/fonts`.

Also, should we try adding *all* of the [extra jsMath fonts](http://www.math.union.edu/~dpvc/jsmath/download/extra-fonts/welcome.html) to the new spkg?

```
bbold10
cmbsy10
cmbx10
cmex10
cm-fonts
cmmi10
cmmib10
cmr10
cmss10
cmsy10
cmti10
eufb10
eufm10
eurb10
eurm10
eusb10
eusm10
lasy10
lasyb10
msam10
msbm10
rsfs10
stmary10
wasy10
wasyb10
```

?


---

Comment by knsam created at 2013-02-03 18:20:09

Changing status from new to needs_review.


---

Comment by knsam created at 2013-02-03 18:22:24

We now use MathJax instead of jsMath, so I think this ticket per se is invalid. But, I am not sure how we use MathJaX and whether this ticket is relevant for our implementation. Can someone look through this and also help me sort this ignorance out?


---

Comment by jdemeyer created at 2013-05-17 12:42:34

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-05-21 07:24:43

Resolution: invalid
