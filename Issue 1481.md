# Issue 1481: showing a matrix plot blows up

archive/issues_001481.json:
```json
{
    "body": "Assignee: was\n\nCC:  kcrisman\n\n\n```\nsage: m=matrix(ZZ,1,[16]); m\n[16]\nsage: matrix_plot(m^10).show()\n---------------------------------------------------------------------------\n<type 'exceptions.OverflowError'>         Traceback (most recent call last)\n\n/home/grout/.sage/<ipython console> in <module>()\n\n/home/grout/sage/local/lib/python2.5/site-packages/sage/plot/plot.py in show(self, xmin, xmax, ymin, ymax, figsize, filename, dpi, axes, axes_label, frame, fontsize, **args)\n    654         if filename is None:\n    655             filename = sage.misc.misc.tmp_filename() + '.png'\n--> 656         self.save(filename, xmin, xmax, ymin, ymax, figsize, dpi=dpi, axes=axes,frame=frame, fontsize=fontsize)\n    657         os.system('%s %s 2>/dev/null 1>/dev/null &'%(sage.misc.viewer.browser(), filename))\n    658\n\n/home/grout/sage/local/lib/python2.5/site-packages/sage/plot/plot.py in save(self, filename, xmin, xmax, ymin, ymax, figsize, figure, sub, savenow, dpi, axes, axes_label, fontsize, frame, verify)\n    766             if isinstance(g, GraphicPrimitive_MatrixPlot):\n    767                 matrixplot = True\n--> 768             g._render_on_subplot(subplot)\n    769\n    770         #adjust the xy limits and draw the axes:\n\n/home/grout/sage/local/lib/python2.5/site-packages/sage/plot/plot.py in _render_on_subplot(self, subplot)\n   1102             print \"The possible color maps include: %s\"%possibilities\n   1103             raise RuntimeError, \"Color map %s not known\"%cmap\n-> 1104         subplot.imshow(self.xy_data_array, cmap=cmap, interpolation='nearest')\n   1105\n   1106 # Below is the base class that is used to make 'field plots'.\n\n/home/grout/sage/local/lib/python2.5/site-packages/matplotlib/axes.py in imshow(self, X, cmap, norm, aspect, interpolation, alpha, vmin, vmax, origin, extent, shape, filternorm, filterrad, imlim, **kwargs)\n   4053                        filterrad=filterrad, **kwargs)\n   4054\n-> 4055         im.set_data(X)\n   4056         im.set_alpha(alpha)\n   4057         self._set_artist_props(im)\n\n/home/grout/sage/local/lib/python2.5/site-packages/matplotlib/image.py in set_data(self, A, shape)\n    224             or X.shape[2] > 4\n    225             or X.shape[2] < 3):\n--> 226             cm.ScalarMappable.set_array(self, X)\n    227         else:\n    228             self._A = X\n\n/home/grout/sage/local/lib/python2.5/site-packages/matplotlib/cm.py in set_array(self, A)\n     65             self._A = A.astype(nx.Float32)\n     66         else:\n---> 67             self._A = A.astype(nx.Int16)\n     68\n     69     def get_array(self):\n\n/home/grout/sage/local/lib/python2.5/site-packages/numpy/core/ma.py in astype(self, tc)\n   1148     def astype (self, tc):\n   1149         \"return self as array of given type.\"\n-> 1150         d = self._data.astype(tc)\n   1151         return array(d, mask=self._mask)\n   1152\n\n<type 'exceptions.OverflowError'>: long int too large to convert to int\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1481\n\n",
    "created_at": "2007-12-12T19:51:52Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "showing a matrix plot blows up",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1481",
    "user": "jason"
}
```
Assignee: was

CC:  kcrisman


```
sage: m=matrix(ZZ,1,[16]); m
[16]
sage: matrix_plot(m^10).show()
---------------------------------------------------------------------------
<type 'exceptions.OverflowError'>         Traceback (most recent call last)

/home/grout/.sage/<ipython console> in <module>()

/home/grout/sage/local/lib/python2.5/site-packages/sage/plot/plot.py in show(self, xmin, xmax, ymin, ymax, figsize, filename, dpi, axes, axes_label, frame, fontsize, **args)
    654         if filename is None:
    655             filename = sage.misc.misc.tmp_filename() + '.png'
--> 656         self.save(filename, xmin, xmax, ymin, ymax, figsize, dpi=dpi, axes=axes,frame=frame, fontsize=fontsize)
    657         os.system('%s %s 2>/dev/null 1>/dev/null &'%(sage.misc.viewer.browser(), filename))
    658

/home/grout/sage/local/lib/python2.5/site-packages/sage/plot/plot.py in save(self, filename, xmin, xmax, ymin, ymax, figsize, figure, sub, savenow, dpi, axes, axes_label, fontsize, frame, verify)
    766             if isinstance(g, GraphicPrimitive_MatrixPlot):
    767                 matrixplot = True
--> 768             g._render_on_subplot(subplot)
    769
    770         #adjust the xy limits and draw the axes:

/home/grout/sage/local/lib/python2.5/site-packages/sage/plot/plot.py in _render_on_subplot(self, subplot)
   1102             print "The possible color maps include: %s"%possibilities
   1103             raise RuntimeError, "Color map %s not known"%cmap
-> 1104         subplot.imshow(self.xy_data_array, cmap=cmap, interpolation='nearest')
   1105
   1106 # Below is the base class that is used to make 'field plots'.

/home/grout/sage/local/lib/python2.5/site-packages/matplotlib/axes.py in imshow(self, X, cmap, norm, aspect, interpolation, alpha, vmin, vmax, origin, extent, shape, filternorm, filterrad, imlim, **kwargs)
   4053                        filterrad=filterrad, **kwargs)
   4054
-> 4055         im.set_data(X)
   4056         im.set_alpha(alpha)
   4057         self._set_artist_props(im)

/home/grout/sage/local/lib/python2.5/site-packages/matplotlib/image.py in set_data(self, A, shape)
    224             or X.shape[2] > 4
    225             or X.shape[2] < 3):
--> 226             cm.ScalarMappable.set_array(self, X)
    227         else:
    228             self._A = X

/home/grout/sage/local/lib/python2.5/site-packages/matplotlib/cm.py in set_array(self, A)
     65             self._A = A.astype(nx.Float32)
     66         else:
---> 67             self._A = A.astype(nx.Int16)
     68
     69     def get_array(self):

/home/grout/sage/local/lib/python2.5/site-packages/numpy/core/ma.py in astype(self, tc)
   1148     def astype (self, tc):
   1149         "return self as array of given type."
-> 1150         d = self._data.astype(tc)
   1151         return array(d, mask=self._mask)
   1152

<type 'exceptions.OverflowError'>: long int too large to convert to int
```


Issue created by migration from https://trac.sagemath.org/ticket/1481





---

archive/issue_comments_009520.json:
```json
{
    "body": "Changing component from algebraic geometry to linear algebra.",
    "created_at": "2007-12-12T19:52:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1481#issuecomment-9520",
    "user": "jason"
}
```

Changing component from algebraic geometry to linear algebra.



---

archive/issue_comments_009521.json:
```json
{
    "body": "This seems to work in 2.9.3:\n\n\n```\nsage: m=matrix(ZZ,1,[16]); m\n[16]\nsage: matrix_plot(m^100).show()\nsage: \n```\n\n\nI do get this warning:\n\n\n```\nsage: matrix_plot(m^1000).show()\nWarning: invalid value encountered in multiply\n```\n\n\nbut the image shows up (a giant black square, just like it should).",
    "created_at": "2008-01-19T07:22:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1481#issuecomment-9521",
    "user": "jason"
}
```

This seems to work in 2.9.3:


```
sage: m=matrix(ZZ,1,[16]); m
[16]
sage: matrix_plot(m^100).show()
sage: 
```


I do get this warning:


```
sage: matrix_plot(m^1000).show()
Warning: invalid value encountered in multiply
```


but the image shows up (a giant black square, just like it should).



---

archive/issue_comments_009522.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-19T07:22:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1481#issuecomment-9522",
    "user": "jason"
}
```

Resolution: fixed



---

archive/issue_comments_009523.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-01-19T07:26:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1481#issuecomment-9523",
    "user": "mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_009524.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-01-19T07:26:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1481#issuecomment-9524",
    "user": "mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_009525.json:
```json
{
    "body": "Ok, but we should still add a doctest to catch this behavior. It can be `#long`, but I will reopen this for now until the doctest is added [which is standard requirement to close bugs these days :)]\n\nCheers,\n\nMichael",
    "created_at": "2008-01-19T07:26:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1481#issuecomment-9525",
    "user": "mabshoff"
}
```

Ok, but we should still add a doctest to catch this behavior. It can be `#long`, but I will reopen this for now until the doctest is added [which is standard requirement to close bugs these days :)]

Cheers,

Michael



---

archive/issue_comments_009526.json:
```json
{
    "body": "Thanks for reopening this.  The following code displays the wrong plot:\n\n\n```\na=matrix(2,[16^1000,0,0,-16^1000]);\nmatrix_plot(a)\n```\n\n\nWhat should be displayed is the same as the plot:\n\n\n```\na=matrix(2,[16,0,0,-16]);\nmatrix_plot(a)\n```\n\n\nSo the matrix plot has gone from blowing up to just being wrong.  Whether this is worse or better is left as an exercise for the reader.",
    "created_at": "2008-01-28T17:50:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1481#issuecomment-9526",
    "user": "jason"
}
```

Thanks for reopening this.  The following code displays the wrong plot:


```
a=matrix(2,[16^1000,0,0,-16^1000]);
matrix_plot(a)
```


What should be displayed is the same as the plot:


```
a=matrix(2,[16,0,0,-16]);
matrix_plot(a)
```


So the matrix plot has gone from blowing up to just being wrong.  Whether this is worse or better is left as an exercise for the reader.



---

archive/issue_comments_009527.json:
```json
{
    "body": "I think this problem is a matplotlib problem and has to do with not dealing with inf or -inf in the matrix.  We could send vmin and vmax parameters to the imshow command to scale the matrix manually if we see an infinity in the matrix, or we could raise an exception, or we could report the bug back up to matplotlib (if it is indeed a matplotlib issue).",
    "created_at": "2008-01-28T18:51:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1481#issuecomment-9527",
    "user": "jason"
}
```

I think this problem is a matplotlib problem and has to do with not dealing with inf or -inf in the matrix.  We could send vmin and vmax parameters to the imshow command to scale the matrix manually if we see an infinity in the matrix, or we could raise an exception, or we could report the bug back up to matplotlib (if it is indeed a matplotlib issue).



---

archive/issue_comments_009528.json:
```json
{
    "body": "Attachment [trac_1481-part1.patch](tarball://root/attachments/some-uuid/ticket1481/trac_1481-part1.patch) by was created at 2010-02-16 19:31:53\n\nthis should completely deal with the dense case.",
    "created_at": "2010-02-16T19:31:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1481#issuecomment-9528",
    "user": "was"
}
```

Attachment [trac_1481-part1.patch](tarball://root/attachments/some-uuid/ticket1481/trac_1481-part1.patch) by was created at 2010-02-16 19:31:53

this should completely deal with the dense case.



---

archive/issue_comments_009529.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-12-22T08:14:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1481#issuecomment-9529",
    "user": "jason"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_009530.json:
```json
{
    "body": "Changing component from linear algebra to graphics.",
    "created_at": "2010-12-22T08:15:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1481#issuecomment-9530",
    "user": "jason"
}
```

Changing component from linear algebra to graphics.



---

archive/issue_comments_009531.json:
```json
{
    "body": "Whoever referees this patch should make sure it works well with the norm, vmin, and vmax parameters in matrix_plot",
    "created_at": "2011-01-11T16:51:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1481#issuecomment-9531",
    "user": "jason"
}
```

Whoever referees this patch should make sure it works well with the norm, vmin, and vmax parameters in matrix_plot



---

archive/issue_comments_009532.json:
```json
{
    "body": "On the surface, it doesn't appear that the patch works with norm, vmin, and vmax, probably because the patch was written before we added those parameters.",
    "created_at": "2011-01-11T16:54:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1481#issuecomment-9532",
    "user": "jason"
}
```

On the surface, it doesn't appear that the patch works with norm, vmin, and vmax, probably because the patch was written before we added those parameters.



---

archive/issue_comments_009533.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-03-12T04:31:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1481#issuecomment-9533",
    "user": "kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_009534.json:
```json
{
    "body": "Does not apply to 4.7.alpha1 in any case.  Needs work - though, impressively, only one hunk failed. Not bad for a patch over a year old.",
    "created_at": "2011-03-12T04:31:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1481#issuecomment-9534",
    "user": "kcrisman"
}
```

Does not apply to 4.7.alpha1 in any case.  Needs work - though, impressively, only one hunk failed. Not bad for a patch over a year old.



---

archive/issue_comments_009535.json:
```json
{
    "body": "The original patch doesn't seem to work at the moment (the numpy array created has dtype=object, so the integers stay as integers instead of becoming floats, so there are no infs to work around).  I have a variant which works, and modified it to handle vmin and vmax, but I'm not sure what to do with norm: should the norm be applied before or after the vmin/vmax?",
    "created_at": "2012-05-25T21:22:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1481",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1481#issuecomment-9535",
    "user": "dsm"
}
```

The original patch doesn't seem to work at the moment (the numpy array created has dtype=object, so the integers stay as integers instead of becoming floats, so there are no infs to work around).  I have a variant which works, and modified it to handle vmin and vmax, but I'm not sure what to do with norm: should the norm be applied before or after the vmin/vmax?
