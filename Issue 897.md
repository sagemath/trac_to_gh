# Issue 897: number_of_partitions -- now broken on OS X PPC

archive/issues_000897.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  sage-combinat\n\nOn OS X PPC with the new number_of_partitions optimized code:\n\n\n```\nfermat:~/sage-2.8.7.rc1 was$ ./sage -t  devel/sage-main/sage/combinat/combinat.py\nsage -t  devel/sage-main/sage/combinat/combinat.py          *******************************************\n***************************  \nFile \"combinat.py\", line 1843:\n    sage: number_of_partitions(100000)\nExpected:\n    274935105697756965126775163209863526881734293159800547582031259843021473281149641730550507416607366\n2159015784477429624894049306307020046179276449303351011607934245719015571894350972531246610845200636955\n8934464248716828789832182345009262853831404597021307130674510624419227311238999702284408609370935531629\n697851569569892196108480158600569421098519\nGot:\n    274935105697756965126775163209863526881734293159800547582031259843021473281149641730550507416607366\n2159015784477429624894049306307020046179276449303351011607934245719015571894350972531246610845200636955\n8934464248716828789832182345009262853831404597021307130674510624419227311238999702284408609370935531629\n697851569569892196108480158600569420104082\n**********************************************************************\nFile \"combinat.py\", line 1867:\n    sage: number_of_partitions( n - (n % 385) + 369) % 385 == 0\nExpected:\n    True\nGot:\n    False\n**********************************************************************\nFile \"combinat.py\", line 1870:\n    sage: number_of_partitions( n - (n % 385) + 369) % 385 == 0\nExpected:\n    True\nGot:\n    False\n\n```\n\n\nThe code works on everything else, i.e., all x86 machines. \n\nIssue created by migration from https://trac.sagemath.org/ticket/897\n\n",
    "created_at": "2007-10-14T20:35:28Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.7",
    "title": "number_of_partitions -- now broken on OS X PPC",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/897",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  sage-combinat

On OS X PPC with the new number_of_partitions optimized code:


```
fermat:~/sage-2.8.7.rc1 was$ ./sage -t  devel/sage-main/sage/combinat/combinat.py
sage -t  devel/sage-main/sage/combinat/combinat.py          *******************************************
***************************  
File "combinat.py", line 1843:
    sage: number_of_partitions(100000)
Expected:
    274935105697756965126775163209863526881734293159800547582031259843021473281149641730550507416607366
2159015784477429624894049306307020046179276449303351011607934245719015571894350972531246610845200636955
8934464248716828789832182345009262853831404597021307130674510624419227311238999702284408609370935531629
697851569569892196108480158600569421098519
Got:
    274935105697756965126775163209863526881734293159800547582031259843021473281149641730550507416607366
2159015784477429624894049306307020046179276449303351011607934245719015571894350972531246610845200636955
8934464248716828789832182345009262853831404597021307130674510624419227311238999702284408609370935531629
697851569569892196108480158600569420104082
**********************************************************************
File "combinat.py", line 1867:
    sage: number_of_partitions( n - (n % 385) + 369) % 385 == 0
Expected:
    True
Got:
    False
**********************************************************************
File "combinat.py", line 1870:
    sage: number_of_partitions( n - (n % 385) + 369) % 385 == 0
Expected:
    True
Got:
    False

```


The code works on everything else, i.e., all x86 machines. 

Issue created by migration from https://trac.sagemath.org/ticket/897





---

archive/issue_comments_005502.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2007-10-14T20:35:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/897#issuecomment-5502",
    "user": "https://github.com/williamstein"
}
```

Changing priority from major to critical.



---

archive/issue_comments_005503.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-14T22:53:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/897#issuecomment-5503",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_005504.json:
```json
{
    "body": "It was always broken on OS X!\n\nAnyway, I've patched this up for the release, but more work needs to be done...",
    "created_at": "2007-10-14T22:53:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/897#issuecomment-5504",
    "user": "https://github.com/williamstein"
}
```

It was always broken on OS X!

Anyway, I've patched this up for the release, but more work needs to be done...



---

archive/issue_comments_005505.json:
```json
{
    "body": "ok, everything is all fixed for sage-2.8.7.",
    "created_at": "2007-10-15T00:33:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/897#issuecomment-5505",
    "user": "https://github.com/williamstein"
}
```

ok, everything is all fixed for sage-2.8.7.
