# Issue 7326: html.table should run jsmath on the resulting table

archive/issues_007326.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  whuss @rbeezer @kcrisman\n\nIt would be *really* nice if you could include latex code in a table, like this:\n\n\n```\nvar('t')\ndensity=t^2\nhtml.table([\n[\"Density $\\delta(x,y)$\", density]\n])\n```\n\n\nand have it do the jsmath magic on the $\\delta(x,y)$ part.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7326\n\n",
    "created_at": "2009-10-27T22:02:22Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "html.table should run jsmath on the resulting table",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7326",
    "user": "https://github.com/jasongrout"
}
```
Assignee: cwitty

CC:  whuss @rbeezer @kcrisman

It would be *really* nice if you could include latex code in a table, like this:


```
var('t')
density=t^2
html.table([
["Density $\delta(x,y)$", density]
])
```


and have it do the jsmath magic on the $\delta(x,y)$ part.

Issue created by migration from https://trac.sagemath.org/ticket/7326





---

archive/issue_comments_061156.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-10-27T22:03:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7326#issuecomment-61156",
    "user": "https://github.com/jasongrout"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_061157.json:
```json
{
    "body": "As a workaround this already works:\n\n\n```\nvar('t')\ndensity=t^2\nhtml.table([\n['Density <span class=\"math\">\\delta(x,y)</span>', density]\n])\n```\n\n\nI am not sure why jsmath does not pick up the $$s in this case.",
    "created_at": "2009-10-28T08:13:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7326#issuecomment-61157",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```

As a workaround this already works:


```
var('t')
density=t^2
html.table([
['Density <span class="math">\delta(x,y)</span>', density]
])
```


I am not sure why jsmath does not pick up the $$s in this case.



---

archive/issue_comments_061158.json:
```json
{
    "body": "Attachment [trac-7326-html-table-math.patch](tarball://root/attachments/some-uuid/ticket7326/trac-7326-html-table-math.patch) by @jasongrout created at 2009-10-28 08:43:35",
    "created_at": "2009-10-28T08:43:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7326#issuecomment-61158",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-7326-html-table-math.patch](tarball://root/attachments/some-uuid/ticket7326/trac-7326-html-table-math.patch) by @jasongrout created at 2009-10-28 08:43:35



---

archive/issue_comments_061159.json:
```json
{
    "body": "This is a very easy patch to review.",
    "created_at": "2009-10-28T08:44:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7326#issuecomment-61159",
    "user": "https://github.com/jasongrout"
}
```

This is a very easy patch to review.



---

archive/issue_comments_061160.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-28T08:44:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7326#issuecomment-61160",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061161.json:
```json
{
    "body": "Replying to [comment:2 whuss]:\n> As a workaround this already works:\n> \n> {{{\n> var('t')\n> density=t^2\n> html.table([\n> ['Density <span class=\"math\">\\delta(x,y)</span>', density]\n> ])\n> }}}\n\n\nso does html.table([This is the Trac macro *sage.misc.html.math_parse* that was inherited from the migration called with arguments ('hi $x^2$'))](https://trac.sagemath.org/wiki/WikiMacros#sage.misc.html.math_parse-macro))\n\nMaybe what is going on is jsmath seems to be not set up to try to find dollar signs, but to only pay attention to class=\"math\" spans and divs.",
    "created_at": "2009-10-28T08:58:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7326#issuecomment-61161",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:2 whuss]:
> As a workaround this already works:
> 
> {{{
> var('t')
> density=t^2
> html.table([
> ['Density <span class="math">\delta(x,y)</span>', density]
> ])
> }}}


so does html.table([This is the Trac macro *sage.misc.html.math_parse* that was inherited from the migration called with arguments ('hi $x^2$'))](https://trac.sagemath.org/wiki/WikiMacros#sage.misc.html.math_parse-macro))

Maybe what is going on is jsmath seems to be not set up to try to find dollar signs, but to only pay attention to class="math" spans and divs.



---

archive/issue_comments_061162.json:
```json
{
    "body": "Replying to [comment:3 jason]:\n> This is a very easy patch to review.\n\nIt works, and passes the tests. Positiv review.",
    "created_at": "2009-10-28T12:52:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7326#issuecomment-61162",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```

Replying to [comment:3 jason]:
> This is a very easy patch to review.

It works, and passes the tests. Positiv review.



---

archive/issue_comments_061163.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-28T12:52:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7326#issuecomment-61163",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061164.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-31T15:57:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7326",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7326#issuecomment-61164",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
