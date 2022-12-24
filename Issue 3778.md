# Issue 3778: [with patch, do not review] part 1 of new configuration system

archive/issues_003778.json:
```json
{
    "body": "Assignee: boothby\n\n(1) Centralized dictionary of the configurable settings with object oriented interface\n(2) CurrentConfig class will have process_runtime method taking the arguments at runtime and updating the current configuration\n(3) run_notebook.py will use current_config.value(SETTING) to retrieve current configuration for each setting needed at run_time\n(4) NotebookObject's __doc__ wil be dynamically created\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3778\n\n",
    "created_at": "2008-08-05T23:27:01Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "title": "[with patch, do not review] part 1 of new configuration system",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3778",
    "user": "TimothyClemans"
}
```
Assignee: boothby

(1) Centralized dictionary of the configurable settings with object oriented interface
(2) CurrentConfig class will have process_runtime method taking the arguments at runtime and updating the current configuration
(3) run_notebook.py will use current_config.value(SETTING) to retrieve current configuration for each setting needed at run_time
(4) NotebookObject's __doc__ wil be dynamically created



Issue created by migration from https://trac.sagemath.org/ticket/3778





---

archive/issue_comments_026865.json:
```json
{
    "body": "Attachment [sage-3778.patch](tarball://root/attachments/some-uuid/ticket3778/sage-3778.patch) by TimothyClemans created at 2008-08-05 23:39:12",
    "created_at": "2008-08-05T23:39:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3778#issuecomment-26865",
    "user": "TimothyClemans"
}
```

Attachment [sage-3778.patch](tarball://root/attachments/some-uuid/ticket3778/sage-3778.patch) by TimothyClemans created at 2008-08-05 23:39:12



---

archive/issue_comments_026866.json:
```json
{
    "body": "This has bitrotted beyond repair.",
    "created_at": "2009-11-19T23:31:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3778#issuecomment-26866",
    "user": "was"
}
```

This has bitrotted beyond repair.



---

archive/issue_comments_026867.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-11-19T23:31:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3778",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3778#issuecomment-26867",
    "user": "was"
}
```

Resolution: invalid
