# Issue 6848: [with patch, needs review] "Definition:" messed up in notebook and command line in cython code

archive/issues_006848.json:
```json
{
    "body": "Assignee: @jhpalmieri\n\nQuoted from #5726:\n\n```\nsage: RDF.random_element?\n...\nDefinition: RDF.random_element(min='-1', max='1')\n```\n\nNotice the stupid quotes around -1 and 1, which are very confusing!\n\nAlso, from the command line, if you type `RDF.random_element?`, you don't see a \"Definition\" line at all.  This patch fixes both issues: the first by using `eval(argument)`, as suggested by timdumol at #5726, and the second by setting \n\n```\nIPython.OInspect.getargspec = sageinspect.sage_getargspec\n```\n\nin sage.misc.interpreter.  Note that `sage_getargspec` is a modified version of `getargspec` to start with, so this modification should work in general.  (It was already in use, essentially, in the notebook -- introspection in the notebook calls `sage_getdef`, which in turn calls `sage_getargspec`.  See the function `docstring` in `sage.server.support`.)\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6848\n\n",
    "created_at": "2009-08-30T21:36:25Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with patch, needs review] \"Definition:\" messed up in notebook and command line in cython code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6848",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @jhpalmieri

Quoted from #5726:

```
sage: RDF.random_element?
...
Definition: RDF.random_element(min='-1', max='1')
```

Notice the stupid quotes around -1 and 1, which are very confusing!

Also, from the command line, if you type `RDF.random_element?`, you don't see a "Definition" line at all.  This patch fixes both issues: the first by using `eval(argument)`, as suggested by timdumol at #5726, and the second by setting 

```
IPython.OInspect.getargspec = sageinspect.sage_getargspec
```

in sage.misc.interpreter.  Note that `sage_getargspec` is a modified version of `getargspec` to start with, so this modification should work in general.  (It was already in use, essentially, in the notebook -- introspection in the notebook calls `sage_getdef`, which in turn calls `sage_getargspec`.  See the function `docstring` in `sage.server.support`.)


Issue created by migration from https://trac.sagemath.org/ticket/6848





---

archive/issue_comments_056370.json:
```json
{
    "body": "Attachment [trac_6848-defn.patch](tarball://root/attachments/some-uuid/ticket6848/trac_6848-defn.patch) by @jhpalmieri created at 2009-08-30 21:38:47\n\ndepends on patch at #5726",
    "created_at": "2009-08-30T21:38:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6848",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6848#issuecomment-56370",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_6848-defn.patch](tarball://root/attachments/some-uuid/ticket6848/trac_6848-defn.patch) by @jhpalmieri created at 2009-08-30 21:38:47

depends on patch at #5726



---

archive/issue_events_016115.json:
```json
{
    "actor": "https://github.com/jhpalmieri",
    "created_at": "2009-09-03T04:36:07Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6848",
    "milestone": "sage-4.1.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6848#event-16115"
}
```



---

archive/issue_comments_056371.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-09-08T23:01:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6848",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6848#issuecomment-56371",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_056372.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-09T10:09:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6848",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6848#issuecomment-56372",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_016116.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-09T10:09:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6848",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6848#event-16116"
}
```
