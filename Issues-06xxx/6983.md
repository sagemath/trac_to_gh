# Issue 6983: completely separate the sage notebook from the core sage library as a new spkg called "sagenb-4.1.2.spkg"

archive/issues_006983.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @qed777\n\nI'm posting releases here:\n\nhttp://sage.math.washington.edu/home/wstein/patches/sagenb/\n\nTry it now online: http://uw.sagenb.org\n\nSuggested steps for trying out the new notebook:\n\n* Download the latest archive from [the URL above](http://sage.math.washington.edu/home/wstein/patches/sagenb/).\n* `tar zxvf sagenb-X.Y.tar.gz`\n* `cd sagenb-X.Y`\n* `sage -hg pull http://sage.math.washington.edu:8100/`\n* `sage -hg update`\n* `sage -python setup.py install`\n* `cd ..`\n* `sage`\n* `sage: import sagenb.notebook.notebook_object as nb`\n* `sage: nb.notebook()`\n\nSee the enclosed `README.txt` for more details.  Please feel free to ask questions on [#sage-devel](http://webchat.freenode.net/?channels=sage-devel) or on [sage-notebook](http://groups.google.com/group/sage-notebook).  See [this wiki page](http://wiki.sagemath.org/SageNotebook) for an overview of the new server infrastructure.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6983\n\n",
    "closed_at": "2009-10-24T07:12:28Z",
    "created_at": "2009-09-22T05:38:58Z",
    "labels": [
        "component: notebook"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "completely separate the sage notebook from the core sage library as a new spkg called \"sagenb-4.1.2.spkg\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6983",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

CC:  @qed777

I'm posting releases here:

http://sage.math.washington.edu/home/wstein/patches/sagenb/

Try it now online: http://uw.sagenb.org

Suggested steps for trying out the new notebook:

* Download the latest archive from [the URL above](http://sage.math.washington.edu/home/wstein/patches/sagenb/).
* `tar zxvf sagenb-X.Y.tar.gz`
* `cd sagenb-X.Y`
* `sage -hg pull http://sage.math.washington.edu:8100/`
* `sage -hg update`
* `sage -python setup.py install`
* `cd ..`
* `sage`
* `sage: import sagenb.notebook.notebook_object as nb`
* `sage: nb.notebook()`

See the enclosed `README.txt` for more details.  Please feel free to ask questions on [#sage-devel](http://webchat.freenode.net/?channels=sage-devel) or on [sage-notebook](http://groups.google.com/group/sage-notebook).  See [this wiki page](http://wiki.sagemath.org/SageNotebook) for an overview of the new server infrastructure.

Issue created by migration from https://trac.sagemath.org/ticket/6983





---

archive/issue_comments_057647.json:
```json
{
    "body": "[New Sage Notebook home page](http://nb.sagemath.org/).",
    "created_at": "2009-10-12T18:47:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6983#issuecomment-57647",
    "user": "https://github.com/qed777"
}
```

[New Sage Notebook home page](http://nb.sagemath.org/).



---

archive/issue_comments_057648.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-24T07:12:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6983#issuecomment-57648",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_016400.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-10-24T07:12:28Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6983",
    "milestone": "sage-4.1.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6983#event-16400"
}
```



---

archive/issue_events_016401.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-10-24T07:12:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6983",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6983#event-16401"
}
```



---

archive/issue_comments_057649.json:
```json
{
    "body": "This was actually done in sage-4.1.2.",
    "created_at": "2009-10-24T07:12:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6983",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6983#issuecomment-57649",
    "user": "https://github.com/williamstein"
}
```

This was actually done in sage-4.1.2.
