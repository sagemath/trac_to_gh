# Issue 7418: %maxima cells are partially broken

Issue created by migration from Trac.

Original creator: whuss

Original creation time: 2009-11-09 16:47:10

Assignee: boothby

CC:  was timdumol

In the new sage notebook maxima cells do not work anymore for inputs
starting with '%'.


```
%maxima
%pi

Traceback (click to the left for traceback)
...
AttributeError: 'sage.symbolic.expression.Expression' object has no
attribute 'eval'
```


or:


```
%maxima
%e^(%i * %pi)

Syntax Error:
    %e^(%i * %pi)
```


This used to work with older Sage versions.


---

Comment by mhansen created at 2009-11-09 18:41:41

I think the best fix for this is to break from processing the percent directives once a system directive has been reached.  It should be easy to detect this as the system directives are the "unknown" one has been reached.


---

Comment by mhansen created at 2010-01-17 04:21:59

Changing status from new to needs_review.


---

Comment by timdumol created at 2010-01-17 06:50:53

Changing status from needs_review to needs_work.


---

Comment by timdumol created at 2010-01-17 06:50:53

Applying the patch on the latest version off the repository (sagenb-0.5.0 + #7843 + #7844 + #7846 + #7871) causes the system directives to display (%html, %maxima, etc. are visible on output).


---

Comment by mhansen created at 2010-01-17 22:11:01

Sorry about that.  I put up a new patch which should fix it.  I opted for duplicating the directives.append line instead of having some sort of check to see if the system was set as it makes the flow a little cleaner.


---

Comment by mhansen created at 2010-01-17 22:11:01

Changing status from needs_work to needs_review.


---

Comment by timdumol created at 2010-01-19 08:44:59

Same problem still here (sagenb-0.6)


---

Comment by timdumol created at 2010-01-19 08:44:59

Changing status from needs_review to needs_work.


---

Comment by mpatel created at 2010-01-25 08:04:31

Add one.  Rebased for queue in comment.  Replaces previous.


---

Comment by mpatel created at 2010-01-25 08:07:53

Changing status from needs_work to needs_review.


---

Attachment

V2 adds one --- I hope it's in the right place.  The queue:

```
SageNB 0.7 / #8051
trac_7784-hgignore_update.patch
trac_5712-interrupt-notification.5.patch
trac_6069-missing_pub_ws.2.patch
trac_8038-email_plus_addressing_v2.patch
trac_7506-notebook_object-documentation.2.patch
trac_693-spawn_notebook.3.patch
trac_5177-delete-cell-dirs.2.patch
trac_7418-maxima_cells.2.patch
```

The patch version numbers may be off by one or so.

Positive review, but someone should review my change.


---

Comment by timdumol created at 2010-04-21 20:33:28

LGTM. Positive review.


---

Comment by timdumol created at 2010-04-21 20:33:28

Changing status from needs_review to positive_review.


---

Comment by timdumol created at 2010-07-11 06:03:52

Resolution: fixed
