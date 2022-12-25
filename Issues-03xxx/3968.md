# Issue 3968: [with patch, positive review] Magma interface sometimes fails on long inputs

archive/issues_003968.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis fails:\n\n```\n%magma\nQt<t> := RationalFunctionField(Rationals());\nR<w,x,y,z> := PolynomialRing(Qt, 4);\nP0 := w^3 + x^3 + y^3 + z^3;\nP := P0 + (w+x)*(w+2*y)*(w+3*z) + x*y*z;\nPt := P0 + t*P;\nPt_gradient := [Derivative(Pt, w), Derivative(Pt, x), Derivative(Pt, y), Derivative(Pt, z)];\nPt_jac := IdealWithFixedBasis(Pt_gradient);\nPt_gradient_long := Append(Pt_gradient, (1+t)*w*x*y*z);\nPt_jac_long := IdealWithFixedBasis(Pt_gradient_long);\nb := (1+t)*w*x*y*z;\ndiffbasis := [2*w*P, 2*x*P, 2*y*P, 2*z*P, 3*b*P];\ntemp := Coordinates(Pt_jac, diffbasis[5]);\ndiffbasis[5] := (Derivative(temp[1],w) + Derivative(temp[2],x) + \\\n    Derivative(temp[3],y) + Derivative(temp[4],z)) / (-3);\n```\nwith the error: \n\n```\n   File \"<ipython console>\", line 1\n     logstr(r\"\"\"Loading \"/home/r1/kedlaya/.sage//temp/DWORK.MIT.EDU/22570//interface//tmp\"\"\"\")\n                                                                                             ^\nSyntaxError: EOL while scanning single-quoted string\n```\nbut if you replace the last two lines by\n\n```\ndiffbasis[5] := (Derivative(temp[1],w) + Derivative(temp[2],x) + Derivative(temp[3],y))/(-3);\n```\nthen nothing breaks.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3968\n\n",
    "closed_at": "2008-08-28T20:40:00Z",
    "created_at": "2008-08-27T17:27:14Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with patch, positive review] Magma interface sometimes fails on long inputs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3968",
    "user": "https://github.com/kedlaya"
}
```
Assignee: @williamstein

This fails:

```
%magma
Qt<t> := RationalFunctionField(Rationals());
R<w,x,y,z> := PolynomialRing(Qt, 4);
P0 := w^3 + x^3 + y^3 + z^3;
P := P0 + (w+x)*(w+2*y)*(w+3*z) + x*y*z;
Pt := P0 + t*P;
Pt_gradient := [Derivative(Pt, w), Derivative(Pt, x), Derivative(Pt, y), Derivative(Pt, z)];
Pt_jac := IdealWithFixedBasis(Pt_gradient);
Pt_gradient_long := Append(Pt_gradient, (1+t)*w*x*y*z);
Pt_jac_long := IdealWithFixedBasis(Pt_gradient_long);
b := (1+t)*w*x*y*z;
diffbasis := [2*w*P, 2*x*P, 2*y*P, 2*z*P, 3*b*P];
temp := Coordinates(Pt_jac, diffbasis[5]);
diffbasis[5] := (Derivative(temp[1],w) + Derivative(temp[2],x) + \
    Derivative(temp[3],y) + Derivative(temp[4],z)) / (-3);
```
with the error: 

```
   File "<ipython console>", line 1
     logstr(r"""Loading "/home/r1/kedlaya/.sage//temp/DWORK.MIT.EDU/22570//interface//tmp"""")
                                                                                             ^
SyntaxError: EOL while scanning single-quoted string
```
but if you replace the last two lines by

```
diffbasis[5] := (Derivative(temp[1],w) + Derivative(temp[2],x) + Derivative(temp[3],y))/(-3);
```
then nothing breaks.


Issue created by migration from https://trac.sagemath.org/ticket/3968





---

archive/issue_comments_028453.json:
```json
{
    "body": "From IRC\n\n```\n[12:20] <jason_> my error has:\n[12:20] <jason_>    File \"<ipython console>\", line 1\n[12:20] <jason_>      logstr(r\"\"\"Loading \"/home/jason/.sage//temp/sage/4426//interface//tmp4426\"\"\"\")\n[12:20] <kedlaya> yeah, I see something similar\n[12:20] <jason_> I think that last \"\"\"\" is the problem\n[12:20] <jason_> is it being parsed as \" \"\"\"\n[12:20] <jason_> or as \"\"\" \"\n[12:21] <wjp> funny that that error message has a \"# TODO: this is a very lazy temporary bug fix\" above the line in the sources\n[12:21] <kedlaya> too lazy, i guess\n[12:21] <wjp> (sage/misc/preparser_ipython.py, search for logstr)\n[12:21] <kedlaya> i wonder if I can find the ticket for it\n[12:21] <jason_> wjp: if you have the sources, can you put a space in between the \" and the \"\"\" ?\n[12:22] <wjp> the line is return 'logstr(r\"\"\"%s\"\"\")'%t, but I'll add a space after the %s\n[12:23] <wjp> works now\n[12:23] <jason_> okay, now time for the ticket :)\n[12:23] <kedlaya> I'm working on it now\n[12:23] <jason_> from http://docs.python.org/ref/strings.html\n[12:23] <jason_> In triple-quoted strings, unescaped newlines and quotes are allowed (and are retained), except that three unescaped quotes in a row terminate the string. (A ``quote'' is the character used to open the string, i.e. either ' or \".) \n[12:23] <jason_> so apparently the first three \"\"\" terminated the string\n[12:24] <wjp> yes\n[12:24] <kedlaya> ticket #3968 created. Now go fix it. :)\n```",
    "created_at": "2008-08-27T17:31:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3968#issuecomment-28453",
    "user": "https://github.com/jasongrout"
}
```

From IRC

```
[12:20] <jason_> my error has:
[12:20] <jason_>    File "<ipython console>", line 1
[12:20] <jason_>      logstr(r"""Loading "/home/jason/.sage//temp/sage/4426//interface//tmp4426"""")
[12:20] <kedlaya> yeah, I see something similar
[12:20] <jason_> I think that last """" is the problem
[12:20] <jason_> is it being parsed as " """
[12:20] <jason_> or as """ "
[12:21] <wjp> funny that that error message has a "# TODO: this is a very lazy temporary bug fix" above the line in the sources
[12:21] <kedlaya> too lazy, i guess
[12:21] <wjp> (sage/misc/preparser_ipython.py, search for logstr)
[12:21] <kedlaya> i wonder if I can find the ticket for it
[12:21] <jason_> wjp: if you have the sources, can you put a space in between the " and the """ ?
[12:22] <wjp> the line is return 'logstr(r"""%s""")'%t, but I'll add a space after the %s
[12:23] <wjp> works now
[12:23] <jason_> okay, now time for the ticket :)
[12:23] <kedlaya> I'm working on it now
[12:23] <jason_> from http://docs.python.org/ref/strings.html
[12:23] <jason_> In triple-quoted strings, unescaped newlines and quotes are allowed (and are retained), except that three unescaped quotes in a row terminate the string. (A ``quote'' is the character used to open the string, i.e. either ' or ".) 
[12:23] <jason_> so apparently the first three """ terminated the string
[12:24] <wjp> yes
[12:24] <kedlaya> ticket #3968 created. Now go fix it. :)
```



---

archive/issue_comments_028454.json:
```json
{
    "body": "Updated patch to escape strings rather than hoping they don't contain triple quotes.",
    "created_at": "2008-08-27T19:22:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3968#issuecomment-28454",
    "user": "https://github.com/jasongrout"
}
```

Updated patch to escape strings rather than hoping they don't contain triple quotes.



---

archive/issue_comments_028455.json:
```json
{
    "body": "Attachment [parser.patch](tarball://root/attachments/some-uuid/ticket3968/parser.patch) by @jasongrout created at 2008-08-27 19:27:32",
    "created_at": "2008-08-27T19:27:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3968#issuecomment-28455",
    "user": "https://github.com/jasongrout"
}
```

Attachment [parser.patch](tarball://root/attachments/some-uuid/ticket3968/parser.patch) by @jasongrout created at 2008-08-27 19:27:32



---

archive/issue_comments_028456.json:
```json
{
    "body": "Okay, again updated to use the much simpler solution: %r instead of %s.",
    "created_at": "2008-08-27T19:28:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3968#issuecomment-28456",
    "user": "https://github.com/jasongrout"
}
```

Okay, again updated to use the much simpler solution: %r instead of %s.



---

archive/issue_comments_028457.json:
```json
{
    "body": "Shouldn't we add a doctest that tests for the case that Kiran discovered?\n\nCheers,\n\nMichael",
    "created_at": "2008-08-27T20:45:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3968#issuecomment-28457",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Shouldn't we add a doctest that tests for the case that Kiran discovered?

Cheers,

Michael



---

archive/issue_events_009100.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-27T20:45:29Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3968",
    "milestone": "sage-3.1.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3968#event-9100"
}
```



---

archive/issue_comments_028458.json:
```json
{
    "body": "For the record: doctests pass with the patch applied.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-27T21:05:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3968#issuecomment-28458",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

For the record: doctests pass with the patch applied.

Cheers,

Michael



---

archive/issue_comments_028459.json:
```json
{
    "body": "For a potential doctest, this is easy to trigger with the singular interface too:\n\n```\nsage: %singular\n\n  --> Switching to Singular <-- \n\n''\nsingular: print(\"\\\"test\\\"\")\n------------------------------------------------------------\n   File \"<ipython console>\", line 1\n     logstr(r\"\"\"\"test\"\"\"\")\n                         ^\nSyntaxError: EOL while scanning single-quoted string\n```",
    "created_at": "2008-08-27T21:15:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3968#issuecomment-28459",
    "user": "https://github.com/wjp"
}
```

For a potential doctest, this is easy to trigger with the singular interface too:

```
sage: %singular

  --> Switching to Singular <-- 

''
singular: print("\"test\"")
------------------------------------------------------------
   File "<ipython console>", line 1
     logstr(r""""test"""")
                         ^
SyntaxError: EOL while scanning single-quoted string
```



---

archive/issue_comments_028460.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-28T20:40:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3968#issuecomment-28460",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_028461.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha2",
    "created_at": "2008-08-28T20:40:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3968",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3968#issuecomment-28461",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.alpha2



---

archive/issue_events_009101.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-28T20:40:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3968",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3968#event-9101"
}
```
