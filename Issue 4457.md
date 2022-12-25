# Issue 4457: tutorial: add find_root()  to "2.4.1 Solving Equations"

archive/issues_004457.json:
```json
{
    "body": "Assignee: tba\n\nCurrently, the section in the tutorial on solving equations refers only to analytical solutions, which are found using \"solve().\"  When solve fails, it may be worth using a numerical solution.  \n\nFor equations with a single variable, this can be done using find_root().  It will save new users time to find \"find_root()\" mentioned with \"solve()\" in the section on solving equations.\n\nExamples:\n\n```\nid=1|\nvar('theta')\n///\n\n<html><span class=\"math\">\\theta</span></html>\n```\n\n\n\n```\nid=2|\nsolve(theta^2 + 1==4)\n///\n\n<html><span class=\"math\">\\left[\\theta  =  -\\sqrt{ 3 }, \n \\theta  =  \\sqrt{ 3 }\\right]</span></html>\n```\n\n\n\n```\nid=3|\nsolve(cos(theta)==sin(theta))\n///\n\n<html><span class=\"math\">\\left[\\sin \\left( \\theta \\right)  =  \\cos \\left( \\theta \\right)\\right]</span></html>\n```\n\n\n\n```\nid=4|\nfind_root(cos(theta)==sin(theta),0,pi/2)\n///\n\n<html><span class=\"math\">0.785398163397</span></html>\n```\n\n\n\n```\nid=5|\npi.n()/4\n///\n\n<html><span class=\"math\">0.785398163397448</span></html>\n```\n\n\n\n```\nid=6|\n\n///\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4457\n\n",
    "created_at": "2008-11-06T23:54:51Z",
    "labels": [
        "component: documentation"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "tutorial: add find_root()  to \"2.4.1 Solving Equations\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4457",
    "user": "https://trac.sagemath.org/admin/accounts/users/dhbradshaw"
}
```
Assignee: tba

Currently, the section in the tutorial on solving equations refers only to analytical solutions, which are found using "solve()."  When solve fails, it may be worth using a numerical solution.  

For equations with a single variable, this can be done using find_root().  It will save new users time to find "find_root()" mentioned with "solve()" in the section on solving equations.

Examples:

```
id=1|
var('theta')
///

<html><span class="math">\theta</span></html>
```



```
id=2|
solve(theta^2 + 1==4)
///

<html><span class="math">\left[\theta  =  -\sqrt{ 3 }, 
 \theta  =  \sqrt{ 3 }\right]</span></html>
```



```
id=3|
solve(cos(theta)==sin(theta))
///

<html><span class="math">\left[\sin \left( \theta \right)  =  \cos \left( \theta \right)\right]</span></html>
```



```
id=4|
find_root(cos(theta)==sin(theta),0,pi/2)
///

<html><span class="math">0.785398163397</span></html>
```



```
id=5|
pi.n()/4
///

<html><span class="math">0.785398163397448</span></html>
```



```
id=6|

///
```


Issue created by migration from https://trac.sagemath.org/ticket/4457





---

archive/issue_comments_032811.json:
```json
{
    "body": "I've made a patch for this against the Sphinx version of the reference manual.\n\nThe output can be found at http://sage.math.washington.edu/home/mhansen/sage/devel/sage/doc/output/html/en/tutorial/tour_algebra.html",
    "created_at": "2009-01-24T10:18:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4457#issuecomment-32811",
    "user": "https://github.com/mwhansen"
}
```

I've made a patch for this against the Sphinx version of the reference manual.

The output can be found at http://sage.math.washington.edu/home/mhansen/sage/devel/sage/doc/output/html/en/tutorial/tour_algebra.html



---

archive/issue_comments_032812.json:
```json
{
    "body": "Changing assignee from tba to @mwhansen.",
    "created_at": "2009-01-24T10:18:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4457#issuecomment-32812",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from tba to @mwhansen.



---

archive/issue_comments_032813.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-24T10:18:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4457#issuecomment-32813",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_032814.json:
```json
{
    "body": "Attachment [trac_4457.patch](tarball://root/attachments/some-uuid/ticket4457/trac_4457.patch) by @mwhansen created at 2009-01-24 10:20:16",
    "created_at": "2009-01-24T10:20:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4457#issuecomment-32814",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_4457.patch](tarball://root/attachments/some-uuid/ticket4457/trac_4457.patch) by @mwhansen created at 2009-01-24 10:20:16



---

archive/issue_comments_032815.json:
```json
{
    "body": "The output looks great and the patch appears fine (modulo my understanding of Sphinx). I did not try to apply it though.",
    "created_at": "2009-01-24T13:31:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4457#issuecomment-32815",
    "user": "https://github.com/wdjoyner"
}
```

The output looks great and the patch appears fine (modulo my understanding of Sphinx). I did not try to apply it though.



---

archive/issue_comments_032816.json:
```json
{
    "body": "I think that's fine.  We can just move it to the Sphinx milestone and close it then.",
    "created_at": "2009-01-24T13:32:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4457#issuecomment-32816",
    "user": "https://github.com/mwhansen"
}
```

I think that's fine.  We can just move it to the Sphinx milestone and close it then.



---

archive/issue_events_004703.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-02-24T17:55:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4457",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4457#event-4703"
}
```



---

archive/issue_comments_032817.json:
```json
{
    "body": "Fixed in Sage 3.4.alpha0 by merging #3479.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-24T17:55:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4457#issuecomment-32817",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed in Sage 3.4.alpha0 by merging #3479.

Cheers,

Michael



---

archive/issue_comments_032818.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-24T17:55:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4457#issuecomment-32818",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
