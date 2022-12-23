# Issue 4166: Separate resource for @interact

Issue created by migration from https://trac.sagemath.org/ticket/4166

Original creator: itolkov

Original creation time: 2008-09-22 02:15:26

Assignee: itolkov

There is a new resource for the initial evaluation and later updates.


---

Attachment

Good, works, but has one problem, which is that it creates a serious security vulnerability.  It needs code like this or something like in the Worksheet_eval Resource:

```
        if owner != '_sage_':
            if W.owner() != self.username and not (self.username in W.collaborators()):
               return InvalidPage(msg = "can't evaluate worksheet cells", username = self.username\
)
```


Once this is resolved, it will get a positive review. 

It might also be nice if there were a comment that explains why we are creating this new resource.  E.g., "make code cleaner"?  "because it will be needed later for something else
that is planned?"
