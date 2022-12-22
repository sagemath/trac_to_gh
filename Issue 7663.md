# Issue 7663: notebook -- synchronization code surprises printing of certain characters

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-12-11 15:13:24

Assignee: was


``` 
This is weird. Occassionaly, in the SAGE notebook, version 4.2.1, the
last characters of output after evaluating a cell are supressed. I've
tried all of string.printable: the only characters supressed are "S",
"A", "G", "E" and "_". No kidding.
 Just try:

print "ASAVFDBAAGGG___EEESS"
///
ASAVFDB


print "ASAVFDBAAGGG___EEESS."
///
ASAVFDBAAGGG___EEESS.

 Is this a private joke or an amazing coincidence?

 Regards
Pablo
```



---

Comment by mpatel created at 2009-12-11 15:58:37

For what it's worth, I don't see this problem with the latest at #6855.  I _may_ have inadvertently fixed it.


---

Comment by mpatel created at 2009-12-14 17:45:03

Possibly related: #7410.  #7666 _may_ fix both.


---

Comment by mpatel created at 2010-01-15 22:41:01

Actually, see #7924.  In particular,

```python
sage: from sagenb.interfaces.expect import WorksheetProcess_ExpectImplementation
sage: wp = WorksheetProcess_ExpectImplementation() 
sage: wp.execute('print "ASAVFDBAAGGG___EEESS"')
sage: wp.output_status()
Output Status:
        output: 'ASAVFDB'
        filenames: []
        done: True
sage: wp.execute('print "ASAVFDBAAGGG___EEESS."')
sage: wp.output_status()
Output Status:
        output: 'ASAVFDBAAGGG___EEESS.'
        filenames: []
        done: True
```



---

Comment by mpatel created at 2010-01-15 23:07:02

Don't use rstrip on internal prompt.  sagenb repo.


---

Attachment


---

Comment by mpatel created at 2010-01-15 23:07:30

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-01-15 23:09:42

The patch here clashes with that at #7648, but it should be easy to reconcile them.


---

Comment by timdumol created at 2010-01-17 18:31:24

Rebased on #7648.


---

Comment by timdumol created at 2010-01-17 18:31:44

Changing status from needs_review to positive_review.


---

Attachment

LGTM.


---

Attachment

Remove extra line to fix #7648.  Replaces previous.


---

Comment by mpatel created at 2010-01-18 08:44:07

V3 drops `s = s.strip()`, to maintain #7648.


---

Comment by timdumol created at 2010-01-19 03:28:21

Resolution: fixed
