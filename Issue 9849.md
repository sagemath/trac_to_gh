# Issue 9849: make style of documentation consistent with sagemath.org

Issue created by migration from https://trac.sagemath.org/ticket/9850

Original creator: niles

Original creation time: 2010-09-02 18:53:58

Assignee: mvngu

CC:  rbeezer

Keywords: style

This was proposed in the following thread at `sage-devel`:

http://groups.google.com/group/sage-devel/browse_thread/thread/73e3c4c995577df0

and a few people voiced support, so a patch will be attached.


---

Comment by niles created at 2010-09-02 18:57:01

use color scheme of sagemath.org


---

Attachment

A first version is now attached.  It simply sets some new colors using the customization options for the Sphinx default theme:

http://sphinx.pocoo.org/theming.html

The second attachment shows a screenshot of what this patch does.


---

Comment by mpatel created at 2010-09-02 21:55:18

Niles, could you later rework the patch to move the changes to

`SAGE_ROOT/devel/sage/doc/common/themes/sage/theme.conf`

instead?  You can set [pygments_style](http://sphinx.pocoo.org/config.html#confval-pygments_style) to use alternate syntax highlights.  Here's a list of Pygments' builtin styles:

```python
sage: from pygments.styles import STYLE_MAP
sage: STYLE_MAP.keys()
['manni', 'colorful', 'murphy', 'autumn', 'bw', 'pastie', 'native', 'perldoc', 'borland', 'trac', 'default', 'fruity', 'vs', 'emacs', 'friendly']
```



---

Comment by niles created at 2010-09-03 20:37:23

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

Comment by jhpalmieri created at 2010-09-03 20:46:47

> I get "all targets are up to date"

The thread on sage-devel cited in the description suggested using `sage -docbuild all html -j -S -a`; the flag "-S" says to pass the rest of the options to Sphinx, and "-a" tells Sphinx to build all files, not just changed ones.  So this command should force the whole thing to be rebuilt.

(It would probably suffice for your purposes to use `sage -docbuild tutorial html -j -S -a` to just build one document instead of all of them, of course.)


---

Comment by niles created at 2010-09-03 21:06:56

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

Comment by mvngu created at 2010-09-11 12:06:39

Changing status from new to needs_review.


---

Comment by mvngu created at 2010-09-11 12:06:39

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

Comment by jhpalmieri created at 2010-09-11 17:42:36

Replying to [comment:2 mpatel]:
> Niles, could you later rework the patch to move the changes to
> 
> `SAGE_ROOT/devel/sage/doc/common/themes/sage/theme.conf`
> 
> instead?  

I agree with this comment.  I'm attaching a patch (intended to replace the others) which does this.


---

Attachment

use in place of all other patches


---

Comment by jhpalmieri created at 2010-09-11 18:02:13

Note: Because of the format of theme.conf files, I think the comments need to look a little different.


---

Comment by rbeezer created at 2010-09-11 20:23:06

I applied the most recent patch (by jpalmieri) and totally rebuilt the html reference manual.

It looks real good to me - the light yellow for code blocks seems to contrast well with python keywords (green), sage prompt (orangish-brown), strings (blue) and most-everything-else (black).  It seems just a slightly lighter shade than Trac uses for the description box at the top of a ticket.  No matter what, a big improvement to my eye over the previous green.

There's a few heavyweights on this ticket already, and maybe there are more additions or modifications coming (I can't see any myself).  So I don't think I'm the one to flip this to positive review, but I'm a big +1 to the whole ticket, and specifically to John's roll-up patch applying properly and to Minh's design sense with the yellow code blocks.

Thanks Niles for starting this, and thanks to Mitesh, Mihn and John for their contributions.

Rob


---

Comment by niles created at 2010-09-12 12:00:07

This looks great -- thanks for the help.  I do think the logo could look better though; I think John had planned to work on this, and maybe still is.  If not, I've uploaded one which just makes the white background transparent ("use BW copy of layer as layer mask (inverted)" from the GIMP).  I know there are issues with transparent pngs in certain browsers, but that issue is quickly becoming history.  Anyway, I or someone else could easily change the background color to purple if it's deemed necessary.

 * logo: [attachment:sagelogo-transp.png]
 * screenshot: [attachment:with-transparent-logo.png]


---

Attachment

The transparent background for the Sage logo looks nice. It works fine for me both in Firefox and Chrome. We need someone to test on a Mac with Safari. I have attached the patch [attachment:trac_9850-logo.patch] produced in niles' name that puts niles' logo under revision control. See the ticket description for instructions on how to apply patches and for relevant screenshots. Positive review from me. See this [sage-devel thread](http://groups.google.com/group/sage-devel/browse_thread/thread/b94df222f7c84620) for my invitation to more people to look over the new style to ensure that it's pleasing to the eyes.


---

Comment by jhpalmieri created at 2010-09-12 15:31:25

Looks fine on my Mac with both Safari and Firefox.  When accessed remotely (I put a copy of the tutorial [on sage.math](http://sage.math.washington.edu/home/palmieri/misc/tutorial/)), it also looks fine on an iPhone.


---

Comment by niles created at 2010-09-12 18:27:10

Replying to [comment:14 jhpalmieri]:
> I put a copy of the tutorial [on sage.math](http://sage.math.washington.edu/home/palmieri/misc/tutorial/)

Thanks!  It also renders as expected with Opera on Mac.  The site [netrenderer](http://ipinfo.info/netrenderer/) provides a service rendering pages with various versions of internet explorer and returning an image; in case no one has a windows machine to test this on.  According to those images, we have the following:

 * IE 8: renders the page just like other browsers do
 * IE 7: same, except the sage logo (which looks fine) shows up on the right side of the page, between the "next" and "index" buttons; this happens with the  [current documentation](http://www.sagemath.org/doc/tutorial/index.html) too though.
 * IE 6: same logo placement as IE 7, and transparent background shows as gray

probably none of these are show-stoppers, but worth mentioning I think.


---

Attachment

I have attached the reviewer patch [attachment:trac_9850-reviewer.patch] that addresses the comments on this [sage-devel message](http://groups.google.com/group/sage-devel/msg/784c039090fddc6c). The documentation generated using this new style can be found [here](http://sage.math.washington.edu/home/mvngu/patch/9850-docstyle/doc/). See the ticket description for instructions on how to apply patches.


---

Attachment


---

Attachment


---

Attachment


---

Comment by jhpalmieri created at 2010-11-02 21:23:28

What needs to be done to give this a positive review?  I think it looks good.  My contribution as an author was pretty minor, so can we give it a positive review, especially given the other positive comments on the ticket so far?


---

Comment by mvngu created at 2010-11-03 06:47:36

Replying to [comment:18 jhpalmieri]:
> What needs to be done to give this a positive review?  I think it looks good.  My contribution as an author was pretty minor, so can we give it a positive review, especially given the other positive comments on the ticket so far?

I think this is ready for a positive review. Of course, I can't officially set the ticket to positive, but I'm OK with the two patches that are not mine. See the ticket description for the rebuilt documentation using the new style.


---

Comment by mpatel created at 2010-11-03 08:27:50

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-11-03 08:27:50

The new style looks great.  I suggest that we open new ticket(s) for any further changes.  Thanks to everyone for their contributions!


---

Comment by jdemeyer created at 2010-11-10 22:20:19

Resolution: fixed
