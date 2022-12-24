# Issue 5412: bug in edit and set_edit_template

archive/issues_005412.json:
```json
{
    "body": "Assignee: cwitty\n\nCheck this out:\n\n```\nsage: edit(0)\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n\n/Users/wstein/.sage/temp/h70_33_89_223.paws.uga.edu/13827/_Users_wstein__sage_init_sage_0.py in <module>()\n\n/Users/wstein/build/sage-3.4.alpha0/local/lib/python2.5/site-packages/sage/misc/edit_module.pyc in edit(obj, editor, bg)\n    243          set_editor(base,opts=opts)\n    244       except (ValueError, KeyError, IndexError):\n--> 245          raise ValueError, \"Use set_edit_template(<template_string>) to set a default\"\n    246       \n    247    if not(edit_template):\n\nValueError: Use set_edit_template(<template_string>) to set a default\nsage: set_edit_template('e')\n---------------------------------------------------------------------------\nNameError                                 Traceback (most recent call last)\n\n/Users/wstein/.sage/temp/h70_33_89_223.paws.uga.edu/13827/_Users_wstein__sage_init_sage_0.py in <module>()\n\nNameError: name 'set_edit_template' is not defined\n```\n\n\nEither the error message should be changed or set_edit_template should be imported at the top level.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5412\n\n",
    "created_at": "2009-03-01T16:10:04Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "title": "bug in edit and set_edit_template",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5412",
    "user": "was"
}
```
Assignee: cwitty

Check this out:

```
sage: edit(0)
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/Users/wstein/.sage/temp/h70_33_89_223.paws.uga.edu/13827/_Users_wstein__sage_init_sage_0.py in <module>()

/Users/wstein/build/sage-3.4.alpha0/local/lib/python2.5/site-packages/sage/misc/edit_module.pyc in edit(obj, editor, bg)
    243          set_editor(base,opts=opts)
    244       except (ValueError, KeyError, IndexError):
--> 245          raise ValueError, "Use set_edit_template(<template_string>) to set a default"
    246       
    247    if not(edit_template):

ValueError: Use set_edit_template(<template_string>) to set a default
sage: set_edit_template('e')
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

/Users/wstein/.sage/temp/h70_33_89_223.paws.uga.edu/13827/_Users_wstein__sage_init_sage_0.py in <module>()

NameError: name 'set_edit_template' is not defined
```


Either the error message should be changed or set_edit_template should be imported at the top level.

Issue created by migration from https://trac.sagemath.org/ticket/5412





---

archive/issue_comments_041845.json:
```json
{
    "body": "Attachment [trac_5412.patch](tarball://root/attachments/some-uuid/ticket5412/trac_5412.patch) by mabshoff created at 2009-03-02 05:20:22",
    "created_at": "2009-03-02T05:20:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5412",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5412#issuecomment-41845",
    "user": "mabshoff"
}
```

Attachment [trac_5412.patch](tarball://root/attachments/some-uuid/ticket5412/trac_5412.patch) by mabshoff created at 2009-03-02 05:20:22



---

archive/issue_comments_041846.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-02T05:20:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5412",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5412#issuecomment-41846",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_041847.json:
```json
{
    "body": "Changing assignee from cwitty to mabshoff.",
    "created_at": "2009-03-02T05:20:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5412",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5412#issuecomment-41847",
    "user": "mabshoff"
}
```

Changing assignee from cwitty to mabshoff.



---

archive/issue_comments_041848.json:
```json
{
    "body": "good!! thanks!!!1",
    "created_at": "2009-03-02T05:21:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5412",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5412#issuecomment-41848",
    "user": "was"
}
```

good!! thanks!!!1



---

archive/issue_comments_041849.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-02T05:22:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5412",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5412#issuecomment-41849",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_041850.json:
```json
{
    "body": "Merged in Sage 3.4.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-02T05:22:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5412",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5412#issuecomment-41850",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.rc0.

Cheers,

Michael
