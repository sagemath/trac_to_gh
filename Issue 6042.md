# Issue 6042: Bring doctests of modular/modsym/ambient.py up to 100%

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2009-05-15 07:21:34

Assignee: craigcitro

Keywords: documentation, modular symbols

This 2500-line file has a low score:
 26% (26 of 97)

I have nearly finished documenting it and will upload a patch over the weekend.



---

Comment by cremona created at 2009-05-16 15:35:16

Applies to 3.4.2


---

Attachment

This is just sickening.  I must have spent over 10 hours in the last week documenting this file, resulting in a patch over 2000 lines long, and 100% doctest coverage.  But now I cannot apply it since after the 7 patches on 3 tickets which David warned me about (#5736, #4357 and #5250 all already merged in 4.0alpha0, in that order) I get this mess:


```
john`@`ubuntu%sage -hg qpush
applying trac_6042.patch
patching file sage/modular/modsym/ambient.py
Hunk #17 FAILED at 800
Hunk #25 FAILED at 1291
Hunk #45 FAILED at 2230
Hunk #60 FAILED at 2829
Hunk #61 FAILED at 2836
Hunk #65 FAILED at 2962
Hunk #71 FAILED at 3195
7 out of 76 hunks FAILED -- saving rejects to file sage/modular/modsym/ambient.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
Errors during apply, please fix and refresh trac_6042.patch
```


I'm really not sure I can be bothered to mess with this any more.  Is there any system to actually help one merge conflicting patches sensibly?  I have never managed to get things like k3diff to work.

I will at least upload my patch  so that it does not get lost, but I have other things to do.


---

Comment by AlexGhitza created at 2009-05-17 00:11:48

Replying to [comment:1 cremona]:
> This is just sickening.  I must have spent over 10 hours in the last week documenting this file, resulting in a patch over 2000 lines long, and 100% doctest coverage.  But now I cannot apply it since after the 7 patches on 3 tickets which David warned me about (#5736, #4357 and #5250 all already merged in 4.0alpha0, in that order) I get this mess:
> 
> I will at least upload my patch  so that it does not get lost, but I have other things to do.

Hi John,

I feel your pain.  I don't know of an automated system to get this done properly.  But I'll try to rebase it to 4.0alpha0, and review it in the process.  Hopefully I can do this in the next 36 hours or so.


---

Comment by davidloeffler created at 2009-05-17 21:51:46

Alex: have you already started on this? (I'm not sure what time zone you're in.) I ask because I'm probably the best placed person to sort it out, as the changes which have caused the conflicts were mine, which also puts me under a certain moral obligation as well :-). I don't want to tread on your toes if you've already done it so let me know if you have, but if not, leave it to me and I'll sort it out tomorrow morning.


---

Comment by AlexGhitza created at 2009-05-17 22:04:39

I have started but haven't gotten very far yet, so I won't be upset if you want to do it.  Most of the stuff is fairly straightforward, but there are some functions where you introduced documentation and examples, and then John's patch is doing things all over again.  So that would best be done by one of you.


---

Comment by davidloeffler created at 2009-05-18 09:08:58

I've rebased the patch to 4.0.alpha0 and checked that it passes doctests, and had a look through the code, and it all looks fine -- let's get this in without further delay!


---

Comment by cremona created at 2009-05-18 09:13:27

Thanks David (and Alex)!


---

Comment by cremona created at 2009-05-18 15:23:41

BTW, I see that "rebasing" has included "reattributing credit in the patch header"! :)


---

Comment by mabshoff created at 2009-05-18 15:35:25

Replying to [comment:7 cremona]:
> BTW, I see that "rebasing" has included "reattributing credit in the patch header"! :)

Hehe, I will fix this once I import the patch. 

David: Before posting the patch you can just edit the credit in the hg header at the top of the file.

Cheers,

Michael


---

Comment by cremona created at 2009-05-18 15:39:13

Replying to [comment:8 mabshoff]:
> Replying to [comment:7 cremona]:
> > BTW, I see that "rebasing" has included "reattributing credit in the patch header"! :)
> 
> Hehe, I will fix this once I import the patch. 
> 
> David: Before posting the patch you can just edit the credit in the hg header at the top of the file.
> 
> Cheers,
> 
> Michael

Of course I would like credit to go to David too, if hg will allow.


---

Attachment

patch against 4.0.alpha0


---

Comment by davidloeffler created at 2009-05-18 15:43:05

I just found out about "qrefresh -u", so I can masquerade as anybody I like. I'll now attribute any patches that don't work to some unsuspecting victim :-) I've uploaded a new version with credit correctly attributed to John.


---

Comment by cremona created at 2009-05-18 15:54:47

Replying to [comment:10 davidloeffler]:
> I just found out about "qrefresh -u", so I can masquerade as anybody I like. I'll now attribute any patches that don't work to some unsuspecting victim :-) I've uploaded a new version with credit correctly attributed to John.

thanks -- I don't really mind, of course, but I was looking when I made sure that yours was a replacement patch and not a second patch.


---

Comment by mabshoff created at 2009-05-18 16:46:56

The rebased patch on top of two other trivial tickets in my 4.0.rc0 merge tree:

```
Overall weighted coverage score:  75.0%
Total number of functions:  22100
We need    6 more function to get to 75% coverage.
```


:))

Cheers,

Michael


---

Comment by cremona created at 2009-05-18 17:03:14

That makes it all worth while!


---

Comment by mabshoff created at 2009-05-18 18:05:27

Merged in Sage 4.0.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-05-18 18:05:27

Resolution: fixed
