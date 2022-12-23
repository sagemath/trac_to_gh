# Issue 3312: dsage.setup() -- very serious bug

archive/issues_003312.json:
```json
{
    "body": "Assignee: yi\n\nDo \n\n```\nsage: dsage.setup()\n```\n\nand take all the defaults, then do it again immediately but enter a non-default hostname.\nBOOM!\nSee http://sage.pastebin.com/m1ff54979 for a log of this. \n\nThe error involves sqlalchemy table insertion; somebody messed up:\n\n```\n    739         if not self.non_primary and '_class_state' in self.class_.__dict__ and (self.entity_name in self.class_._class_state.mappers):\n--> 740              raise exceptions.ArgumentError(\"Class '%s' already has a primary mapper defined with entity name '%s'.  Use non_primary=True to create a non primary Mapper.  clear_mappers() will remove *all* current mappers from all classes.\" % (self.class_, self.entity_name))\n    741 \n    742         def extra_init(class_, oldinit, instance, args, kwargs):\n\nArgumentError: Class '<class 'sage.dsage.database.job.Job'>' already has a primary mapper defined with entity name 'None'.  Use non_primary=True to create a non primary Mapper.  clear_mappers() will remove *all* current mappers from all classes.\nsage: \n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3312\n\n",
    "created_at": "2008-05-27T04:24:16Z",
    "labels": [
        "dsage",
        "blocker",
        "bug"
    ],
    "title": "dsage.setup() -- very serious bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3312",
    "user": "was"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/3312





---

archive/issue_comments_022907.json:
```json
{
    "body": "Attachment\n\nadd clear_mapper call to db_config.py",
    "created_at": "2008-05-27T05:14:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3312",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3312#issuecomment-22907",
    "user": "yi"
}
```

Attachment

add clear_mapper call to db_config.py



---

archive/issue_comments_022908.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_gfurnish\".",
    "created_at": "2008-06-15T21:32:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3312",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3312#issuecomment-22908",
    "user": "craigcitro"
}
```

Changing keywords from "" to "editor_gfurnish".



---

archive/issue_comments_022909.json:
```json
{
    "body": "DSage is completely broken in 3.0.2 and 3.0.3!!!!! Can you post some patches so that we can run it out of the box?",
    "created_at": "2008-06-16T20:32:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3312",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3312#issuecomment-22909",
    "user": "gfurnish"
}
```

DSage is completely broken in 3.0.2 and 3.0.3!!!!! Can you post some patches so that we can run it out of the box?



---

archive/issue_comments_022910.json:
```json
{
    "body": "What exactly is wrong with this patch? Use this ticket to provide feedback about this particular patch and the issue it aims to fix. File a separate bug if dsage doesn't run for you and include some actual repro steps.",
    "created_at": "2008-06-17T22:05:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3312",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3312#issuecomment-22910",
    "user": "yi"
}
```

What exactly is wrong with this patch? Use this ticket to provide feedback about this particular patch and the issue it aims to fix. File a separate bug if dsage doesn't run for you and include some actual repro steps.



---

archive/issue_comments_022911.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-18T04:39:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3312",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3312#issuecomment-22911",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_022912.json:
```json
{
    "body": "Merged in Sage 3.0.3.final",
    "created_at": "2008-06-18T23:18:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3312",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3312#issuecomment-22912",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.3.final
