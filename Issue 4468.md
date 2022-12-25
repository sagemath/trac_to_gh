# Issue 4468: [with patch, positive review] assertion error when (some) bad color map given

archive/issues_004468.json:
```json
{
    "body": "Assignee: @seblabbe\n\nKeywords: cmap\n\nThe following example works well :\n\n```\nsage: matrix_plot(random_matrix(RDF, 50), cmap='hsv')\n```\n\nBut the next one doesn't which is fine because 'jolies' doesn't correspond to a color map.\n\n```\nsage: matrix_plot(random_matrix(RDF, 50), cmap='jolies')\nverbose 0 (2212: plot.py, _render_on_subplot) The possible color maps include: Spectral, summer, pink_r, Set1, Set2, Set3, Dark2, prism, PuOr_r, PuBuGn_r, RdPu, gist_ncar_r, Dark2_r, YlGnBu, RdYlBu, hot_r, gist_rainbow_r, gist_stern, cool_r, cool, gray, copper_r, Greens_r, GnBu, gist_ncar, spring_r, gist_rainbow, gist_heat_r, summer_r, OrRd_r, bone, gist_stern_r, RdYlGn, Pastel2_r, spring, Accent, YlOrRd_r, Set2_r, PuBu, RdGy_r, spectral, flag_r, jet_r, RdPu_r, gist_yarg, BuGn, Paired_r, hsv_r, YlOrRd, Greens, PRGn, gist_heat, spectral_r, Paired, hsv, Oranges_r, prism_r, Pastel2, Pastel1_r, Pastel1, gray_r, PuRd_r, Spectral_r, BuPu, YlGnBu_r, copper, gist_earth_r, Set3_r, OrRd, PuBu_r, winter_r, RdBu, jet, bone_r, gist_earth, Oranges, RdYlGn_r, PiYG, YlGn, binary_r, gist_gray_r, gist_gray, flag, RdBu_r, BrBG, Reds, GnBu_r, BrBG_r, Reds_r, RdGy, PuRd, Accent_r, Blues, Greys, autumn, PRGn_r, Greys_r, pink, binary, winter, gist_yarg_r, RdYlBu_r, hot, YlOrBr, BuPu_r, Purples_r, PiYG_r, YlGn_r, Blues_r, YlOrBr_r, Purples, autumn_r, BuGn_r, Set1_r, PuOr, PuBuGn\n---------------------------------------------------------------------------\nRuntimeError                              Traceback (most recent call last):\n...\nRuntimeError: Color map jolies not known\n```\n\nWhat about 'mpl' which as well doesn't correspond to a color map :\n\n```\nsage: matrix_plot(random_matrix(RDF, 50), cmap='mpl')\n---------------------------------------------------------------------------\nAssertionError                            Traceback (most recent call last):\n...\nAssertionError: \n```\n\nAn assertion error : why ? Because in plot.py, we test only if the given cmap is a key of a certain dictionary but not *all* the key of this dictionary correspond to a color map. In fact, there are 18 exceptions as shown below.\n\n```\nsage: from matplotlib import cm                                 \nsage: d = cm.__dict__                                           \nsage: from matplotlib.colors import LinearSegmentedColormap as C\nsage: 'mpl' in [x for x in d.keys() if not isinstance(d[x], C)]       \nTrue\nsage: [x for x in d.keys() if not isinstance(d[x], C)]          \n\n['colors',\n 'cmapname_r',\n 'ScalarMappable',\n 'LUTSIZE',\n 'cmapname',\n 'cbook',\n '__file__',\n 'cmapnames',\n 'cmapdat_r',\n '__builtins__',\n '__name__',\n 'get_cmap',\n '__doc__',\n 'revcmap',\n 'ma',\n 'np',\n 'mpl',\n 'datad']\nsage: len(_)\n18\n```\n\na patch to come...\n\nIssue created by migration from https://trac.sagemath.org/ticket/4468\n\n",
    "closed_at": "2008-11-21T20:22:12Z",
    "created_at": "2008-11-08T06:38:21Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "[with patch, positive review] assertion error when (some) bad color map given",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4468",
    "user": "https://github.com/seblabbe"
}
```
Assignee: @seblabbe

Keywords: cmap

The following example works well :

```
sage: matrix_plot(random_matrix(RDF, 50), cmap='hsv')
```

But the next one doesn't which is fine because 'jolies' doesn't correspond to a color map.

```
sage: matrix_plot(random_matrix(RDF, 50), cmap='jolies')
verbose 0 (2212: plot.py, _render_on_subplot) The possible color maps include: Spectral, summer, pink_r, Set1, Set2, Set3, Dark2, prism, PuOr_r, PuBuGn_r, RdPu, gist_ncar_r, Dark2_r, YlGnBu, RdYlBu, hot_r, gist_rainbow_r, gist_stern, cool_r, cool, gray, copper_r, Greens_r, GnBu, gist_ncar, spring_r, gist_rainbow, gist_heat_r, summer_r, OrRd_r, bone, gist_stern_r, RdYlGn, Pastel2_r, spring, Accent, YlOrRd_r, Set2_r, PuBu, RdGy_r, spectral, flag_r, jet_r, RdPu_r, gist_yarg, BuGn, Paired_r, hsv_r, YlOrRd, Greens, PRGn, gist_heat, spectral_r, Paired, hsv, Oranges_r, prism_r, Pastel2, Pastel1_r, Pastel1, gray_r, PuRd_r, Spectral_r, BuPu, YlGnBu_r, copper, gist_earth_r, Set3_r, OrRd, PuBu_r, winter_r, RdBu, jet, bone_r, gist_earth, Oranges, RdYlGn_r, PiYG, YlGn, binary_r, gist_gray_r, gist_gray, flag, RdBu_r, BrBG, Reds, GnBu_r, BrBG_r, Reds_r, RdGy, PuRd, Accent_r, Blues, Greys, autumn, PRGn_r, Greys_r, pink, binary, winter, gist_yarg_r, RdYlBu_r, hot, YlOrBr, BuPu_r, Purples_r, PiYG_r, YlGn_r, Blues_r, YlOrBr_r, Purples, autumn_r, BuGn_r, Set1_r, PuOr, PuBuGn
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last):
...
RuntimeError: Color map jolies not known
```

What about 'mpl' which as well doesn't correspond to a color map :

```
sage: matrix_plot(random_matrix(RDF, 50), cmap='mpl')
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last):
...
AssertionError: 
```

An assertion error : why ? Because in plot.py, we test only if the given cmap is a key of a certain dictionary but not *all* the key of this dictionary correspond to a color map. In fact, there are 18 exceptions as shown below.

```
sage: from matplotlib import cm                                 
sage: d = cm.__dict__                                           
sage: from matplotlib.colors import LinearSegmentedColormap as C
sage: 'mpl' in [x for x in d.keys() if not isinstance(d[x], C)]       
True
sage: [x for x in d.keys() if not isinstance(d[x], C)]          

['colors',
 'cmapname_r',
 'ScalarMappable',
 'LUTSIZE',
 'cmapname',
 'cbook',
 '__file__',
 'cmapnames',
 'cmapdat_r',
 '__builtins__',
 '__name__',
 'get_cmap',
 '__doc__',
 'revcmap',
 'ma',
 'np',
 'mpl',
 'datad']
sage: len(_)
18
```

a patch to come...

Issue created by migration from https://trac.sagemath.org/ticket/4468





---

archive/issue_comments_032921.json:
```json
{
    "body": "Attachment [cmap_4468.patch](tarball://root/attachments/some-uuid/ticket4468/cmap_4468.patch) by @seblabbe created at 2008-11-08 06:41:30",
    "created_at": "2008-11-08T06:41:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4468#issuecomment-32921",
    "user": "https://github.com/seblabbe"
}
```

Attachment [cmap_4468.patch](tarball://root/attachments/some-uuid/ticket4468/cmap_4468.patch) by @seblabbe created at 2008-11-08 06:41:30



---

archive/issue_comments_032922.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-08T06:45:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4468#issuecomment-32922",
    "user": "https://github.com/seblabbe"
}
```

Changing status from new to assigned.



---

archive/issue_comments_032923.json:
```json
{
    "body": "Hi Sebastian,\n\nplease also add a doctest(s) for this patch.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-08T20:39:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4468#issuecomment-32923",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi Sebastian,

please also add a doctest(s) for this patch.

Cheers,

Michael



---

archive/issue_comments_032924.json:
```json
{
    "body": "This patch replace the precedent.",
    "created_at": "2008-11-08T22:28:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4468#issuecomment-32924",
    "user": "https://github.com/seblabbe"
}
```

This patch replace the precedent.



---

archive/issue_comments_032925.json:
```json
{
    "body": "Attachment [cmap_4468-2.patch](tarball://root/attachments/some-uuid/ticket4468/cmap_4468-2.patch) by @seblabbe created at 2008-11-08 22:39:47\n\nI just added two doctests in a second patch (witch replace the precedent). I tested those doctests in another and smaller file because sage -t plot.py takes a while. On my computer, I am not able to end it...\n\n```\n***sage/plot$ sage -t all.py axes.py\nsage -t  devel/sage-word/sage/plot/all.py                   \n\t [2.9 s]\nsage -t  devel/sage-word/sage/plot/axes.py                  \n\t [8.3 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 11.2 seconds\n***sage/plot$ sage -t plot.py\nsage -t  sage/plot/plot.py                  *** *** Error: TIMED OUT! *** ***\n*** *** Error: TIMED OUT! *** ***\n\t [602.3 s]\nexit code: 1024\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t  devel/sage-word/sage/plot/plot.py\nTotal time for all tests: 602.3 seconds\n```",
    "created_at": "2008-11-08T22:39:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4468#issuecomment-32925",
    "user": "https://github.com/seblabbe"
}
```

Attachment [cmap_4468-2.patch](tarball://root/attachments/some-uuid/ticket4468/cmap_4468-2.patch) by @seblabbe created at 2008-11-08 22:39:47

I just added two doctests in a second patch (witch replace the precedent). I tested those doctests in another and smaller file because sage -t plot.py takes a while. On my computer, I am not able to end it...

```
***sage/plot$ sage -t all.py axes.py
sage -t  devel/sage-word/sage/plot/all.py                   
	 [2.9 s]
sage -t  devel/sage-word/sage/plot/axes.py                  
	 [8.3 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 11.2 seconds
***sage/plot$ sage -t plot.py
sage -t  sage/plot/plot.py                  *** *** Error: TIMED OUT! *** ***
*** *** Error: TIMED OUT! *** ***
	 [602.3 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  devel/sage-word/sage/plot/plot.py
Total time for all tests: 602.3 seconds
```



---

archive/issue_comments_032926.json:
```json
{
    "body": "Looks good and passes tests for me.",
    "created_at": "2008-11-21T17:00:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4468#issuecomment-32926",
    "user": "https://github.com/mwhansen"
}
```

Looks good and passes tests for me.



---

archive/issue_comments_032927.json:
```json
{
    "body": "Sebastian,\n\nplease make sure to post a proper hg patch and not a diff. I checked in your changes under your name, so credit goes where credit is due :)\n\nCheers,\n\nMichael",
    "created_at": "2008-11-21T20:19:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4468#issuecomment-32927",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Sebastian,

please make sure to post a proper hg patch and not a diff. I checked in your changes under your name, so credit goes where credit is due :)

Cheers,

Michael



---

archive/issue_comments_032928.json:
```json
{
    "body": "Merged cmap_4468-2.patch in Sage 3.2.1.alpha0",
    "created_at": "2008-11-21T20:22:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4468#issuecomment-32928",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged cmap_4468-2.patch in Sage 3.2.1.alpha0



---

archive/issue_comments_032929.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-21T20:22:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4468#issuecomment-32929",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_010096.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-21T20:22:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4468",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4468#event-10096"
}
```
