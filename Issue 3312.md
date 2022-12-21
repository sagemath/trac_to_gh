# Issue 3312: dsage.setup() -- very serious bug

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-05-27 04:24:16

Assignee: yi

Do 

```
sage: dsage.setup()
```

and take all the defaults, then do it again immediately but enter a non-default hostname.
BOOM!
See http://sage.pastebin.com/m1ff54979 for a log of this. 

The error involves sqlalchemy table insertion; somebody messed up:

```
    739         if not self.non_primary and '_class_state' in self.class_.__dict__ and (self.entity_name in self.class_._class_state.mappers):
--> 740              raise exceptions.ArgumentError("Class '%s' already has a primary mapper defined with entity name '%s'.  Use non_primary=True to create a non primary Mapper.  clear_mappers() will remove *all* current mappers from all classes." % (self.class_, self.entity_name))
    741 
    742         def extra_init(class_, oldinit, instance, args, kwargs):

ArgumentError: Class '<class 'sage.dsage.database.job.Job'>' already has a primary mapper defined with entity name 'None'.  Use non_primary=True to create a non primary Mapper.  clear_mappers() will remove *all* current mappers from all classes.
sage: 

```



---

Attachment

add clear_mapper call to db_config.py


---

Comment by craigcitro created at 2008-06-15 21:32:21

Changing keywords from "" to "editor_gfurnish".


---

Comment by gfurnish created at 2008-06-16 20:32:44

DSage is completely broken in 3.0.2 and 3.0.3!!!!! Can you post some patches so that we can run it out of the box?


---

Comment by yi created at 2008-06-17 22:05:51

What exactly is wrong with this patch? Use this ticket to provide feedback about this particular patch and the issue it aims to fix. File a separate bug if dsage doesn't run for you and include some actual repro steps.


---

Comment by was created at 2008-06-18 04:39:55

Resolution: fixed


---

Comment by mabshoff created at 2008-06-18 23:18:29

Merged in Sage 3.0.3.final
