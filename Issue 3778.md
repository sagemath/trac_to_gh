# Issue 3778: [with patch, do not review] part 1 of new configuration system

archive/issues_003778.json:
```json
{
    "body": "Assignee: boothby\n\n(1) Centralized dictionary of the configurable settings with object oriented interface\n(2) CurrentConfig class will have process_runtime method taking the arguments at runtime and updating the current configuration\n(3) run_notebook.py will use current_config.value(SETTING) to retrieve current configuration for each setting needed at run_time\n(4) NotebookObject's __doc__ wil be dynamically created\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3778\n\n",
    "created_at": "2008-08-05T23:27:01Z",
    "labels": [
        "component: notebook"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "[with patch, do not review] part 1 of new configuration system",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3778",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```
Assignee: boothby

(1) Centralized dictionary of the configurable settings with object oriented interface
(2) CurrentConfig class will have process_runtime method taking the arguments at runtime and updating the current configuration
(3) run_notebook.py will use current_config.value(SETTING) to retrieve current configuration for each setting needed at run_time
(4) NotebookObject's __doc__ wil be dynamically created



Issue created by migration from https://trac.sagemath.org/ticket/3778





---

archive/issue_comments_026807.json:
```json
{
    "body": "Attachment [sage-3778.patch](tarball://root/attachments/some-uuid/ticket3778/sage-3778.patch) by TimothyClemans created at 2008-08-05 23:39:12",
    "created_at": "2008-08-05T23:39:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3778#issuecomment-26807",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Attachment [sage-3778.patch](tarball://root/attachments/some-uuid/ticket3778/sage-3778.patch) by TimothyClemans created at 2008-08-05 23:39:12



---

archive/issue_comments_026808.json:
```json
{
    "body": "This has bitrotted beyond repair.",
    "created_at": "2009-11-19T23:31:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3778#issuecomment-26808",
    "user": "https://github.com/williamstein"
}
```

This has bitrotted beyond repair.



---

archive/issue_comments_026809.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-11-19T23:31:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3778#issuecomment-26809",
    "user": "https://github.com/williamstein"
}
```

Resolution: invalid



---

archive/issue_events_004000.json:
```json
{
    "actor": "@williamstein",
    "created_at": "2009-11-19T23:31:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3778",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3778#event-4000"
}
```
