# Issue 8303: Sage cannot work with files with spaces in their names

archive/issues_008303.json:
```json
{
    "body": "Assignee: was\n\nKeywords: spaces filenames\n\nScripts with spaces in their names defeat Sage:\n\n```\n$ sage \"my script.sage\" \n/opt/sage/local/bin/sage-sage: line 147: [: too many arguments\n/opt/sage/local/bin/sage-sage: line 150: [: too many arguments\n/opt/sage/local/bin/sage-sage: line 200: [: too many arguments\n[...]\n/opt/sage/local/bin/sage-sage: line 892: [: too many arguments\n/opt/sage/local/bin/sage-preparse: File my is missing\n/opt/sage/local/bin/sage-preparse: File script.sage is missing\npython: can't open file 'my': [Errno 2] No such file or directory\n```\n\nTicket #4354 claimed to fix this, but it's still broken on 4.3.2.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8303\n\n",
    "created_at": "2010-02-19T02:32:06Z",
    "labels": [
        "user interface",
        "major",
        "bug"
    ],
    "title": "Sage cannot work with files with spaces in their names",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8303",
    "user": "ddrake"
}
```
Assignee: was

Keywords: spaces filenames

Scripts with spaces in their names defeat Sage:

```
$ sage "my script.sage" 
/opt/sage/local/bin/sage-sage: line 147: [: too many arguments
/opt/sage/local/bin/sage-sage: line 150: [: too many arguments
/opt/sage/local/bin/sage-sage: line 200: [: too many arguments
[...]
/opt/sage/local/bin/sage-sage: line 892: [: too many arguments
/opt/sage/local/bin/sage-preparse: File my is missing
/opt/sage/local/bin/sage-preparse: File script.sage is missing
python: can't open file 'my': [Errno 2] No such file or directory
```

Ticket #4354 claimed to fix this, but it's still broken on 4.3.2.

Issue created by migration from https://trac.sagemath.org/ticket/8303





---

archive/issue_comments_073568.json:
```json
{
    "body": "Changing assignee from was to ddrake.",
    "created_at": "2010-02-19T04:35:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8303#issuecomment-73568",
    "user": "ddrake"
}
```

Changing assignee from was to ddrake.



---

archive/issue_comments_073569.json:
```json
{
    "body": "I have the beginnings of patch, but I already know some of the problems going on here.\n\n* First, if $1 contains spaces, then whenever you do `if [ $1 = \"blah\" ]` the shell expands $1 into multiple words and the test gets confused. The script `sage-sage` is riddled with such things, which is the source of the \"too many arguments\" business above.\n\n* Second, the sage-sage script, if given non-option arguments (i.e., no -python, -preparse, etc) punts to the Python script sage-run. Inside sage-run, we have things like\n\n```\n os.system('\"$SAGE_LOCAL/bin/sage-python\" %s.py %s'%(file[:-5], options))\n```\n\nwhere \"options\" contains all the arguments you originally passed to Sage. Unfortunately, when you do `os.system`, it seems to split words on all whitespace, which means at this point, we lose all information about command-line arguments with spaces in them.\n\nIt looks like we should be using subprocess.Popen (http://docs.python.org/library/subprocess.html#subprocess.Popen), which accepts a *list* of arguments and hence can deal with spaces properly.",
    "created_at": "2010-02-19T04:35:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8303#issuecomment-73569",
    "user": "ddrake"
}
```

I have the beginnings of patch, but I already know some of the problems going on here.

* First, if $1 contains spaces, then whenever you do `if [ $1 = "blah" ]` the shell expands $1 into multiple words and the test gets confused. The script `sage-sage` is riddled with such things, which is the source of the "too many arguments" business above.

* Second, the sage-sage script, if given non-option arguments (i.e., no -python, -preparse, etc) punts to the Python script sage-run. Inside sage-run, we have things like

```
 os.system('"$SAGE_LOCAL/bin/sage-python" %s.py %s'%(file[:-5], options))
```

where "options" contains all the arguments you originally passed to Sage. Unfortunately, when you do `os.system`, it seems to split words on all whitespace, which means at this point, we lose all information about command-line arguments with spaces in them.

It looks like we should be using subprocess.Popen (http://docs.python.org/library/subprocess.html#subprocess.Popen), which accepts a *list* of arguments and hence can deal with spaces properly.



---

archive/issue_comments_073570.json:
```json
{
    "body": "apply to sage_scripts spkg",
    "created_at": "2010-02-21T07:52:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8303#issuecomment-73570",
    "user": "ddrake"
}
```

apply to sage_scripts spkg



---

archive/issue_comments_073571.json:
```json
{
    "body": "Attachment [trac_8303.patch](tarball://root/attachments/some-uuid/ticket8303/trac_8303.patch) by ddrake created at 2010-02-21 08:05:42\n\nPatch up. Apply to sage_scripts spkg, or equivalently, to the repo in SAGE_ROOT/local/bin.\n\nTo test, try making a file with spaces in its name, and passing arguments with spaces in them. If the file is \"script with spaces.sage\" and it contains:\n\n```\nimport sys\nprint integrate(x*cos(x)*sin(x), x)\nprint sys.argv\nsys.exit(int(5))\n```\n\nthen something like this should work properly:\n\n```\n$ sage \"script with spaces.sage\" \"foo bar\" arg2\n-1/4*x*cos(2*x) + 1/8*sin(2*x)\n['script with spaces.py', 'foo bar', 'arg2']\n$ echo $?\n5\n```\n\nI'd like to have the return code tested to make sure we don't get a regression on #2861.\n\nPlease test and review!",
    "created_at": "2010-02-21T08:05:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8303#issuecomment-73571",
    "user": "ddrake"
}
```

Attachment [trac_8303.patch](tarball://root/attachments/some-uuid/ticket8303/trac_8303.patch) by ddrake created at 2010-02-21 08:05:42

Patch up. Apply to sage_scripts spkg, or equivalently, to the repo in SAGE_ROOT/local/bin.

To test, try making a file with spaces in its name, and passing arguments with spaces in them. If the file is "script with spaces.sage" and it contains:

```
import sys
print integrate(x*cos(x)*sin(x), x)
print sys.argv
sys.exit(int(5))
```

then something like this should work properly:

```
$ sage "script with spaces.sage" "foo bar" arg2
-1/4*x*cos(2*x) + 1/8*sin(2*x)
['script with spaces.py', 'foo bar', 'arg2']
$ echo $?
5
```

I'd like to have the return code tested to make sure we don't get a regression on #2861.

Please test and review!



---

archive/issue_comments_073572.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-21T08:05:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8303#issuecomment-73572",
    "user": "ddrake"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_073573.json:
```json
{
    "body": "Also, there is a script called sage-run2 in SAGE_ROOT/local/bin, which seems to me like abandoned cruft. There are no references to that file outside of the Mercurial repo store. It appears to be a script that allows you to sequentially run Sage on several files. I think that functionality would be easy to add to sage-run. Should we remove sage-run2 and put the functionality into sage-run?",
    "created_at": "2010-02-21T08:18:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8303#issuecomment-73573",
    "user": "ddrake"
}
```

Also, there is a script called sage-run2 in SAGE_ROOT/local/bin, which seems to me like abandoned cruft. There are no references to that file outside of the Mercurial repo store. It appears to be a script that allows you to sequentially run Sage on several files. I think that functionality would be easy to add to sage-run. Should we remove sage-run2 and put the functionality into sage-run?



---

archive/issue_comments_073574.json:
```json
{
    "body": "Another point for testing: #4354 later got reverted (see changeset 1119:553a52746e3c in sage_scripts) because it interfered with -sdist; I tested this patch and it appears to cooperate with -sdist.",
    "created_at": "2010-02-23T13:10:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8303#issuecomment-73574",
    "user": "ddrake"
}
```

Another point for testing: #4354 later got reverted (see changeset 1119:553a52746e3c in sage_scripts) because it interfered with -sdist; I tested this patch and it appears to cooperate with -sdist.



---

archive/issue_comments_073575.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-28T03:41:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8303#issuecomment-73575",
    "user": "was"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_073576.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-29T05:17:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8303#issuecomment-73576",
    "user": "was"
}
```

Resolution: fixed
