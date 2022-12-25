# Issue 9322: bug in simon_two_descent for elliptic curves

archive/issues_009322.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @categorie jeremywest\n\n[NB This is a different bug from the one on #5153]\n\nChris Wuthrich reports:\n\n```\nsage: K.<w> = NumberField(x^2-x-232)\nsage: E = EllipticCurve([2-w,18+3*w,209+9*w,2581+175*w,852-55*w])\nsage: E.local_data()\n[]\nsage: E.simon_two_descent(verbose=2)\nbooom.\n```\n\n\nThe same example runs fine in gp using the same version of the script ell.gp that Sage has (in version 4.4.4) and the same version of gp.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9322\n\n",
    "created_at": "2010-06-24T03:00:39Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.2",
    "title": "bug in simon_two_descent for elliptic curves",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9322",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @aghitza

CC:  @categorie jeremywest

[NB This is a different bug from the one on #5153]

Chris Wuthrich reports:

```
sage: K.<w> = NumberField(x^2-x-232)
sage: E = EllipticCurve([2-w,18+3*w,209+9*w,2581+175*w,852-55*w])
sage: E.local_data()
[]
sage: E.simon_two_descent(verbose=2)
booom.
```


The same example runs fine in gp using the same version of the script ell.gp that Sage has (in version 4.4.4) and the same version of gp.

Issue created by migration from https://trac.sagemath.org/ticket/9322





---

archive/issue_comments_087748.json:
```json
{
    "body": "\n```\n\njohn@ubuntu%sage -gp\n                  GP/PARI CALCULATOR Version 2.3.5 (released)\n...\n\n? bnf=bnfinit(y^2-y-232);\n? w=Mod(y,y^2-y-232)\n%8 = Mod(y, y^2 - y - 232)\n? e=ellinit([2-w,18+3*w,209+9*w,2581+175*w,852-55*w]);\n? bnfellrank(bnf,e)\ncourbe elliptique : Y^2 = x^3 + Mod(9*y + 308, y^2 - y - 232)*x^2 + Mod(1200*y + 27936, y^2 - y - 232)*x + Mod(57968*y + 1054096, y^2 - y - 232)\npoints triviaux sur la courbe = [[1, 1, 0]]\n#S(E/K)[2]    = 4\n#E(K)/2E(K)  >= 1\n#III(E/K)[2] <= 4\nrang(E/K)    >= 0\nlistpointsmwr = []\n%10 = [0, 2, []]\n```\n",
    "created_at": "2010-06-24T03:02:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9322#issuecomment-87748",
    "user": "https://github.com/JohnCremona"
}
```


```

john@ubuntu%sage -gp
                  GP/PARI CALCULATOR Version 2.3.5 (released)
...

? bnf=bnfinit(y^2-y-232);
? w=Mod(y,y^2-y-232)
%8 = Mod(y, y^2 - y - 232)
? e=ellinit([2-w,18+3*w,209+9*w,2581+175*w,852-55*w]);
? bnfellrank(bnf,e)
courbe elliptique : Y^2 = x^3 + Mod(9*y + 308, y^2 - y - 232)*x^2 + Mod(1200*y + 27936, y^2 - y - 232)*x + Mod(57968*y + 1054096, y^2 - y - 232)
points triviaux sur la courbe = [[1, 1, 0]]
#S(E/K)[2]    = 4
#E(K)/2E(K)  >= 1
#III(E/K)[2] <= 4
rang(E/K)    >= 0
listpointsmwr = []
%10 = [0, 2, []]
```




---

archive/issue_comments_087749.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-07-01T06:32:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9322#issuecomment-87749",
    "user": "https://trac.sagemath.org/admin/accounts/users/jeremywest"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_087750.json:
```json
{
    "body": "I also noticed this same problem, although it seems to be nearly ubiquitous for number fields. I found it for several quadratic and cubic extensions as well as for a degree seven extension. For one I got an index out of bounds error which I believe originates because gp does not hand back the results expected by the sage script. For the rest I found that the sage script was attempting to coerce a point from one curve to another and it reports that the point does not lie on the curve.\n\nUnfortunately, I don't currently have access to sage so I am unable to report line numbers. The problem occurs in sage/schemes/elliptic_curves/gp_simon.py near the bottom of the only function defined.",
    "created_at": "2010-07-01T06:32:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9322#issuecomment-87750",
    "user": "https://trac.sagemath.org/admin/accounts/users/jeremywest"
}
```

I also noticed this same problem, although it seems to be nearly ubiquitous for number fields. I found it for several quadratic and cubic extensions as well as for a degree seven extension. For one I got an index out of bounds error which I believe originates because gp does not hand back the results expected by the sage script. For the rest I found that the sage script was attempting to coerce a point from one curve to another and it reports that the point does not lie on the curve.

Unfortunately, I don't currently have access to sage so I am unable to report line numbers. The problem occurs in sage/schemes/elliptic_curves/gp_simon.py near the bottom of the only function defined.



---

archive/issue_events_022967.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/jeremywest",
    "created_at": "2010-07-01T06:32:20Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "milestone": "sage-4.5",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9322#event-22967"
}
```



---

archive/issue_comments_087751.json:
```json
{
    "body": "Changing component from algebra to elliptic curves.",
    "created_at": "2010-07-01T06:32:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9322#issuecomment-87751",
    "user": "https://trac.sagemath.org/admin/accounts/users/jeremywest"
}
```

Changing component from algebra to elliptic curves.



---

archive/issue_comments_087752.json:
```json
{
    "body": "With 4.7.alpha1 this works fine:\n\n```\nsage: K.<w> = NumberField(x^2-x-232)                                   \nsage: E = EllipticCurve([2-w,18+3*w,209+9*w,2581+175*w,852-55*w])      \nsage: E.local_data()                                                   \n[]\nsage: E.simon_two_descent()                                      \n(0, 2, [])\n```\n\nbut after #11005 (which updates to a newer version of Simon's GP scripts) we run into an infinite loop:\n\n```\n **** Warning: doubling the real precision in nfsign_s **** 76\n **** Warning: doubling the real precision in nfsign_s **** 152\n **** Warning: doubling the real precision in nfsign_s **** 76\n **** Warning: doubling the real precision in nfsign_s **** 152\n **** Warning: doubling the real precision in nfsign_s **** 76\n```\n\nwhich I will test on a stand-alone gp and report upstream.",
    "created_at": "2011-03-25T04:47:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9322#issuecomment-87752",
    "user": "https://github.com/JohnCremona"
}
```

With 4.7.alpha1 this works fine:

```
sage: K.<w> = NumberField(x^2-x-232)                                   
sage: E = EllipticCurve([2-w,18+3*w,209+9*w,2581+175*w,852-55*w])      
sage: E.local_data()                                                   
[]
sage: E.simon_two_descent()                                      
(0, 2, [])
```

but after #11005 (which updates to a newer version of Simon's GP scripts) we run into an infinite loop:

```
 **** Warning: doubling the real precision in nfsign_s **** 76
 **** Warning: doubling the real precision in nfsign_s **** 152
 **** Warning: doubling the real precision in nfsign_s **** 76
 **** Warning: doubling the real precision in nfsign_s **** 152
 **** Warning: doubling the real precision in nfsign_s **** 76
```

which I will test on a stand-alone gp and report upstream.



---

archive/issue_comments_087753.json:
```json
{
    "body": "Changing keywords from \"\" to \"Simon\".",
    "created_at": "2011-03-25T04:47:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9322#issuecomment-87753",
    "user": "https://github.com/JohnCremona"
}
```

Changing keywords from "" to "Simon".



---

archive/issue_comments_087754.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2011-03-25T04:47:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9322#issuecomment-87754",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_087755.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2011-03-25T04:54:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9322#issuecomment-87755",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_087756.json:
```json
{
    "body": "Running under gp directly:\n\n```\n? K = bnfinit(y^2 - y - 232);\n? a = Mod(y,K.pol);\n? bnfellrank(K, [-a + 2,3*a + 18,9*a + 209,175*a + 2581,-55*a + 852])\ncourbe elliptique : Y^2 = x^3 + Mod(9*y + 308, y^2 - y - 232)*x^2 + Mod(1200*y + 27936, y^2 - y - 232)*x + Mod(57968*y + 1054096, y^2 - y - 232)\npoints triviaux sur la courbe = [[1, 1, 0]]\n#S(E/K)[2]    = 4\n#E(K)/2E(K)  >= 2\n#III(E/K)[2] <= 2\nrang(E/K)    >= 1\n III devrait etre un carre, donc \n#E(K)/2E(K)  = 4\n#III(E/K)[2] = 1\nrang(E/K)    = 2\nlistpointsmwr = [[Mod(-35/4*y - 186, y^2 - y - 232), Mod(-21/8*y - 37, y^2 - y - 232)]]\n%71 = [2, 2, [[Mod(-35/16*y - 93/2, y^2 - y - 232), Mod(-1727/64*y - 2531/8, y^2 - y - 232)]]]\n```\n\nwe get instant success.  Also with the gp2c-compiled version.  So it is *not* an upstream problem,and one which should be solvable within Sage.",
    "created_at": "2011-03-25T04:54:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9322#issuecomment-87756",
    "user": "https://github.com/JohnCremona"
}
```

Running under gp directly:

```
? K = bnfinit(y^2 - y - 232);
? a = Mod(y,K.pol);
? bnfellrank(K, [-a + 2,3*a + 18,9*a + 209,175*a + 2581,-55*a + 852])
courbe elliptique : Y^2 = x^3 + Mod(9*y + 308, y^2 - y - 232)*x^2 + Mod(1200*y + 27936, y^2 - y - 232)*x + Mod(57968*y + 1054096, y^2 - y - 232)
points triviaux sur la courbe = [[1, 1, 0]]
#S(E/K)[2]    = 4
#E(K)/2E(K)  >= 2
#III(E/K)[2] <= 2
rang(E/K)    >= 1
 III devrait etre un carre, donc 
#E(K)/2E(K)  = 4
#III(E/K)[2] = 1
rang(E/K)    = 2
listpointsmwr = [[Mod(-35/4*y - 186, y^2 - y - 232), Mod(-21/8*y - 37, y^2 - y - 232)]]
%71 = [2, 2, [[Mod(-35/16*y - 93/2, y^2 - y - 232), Mod(-1727/64*y - 2531/8, y^2 - y - 232)]]]
```

we get instant success.  Also with the gp2c-compiled version.  So it is *not* an upstream problem,and one which should be solvable within Sage.



---

archive/issue_comments_087757.json:
```json
{
    "body": "I've been struggling with that bug for a few hours, and have made only little progress.\nWith Sage 4.7.1 and Pari 2.4.3 (development), I've noticed that Pari 2.4.3 and the version of Pari within Sage differ at `bbnf = bnfinit(rnfeq[1],1)` in `ell.gp`, where\n`rnfep[1] = x^6 + 625*x^5 + 135916*x^4 + 14984560*x^3 + 914453072*x^2 + 29502178560*x + 392635160576`.\n\nPari 2.4.3 returns `bbnf: [Mat(2), Mat([0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, ...` whereas\nPari within Sage returns `bbnf: [Mat(2), Mat([0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, ...`\n\nHowever I don't know if `bnfinit` should be deterministic...\n\nPaul",
    "created_at": "2011-09-14T15:59:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9322#issuecomment-87757",
    "user": "https://github.com/zimmermann6"
}
```

I've been struggling with that bug for a few hours, and have made only little progress.
With Sage 4.7.1 and Pari 2.4.3 (development), I've noticed that Pari 2.4.3 and the version of Pari within Sage differ at `bbnf = bnfinit(rnfeq[1],1)` in `ell.gp`, where
`rnfep[1] = x^6 + 625*x^5 + 135916*x^4 + 14984560*x^3 + 914453072*x^2 + 29502178560*x + 392635160576`.

Pari 2.4.3 returns `bbnf: [Mat(2), Mat([0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, ...` whereas
Pari within Sage returns `bbnf: [Mat(2), Mat([0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, ...`

However I don't know if `bnfinit` should be deterministic...

Paul



---

archive/issue_comments_087758.json:
```json
{
    "body": "is there a way to get the output of the print commands from the ell.gp script\nwhen it is called from within Sage? Even with a large value of DEBUGLEVEL_ell, the output\nof those print statements does not appear in the Sage session, thus it is difficult to debug.\n\nPaul",
    "created_at": "2011-09-15T15:25:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9322#issuecomment-87758",
    "user": "https://github.com/zimmermann6"
}
```

is there a way to get the output of the print commands from the ell.gp script
when it is called from within Sage? Even with a large value of DEBUGLEVEL_ell, the output
of those print statements does not appear in the Sage session, thus it is difficult to debug.

Paul



---

archive/issue_comments_087759.json:
```json
{
    "body": "Replying to [comment:6 zimmerma]:\n> is there a way to get the output of the print commands from the ell.gp script\n> when it is called from within Sage? Even with a large value of DEBUGLEVEL_ell, the output\n> of those print statements does not appear in the Sage session, thus it is difficult to debug.\n> \n> Paul\n\nYou can get a whole gp session logged to a file by setting gp=Gp(logfile=foobar.txt').  But the code in gp-simon.py creates its own gp instance without using the logfile option.  In the short term, edit line 38 of sage/sage/schemes/elliptic_curves/gp-simon.py to add the logfile option.  A better long-term solution would be to have a logfile parameter to the two-descent function itself and pass that on.\n\nBy the way, there are new version of Simon's scripts which in Sage Days in March (6 months ago!) I got working in a better way, using gp2c to convert to C code.  There was some reason which I now cannot remember why there was a delay in getting this merged, and after 6 months I fear that the patches we made then would no longer work.  Damn.  Anyway, I strongly suggest if you have problem cases that you run the curves directly through ell.gp (outside Sage) using the newest version of ell.gp from Simon's web page, since you may be seeing a problem which has already been fixed.",
    "created_at": "2011-09-15T15:50:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9322#issuecomment-87759",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:6 zimmerma]:
> is there a way to get the output of the print commands from the ell.gp script
> when it is called from within Sage? Even with a large value of DEBUGLEVEL_ell, the output
> of those print statements does not appear in the Sage session, thus it is difficult to debug.
> 
> Paul

You can get a whole gp session logged to a file by setting gp=Gp(logfile=foobar.txt').  But the code in gp-simon.py creates its own gp instance without using the logfile option.  In the short term, edit line 38 of sage/sage/schemes/elliptic_curves/gp-simon.py to add the logfile option.  A better long-term solution would be to have a logfile parameter to the two-descent function itself and pass that on.

By the way, there are new version of Simon's scripts which in Sage Days in March (6 months ago!) I got working in a better way, using gp2c to convert to C code.  There was some reason which I now cannot remember why there was a delay in getting this merged, and after 6 months I fear that the patches we made then would no longer work.  Damn.  Anyway, I strongly suggest if you have problem cases that you run the curves directly through ell.gp (outside Sage) using the newest version of ell.gp from Simon's web page, since you may be seeing a problem which has already been fixed.



---

archive/issue_comments_087760.json:
```json
{
    "body": "thank you John for your advice. After trying it, I figured out that with Sage 4.7.1 on my laptop\nin fact the example in the description actually works, but takes about 2.5 minutes, during which\ntop reports that the gp process takes 100% of the cpu time, while evaluating the command\n\n```\nans=bnfellrank(K, [-a + 2,3*a + 18,9*a + 209,175*a + 2581,-55*a + 852]);;\n```\n\nCan someone else confirm? Maybe a problem in the Sage-gp interface?\nWhat should we do with that ticket?\n\nPaul",
    "created_at": "2011-09-16T10:18:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9322#issuecomment-87760",
    "user": "https://github.com/zimmermann6"
}
```

thank you John for your advice. After trying it, I figured out that with Sage 4.7.1 on my laptop
in fact the example in the description actually works, but takes about 2.5 minutes, during which
top reports that the gp process takes 100% of the cpu time, while evaluating the command

```
ans=bnfellrank(K, [-a + 2,3*a + 18,9*a + 209,175*a + 2581,-55*a + 852]);;
```

Can someone else confirm? Maybe a problem in the Sage-gp interface?
What should we do with that ticket?

Paul



---

archive/issue_comments_087761.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2011-09-16T10:18:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9322#issuecomment-87761",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_087762.json:
```json
{
    "body": "Changing keywords from \"Simon\" to \"Simon ecc2011\".",
    "created_at": "2011-09-16T14:56:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9322#issuecomment-87762",
    "user": "https://github.com/zimmermann6"
}
```

Changing keywords from "Simon" to "Simon ecc2011".



---

archive/issue_comments_087763.json:
```json
{
    "body": "ok, I found where the problem comes from. In the file `ellQ.gp` which is also loaded by the\n`gp_simon.py` file, the global constants `LIM1, LIM3, LIMTRIV` have different values than\nin `ell.gp`, respectively 5, 50, 50 instead of 2, 4, 2.\n\nThe slow behaviour can be reproduced with `sage -gp` if one reads both `ell.gp`\n*and* `ellQ.gp`. If one only reads `ell.gp`, it is fast. Apparently `ellQ.gp` is not\nneeded for this computation.\n\nMoreover the default values in Sage are again different: 5, 50, 10.\n\nWith 5, 5, 10 it takes only 1.45s (wall clock time) on my laptop.\nWith 5, 10, 10 it takes 2.19s.\nWith 5, 20, 10 it takes 11.63s.\n\nNote that those values should be modified both in `ell_number_field.py` and in\n`gp_simon.py` (the former function is critical in this example).\n\nOne should also share the default values for `lim1, lim3, limtriv` between the\n`simon_two_descent` functions in `ell_number_field.py` and `gp_simon.py`.\n\nPaul",
    "created_at": "2011-09-16T14:56:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9322#issuecomment-87763",
    "user": "https://github.com/zimmermann6"
}
```

ok, I found where the problem comes from. In the file `ellQ.gp` which is also loaded by the
`gp_simon.py` file, the global constants `LIM1, LIM3, LIMTRIV` have different values than
in `ell.gp`, respectively 5, 50, 50 instead of 2, 4, 2.

The slow behaviour can be reproduced with `sage -gp` if one reads both `ell.gp`
*and* `ellQ.gp`. If one only reads `ell.gp`, it is fast. Apparently `ellQ.gp` is not
needed for this computation.

Moreover the default values in Sage are again different: 5, 50, 10.

With 5, 5, 10 it takes only 1.45s (wall clock time) on my laptop.
With 5, 10, 10 it takes 2.19s.
With 5, 20, 10 it takes 11.63s.

Note that those values should be modified both in `ell_number_field.py` and in
`gp_simon.py` (the former function is critical in this example).

One should also share the default values for `lim1, lim3, limtriv` between the
`simon_two_descent` functions in `ell_number_field.py` and `gp_simon.py`.

Paul



---

archive/issue_comments_087764.json:
```json
{
    "body": "In the other ticket on this we changed Simon's scripts so that the use of these \"environment variables\" for passing configuration parameters was replaced by actual parameters to the functions (with default values).  So this problem should go away then.  We also persuaded Simon not to have the same function name for different functions in his various script files (he even had the same name for two different an incompatible versions of functions to do the same thing!).",
    "created_at": "2011-09-26T09:14:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9322#issuecomment-87764",
    "user": "https://github.com/JohnCremona"
}
```

In the other ticket on this we changed Simon's scripts so that the use of these "environment variables" for passing configuration parameters was replaced by actual parameters to the functions (with default values).  So this problem should go away then.  We also persuaded Simon not to have the same function name for different functions in his various script files (he even had the same name for two different an incompatible versions of functions to do the same thing!).



---

archive/issue_events_022968.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "milestone": "sage-4.5",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9322#event-22968"
}
```



---

archive/issue_events_022969.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9322#event-22969"
}
```



---

archive/issue_comments_087765.json:
```json
{
    "body": "Changing keywords from \"Simon ecc2011\" to \"simon_two_descent ecc2011\".",
    "created_at": "2013-09-21T12:28:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9322#issuecomment-87765",
    "user": "https://github.com/fchapoton"
}
```

Changing keywords from "Simon ecc2011" to "simon_two_descent ecc2011".



---

archive/issue_events_022970.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9322#event-22970"
}
```



---

archive/issue_events_022971.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9322#event-22971"
}
```



---

archive/issue_comments_087766.json:
```json
{
    "body": "After applying #11005 (upgrade Simon's script to the latest version), rather than running for a long time, this example now gives an error similar to #15483:\n\n```\nsage: K.<w> = NumberField(x^2-x-232)\nsage: E = EllipticCurve([2-w,18+3*w,209+9*w,2581+175*w,852-55*w])\nsage: E.local_data()\n[]\nsage: E.simon_two_descent()\nTraceback (most recent call last):\n...\nRuntimeError: \n  ***   at top-level: ans=bnfellrank(K,[-a+2,3\n  ***                     ^--------------------\n  ***   in function bnfellrank: ...eqtheta,rnfeq,bbnf];rang=\n  ***   bnfell2descent_gen(b\n  ***   ^--------------------\n  ***   in function bnfell2descent_gen: ...und,r=nfsqrt(nf,norm(zc))\n  ***   [1];if(DEBUGLEVEL_el\n  ***   ^--------------------\n  ***   array index (1) out of allowed range [none].\nAn error occurred while running Simon's 2-descent program\n```\n\nWith the fix I just made at #15483, it again gives the correct result, but after a long time.",
    "created_at": "2014-02-11T20:00:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9322#issuecomment-87766",
    "user": "https://github.com/pjbruin"
}
```

After applying #11005 (upgrade Simon's script to the latest version), rather than running for a long time, this example now gives an error similar to #15483:

```
sage: K.<w> = NumberField(x^2-x-232)
sage: E = EllipticCurve([2-w,18+3*w,209+9*w,2581+175*w,852-55*w])
sage: E.local_data()
[]
sage: E.simon_two_descent()
Traceback (most recent call last):
...
RuntimeError: 
  ***   at top-level: ans=bnfellrank(K,[-a+2,3
  ***                     ^--------------------
  ***   in function bnfellrank: ...eqtheta,rnfeq,bbnf];rang=
  ***   bnfell2descent_gen(b
  ***   ^--------------------
  ***   in function bnfell2descent_gen: ...und,r=nfsqrt(nf,norm(zc))
  ***   [1];if(DEBUGLEVEL_el
  ***   ^--------------------
  ***   array index (1) out of allowed range [none].
An error occurred while running Simon's 2-descent program
```

With the fix I just made at #15483, it again gives the correct result, but after a long time.



---

archive/issue_comments_087767.json:
```json
{
    "body": "In principle it is not a bug if Sage uses different default values than Simon's script for the various parameters (`lim1`, `lim3`, `limtriv` and the more technical `maxprob` and `limbigprime`).  The defaults should be sensible, of course.  I guess we should find out if there is a good reason to use different defaults, and if so, what settings would be reasonable.",
    "created_at": "2014-02-12T16:55:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9322#issuecomment-87767",
    "user": "https://github.com/pjbruin"
}
```

In principle it is not a bug if Sage uses different default values than Simon's script for the various parameters (`lim1`, `lim3`, `limtriv` and the more technical `maxprob` and `limbigprime`).  The defaults should be sensible, of course.  I guess we should find out if there is a good reason to use different defaults, and if so, what settings would be reasonable.



---

archive/issue_comments_087768.json:
```json
{
    "body": "Is there a good reason to not use the default values that pari is using? What is troubling is that an example that runs fast in pari does take forever in Sage. So I would put the defaults to None, and then pass different defaults when the curve is over QQ or over a number field (according to DS's scripts).\n\nOne exception to this: the parameter `limbigprime` should be set to 0, to avoid the use of probabilistic (and thus not provably true) prime testing.",
    "created_at": "2014-03-25T18:14:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9322#issuecomment-87768",
    "user": "https://github.com/mmasdeu"
}
```

Is there a good reason to not use the default values that pari is using? What is troubling is that an example that runs fast in pari does take forever in Sage. So I would put the defaults to None, and then pass different defaults when the curve is over QQ or over a number field (according to DS's scripts).

One exception to this: the parameter `limbigprime` should be set to 0, to avoid the use of probabilistic (and thus not provably true) prime testing.



---

archive/issue_comments_087769.json:
```json
{
    "body": "Replying to [comment:17 mmasdeu]:\n> So I would put the defaults to None, and then pass different defaults when the curve is over QQ or over a number field (according to DS's scripts).\n> \n> One exception to this: the parameter `limbigprime` should be set to 0, to avoid the use of probabilistic (and thus not provably true) prime testing.\nAgree with all of this.",
    "created_at": "2014-03-25T19:41:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9322#issuecomment-87769",
    "user": "https://github.com/pjbruin"
}
```

Replying to [comment:17 mmasdeu]:
> So I would put the defaults to None, and then pass different defaults when the curve is over QQ or over a number field (according to DS's scripts).
> 
> One exception to this: the parameter `limbigprime` should be set to 0, to avoid the use of probabilistic (and thus not provably true) prime testing.
Agree with all of this.



---

archive/issue_comments_087770.json:
```json
{
    "body": "I have implemented the above suggestions. However, it seems that the using limbigprime=0 raises errors (I found them when using gp directly) and so I have currently set it to 30 (DS's default).\n\nWhen simon_two_descent() is called with default arguments, the infinite-order points change (this is expected). I have checked that the answer is still correct (in particular, the rank bounds are the same), and changed the doctests (which affected four files in total).\n\nNow the doctests pass for everything in the schemes/elliptic_curves folder, but I haven't run all the others.\n----\nNew commits:",
    "created_at": "2014-03-26T13:35:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9322#issuecomment-87770",
    "user": "https://github.com/mmasdeu"
}
```

I have implemented the above suggestions. However, it seems that the using limbigprime=0 raises errors (I found them when using gp directly) and so I have currently set it to 30 (DS's default).

When simon_two_descent() is called with default arguments, the infinite-order points change (this is expected). I have checked that the answer is still correct (in particular, the rank bounds are the same), and changed the doctests (which affected four files in total).

Now the doctests pass for everything in the schemes/elliptic_curves folder, but I haven't run all the others.
----
New commits:



---

archive/issue_comments_087771.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2014-03-26T13:35:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9322#issuecomment-87771",
    "user": "https://github.com/mmasdeu"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_087772.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2014-03-26T14:15:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9322#issuecomment-87772",
    "user": "https://github.com/pjbruin"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_087773.json:
```json
{
    "body": "Merged with development branch.  There are some doctest failures, one of which seems to be non-trivial (reported rank changing from 1 to 0).",
    "created_at": "2014-03-26T14:15:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9322#issuecomment-87773",
    "user": "https://github.com/pjbruin"
}
```

Merged with development branch.  There are some doctest failures, one of which seems to be non-trivial (reported rank changing from 1 to 0).



---

archive/issue_comments_087774.json:
```json
{
    "body": "The failing example is the new doctest from #16009 in `gp_simon.py`; it now returns `(0, 0, [])`.\n\n```\nsage: F.<a> = QuadraticField(29)\nsage: x = QQ['x'].gen()\nsage: K.<b> = F.extension(x^2-1/2*a+1/2)\nsage: E = EllipticCurve(K,[1, 0, 5/2*a + 27/2, 0, 0])\nsage: E.simon_two_descent(lim1=2, limtriv=3)\n(1, 1, [((-369/50*a - 1987/50)*b + 539/50*a + 2897/50 : (-27193/250*a - 146439/250)*b + 39683/250*a + 213709/250 : 1)])\n```\n\nThis is reproducible inside `gp` (2.5.x) with the current version of Simon's script (as included in Sage since #11005):\n\n```\nK = bnfinit(y^4 + y^2 - 7);\na = Mod(y, K.pol);\nE = [1, 0, 5*a^2 + 16, 0, 0];\nLIM1 = 2;\nLIMTRIV = 3;\nbnfellrank(K, E)\n```\n\nThis returns `[0, 0, []]`.",
    "created_at": "2014-03-26T14:20:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9322#issuecomment-87774",
    "user": "https://github.com/pjbruin"
}
```

The failing example is the new doctest from #16009 in `gp_simon.py`; it now returns `(0, 0, [])`.

```
sage: F.<a> = QuadraticField(29)
sage: x = QQ['x'].gen()
sage: K.<b> = F.extension(x^2-1/2*a+1/2)
sage: E = EllipticCurve(K,[1, 0, 5/2*a + 27/2, 0, 0])
sage: E.simon_two_descent(lim1=2, limtriv=3)
(1, 1, [((-369/50*a - 1987/50)*b + 539/50*a + 2897/50 : (-27193/250*a - 146439/250)*b + 39683/250*a + 213709/250 : 1)])
```

This is reproducible inside `gp` (2.5.x) with the current version of Simon's script (as included in Sage since #11005):

```
K = bnfinit(y^4 + y^2 - 7);
a = Mod(y, K.pol);
E = [1, 0, 5*a^2 + 16, 0, 0];
LIM1 = 2;
LIMTRIV = 3;
bnfellrank(K, E)
```

This returns `[0, 0, []]`.



---

archive/issue_comments_087775.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-03-27T14:19:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9322#issuecomment-87775",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_087776.json:
```json
{
    "body": "Merged #16009 and indirectly #16022, and fixed the two remaining doctest failures.  No other unexpected things, so I think this can safely be regarded as a reviewer patch.",
    "created_at": "2014-03-27T14:22:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9322#issuecomment-87776",
    "user": "https://github.com/pjbruin"
}
```

Merged #16009 and indirectly #16022, and fixed the two remaining doctest failures.  No other unexpected things, so I think this can safely be regarded as a reviewer patch.



---

archive/issue_comments_087777.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2014-03-27T14:22:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9322#issuecomment-87777",
    "user": "https://github.com/pjbruin"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_087778.json:
```json
{
    "body": "Changing status from positive_review to needs_review.",
    "created_at": "2014-03-28T18:43:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9322#issuecomment-87778",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Changing status from positive_review to needs_review.



---

archive/issue_comments_087779.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1 and set ticket back to needs_review. New commits:",
    "created_at": "2014-03-28T18:43:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9322#issuecomment-87779",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1 and set ticket back to needs_review. New commits:



---

archive/issue_comments_087780.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2014-03-28T18:49:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9322#issuecomment-87780",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_087781.json:
```json
{
    "body": "While looking at #10745 I noticed that the default `limtriv` over **Q** in Simon's script `ellQ.gp` changed from 50 to 3 in the latest version, so I changed the default setting in `ell_rational_field.py` and `gp_simon.py` accordingly.  Still qualifies as a reviewer patch, I guess.",
    "created_at": "2014-03-28T18:53:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9322#issuecomment-87781",
    "user": "https://github.com/pjbruin"
}
```

While looking at #10745 I noticed that the default `limtriv` over **Q** in Simon's script `ellQ.gp` changed from 50 to 3 in the latest version, so I changed the default setting in `ell_rational_field.py` and `gp_simon.py` accordingly.  Still qualifies as a reviewer patch, I guess.



---

archive/issue_comments_087782.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-03-28T18:53:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9322#issuecomment-87782",
    "user": "https://github.com/pjbruin"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087783.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-03-31T14:57:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9322#issuecomment-87783",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_022972.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-03-31T14:57:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9322",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9322#event-22972"
}
```
