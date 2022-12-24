# Issue 3624: cookbook documentation chapter: coding theory

archive/issues_003624.json:
```json
{
    "body": "Assignee: tba\n\nI've put a draft for the coding theory chapter for the cookbook.tex document in \nhttp://sage.math.washington.edu/home/wdj/cookbook/\nTo possibly make it easier, I've created this tarball of the directory:\nhttp://sage.math.washington.edu/home/wdj/cookbook2008-07-09.tar.gz\n\nIssue created by migration from https://trac.sagemath.org/ticket/3624\n\n",
    "created_at": "2008-07-09T12:59:24Z",
    "labels": [
        "documentation",
        "minor",
        "enhancement"
    ],
    "title": "cookbook documentation chapter: coding theory",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3624",
    "user": "wdj"
}
```
Assignee: tba

I've put a draft for the coding theory chapter for the cookbook.tex document in 
http://sage.math.washington.edu/home/wdj/cookbook/
To possibly make it easier, I've created this tarball of the directory:
http://sage.math.washington.edu/home/wdj/cookbook2008-07-09.tar.gz

Issue created by migration from https://trac.sagemath.org/ticket/3624





---

archive/issue_comments_025634.json:
```json
{
    "body": "This is unrelated to coercion and should not be assigned against the coercion milestone. Right now 3.0.6 is the default milestone, so please assign new tickets against that milestone.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-10T13:23:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3624#issuecomment-25634",
    "user": "mabshoff"
}
```

This is unrelated to coercion and should not be assigned against the coercion milestone. Right now 3.0.6 is the default milestone, so please assign new tickets against that milestone.

Cheers,

Michael



---

archive/issue_comments_025635.json:
```json
{
    "body": "Is this TeX code stand alone or is there a patch in there somewhere for the new cookbook? If so we should create the cookbook and migrate chapter by chapter over from the old construction manual. Once that is done we remove const.tex and all the other bits related to it.\n\nCheers,\n\nMichael",
    "created_at": "2008-07-10T13:24:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3624#issuecomment-25635",
    "user": "mabshoff"
}
```

Is this TeX code stand alone or is there a patch in there somewhere for the new cookbook? If so we should create the cookbook and migrate chapter by chapter over from the old construction manual. Once that is done we remove const.tex and all the other bits related to it.

Cheers,

Michael



---

archive/issue_comments_025636.json:
```json
{
    "body": "I put a standalone latex file there (http://sage.math.washington.edu/home/wdj/cookbook/coding-theory/sage-coding-cookbook.tex) for just that chapter (not in manual style) but also the full latex setup for a new subdirectory of SAGE_ROOT/devel/doc. I don't know how to make a patch to add a cookbook subdirectory to devel/doc. The programming guide discusses adding new files at http://sage.scipy.org/sage/doc/html/prog/node72.html The book http://hgbook.red-bean.com/hgbook.html is hard to search through since the index is for page numbers but the html is in sections, not page numbers.",
    "created_at": "2008-07-10T14:44:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3624#issuecomment-25636",
    "user": "wdj"
}
```

I put a standalone latex file there (http://sage.math.washington.edu/home/wdj/cookbook/coding-theory/sage-coding-cookbook.tex) for just that chapter (not in manual style) but also the full latex setup for a new subdirectory of SAGE_ROOT/devel/doc. I don't know how to make a patch to add a cookbook subdirectory to devel/doc. The programming guide discusses adding new files at http://sage.scipy.org/sage/doc/html/prog/node72.html The book http://hgbook.red-bean.com/hgbook.html is hard to search through since the index is for page numbers but the html is in sections, not page numbers.



---

archive/issue_comments_025637.json:
```json
{
    "body": "fixes typos in sage-coding-cookbook.tex",
    "created_at": "2008-10-29T11:22:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3624#issuecomment-25637",
    "user": "mvngu"
}
```

fixes typos in sage-coding-cookbook.tex



---

archive/issue_comments_025638.json:
```json
{
    "body": "Attachment [3624-doc.patch](tarball://root/attachments/some-uuid/ticket3624/3624-doc.patch) by mvngu created at 2008-10-29 11:28:07\n\nReplying to [comment:3 wdj]:\n> I put a standalone latex file there (http://sage.math.washington.edu/home/wdj/cookbook/coding-theory/sage-coding-cookbook.tex) for just that chapter (not in manual style) but also the full latex setup for a new subdirectory of SAGE_ROOT/devel/doc. \n\n\nI've attached a patch to your file [sage-coding-cookbook.tex](http://sage.math.washington.edu/home/wdj/cookbook/coding-theory/sage-coding-cookbook.tex). It mainly fixes typos. I'm still waiting for sage-3.1.4 to finish building on my machine, so at the moment I can't review the sample code in your file.",
    "created_at": "2008-10-29T11:28:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3624#issuecomment-25638",
    "user": "mvngu"
}
```

Attachment [3624-doc.patch](tarball://root/attachments/some-uuid/ticket3624/3624-doc.patch) by mvngu created at 2008-10-29 11:28:07

Replying to [comment:3 wdj]:
> I put a standalone latex file there (http://sage.math.washington.edu/home/wdj/cookbook/coding-theory/sage-coding-cookbook.tex) for just that chapter (not in manual style) but also the full latex setup for a new subdirectory of SAGE_ROOT/devel/doc. 


I've attached a patch to your file [sage-coding-cookbook.tex](http://sage.math.washington.edu/home/wdj/cookbook/coding-theory/sage-coding-cookbook.tex). It mainly fixes typos. I'm still waiting for sage-3.1.4 to finish building on my machine, so at the moment I can't review the sample code in your file.



---

archive/issue_comments_025639.json:
```json
{
    "body": "Ticket #8466 supersedes the current ticket.",
    "created_at": "2010-03-07T02:11:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3624#issuecomment-25639",
    "user": "mvngu"
}
```

Ticket #8466 supersedes the current ticket.



---

archive/issue_comments_025640.json:
```json
{
    "body": "I took the latest corrected version of the paper, converted it to ReST using pandoc, and fixed that document, including a few typos. I converted the EPS figures to PNG using inkscape. The file is included in the toctree and the general index under number theory because I didn't want a toplevel entry. Maybe replace number theory with discrete math?\n----\nNew commits:",
    "created_at": "2014-03-20T16:56:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3624#issuecomment-25640",
    "user": "rws"
}
```

I took the latest corrected version of the paper, converted it to ReST using pandoc, and fixed that document, including a few typos. I converted the EPS figures to PNG using inkscape. The file is included in the toctree and the general index under number theory because I didn't want a toplevel entry. Maybe replace number theory with discrete math?
----
New commits:



---

archive/issue_comments_025641.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-03-20T16:56:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3624#issuecomment-25641",
    "user": "rws"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_025642.json:
```json
{
    "body": "\n```\nsage -t --long src/doc/en/thematic_tutorials/coding_theory.rst\n    Error: TAB character found at lines 860,864,865,.,.,.,1064\n```\n\n\n\n```\n+Included in Sage is the group theory package GAP [GAP]_ and GUAVA [GUAVA]_, GA\nP\u2019s coding\n+theory package. All of GUAVA\u2019s functions can be accessed within Sage.\n+   (calling Steve Linton\u2019s C programs in GAP),\n+#. Boolean-valueTraceback (most recent call last):\n  File \"/home/ralf/sage/local/bin/patchbot/patchbot.py\", line 468, in test_a_ticket\n    res = plugin(ticket, is_git=True, baseline=baseline, **kwds)\n  File \"/home/ralf/git/sage-patchbot/src/plugins.py\", line 149, in non_ascii\n    exclude_new(ticket, regex=r'[^\\x00-\\x7F]', msg=\"Non-ascii characters\", **kwds)\n  File \"/home/ralf/git/sage-patchbot/src/plugins.py\", line 143, in exclude_new\n    raise ValueError(full_msg)\nValueError: Non-ascii characters inserted on 35 non-empty lines\n```\n",
    "created_at": "2014-05-08T07:06:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3624#issuecomment-25642",
    "user": "rws"
}
```


```
sage -t --long src/doc/en/thematic_tutorials/coding_theory.rst
    Error: TAB character found at lines 860,864,865,.,.,.,1064
```



```
+Included in Sage is the group theory package GAP [GAP]_ and GUAVA [GUAVA]_, GA
P’s coding
+theory package. All of GUAVA’s functions can be accessed within Sage.
+   (calling Steve Linton’s C programs in GAP),
+#. Boolean-valueTraceback (most recent call last):
  File "/home/ralf/sage/local/bin/patchbot/patchbot.py", line 468, in test_a_ticket
    res = plugin(ticket, is_git=True, baseline=baseline, **kwds)
  File "/home/ralf/git/sage-patchbot/src/plugins.py", line 149, in non_ascii
    exclude_new(ticket, regex=r'[^\x00-\x7F]', msg="Non-ascii characters", **kwds)
  File "/home/ralf/git/sage-patchbot/src/plugins.py", line 143, in exclude_new
    raise ValueError(full_msg)
ValueError: Non-ascii characters inserted on 35 non-empty lines
```




---

archive/issue_comments_025643.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2014-05-08T07:06:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3624#issuecomment-25643",
    "user": "rws"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_025644.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-05-13T07:14:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3624#issuecomment-25644",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_025645.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-05-13T07:15:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3624#issuecomment-25645",
    "user": "rws"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_025646.json:
```json
{
    "body": "Could you please rebase this on top of current release (and/or tell me how to do it)? This would be immensely helpful. \n\n/p/s/ This should be an easy review for me but I have forgotten how to rebase a branch on top of another.",
    "created_at": "2014-08-11T08:35:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3624#issuecomment-25646",
    "user": "knsam"
}
```

Could you please rebase this on top of current release (and/or tell me how to do it)? This would be immensely helpful. 

/p/s/ This should be an easy review for me but I have forgotten how to rebase a branch on top of another.



---

archive/issue_comments_025647.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-08-11T08:39:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3624#issuecomment-25647",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_025648.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-08-14T17:49:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3624#issuecomment-25648",
    "user": "knsam"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_025649.json:
```json
{
    "body": "I am setting this to Positive Review! Thank to the authors and editor for the great work on this branch!",
    "created_at": "2014-08-14T17:49:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3624#issuecomment-25649",
    "user": "knsam"
}
```

I am setting this to Positive Review! Thank to the authors and editor for the great work on this branch!



---

archive/issue_comments_025650.json:
```json
{
    "body": "Thanks for the review!",
    "created_at": "2014-08-14T17:52:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3624#issuecomment-25650",
    "user": "rws"
}
```

Thanks for the review!



---

archive/issue_comments_025651.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2014-08-15T07:35:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3624#issuecomment-25651",
    "user": "vbraun"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_025652.json:
```json
{
    "body": "PDF docs don't build\n\n```\nl.14519 \\end{gather}\n                    \n? \n! Emergency stop.\n\\math@cr@@@ ...@ \\@ne \\add@amps \\maxfields@ \\omit \n                                                  \\kern -\\alignsep@ \\iftag@ ...\nl.14519 \\end{gather}\n                    \n!  ==> Fatal error occurred, no output PDF file produced!\nTranscript written on thematic_tutorials.log.\n [23make[1]: *** [thematic_tutorials.pdf] Error 1\nmake[1]: Leaving directory `/home/release/Sage/src/doc/output/latex/en/thematic_tutorials'\n]\n```\n",
    "created_at": "2014-08-15T07:35:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3624#issuecomment-25652",
    "user": "vbraun"
}
```

PDF docs don't build

```
l.14519 \end{gather}
                    
? 
! Emergency stop.
\math@cr@@@ ...@ \@ne \add@amps \maxfields@ \omit 
                                                  \kern -\alignsep@ \iftag@ ...
l.14519 \end{gather}
                    
!  ==> Fatal error occurred, no output PDF file produced!
Transcript written on thematic_tutorials.log.
 [23make[1]: *** [thematic_tutorials.pdf] Error 1
make[1]: Leaving directory `/home/release/Sage/src/doc/output/latex/en/thematic_tutorials'
]
```




---

archive/issue_comments_025653.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-08-15T13:40:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3624#issuecomment-25653",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_025654.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2014-08-15T13:41:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3624#issuecomment-25654",
    "user": "rws"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_025655.json:
```json
{
    "body": "I really thought I had tested this.",
    "created_at": "2014-08-15T13:41:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3624#issuecomment-25655",
    "user": "rws"
}
```

I really thought I had tested this.



---

archive/issue_comments_025656.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-08-16T09:32:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3624#issuecomment-25656",
    "user": "vbraun"
}
```

Resolution: fixed
