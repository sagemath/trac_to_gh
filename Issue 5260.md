# Issue 5260: document the requirement for a compiler better for f2py/weave/ctypes and error out with a sensible error message when no compiler is present

archive/issues_005260.json:
```json
{
    "body": "Assignee: cwitty\n\nThis is motivated by http://groups.google.com/group/sage-devel/browse_thread/thread/ef0eecd9f3473215\n\n```\nHi everyone, \nbeing a new Sage user under Mac OS X, I spent a whole day trying to \nget the examples for using compiled code from \nhttp://www.math.washington.edu/~jkantor/Numerical_Sage/node10.html to \nwork. Trying to make sense of the error messages and googling for \nfixes, I did not realise the most simple explanation - until I ran \n\"which gcc\" in the terminal and got no result. I simply didn't have \ngcc installed! Unless I'm blind, there is no hint to check if gcc is \ninstalled in an obvious place on website or in the documentation. Of \ncourse, the problem was fixed easily by installing XcodeTools. \nI think it would be very helpful for new users to have a remark in the \nreadme or on the download page, that sage does not include gcc, but \nrequires it for certain features. Maybe this is so obvious, that \nnobody thought of it before. \nOtherwise, Sage seems to be a great piece of Software, keep on the \ngreat Work \nFelix \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5260\n\n",
    "created_at": "2009-02-13T22:14:35Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "document the requirement for a compiler better for f2py/weave/ctypes and error out with a sensible error message when no compiler is present",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5260",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: cwitty

This is motivated by http://groups.google.com/group/sage-devel/browse_thread/thread/ef0eecd9f3473215

```
Hi everyone, 
being a new Sage user under Mac OS X, I spent a whole day trying to 
get the examples for using compiled code from 
http://www.math.washington.edu/~jkantor/Numerical_Sage/node10.html to 
work. Trying to make sense of the error messages and googling for 
fixes, I did not realise the most simple explanation - until I ran 
"which gcc" in the terminal and got no result. I simply didn't have 
gcc installed! Unless I'm blind, there is no hint to check if gcc is 
installed in an obvious place on website or in the documentation. Of 
course, the problem was fixed easily by installing XcodeTools. 
I think it would be very helpful for new users to have a remark in the 
readme or on the download page, that sage does not include gcc, but 
requires it for certain features. Maybe this is so obvious, that 
nobody thought of it before. 
Otherwise, Sage seems to be a great piece of Software, keep on the 
great Work 
Felix 
```


Issue created by migration from https://trac.sagemath.org/ticket/5260





---

archive/issue_comments_040292.json:
```json
{
    "body": "Changing component from misc to documentation.",
    "created_at": "2009-02-13T22:30:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5260#issuecomment-40292",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing component from misc to documentation.



---

archive/issue_comments_040293.json:
```json
{
    "body": "D'oh, this is probably better assigned to component \"documentation\".\n\nCheers,\n\nMichael",
    "created_at": "2009-02-13T22:30:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5260#issuecomment-40293",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

D'oh, this is probably better assigned to component "documentation".

Cheers,

Michael



---

archive/issue_comments_040294.json:
```json
{
    "body": "Changing assignee from cwitty to tba.",
    "created_at": "2009-02-13T22:30:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5260#issuecomment-40294",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing assignee from cwitty to tba.



---

archive/issue_comments_040295.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-09-07T19:05:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5260#issuecomment-40295",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_040296.json:
```json
{
    "body": "`gcc` is included with Sage now.",
    "created_at": "2015-09-07T19:05:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5260#issuecomment-40296",
    "user": "https://github.com/jdemeyer"
}
```

`gcc` is included with Sage now.



---

archive/issue_comments_040297.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-09-07T19:06:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5260#issuecomment-40297",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_040298.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-09-12T13:57:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5260#issuecomment-40298",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
