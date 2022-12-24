# Issue 4457: tutorial: add find_root()  to "2.4.1 Solving Equations"

archive/issues_004457.json:
```json
{
    "body": "Assignee: tba\n\nCurrently, the section in the tutorial on solving equations refers only to analytical solutions, which are found using \"solve().\"  When solve fails, it may be worth using a numerical solution.  \n\nFor equations with a single variable, this can be done using find_root().  It will save new users time to find \"find_root()\" mentioned with \"solve()\" in the section on solving equations.\n\nExamples:\n\n```\nid=1|\nvar('theta')\n///\n\n<html><span class=\"math\">\\theta</span></html>\n```\n\n\n\n```\nid=2|\nsolve(theta^2 + 1==4)\n///\n\n<html><span class=\"math\">\\left[\\theta  =  -\\sqrt{ 3 }, \n \\theta  =  \\sqrt{ 3 }\\right]</span></html>\n```\n\n\n\n```\nid=3|\nsolve(cos(theta)==sin(theta))\n///\n\n<html><span class=\"math\">\\left[\\sin \\left( \\theta \\right)  =  \\cos \\left( \\theta \\right)\\right]</span></html>\n```\n\n\n\n```\nid=4|\nfind_root(cos(theta)==sin(theta),0,pi/2)\n///\n\n<html><span class=\"math\">0.785398163397</span></html>\n```\n\n\n\n```\nid=5|\npi.n()/4\n///\n\n<html><span class=\"math\">0.785398163397448</span></html>\n```\n\n\n\n```\nid=6|\n\n///\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4457\n\n",
    "created_at": "2008-11-06T23:54:51Z",
    "labels": [
        "documentation",
        "major",
        "enhancement"
    ],
    "title": "tutorial: add find_root()  to \"2.4.1 Solving Equations\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4457",
    "user": "dhbradshaw"
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

archive/issue_comments_032875.json:
```json
{
    "body": "I've made a patch for this against the Sphinx version of the reference manual.\n\nThe output can be found at http://sage.math.washington.edu/home/mhansen/sage/devel/sage/doc/output/html/en/tutorial/tour_algebra.html",
    "created_at": "2009-01-24T10:18:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4457#issuecomment-32875",
    "user": "mhansen"
}
```

I've made a patch for this against the Sphinx version of the reference manual.

The output can be found at http://sage.math.washington.edu/home/mhansen/sage/devel/sage/doc/output/html/en/tutorial/tour_algebra.html



---

archive/issue_comments_032876.json:
```json
{
    "body": "Changing assignee from tba to mhansen.",
    "created_at": "2009-01-24T10:18:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4457#issuecomment-32876",
    "user": "mhansen"
}
```

Changing assignee from tba to mhansen.



---

archive/issue_comments_032877.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-24T10:18:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4457#issuecomment-32877",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_032878.json:
```json
{
    "body": "Attachment [trac_4457.patch](tarball://root/attachments/some-uuid/ticket4457/trac_4457.patch) by mhansen created at 2009-01-24 10:20:16",
    "created_at": "2009-01-24T10:20:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4457#issuecomment-32878",
    "user": "mhansen"
}
```

Attachment [trac_4457.patch](tarball://root/attachments/some-uuid/ticket4457/trac_4457.patch) by mhansen created at 2009-01-24 10:20:16



---

archive/issue_comments_032879.json:
```json
{
    "body": "The output looks great and the patch appears fine (modulo my understanding of Sphinx). I did not try to apply it though.",
    "created_at": "2009-01-24T13:31:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4457#issuecomment-32879",
    "user": "wdj"
}
```

The output looks great and the patch appears fine (modulo my understanding of Sphinx). I did not try to apply it though.



---

archive/issue_comments_032880.json:
```json
{
    "body": "I think that's fine.  We can just move it to the Sphinx milestone and close it then.",
    "created_at": "2009-01-24T13:32:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4457#issuecomment-32880",
    "user": "mhansen"
}
```

I think that's fine.  We can just move it to the Sphinx milestone and close it then.



---

archive/issue_comments_032881.json:
```json
{
    "body": "Fixed in Sage 3.4.alpha0 by merging #3479.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-24T17:55:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4457#issuecomment-32881",
    "user": "mabshoff"
}
```

Fixed in Sage 3.4.alpha0 by merging #3479.

Cheers,

Michael



---

archive/issue_comments_032882.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-24T17:55:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4457",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4457#issuecomment-32882",
    "user": "mabshoff"
}
```

Resolution: fixed
