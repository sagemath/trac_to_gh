# Issue 6345: load/attach do not recursively preparse files when run in interpreter

archive/issues_006345.json:
```json
{
    "body": "Assignee: was\n\nCC:  mvngu\n\nKeywords: preparse ipython attach load\n\nFrom http://groups.google.com/group/sage-support/browse_thread/thread/9aa4fa8cdb5d8b90:\n\n\n```\nAfter a lot of headaches over some mysterious behaviour in some\nscripts, I found the following:\nI have two files:\ntest1.sage contains:\nattach test2.sage\nprint \"test1\", 1/2\n\ntest2.sage contains:\nprint \"test2\", 1/2\n\nWhen I say on the command line of sage 3.3: attach test1.sage, the\noutput is (correctly):\nsage: attach test1.sage\ntest2 1/2\ntest1 1/2\n\nBut on sage 4.01, the output is:\nsage: attach test1.sage\ntest2 0\ntest1 1/2\n\nIt looks as if on a file that is attached from another attached file,\nno preparsing takes place. If within this same session I touch\ntest2.sage, it works fine. \n```\n\n\nThis is only a problem in the IPython interpeter; when running from the command line, the files are recursively preparsed correctly.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6345\n\n",
    "created_at": "2009-06-17T00:51:06Z",
    "labels": [
        "user interface",
        "major",
        "bug"
    ],
    "title": "load/attach do not recursively preparse files when run in interpreter",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6345",
    "user": "ddrake"
}
```
Assignee: was

CC:  mvngu

Keywords: preparse ipython attach load

From http://groups.google.com/group/sage-support/browse_thread/thread/9aa4fa8cdb5d8b90:


```
After a lot of headaches over some mysterious behaviour in some
scripts, I found the following:
I have two files:
test1.sage contains:
attach test2.sage
print "test1", 1/2

test2.sage contains:
print "test2", 1/2

When I say on the command line of sage 3.3: attach test1.sage, the
output is (correctly):
sage: attach test1.sage
test2 1/2
test1 1/2

But on sage 4.01, the output is:
sage: attach test1.sage
test2 0
test1 1/2

It looks as if on a file that is attached from another attached file,
no preparsing takes place. If within this same session I touch
test2.sage, it works fine. 
```


This is only a problem in the IPython interpeter; when running from the command line, the files are recursively preparsed correctly.

Issue created by migration from https://trac.sagemath.org/ticket/6345





---

archive/issue_comments_050729.json:
```json
{
    "body": "Just briefly looking around, perhaps there's a problem in `preparse_file()` in `sage.misc.preparser`: when attaching a .sage file, it does:\n\n```\nelif name_load[-5:] == '.sage':\n                try:\n                    G = open(name_load)\n                except IOError:\n                    print \"File '%s' not found, so skipping load of %s\"%(name_load, name_load)\n                    i += 1\n                    continue\n                else:\n                    A = A[:i] + G.readlines() + A[i+1:]\n                    continue\n```\n\nIn the example given in this ticket, it seems to just insert the lines of test2.sage without preparsing them.",
    "created_at": "2009-06-17T01:05:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6345#issuecomment-50729",
    "user": "ddrake"
}
```

Just briefly looking around, perhaps there's a problem in `preparse_file()` in `sage.misc.preparser`: when attaching a .sage file, it does:

```
elif name_load[-5:] == '.sage':
                try:
                    G = open(name_load)
                except IOError:
                    print "File '%s' not found, so skipping load of %s"%(name_load, name_load)
                    i += 1
                    continue
                else:
                    A = A[:i] + G.readlines() + A[i+1:]
                    continue
```

In the example given in this ticket, it seems to just insert the lines of test2.sage without preparsing them.



---

archive/issue_comments_050730.json:
```json
{
    "body": "This appears to be fixed, post-#7514.  For example, with\n\n```sh\n> cat test1.sage \nattach test2.sage\nprint \"test1\", [1..10]\n> cat test2.sage \nprint \"test2\", [11..20]\n```\n\nI see\n\n```python\nsage: attach test1.sage\ntest2 [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]\ntest1 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\nsage: attached_files()\n['test1.sage', 'test2.sage']\nsage: # After 'touch test2.sage'\ntest2 [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]\nsage: # After 'touch test1.sage'\ntest2 [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]\ntest1 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n```\n\nIf I'm correct, should we close this ticket?",
    "created_at": "2010-01-20T11:13:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6345#issuecomment-50730",
    "user": "mpatel"
}
```

This appears to be fixed, post-#7514.  For example, with

```sh
> cat test1.sage 
attach test2.sage
print "test1", [1..10]
> cat test2.sage 
print "test2", [11..20]
```

I see

```python
sage: attach test1.sage
test2 [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
test1 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sage: attached_files()
['test1.sage', 'test2.sage']
sage: # After 'touch test2.sage'
test2 [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
sage: # After 'touch test1.sage'
test2 [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
test1 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

If I'm correct, should we close this ticket?



---

archive/issue_comments_050731.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2010-01-20T11:13:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6345#issuecomment-50731",
    "user": "mpatel"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_050732.json:
```json
{
    "body": "Close as fixed by #7514:\n\n```\n[mvngu@sage sage]$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nsage: attach test1.sage\ntest2 1/2\ntest1 1/2\nsage: attach test3.sage\ntest4 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\ntest3 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\nsage: !touch test2.sage\nsage: attach test1.sage\ntest2 1/2\ntest2 1/2\ntest1 1/2\nsage: !touch test4.sage\nsage: attach test3.sage\ntest4 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\ntest4 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\ntest3 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\nsage: !more test1.sage\nattach test2.sage\nprint \"test1\", 1/2\nsage: !more test2.sage\nprint \"test2\", 1/2\nsage: !more test3.sage\nattach test4.sage\nprint \"test3\", [1..10]\nsage: !more test4.sage\nprint \"test4\", [1..10]\n```\n",
    "created_at": "2010-02-05T19:57:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6345#issuecomment-50732",
    "user": "mvngu"
}
```

Close as fixed by #7514:

```
[mvngu@sage sage]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: attach test1.sage
test2 1/2
test1 1/2
sage: attach test3.sage
test4 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test3 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sage: !touch test2.sage
sage: attach test1.sage
test2 1/2
test2 1/2
test1 1/2
sage: !touch test4.sage
sage: attach test3.sage
test4 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test4 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test3 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sage: !more test1.sage
attach test2.sage
print "test1", 1/2
sage: !more test2.sage
print "test2", 1/2
sage: !more test3.sage
attach test4.sage
print "test3", [1..10]
sage: !more test4.sage
print "test4", [1..10]
```




---

archive/issue_comments_050733.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-05T19:57:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6345",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6345#issuecomment-50733",
    "user": "mvngu"
}
```

Resolution: fixed
