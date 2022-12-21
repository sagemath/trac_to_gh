# Issue 7063: SageNB -- Get SageNB to work seamlessly with old notebook saves

Issue created by migration from Trac.

Original creator: timdumol

Original creation time: 2009-09-29 04:37:12

Assignee: tbd

CC:  was

Keywords: sagenb notebook

[ ] make sure that the old notebook directory "just works" with the new notebook:
problem -- old notebooks unpickle into the old notebook code!


---

Comment by timdumol created at 2009-09-29 04:39:30

Migrates old notebook saves to the new notebook


---

Attachment

Apply this patch only.


---

Attachment

Excludes everything under `backups` and `worksheets`. Apply this patch only./


---

Comment by timdumol created at 2009-09-29 05:51:12

Only backs up `nb.sobj` and `conf.sobj`s, since they're the only things affected anyways.


---

Comment by was created at 2009-09-29 06:28:34

Resolution: fixed


---

Attachment


---

Comment by jason created at 2009-10-23 21:47:29

Changing component from algebra to notebook.
