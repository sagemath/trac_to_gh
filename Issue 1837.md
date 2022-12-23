# Issue 1837: [with patch] pass through options from groebner_basis

archive/issues_001837.json:
```json
{
    "body": "Assignee: malb\n\nNow this has an effect:\n\n```\nsage: sr = mq.SR()\nsage: F,s = sr.polynomial_system()\nsage: F.groebner_basis(redSB=False)\n[(a)*k002 + (a^2)*k003 + 1, k001 + (a^2 + 1)*k002 + (a^3 + a + 1), k000 + (a^3 + a^2 + 1)*k003 + (a^3 + a^2 + a), (a^2)*s003 + (a^3 + a^2)*k003 + (a + 1), s002 + (a^2)*k002 + (a), s001 + (a)*k001 + (a^2 + 1), s000 + (a^2 + 1)*k000 + (a + 1), w103 + k003 + (a^3 + a^2 + 1), w102 + k002 + (a^3 + 1), w101 + k001 + (a^3 + a + 1), w100 + k000 + (a^3 + a^2 + a), (a^2)*x103 + (a^2)*s003 + (a + 1), x102 + s002 + (a), x101 + (a^3 + a + 1)*x102 + (a^3 + 1)*x103 + s001 + (a^3 + a + 1)*s002 + (a^3 + 1)*s003 + (a), x100 + (a^3)*x101 + (a + 1)*x102 + (a + 1)*x103 + s000 + (a^3)*s001 + (a + 1)*s002 + (a + 1)*s003 + (a^2 + a + 1), k103 + s000 + (a^3)*s001 + (a + 1)*s002 + (a + 1)*s003 + (a^2 + a), k102 + (a^3 + a)*s000 + (a^2)*s001 + (a^2)*s002 + s003 + (a^2 + a + 1), k101 + (a)*s000 + (a)*s001 + s002 + (a^3 + a^2 + a + 1)*s003 + (a^2 + a), k100 + (a^2 + 1)*s000 + s001 + (a^3 + a^2)*s002 + (a^2 + 1)*s003 + (a^2 + a + 1), k003^2 + k000]\n\nsage: F.groebner_basis(redSB=True)\n[(a)*k002 + (a^2)*k003 + 1, (a)*k001 + (a^2 + a + 1)*k003, k000 + (a^3 + a^2 + 1)*k003 + (a^3 + a^2 + a), (a^2)*s003 + (a^3 + a^2)*k003 + (a + 1), (a)*s002 + (a + 1)*k003, s001 + (a^2 + a + 1)*k003 + (a^2 + 1), s000 + (a^3 + a^2)*k003, w103 + k003 + (a^3 + a^2 + 1), w102 + (a)*k003, (a)*w101 + (a^2 + a + 1)*k003 + (a^2 + 1), w100 + (a^3 + a^2 + 1)*k003, x103 + (a + 1)*k003, (a)*x102 + (a + 1)*k003 + (a^2), (a^3)*x101 + (a^3 + a^2 + 1)*k003, (a^2)*x100 + (a^2 + 1)*k003 + (a^3 + a^2), (a^3)*k103 + k003 + (a^2 + a), (a^3)*k102 + (a^2 + a + 1)*k003 + (a^2 + a), (a^3)*k101 + k003 + (a^3 + a^2 + a), (a^3)*k100 + (a^2 + a + 1)*k003 + (a^3 + a^2 + a), k003^2 + (a^3 + a^2 + 1)*k003 + (a^3 + a^2 + a)]\n```\n\n\nThis is not equivalent to #1396 because this isn't unified yet.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1837\n\n",
    "created_at": "2008-01-18T19:53:57Z",
    "labels": [
        "commutative algebra",
        "minor",
        "enhancement"
    ],
    "title": "[with patch] pass through options from groebner_basis",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1837",
    "user": "malb"
}
```
Assignee: malb

Now this has an effect:

```
sage: sr = mq.SR()
sage: F,s = sr.polynomial_system()
sage: F.groebner_basis(redSB=False)
[(a)*k002 + (a^2)*k003 + 1, k001 + (a^2 + 1)*k002 + (a^3 + a + 1), k000 + (a^3 + a^2 + 1)*k003 + (a^3 + a^2 + a), (a^2)*s003 + (a^3 + a^2)*k003 + (a + 1), s002 + (a^2)*k002 + (a), s001 + (a)*k001 + (a^2 + 1), s000 + (a^2 + 1)*k000 + (a + 1), w103 + k003 + (a^3 + a^2 + 1), w102 + k002 + (a^3 + 1), w101 + k001 + (a^3 + a + 1), w100 + k000 + (a^3 + a^2 + a), (a^2)*x103 + (a^2)*s003 + (a + 1), x102 + s002 + (a), x101 + (a^3 + a + 1)*x102 + (a^3 + 1)*x103 + s001 + (a^3 + a + 1)*s002 + (a^3 + 1)*s003 + (a), x100 + (a^3)*x101 + (a + 1)*x102 + (a + 1)*x103 + s000 + (a^3)*s001 + (a + 1)*s002 + (a + 1)*s003 + (a^2 + a + 1), k103 + s000 + (a^3)*s001 + (a + 1)*s002 + (a + 1)*s003 + (a^2 + a), k102 + (a^3 + a)*s000 + (a^2)*s001 + (a^2)*s002 + s003 + (a^2 + a + 1), k101 + (a)*s000 + (a)*s001 + s002 + (a^3 + a^2 + a + 1)*s003 + (a^2 + a), k100 + (a^2 + 1)*s000 + s001 + (a^3 + a^2)*s002 + (a^2 + 1)*s003 + (a^2 + a + 1), k003^2 + k000]

sage: F.groebner_basis(redSB=True)
[(a)*k002 + (a^2)*k003 + 1, (a)*k001 + (a^2 + a + 1)*k003, k000 + (a^3 + a^2 + 1)*k003 + (a^3 + a^2 + a), (a^2)*s003 + (a^3 + a^2)*k003 + (a + 1), (a)*s002 + (a + 1)*k003, s001 + (a^2 + a + 1)*k003 + (a^2 + 1), s000 + (a^3 + a^2)*k003, w103 + k003 + (a^3 + a^2 + 1), w102 + (a)*k003, (a)*w101 + (a^2 + a + 1)*k003 + (a^2 + 1), w100 + (a^3 + a^2 + 1)*k003, x103 + (a + 1)*k003, (a)*x102 + (a + 1)*k003 + (a^2), (a^3)*x101 + (a^3 + a^2 + 1)*k003, (a^2)*x100 + (a^2 + 1)*k003 + (a^3 + a^2), (a^3)*k103 + k003 + (a^2 + a), (a^3)*k102 + (a^2 + a + 1)*k003 + (a^2 + a), (a^3)*k101 + k003 + (a^3 + a^2 + a), (a^3)*k100 + (a^2 + a + 1)*k003 + (a^3 + a^2 + a), k003^2 + (a^3 + a^2 + 1)*k003 + (a^3 + a^2 + a)]
```


This is not equivalent to #1396 because this isn't unified yet.

Issue created by migration from https://trac.sagemath.org/ticket/1837





---

archive/issue_comments_011627.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-01-18T19:54:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1837#issuecomment-11627",
    "user": "malb"
}
```

Attachment



---

archive/issue_comments_011628.json:
```json
{
    "body": "Patch looks good to me.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-22T00:07:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1837#issuecomment-11628",
    "user": "mabshoff"
}
```

Patch looks good to me.

Cheers,

Michael



---

archive/issue_comments_011629.json:
```json
{
    "body": "But there is some trouble applying it: \n\nhunk 1 has a reject, but that is easily fixed, see http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/alpha1/groebner-kwds-hunk-1.patch\n\nhunk 2 seems unrelated to the patch and I cannot find anything remotely similar that this part of the patch would apply against:\n\n```\n537\t537\t            singular = S.parent() \n538\t538\t            ov = singular.option(\"get\") \n539\t539\t            singular.option(\"redSB\") # make sure we always compute reduced bases \n \t540\t \n \t541\t            for o,v in kwds.iteritems(): \n \t542\t                if v: \n \t543\t                    singular.option(o) \n \t544\t                     \n \t545\t                else: \n \t546\t                    singular.option(\"no\"+o) \n540\t547\t \n541\t548\t            if algorithm==\"groebner\": \n542\t549\t                S = S.groebner() \n```\n\n\nhunk 3 & 4 work as expected, with slight fuzz. See http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/alpha1/groebner-kwds.patch\n\nI am doctesting the resulting merge at the moment. Please let me know if hunk #2 was a mistake in which case I will close this ticket, assuming the doctests pass.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-22T00:29:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1837#issuecomment-11629",
    "user": "mabshoff"
}
```

But there is some trouble applying it: 

hunk 1 has a reject, but that is easily fixed, see http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/alpha1/groebner-kwds-hunk-1.patch

hunk 2 seems unrelated to the patch and I cannot find anything remotely similar that this part of the patch would apply against:

```
537	537	            singular = S.parent() 
538	538	            ov = singular.option("get") 
539	539	            singular.option("redSB") # make sure we always compute reduced bases 
 	540	 
 	541	            for o,v in kwds.iteritems(): 
 	542	                if v: 
 	543	                    singular.option(o) 
 	544	                     
 	545	                else: 
 	546	                    singular.option("no"+o) 
540	547	 
541	548	            if algorithm=="groebner": 
542	549	                S = S.groebner() 
```


hunk 3 & 4 work as expected, with slight fuzz. See http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/alpha1/groebner-kwds.patch

I am doctesting the resulting merge at the moment. Please let me know if hunk #2 was a mistake in which case I will close this ticket, assuming the doctests pass.

Cheers,

Michael



---

archive/issue_comments_011630.json:
```json
{
    "body": "Doctests pass, so I am closing this.\n\nmalb: Please reopen the ticket if it turns out that the second hunk wasn't included by mistake. I will release 2.10.1.alpha1 very shortly, so you can use that as a base to patch things up.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-22T01:23:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1837#issuecomment-11630",
    "user": "mabshoff"
}
```

Doctests pass, so I am closing this.

malb: Please reopen the ticket if it turns out that the second hunk wasn't included by mistake. I will release 2.10.1.alpha1 very shortly, so you can use that as a base to patch things up.

Cheers,

Michael



---

archive/issue_comments_011631.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-22T01:24:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1837#issuecomment-11631",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_011632.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha1",
    "created_at": "2008-01-22T01:24:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1837#issuecomment-11632",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.alpha1



---

archive/issue_comments_011633.json:
```json
{
    "body": "I'll check as soon as I get my hands on alpha1",
    "created_at": "2008-01-22T11:49:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1837",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1837#issuecomment-11633",
    "user": "malb"
}
```

I'll check as soon as I get my hands on alpha1
