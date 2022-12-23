# Issue 6999: [with patch, needs review] doctest failures on 32-bit systems due to #4948 patches

archive/issues_006999.json:
```json
{
    "body": "Assignee: flawrence\n\nSome doctests added in the patches for #4948 fail on 32-bit systems:\n\n```\nsage -t -long \"devel/sage/sage/interfaces/expect.py\" \n********************************************************************** \nFile \"/space/wstein/farm/sage-4.1.2.alpha2/devel/sage/sage/interfaces/expect.py\" , \nline 1599: \n    sage: gp(10.^80)._sage_repr() \nExpected nothing \nGot: \n    '1.000000000000000000000000000e80' \n********************************************************************** \n1 items had failures: \n   1 of   3 in __main__.example_45 \n***Test Failed*** 1 failures. \nFor whitespace errors, see the file \n/space/wstein/farm/sage-4.1.2.alpha2/tmp/.doctest_expect.py \n         [17.4 s] \nsage -t -long \"devel/sage/sage/interfaces/all.py\" \n         [0.1 s] \nsage -t -long \"devel/sage/sage/interfaces/rubik.py\" \n         [37.8 s] \nsage -t -long \"devel/sage/sage/interfaces/gp.py\" \n********************************************************************** \nFile \"/space/wstein/farm/sage-4.1.2.alpha2/devel/sage/sage/interfaces/gp.py\", \nline 567: \n    sage: repr(gp(10.^80)).replace(gp._exponent_symbol(), 'e') \nExpected nothing \nGot: \n    '1.000000000000000000000000000e80' \n********************************************************************** \n1 items had failures: \n   1 of   4 in __main__.example_26 \n***Test Failed*** 1 failures. \nFor whitespace errors, see the file \n/space/wstein/farm/sage-4.1.2.alpha2/tmp/.doctest_gp.py \n         [3.5 s] \n---------------------------------------------------------------------- \n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6999\n\n",
    "created_at": "2009-09-23T04:00:14Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] doctest failures on 32-bit systems due to #4948 patches",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6999",
    "user": "flawrence"
}
```
Assignee: flawrence

Some doctests added in the patches for #4948 fail on 32-bit systems:

```
sage -t -long "devel/sage/sage/interfaces/expect.py" 
********************************************************************** 
File "/space/wstein/farm/sage-4.1.2.alpha2/devel/sage/sage/interfaces/expect.py" , 
line 1599: 
    sage: gp(10.^80)._sage_repr() 
Expected nothing 
Got: 
    '1.000000000000000000000000000e80' 
********************************************************************** 
1 items had failures: 
   1 of   3 in __main__.example_45 
***Test Failed*** 1 failures. 
For whitespace errors, see the file 
/space/wstein/farm/sage-4.1.2.alpha2/tmp/.doctest_expect.py 
         [17.4 s] 
sage -t -long "devel/sage/sage/interfaces/all.py" 
         [0.1 s] 
sage -t -long "devel/sage/sage/interfaces/rubik.py" 
         [37.8 s] 
sage -t -long "devel/sage/sage/interfaces/gp.py" 
********************************************************************** 
File "/space/wstein/farm/sage-4.1.2.alpha2/devel/sage/sage/interfaces/gp.py", 
line 567: 
    sage: repr(gp(10.^80)).replace(gp._exponent_symbol(), 'e') 
Expected nothing 
Got: 
    '1.000000000000000000000000000e80' 
********************************************************************** 
1 items had failures: 
   1 of   4 in __main__.example_26 
***Test Failed*** 1 failures. 
For whitespace errors, see the file 
/space/wstein/farm/sage-4.1.2.alpha2/tmp/.doctest_gp.py 
         [3.5 s] 
---------------------------------------------------------------------- 
```



Issue created by migration from https://trac.sagemath.org/ticket/6999





---

archive/issue_comments_057876.json:
```json
{
    "body": "Attachment\n\nWorks ok for me on 32 bit. So positive review.\n\nJaap",
    "created_at": "2009-09-23T20:59:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6999#issuecomment-57876",
    "user": "jsp"
}
```

Attachment

Works ok for me on 32 bit. So positive review.

Jaap



---

archive/issue_comments_057877.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-24T07:18:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6999#issuecomment-57877",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_057878.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T09:59:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6999",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6999#issuecomment-57878",
    "user": "mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
