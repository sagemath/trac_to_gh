# Issue 4715: Small bug in KodairaSymbol

archive/issues_004715.json:
```json
{
    "body": "Assignee: was\n\nCC:  tnagel\n\n#4412 had a buglet:  for Kodaira Class Im the _roman field was not being set (it should be 1).  This is only currently used in the tamagawa_exponent() function for elliptic curves over number fields.\n\nOne-line patch coming up, plus a corresponding doctest.\n\nThis was reported by Tobias Nagel:\n\n```\nsage: E=EllipticCurve('117a3');                        \nsage: E.tamagawa_exponent(13)\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/home/tobi/test_Sint/<ipython console> in <module>()\n\n/home/tobi/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.pyc in tamagawa_exponent(self, p)\n 2190             return cp\n 2191         ks = self.kodaira_type(p)\n-> 2192         if ks._roman==1 and ks._n%2==0 and ks._starred:\n 2193             return 2\n 2194         return 4\n\nAttributeError: 'KodairaSymbol_class' object has no attribute '_roman'\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4715\n\n",
    "created_at": "2008-12-05T11:58:25Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "title": "Small bug in KodairaSymbol",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4715",
    "user": "cremona"
}
```
Assignee: was

CC:  tnagel

#4412 had a buglet:  for Kodaira Class Im the _roman field was not being set (it should be 1).  This is only currently used in the tamagawa_exponent() function for elliptic curves over number fields.

One-line patch coming up, plus a corresponding doctest.

This was reported by Tobias Nagel:

```
sage: E=EllipticCurve('117a3');                        
sage: E.tamagawa_exponent(13)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/tobi/test_Sint/<ipython console> in <module>()

/home/tobi/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.pyc in tamagawa_exponent(self, p)
 2190             return cp
 2191         ks = self.kodaira_type(p)
-> 2192         if ks._roman==1 and ks._n%2==0 and ks._starred:
 2193             return 2
 2194         return 4

AttributeError: 'KodairaSymbol_class' object has no attribute '_roman'
```



Issue created by migration from https://trac.sagemath.org/ticket/4715





---

archive/issue_comments_035570.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-12-05T12:02:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4715#issuecomment-35570",
    "user": "cremona"
}
```

Attachment



---

archive/issue_comments_035571.json:
```json
{
    "body": "There's another problem, watch this space:\n\n```\nsage: E=EllipticCurve('153c2')\nsage: E.tamagawa_exponent(3)\n<boom>\n```\n",
    "created_at": "2008-12-05T12:17:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4715#issuecomment-35571",
    "user": "cremona"
}
```

There's another problem, watch this space:

```
sage: E=EllipticCurve('153c2')
sage: E.tamagawa_exponent(3)
<boom>
```




---

archive/issue_comments_035572.json:
```json
{
    "body": "Attachment\n\nFixing that also showed up the following completely independent bug (only on 32-bit machines though):\n\n```\nsage: E=EllipticCurve('903b3')\nsage: E.pari_curve()\n<boom> (PariError: precision too low)\n```\n\n\nThe second patch fixes that as well as the other (which only applied to type I*0).  Now I have checked tamagawa_index() for all curves in the database up to conductor 10000 and all bad primes for each, so I hope that's that.\n\nTo fix the pari precision problem I did a try/except which keeps doubling the precision until it's ok.  I hope that is not against the rules:  if pari's ellinit every crashes for a reason other than precision, this would be an infinite loop.\n\nIn the course of this testing I found that looping through thousands of curves ate up a lot of memory.  I made a change so that for curves over QQ, local_data() uses prime integers arther than prime ideals, and that helps a bit, but there is still more memory begin eaten up than I would like.  For example:\n\n```\nsage: for e in cremona_curves(srange(11,10000)):\n    for p in e.conductor().support():\n        ld = e.local_data(p)\n        print e.cremona_label()   \n```\n\nOn my machine the used RAM creeps up gradually, hits 1GB at around conductor 2400, and if I let it continue it starts to make my machine really suffer at 1.7GB (no prizes for guessing the amount of RAM I have).\n\nThis might deserve a separate ticket.",
    "created_at": "2008-12-05T13:44:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4715#issuecomment-35572",
    "user": "cremona"
}
```

Attachment

Fixing that also showed up the following completely independent bug (only on 32-bit machines though):

```
sage: E=EllipticCurve('903b3')
sage: E.pari_curve()
<boom> (PariError: precision too low)
```


The second patch fixes that as well as the other (which only applied to type I*0).  Now I have checked tamagawa_index() for all curves in the database up to conductor 10000 and all bad primes for each, so I hope that's that.

To fix the pari precision problem I did a try/except which keeps doubling the precision until it's ok.  I hope that is not against the rules:  if pari's ellinit every crashes for a reason other than precision, this would be an infinite loop.

In the course of this testing I found that looping through thousands of curves ate up a lot of memory.  I made a change so that for curves over QQ, local_data() uses prime integers arther than prime ideals, and that helps a bit, but there is still more memory begin eaten up than I would like.  For example:

```
sage: for e in cremona_curves(srange(11,10000)):
    for p in e.conductor().support():
        ld = e.local_data(p)
        print e.cremona_label()   
```

On my machine the used RAM creeps up gradually, hits 1GB at around conductor 2400, and if I let it continue it starts to make my machine really suffer at 1.7GB (no prizes for guessing the amount of RAM I have).

This might deserve a separate ticket.



---

archive/issue_comments_035573.json:
```json
{
    "body": "Hi John,\n\nplease open a ticket for the memory issues/leaks you are seeing. We are current chasing a number of leaks, most of which seem coercion related.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-05T18:42:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4715#issuecomment-35573",
    "user": "mabshoff"
}
```

Hi John,

please open a ticket for the memory issues/leaks you are seeing. We are current chasing a number of leaks, most of which seem coercion related.

Cheers,

Michael



---

archive/issue_comments_035574.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-07T09:07:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4715#issuecomment-35574",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_035575.json:
```json
{
    "body": "Merged both patches in Sage 3.2.2.alpha1",
    "created_at": "2008-12-07T09:07:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4715#issuecomment-35575",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.2.2.alpha1



---

archive/issue_comments_035576.json:
```json
{
    "body": "In #9931, I plan to revert this ticket's patch to `sage/schemes/elliptic_curves/ell_rational_field.py`, since the workaround seems not needed anymore.",
    "created_at": "2010-09-19T09:34:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4715",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4715#issuecomment-35576",
    "user": "jdemeyer"
}
```

In #9931, I plan to revert this ticket's patch to `sage/schemes/elliptic_curves/ell_rational_field.py`, since the workaround seems not needed anymore.
