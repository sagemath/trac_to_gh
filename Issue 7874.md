# Issue 7874: Typeset labels for interact controls

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-01-08 21:34:57

Assignee: was

CC:  rbeezer

Can we typeset the labels of interact controls

```python
`@`interact
def test(x=slider(-2,2,1, label='$x^2$')):
    print "Doing nothing in an interact"
```

?

See [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/312cab9514bece7c).


---

Attachment

`jsMath.Process()` wrapped output text for interacts.  sagenb repo.


---

Comment by mpatel created at 2010-01-08 21:42:55

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-01-08 21:42:55

The attached patch works for me with the example above, but it is _not_ extensively tested.


---

Comment by mpatel created at 2010-01-08 21:51:40

`sage.misc.html.html` `print`s HTML code as a side-effect.  The server captures this as output from the worksheet process, but the position depends, I think, on the order of evaluation.


---

Comment by rbeezer created at 2010-01-08 22:29:56

Hi Pat,

Thanks for the quick work on this one!  I was going to try to test it with my original purpose.  But I can't seem to find a sagenb repo in my development tree.

What does it take to apply and run the patch?  I have a 4.3.1.alpha1 installation and know how to apply patches in /sage/devel.  is it much different?  Do I get everything I need in the Sage source distribution?

Thanks,
Rob


---

Comment by mpatel created at 2010-01-08 22:44:55

Please see [SageNB's home](http://nb.sagemath.org/) for brief directions.  In particular,

```sh
mkdir tmp; cd tmp
wget http://boxen.math.washington.edu/home/wstein/patches/sagenb/sagenb-0.4.9.spkg
tar jxvf sagenb-0.4.9.spkg
cd sagenb-0.4.9/src/sagenb
sage -hg pull http://boxen.math.washington.edu:8100
sage -hg update
```

Then apply the patch, do

```sh
sage -python setup.py develop
```

and run the notebook.  (The "develop" command, unlike the "install" command, just tells `setuptools` to use the current directory as the installation.)  To revert to original version, you can `hg qpop` the patch (if you're using [queues](http://wiki.sagemath.org/MercurialQueues)) or do

```sh
sage -f sagenb-0.4.9.spkg
```

Please let me know, if you have questions.


---

Comment by mpatel created at 2010-01-08 22:55:30

Or use `SAGE_ROOT/spkg/standard/sagenb-0.4.9.spkg`.


---

Comment by rbeezer created at 2010-01-08 22:56:57

Perfect!  Thanks for the primer.  I'll get back to it later today.


---

Comment by mpatel created at 2010-01-09 00:17:18

Hi Rob -- If you're feeling adventurous and have some spare time, please try testing the spkg at #7666.


---

Comment by rbeezer created at 2010-01-09 00:45:45

mpatel,

Works just fine for me with the interact I was building.  Leads with four sliders all with nice labels.  Screenshot here, and I'll post on sage-devel and sagenb.

Thanks - this will make interacts look all the better.

Rob


---

Attachment

Replying to [comment:7 mpatel]:
> Hi Rob -- If you're feeling adventurous and have some spare time, please try testing the spkg at #7666.

Yes, to adventurous, no to spare time.  But I think adventure wins.  

But (this is embarrassing) I've never installed an spkg.  How should I do this so I can back it out again without having a mess on my hands?  ;-)  I don't have anything important to lose, so it won't be a crisis if I screw up.  Can you give me another short primer?

Should have said above: I don't think I know enough to give a review.  But I'm going to go right now and advertise how good the patch is and see if we can get one.

Rob


---

Comment by mpatel created at 2010-01-09 01:03:58

To install any spkg, local or remote, just do, e.g.,

```
sage -f http://boxen.math.washington.edu/home/mpatel/trac/7666/sagenb-0.5-7666b2.spkg
```

To revert to the "default" spkg (or another version), just do, e.g.,

```
sage -f $SAGE_ROOT/spkg/standard/sagenb-0.4.9.spkg
```

(The default should already be part of the source distribution.)  Actually, `sage -advanced` also gives `sage -i thepackage.spkg` as a way to install an spkg.  The `-f` option forces a reinstall, even if the package is already installed.

As always, please let me know, if there are questions and/or problems.


---

Comment by mpatel created at 2010-01-09 01:11:46

Hmmm... I just tried the first line, but I got an error.  It may be better to download the spkg first and rename it:

```
wget http://boxen.math.washington.edu/home/mpatel/trac/7666/sagenb-0.5-7666b2.spkg
mv sagenb-0.5-7666b2.spkg sagenb-0.5.spkg
sage -f sagenb-0.5.spkg
```

I apologize for this.


---

Comment by rbeezer created at 2010-01-09 01:13:37

Replying to [comment:10 mpatel]:
I thought it was that easy.  ;-)  I'll get to it a bit later this evening.  Thanks.


---

Comment by mpatel created at 2010-01-09 01:22:49

The one-liner should now work.  Another lesson learned.  (I didn't rename the internal directory to `sagenb-0.5-7666b2`.)


---

Comment by rbeezer created at 2010-01-10 06:23:26

Replying to [comment:13 mpatel]:
> The one-liner should now work.  Another lesson learned.  (I didn't rename the internal directory to `sagenb-0.5-7666b2`.)

Looks like the package has been fixed, so no renaming is needed.


---

Comment by timdumol created at 2010-01-17 20:05:34

Changing status from needs_review to positive_review.


---

Comment by timdumol created at 2010-01-17 20:05:34

LGTM. Nice work.


---

Comment by mpatel created at 2010-01-25 00:55:41

Resolution: fixed


---

Comment by mpatel created at 2010-01-25 00:57:05

The milestone should be sage-4.3.1.
