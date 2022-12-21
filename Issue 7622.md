# Issue 7622: Fix OSX plist copyright situation

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2009-12-08 15:27:34

Assignee: mvngu

CC:  iandrus mhansen was

From #5261: 

```
remove the extra copyright work in credits as well as give credit to "William Stein and the Sage Development Team"
```


```
Someone with a better understanding of the copyright situation should change data/extcode/sage/ext/mac-app/Sage.app/Contents/Info.plist (it's an xml file) in two places.
```

This shouldn't be hard to fix.  Use hg_sage.extcode!


---

Attachment

Based on 4.3.alpha1


---

Comment by kcrisman created at 2009-12-14 16:59:06

Changing status from new to needs_review.


---

Comment by kcrisman created at 2009-12-14 16:59:06

I hope this will be good; I have put 2005- rather than 2005-2009 or whatever so that it won't have to be updated constantly.  I have also cc:ed two people who should be able to review the correctness of this attribution, which is the one found on all documentation but (curiously) nowhere I can find on the software itself.


---

Attachment

reviewer patch


---

Comment by mvngu created at 2009-12-15 00:41:12

The relevant Mercurial repository is


```
SAGE_ROOT/data/extcode
```


At least with Sage 4.3.rc0, it has a junk file which should be removed:


```
[mvngu`@`sage extcode]$ pwd
/scratch/mvngu/build/sage-4.3.rc0/data/extcode
[mvngu`@`sage extcode]$ hg st
? sage/ext/.DS_Store.rej
```


So I removed that junk file as follows:


```
[mvngu`@`sage extcode]$ rm -rf sage/ext/.DS_Store.rej
[mvngu`@`sage extcode]$ hg st
<no output>
```


I applied `trac_7622.patch` against Sage 4.3.rc0 successfully. I also attached `trac_7622-reviewer.patch` which fixes the copyright notice in another file specific to OS X. The reviewer patch also ensures that the copyright notices are consistent with that shown on the standard documentation. In particular, I use "2005-2009" as is used on the documentation. I have created a [wiki page](http://wiki.sagemath.org/UpdateCopyright) which lists files that need to be updated when the copyright notice is updated. Patches should be applied in this order:

 1. Delete the file `data/extcode/sage/ext/.DS_Store.rej`
 1. Apply `trac_7622.patch`
 1. Finally, apply `trac_7622-reviewer.patch`
 
Only my patch needs review.


---

Comment by kcrisman created at 2009-12-15 13:27:37

It would be good if this got into 4.3 still, since it is not about functionality but rather clarifying copyright.

The "junk" file is fallout from iandrus' changing the Mac app structure from a tar.gz file to a normal directory structure, and hopefully this will fix things from that.

The other patch looks good to me - we hadn't noticed that other plist that needed this.  It applies fine as well.

However, I think that this wiki page is liable to get lost in the wilderness.  Maybe not right away, since 2010 is so close, but for 2011... can anyone think of somewhere this can link to that would be more prominent?  Or, perhaps one should open a ticket for 2010, and put on there to open a ticket for 2011 once that ticket is closed... maybe.


---

Comment by kcrisman created at 2009-12-15 13:27:37

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-12-15 16:08:27

Resolution: fixed
