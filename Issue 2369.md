# Issue 2369: clean up the Notebook HTML & CSS

archive/issues_002369.json:
```json
{
    "body": "Assignee: TimothyClemans\n\nCC:  @williamstein @jhpalmieri\n\nThis is critical to the success of the up-coming manipulate functionality.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2369\n\n",
    "created_at": "2008-03-02T17:16:05Z",
    "labels": [
        "component: notebook"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "clean up the Notebook HTML & CSS",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2369",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```
Assignee: TimothyClemans

CC:  @williamstein @jhpalmieri

This is critical to the success of the up-coming manipulate functionality.

Issue created by migration from https://trac.sagemath.org/ticket/2369





---

archive/issue_comments_015945.json:
```json
{
    "body": "> This is critical to the success of the up-coming manipulate functionality.\n\nThanks for caring about this issue so much.\n\nI don't think fixing this is critical to the success of manipulate.  I do appreciate your concern.  This ticket is pretty vague...",
    "created_at": "2008-03-02T17:21:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2369#issuecomment-15945",
    "user": "https://github.com/williamstein"
}
```

> This is critical to the success of the up-coming manipulate functionality.

Thanks for caring about this issue so much.

I don't think fixing this is critical to the success of manipulate.  I do appreciate your concern.  This ticket is pretty vague...



---

archive/issue_comments_015946.json:
```json
{
    "body": "I've had a lot of trouble writing HTML in the Notebook because of how the Notebook HTML & CSS are written. Looking at the output of running the HTML of a worksheet through the W3C Validator I noticed font tags are being used. Font tags are extremely bad for use in the Notebook because block level tags such as P, DIV, etc can't go inside them.",
    "created_at": "2008-03-02T17:36:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2369#issuecomment-15946",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

I've had a lot of trouble writing HTML in the Notebook because of how the Notebook HTML & CSS are written. Looking at the output of running the HTML of a worksheet through the W3C Validator I noticed font tags are being used. Font tags are extremely bad for use in the Notebook because block level tags such as P, DIV, etc can't go inside them.



---

archive/issue_comments_015947.json:
```json
{
    "body": "Timothy,\n\nas William pointed out the ticket you opened is vague and cannot really be solved. So I changed the summary to something more achievable and from your comment it is what you intend to do. Feel free to correct the \"Summary\" line.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-02T18:10:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2369#issuecomment-15947",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Timothy,

as William pointed out the ticket you opened is vague and cannot really be solved. So I changed the summary to something more achievable and from your comment it is what you intend to do. Feel free to correct the "Summary" line.

Cheers,

Michael



---

archive/issue_comments_015948.json:
```json
{
    "body": "This ticket is 22 months old and the notebook has changed in that time, but I think it is well worth fixing the W3C validation errors, for reasons that are not so obvious. \n\nWhen I look at the Wolfram Reserach site\n\nhttp://www.wolfram.com/\n\nand see 259 Errors, 4 warning(s)\n\nhttp://validator.w3.org/check?uri=http%3A%2F%2Fwww.wolfram.com&charset=%28detect+automatically%29&doctype=Inline&group=0&user-agent=W3C_Validator%2F1.654\n\n\nit gives me the impression of not taking care of details. Wolfram Reserach could reasonably argue they would rather devote time to improving Mathematica, than fixing the web site. One can see some logic to that. But I personally still see this as not paying attention to detail. \n\nIn contrast, the Sage web \n\nsite has few if any issues with the W3C validator. The home page is faultless in this respect \n\nhttp://validator.w3.org/check?uri=http%3A%2F%2Fwww.sagemath.org%2F&charset=%28detect+automatically%29&doctype=Inline&group=0\n\nAs such, even if the notebook looks fine, I believe the errors should be removed, to give the impression that attention is paid to detail. \n\nA google search on 'W3C validator' shows 2,230,000 hits. It is obvious people do use that tool. \n\nDave",
    "created_at": "2009-12-25T17:44:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2369#issuecomment-15948",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

This ticket is 22 months old and the notebook has changed in that time, but I think it is well worth fixing the W3C validation errors, for reasons that are not so obvious. 

When I look at the Wolfram Reserach site

http://www.wolfram.com/

and see 259 Errors, 4 warning(s)

http://validator.w3.org/check?uri=http%3A%2F%2Fwww.wolfram.com&charset=%28detect+automatically%29&doctype=Inline&group=0&user-agent=W3C_Validator%2F1.654


it gives me the impression of not taking care of details. Wolfram Reserach could reasonably argue they would rather devote time to improving Mathematica, than fixing the web site. One can see some logic to that. But I personally still see this as not paying attention to detail. 

In contrast, the Sage web 

site has few if any issues with the W3C validator. The home page is faultless in this respect 

http://validator.w3.org/check?uri=http%3A%2F%2Fwww.sagemath.org%2F&charset=%28detect+automatically%29&doctype=Inline&group=0

As such, even if the notebook looks fine, I believe the errors should be removed, to give the impression that attention is paid to detail. 

A google search on 'W3C validator' shows 2,230,000 hits. It is obvious people do use that tool. 

Dave



---

archive/issue_comments_015949.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2014-09-17T19:04:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2369#issuecomment-15949",
    "user": "https://github.com/kcrisman"
}
```

Changing priority from major to minor.



---

archive/issue_comments_015950.json:
```json
{
    "body": "Upstream at https://github.com/sagemath/sagenb/issues/232.  Certainly this is worth doing, though I would argue much lower priority than some other things.",
    "created_at": "2014-09-17T19:04:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2369#issuecomment-15950",
    "user": "https://github.com/kcrisman"
}
```

Upstream at https://github.com/sagemath/sagenb/issues/232.  Certainly this is worth doing, though I would argue much lower priority than some other things.



---

archive/issue_comments_015951.json:
```json
{
    "body": "old ticket about deprecated sagenb. Can we close ?",
    "created_at": "2020-03-28T10:03:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2369#issuecomment-15951",
    "user": "https://github.com/fchapoton"
}
```

old ticket about deprecated sagenb. Can we close ?



---

archive/issue_comments_015952.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-03-28T10:47:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2369#issuecomment-15952",
    "user": "https://github.com/fchapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_015953.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-03-28T14:32:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2369#issuecomment-15953",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_015954.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-03-28T15:22:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2369#issuecomment-15954",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid



---

archive/issue_events_002546.json:
```json
{
    "actor": "@fchapoton",
    "created_at": "2020-03-28T15:22:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2369",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2369#event-2546"
}
```



---

archive/issue_comments_015955.json:
```json
{
    "body": "thx",
    "created_at": "2020-03-28T15:22:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2369",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2369#issuecomment-15955",
    "user": "https://github.com/fchapoton"
}
```

thx
