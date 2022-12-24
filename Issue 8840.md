# Issue 8840: about  CSRF attacks

archive/issues_008840.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  chapoton\n\nsage contain Multiple cross site reference vulnerability\nbecause authority does not checked before preforming an action\n\n**CSRF attacks explain:**\nIf create a file on my domain called \"blah.jpg\". It's really a php file, renamed.\nThe PHP file redirects you back to the referring host (or any host I want to really), to a special URL.\nThat URL takes an action based on the submitted data.\nI then use an img  tag <img> to link to my \"image\" on your site.\n\nWhen you view the page, your browser makes a request to that image, and that request is then redirected to the page on your site. Your browser won't display the image (or will display a broken image) but that's not important. What's important is that you just executed an action without knowing it.\n\nSome examples of  CSRF attacks in sage :\n\n1) upload a worksheet\n2) create worksheet\n3) change email \n4) .............\n...........\n.............\n...........\n\n\n**example:**\n1- login in at\nhttp://alpha.sagenb.org/\n\n2- open this published worksheet\nhttp://alpha.sagenb.org/home/pub/16/\n\n3-go to your home you will see that I uploaded a worksheet to your account .\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8840\n\n",
    "created_at": "2010-05-02T00:17:50Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "about  CSRF attacks",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8840",
    "user": "aliajouz"
}
```
Assignee: jason, was

CC:  chapoton

sage contain Multiple cross site reference vulnerability
because authority does not checked before preforming an action

**CSRF attacks explain:**
If create a file on my domain called "blah.jpg". It's really a php file, renamed.
The PHP file redirects you back to the referring host (or any host I want to really), to a special URL.
That URL takes an action based on the submitted data.
I then use an img  tag <img> to link to my "image" on your site.

When you view the page, your browser makes a request to that image, and that request is then redirected to the page on your site. Your browser won't display the image (or will display a broken image) but that's not important. What's important is that you just executed an action without knowing it.

Some examples of  CSRF attacks in sage :

1) upload a worksheet
2) create worksheet
3) change email 
4) .............
...........
.............
...........


**example:**
1- login in at
http://alpha.sagenb.org/

2- open this published worksheet
http://alpha.sagenb.org/home/pub/16/

3-go to your home you will see that I uploaded a worksheet to your account .




Issue created by migration from https://trac.sagemath.org/ticket/8840





---

archive/issue_comments_081278.json:
```json
{
    "body": "Changing assignee from jason, was to aliajouz.",
    "created_at": "2010-05-02T00:18:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8840#issuecomment-81278",
    "user": "aliajouz"
}
```

Changing assignee from jason, was to aliajouz.



---

archive/issue_comments_081279.json:
```json
{
    "body": "This is probably a big reason why public worksheets are currently disabled...\n\nhttps://github.com/sagemath/sagenb/issues/319",
    "created_at": "2014-12-19T04:43:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8840#issuecomment-81279",
    "user": "kcrisman"
}
```

This is probably a big reason why public worksheets are currently disabled...

https://github.com/sagemath/sagenb/issues/319



---

archive/issue_comments_081280.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-08-18T00:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8840#issuecomment-81280",
    "user": "mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081281.json:
```json
{
    "body": "Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.",
    "created_at": "2020-08-18T00:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8840#issuecomment-81281",
    "user": "mkoeppe"
}
```

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.



---

archive/issue_comments_081282.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-09-08T17:59:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8840",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8840#issuecomment-81282",
    "user": "chapoton"
}
```

Resolution: invalid
