# Issue 1893: Added graphical plotting to discrete random variables.

archive/issues_001893.json:
```json
{
    "body": "Assignee: boothby\n\nThis example explains the functionality for the new function 'plot':\nsage: import urllib2\nsage: S = AlphabeticStrings()\nsage: ISARC = 'http://iml.univ-mrs.fr/~kohel/tch/ISARC/'\nsage: en = S.encoding(urllib2.urlopen(ISARC + 'blackcat.txt').read())\nsage: F_en = en.frequency_distribution()\nsage: F_en.plot()\nsage: fr = S.encoding(urllib2.urlopen(ISARC + 'chapitre.1.txt').read())\nsage: F_fr = fr.frequency_distribution()\nsage: F_fr.plot()\n\nUnfortunately, I did not include such an example in the function \nsince it hard-codes an external web address, and would otherwise \nrequire a reasonably sized sample text for a proper demonstration.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1893\n\n",
    "created_at": "2008-01-23T14:14:36Z",
    "labels": [
        "notebook",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Added graphical plotting to discrete random variables.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1893",
    "user": "kohel"
}
```
Assignee: boothby

This example explains the functionality for the new function 'plot':
sage: import urllib2
sage: S = AlphabeticStrings()
sage: ISARC = 'http://iml.univ-mrs.fr/~kohel/tch/ISARC/'
sage: en = S.encoding(urllib2.urlopen(ISARC + 'blackcat.txt').read())
sage: F_en = en.frequency_distribution()
sage: F_en.plot()
sage: fr = S.encoding(urllib2.urlopen(ISARC + 'chapitre.1.txt').read())
sage: F_fr = fr.frequency_distribution()
sage: F_fr.plot()

Unfortunately, I did not include such an example in the function 
since it hard-codes an external web address, and would otherwise 
require a reasonably sized sample text for a proper demonstration.

Issue created by migration from https://trac.sagemath.org/ticket/1893





---

archive/issue_comments_011986.json:
```json
{
    "body": "Attachment [probabiity.hg](tarball://root/attachments/some-uuid/ticket1893/probabiity.hg) by mabshoff created at 2008-01-23 23:02:30",
    "created_at": "2008-01-23T23:02:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1893",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1893#issuecomment-11986",
    "user": "mabshoff"
}
```

Attachment [probabiity.hg](tarball://root/attachments/some-uuid/ticket1893/probabiity.hg) by mabshoff created at 2008-01-23 23:02:30



---

archive/issue_comments_011987.json:
```json
{
    "body": "This patch has been submitted (twice!) in the bundle accompanying #2153.\n\nWhether it should be applied... I say yes, but I'm worried that it will fail on infinite domains.",
    "created_at": "2008-02-15T04:45:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1893",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1893#issuecomment-11987",
    "user": "@ncalexan"
}
```

This patch has been submitted (twice!) in the bundle accompanying #2153.

Whether it should be applied... I say yes, but I'm worried that it will fail on infinite domains.



---

archive/issue_comments_011988.json:
```json
{
    "body": "Nick raised some issue which should be addressed.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-12T01:08:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1893",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1893#issuecomment-11988",
    "user": "mabshoff"
}
```

Nick raised some issue which should be addressed.

Cheers,

Michael



---

archive/issue_comments_011989.json:
```json
{
    "body": "According to `hg in probabiity.hg -p` in 4.3.1.rc0,\n\n```diff\nsummary:     Added plotting function for graphical display of a discrete random variable.\n\ndiff --git a/sage/probability/random_variable.py b/sage/probability/random_variable.py\n--- a/sage/probability/random_variable.py\n+++ b/sage/probability/random_variable.py\n@@ -21,6 +21,7 @@ from sage.structure.parent_base import P\n from sage.misc.functional import sqrt, log\n from sage.rings.all import RealField, RationalField\n from sage.sets.set import Set\n+import sage.plot.plot as plot\n \n ################################################################################\n ################################################################################\n@@ -265,6 +266,25 @@ class DiscreteRandomVariable(RandomVaria\n                \"Correlation not defined if standard deviations are not both nonzero.\"\n        return cov/(sigX*sigY)\n \n+    def plot(f, rgbcolor=(1,0,0)):\n+        \"\"\"\n+        Create a histogram from a frequency distribution or random variable.\n+        \"\"\"\n+       X = f.domain()\n+       Text = []\n+        Bars = []\n+        fnc_max = 0.0\n+        N = len(X)\n+        for n in range(N):\n+            x = X[n]\n+            y = f(x)\n+            fnc_max = max(fnc_max,y)\n+            Text.append(plot.text(str(x),(n+0.5,-0.01),rgbcolor = (0,0,0)))\n+            Bars.append(plot.polygon([ [n,0], [n,y], [n+1,y], [n+1,0] ], rgbcolor = rgbcolor))\n+        Hist = sum(Text+Bars)\n+        Hist.range(xmin=0,xmax=N,ymin=0,ymax=fnc_max)\n+        return Hist\n+\n```\n\nDoes this belong in [graphics](http://trac.sagemath.org/sage_trac/query?component=graphics&order=priority)?",
    "created_at": "2010-01-18T11:33:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1893",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1893#issuecomment-11989",
    "user": "@qed777"
}
```

According to `hg in probabiity.hg -p` in 4.3.1.rc0,

```diff
summary:     Added plotting function for graphical display of a discrete random variable.

diff --git a/sage/probability/random_variable.py b/sage/probability/random_variable.py
--- a/sage/probability/random_variable.py
+++ b/sage/probability/random_variable.py
@@ -21,6 +21,7 @@ from sage.structure.parent_base import P
 from sage.misc.functional import sqrt, log
 from sage.rings.all import RealField, RationalField
 from sage.sets.set import Set
+import sage.plot.plot as plot
 
 ################################################################################
 ################################################################################
@@ -265,6 +266,25 @@ class DiscreteRandomVariable(RandomVaria
                "Correlation not defined if standard deviations are not both nonzero."
        return cov/(sigX*sigY)
 
+    def plot(f, rgbcolor=(1,0,0)):
+        """
+        Create a histogram from a frequency distribution or random variable.
+        """
+       X = f.domain()
+       Text = []
+        Bars = []
+        fnc_max = 0.0
+        N = len(X)
+        for n in range(N):
+            x = X[n]
+            y = f(x)
+            fnc_max = max(fnc_max,y)
+            Text.append(plot.text(str(x),(n+0.5,-0.01),rgbcolor = (0,0,0)))
+            Bars.append(plot.polygon([ [n,0], [n,y], [n+1,y], [n+1,0] ], rgbcolor = rgbcolor))
+        Hist = sum(Text+Bars)
+        Hist.range(xmin=0,xmax=N,ymin=0,ymax=fnc_max)
+        return Hist
+
```

Does this belong in [graphics](http://trac.sagemath.org/sage_trac/query?component=graphics&order=priority)?



---

archive/issue_comments_011990.json:
```json
{
    "body": "Changing component from notebook to graphics.",
    "created_at": "2010-01-18T11:33:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1893",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1893#issuecomment-11990",
    "user": "@qed777"
}
```

Changing component from notebook to graphics.



---

archive/issue_comments_011991.json:
```json
{
    "body": "I have a feeling that #9671 will address this sufficiently if one could plug it into the class in question.",
    "created_at": "2014-10-28T20:12:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1893",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1893#issuecomment-11991",
    "user": "@kcrisman"
}
```

I have a feeling that #9671 will address this sufficiently if one could plug it into the class in question.
