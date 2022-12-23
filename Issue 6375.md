# Issue 6375: Run sage once as part of install process to generate sage-flags.txt

archive/issues_006375.json:
```json
{
    "body": "Assignee: tbd\n\nWhen sage runs for the first time, it creates a file `sage-flags.txt` to keep track of what special instructions the CPU supports. Several people have run into trouble compiling and installing sage as root, and then running it as a normal user, because they don't have permission to create the file. Here's such a traceback:\n\n\n```\nTraceback (most recent call last):\n  File \"/usr/local/sage-4.0.2/local/bin/sage-location\", line 174, in <module>\n    t, R = install_moved()\n  File \"/usr/local/sage-4.0.2/local/bin/sage-location\", line 18, in install_moved\n    write_flags_file()\n  File \"/usr/local/sage-4.0.2/local/bin/sage-location\", line 82, in write_flags_file\n    open(flags_file,'w').write(get_flags_info())\nIOError: [Errno 13] Permission denied: '/usr/local/sage-4.0.2/local/lib/sage-flags.txt'\n```\n\n\nIt would seem sensible to run `local/bin/sage-starts` once during the install process to create this file.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6375\n\n",
    "created_at": "2009-06-20T20:53:26Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "title": "Run sage once as part of install process to generate sage-flags.txt",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6375",
    "user": "craigcitro"
}
```
Assignee: tbd

When sage runs for the first time, it creates a file `sage-flags.txt` to keep track of what special instructions the CPU supports. Several people have run into trouble compiling and installing sage as root, and then running it as a normal user, because they don't have permission to create the file. Here's such a traceback:


```
Traceback (most recent call last):
  File "/usr/local/sage-4.0.2/local/bin/sage-location", line 174, in <module>
    t, R = install_moved()
  File "/usr/local/sage-4.0.2/local/bin/sage-location", line 18, in install_moved
    write_flags_file()
  File "/usr/local/sage-4.0.2/local/bin/sage-location", line 82, in write_flags_file
    open(flags_file,'w').write(get_flags_info())
IOError: [Errno 13] Permission denied: '/usr/local/sage-4.0.2/local/lib/sage-flags.txt'
```


It would seem sensible to run `local/bin/sage-starts` once during the install process to create this file.

Issue created by migration from https://trac.sagemath.org/ticket/6375





---

archive/issue_comments_051019.json:
```json
{
    "body": "Duplicate of #11926.",
    "created_at": "2012-04-02T15:46:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6375#issuecomment-51019",
    "user": "jdemeyer"
}
```

Duplicate of #11926.



---

archive/issue_comments_051020.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2012-04-02T15:46:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6375#issuecomment-51020",
    "user": "jdemeyer"
}
```

Resolution: duplicate
