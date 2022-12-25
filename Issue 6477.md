# Issue 6477: notebook -- improve UNICODE handling of truncated_name function in worksheet.py

archive/issues_006477.json:
```json
{
    "body": "Assignee: boothby\n\n\n```\nHello.\n\nI use Sagemath to show the Linear Algebra problems solution.\n\nAnd I am Korean.\n\nTherefore I write the title in Korean.\n```\n\n\nhttp://nosyu.pe.kr/attach/1/5682987737.png\n\n\n```\nBut in worksheet,  the title is broken because of truncated_name\nfunction in worksheet.py.\n\n\ndef truncated_name(self, max=30):\n       name = self.name()\n       if len(name) > max:\n           name = name[:max] + ' ...'\n       return name\n\n\nBut Unicode is not 1 byte by character.\n\nSo Korean is broken if max is midpoint of Korean one character.\n\nTherefore I modify the function code like this.\n\n\ndef truncated_name(self, max=30):\n       name = unicode(self.name(), \"utf-8\") # name = self.name()\n       if len(name) > max:\n           name = name[:max] + ' ...'\n       return name.encode('utf-8') # return name\n\n\nNow name is encoded by unicode, then Korean one character's length is\n1, not 2 or 3.\n\nSo I can see the right title.\n\n\nI think there are more good choice to solve the problem.\nBecause I don't know about Python well and unicode also.\nSo I suggest this.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6477\n\n",
    "created_at": "2009-07-08T01:43:54Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "notebook -- improve UNICODE handling of truncated_name function in worksheet.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6477",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby


```
Hello.

I use Sagemath to show the Linear Algebra problems solution.

And I am Korean.

Therefore I write the title in Korean.
```


http://nosyu.pe.kr/attach/1/5682987737.png


```
But in worksheet,  the title is broken because of truncated_name
function in worksheet.py.


def truncated_name(self, max=30):
       name = self.name()
       if len(name) > max:
           name = name[:max] + ' ...'
       return name


But Unicode is not 1 byte by character.

So Korean is broken if max is midpoint of Korean one character.

Therefore I modify the function code like this.


def truncated_name(self, max=30):
       name = unicode(self.name(), "utf-8") # name = self.name()
       if len(name) > max:
           name = name[:max] + ' ...'
       return name.encode('utf-8') # return name


Now name is encoded by unicode, then Korean one character's length is
1, not 2 or 3.

So I can see the right title.


I think there are more good choice to solve the problem.
Because I don't know about Python well and unicode also.
So I suggest this.
```


Issue created by migration from https://trac.sagemath.org/ticket/6477





---

archive/issue_comments_052263.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-01-19T07:24:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6477#issuecomment-52263",
    "user": "https://github.com/TimDumol"
}
```

Resolution: duplicate



---

archive/issue_events_006714.json:
```json
{
    "actor": "https://github.com/TimDumol",
    "created_at": "2010-01-19T07:24:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6477",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6477#event-6714"
}
```



---

archive/issue_comments_052264.json:
```json
{
    "body": "I'll mark this as a duplicate since #7249 subsumes this.",
    "created_at": "2010-01-19T07:24:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6477",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6477#issuecomment-52264",
    "user": "https://github.com/TimDumol"
}
```

I'll mark this as a duplicate since #7249 subsumes this.
