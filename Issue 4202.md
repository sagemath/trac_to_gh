# Issue 4202: latex derivatives of symbolic functions nicely

archive/issues_004202.json:
```json
{
    "body": "Assignee: @burcin\n\nThis patch makes it so that symbolic functions attempt to call maxima to get a latex representation before printing out the default functionname(arguments) notation.\n\n\nHere is some Sage code that did derivative printing.  I post it here since this code tries to intelligently print partials versus total derivatives, while maxima's seems to only print total derivative \"d\"s.  If there is interest, we can include this as part of the _latex_ function.\n\n```\n        if self._f._name == 'diff':\n            if len(self._args[0].variables())==1:\n                d_latex = \"d\"\n            else:\n                d_latex = \"\\\\partial\"\n\n            variables = [(self._args[2*i+1]._latex_(), self._args[2*i+2]) \n                         for i in xrange((len(self._args)-1)/2)]\n            variables_latex = ''.join([d_latex+var if power==1 else d_latex+var+\"^%r\"%power\n                                       for var,power in variables])\n\n\n            order = sum([power for var,power in variables])\n            if order == 1:\n                order_latex = \"\"\n            else:\n                order_latex = \"^%r\"%order\n        \n            return \"\\\\frac{%s%s}{%s}(%s)\"%(d_latex,\n                                              order_latex,\n                                              variables_latex,\n                                              self._args[0]._latex_())\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4202\n\n",
    "created_at": "2008-09-26T21:41:59Z",
    "labels": [
        "component: calculus"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "latex derivatives of symbolic functions nicely",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4202",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @burcin

This patch makes it so that symbolic functions attempt to call maxima to get a latex representation before printing out the default functionname(arguments) notation.


Here is some Sage code that did derivative printing.  I post it here since this code tries to intelligently print partials versus total derivatives, while maxima's seems to only print total derivative "d"s.  If there is interest, we can include this as part of the _latex_ function.

```
        if self._f._name == 'diff':
            if len(self._args[0].variables())==1:
                d_latex = "d"
            else:
                d_latex = "\\partial"

            variables = [(self._args[2*i+1]._latex_(), self._args[2*i+2]) 
                         for i in xrange((len(self._args)-1)/2)]
            variables_latex = ''.join([d_latex+var if power==1 else d_latex+var+"^%r"%power
                                       for var,power in variables])


            order = sum([power for var,power in variables])
            if order == 1:
                order_latex = ""
            else:
                order_latex = "^%r"%order
        
            return "\\frac{%s%s}{%s}(%s)"%(d_latex,
                                              order_latex,
                                              variables_latex,
                                              self._args[0]._latex_())
```



Issue created by migration from https://trac.sagemath.org/ticket/4202





---

archive/issue_comments_030437.json:
```json
{
    "body": "Attachment [diff-latex.patch](tarball://root/attachments/some-uuid/ticket4202/diff-latex.patch) by @mwhansen created at 2008-09-26 21:53:05\n\nNice job.  Looks good to me.",
    "created_at": "2008-09-26T21:53:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4202",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4202#issuecomment-30437",
    "user": "https://github.com/mwhansen"
}
```

Attachment [diff-latex.patch](tarball://root/attachments/some-uuid/ticket4202/diff-latex.patch) by @mwhansen created at 2008-09-26 21:53:05

Nice job.  Looks good to me.



---

archive/issue_events_009521.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-27T00:53:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4202",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4202#event-9521"
}
```



---

archive/issue_comments_030438.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-27T00:53:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4202",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4202#issuecomment-30438",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030439.json:
```json
{
    "body": "Merged in Sage 3.1.3.alpha2",
    "created_at": "2008-09-27T00:53:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4202",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4202#issuecomment-30439",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.3.alpha2
