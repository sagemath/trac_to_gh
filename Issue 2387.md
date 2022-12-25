# Issue 2387: Create a _sage_init_ function for all objects

archive/issues_002387.json:
```json
{
    "body": "Assignee: @williamstein\n\nCreate a _sage_init_ function that behaves like the _maxima_init_, _magma_init_, etc., functions which returns a string sufficient to construct the given object in Sage.\n\nFor example:\n\n\n```\nsage: a=matrix([[1,2,3],[4,5,6],[7,8,9]])\nsage: a._sage_init_\n'matrix([[1,2,3],[4,5,6],[7,8,9]])'\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2387\n\n",
    "created_at": "2008-03-04T20:45:45Z",
    "labels": [
        "component: interfaces"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Create a _sage_init_ function for all objects",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2387",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @williamstein

Create a _sage_init_ function that behaves like the _maxima_init_, _magma_init_, etc., functions which returns a string sufficient to construct the given object in Sage.

For example:


```
sage: a=matrix([[1,2,3],[4,5,6],[7,8,9]])
sage: a._sage_init_
'matrix([[1,2,3],[4,5,6],[7,8,9]])'
```



Issue created by migration from https://trac.sagemath.org/ticket/2387





---

archive/issue_comments_016075.json:
```json
{
    "body": "I've posted a stab at it by searching for _magma_init_ functions and implementing _sage_init_ next to it for most cases.\n\nHow should we deal with:\n\n\n```\nsage: R.<y>=ZZ[]                                           \nsage: a=matrix(R, [[y,1],[1,y^2]])                         \nsage: a._sage_init_()                                      \n\"matrix(PolynomialRing(ZZ, 'y'), [[y, 1], [1, y^2]])\"\n```\n\n\nThe string returned will not construct the object usually since y is not a variable in a new session.  However, putting in the parent of y would make things much uglier.  How would you handle this situation?",
    "created_at": "2008-03-05T19:07:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2387#issuecomment-16075",
    "user": "https://github.com/jasongrout"
}
```

I've posted a stab at it by searching for _magma_init_ functions and implementing _sage_init_ next to it for most cases.

How should we deal with:


```
sage: R.<y>=ZZ[]                                           
sage: a=matrix(R, [[y,1],[1,y^2]])                         
sage: a._sage_init_()                                      
"matrix(PolynomialRing(ZZ, 'y'), [[y, 1], [1, y^2]])"
```


The string returned will not construct the object usually since y is not a variable in a new session.  However, putting in the parent of y would make things much uglier.  How would you handle this situation?



---

archive/issue_comments_016076.json:
```json
{
    "body": "Attachment [sage_init.patch](tarball://root/attachments/some-uuid/ticket2387/sage_init.patch) by @jasongrout created at 2008-03-05 19:09:40\n\nAlso, there aren't any doctests...I'll be adding those.  If anyone wants to comment on something I did, please do so!  I'm not very familiar with the coercion system and did the above mainly by searching for _magma_init_ and copying where it made sense.",
    "created_at": "2008-03-05T19:09:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2387#issuecomment-16076",
    "user": "https://github.com/jasongrout"
}
```

Attachment [sage_init.patch](tarball://root/attachments/some-uuid/ticket2387/sage_init.patch) by @jasongrout created at 2008-03-05 19:09:40

Also, there aren't any doctests...I'll be adding those.  If anyone wants to comment on something I did, please do so!  I'm not very familiar with the coercion system and did the above mainly by searching for _magma_init_ and copying where it made sense.



---

archive/issue_comments_016077.json:
```json
{
    "body": "> However, putting in the parent of y would make things much \n> uglier. How would you handle this situation?\n\nI don't think it is possible without changing _sage_init_'s protocol\nas suggested by carl witty (either allow a sequence of semicolon separated statements or have two blocks, an initialization block and a eval block).  I think I prefer the latter solution, since it can be used to do the former and more, but not conversely.",
    "created_at": "2008-03-05T23:12:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2387#issuecomment-16077",
    "user": "https://github.com/williamstein"
}
```

> However, putting in the parent of y would make things much 
> uglier. How would you handle this situation?

I don't think it is possible without changing _sage_init_'s protocol
as suggested by carl witty (either allow a sequence of semicolon separated statements or have two blocks, an initialization block and a eval block).  I think I prefer the latter solution, since it can be used to do the former and more, but not conversely.



---

archive/issue_comments_016078.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_wstein\".",
    "created_at": "2008-06-20T04:44:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2387#issuecomment-16078",
    "user": "https://github.com/craigcitro"
}
```

Changing keywords from "" to "editor_wstein".



---

archive/issue_comments_016079.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2008-08-25T19:34:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2387#issuecomment-16079",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: wontfix



---

archive/issue_comments_016080.json:
```json
{
    "body": "Closed as wontfix due to #3484 and #3485.\n\n```\n[12:29pm] jason-: mabshoff_, cwitty: I believe that 3484 and 3485 make 2387 obsolete.  Comments?\n[12:29pm] mabshoff_: let me check\n[12:29pm] jason-: (it's the sage_input stuff; I made a simple sage_init patch a long time ago)\n[12:30pm] cwitty: I agree.\n[12:30pm] mabshoff_: Ok, let's close it as \"wontfix\" then.\n[12:30pm] mabshoff_: objections?\n[12:30pm] You are now known as mabshoff.\n[12:31pm] jason-: hehe, *another* ticket that is < 0.61*(current ticket number) down!\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-08-25T19:34:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2387",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2387#issuecomment-16080",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Closed as wontfix due to #3484 and #3485.

```
[12:29pm] jason-: mabshoff_, cwitty: I believe that 3484 and 3485 make 2387 obsolete.  Comments?
[12:29pm] mabshoff_: let me check
[12:29pm] jason-: (it's the sage_input stuff; I made a simple sage_init patch a long time ago)
[12:30pm] cwitty: I agree.
[12:30pm] mabshoff_: Ok, let's close it as "wontfix" then.
[12:30pm] mabshoff_: objections?
[12:30pm] You are now known as mabshoff.
[12:31pm] jason-: hehe, *another* ticket that is < 0.61*(current ticket number) down!
```


Cheers,

Michael



---

archive/issue_events_002563.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-25T19:34:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2387",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2387#event-2563"
}
```
