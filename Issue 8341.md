# Issue 8341: detect_poles doesn't find a vertical asymptote where both sides go to infinity

Issue created by migration from https://trac.sagemath.org/ticket/8341

Original creator: jason

Original creation time: 2010-02-24 01:07:10

Assignee: was

CC:  whuss robert.marik

It seems like this should show a vertical asymptote at x=1, but it doesn't:


```
plot(1/((x-1)^2), (x, -3.5, 3.5), detect_poles='show', ymin = -5, ymax = 5) 
```




---

Comment by robert.marik created at 2010-03-06 14:26:13

It would be nice to fix this. But current detect_poles simply skips the lines with slope close to pi/2 and draws the vertical asyptote, if the function changes sign (skips from -infinity to +infinity). I think that using this idea it is not possible to detect vertical asymptote. 

Just some attempts: If we drop the condition which requires change in sign, 
we get "interval of asymptotes" - the asymptote is too thick.
Making epsilon smaller introduces problems with other graphs.

This is the diff with my experiments, if someone is interested

```
diff -r a1d167a37d52 sage/plot/plot.py
--- a/sage/plot/plot.py Thu Feb 25 13:42:16 2010 -0600
+++ b/sage/plot/plot.py Sat Mar 06 15:23:11 2010 +0100
@@ -2698,17 +2698,16 @@
             x0, y0 = exclude_data[i]
             x1, y1 = exclude_data[i+1]
             # detect poles
-            if (not (polar or parametric)) and detect_poles != False \
-               and ((y1 > 0 and y0 < 0) or (y1 < 0 and y0 > 0)):
+            if (not (polar or parametric)) and detect_poles != False:
                 # calculate the slope of the line segment
                 dy = abs(y1-y0)
                 dx = x1 - x0
                 alpha = (RDF(dy)/RDF(dx)).arctan()
-                if alpha >= RDF(pi/2) - epsilon:
+                if alpha >= RDF(pi/2) - 0.00001:
                     G += line(data[start_index:i], **options)
                     if detect_poles == 'show':
                         # draw a vertical asymptote
-                        G += line([(x0, y0), (x1, y1)], **pole_options)
+                        G += line([(x0, -1e100), (x1, 1e100)], **pole_options)
                     start_index = i+2
```



---

Comment by kcrisman created at 2013-01-14 15:42:52

See also #3985.
