# Issue 6555: Twisted produces deprecation warning about using md5 module in Python 2.6

archive/issues_006555.json:
```json
{
    "body": "Assignee: boothby\n\nWhen I start up the notebook in 4.1, I get:\n\n\n```\nsage: notebook()\nThe notebook files are stored in: /home/grout/.sage//sage_notebook\n**************************************************\n*                                                *\n* Open your web browser to http://localhost:8000 *\n*                                                *\n**************************************************\n/home/grout/sage/local/lib/python2.6/site-packages/twisted/persisted/sob.py:12: DeprecationWarning: the md5 module is deprecated; use hashlib instead\n  import os, md5, sys\n```\n\n\n\nIt looks like this was fixed a while ago in twisted: http://twistedmatrix.com/trac/ticket/2763\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6555\n\n",
    "created_at": "2009-07-18T19:27:35Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Twisted produces deprecation warning about using md5 module in Python 2.6",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6555",
    "user": "https://github.com/jasongrout"
}
```
Assignee: boothby

When I start up the notebook in 4.1, I get:


```
sage: notebook()
The notebook files are stored in: /home/grout/.sage//sage_notebook
**************************************************
*                                                *
* Open your web browser to http://localhost:8000 *
*                                                *
**************************************************
/home/grout/sage/local/lib/python2.6/site-packages/twisted/persisted/sob.py:12: DeprecationWarning: the md5 module is deprecated; use hashlib instead
  import os, md5, sys
```



It looks like this was fixed a while ago in twisted: http://twistedmatrix.com/trac/ticket/2763



Issue created by migration from https://trac.sagemath.org/ticket/6555





---

archive/issue_comments_053357.json:
```json
{
    "body": "It also appears that there is other work for them to be compatible with Python 2.6: http://twistedmatrix.com/trac/query?status=new&status=assigned&status=reopened&milestone=Python-2.6",
    "created_at": "2009-07-18T19:30:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6555#issuecomment-53357",
    "user": "https://github.com/jasongrout"
}
```

It also appears that there is other work for them to be compatible with Python 2.6: http://twistedmatrix.com/trac/query?status=new&status=assigned&status=reopened&milestone=Python-2.6



---

archive/issue_events_006792.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-14T08:50:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6555",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6555#event-6792"
}
```



---

archive/issue_comments_053358.json:
```json
{
    "body": "This was fixed by #6676.",
    "created_at": "2009-11-14T08:50:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6555#issuecomment-53358",
    "user": "https://github.com/mwhansen"
}
```

This was fixed by #6676.



---

archive/issue_comments_053359.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-11-14T08:50:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6555",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6555#issuecomment-53359",
    "user": "https://github.com/mwhansen"
}
```

Resolution: duplicate
