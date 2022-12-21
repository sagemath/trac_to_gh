# Issue 2364: animate .show() method is poorly documented

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2008-03-01 22:14:14

Assignee: was

It should be better documented in animate.py how to specify the interframe delay and the number of iterations.  At the very least, this should be described in the .show() docstring; better yet if it was also documented in the class docstring for Animation, which is what you see when you type:

```
sage: animate?
```




---

Comment by AlexGhitza created at 2008-03-16 02:23:52

Changing component from algebraic geometry to documentation.


---

Comment by AlexGhitza created at 2008-03-16 02:23:52

Changing assignee from was to tba.


---

Attachment

Here's a patch, based on 3.1.3.alpha2. I started working on animate.py before I knew about this ticket, so the patch does more than is required:

1. It improves the documentation for `show` and `animate`, as requested.

2. It adds docstrings and doctests to several functions for which they were missing; the file now has over 90% coverage.  (Only `__init__` is undocumented now.)

3. Many doctests used to be optional, things like

```
sage: a = animate([sin(x + float(k)) for k in srange(0,2*pi,0.3)], 
...                xmin=0, xmax=2*pi, figsize=[2,1])
```

These don't need to be optional -- the optional part comes in calls to `a.show()`, which calls the `convert` program -- so I've removed lots of optional tags. This way more of the code is actually doctested.

4. I also deleted one method: `_set_axes`. This method was undocumented. It was short and pretty simple. It was also called every time an animation was created; indeed, that was its only appearance in the code. So I just copied its contents (only 5 lines) to where it was called in the `__init__` method.


---

Comment by jhpalmieri created at 2008-10-01 21:07:15

Changing keywords from "" to "animate, documentation, doctest".


---

Comment by jhpalmieri created at 2008-10-01 21:11:37

5. Oh, one other thing: in the `gif` method (and hence in `save` and `show` which call it), I added a message saying where the file was being saved.  Before, you would type

```
a.save('bozo.gif')
```

and, if you were using the notebook interface, the file would be saved something like 5 subdirectories below .sage.  This is still true, but at least now you're told where the file is.


---

Comment by mhampton created at 2008-10-22 19:40:52

Although I too have been frustrated sometimes by the depth of the saves of things in sage, I don't think I like the solution here of always printing the path.  I think this should be an option - perhaps a keyword/default like show_path = False, and if show_path were True then the path is displayed.  That would also be useful for other saved graphics as well.

Otherwise this patch gets a very positive review; in general the show() documentation needs a lot of work and this is a great step in that direction.


---

Comment by jhpalmieri created at 2008-10-22 20:59:44

do not apply: this is only here to help the referee


---

Attachment

Here are two new patches to deal with mhampton's comments.  The one which should be applied is *2364-new.patch*.  The other patch, *2364-delta.patch*, shows the difference between the old patch and the new patch.  This way mhampton (for example) can referee the new patch more easily, I hope.  

(That is, if you apply the original patch and then 2364-delta.patch, it should give the same result as just applying the new patch.  I'm trying to achieve ease of refereeing as well as ease of incorporating the patch...)


---

Comment by mabshoff created at 2008-10-28 12:49:43

I don't particularly like the delta patch, i.e. the test file generated should be saved in SAGE_TMP for example since the $SAGE_ROOT tree or cwd might not be writable. 

Cheers,

Michael


---

Comment by jhpalmieri created at 2008-10-28 14:46:51

Replying to [comment:6 mabshoff]:
> I don't particularly like the delta patch, i.e. the test file generated should be saved in SAGE_TMP for example since the $SAGE_ROOT tree or cwd might not be writable. 

I didn't change the location of the file -- as far as I know it's always been this way.  Given this, it seems like the patch does not make anything worse, and for the most part improves the original file.  I think the issue about the location of the save file should be a new ticket.


---

Comment by mabshoff created at 2008-10-28 14:49:58

Replying to [comment:7 jhpalmieri]:

> I didn't change the location of the file -- as far as I know it's always been this way.  Given this, it seems like the patch does not make anything worse, and for the most part improves the original file.  I think the issue about the location of the save file should be a new ticket.

Sure. The issue will pop up once somebody runs doctests as non-owner. I don't particularly care if that issue gets fixed now or not, so a new ticket would get this patch a positive review.

Cheers,

Michael


---

Comment by jhpalmieri created at 2008-10-28 15:01:53

Unfortunately (?), doctests won't catch it, since these commands are all optional -- they all rely on the `convert` command being present.

  John


---

Comment by mabshoff created at 2008-10-28 15:06:04

Replying to [comment:9 jhpalmieri]:
> Unfortunately (?), doctests won't catch it, since these commands are all optional -- they all rely on the `convert` command being present.
> 
>   John

Yes, but someone [can you guess? :)] has started running Sage with "-t -long -optional", so in the future we will catch this. I am all for merging this patch after someone verifies that the animate command still works as expected. 

Cheers,

Michael


---

Comment by jhpalmieri created at 2008-10-28 18:43:31

Oh dear.  I don't know how to write the doctests, then.  For example, I have a doctest which shows what happens when `convert` is missing: 

```
        If ImageMagick is not installed, you will get an error message:
            sage: a.gif()       # optional
            /usr/local/share/sage/local/bin/sage-native-execute: 8: convert: not
            found

            Error: ImageMagick does not appear to be installed. Saving an
            animation to a GIF file or displaying an animation requires
            ImageMagick, so please install it and try again.

            See www.imagemagick.org, for example.
```

This will fail if you run the optional doctests with `convert` installed.  Should I delete the doctest and just display the error message?

Also, I have doctests like this

```
            sage: a.save(show_path=True)  # optional
            Animation saved to file /home/isaac/.sage/sage0.gif.
```

in which I have inserted an invented pathname. What should I do about these?


---

Comment by mabshoff created at 2008-10-28 18:56:14

Replying to [comment:11 jhpalmieri]:
> Oh dear.  I don't know how to write the doctests, then.  For example, I have a doctest which shows what happens when `convert` is missing: 
> {{{
>         If ImageMagick is not installed, you will get an error message:
>             sage: a.gif()       # optional
>             /usr/local/share/sage/local/bin/sage-native-execute: 8: convert: not
>             found
> 
>             Error: ImageMagick does not appear to be installed. Saving an
>             animation to a GIF file or displaying an animation requires
>             ImageMagick, so please install it and try again.
> 
>             See www.imagemagick.org, for example.
> }}}
> This will fail if you run the optional doctests with `convert` installed.  Should I delete the doctest and just display the error message?

Nope, if someone runs optional doctests and the binary required is not there it will blow up. Nothing can change that until we have a more clever "#optinal" doctest treatment. 

> Also, I have doctests like this
> {{{
>             sage: a.save(show_path=True)  # optional
>             Animation saved to file /home/isaac/.sage/sage0.gif.
> }}}
> in which I have inserted an invented pathname. What should I do about these?

This would need to be changed to 

 "Animation saved to file .../sage0.gif."

Cheers,

Michael


---

Comment by jhpalmieri created at 2008-10-28 19:58:27

fix optional doctests


---

Attachment

only apply this patch!


---

Attachment

Here are two patches, fixing the optional doctests.  Now `sage -t -optional animate.py` works on my machine.

The patch *2364-doctest-delta.patch* shows the differences between the previous patch and this one: only a few doctests were changed.

The patch *2364-new.patch* incorporates all of the patches into one file (so if you apply 2364.patch, 2364-delta.patch, and 2364-doctest-delta.patch, you will get the same as if you just applied this one).

So: either the two delta patches need to be refereed (since 2364.patch has received an essentially positive review), or 2364-new.patch needs to be refereed.


---

Comment by mabshoff created at 2008-10-30 08:39:29

Bug Day 15 review material. This patch could bit rot easily, so let's get it in.

Cheers,

Michael


---

Comment by mhampton created at 2008-10-30 12:21:12

Thanks for incorporating all those changes.  I think this looks very good now.  Optional tests pass on my machine.


---

Comment by mabshoff created at 2008-10-30 16:20:10

Resolution: fixed


---

Comment by mabshoff created at 2008-10-30 16:20:10

Merged 2364-new.patch in Sage 3.2.alpha2
