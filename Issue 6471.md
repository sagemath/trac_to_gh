# Issue 6471: clarify differences between c.abs() and c.norm() for complex c

archive/issues_006471.json:
```json
{
    "body": "Assignee: tbd\n\nIf `c` is of type `CC`, then `c.abs()` returns the absolute value of a complex number and `c.norm()` returns the norm of a complex number. One problem with this is that the absolute value of a complex number is also referred to as the complex norm. This problem was noticed in IRC:\n\n```\n15:32 < greg> the sage command norm() returns the modulus squared of complex\n             numbers, is this the desired behavior?\n15:44 < mvngu> greg: If c is a complex number (type CC), then c.norm() returns\n              the complex norm of c. That is, if c = a + bi then c.norm()\n              returns a^2 + b^2.\n15:44 < mvngu> Is that what you mean?\n15:46 < greg> isn't the complex norm typicaly sqrt(a^2 + b^2)\n15:50 < mvngu> greg: That's the absolute value. In that case, use c.abs().\n15:53 < mvngu> And I agree that there's various names for this: modulue of\n              complex number, absolute value of complex number, complex norm.\n15:54 < greg> mvngu: okay thanks\n15:54 < mvngu> So it clarifies for you?\n15:56 < greg> yeah, I think so.\n15:56 < greg> out of curiosity, where is a^2 + b^2 typically used as the norm?\n             I'm checking mathworld and wikipedia and my complex analysis\n             books and they all use the L2 norm\n15:58 < mvngu> You know Gaussian integers?\n15:58 < greg> yeah\n15:58 < greg> okay i see that\n15:58 < greg> cool thanks\n15:58 < mvngu> yeah... the norm of a Gaussian integer is defined like that.\n15:59 < greg> okay i see\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6471\n\n",
    "created_at": "2009-07-07T04:15:30Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "clarify differences between c.abs() and c.norm() for complex c",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6471",
    "user": "mvngu"
}
```
Assignee: tbd

If `c` is of type `CC`, then `c.abs()` returns the absolute value of a complex number and `c.norm()` returns the norm of a complex number. One problem with this is that the absolute value of a complex number is also referred to as the complex norm. This problem was noticed in IRC:

```
15:32 < greg> the sage command norm() returns the modulus squared of complex
             numbers, is this the desired behavior?
15:44 < mvngu> greg: If c is a complex number (type CC), then c.norm() returns
              the complex norm of c. That is, if c = a + bi then c.norm()
              returns a^2 + b^2.
15:44 < mvngu> Is that what you mean?
15:46 < greg> isn't the complex norm typicaly sqrt(a^2 + b^2)
15:50 < mvngu> greg: That's the absolute value. In that case, use c.abs().
15:53 < mvngu> And I agree that there's various names for this: modulue of
              complex number, absolute value of complex number, complex norm.
15:54 < greg> mvngu: okay thanks
15:54 < mvngu> So it clarifies for you?
15:56 < greg> yeah, I think so.
15:56 < greg> out of curiosity, where is a^2 + b^2 typically used as the norm?
             I'm checking mathworld and wikipedia and my complex analysis
             books and they all use the L2 norm
15:58 < mvngu> You know Gaussian integers?
15:58 < greg> yeah
15:58 < greg> okay i see that
15:58 < greg> cool thanks
15:58 < mvngu> yeah... the norm of a Gaussian integer is defined like that.
15:59 < greg> okay i see
```


Issue created by migration from https://trac.sagemath.org/ticket/6471





---

archive/issue_comments_052312.json:
```json
{
    "body": "Attachment\n\nbased on Sage 4.1.rc0",
    "created_at": "2009-07-07T06:06:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6471",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6471#issuecomment-52312",
    "user": "mvngu"
}
```

Attachment

based on Sage 4.1.rc0



---

archive/issue_comments_052313.json:
```json
{
    "body": "Changing assignee from tbd to tba.",
    "created_at": "2009-07-07T06:08:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6471",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6471#issuecomment-52313",
    "user": "mvngu"
}
```

Changing assignee from tbd to tba.



---

archive/issue_comments_052314.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-07-07T06:08:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6471",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6471#issuecomment-52314",
    "user": "mvngu"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_052315.json:
```json
{
    "body": "Changing component from algebra to documentation.",
    "created_at": "2009-07-07T06:08:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6471",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6471#issuecomment-52315",
    "user": "mvngu"
}
```

Changing component from algebra to documentation.



---

archive/issue_comments_052316.json:
```json
{
    "body": "Changing keywords from \"\" to \"absolute value, complex norm\".",
    "created_at": "2009-07-07T06:08:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6471",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6471#issuecomment-52316",
    "user": "mvngu"
}
```

Changing keywords from "" to "absolute value, complex norm".



---

archive/issue_comments_052317.json:
```json
{
    "body": "Looks good.",
    "created_at": "2009-07-11T09:22:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6471",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6471#issuecomment-52317",
    "user": "AlexGhitza"
}
```

Looks good.



---

archive/issue_comments_052318.json:
```json
{
    "body": "I agree.  Blame the number theorists!  In number theory there are lots of norms with different norm-alizations (joke) which causes a lot of confusion.   In the implementation of local and global heights for number field elements the same issue arose (see #6046, now merged): for complex embeddings there is an issue of whether or not to multiply by 2 (which is the logarithmic equivalent of the current discussion) and I allowed both, with a boolean \"weighted\" parameter to switch between them.",
    "created_at": "2009-07-11T15:30:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6471",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6471#issuecomment-52318",
    "user": "cremona"
}
```

I agree.  Blame the number theorists!  In number theory there are lots of norms with different norm-alizations (joke) which causes a lot of confusion.   In the implementation of local and global heights for number field elements the same issue arose (see #6046, now merged): for complex embeddings there is an issue of whether or not to multiply by 2 (which is the logarithmic equivalent of the current discussion) and I allowed both, with a boolean "weighted" parameter to switch between them.



---

archive/issue_comments_052319.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-17T08:21:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6471",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6471#issuecomment-52319",
    "user": "mvngu"
}
```

Resolution: fixed
