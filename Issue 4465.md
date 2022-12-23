# Issue 4465: zero-length errors give division error instead of just drawing a point.

archive/issues_004465.json:
```json
{
    "body": "Assignee: was\n\nThis is an error to a custom patch that we have to the matplotlib code so that we can have arrows that are shortened by a certain number of points.\n\n\n```\nThis week, I was drawing plot vector field using two ways : (1) plot_vector_field and (2) by simply suming up plenty of arrows as I wished. Since their was a fixed point somewhere, I came up with the problem of drawing a zero length arrow. Using sage 3.1.4, I get a zero division error. Where is this division from? The example below show that it is not from the slope as it can draw a vertical arrow.\n\nsage: arrow((1, 1), (2, 1))\nsage: arrow((1, 1), (1, 2))\nsage: arrow((1, 1), (1, 1))\n---------------------------------------------------------------------------\nZeroDivisionError                         Traceback (most recent call last) :\n...\n/home/slabbe/sage/local/lib/python2.5/site-packages/matplotlib/arrow_line.pyc in draw(self, renderer)\n    100         pixel_vector = (orig_t.transform_point(points[1]) - orig_t.transform_point(points[0]))\n    101         pixel_length=math.sqrt(sum(pixel_vector**2))\n--> 102         clip_fraction = renderer.points_to_pixels(self._arrowshorten)/pixel_length\n    103         head_clip_fraction = renderer.points_to_pixels(self._arrowshorten+self._arrowheadlength*0.8)/pixel_length\n    104\n\nZeroDivisionError: float division\n\nIn my problem, I would have been happy if arrow(x,x) would draw simply a point. I know I can define my own arrow but maybe sage's arrow could behave like myarrow ?\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4465\n\n",
    "created_at": "2008-11-08T03:03:22Z",
    "labels": [
        "graphics",
        "major",
        "bug"
    ],
    "title": "zero-length errors give division error instead of just drawing a point.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4465",
    "user": "jason"
}
```
Assignee: was

This is an error to a custom patch that we have to the matplotlib code so that we can have arrows that are shortened by a certain number of points.


```
This week, I was drawing plot vector field using two ways : (1) plot_vector_field and (2) by simply suming up plenty of arrows as I wished. Since their was a fixed point somewhere, I came up with the problem of drawing a zero length arrow. Using sage 3.1.4, I get a zero division error. Where is this division from? The example below show that it is not from the slope as it can draw a vertical arrow.

sage: arrow((1, 1), (2, 1))
sage: arrow((1, 1), (1, 2))
sage: arrow((1, 1), (1, 1))
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last) :
...
/home/slabbe/sage/local/lib/python2.5/site-packages/matplotlib/arrow_line.pyc in draw(self, renderer)
    100         pixel_vector = (orig_t.transform_point(points[1]) - orig_t.transform_point(points[0]))
    101         pixel_length=math.sqrt(sum(pixel_vector**2))
--> 102         clip_fraction = renderer.points_to_pixels(self._arrowshorten)/pixel_length
    103         head_clip_fraction = renderer.points_to_pixels(self._arrowshorten+self._arrowheadlength*0.8)/pixel_length
    104

ZeroDivisionError: float division

In my problem, I would have been happy if arrow(x,x) would draw simply a point. I know I can define my own arrow but maybe sage's arrow could behave like myarrow ?
```


Issue created by migration from https://trac.sagemath.org/ticket/4465





---

archive/issue_comments_032972.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-08T03:04:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4465#issuecomment-32972",
    "user": "jason"
}
```

Changing status from new to assigned.



---

archive/issue_comments_032973.json:
```json
{
    "body": "Changing assignee from was to jason.",
    "created_at": "2008-11-08T03:04:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4465#issuecomment-32973",
    "user": "jason"
}
```

Changing assignee from was to jason.



---

archive/issue_comments_032974.json:
```json
{
    "body": "This should be fixed by #4774",
    "created_at": "2009-01-26T16:08:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4465#issuecomment-32974",
    "user": "jason"
}
```

This should be fixed by #4774



---

archive/issue_comments_032975.json:
```json
{
    "body": "This is still a problem after #4774.  We should probably take care of this in our arrow-drawing code, then, instead of just passing things on to matplotlib.",
    "created_at": "2009-02-13T17:38:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4465#issuecomment-32975",
    "user": "jason"
}
```

This is still a problem after #4774.  We should probably take care of this in our arrow-drawing code, then, instead of just passing things on to matplotlib.



---

archive/issue_comments_032976.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-06-04T23:33:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4465#issuecomment-32976",
    "user": "mhansen"
}
```

Resolution: invalid



---

archive/issue_comments_032977.json:
```json
{
    "body": "This works fine in 4.0.1.rc1:\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: arrow((1, 1), (1, 1))\n| Sage Version 4.0.1.rc1, Release Date: 2009-06-04                   |\n| Type notebook() for the GUI, and license() for information.        |\nsage: \n```\n",
    "created_at": "2009-06-04T23:33:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4465#issuecomment-32977",
    "user": "mhansen"
}
```

This works fine in 4.0.1.rc1:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: arrow((1, 1), (1, 1))
| Sage Version 4.0.1.rc1, Release Date: 2009-06-04                   |
| Type notebook() for the GUI, and license() for information.        |
sage: 
```

