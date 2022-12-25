# Issue 4878: [with patch; positive review] Add a density_plot() function

archive/issues_004878.json:
```json
{
    "body": "Assignee: abergeron\n\nAs was requested a long time ago (in september!), I did the density_plot() function.\n\nI've added as copyright-holders all the copyright-holders from contour_plot since over 80% of density_plot file is copy and paste from that.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4878\n\n",
    "closed_at": "2009-01-12T01:54:27Z",
    "created_at": "2008-12-25T05:49:42Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch; positive review] Add a density_plot() function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4878",
    "user": "https://trac.sagemath.org/admin/accounts/users/abergeron"
}
```
Assignee: abergeron

As was requested a long time ago (in september!), I did the density_plot() function.

I've added as copyright-holders all the copyright-holders from contour_plot since over 80% of density_plot file is copy and paste from that.



Issue created by migration from https://trac.sagemath.org/ticket/4878





---

archive/issue_comments_036862.json:
```json
{
    "body": "Attachment [trac_4878.patch](tarball://root/attachments/some-uuid/ticket4878/trac_4878.patch) by @wdjoyner created at 2008-12-26 13:21:47\n\nApplies to 3.2.2 cleanly and passes sage -t. The docstrings look fine.\n\nI tried\n\n```\nsage: density_plot(sin(x^2 + y^2)*cos(x)*sin(y), (-4, 4), (-4, 4), cmap='winter', plot_points=100)\n\nsage: contour_plot(sin(x^2 + y^2)*cos(x)*sin(y), (-4, 4), (-4, 4), cmap='winter', plot_points=100, contours=40)\n```\nand noticed that they look very similar (modulo scaling). However, there are some plotting artifacts contour_plot leaves at the \"corners\" where cos(x)=0 and sin(y)=0. density_plot seems to avoid these problems. Nice patch.\n\nBTW, where can one find the list of \"legal\" values of cmap? For example, _allowed_options gives this:\n\n```\n    cmap           The colormap, one of (autumn, bone, cool, copper,\n                       gray, hot, hsv, jet, pink, prism, spring, summer, winter)\n```\n\nBut this is incomplete, since Oranges, Blues, etc also work. For example, try\n\n```\nsage: x,y = var('x,y')\nsage: density_plot(sin(x^2 + y^2)*exp((x^2+y^2)/10), (-4, 4), (-4, 4), cmap='Greens')\n```\nI'm happy giving this a positive review but am wondering about this one small issue with the output of _allowed_options. Can the author please comment on this?",
    "created_at": "2008-12-26T13:21:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4878#issuecomment-36862",
    "user": "https://github.com/wdjoyner"
}
```

Attachment [trac_4878.patch](tarball://root/attachments/some-uuid/ticket4878/trac_4878.patch) by @wdjoyner created at 2008-12-26 13:21:47

Applies to 3.2.2 cleanly and passes sage -t. The docstrings look fine.

I tried

```
sage: density_plot(sin(x^2 + y^2)*cos(x)*sin(y), (-4, 4), (-4, 4), cmap='winter', plot_points=100)

sage: contour_plot(sin(x^2 + y^2)*cos(x)*sin(y), (-4, 4), (-4, 4), cmap='winter', plot_points=100, contours=40)
```
and noticed that they look very similar (modulo scaling). However, there are some plotting artifacts contour_plot leaves at the "corners" where cos(x)=0 and sin(y)=0. density_plot seems to avoid these problems. Nice patch.

BTW, where can one find the list of "legal" values of cmap? For example, _allowed_options gives this:

```
    cmap           The colormap, one of (autumn, bone, cool, copper,
                       gray, hot, hsv, jet, pink, prism, spring, summer, winter)
```

But this is incomplete, since Oranges, Blues, etc also work. For example, try

```
sage: x,y = var('x,y')
sage: density_plot(sin(x^2 + y^2)*exp((x^2+y^2)/10), (-4, 4), (-4, 4), cmap='Greens')
```
I'm happy giving this a positive review but am wondering about this one small issue with the output of _allowed_options. Can the author please comment on this?



---

archive/issue_comments_036863.json:
```json
{
    "body": "Attachment [trac_4878.2.patch](tarball://root/attachments/some-uuid/ticket4878/trac_4878.2.patch) by abergeron created at 2008-12-27 23:19:37\n\nFix some problems with original patch, incremental",
    "created_at": "2008-12-27T23:19:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4878#issuecomment-36863",
    "user": "https://trac.sagemath.org/admin/accounts/users/abergeron"
}
```

Attachment [trac_4878.2.patch](tarball://root/attachments/some-uuid/ticket4878/trac_4878.2.patch) by abergeron created at 2008-12-27 23:19:37

Fix some problems with original patch, incremental



---

archive/issue_comments_036864.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-27T23:21:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4878#issuecomment-36864",
    "user": "https://trac.sagemath.org/admin/accounts/users/abergeron"
}
```

Changing status from new to assigned.



---

archive/issue_comments_036865.json:
```json
{
    "body": "The thing about cmap options is that every time we update matplotlib new colormap names become available.  The docstrings are just a fixed list and we do not update them every time we update matplotlib.\n\nI've just opened a ticket at #4884 to fix colormap handling that includes a fix for this issue and another patch that uses the new function to do the cmap handling.\n\nThis means that this ticket depends on #4884 now.\n\nI've also fixed a couple of small problems with the code and docs.",
    "created_at": "2008-12-27T23:21:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4878#issuecomment-36865",
    "user": "https://trac.sagemath.org/admin/accounts/users/abergeron"
}
```

The thing about cmap options is that every time we update matplotlib new colormap names become available.  The docstrings are just a fixed list and we do not update them every time we update matplotlib.

I've just opened a ticket at #4884 to fix colormap handling that includes a fix for this issue and another patch that uses the new function to do the cmap handling.

This means that this ticket depends on #4884 now.

I've also fixed a couple of small problems with the code and docs.



---

archive/issue_comments_036866.json:
```json
{
    "body": "> The thing about cmap options is that every time we update matplotlib \n> new colormap names become available. The docstrings are just a fixed \n> list and we do not update them every time we update matplotlib. \n\n\nAt a bare minimum, the docstring should explain precisely what one needs to type to get a list of all valid colormaps.  This could be included in a docstring, so that when matplotlib changes the colormap options, the docstring will suddenly break, and we will know to fix it.\n\nIncidentally, right now one way to get a list of valid colormaps is to just make a mistake with the cmap option, and a list of all valid options is displayed.\n\n```\nsage: var('x,y')\nsage: z = contour_plot(cos(x^2+y^2), (-4, 4), (-4, 4),cmap='foobar')  \nsage: z.save('a.png')                                               \n```\nverbose 0 (63: contour_plot.py, _render_on_subplot) The possible color maps include: Spectral, summer, pink_r, Set1, Set2, Set3, Dark2, prism, PuOr_r, PuBuGn_r, RdPu, gist_ncar_r, Dark2_r, YlGnBu, RdYlBu, hot_r, gist_rainbow_r, gist_stern, cool_r, cool, gray, copper_r, Greens_r, GnBu, gist_ncar, spring_r, gist_rainbow, gist_heat_r, summer_r, OrRd_r, bone, gist_stern_r, RdYlGn, Pastel2_r, spring, Accent, YlOrRd_r, Set2_r, PuBu, RdGy_r, spectral, flag_r, jet_r, RdPu_r, gist_yarg, BuGn, Paired_r, hsv_r, YlOrRd, Greens, PRGn, gist_heat, spectral_r, Paired, hsv, Oranges_r, prism_r, Pastel2, Pastel1_r, Pastel1, gray_r, PuRd_r, Spectral_r, BuPu, YlGnBu_r, copper, gist_earth_r, Set3_r, OrRd, PuBu_r, winter_r, RdBu, jet, bone_r, gist_earth, Oranges, RdYlGn_r, PiYG, YlGn, binary_r, gist_gray_r, gist_gray, flag, RdBu_r, BrBG, Reds, GnBu_r, BrBG_r, Reds_r, RdGy, PuRd, Accent_r, Blues, Greys, autumn, PRGn_r, Greys_r, pink, binary, winter, gist_yarg_r, RdYlBu_r, hot, YlOrBr, BuPu_r, Purples_r, PiYG_r, YlGn_r, Blues_r, YlOrBr_r, Purples, autumn_r, BuGn_r, Set1_r, PuOr, PuBuGn\n}}}",
    "created_at": "2008-12-29T06:15:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4878#issuecomment-36866",
    "user": "https://github.com/williamstein"
}
```

> The thing about cmap options is that every time we update matplotlib 
> new colormap names become available. The docstrings are just a fixed 
> list and we do not update them every time we update matplotlib. 


At a bare minimum, the docstring should explain precisely what one needs to type to get a list of all valid colormaps.  This could be included in a docstring, so that when matplotlib changes the colormap options, the docstring will suddenly break, and we will know to fix it.

Incidentally, right now one way to get a list of valid colormaps is to just make a mistake with the cmap option, and a list of all valid options is displayed.

```
sage: var('x,y')
sage: z = contour_plot(cos(x^2+y^2), (-4, 4), (-4, 4),cmap='foobar')  
sage: z.save('a.png')                                               
```
verbose 0 (63: contour_plot.py, _render_on_subplot) The possible color maps include: Spectral, summer, pink_r, Set1, Set2, Set3, Dark2, prism, PuOr_r, PuBuGn_r, RdPu, gist_ncar_r, Dark2_r, YlGnBu, RdYlBu, hot_r, gist_rainbow_r, gist_stern, cool_r, cool, gray, copper_r, Greens_r, GnBu, gist_ncar, spring_r, gist_rainbow, gist_heat_r, summer_r, OrRd_r, bone, gist_stern_r, RdYlGn, Pastel2_r, spring, Accent, YlOrRd_r, Set2_r, PuBu, RdGy_r, spectral, flag_r, jet_r, RdPu_r, gist_yarg, BuGn, Paired_r, hsv_r, YlOrRd, Greens, PRGn, gist_heat, spectral_r, Paired, hsv, Oranges_r, prism_r, Pastel2, Pastel1_r, Pastel1, gray_r, PuRd_r, Spectral_r, BuPu, YlGnBu_r, copper, gist_earth_r, Set3_r, OrRd, PuBu_r, winter_r, RdBu, jet, bone_r, gist_earth, Oranges, RdYlGn_r, PiYG, YlGn, binary_r, gist_gray_r, gist_gray, flag, RdBu_r, BrBG, Reds, GnBu_r, BrBG_r, Reds_r, RdGy, PuRd, Accent_r, Blues, Greys, autumn, PRGn_r, Greys_r, pink, binary, winter, gist_yarg_r, RdYlBu_r, hot, YlOrBr, BuPu_r, Purples_r, PiYG_r, YlGn_r, Blues_r, YlOrBr_r, Purples, autumn_r, BuGn_r, Set1_r, PuOr, PuBuGn
}}}



---

archive/issue_comments_036867.json:
```json
{
    "body": "I am not sure what you mean with this comment.\n\nThe proposed patch add a mention to the docstring saying that you have to type cmap_help() to get detailed info on colormaps.  This function contains a list of all defined colormaps in the installed matplotlib version.  The list is automatically fetched just like the current error code for cmap does right now.\n\nIs this what you want?  If not, what do you want?",
    "created_at": "2008-12-29T06:38:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4878#issuecomment-36867",
    "user": "https://trac.sagemath.org/admin/accounts/users/abergeron"
}
```

I am not sure what you mean with this comment.

The proposed patch add a mention to the docstring saying that you have to type cmap_help() to get detailed info on colormaps.  This function contains a list of all defined colormaps in the installed matplotlib version.  The list is automatically fetched just like the current error code for cmap does right now.

Is this what you want?  If not, what do you want?



---

archive/issue_comments_036868.json:
```json
{
    "body": "Arnaud: I think you have addressed William's complaint in your second patch. (I was basically arguing the same thing, though maybe not so clearly.) You describe cmap as one of the options to density_plot and \"Type \"cmap_hlp() for more information\". The patch 4884 (which has a positive review) impliments that.\n\nWith the second patch, I think this is an excellent addition. Both patches to be applied together with that in #4884.\n\nPositive review. Thanks Arnaud!",
    "created_at": "2008-12-29T11:52:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4878#issuecomment-36868",
    "user": "https://github.com/wdjoyner"
}
```

Arnaud: I think you have addressed William's complaint in your second patch. (I was basically arguing the same thing, though maybe not so clearly.) You describe cmap as one of the options to density_plot and "Type "cmap_hlp() for more information". The patch 4884 (which has a positive review) impliments that.

With the second patch, I think this is an excellent addition. Both patches to be applied together with that in #4884.

Positive review. Thanks Arnaud!



---

archive/issue_comments_036869.json:
```json
{
    "body": "Since there is heavy discussion at #4884, I will wait until that settles before updating the patch here to conform with whatever interface (and documentation) will be decided upon.",
    "created_at": "2008-12-29T20:45:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4878#issuecomment-36869",
    "user": "https://trac.sagemath.org/admin/accounts/users/abergeron"
}
```

Since there is heavy discussion at #4884, I will wait until that settles before updating the patch here to conform with whatever interface (and documentation) will be decided upon.



---

archive/issue_comments_036870.json:
```json
{
    "body": "#4884 is settled.  Since there is no change of interface, back to positive.",
    "created_at": "2008-12-30T01:52:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4878#issuecomment-36870",
    "user": "https://trac.sagemath.org/admin/accounts/users/abergeron"
}
```

#4884 is settled.  Since there is no change of interface, back to positive.



---

archive/issue_comments_036871.json:
```json
{
    "body": "Merged both patches in Sage 3.3.alpha0",
    "created_at": "2009-01-12T01:54:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4878#issuecomment-36871",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.3.alpha0



---

archive/issue_events_011246.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-12T01:54:27Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4878",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4878#event-11246"
}
```



---

archive/issue_events_011247.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-12T01:54:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4878",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4878#event-11247"
}
```



---

archive/issue_comments_036872.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-12T01:54:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4878#issuecomment-36872",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_036873.json:
```json
{
    "body": "Is it possible for someone to attach an image or two to this ticket? I'm looking for an image of a plot resulting from using the function `density_plot()`. What I have in mind is something along the line of the images attached to #2770 and #4976. Such images should serve as a high-level summary of what a (new) plotting function can do. And having such images mean that they can be referred to from a release tour note on the Sage wiki. I don't always have the latest alpha on my work machine, only the latest stable version.",
    "created_at": "2009-02-07T04:10:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4878#issuecomment-36873",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Is it possible for someone to attach an image or two to this ticket? I'm looking for an image of a plot resulting from using the function `density_plot()`. What I have in mind is something along the line of the images attached to #2770 and #4976. Such images should serve as a high-level summary of what a (new) plotting function can do. And having such images mean that they can be referred to from a release tour note on the Sage wiki. I don't always have the latest alpha on my work machine, only the latest stable version.



---

archive/issue_comments_036874.json:
```json
{
    "body": "Attachment [4878_example.png](tarball://root/attachments/some-uuid/ticket4878/4878_example.png) by abergeron created at 2009-02-18 18:41:46\n\nexample image for mvngu",
    "created_at": "2009-02-18T18:41:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4878#issuecomment-36874",
    "user": "https://trac.sagemath.org/admin/accounts/users/abergeron"
}
```

Attachment [4878_example.png](tarball://root/attachments/some-uuid/ticket4878/4878_example.png) by abergeron created at 2009-02-18 18:41:46

example image for mvngu



---

archive/issue_comments_036875.json:
```json
{
    "body": "Thanks, Arnaud, for attaching that sample image. Just out of curiosity, what code did you use to produce that plot?",
    "created_at": "2009-02-20T04:44:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4878#issuecomment-36875",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Thanks, Arnaud, for attaching that sample image. Just out of curiosity, what code did you use to produce that plot?



---

archive/issue_comments_036876.json:
```json
{
    "body": "Attachment [trac_4878-sample-plot-bw.png](tarball://root/attachments/some-uuid/ticket4878/trac_4878-sample-plot-bw.png) by mvngu created at 2009-02-20 04:50:47\n\nanother sample plot in black and white",
    "created_at": "2009-02-20T04:50:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4878#issuecomment-36876",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_4878-sample-plot-bw.png](tarball://root/attachments/some-uuid/ticket4878/trac_4878-sample-plot-bw.png) by mvngu created at 2009-02-20 04:50:47

another sample plot in black and white



---

archive/issue_comments_036877.json:
```json
{
    "body": "The image `trac_4878-sample-plot-bw.png` is another sample plot showcasing the new function `density_plot()`. The image is in gray scale.",
    "created_at": "2009-02-20T04:52:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4878#issuecomment-36877",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The image `trac_4878-sample-plot-bw.png` is another sample plot showcasing the new function `density_plot()`. The image is in gray scale.



---

archive/issue_comments_036878.json:
```json
{
    "body": "Hi Minh,\n\nany reason you don't want to attach those snapshots to a wiki page directly? It doesn't matter too much, but that is what we do for all the interact examples, too and that way it would be all on one host.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T05:39:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4878#issuecomment-36878",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi Minh,

any reason you don't want to attach those snapshots to a wiki page directly? It doesn't matter too much, but that is what we do for all the interact examples, too and that way it would be all on one host.

Cheers,

Michael



---

archive/issue_comments_036879.json:
```json
{
    "body": "`@`mvngu:\n\nThis code: \n\n```\nsage: density_plot(sin(x^2 + y^2)*cos(x)*sin(y), (-4, 4), (-4, 4), cmap='jet', plot_points=100)\n```\n\nfrom the examples.",
    "created_at": "2009-02-20T07:07:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4878#issuecomment-36879",
    "user": "https://trac.sagemath.org/admin/accounts/users/abergeron"
}
```

`@`mvngu:

This code: 

```
sage: density_plot(sin(x^2 + y^2)*cos(x)*sin(y), (-4, 4), (-4, 4), cmap='jet', plot_points=100)
```

from the examples.



---

archive/issue_comments_036880.json:
```json
{
    "body": "Replying to [comment:12 mabshoff]:\n> Hi Minh,\n> \n> any reason you don't want to attach those snapshots to a wiki page directly? \n> It doesn't matter too much, but that is what we do for all the interact examples, \n> too and that way it would be all on one host.\n\nPreviously, I didn't know how to attach a file to a wiki page. But don't worry, I sort of know it now. The images I referred to are now attached to the release tour wiki.",
    "created_at": "2009-02-23T04:41:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4878#issuecomment-36880",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:12 mabshoff]:
> Hi Minh,
> 
> any reason you don't want to attach those snapshots to a wiki page directly? 
> It doesn't matter too much, but that is what we do for all the interact examples, 
> too and that way it would be all on one host.

Previously, I didn't know how to attach a file to a wiki page. But don't worry, I sort of know it now. The images I referred to are now attached to the release tour wiki.



---

archive/issue_comments_036881.json:
```json
{
    "body": "Replying to [comment:13 abergeron]:\n> `@`mvngu:\n> \n> This code: \n> \n> \n> ```\n> sage: density_plot(sin(x^2 + y^2)*cos(x)*sin(y), (-4, 4), (-4, 4), cmap='jet', plot_points=100)\n> ```\n> \n> from the examples.\n\nGreatly appreciated, Arnaud. And the plot looks damn cool :-)",
    "created_at": "2009-02-23T04:43:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4878",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4878#issuecomment-36881",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:13 abergeron]:
> `@`mvngu:
> 
> This code: 
> 
> 
> ```
> sage: density_plot(sin(x^2 + y^2)*cos(x)*sin(y), (-4, 4), (-4, 4), cmap='jet', plot_points=100)
> ```
> 
> from the examples.

Greatly appreciated, Arnaud. And the plot looks damn cool :-)
