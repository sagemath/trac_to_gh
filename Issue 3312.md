# Issue 3312: dsage.setup() -- very serious bug

archive/issues_003312.json:
```json
{
    "body": "Assignee: @yqiang\n\nDo \n\n```\nsage: dsage.setup()\n```\n\nand take all the defaults, then do it again immediately but enter a non-default hostname.\nBOOM!\nSee http://sage.pastebin.com/m1ff54979 for a log of this. \n\nThe error involves sqlalchemy table insertion; somebody messed up:\n\n```\n    739         if not self.non_primary and '_class_state' in self.class_.__dict__ and (self.entity_name in self.class_._class_state.mappers):\n--> 740              raise exceptions.ArgumentError(\"Class '%s' already has a primary mapper defined with entity name '%s'.  Use non_primary=True to create a non primary Mapper.  clear_mappers() will remove *all* current mappers from all classes.\" % (self.class_, self.entity_name))\n    741 \n    742         def extra_init(class_, oldinit, instance, args, kwargs):\n\nArgumentError: Class '<class 'sage.dsage.database.job.Job'>' already has a primary mapper defined with entity name 'None'.  Use non_primary=True to create a non primary Mapper.  clear_mappers() will remove *all* current mappers from all classes.\nsage: \n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3312\n\n",
    "created_at": "2008-05-27T04:24:16Z",
    "labels": [
        "component: dsage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.3",
    "title": "dsage.setup() -- very serious bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3312",
    "user": "https://github.com/williamstein"
}
```
Assignee: @yqiang

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


Issue created by migration from https://trac.sagemath.org/ticket/3312





---

archive/issue_comments_022859.json:
```json
{
    "body": "Attachment [3312_clearmappers.patch](tarball://root/attachments/some-uuid/ticket3312/3312_clearmappers.patch) by @yqiang created at 2008-05-27 05:14:46\n\nadd clear_mapper call to db_config.py",
    "created_at": "2008-05-27T05:14:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3312",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3312#issuecomment-22859",
    "user": "https://github.com/yqiang"
}
```

Attachment [3312_clearmappers.patch](tarball://root/attachments/some-uuid/ticket3312/3312_clearmappers.patch) by @yqiang created at 2008-05-27 05:14:46

add clear_mapper call to db_config.py



---

archive/issue_comments_022860.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_gfurnish\".",
    "created_at": "2008-06-15T21:32:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3312",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3312#issuecomment-22860",
    "user": "https://github.com/craigcitro"
}
```

Changing keywords from "" to "editor_gfurnish".



---

archive/issue_comments_022861.json:
```json
{
    "body": "DSage is completely broken in 3.0.2 and 3.0.3!!!!! Can you post some patches so that we can run it out of the box?",
    "created_at": "2008-06-16T20:32:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3312",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3312#issuecomment-22861",
    "user": "https://github.com/garyfurnish"
}
```

DSage is completely broken in 3.0.2 and 3.0.3!!!!! Can you post some patches so that we can run it out of the box?



---

archive/issue_comments_022862.json:
```json
{
    "body": "What exactly is wrong with this patch? Use this ticket to provide feedback about this particular patch and the issue it aims to fix. File a separate bug if dsage doesn't run for you and include some actual repro steps.",
    "created_at": "2008-06-17T22:05:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3312",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3312#issuecomment-22862",
    "user": "https://github.com/yqiang"
}
```

What exactly is wrong with this patch? Use this ticket to provide feedback about this particular patch and the issue it aims to fix. File a separate bug if dsage doesn't run for you and include some actual repro steps.



---

archive/issue_events_003532.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2008-06-18T04:39:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3312",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3312#event-3532"
}
```



---

archive/issue_comments_022863.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-18T04:39:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3312",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3312#issuecomment-22863",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_022864.json:
```json
{
    "body": "Merged in Sage 3.0.3.final",
    "created_at": "2008-06-18T23:18:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3312",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3312#issuecomment-22864",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.3.final
