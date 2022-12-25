# Issue 1395: notebook(directory="foo/") misbehaves

archive/issues_001395.json:
```json
{
    "body": "Assignee: boothby\n\nIf the directory name is provied with a trailing \"/\" then\n\n```\nSAGE/local/lib/python2.5/site-packages/sage/server/notebook/notebook.py in __init__(self, dir, system, show_debug, log_server, address, port, secure, server_pool)\n     59         self.__worksheet_dir = '%s/worksheets'%dir\n     60         self.__object_dir    = '%s/objects'%dir\n---> 61         self.__makedirs()\n     62         self.__history = []\n     63         self.__history_count = 0\n\nSAGE/local/lib/python2.5/site-packages/sage/server/notebook/notebook.py in __makedirs(self)\n    666     def __makedirs(self):\n    667         if not os.path.exists(self.__dir):\n--> 668             os.makedirs(self.__dir)\n    669         if not os.path.exists(self.__worksheet_dir):\n    670             os.makedirs(self.__worksheet_dir)\n\n\nSAGE/local/lib/python2.5/os.py in makedirs(name, mode)\n    170         if tail == curdir:           # xxx/newdir/. exists if xxx/newdir exists\n    171             return\n--> 172     mkdir(name, mode)\n    173\n    174 def removedirs(name):\n\n<type 'exceptions.OSError'>: [Errno 2] No such file or directory: ''\n```\n\n\nThis is particularly annoying because tab completion returns directory names with trailing \"/\".\n\nIssue created by migration from https://trac.sagemath.org/ticket/1395\n\n",
    "created_at": "2007-12-04T15:37:30Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "notebook(directory=\"foo/\") misbehaves",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1395",
    "user": "https://github.com/malb"
}
```
Assignee: boothby

If the directory name is provied with a trailing "/" then

```
SAGE/local/lib/python2.5/site-packages/sage/server/notebook/notebook.py in __init__(self, dir, system, show_debug, log_server, address, port, secure, server_pool)
     59         self.__worksheet_dir = '%s/worksheets'%dir
     60         self.__object_dir    = '%s/objects'%dir
---> 61         self.__makedirs()
     62         self.__history = []
     63         self.__history_count = 0

SAGE/local/lib/python2.5/site-packages/sage/server/notebook/notebook.py in __makedirs(self)
    666     def __makedirs(self):
    667         if not os.path.exists(self.__dir):
--> 668             os.makedirs(self.__dir)
    669         if not os.path.exists(self.__worksheet_dir):
    670             os.makedirs(self.__worksheet_dir)


SAGE/local/lib/python2.5/os.py in makedirs(name, mode)
    170         if tail == curdir:           # xxx/newdir/. exists if xxx/newdir exists
    171             return
--> 172     mkdir(name, mode)
    173
    174 def removedirs(name):

<type 'exceptions.OSError'>: [Errno 2] No such file or directory: ''
```


This is particularly annoying because tab completion returns directory names with trailing "/".

Issue created by migration from https://trac.sagemath.org/ticket/1395





---

archive/issue_comments_008943.json:
```json
{
    "body": "Changing assignee from boothby to @mwhansen.",
    "created_at": "2007-12-06T00:38:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1395#issuecomment-8943",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from boothby to @mwhansen.



---

archive/issue_comments_008944.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-06T00:38:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1395#issuecomment-8944",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_008945.json:
```json
{
    "body": "Attachment [1395.patch](tarball://root/attachments/some-uuid/ticket1395/1395.patch) by @mwhansen created at 2007-12-06 00:38:51",
    "created_at": "2007-12-06T00:38:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1395#issuecomment-8945",
    "user": "https://github.com/mwhansen"
}
```

Attachment [1395.patch](tarball://root/attachments/some-uuid/ticket1395/1395.patch) by @mwhansen created at 2007-12-06 00:38:51



---

archive/issue_comments_008946.json:
```json
{
    "body": "Looks good: code seems reasonable, and it does fix the problem.",
    "created_at": "2007-12-15T02:15:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1395#issuecomment-8946",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Looks good: code seems reasonable, and it does fix the problem.



---

archive/issue_comments_008947.json:
```json
{
    "body": "Merged in 2.9.rc0.",
    "created_at": "2007-12-15T04:47:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1395#issuecomment-8947",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.rc0.



---

archive/issue_events_003596.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-15T04:47:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1395",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1395#event-3596"
}
```



---

archive/issue_comments_008948.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-15T04:47:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1395",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1395#issuecomment-8948",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
