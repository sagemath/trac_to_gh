# Issue 6732: spell-check all modules under sage/server

archive/issues_006732.json:
```json
{
    "body": "Assignee: tba\n\nAs the subject says.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6732\n\n",
    "created_at": "2009-08-11T08:40:06Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "spell-check all modules under sage/server",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6732",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: tba

As the subject says.

Issue created by migration from https://trac.sagemath.org/ticket/6732





---

archive/issue_comments_055093.json:
```json
{
    "body": "based on Sage 4.1.1.rc2",
    "created_at": "2009-08-11T17:23:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6732#issuecomment-55093",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

based on Sage 4.1.1.rc2



---

archive/issue_comments_055094.json:
```json
{
    "body": "Attachment [trac_6732-spell-check-server.patch](tarball://root/attachments/some-uuid/ticket6732/trac_6732-spell-check-server.patch) by @qed777 created at 2009-08-11 22:41:34\n\n```\n$ cd $SAGE_ROOT/devel/sage/sage/server/notebook; grep rrr *.py\n./notebook.py:        except AttributeErrro:\n```\nSeparate ticket?",
    "created_at": "2009-08-11T22:41:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6732#issuecomment-55094",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_6732-spell-check-server.patch](tarball://root/attachments/some-uuid/ticket6732/trac_6732-spell-check-server.patch) by @qed777 created at 2009-08-11 22:41:34

```
$ cd $SAGE_ROOT/devel/sage/sage/server/notebook; grep rrr *.py
./notebook.py:        except AttributeErrro:
```
Separate ticket?



---

archive/issue_comments_055095.json:
```json
{
    "body": "Replying to [comment:2 mpatel]:\n> {{{\n> $ cd $SAGE_ROOT/devel/sage/sage/server/notebook; grep rrr *.py\n> ./notebook.py:        except AttributeErrro:\n> }}}\n> Separate ticket?\n\nNice catch. Can you please open a ticket for that? Here's a relevant snippet from the file `sage/server/notebook/notebook.py`:\n\n```\ntry:\n    dir = self.__absdir\nexcept AttributeErrro:\n    dir = self.__dir\nimport shutil\n# We ignore_errors because in rare parallel doctesting                  \n# situations sometimes the directory gets cleaned up too                \n# quickly, etc.                                                         \nshutil.rmtree(dir, ignore_errors=True)\n```\nAs I see it, this is a case where only some of the execution paths of the above code have been doctested. One should endeavour to test all the execution paths of a function. In particular, doctest the case where the try block is successfully executed. And also the case where the try block fails so that the flow of control then jumps to the except block, in which case the Python interpreter would complain about syntax errors. It would be nice to have some sort of static code analysis tool for Sage, something that would catch errors that would be reported by a compiler of a statically typed language such as C/C++, Java. See Dough Hellmann's [article](http://www.doughellmann.com/articles/CompletelyDifferent-2008-03-linters/index.html) for some inspiration on this issue.",
    "created_at": "2009-08-11T23:02:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6732#issuecomment-55095",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:2 mpatel]:
> {{{
> $ cd $SAGE_ROOT/devel/sage/sage/server/notebook; grep rrr *.py
> ./notebook.py:        except AttributeErrro:
> }}}
> Separate ticket?

Nice catch. Can you please open a ticket for that? Here's a relevant snippet from the file `sage/server/notebook/notebook.py`:

```
try:
    dir = self.__absdir
except AttributeErrro:
    dir = self.__dir
import shutil
# We ignore_errors because in rare parallel doctesting                  
# situations sometimes the directory gets cleaned up too                
# quickly, etc.                                                         
shutil.rmtree(dir, ignore_errors=True)
```
As I see it, this is a case where only some of the execution paths of the above code have been doctested. One should endeavour to test all the execution paths of a function. In particular, doctest the case where the try block is successfully executed. And also the case where the try block fails so that the flow of control then jumps to the except block, in which case the Python interpreter would complain about syntax errors. It would be nice to have some sort of static code analysis tool for Sage, something that would catch errors that would be reported by a compiler of a statically typed language such as C/C++, Java. See Dough Hellmann's [article](http://www.doughellmann.com/articles/CompletelyDifferent-2008-03-linters/index.html) for some inspiration on this issue.



---

archive/issue_comments_055096.json:
```json
{
    "body": "Note: I haven't checked that these are the only spelling errors.\n\nI think the \"winner\" here is `fludded`.",
    "created_at": "2009-08-13T01:03:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6732#issuecomment-55096",
    "user": "https://github.com/qed777"
}
```

Note: I haven't checked that these are the only spelling errors.

I think the "winner" here is `fludded`.



---

archive/issue_comments_055097.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-13T07:59:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6732#issuecomment-55097",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_015883.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-08-13T07:59:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6732",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6732#event-15883"
}
```



---

archive/issue_comments_055098.json:
```json
{
    "body": "Replying to [comment:4 mpatel]:\n> Note: I haven't checked that these are the only spelling errors.\n\nGiven that I spell-checked all the modules in the Sage library in 3 days, I mostly used a spell checker (in particular, aspell) to do most of the hard work. Occasionally I did read some snippets from library files. The time constraint did not allow me to actually read through all the library files. That would catch many more typos, but would also require substantially more time than what has been allocated for the current release. The release of Sage 4.1.1 has been delayed for far too long now. Originally it was planned to be released on the 01st August 2009, but it has dragged on for over a week now, in part due to #6645 and some unexpected issues that needed to be sorted out.",
    "created_at": "2009-08-13T07:59:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6732",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6732#issuecomment-55098",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:4 mpatel]:
> Note: I haven't checked that these are the only spelling errors.

Given that I spell-checked all the modules in the Sage library in 3 days, I mostly used a spell checker (in particular, aspell) to do most of the hard work. Occasionally I did read some snippets from library files. The time constraint did not allow me to actually read through all the library files. That would catch many more typos, but would also require substantially more time than what has been allocated for the current release. The release of Sage 4.1.1 has been delayed for far too long now. Originally it was planned to be released on the 01st August 2009, but it has dragged on for over a week now, in part due to #6645 and some unexpected issues that needed to be sorted out.
