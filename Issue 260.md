# Issue 260: transparent graphics output

archive/issues_000260.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  @kcrisman\n\n\n```\n\nIt may be helpful for users who want to use SAGE graphics on their web\npages to be able to set the background as transparent.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/260\n\n",
    "created_at": "2007-02-12T04:20:44Z",
    "labels": [
        "component: notebook",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "transparent graphics output",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/260",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

CC:  @kcrisman


```

It may be helpful for users who want to use SAGE graphics on their web
pages to be able to set the background as transparent.
```


Issue created by migration from https://trac.sagemath.org/ticket/260





---

archive/issue_comments_001204.json:
```json
{
    "body": "Attachment [trac_260-transparent_graphics.patch](tarball://root/attachments/some-uuid/ticket260/trac_260-transparent_graphics.patch) by @qed777 created at 2009-08-10 15:25:48\n\nThe attached patch adds a keyword argument `transparency` to `plot.show()`.  The default value is `None`, which makes the image background opaque.  A number between 0 (transparent) and 1 (opaque) determines the degree of transparency.\n\nPlease test and make changes.  I'm new to the plotting code, so it's likely that I've missed and/or broken something.",
    "created_at": "2009-08-10T15:25:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/260#issuecomment-1204",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_260-transparent_graphics.patch](tarball://root/attachments/some-uuid/ticket260/trac_260-transparent_graphics.patch) by @qed777 created at 2009-08-10 15:25:48

The attached patch adds a keyword argument `transparency` to `plot.show()`.  The default value is `None`, which makes the image background opaque.  A number between 0 (transparent) and 1 (opaque) determines the degree of transparency.

Please test and make changes.  I'm new to the plotting code, so it's likely that I've missed and/or broken something.



---

archive/issue_comments_001205.json:
```json
{
    "body": "Added examples.",
    "created_at": "2009-08-11T02:26:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/260#issuecomment-1205",
    "user": "https://github.com/qed777"
}
```

Added examples.



---

archive/issue_comments_001206.json:
```json
{
    "body": "Attachment [trac_260-transparent_graphics_v2.patch](tarball://root/attachments/some-uuid/ticket260/trac_260-transparent_graphics_v2.patch) by @qed777 created at 2009-08-17 09:13:52\n\nPerhaps `opacity` is a more appropriate keyword (`alpha` gave errors).",
    "created_at": "2009-08-17T09:13:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/260#issuecomment-1206",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_260-transparent_graphics_v2.patch](tarball://root/attachments/some-uuid/ticket260/trac_260-transparent_graphics_v2.patch) by @qed777 created at 2009-08-17 09:13:52

Perhaps `opacity` is a more appropriate keyword (`alpha` gave errors).



---

archive/issue_comments_001207.json:
```json
{
    "body": "Changing component from notebook to graphics.",
    "created_at": "2009-08-17T09:13:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/260#issuecomment-1207",
    "user": "https://github.com/qed777"
}
```

Changing component from notebook to graphics.



---

archive/issue_comments_001208.json:
```json
{
    "body": "Changing assignee from boothby to @williamstein.",
    "created_at": "2009-08-17T09:13:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/260#issuecomment-1208",
    "user": "https://github.com/qed777"
}
```

Changing assignee from boothby to @williamstein.



---

archive/issue_comments_001209.json:
```json
{
    "body": "Ticket #5448 may necessitate an update.",
    "created_at": "2009-08-30T11:31:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/260#issuecomment-1209",
    "user": "https://github.com/qed777"
}
```

Ticket #5448 may necessitate an update.



---

archive/issue_comments_001210.json:
```json
{
    "body": "Yes, I'm almost sure that #5448 will necessitate an update (or this will necessitate an update of #5448).\n\n1. I would change the keyword argument to something that is used more in Sage (like alpha or opacity) if we are going to have multiple levels of transparency.  If it is just a True/False option, then \"transparent\" seems like a fine keyword.\n\n2. What do you think about using the \"transparent\" option of savefig, as documented here: http://matplotlib.sourceforge.net/api/figure_api.html#matplotlib.figure.Figure.savefig ?\n\n3. The transparent option of savefig has the following code.  It looks like this code not only sets the figure patch, but goes through each axes object in the figure and sets the axes patch alpha level.  We should probably do the same.\n\n\n```\n 1036         if transparent:\n 1037             original_figure_alpha = self.patch.get_alpha()\n 1038             self.patch.set_alpha(0.0)\n 1039             original_axes_alpha = []\n 1040             for ax in self.axes:\n 1041                 patch = ax.patch\n 1042                 original_axes_alpha.append(patch.get_alpha())\n 1043                 patch.set_alpha(0.0)\n```\n",
    "created_at": "2009-08-31T13:25:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/260#issuecomment-1210",
    "user": "https://github.com/jasongrout"
}
```

Yes, I'm almost sure that #5448 will necessitate an update (or this will necessitate an update of #5448).

1. I would change the keyword argument to something that is used more in Sage (like alpha or opacity) if we are going to have multiple levels of transparency.  If it is just a True/False option, then "transparent" seems like a fine keyword.

2. What do you think about using the "transparent" option of savefig, as documented here: http://matplotlib.sourceforge.net/api/figure_api.html#matplotlib.figure.Figure.savefig ?

3. The transparent option of savefig has the following code.  It looks like this code not only sets the figure patch, but goes through each axes object in the figure and sets the axes patch alpha level.  We should probably do the same.


```
 1036         if transparent:
 1037             original_figure_alpha = self.patch.get_alpha()
 1038             self.patch.set_alpha(0.0)
 1039             original_axes_alpha = []
 1040             for ax in self.axes:
 1041                 patch = ax.patch
 1042                 original_axes_alpha.append(patch.get_alpha())
 1043                 patch.set_alpha(0.0)
```




---

archive/issue_comments_001211.json:
```json
{
    "body": "How about adapting `savefig()`'s code for a numerical scalar option with keyword `alpha`?  Or should we consider allowing color 4-tuples, e.g., RGBA, for different figure components and plotted objects?  A disclaimer: I'm not very familiar with how matplotlib or Sage plotting works.\n\nI'm happy to postpone this ticket's review until #5448 merges.  Alternatively, I can recommend closing this one, if it's easier to treat transparency at #5448.",
    "created_at": "2009-08-31T22:51:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/260#issuecomment-1211",
    "user": "https://github.com/qed777"
}
```

How about adapting `savefig()`'s code for a numerical scalar option with keyword `alpha`?  Or should we consider allowing color 4-tuples, e.g., RGBA, for different figure components and plotted objects?  A disclaimer: I'm not very familiar with how matplotlib or Sage plotting works.

I'm happy to postpone this ticket's review until #5448 merges.  Alternatively, I can recommend closing this one, if it's easier to treat transparency at #5448.



---

archive/issue_comments_001212.json:
```json
{
    "body": "I added a quick \"transparent\" option to the patch at #5448.  If you think it is needed, I think this ticket ought to go ahead and implement a \"background_color\" and/or \"background_opacity\" keywords, or something like that, that lets a user specify a background color and opacity.\n\nPlease look at the patch at #5448 and let me know if I didn't cover something you need done.",
    "created_at": "2009-09-01T15:59:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/260#issuecomment-1212",
    "user": "https://github.com/jasongrout"
}
```

I added a quick "transparent" option to the patch at #5448.  If you think it is needed, I think this ticket ought to go ahead and implement a "background_color" and/or "background_opacity" keywords, or something like that, that lets a user specify a background color and opacity.

Please look at the patch at #5448 and let me know if I didn't cover something you need done.



---

archive/issue_comments_001213.json:
```json
{
    "body": "FYI, #5448 did implement the transparency=True/False option to show.  However, this ticket can have larger scope.  I'm slightly enlarging the title/description to reflect that fact.\n\nOn the other hand, if it's not wanted, maybe we should close this ticket after all.",
    "created_at": "2009-09-17T08:20:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/260#issuecomment-1213",
    "user": "https://github.com/jasongrout"
}
```

FYI, #5448 did implement the transparency=True/False option to show.  However, this ticket can have larger scope.  I'm slightly enlarging the title/description to reflect that fact.

On the other hand, if it's not wanted, maybe we should close this ticket after all.



---

archive/issue_comments_001214.json:
```json
{
    "body": "A quick (and crude) change to `Graphics.save()` sets up a `background_color` option:\n\n```python\n        if savenow:\n[...]\n            background_color = None\n            if kwds.has_key('background_color'):\n                background_color = kwds.pop('background_color', False)\n\n            figure=self.matplotlib(*args, **kwds)\n[...]\n            if background_color:\n                figure.patch.set_color(background_color)\n                for ax in figure.axes:\n                    ax.patch.set_color(background_color)\n                # Not sure how to avoid using these:\n                options['edgecolor'] = background_color\n                options['facecolor'] = background_color\n\n            figure.savefig(filename,dpi=dpi,bbox_inches='tight',**options)\n```\n\nIf we can avoid using the `savefig()` options, perhaps we can set a background color *and* transparency level entirely in `matplotlib()`.  Then, I think, we could handle combinations like\n\n* `transparent=True, opacity=0.5`\n* `opacity=0.8, background_color='#ffbefa'`\n\nin a way a user expects.  Thoughts?",
    "created_at": "2009-09-18T06:04:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/260#issuecomment-1214",
    "user": "https://github.com/qed777"
}
```

A quick (and crude) change to `Graphics.save()` sets up a `background_color` option:

```python
        if savenow:
[...]
            background_color = None
            if kwds.has_key('background_color'):
                background_color = kwds.pop('background_color', False)

            figure=self.matplotlib(*args, **kwds)
[...]
            if background_color:
                figure.patch.set_color(background_color)
                for ax in figure.axes:
                    ax.patch.set_color(background_color)
                # Not sure how to avoid using these:
                options['edgecolor'] = background_color
                options['facecolor'] = background_color

            figure.savefig(filename,dpi=dpi,bbox_inches='tight',**options)
```

If we can avoid using the `savefig()` options, perhaps we can set a background color *and* transparency level entirely in `matplotlib()`.  Then, I think, we could handle combinations like

* `transparent=True, opacity=0.5`
* `opacity=0.8, background_color='#ffbefa'`

in a way a user expects.  Thoughts?



---

archive/issue_comments_001215.json:
```json
{
    "body": "Add opacity and background_color plot options.  Apply only this patch.",
    "created_at": "2009-10-23T00:25:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/260#issuecomment-1215",
    "user": "https://github.com/qed777"
}
```

Add opacity and background_color plot options.  Apply only this patch.



---

archive/issue_comments_001216.json:
```json
{
    "body": "Attachment [trac_260-plot_bg_alpha.patch](tarball://root/attachments/some-uuid/ticket260/trac_260-plot_bg_alpha.patch) by @qed777 created at 2009-10-23 00:35:44\n\nThe [attachment:trac_260-plot_bg_alpha.patch new patch] adds `background_color` and `opacity` keyword options to `plot()`.  Examples:\n\n```python\nsage: plot(x^cos(x^(sin(x))), (0, 30),  fill='axis', fillcolor='yellow', opacity=0.5)\n```\n\n\n```python\nsage: C = 1.0\nsage: a, b = var('a, b')\nsage: lem = contour_plot(2 * C^2 * (b^2 - a^2) - (a^2 + b^2)^2, (a, -2, 2), (b, -2, 2), plot_points=100, transparent=True, contours=25, cmap='Spectral')\nsage: lem.show(aspect_ratio=1.0, background_color='khaki')\n```\n\n\nCan a Sage plotting or matplotlib expert point out how to make the background uniform when *both* `background_color` and `opacity` are given?  Try this:\n\n```python\nsage: plot(x^cos(x^(sin(x))), (0, 30),  fill='axis', fillcolor='yellow', background_color='red', opacity=0.5)\n```\n\nNote how the plot's thick \"border\" has a different apparent transparency level.  Is this an [alpha compositing](http://en.wikipedia.org/wiki/Alpha_compositing) or blending problem?",
    "created_at": "2009-10-23T00:35:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/260#issuecomment-1216",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_260-plot_bg_alpha.patch](tarball://root/attachments/some-uuid/ticket260/trac_260-plot_bg_alpha.patch) by @qed777 created at 2009-10-23 00:35:44

The [attachment:trac_260-plot_bg_alpha.patch new patch] adds `background_color` and `opacity` keyword options to `plot()`.  Examples:

```python
sage: plot(x^cos(x^(sin(x))), (0, 30),  fill='axis', fillcolor='yellow', opacity=0.5)
```


```python
sage: C = 1.0
sage: a, b = var('a, b')
sage: lem = contour_plot(2 * C^2 * (b^2 - a^2) - (a^2 + b^2)^2, (a, -2, 2), (b, -2, 2), plot_points=100, transparent=True, contours=25, cmap='Spectral')
sage: lem.show(aspect_ratio=1.0, background_color='khaki')
```


Can a Sage plotting or matplotlib expert point out how to make the background uniform when *both* `background_color` and `opacity` are given?  Try this:

```python
sage: plot(x^cos(x^(sin(x))), (0, 30),  fill='axis', fillcolor='yellow', background_color='red', opacity=0.5)
```

Note how the plot's thick "border" has a different apparent transparency level.  Is this an [alpha compositing](http://en.wikipedia.org/wiki/Alpha_compositing) or blending problem?



---

archive/issue_comments_001217.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-10-23T00:35:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/260#issuecomment-1217",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_001218.json:
```json
{
    "body": "It looks like there are two patches; one for the image, and one for the axes background.  Each is set to 50% opacity, and they are layered on top of each other.\n\nBut post to the matplotlib mailing list.  I'm sure they'll have a good answer for you.",
    "created_at": "2009-10-23T01:07:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/260#issuecomment-1218",
    "user": "https://github.com/jasongrout"
}
```

It looks like there are two patches; one for the image, and one for the axes background.  Each is set to 50% opacity, and they are layered on top of each other.

But post to the matplotlib mailing list.  I'm sure they'll have a good answer for you.



---

archive/issue_comments_001219.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-11T11:19:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/260#issuecomment-1219",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_001220.json:
```json
{
    "body": "Replying to [comment:12 jason]:\n> But post to the matplotlib mailing list.  I'm sure they'll have a good answer for you.\n\nOops.  I didn't notice your response.  I'll ask the matplotlib mavens.",
    "created_at": "2009-12-11T11:41:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/260#issuecomment-1220",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:12 jason]:
> But post to the matplotlib mailing list.  I'm sure they'll have a good answer for you.

Oops.  I didn't notice your response.  I'll ask the matplotlib mavens.



---

archive/issue_comments_001221.json:
```json
{
    "body": "Any responses?",
    "created_at": "2010-07-27T17:49:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/260#issuecomment-1221",
    "user": "https://github.com/kcrisman"
}
```

Any responses?



---

archive/issue_comments_001222.json:
```json
{
    "body": "No, because I stupidly neglected to ask.  Sorry about this!  I'll try to ask on the matplotlib mailing list soon, probably after we release Sage 4.5.2.",
    "created_at": "2010-07-29T07:08:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/260#issuecomment-1222",
    "user": "https://github.com/qed777"
}
```

No, because I stupidly neglected to ask.  Sorry about this!  I'll try to ask on the matplotlib mailing list soon, probably after we release Sage 4.5.2.



---

archive/issue_comments_001223.json:
```json
{
    "body": "Replying to [comment:16 mpatel]:\n> No, because I stupidly neglected to ask.  Sorry about this!  I'll try to ask on the matplotlib mailing list soon, probably after we release Sage 4.5.2.\n\nI've [posted to matplotlib-users](http://sourceforge.net/mailarchive/forum.php?thread_name=4C7F4F10.8060208%40gmail.com&forum_name=matplotlib-users).",
    "created_at": "2010-09-02T07:18:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/260#issuecomment-1223",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:16 mpatel]:
> No, because I stupidly neglected to ask.  Sorry about this!  I'll try to ask on the matplotlib mailing list soon, probably after we release Sage 4.5.2.

I've [posted to matplotlib-users](http://sourceforge.net/mailarchive/forum.php?thread_name=4C7F4F10.8060208%40gmail.com&forum_name=matplotlib-users).



---

archive/issue_comments_001224.json:
```json
{
    "body": "Attachment [trac_260-plot_bg_alpha_rebased.patch](tarball://root/attachments/some-uuid/ticket260/trac_260-plot_bg_alpha_rebased.patch) by ryan created at 2011-04-16 05:12:44\n\nRebased.  Applies cleanly to Sage 4.6.2.",
    "created_at": "2011-04-16T05:12:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/260#issuecomment-1224",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Attachment [trac_260-plot_bg_alpha_rebased.patch](tarball://root/attachments/some-uuid/ticket260/trac_260-plot_bg_alpha_rebased.patch) by ryan created at 2011-04-16 05:12:44

Rebased.  Applies cleanly to Sage 4.6.2.



---

archive/issue_comments_001225.json:
```json
{
    "body": "Rebased for Sage 4.6.2 so it applies cleanly.  Hopefully this helps with further testing.",
    "created_at": "2011-04-16T05:17:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/260#issuecomment-1225",
    "user": "https://trac.sagemath.org/admin/accounts/users/ryan"
}
```

Rebased for Sage 4.6.2 so it applies cleanly.  Hopefully this helps with further testing.



---

archive/issue_comments_001226.json:
```json
{
    "body": "If I recall correctly, the only issue was this image versus background thing, and the mpl devels in the thread above didn't have much to say that was helpful.  If things look okay with this, maybe fixing whatever is left could be another ticket.  It's sort of said we don't have this merged yet.",
    "created_at": "2011-04-17T00:05:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/260#issuecomment-1226",
    "user": "https://github.com/kcrisman"
}
```

If I recall correctly, the only issue was this image versus background thing, and the mpl devels in the thread above didn't have much to say that was helpful.  If things look okay with this, maybe fixing whatever is left could be another ticket.  It's sort of said we don't have this merged yet.



---

archive/issue_comments_001227.json:
```json
{
    "body": "Well, Jason, what do you think?  I wonder if mpl has new ways of designating these things now... anyway, just pinging about the status of this.",
    "created_at": "2013-01-29T20:55:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/260#issuecomment-1227",
    "user": "https://github.com/kcrisman"
}
```

Well, Jason, what do you think?  I wonder if mpl has new ways of designating these things now... anyway, just pinging about the status of this.
