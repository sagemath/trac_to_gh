# Issue 466: -b is actually not an option for hg_sage.merge()

Issue created by migration from Trac.

Original creator: pdehaye

Original creation time: 2007-08-20 09:20:13

Assignee: was

sage: hg_sage.merge?                        
Type:           instancemethod
Base Class:     <type 'instancemethod'>
String Form:    <bound method HG.merge of Hg repository 'SAGE Library Source Code' in directory /Library/sage/devel/sage>
Namespace:      Interactive
File:           /Library/sage/local/lib/python2.5/site-packages/sage/misc/hg.py
Definition:     hg_sage.merge(self, options='')
Docstring:
    
            Merge working directory with another revision
            
            Merge the contents of the current working directory and the
            requested revision. Files that changed between either parent are
            marked as changed for the next commit and a commit must be
            performed before any further updates are allowed.
    
            INPUT:
                options -- default: ''
                    'tip' -- tip
                     -b --branch  merge with head of a specific branch
                     -f --force   force a merge with outstanding changes
            

contradicted by


sage: hg_sage.merge(options="--branch main")
cd "/Library/sage/devel/sage" && hg merge --branch main
hg merge: option --branch not recognized
hg merge [-f] [[-r] REV]

merge working directory with another revision

    Merge the contents of the current working directory and the
    requested revision. Files that changed between either parent are
    marked as changed for the next commit and a commit must be
    performed before any further updates are allowed.

    If no revision is specified, the working directory's parent is a
    head revision, and the repository contains exactly one other head,
    the other head is merged with by default.  Otherwise, an explicit
    revision to merge with must be provided.

options:

 -f --force  force a merge with outstanding changes
 -r --rev    revision to merge

use "hg -v help merge" to show global options





---

Comment by pdehaye created at 2007-08-22 13:43:02

That would be

```
sage: hg_sage.merge?
Type:           instancemethod
Base Class:     <type 'instancemethod'>
String Form:    <bound method HG.merge of Hg repository 'SAGE Library Source Code' in directory /Library/sage/devel/sage>
Namespace:      Interactive
File:           /Library/sage/local/lib/python2.5/site-packages/sage/misc/hg.py
Definition:     hg_sage.merge(self, options='')
Docstring:
    
            Merge working directory with another revision
            
            Merge the contents of the current working directory and the
            requested revision. Files that changed between either parent are
            marked as changed for the next commit and a commit must be
            performed before any further updates are allowed.
    
            INPUT:
                options -- default: ''
                    'tip' -- tip
                     -b --branch  merge with head of a specific branch
                     -f --force   force a merge with outstanding changes
            

sage: hg_sage.merge(options="--branch main")
cd "/Library/sage/devel/sage" && hg merge --branch main
hg merge: option --branch not recognized
hg merge [-f] [[-r] REV]

merge working directory with another revision

    Merge the contents of the current working directory and the
    requested revision. Files that changed between either parent are
    marked as changed for the next commit and a commit must be
    performed before any further updates are allowed.

    If no revision is specified, the working directory's parent is a
    head revision, and the repository contains exactly one other head,
    the other head is merged with by default.  Otherwise, an explicit
    revision to merge with must be provided.

options:

 -f --force  force a merge with outstanding changes
 -r --rev    revision to merge

use "hg -v help merge" to show global options
```



---

Attachment


---

Comment by pdehaye created at 2007-08-22 19:30:08

Changing status from new to assigned.


---

Comment by pdehaye created at 2007-08-22 19:30:08

the file attached should fix the bug


---

Comment by pdehaye created at 2007-08-22 19:30:08

Changing assignee from was to pdehaye.


---

Comment by was created at 2007-08-29 02:52:03

Applied for sage-2.8.3


---

Comment by was created at 2007-08-29 02:54:35

Resolution: fixed
