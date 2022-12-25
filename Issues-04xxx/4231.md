# Issue 4231: [with patch, positive review]  magma -- long input too verbose in some cases

archive/issues_004231.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  georgsweber\n\n```\nWhen evaluating this in the notebook:\n\n%magma\npolt<t> := RationalFunctionField(Rationals());\nR<w,x,y,z> := PolynomialRing(polt, 4);\nQ0 := w^3 + x^3 + y^3 + z^3;\nQ := (w+x)*(w+2*y)*(w+3*z) + 3*x*y*(w+x+z);\nQt := Q0 + t*Q;\nQt_gradient := [Derivative(Qt, w), Derivative(Qt, x), Derivative(Qt, y), Derivative(Qt, z)];\nQt_jac := IdealWithFixedBasis(Qt_gradient);\nb := w*x*y*z;\ntemp := Coordinates(Qt_jac, 3*b*Q);\ntemp2 := Derivative(temp[1],w) + Derivative(temp[2],x) + Derivative(temp[3],y) + Derivative(temp[4],z);\n\n\n> ---\n> I get the funny error message:\n> ---\n> Loading\n> \"/home/r1/kedlaya/.sage//temp/DWORK.MIT.EDU/5272//interface//tmp5272\"\n> ---\n> but I think the calculation goes through. I'm guessing this is because\n> Magma is returning a long output which gets saved to  a temporary\n> file. But does the notebook user really need to see this message? I\n> don't.\n>\n> Incidentally, if I change the last line to the following two lines:\n> ---\n> temp2 := Derivative(temp[1],w) + Derivative(temp[2],x);\n> temp2 := temp2 + Derivative(temp[3],y) + Derivative(temp[4],z);\n> ---\n> then I don't get any error message.\n \nI believe that Sage uses temp files for inputs larger than a certain\nsize.  It seems this long input passed that size and you're seeing a\n\"verbose loading\" message.  Not really an error message, but I'm sure\nWilliam can add it to his list of Magma interface things to do.\n\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/4231\n\n",
    "closed_at": "2008-10-12T15:33:49Z",
    "created_at": "2008-10-01T16:18:13Z",
    "labels": [
        "component: interfaces",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "[with patch, positive review]  magma -- long input too verbose in some cases",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4231",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  georgsweber

```
When evaluating this in the notebook:

%magma
polt<t> := RationalFunctionField(Rationals());
R<w,x,y,z> := PolynomialRing(polt, 4);
Q0 := w^3 + x^3 + y^3 + z^3;
Q := (w+x)*(w+2*y)*(w+3*z) + 3*x*y*(w+x+z);
Qt := Q0 + t*Q;
Qt_gradient := [Derivative(Qt, w), Derivative(Qt, x), Derivative(Qt, y), Derivative(Qt, z)];
Qt_jac := IdealWithFixedBasis(Qt_gradient);
b := w*x*y*z;
temp := Coordinates(Qt_jac, 3*b*Q);
temp2 := Derivative(temp[1],w) + Derivative(temp[2],x) + Derivative(temp[3],y) + Derivative(temp[4],z);


> ---
> I get the funny error message:
> ---
> Loading
> "/home/r1/kedlaya/.sage//temp/DWORK.MIT.EDU/5272//interface//tmp5272"
> ---
> but I think the calculation goes through. I'm guessing this is because
> Magma is returning a long output which gets saved to  a temporary
> file. But does the notebook user really need to see this message? I
> don't.
>
> Incidentally, if I change the last line to the following two lines:
> ---
> temp2 := Derivative(temp[1],w) + Derivative(temp[2],x);
> temp2 := temp2 + Derivative(temp[3],y) + Derivative(temp[4],z);
> ---
> then I don't get any error message.
 
I believe that Sage uses temp files for inputs larger than a certain
size.  It seems this long input passed that size and you're seeing a
"verbose loading" message.  Not really an error message, but I'm sure
William can add it to his list of Magma interface things to do.

```

Issue created by migration from https://trac.sagemath.org/ticket/4231





---

archive/issue_comments_030689.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-01T16:18:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4231#issuecomment-30689",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to assigned.



---

archive/issue_comments_030690.json:
```json
{
    "body": "Attachment [sage-4231.patch](tarball://root/attachments/some-uuid/ticket4231/sage-4231.patch) by @williamstein created at 2008-10-04 03:37:55",
    "created_at": "2008-10-04T03:37:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4231#issuecomment-30690",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-4231.patch](tarball://root/attachments/some-uuid/ticket4231/sage-4231.patch) by @williamstein created at 2008-10-04 03:37:55



---

archive/issue_comments_030691.json:
```json
{
    "body": "NOTE: I forgot some # optionals, yet again for the doctests.  Those will be in #4240, which should be done within a day.",
    "created_at": "2008-10-04T04:46:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4231#issuecomment-30691",
    "user": "https://github.com/williamstein"
}
```

NOTE: I forgot some # optionals, yet again for the doctests.  Those will be in #4240, which should be done within a day.



---

archive/issue_comments_030692.json:
```json
{
    "body": "The first half of the patch does indeed fix the issue reported.\n\nThe second half of this patch adds a doctest showing that the patch really works,\nmore precisely this doctest fails without the patch.\n\nHowever the new doctest fails also (earlier) if no local magma install may be found.\n\nI'd vote nevertheless to take this patch in right now; and then apply #4240 as soon as possible. Other solution would imply having to change the patch(es) in #4240 accordingly, which seems to be superfluous work.",
    "created_at": "2008-10-05T10:05:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4231#issuecomment-30692",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

The first half of the patch does indeed fix the issue reported.

The second half of this patch adds a doctest showing that the patch really works,
more precisely this doctest fails without the patch.

However the new doctest fails also (earlier) if no local magma install may be found.

I'd vote nevertheless to take this patch in right now; and then apply #4240 as soon as possible. Other solution would imply having to change the patch(es) in #4240 accordingly, which seems to be superfluous work.



---

archive/issue_comments_030693.json:
```json
{
    "body": "Better luck next time since I don't want to break the followup patch - which is not ready for review and either way itself needs to add a couple #optional tags anyway.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-11T09:00:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4231#issuecomment-30693",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Better luck next time since I don't want to break the followup patch - which is not ready for review and either way itself needs to add a couple #optional tags anyway.

Cheers,

Michael



---

archive/issue_events_009573.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-11T09:00:36Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4231",
    "milestone": "sage-3.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4231#event-9573"
}
```



---

archive/issue_events_009574.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-12T15:33:49Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4231",
    "milestone": "sage-3.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4231#event-9574"
}
```



---

archive/issue_events_009575.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-12T15:33:49Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4231",
    "milestone": "sage-3.1.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4231#event-9575"
}
```



---

archive/issue_events_009576.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-12T15:33:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4231",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4231#event-9576"
}
```



---

archive/issue_comments_030694.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-12T15:33:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4231#issuecomment-30694",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030695.json:
```json
{
    "body": "Merged in Sage 3.1.3.rc0",
    "created_at": "2008-10-12T15:33:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4231#issuecomment-30695",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.3.rc0
