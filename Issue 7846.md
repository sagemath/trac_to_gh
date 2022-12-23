# Issue 7846: Missing triple-secret ___code___.py files when copying a worksheet

archive/issues_007846.json:
```json
{
    "body": "Assignee: was\n\nCC:  was\n\nCopying a worksheet in Sage 4.3.1.alpha0 sometimes gives\n\n```python\n          File \"/home/sage/notebook/sagenb-0.4.9/sagenb/notebook/twist.py\", line 795, in render\n            W = notebook.copy_worksheet(self.worksheet, self.username)\n          File \"/home/sage/notebook/sagenb-0.4.9/sagenb/notebook/notebook.py\", line 719, in copy_worksheet\n            self._initialize_worksheet(ws, W)\n          File \"/home/sage/notebook/sagenb-0.4.9/sagenb/notebook/notebook.py\", line 631, in _initialize_worksheet\n            shutil.copytree(cells, target)\n          File \"/home/apps/sage/local/lib/python/shutil.py\", line 177, in copytree\n            raise Error, errors\n        shutil.Error: [('/home/.sage/sage_notebook.sagenb/home/aaaa/21/cells/2/___code___.py', '/home/.sage/sage_notebook.sagenb/home/aaaa/28/cells/2/___code___.py', \"[Errno 2] No such file or directory: '/home/.sage/sage_notebook.sagenb/home/aaaa/21/cells/2/___code___.py'\")]\n\n```\n\n\nThis is a follow-up to #7514.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7846\n\n",
    "created_at": "2010-01-05T03:27:06Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "Missing triple-secret ___code___.py files when copying a worksheet",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7846",
    "user": "mpatel"
}
```
Assignee: was

CC:  was

Copying a worksheet in Sage 4.3.1.alpha0 sometimes gives

```python
          File "/home/sage/notebook/sagenb-0.4.9/sagenb/notebook/twist.py", line 795, in render
            W = notebook.copy_worksheet(self.worksheet, self.username)
          File "/home/sage/notebook/sagenb-0.4.9/sagenb/notebook/notebook.py", line 719, in copy_worksheet
            self._initialize_worksheet(ws, W)
          File "/home/sage/notebook/sagenb-0.4.9/sagenb/notebook/notebook.py", line 631, in _initialize_worksheet
            shutil.copytree(cells, target)
          File "/home/apps/sage/local/lib/python/shutil.py", line 177, in copytree
            raise Error, errors
        shutil.Error: [('/home/.sage/sage_notebook.sagenb/home/aaaa/21/cells/2/___code___.py', '/home/.sage/sage_notebook.sagenb/home/aaaa/28/cells/2/___code___.py', "[Errno 2] No such file or directory: '/home/.sage/sage_notebook.sagenb/home/aaaa/21/cells/2/___code___.py'")]

```


This is a follow-up to #7514.

Issue created by migration from https://trac.sagemath.org/ticket/7846





---

archive/issue_comments_067958.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2010-01-05T03:45:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7846#issuecomment-67958",
    "user": "was"
}
```

Changing priority from major to critical.



---

archive/issue_comments_067959.json:
```json
{
    "body": "Can you systematically trigger this?  It looks serious?  What was the worksheet that caused this.  The problem is probably symlinks to ___code___.py files being created when they shouldn't be, or something.   Those files should be completely ignored when copying the worksheet.",
    "created_at": "2010-01-05T03:45:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7846#issuecomment-67959",
    "user": "was"
}
```

Can you systematically trigger this?  It looks serious?  What was the worksheet that caused this.  The problem is probably symlinks to ___code___.py files being created when they shouldn't be, or something.   Those files should be completely ignored when copying the worksheet.



---

archive/issue_comments_067960.json:
```json
{
    "body": "I'll try to find a reproducible case.",
    "created_at": "2010-01-05T04:07:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7846#issuecomment-67960",
    "user": "mpatel"
}
```

I'll try to find a reproducible case.



---

archive/issue_comments_067961.json:
```json
{
    "body": "Suppress `CODE_PY` symlinks.  sagenb repo.",
    "created_at": "2010-01-05T06:24:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7846#issuecomment-67961",
    "user": "mpatel"
}
```

Suppress `CODE_PY` symlinks.  sagenb repo.



---

archive/issue_comments_067962.json:
```json
{
    "body": "Attachment\n\nThe attached patch should work for copying and re-publishing worksheets --- both use `Notebook._initialize_worksheet`.  But we should cover\n\n```python\nfname = 'foo.txt'\nfd = open(fname, 'w')\nfd.write('bar')\nfd.close()\nprint os.listdir('.')\nimport time; time.sleep(3)\nos.unlink(fname)\nprint os.listdir('.')\n```\n\ntoo...",
    "created_at": "2010-01-05T06:35:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7846#issuecomment-67962",
    "user": "mpatel"
}
```

Attachment

The attached patch should work for copying and re-publishing worksheets --- both use `Notebook._initialize_worksheet`.  But we should cover

```python
fname = 'foo.txt'
fd = open(fname, 'w')
fd.write('bar')
fd.close()
print os.listdir('.')
import time; time.sleep(3)
os.unlink(fname)
print os.listdir('.')
```

too...



---

archive/issue_comments_067963.json:
```json
{
    "body": "Which is better\n\n```python\nimport os, shutil\n\ndef ignore_nonexistent_files(curdir, dirlist):\n    ignore = []\n    for x in dirlist:\n        if not os.path.exists(os.path.join(curdir, x)):\n            ignore.append(x)\n    return ignore\n\n# This:\nshutil.copytree('foo', 'bar', ignore=ignore_nonexistent_files)\n# Or this:\nshutil.copytree('foo', 'bar', symlinks=True)\n```\n\n?  We use [shutil.copytree](http://docs.python.org/library/shutil.html#shutil.copytree) in 5 places under `sagenb`.  If it's necessary, I can add `sagenb.misc.misc.ignore_nonexistent_files`.",
    "created_at": "2010-01-05T07:21:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7846#issuecomment-67963",
    "user": "mpatel"
}
```

Which is better

```python
import os, shutil

def ignore_nonexistent_files(curdir, dirlist):
    ignore = []
    for x in dirlist:
        if not os.path.exists(os.path.join(curdir, x)):
            ignore.append(x)
    return ignore

# This:
shutil.copytree('foo', 'bar', ignore=ignore_nonexistent_files)
# Or this:
shutil.copytree('foo', 'bar', symlinks=True)
```

?  We use [shutil.copytree](http://docs.python.org/library/shutil.html#shutil.copytree) in 5 places under `sagenb`.  If it's necessary, I can add `sagenb.misc.misc.ignore_nonexistent_files`.



---

archive/issue_comments_067964.json:
```json
{
    "body": "Attachment\n\nAlso ignore non-existent files.  Replaces previous.",
    "created_at": "2010-01-05T08:13:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7846#issuecomment-67964",
    "user": "mpatel"
}
```

Attachment

Also ignore non-existent files.  Replaces previous.



---

archive/issue_comments_067965.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-05T08:21:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7846#issuecomment-67965",
    "user": "mpatel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067966.json:
```json
{
    "body": "It seems safer to skip non-existent files.  I haven't changed the lines in `Notebook.migrate_old_worksheet`, since the they're wrapped in Try-N-Save blocks.\n\nShould we delete all files that are temporarily symlinked but not actually in the final output?  Do people like to keep track of intermediaries?\n\nDifferent problem: Should deleting a cell in the notebook delete its contents on disk?",
    "created_at": "2010-01-05T08:21:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7846#issuecomment-67966",
    "user": "mpatel"
}
```

It seems safer to skip non-existent files.  I haven't changed the lines in `Notebook.migrate_old_worksheet`, since the they're wrapped in Try-N-Save blocks.

Should we delete all files that are temporarily symlinked but not actually in the final output?  Do people like to keep track of intermediaries?

Different problem: Should deleting a cell in the notebook delete its contents on disk?



---

archive/issue_comments_067967.json:
```json
{
    "body": "Positive review.  \n\nMerged into sagenb-0.5",
    "created_at": "2010-01-08T20:00:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7846#issuecomment-67967",
    "user": "was"
}
```

Positive review.  

Merged into sagenb-0.5



---

archive/issue_comments_067968.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-08T20:00:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7846#issuecomment-67968",
    "user": "was"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067969.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-08T20:00:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7846#issuecomment-67969",
    "user": "was"
}
```

Resolution: fixed
