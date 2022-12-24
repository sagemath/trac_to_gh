# Issue 7586: develoers' guide: document features of attach, load, iload, ed, %ed, %edit, edit()

archive/issues_007586.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  jhpalmieri\n\nFrom this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/c0543314ff9c15cb) thread:\n\n```\nBy the way, I discovered accidentally that from the command line (not\nthe notebook) if you type:\n\nsage: ed   # or %ed or %edit\n\nthen it opens up your favorite editor (whatever is set by the $EDITOR\nshell variable).  Then in the editor you can type\n\ndef FF(x):\n    long definition here\n    which would be really annoying\n    to type on the command line\n\nthen save it -- it gets written to a temporary file -- and the code\ngets executed and you have thus redefined FF.  Then later you can do\n\nsage: ed FF\n\nand it will let you modify your code.  This is an ipython feature, it\nseems.  Should it be described somewhere in the Sage documentation?\n```\n\nThe following commands should at least be documented in the Developers' Guide together with explanation on how to use them for interactive development:\n\n1. `load`\n2. `attach`\n3. `iload`\n4. `ed`\n5. `%ed`\n6. `%edit`\n7. `edit()`\n\nIssue created by migration from https://trac.sagemath.org/ticket/7586\n\n",
    "created_at": "2009-12-02T20:33:17Z",
    "labels": [
        "documentation",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "develoers' guide: document features of attach, load, iload, ed, %ed, %edit, edit()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7586",
    "user": "mvngu"
}
```
Assignee: mvngu

CC:  jhpalmieri

From this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/c0543314ff9c15cb) thread:

```
By the way, I discovered accidentally that from the command line (not
the notebook) if you type:

sage: ed   # or %ed or %edit

then it opens up your favorite editor (whatever is set by the $EDITOR
shell variable).  Then in the editor you can type

def FF(x):
    long definition here
    which would be really annoying
    to type on the command line

then save it -- it gets written to a temporary file -- and the code
gets executed and you have thus redefined FF.  Then later you can do

sage: ed FF

and it will let you modify your code.  This is an ipython feature, it
seems.  Should it be described somewhere in the Sage documentation?
```

The following commands should at least be documented in the Developers' Guide together with explanation on how to use them for interactive development:

1. `load`
2. `attach`
3. `iload`
4. `ed`
5. `%ed`
6. `%edit`
7. `edit()`

Issue created by migration from https://trac.sagemath.org/ticket/7586





---

archive/issue_comments_064682.json:
```json
{
    "body": "Some of those commands -- the % ones -- come from IPython, right? If so, we should find where their documentation is online and link to that, along with some brief descriptions of useful commands. One that I like is `!clear` which simply clears the screen.",
    "created_at": "2009-12-02T23:18:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7586#issuecomment-64682",
    "user": "ddrake"
}
```

Some of those commands -- the % ones -- come from IPython, right? If so, we should find where their documentation is online and link to that, along with some brief descriptions of useful commands. One that I like is `!clear` which simply clears the screen.



---

archive/issue_comments_064683.json:
```json
{
    "body": "Just a quick, somewhat-related note: `attach` and `load` have been rewritten at #7514.",
    "created_at": "2009-12-29T06:35:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7586#issuecomment-64683",
    "user": "mpatel"
}
```

Just a quick, somewhat-related note: `attach` and `load` have been rewritten at #7514.



---

archive/issue_comments_064684.json:
```json
{
    "body": "See #11219 for a related ticket.  (I thought that \"%edit\" was useful enough for general users that it should be in the tutorial, not just the developer's guide.)",
    "created_at": "2011-04-19T19:04:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7586#issuecomment-64684",
    "user": "jhpalmieri"
}
```

See #11219 for a related ticket.  (I thought that "%edit" was useful enough for general users that it should be in the tutorial, not just the developer's guide.)
