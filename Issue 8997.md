# Issue 8997: riemann_roch_basis is implemented incorrectly in sage

archive/issues_008997.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  rkirov minz oleksandrmotsak\n\nSee the file schemes/plane_curves/projective_curve.py, where it says\n\n```\n\n        The following example illustrates that the Riemann-Roch space\n        function in Singular doesn't *not* work correctly.\n        \n        ::\n        \n            sage: R.<x,y,z> = GF(5)[]\n            sage: f = x^7 + y^7 + z^7\n            sage: C = Curve(f); pts = C.rational_points()\n            sage: D = C.divisor([ (3, pts[0]), (-1,pts[1]), (10, pts[5]) ])\n            sage: C.riemann_roch_basis(D)    # output is random (!!!!)\n            [x/(y + x), (z + y)/(y + x)]\n        \n        The answer has dimension 2 (confirmed via Magma). But it varies\n        between 1 and quite large with Singular.\n```\n\n\nThe problem can be solved by learning how the relevant code in Singular works then correctly wrapping it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8997\n\n",
    "created_at": "2010-05-20T00:19:02Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "riemann_roch_basis is implemented incorrectly in sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8997",
    "user": "https://github.com/williamstein"
}
```
Assignee: @aghitza

CC:  rkirov minz oleksandrmotsak

See the file schemes/plane_curves/projective_curve.py, where it says

```

        The following example illustrates that the Riemann-Roch space
        function in Singular doesn't *not* work correctly.
        
        ::
        
            sage: R.<x,y,z> = GF(5)[]
            sage: f = x^7 + y^7 + z^7
            sage: C = Curve(f); pts = C.rational_points()
            sage: D = C.divisor([ (3, pts[0]), (-1,pts[1]), (10, pts[5]) ])
            sage: C.riemann_roch_basis(D)    # output is random (!!!!)
            [x/(y + x), (z + y)/(y + x)]
        
        The answer has dimension 2 (confirmed via Magma). But it varies
        between 1 and quite large with Singular.
```


The problem can be solved by learning how the relevant code in Singular works then correctly wrapping it.

Issue created by migration from https://trac.sagemath.org/ticket/8997





---

archive/issue_comments_083049.json:
```json
{
    "body": "Changing component from algebra to algebraic geometry.",
    "created_at": "2010-05-20T00:19:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8997#issuecomment-83049",
    "user": "https://github.com/williamstein"
}
```

Changing component from algebra to algebraic geometry.



---

archive/issue_comments_083050.json:
```json
{
    "body": "Replying to [ticket:8997 was]:\n\n> \n> The problem can be solved by learning how the relevant code in Singular works then correctly wrapping it. \n\nAre there any more details on this available?",
    "created_at": "2010-05-21T16:41:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8997#issuecomment-83050",
    "user": "https://github.com/wdjoyner"
}
```

Replying to [ticket:8997 was]:

> 
> The problem can be solved by learning how the relevant code in Singular works then correctly wrapping it. 

Are there any more details on this available?



---

archive/issue_comments_083051.json:
```json
{
    "body": "For the record, the relevant Singular ticket is here: http://www.singular.uni-kl.de:8002/trac/ticket/153",
    "created_at": "2010-05-25T07:22:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8997#issuecomment-83051",
    "user": "https://github.com/williamstein"
}
```

For the record, the relevant Singular ticket is here: http://www.singular.uni-kl.de:8002/trac/ticket/153



---

archive/issue_comments_083052.json:
```json
{
    "body": "Replying to [comment:3 was]:\n> For the record, the relevant Singular ticket is here: http://www.singular.uni-kl.de:8002/trac/ticket/153\n\nThanks. This suggests that all one needs to do is to add the singular command \n\n```\nsystem(\"random\", mySeedAsAnInt);\n```\n\nat the top of the function code.",
    "created_at": "2010-05-25T11:13:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8997#issuecomment-83052",
    "user": "https://github.com/wdjoyner"
}
```

Replying to [comment:3 was]:
> For the record, the relevant Singular ticket is here: http://www.singular.uni-kl.de:8002/trac/ticket/153

Thanks. This suggests that all one needs to do is to add the singular command 

```
system("random", mySeedAsAnInt);
```

at the top of the function code.



---

archive/issue_comments_083053.json:
```json
{
    "body": "apply to 4.4.2",
    "created_at": "2010-05-26T18:53:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8997#issuecomment-83053",
    "user": "https://github.com/wdjoyner"
}
```

apply to 4.4.2



---

archive/issue_comments_083054.json:
```json
{
    "body": "Attachment [trac_8997-riemann-roch.patch](tarball://root/attachments/some-uuid/ticket8997/trac_8997-riemann-roch.patch) by @wdjoyner created at 2010-05-26 18:56:52\n\nThe attached patch seems to fix the problem. When applied to 4.4.2 on a 10.6.3 mac, it passes sage -testall except for an unrelated docstring failure (in interfaces/r.py).\n\nI'm leaving it as needs work for now since I want to test it on more machines. I'm posting it in case others want to test it too.",
    "created_at": "2010-05-26T18:56:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8997#issuecomment-83054",
    "user": "https://github.com/wdjoyner"
}
```

Attachment [trac_8997-riemann-roch.patch](tarball://root/attachments/some-uuid/ticket8997/trac_8997-riemann-roch.patch) by @wdjoyner created at 2010-05-26 18:56:52

The attached patch seems to fix the problem. When applied to 4.4.2 on a 10.6.3 mac, it passes sage -testall except for an unrelated docstring failure (in interfaces/r.py).

I'm leaving it as needs work for now since I want to test it on more machines. I'm posting it in case others want to test it too.



---

archive/issue_comments_083055.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-05-26T18:56:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8997#issuecomment-83055",
    "user": "https://github.com/wdjoyner"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_083056.json:
```json
{
    "body": "This patch does not work. My guess is that\n\n\n```\nsystem(\"random\", mySeedAsAnInt);\n```\n\ndoes not really set the random seed for all commands, but I could easily be wrong. In any case, it seems that the command now does return the dimension in a consistent way for different machines. That is progress, since the old version was much worse. However, the basis (ie, the list of functions spanning the RR space) is not deterministic. I'm not sure how to fix that.",
    "created_at": "2010-05-27T17:39:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8997#issuecomment-83056",
    "user": "https://github.com/wdjoyner"
}
```

This patch does not work. My guess is that


```
system("random", mySeedAsAnInt);
```

does not really set the random seed for all commands, but I could easily be wrong. In any case, it seems that the command now does return the dimension in a consistent way for different machines. That is progress, since the old version was much worse. However, the basis (ie, the list of functions spanning the RR space) is not deterministic. I'm not sure how to fix that.



---

archive/issue_comments_083057.json:
```json
{
    "body": "My impression is that the problem lies with Singular. I adapted the example in the description above and typed directly into Singular the following:\n\n\n```\nkill s, C, Ctemp, temp, G, R, LG;\n\nLIB \"brnoeth.lib\";\nint plevel=printlevel;\nprintlevel=-1;\nsystem(\"random\", 1);\n\nring s=5,(x,y),lp;\nlist C=Adj_div(x7+y7+1);\nC=NSplaces(1,C);\ndef R=C[1][2];\n\n# I want to look at the points to be able to define\n# the same divisor each time, see below\ndef Ctemp=extcurve(1,C);\ndef temp=Ctemp[1][5];\nsetring temp;\nprint(POINTS);\n\nsetring R;\n\n# adapt the line below according to the ordering of the points\n# i always chose the divisor 3(0,-1,1)-1(1,2,1)+10(2,1,1)\nintvec G = ;\n\nlist LG=BrillNoether(G,C);\nLG;\n\nprintlevel=plevel;\n```\n\n\nNot only did the bases vary each time I ran this code (even though I fixed the random seed in the sixth line), the resulting bases also had different cardinality (either 0 or 2).\n\n(I also tried to post this on the Singular trac server, but failed to do so. Maybe someone else is able to update the Singular ticket?)",
    "created_at": "2010-07-19T09:47:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8997#issuecomment-83057",
    "user": "https://trac.sagemath.org/admin/accounts/users/minz"
}
```

My impression is that the problem lies with Singular. I adapted the example in the description above and typed directly into Singular the following:


```
kill s, C, Ctemp, temp, G, R, LG;

LIB "brnoeth.lib";
int plevel=printlevel;
printlevel=-1;
system("random", 1);

ring s=5,(x,y),lp;
list C=Adj_div(x7+y7+1);
C=NSplaces(1,C);
def R=C[1][2];

# I want to look at the points to be able to define
# the same divisor each time, see below
def Ctemp=extcurve(1,C);
def temp=Ctemp[1][5];
setring temp;
print(POINTS);

setring R;

# adapt the line below according to the ordering of the points
# i always chose the divisor 3(0,-1,1)-1(1,2,1)+10(2,1,1)
intvec G = ;

list LG=BrillNoether(G,C);
LG;

printlevel=plevel;
```


Not only did the bases vary each time I ran this code (even though I fixed the random seed in the sixth line), the resulting bases also had different cardinality (either 0 or 2).

(I also tried to post this on the Singular trac server, but failed to do so. Maybe someone else is able to update the Singular ticket?)



---

archive/issue_comments_083058.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2010-10-14T16:09:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8997#issuecomment-83058",
    "user": "https://trac.sagemath.org/admin/accounts/users/OleksandrMotsak"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_083059.json:
```json
{
    "body": "Dear minz,\n\n1. what do you mean with \"intvec G = ;\" in the Singular code?\n2. could you please answer to the comment by Jose Ignacio Farran at\nhttp://www.singular.uni-kl.de:8002/trac/ticket/153#comment:7 ?",
    "created_at": "2010-10-14T16:09:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8997#issuecomment-83059",
    "user": "https://trac.sagemath.org/admin/accounts/users/OleksandrMotsak"
}
```

Dear minz,

1. what do you mean with "intvec G = ;" in the Singular code?
2. could you please answer to the comment by Jose Ignacio Farran at
http://www.singular.uni-kl.de:8002/trac/ticket/153#comment:7 ?



---

archive/issue_comments_083060.json:
```json
{
    "body": "apply to 4.6",
    "created_at": "2010-11-21T12:39:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8997#issuecomment-83060",
    "user": "https://trac.sagemath.org/admin/accounts/users/minz"
}
```

apply to 4.6



---

archive/issue_comments_083061.json:
```json
{
    "body": "Attachment [trac_8997_fix_rr_basis_and_doc.patch](tarball://root/attachments/some-uuid/ticket8997/trac_8997_fix_rr_basis_and_doc.patch) by minz created at 2010-11-21 12:50:44\n\nFollowing Jose's explanations on the Singular trac server, the modified Sage wrapper should now work with the new patch. What the unmodified wrapper did wrong was how it defined the divisor in Singular. There's actually two lists that are important: The divisor needs to be defined relative to the list of points C[3] (in the above example), but to know which point the k-th entry of this list actually refers to, one has to parse the list POINTS of the rings C[5][d][1], where d is the degree of the point. -- The patch also modifies the documentation to illustrate this with an example.",
    "created_at": "2010-11-21T12:50:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8997#issuecomment-83061",
    "user": "https://trac.sagemath.org/admin/accounts/users/minz"
}
```

Attachment [trac_8997_fix_rr_basis_and_doc.patch](tarball://root/attachments/some-uuid/ticket8997/trac_8997_fix_rr_basis_and_doc.patch) by minz created at 2010-11-21 12:50:44

Following Jose's explanations on the Singular trac server, the modified Sage wrapper should now work with the new patch. What the unmodified wrapper did wrong was how it defined the divisor in Singular. There's actually two lists that are important: The divisor needs to be defined relative to the list of points C[3] (in the above example), but to know which point the k-th entry of this list actually refers to, one has to parse the list POINTS of the rings C[5][d][1], where d is the degree of the point. -- The patch also modifies the documentation to illustrate this with an example.



---

archive/issue_comments_083062.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-11-21T12:50:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8997#issuecomment-83062",
    "user": "https://trac.sagemath.org/admin/accounts/users/minz"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_083063.json:
```json
{
    "body": "Replying to [comment:12 minz]:\n> Following Jose's explanations on the Singular trac server, the modified Sage wrapper \n\n...\n\nThank you! \n\nI'll look at this carefully when classes end this semester, which will be in a few weeks.",
    "created_at": "2010-11-29T00:27:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8997#issuecomment-83063",
    "user": "https://github.com/wdjoyner"
}
```

Replying to [comment:12 minz]:
> Following Jose's explanations on the Singular trac server, the modified Sage wrapper 

...

Thank you! 

I'll look at this carefully when classes end this semester, which will be in a few weeks.



---

archive/issue_comments_083064.json:
```json
{
    "body": "This looks good. It applies fine to sage 4.6 on an ubuntu linux machine and passes sage -testall. I have fixed the code and docstrings in agcode.py so that it runs too. I guess this should be a separate ticket?\n\nAgain, thanks *very* much!",
    "created_at": "2010-12-20T03:36:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8997#issuecomment-83064",
    "user": "https://github.com/wdjoyner"
}
```

This looks good. It applies fine to sage 4.6 on an ubuntu linux machine and passes sage -testall. I have fixed the code and docstrings in agcode.py so that it runs too. I guess this should be a separate ticket?

Again, thanks *very* much!



---

archive/issue_comments_083065.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-12-20T03:36:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8997#issuecomment-83065",
    "user": "https://github.com/wdjoyner"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083066.json:
```json
{
    "body": "Changing status from positive_review to needs_info.",
    "created_at": "2011-01-18T13:57:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8997#issuecomment-83066",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_info.



---

archive/issue_comments_083067.json:
```json
{
    "body": "This needs some clarifications:\n* which patch(es) need to be applied?\n* who are the authors/reviewers? (please fill in the real names in the Author and Reviewer fields on this ticket)",
    "created_at": "2011-01-18T13:57:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8997#issuecomment-83067",
    "user": "https://github.com/jdemeyer"
}
```

This needs some clarifications:
* which patch(es) need to be applied?
* who are the authors/reviewers? (please fill in the real names in the Author and Reviewer fields on this ticket)



---

archive/issue_comments_083068.json:
```json
{
    "body": "Replying to [comment:16 jdemeyer]:\n> This needs some clarifications:\n>  * which patch(es) need to be applied?\n>  * who are the authors/reviewers? (please fill in the real names in \n> the Author and Reviewer fields on this ticket)\n\nDone. Others helped, such as William Stein and Jose Farran.\n\nMany thanks to everyone who helped with fixing this issue!\n\nCan this be changed back to positive review now?",
    "created_at": "2011-01-18T20:55:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8997#issuecomment-83068",
    "user": "https://github.com/wdjoyner"
}
```

Replying to [comment:16 jdemeyer]:
> This needs some clarifications:
>  * which patch(es) need to be applied?
>  * who are the authors/reviewers? (please fill in the real names in 
> the Author and Reviewer fields on this ticket)

Done. Others helped, such as William Stein and Jose Farran.

Many thanks to everyone who helped with fixing this issue!

Can this be changed back to positive review now?



---

archive/issue_comments_083069.json:
```json
{
    "body": "Replying to [comment:17 wdj]:\n> Replying to [comment:16 jdemeyer]:\n> > This needs some clarifications:\n> >  * which patch(es) need to be applied?\nYou didn't answer this question...",
    "created_at": "2011-01-19T01:30:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8997#issuecomment-83069",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:17 wdj]:
> Replying to [comment:16 jdemeyer]:
> > This needs some clarifications:
> >  * which patch(es) need to be applied?
You didn't answer this question...



---

archive/issue_comments_083070.json:
```json
{
    "body": "Replying to [comment:18 jdemeyer]:\n> Replying to [comment:17 wdj]:\n> > Replying to [comment:16 jdemeyer]:\n> > > This needs some clarifications:\n> > >  * which patch(es) need to be applied?\n> You didn't answer this question...\n\nSorry! Just trac_8997_fix_rr_basis_and_doc.patch",
    "created_at": "2011-01-19T01:43:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8997#issuecomment-83070",
    "user": "https://github.com/wdjoyner"
}
```

Replying to [comment:18 jdemeyer]:
> Replying to [comment:17 wdj]:
> > Replying to [comment:16 jdemeyer]:
> > > This needs some clarifications:
> > >  * which patch(es) need to be applied?
> You didn't answer this question...

Sorry! Just trac_8997_fix_rr_basis_and_doc.patch



---

archive/issue_comments_083071.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-01-19T01:51:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8997#issuecomment-83071",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_083072.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-19T01:52:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8997#issuecomment-83072",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083073.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-19T22:19:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8997",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8997#issuecomment-83073",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_009151.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-01-19T22:19:54Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8997",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8997#event-9151"
}
```
