# Issue 4303: Plotting: points(list_of_points, rgbcolor=c) gives strangely colored results with exactly 3 points.

archive/issues_004303.json:
```json
{
    "body": "Assignee: was\n\nKeywords: plotting\n\nFrom the docstring for point2d, the following works fine:\n\nsage: p = point(((0.5, 0.5), (1, 2), (0.5, 0.9), (-1,-1)), rgbcolor=hue(1), pointsize=30); p.show()\n\nHowever\n\nsage: p = point(((0.5, 0.5), (1, 2), (0.5, 0.9)), rgbcolor=hue(1), pointsize=30); p.show()\n\ngives one purple(?) point and two blue points.  This seems to happen if and only if the number of points specified is exactly three, regardless of the specified color.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4303\n\n",
    "created_at": "2008-10-15T17:33:34Z",
    "labels": [
        "user interface",
        "major",
        "bug"
    ],
    "title": "Plotting: points(list_of_points, rgbcolor=c) gives strangely colored results with exactly 3 points.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4303",
    "user": "jbandlow"
}
```
Assignee: was

Keywords: plotting

From the docstring for point2d, the following works fine:

sage: p = point(((0.5, 0.5), (1, 2), (0.5, 0.9), (-1,-1)), rgbcolor=hue(1), pointsize=30); p.show()

However

sage: p = point(((0.5, 0.5), (1, 2), (0.5, 0.9)), rgbcolor=hue(1), pointsize=30); p.show()

gives one purple(?) point and two blue points.  This seems to happen if and only if the number of points specified is exactly three, regardless of the specified color.



Issue created by migration from https://trac.sagemath.org/ticket/4303





---

archive/issue_comments_031489.json:
```json
{
    "body": "I wonder if this is related to the apparent special casing of 3 or fewer points in GraphicPrimitiveFactory_from_point_list (code below, from sage/plot/plot.py).  That was the best lead I can find with the time I have, hope it helps.\n\n\n```\nclass GraphicPrimitiveFactory_from_point_list(GraphicPrimitiveFactory):\n    def __call__(self, points, coerce=True, **kwds):\n        try:\n            return points.plot(**kwds)\n        except AttributeError:\n            pass\n        options = dict(self.options)\n        for k, v in kwds.iteritems():\n            options[k] = v\n\n        if not isinstance(points, (list,tuple)) or \\\n           (isinstance(points,(list,tuple)) and len(points) <= 3 \\\n            and len(points) > 0 \\\n            and not isinstance(points[0], (list,tuple))):\n            try:\n                points = [[float(z) for z in points]]\n            except TypeError:\n                pass\n\n        try:\n            if len(points) > 0 and len(points[0]) == 3:\n                return self._graphic3d()(points, coerce=coerce, **kwds)\n        except (AttributeError, TypeError):\n            pass\n        xdata = []\n        ydata = []\n        if coerce:\n            xdata = [float(z[0]) for z in points]\n            ydata = [float(z[1]) for z in points]            \n        else:\n            xdata = [z[0] for z in points]\n            ydata = [z[1] for z in points]            \n\n        return self._from_xdata_ydata(xdata, ydata, True, options=options)\n```\n",
    "created_at": "2008-10-15T18:38:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4303#issuecomment-31489",
    "user": "mhampton"
}
```

I wonder if this is related to the apparent special casing of 3 or fewer points in GraphicPrimitiveFactory_from_point_list (code below, from sage/plot/plot.py).  That was the best lead I can find with the time I have, hope it helps.


```
class GraphicPrimitiveFactory_from_point_list(GraphicPrimitiveFactory):
    def __call__(self, points, coerce=True, **kwds):
        try:
            return points.plot(**kwds)
        except AttributeError:
            pass
        options = dict(self.options)
        for k, v in kwds.iteritems():
            options[k] = v

        if not isinstance(points, (list,tuple)) or \
           (isinstance(points,(list,tuple)) and len(points) <= 3 \
            and len(points) > 0 \
            and not isinstance(points[0], (list,tuple))):
            try:
                points = [[float(z) for z in points]]
            except TypeError:
                pass

        try:
            if len(points) > 0 and len(points[0]) == 3:
                return self._graphic3d()(points, coerce=coerce, **kwds)
        except (AttributeError, TypeError):
            pass
        xdata = []
        ydata = []
        if coerce:
            xdata = [float(z[0]) for z in points]
            ydata = [float(z[1]) for z in points]            
        else:
            xdata = [z[0] for z in points]
            ydata = [z[1] for z in points]            

        return self._from_xdata_ydata(xdata, ydata, True, options=options)
```




---

archive/issue_comments_031490.json:
```json
{
    "body": "This is a duplicate of #2076.",
    "created_at": "2008-10-15T19:12:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4303#issuecomment-31490",
    "user": "mhansen"
}
```

This is a duplicate of #2076.



---

archive/issue_comments_031491.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2008-10-15T19:12:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4303",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4303#issuecomment-31491",
    "user": "mhansen"
}
```

Resolution: duplicate
