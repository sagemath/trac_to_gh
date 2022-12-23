# Issue 6847: Auto-generate and insert images into the documentation

archive/issues_006847.json:
```json
{
    "body": "Assignee: tba\n\nCC:  eviatarbach\n\nCurrently, images included in the Sage documentation must be generated separately from the docbuild process itself (cf. #6685).  For the sake of consistency, convenience, testing, etc., we should have an option to automate this process, particularly for the reference manual.\n\nPlease see the discussion at #6685.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6847\n\n",
    "created_at": "2009-08-30T13:00:09Z",
    "labels": [
        "documentation",
        "minor",
        "enhancement"
    ],
    "title": "Auto-generate and insert images into the documentation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6847",
    "user": "mpatel"
}
```
Assignee: tba

CC:  eviatarbach

Currently, images included in the Sage documentation must be generated separately from the docbuild process itself (cf. #6685).  For the sake of consistency, convenience, testing, etc., we should have an option to automate this process, particularly for the reference manual.

Please see the discussion at #6685.


Issue created by migration from https://trac.sagemath.org/ticket/6847





---

archive/issue_comments_056466.json:
```json
{
    "body": "The file [doc/users/transforms_tutorial.rst](http://matplotlib.svn.sourceforge.net/viewvc/matplotlib/trunk/matplotlib/doc/users/transforms_tutorial.rst?view=markup) from [matplotlib's](http://matplotlib.sourceforge.net/index.html) [trunk](http://matplotlib.svn.sourceforge.net/viewvc/matplotlib/trunk/matplotlib/) includes:\n\n```\n.. plot:: pyplots/annotate_transform.py\n```\n\nand\n\n```\n.. plot::\n   :include-source:\n\n   import numpy as np\n   import matplotlib.pyplot as plt\n\n   x = np.arange(0, 10, 0.005)\n   y = np.exp(-x/2.) * np.sin(2*np.pi*x)\n\n   fig = plt.figure()\n   ax = fig.add_subplot(111)\n   ax.plot(x, y)\n   ax.set_xlim(0, 10)\n   ax.set_ylim(-1, 1)\n\n   plt.show()\n```\n\nPossible [output](http://matplotlib.sourceforge.net/users/transforms_tutorial.html).  Elsewhere, I've seen\n\n```\n.. plot:: pyplots/tex_demo.py\n   :include-source:\n```\n\nI think the `:include-[`](../tree/master/`) option includes the formatted source before the image in \"place\" of a link to the plain-text source.",
    "created_at": "2009-08-30T13:35:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6847#issuecomment-56466",
    "user": "mpatel"
}
```

The file [doc/users/transforms_tutorial.rst](http://matplotlib.svn.sourceforge.net/viewvc/matplotlib/trunk/matplotlib/doc/users/transforms_tutorial.rst?view=markup) from [matplotlib's](http://matplotlib.sourceforge.net/index.html) [trunk](http://matplotlib.svn.sourceforge.net/viewvc/matplotlib/trunk/matplotlib/) includes:

```
.. plot:: pyplots/annotate_transform.py
```

and

```
.. plot::
   :include-source:

   import numpy as np
   import matplotlib.pyplot as plt

   x = np.arange(0, 10, 0.005)
   y = np.exp(-x/2.) * np.sin(2*np.pi*x)

   fig = plt.figure()
   ax = fig.add_subplot(111)
   ax.plot(x, y)
   ax.set_xlim(0, 10)
   ax.set_ylim(-1, 1)

   plt.show()
```

Possible [output](http://matplotlib.sourceforge.net/users/transforms_tutorial.html).  Elsewhere, I've seen

```
.. plot:: pyplots/tex_demo.py
   :include-source:
```

I think the `:include-[`](../tree/master/`) option includes the formatted source before the image in "place" of a link to the plain-text source.



---

archive/issue_comments_056467.json:
```json
{
    "body": "For the `plot` directive's implementation, see [plot_directive.py](http://matplotlib.svn.sourceforge.net/viewvc/matplotlib/trunk/matplotlib/lib/matplotlib/sphinxext/plot_directive.py?view=markup).\n\nOther goodies:\n\n* Formatted [examples](http://matplotlib.sourceforge.net/examples/index.html) with code and plots.  See [gen_rst.py](http://matplotlib.svn.sourceforge.net/viewvc/matplotlib/trunk/matplotlib/doc/sphinxext/gen_rst.py?view=markup).\n* Plot [gallery](http://matplotlib.sourceforge.net/gallery.html).  See [gen_gallery.py](http://matplotlib.svn.sourceforge.net/viewvc/matplotlib/trunk/matplotlib/doc/sphinxext/gen_gallery.py?view=markup).\n\nTo check out the trunk:\n* `svn co http://matplotlib.svn.sourceforge.net/svnroot/matplotlib/trunk/matplotlib/ matplotlib`",
    "created_at": "2009-08-30T14:40:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6847#issuecomment-56467",
    "user": "mpatel"
}
```

For the `plot` directive's implementation, see [plot_directive.py](http://matplotlib.svn.sourceforge.net/viewvc/matplotlib/trunk/matplotlib/lib/matplotlib/sphinxext/plot_directive.py?view=markup).

Other goodies:

* Formatted [examples](http://matplotlib.sourceforge.net/examples/index.html) with code and plots.  See [gen_rst.py](http://matplotlib.svn.sourceforge.net/viewvc/matplotlib/trunk/matplotlib/doc/sphinxext/gen_rst.py?view=markup).
* Plot [gallery](http://matplotlib.sourceforge.net/gallery.html).  See [gen_gallery.py](http://matplotlib.svn.sourceforge.net/viewvc/matplotlib/trunk/matplotlib/doc/sphinxext/gen_gallery.py?view=markup).

To check out the trunk:
* `svn co http://matplotlib.svn.sourceforge.net/svnroot/matplotlib/trunk/matplotlib/ matplotlib`



---

archive/issue_comments_056468.json:
```json
{
    "body": "this is now working",
    "created_at": "2016-08-08T14:00:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6847#issuecomment-56468",
    "user": "chapoton"
}
```

this is now working



---

archive/issue_comments_056469.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-08-08T14:00:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6847#issuecomment-56469",
    "user": "chapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_056470.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-08-08T14:01:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6847#issuecomment-56470",
    "user": "chapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_056471.json:
```json
{
    "body": "Determined to be invalid/duplicate/wontfix (closing as \"wontfix\" as a catch-all resolution).",
    "created_at": "2016-08-30T13:32:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6847#issuecomment-56471",
    "user": "embray"
}
```

Determined to be invalid/duplicate/wontfix (closing as "wontfix" as a catch-all resolution).



---

archive/issue_comments_056472.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2016-08-30T13:32:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6847#issuecomment-56472",
    "user": "embray"
}
```

Resolution: wontfix
