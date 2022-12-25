# Issue 9849: make style of documentation consistent with sagemath.org

archive/issues_009849.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @rbeezer\n\nKeywords: style\n\nThis was proposed in the following thread at `sage-devel`:\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/73e3c4c995577df0\n\nand a few people voiced support, so a patch will be attached.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9850\n\n",
    "created_at": "2010-09-02T18:53:58Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.1",
    "title": "make style of documentation consistent with sagemath.org",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9849",
    "user": "https://github.com/nilesjohnson"
}
```
Assignee: mvngu

CC:  @rbeezer

Keywords: style

This was proposed in the following thread at `sage-devel`:

http://groups.google.com/group/sage-devel/browse_thread/thread/73e3c4c995577df0

and a few people voiced support, so a patch will be attached.

Issue created by migration from https://trac.sagemath.org/ticket/9850





---

archive/issue_comments_097044.json:
```json
{
    "body": "use color scheme of sagemath.org",
    "created_at": "2010-09-02T18:57:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9849#issuecomment-97044",
    "user": "https://github.com/nilesjohnson"
}
```

use color scheme of sagemath.org



---

archive/issue_comments_097045.json:
```json
{
    "body": "Attachment [trac_9850_doc_style.patch](tarball://root/attachments/some-uuid/ticket9850/trac_9850_doc_style.patch) by @nilesjohnson created at 2010-09-02 19:09:02\n\nA first version is now attached.  It simply sets some new colors using the customization options for the Sphinx default theme:\n\nhttp://sphinx.pocoo.org/theming.html\n\nThe second attachment shows a screenshot of what this patch does.",
    "created_at": "2010-09-02T19:09:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9849#issuecomment-97045",
    "user": "https://github.com/nilesjohnson"
}
```

Attachment [trac_9850_doc_style.patch](tarball://root/attachments/some-uuid/ticket9850/trac_9850_doc_style.patch) by @nilesjohnson created at 2010-09-02 19:09:02

A first version is now attached.  It simply sets some new colors using the customization options for the Sphinx default theme:

http://sphinx.pocoo.org/theming.html

The second attachment shows a screenshot of what this patch does.



---

archive/issue_comments_097046.json:
```json
{
    "body": "Niles, could you later rework the patch to move the changes to\n\n`SAGE_ROOT/devel/sage/doc/common/themes/sage/theme.conf`\n\ninstead?  You can set [pygments_style](http://sphinx.pocoo.org/config.html#confval-pygments_style) to use alternate syntax highlights.  Here's a list of Pygments' builtin styles:\n\n```python\nsage: from pygments.styles import STYLE_MAP\nsage: STYLE_MAP.keys()\n['manni', 'colorful', 'murphy', 'autumn', 'bw', 'pastie', 'native', 'perldoc', 'borland', 'trac', 'default', 'fruity', 'vs', 'emacs', 'friendly']\n```\n",
    "created_at": "2010-09-02T21:55:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9849#issuecomment-97046",
    "user": "https://github.com/qed777"
}
```

Niles, could you later rework the patch to move the changes to

`SAGE_ROOT/devel/sage/doc/common/themes/sage/theme.conf`

instead?  You can set [pygments_style](http://sphinx.pocoo.org/config.html#confval-pygments_style) to use alternate syntax highlights.  Here's a list of Pygments' builtin styles:

```python
sage: from pygments.styles import STYLE_MAP
sage: STYLE_MAP.keys()
['manni', 'colorful', 'murphy', 'autumn', 'bw', 'pastie', 'native', 'perldoc', 'borland', 'trac', 'default', 'fruity', 'vs', 'emacs', 'friendly']
```




---

archive/issue_comments_097047.json:
```json
{
    "body": "Replying to [comment:2 mpatel]:\n> Niles, could you later rework the patch to move the changes to\n> \n> `SAGE_ROOT/devel/sage/doc/common/themes/sage/theme.conf`\n\nI did try this, but I'm afraid it didn't seem to work.  I tried both uncommenting the lines that were already there, such as \n\n\n```\nfooterbgcolor    =  #B8B9F6\n```\n\n\nand also adding the dict `html_theme_options` from `conf.py`, but neither of these were recognized . . . in fact, when I change `theme.conf` and try to rebuild the documentation, I get \"all targets are up to date\", so maybe I need to issue a different rebuild command (rather than, e.g. `sage -docbuild constructions html`).\n\n\n\n> \n> You can set [pygments_style](http://sphinx.pocoo.org/config.html#confval-pygments_style) to use alternate syntax highlights.  \n\nthis also doesn't seem to work from `theme.conf`, but does from `conf.py`.\n\n\n\n> Here's a list of Pygments' builtin styles: \n> \n\n```\n #!python\n sage: from pygments.styles import STYLE_MAP\n sage: STYLE_MAP.keys()\n ['manni', 'colorful', 'murphy', 'autumn', 'bw', 'pastie', 'native', 'perldoc', 'borland', 'trac', 'default', 'fruity', 'vs', 'emacs', 'friendly']\n }}}\n\n>\n\nI tried these out, but most of them are worse than the default (which is not the same as when I set `pygments_style = 'default'`).  `manni` comes the closest to being usable (and better), but the color of sage output is too-light gray.",
    "created_at": "2010-09-03T20:37:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9849#issuecomment-97047",
    "user": "https://github.com/nilesjohnson"
}
```

Replying to [comment:2 mpatel]:
> Niles, could you later rework the patch to move the changes to
> 
> `SAGE_ROOT/devel/sage/doc/common/themes/sage/theme.conf`

I did try this, but I'm afraid it didn't seem to work.  I tried both uncommenting the lines that were already there, such as 


```
footerbgcolor    =  #B8B9F6
```


and also adding the dict `html_theme_options` from `conf.py`, but neither of these were recognized . . . in fact, when I change `theme.conf` and try to rebuild the documentation, I get "all targets are up to date", so maybe I need to issue a different rebuild command (rather than, e.g. `sage -docbuild constructions html`).



> 
> You can set [pygments_style](http://sphinx.pocoo.org/config.html#confval-pygments_style) to use alternate syntax highlights.  

this also doesn't seem to work from `theme.conf`, but does from `conf.py`.



> Here's a list of Pygments' builtin styles: 
> 

```
 #!python
 sage: from pygments.styles import STYLE_MAP
 sage: STYLE_MAP.keys()
 ['manni', 'colorful', 'murphy', 'autumn', 'bw', 'pastie', 'native', 'perldoc', 'borland', 'trac', 'default', 'fruity', 'vs', 'emacs', 'friendly']
 }}}

>

I tried these out, but most of them are worse than the default (which is not the same as when I set `pygments_style = 'default'`).  `manni` comes the closest to being usable (and better), but the color of sage output is too-light gray.



---

archive/issue_comments_097048.json:
```json
{
    "body": "> I get \"all targets are up to date\"\n\nThe thread on sage-devel cited in the description suggested using `sage -docbuild all html -j -S -a`; the flag \"-S\" says to pass the rest of the options to Sphinx, and \"-a\" tells Sphinx to build all files, not just changed ones.  So this command should force the whole thing to be rebuilt.\n\n(It would probably suffice for your purposes to use `sage -docbuild tutorial html -j -S -a` to just build one document instead of all of them, of course.)",
    "created_at": "2010-09-03T20:46:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9849#issuecomment-97048",
    "user": "https://github.com/jhpalmieri"
}
```

> I get "all targets are up to date"

The thread on sage-devel cited in the description suggested using `sage -docbuild all html -j -S -a`; the flag "-S" says to pass the rest of the options to Sphinx, and "-a" tells Sphinx to build all files, not just changed ones.  So this command should force the whole thing to be rebuilt.

(It would probably suffice for your purposes to use `sage -docbuild tutorial html -j -S -a` to just build one document instead of all of them, of course.)



---

archive/issue_comments_097049.json:
```json
{
    "body": "Replying to [comment:4 jhpalmieri]:\n> > I get \"all targets are up to date\"\n> \n> The thread on sage-devel cited in the description suggested using `sage -docbuild all html -j -S -a`;\n\nah, thanks for that reminder :)  \n\nA little more testing and I still can't get it to work, but I'm getting closer to the issue.  Setting the `html_style_options` dict does nothing -- style reverts to usual settings.  Uncommenting the lines as I indicated above will obviously not work: `#` is the comment character!  Wrapping the css colors in quotes, as in \n\n\n```\nfooterbgcolor    =  \"#B8B9F6\"\n```\n\n\ndoes *something*, but not the expected thing.  I.e., the color changes, but not to what I indicated . . . confusing.",
    "created_at": "2010-09-03T21:06:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9849#issuecomment-97049",
    "user": "https://github.com/nilesjohnson"
}
```

Replying to [comment:4 jhpalmieri]:
> > I get "all targets are up to date"
> 
> The thread on sage-devel cited in the description suggested using `sage -docbuild all html -j -S -a`;

ah, thanks for that reminder :)  

A little more testing and I still can't get it to work, but I'm getting closer to the issue.  Setting the `html_style_options` dict does nothing -- style reverts to usual settings.  Uncommenting the lines as I indicated above will obviously not work: `#` is the comment character!  Wrapping the css colors in quotes, as in 


```
footerbgcolor    =  "#B8B9F6"
```


does *something*, but not the expected thing.  I.e., the color changes, but not to what I indicated . . . confusing.



---

archive/issue_comments_097050.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-11T12:06:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9849#issuecomment-97050",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097051.json:
```json
{
    "body": "When (re)building documentation, I would first delete the whole output directory and then proceed with the (re)building: \n\n\n```sh\n$ cd SAGE_ROOT\n$ rm -rf devel/sage-main/doc/output/\n$ ./sage -docbuild --no-pdf-links all html 2>&1 | tee -a dochtml.log\n```\n\n\nThis guarantees that the documentation I'm interested in (re)building would build, regardless of whether I have made any changes. In niles' case where changes were observed to not take place, I find the approach above worked for me. With that in mind, I have attached a reviewer patch with the following changes:\n\n* Use a very pale yellow for the code background colour.\n* Annotate most of the hex colour code with descriptive English names. All names were taken from [this site](http://www.perbang.dk).\n\nSee the attachment [attachment:reviewer-style.png] for a preview of the new colour for the code background. I'm OK with niles' patch. What we need now is for someone other than me to look over my changes.",
    "created_at": "2010-09-11T12:06:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9849#issuecomment-97051",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

When (re)building documentation, I would first delete the whole output directory and then proceed with the (re)building: 


```sh
$ cd SAGE_ROOT
$ rm -rf devel/sage-main/doc/output/
$ ./sage -docbuild --no-pdf-links all html 2>&1 | tee -a dochtml.log
```


This guarantees that the documentation I'm interested in (re)building would build, regardless of whether I have made any changes. In niles' case where changes were observed to not take place, I find the approach above worked for me. With that in mind, I have attached a reviewer patch with the following changes:

* Use a very pale yellow for the code background colour.
* Annotate most of the hex colour code with descriptive English names. All names were taken from [this site](http://www.perbang.dk).

See the attachment [attachment:reviewer-style.png] for a preview of the new colour for the code background. I'm OK with niles' patch. What we need now is for someone other than me to look over my changes.



---

archive/issue_events_024794.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-09-11T12:06:39Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9849",
    "milestone": "sage-4.6",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9849#event-24794"
}
```



---

archive/issue_comments_097052.json:
```json
{
    "body": "Replying to [comment:2 mpatel]:\n> Niles, could you later rework the patch to move the changes to\n> \n> `SAGE_ROOT/devel/sage/doc/common/themes/sage/theme.conf`\n> \n> instead?  \n\nI agree with this comment.  I'm attaching a patch (intended to replace the others) which does this.",
    "created_at": "2010-09-11T17:42:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9849#issuecomment-97052",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:2 mpatel]:
> Niles, could you later rework the patch to move the changes to
> 
> `SAGE_ROOT/devel/sage/doc/common/themes/sage/theme.conf`
> 
> instead?  

I agree with this comment.  I'm attaching a patch (intended to replace the others) which does this.



---

archive/issue_comments_097053.json:
```json
{
    "body": "Attachment [trac_9850-theme-conf.patch](tarball://root/attachments/some-uuid/ticket9850/trac_9850-theme-conf.patch) by @jhpalmieri created at 2010-09-11 18:01:32\n\nuse in place of all other patches",
    "created_at": "2010-09-11T18:01:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9849#issuecomment-97053",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_9850-theme-conf.patch](tarball://root/attachments/some-uuid/ticket9850/trac_9850-theme-conf.patch) by @jhpalmieri created at 2010-09-11 18:01:32

use in place of all other patches



---

archive/issue_comments_097054.json:
```json
{
    "body": "Note: Because of the format of theme.conf files, I think the comments need to look a little different.",
    "created_at": "2010-09-11T18:02:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9849#issuecomment-97054",
    "user": "https://github.com/jhpalmieri"
}
```

Note: Because of the format of theme.conf files, I think the comments need to look a little different.



---

archive/issue_comments_097055.json:
```json
{
    "body": "I applied the most recent patch (by jpalmieri) and totally rebuilt the html reference manual.\n\nIt looks real good to me - the light yellow for code blocks seems to contrast well with python keywords (green), sage prompt (orangish-brown), strings (blue) and most-everything-else (black).  It seems just a slightly lighter shade than Trac uses for the description box at the top of a ticket.  No matter what, a big improvement to my eye over the previous green.\n\nThere's a few heavyweights on this ticket already, and maybe there are more additions or modifications coming (I can't see any myself).  So I don't think I'm the one to flip this to positive review, but I'm a big +1 to the whole ticket, and specifically to John's roll-up patch applying properly and to Minh's design sense with the yellow code blocks.\n\nThanks Niles for starting this, and thanks to Mitesh, Mihn and John for their contributions.\n\nRob",
    "created_at": "2010-09-11T20:23:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9849#issuecomment-97055",
    "user": "https://github.com/rbeezer"
}
```

I applied the most recent patch (by jpalmieri) and totally rebuilt the html reference manual.

It looks real good to me - the light yellow for code blocks seems to contrast well with python keywords (green), sage prompt (orangish-brown), strings (blue) and most-everything-else (black).  It seems just a slightly lighter shade than Trac uses for the description box at the top of a ticket.  No matter what, a big improvement to my eye over the previous green.

There's a few heavyweights on this ticket already, and maybe there are more additions or modifications coming (I can't see any myself).  So I don't think I'm the one to flip this to positive review, but I'm a big +1 to the whole ticket, and specifically to John's roll-up patch applying properly and to Minh's design sense with the yellow code blocks.

Thanks Niles for starting this, and thanks to Mitesh, Mihn and John for their contributions.

Rob



---

archive/issue_comments_097056.json:
```json
{
    "body": "This looks great -- thanks for the help.  I do think the logo could look better though; I think John had planned to work on this, and maybe still is.  If not, I've uploaded one which just makes the white background transparent (\"use BW copy of layer as layer mask (inverted)\" from the GIMP).  I know there are issues with transparent pngs in certain browsers, but that issue is quickly becoming history.  Anyway, I or someone else could easily change the background color to purple if it's deemed necessary.\n\n* logo: [attachment:sagelogo-transp.png]\n* screenshot: [attachment:with-transparent-logo.png]",
    "created_at": "2010-09-12T12:00:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9849#issuecomment-97056",
    "user": "https://github.com/nilesjohnson"
}
```

This looks great -- thanks for the help.  I do think the logo could look better though; I think John had planned to work on this, and maybe still is.  If not, I've uploaded one which just makes the white background transparent ("use BW copy of layer as layer mask (inverted)" from the GIMP).  I know there are issues with transparent pngs in certain browsers, but that issue is quickly becoming history.  Anyway, I or someone else could easily change the background color to purple if it's deemed necessary.

* logo: [attachment:sagelogo-transp.png]
* screenshot: [attachment:with-transparent-logo.png]



---

archive/issue_comments_097057.json:
```json
{
    "body": "Attachment [trac_9850-logo.patch](tarball://root/attachments/some-uuid/ticket9850/trac_9850-logo.patch) by mvngu created at 2010-09-12 15:15:40\n\nThe transparent background for the Sage logo looks nice. It works fine for me both in Firefox and Chrome. We need someone to test on a Mac with Safari. I have attached the patch [attachment:trac_9850-logo.patch] produced in niles' name that puts niles' logo under revision control. See the ticket description for instructions on how to apply patches and for relevant screenshots. Positive review from me. See this [sage-devel thread](http://groups.google.com/group/sage-devel/browse_thread/thread/b94df222f7c84620) for my invitation to more people to look over the new style to ensure that it's pleasing to the eyes.",
    "created_at": "2010-09-12T15:15:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9849#issuecomment-97057",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_9850-logo.patch](tarball://root/attachments/some-uuid/ticket9850/trac_9850-logo.patch) by mvngu created at 2010-09-12 15:15:40

The transparent background for the Sage logo looks nice. It works fine for me both in Firefox and Chrome. We need someone to test on a Mac with Safari. I have attached the patch [attachment:trac_9850-logo.patch] produced in niles' name that puts niles' logo under revision control. See the ticket description for instructions on how to apply patches and for relevant screenshots. Positive review from me. See this [sage-devel thread](http://groups.google.com/group/sage-devel/browse_thread/thread/b94df222f7c84620) for my invitation to more people to look over the new style to ensure that it's pleasing to the eyes.



---

archive/issue_comments_097058.json:
```json
{
    "body": "Looks fine on my Mac with both Safari and Firefox.  When accessed remotely (I put a copy of the tutorial [on sage.math](http://sage.math.washington.edu/home/palmieri/misc/tutorial/)), it also looks fine on an iPhone.",
    "created_at": "2010-09-12T15:31:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9849#issuecomment-97058",
    "user": "https://github.com/jhpalmieri"
}
```

Looks fine on my Mac with both Safari and Firefox.  When accessed remotely (I put a copy of the tutorial [on sage.math](http://sage.math.washington.edu/home/palmieri/misc/tutorial/)), it also looks fine on an iPhone.



---

archive/issue_comments_097059.json:
```json
{
    "body": "Replying to [comment:14 jhpalmieri]:\n> I put a copy of the tutorial [on sage.math](http://sage.math.washington.edu/home/palmieri/misc/tutorial/)\n\nThanks!  It also renders as expected with Opera on Mac.  The site [netrenderer](http://ipinfo.info/netrenderer/) provides a service rendering pages with various versions of internet explorer and returning an image; in case no one has a windows machine to test this on.  According to those images, we have the following:\n\n* IE 8: renders the page just like other browsers do\n* IE 7: same, except the sage logo (which looks fine) shows up on the right side of the page, between the \"next\" and \"index\" buttons; this happens with the  [current documentation](http://www.sagemath.org/doc/tutorial/index.html) too though.\n* IE 6: same logo placement as IE 7, and transparent background shows as gray\n\nprobably none of these are show-stoppers, but worth mentioning I think.",
    "created_at": "2010-09-12T18:27:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9849#issuecomment-97059",
    "user": "https://github.com/nilesjohnson"
}
```

Replying to [comment:14 jhpalmieri]:
> I put a copy of the tutorial [on sage.math](http://sage.math.washington.edu/home/palmieri/misc/tutorial/)

Thanks!  It also renders as expected with Opera on Mac.  The site [netrenderer](http://ipinfo.info/netrenderer/) provides a service rendering pages with various versions of internet explorer and returning an image; in case no one has a windows machine to test this on.  According to those images, we have the following:

* IE 8: renders the page just like other browsers do
* IE 7: same, except the sage logo (which looks fine) shows up on the right side of the page, between the "next" and "index" buttons; this happens with the  [current documentation](http://www.sagemath.org/doc/tutorial/index.html) too though.
* IE 6: same logo placement as IE 7, and transparent background shows as gray

probably none of these are show-stoppers, but worth mentioning I think.



---

archive/issue_comments_097060.json:
```json
{
    "body": "Attachment [trac_9850-reviewer.patch](tarball://root/attachments/some-uuid/ticket9850/trac_9850-reviewer.patch) by mvngu created at 2010-09-13 09:22:39\n\nI have attached the reviewer patch [attachment:trac_9850-reviewer.patch] that addresses the comments on this [sage-devel message](http://groups.google.com/group/sage-devel/msg/784c039090fddc6c). The documentation generated using this new style can be found [here](http://sage.math.washington.edu/home/mvngu/patch/9850-docstyle/doc/). See the ticket description for instructions on how to apply patches.",
    "created_at": "2010-09-13T09:22:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9849#issuecomment-97060",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_9850-reviewer.patch](tarball://root/attachments/some-uuid/ticket9850/trac_9850-reviewer.patch) by mvngu created at 2010-09-13 09:22:39

I have attached the reviewer patch [attachment:trac_9850-reviewer.patch] that addresses the comments on this [sage-devel message](http://groups.google.com/group/sage-devel/msg/784c039090fddc6c). The documentation generated using this new style can be found [here](http://sage.math.washington.edu/home/mvngu/patch/9850-docstyle/doc/). See the ticket description for instructions on how to apply patches.



---

archive/issue_comments_097061.json:
```json
{
    "body": "Attachment [doc-home.png](tarball://root/attachments/some-uuid/ticket9850/doc-home.png) by mvngu created at 2010-09-13 09:34:17",
    "created_at": "2010-09-13T09:34:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9849#issuecomment-97061",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [doc-home.png](tarball://root/attachments/some-uuid/ticket9850/doc-home.png) by mvngu created at 2010-09-13 09:34:17



---

archive/issue_comments_097062.json:
```json
{
    "body": "Attachment [inline-code.png](tarball://root/attachments/some-uuid/ticket9850/inline-code.png) by mvngu created at 2010-09-13 09:34:53",
    "created_at": "2010-09-13T09:34:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9849#issuecomment-97062",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [inline-code.png](tarball://root/attachments/some-uuid/ticket9850/inline-code.png) by mvngu created at 2010-09-13 09:34:53



---

archive/issue_comments_097063.json:
```json
{
    "body": "Attachment [reference-home.png](tarball://root/attachments/some-uuid/ticket9850/reference-home.png) by mvngu created at 2010-09-13 09:36:52",
    "created_at": "2010-09-13T09:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9849#issuecomment-97063",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [reference-home.png](tarball://root/attachments/some-uuid/ticket9850/reference-home.png) by mvngu created at 2010-09-13 09:36:52



---

archive/issue_comments_097064.json:
```json
{
    "body": "What needs to be done to give this a positive review?  I think it looks good.  My contribution as an author was pretty minor, so can we give it a positive review, especially given the other positive comments on the ticket so far?",
    "created_at": "2010-11-02T21:23:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9849#issuecomment-97064",
    "user": "https://github.com/jhpalmieri"
}
```

What needs to be done to give this a positive review?  I think it looks good.  My contribution as an author was pretty minor, so can we give it a positive review, especially given the other positive comments on the ticket so far?



---

archive/issue_comments_097065.json:
```json
{
    "body": "Replying to [comment:18 jhpalmieri]:\n> What needs to be done to give this a positive review?  I think it looks good.  My contribution as an author was pretty minor, so can we give it a positive review, especially given the other positive comments on the ticket so far?\n\nI think this is ready for a positive review. Of course, I can't officially set the ticket to positive, but I'm OK with the two patches that are not mine. See the ticket description for the rebuilt documentation using the new style.",
    "created_at": "2010-11-03T06:47:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9849#issuecomment-97065",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:18 jhpalmieri]:
> What needs to be done to give this a positive review?  I think it looks good.  My contribution as an author was pretty minor, so can we give it a positive review, especially given the other positive comments on the ticket so far?

I think this is ready for a positive review. Of course, I can't officially set the ticket to positive, but I'm OK with the two patches that are not mine. See the ticket description for the rebuilt documentation using the new style.



---

archive/issue_comments_097066.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-03T08:27:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9849#issuecomment-97066",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_097067.json:
```json
{
    "body": "The new style looks great.  I suggest that we open new ticket(s) for any further changes.  Thanks to everyone for their contributions!",
    "created_at": "2010-11-03T08:27:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9849#issuecomment-97067",
    "user": "https://github.com/qed777"
}
```

The new style looks great.  I suggest that we open new ticket(s) for any further changes.  Thanks to everyone for their contributions!



---

archive/issue_events_024795.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-11-10T22:20:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9849",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9849#event-24795"
}
```



---

archive/issue_comments_097068.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-11-10T22:20:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9849",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9849#issuecomment-97068",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
