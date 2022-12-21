# Issue 1893: Added graphical plotting to discrete random variables.

Issue created by migration from Trac.

Original creator: kohel

Original creation time: 2008-01-23 14:14:36

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


---

Attachment


---

Comment by ncalexan created at 2008-02-15 04:45:53

This patch has been submitted (twice!) in the bundle accompanying #2153.

Whether it should be applied... I say yes, but I'm worried that it will fail on infinite domains.


---

Comment by mabshoff created at 2008-03-12 01:08:47

Nick raised some issue which should be addressed.

Cheers,

Michael


---

Comment by mpatel created at 2010-01-18 11:33:20

According to `hg in probabiity.hg -p` in 4.3.1.rc0,

```diff
summary:     Added plotting function for graphical display of a discrete random variable.

diff --git a/sage/probability/random_variable.py b/sage/probability/random_variable.py
--- a/sage/probability/random_variable.py
+++ b/sage/probability/random_variable.py
`@``@` -21,6 +21,7 `@``@` from sage.structure.parent_base import P
 from sage.misc.functional import sqrt, log
 from sage.rings.all import RealField, RationalField
 from sage.sets.set import Set
+import sage.plot.plot as plot
 
 ################################################################################
 ################################################################################
`@``@` -265,6 +266,25 `@``@` class DiscreteRandomVariable(RandomVaria
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

Comment by mpatel created at 2010-01-18 11:33:20

Changing component from notebook to graphics.


---

Comment by kcrisman created at 2014-10-28 20:12:03

I have a feeling that #9671 will address this sufficiently if one could plug it into the class in question.
