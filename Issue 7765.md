# Issue 7765: In sage-4.3, the command "sage -bdist" is broken on OS X

Issue created by migration from https://trac.sagemath.org/ticket/7765

Original creator: was

Original creation time: 2009-12-25 09:32:40

Assignee: tbd

CC:  georgsweber

On OS X with sage-4.3, if you do "sage -bdist" it creates the dist/sage-* directory correctly. However, it doesn't create the dmg anymore.  It can evidently be made to do so by setting environment variables.  But the default "sage -bdist" doesn't create a bdist.     This is confusing and very inconsistent with the behavior on all other OS's.  For some reason Ivan Andrus changed this in #7546. 

This will have to be fixed back for 4.3.1. 


---

Comment by kcrisman created at 2009-12-28 17:19:51

Based on 4.3


---

Comment by kcrisman created at 2009-12-28 17:20:50

Changing status from new to needs_review.


---

Attachment

This is a very naive solution, but hopefully it is sufficient.  Since I was the one who didn't realize that was changing standard behavior (in fact, I thought it was a feature!) on the previous ticket, I figure I should attempt to fix it.


---

Comment by was created at 2010-02-07 06:13:52

Your patch has the line:

```  
if [ "$SAGE_APP_DMG" = "no" ]; then 
```


This seems to thus bizarrely assume that  SAGE_APP_DMG is either "yes" or "no". But it is an environment variable, so can be anything, and defaults to being "".   Did you test the above with SAGE_APP_DMG not set?


---

Comment by was created at 2010-02-07 06:13:52

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2010-02-08 02:11:11

Like I said, it is a very naive solution; I never claimed to be a shell script expert :)  Will do my best to make it better but am not sure when I will have time.


---

Comment by kcrisman created at 2010-02-08 19:54:14

Replying to [comment:2 was]:
> Your patch has the line:
> {{{  
> if [ "$SAGE_APP_DMG" = "no" ]; then 
> }}}
> 
> This seems to thus bizarrely assume that  SAGE_APP_DMG is either "yes" or "no". But it is an environment variable, so can be anything, and defaults to being "".   Did you test the above with SAGE_APP_DMG not set?

Well, apparently as long as you don't have SAGE_APP_DMG being 'no', it will make the dmg.   At least, that's what happened when I tested this, and Sage worked.  Should I change

```
        echo 'If you wish to create a disk image please set'
        echo 'SAGE_APP_DMG=yes'
```

to something about

```
        echo 'If you wish to create a disk image please do'
        echo 'unset SAGE_APP_DMG'
```

or something similar?

I just don't know what is best; since we want the default to be making a dmg, I guess any of these options make it maximally hard to *not* make a dmg, but maybe they are not very 'shell-script'-y.  I'm putting this as 'needs review' again, but feel free to put it back to 'needs work' with any comments that would make it better.


---

Comment by kcrisman created at 2010-02-08 19:54:14

Changing status from needs_work to needs_review.


---

Comment by GeorgSWeber created at 2010-02-13 06:50:39

I'll see how much time time I find this weekend.
The current situation is annoying me, too.


---

Comment by GeorgSWeber created at 2010-02-14 13:43:02

Changing status from needs_review to needs_work.


---

Comment by GeorgSWeber created at 2010-02-14 13:43:02

After the patch "trac_7765-dmg.patch" from seven weeks ago, the functionality is as (I think) it should be, i.e. unless an environment variable "SAGE_APP_DMG" both exists and has a value of "no", the dmg will be built. Good.

As for the documentation/printout statements, one might think of something along the following lines to be more verbose:

``` 
    if [ "$SAGE_APP_DMG" = "no" ]; then
        echo 'If you wish to create a disk image please set'
        echo 'SAGE_APP_DMG=yes'
        echo '(or to anything else but the current SAGE_APP_DMG=no,'
        echo ' or completely unset SAGE_APP_DMG)'
    else
        echo "Creating dmg"
        echo '(If you don't wish to create a disk image please set'
        echo ' SAGE_APP_DMG=no)'
        DYLD_LIBRARY_PATH=$SAGE_ORIG_DYLD_LIBRARY_PATH; export DYLD_LIBRARY_PATH
        hdiutil create -srcfolder "$TARGET" -format UDBZ "$TARGET".dmg
    fi
```

Could you update the patch, or should I do it (I didn't because otherwise I couldn't be the reviewer, could I)?


---

Attachment

Sorry about that, mabshoff mentioned that making a dmg should be optional since it takes so long e.g. when testing things.  For some reason I took that to mean not the default.  I created a new patch trac_7765-dmg.2.patch so that either of you can referee it.


---

Comment by iandrus created at 2010-03-07 15:54:25

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2010-04-22 07:53:11

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2010-04-22 07:53:11

I see one problem with this script that no one has yet noticed, and perhaps was William's initial question about it. 

```
Moving final distribution file to /Users/.../sage-4.3.5/dist
mv: rename sage-Sage2-PowerMacintosh-Darwin.* to /Users/.../sage-4.3.5/dist/sage-Sage2-PowerMacintosh-Darwin.*: No such file or directory
```

Right!  Because

```
if [ "$UNAME" = "Darwin" ]; then
...
    else
        echo 'If you wish to create a disk image please set'
        echo 'SAGE_APP_DMG=yes'
        echo '(or to anything else but the current SAGE_APP_DMG=no,'
        echo ' or completely unset SAGE_APP_DMG)'
    fi
else
    echo "Creating tar.gz"
    tar zcvf "$TARGET".tar.gz "$TARGET"
fi
```

but

```
echo "Moving final distribution file to $SAGE_ROOT/dist"

mv $TARGET $SAGE_ROOT/dist/
mv $TARGET.* $SAGE_ROOT/dist/
```

So the point is that when SAGE_APP_DMG=no, not only is there not a DMG, but not even a .tgz file is created!  Which yields the weird error message I always see from the very last line.

However, testing once again showed that default behavior is now .dmg creation (as it was with the other version of the patch), and none of this should affect anything other than Darwin, so we just have to make sure that we add the right lines to the "else" above and then this should be good to go.  I'll do that in the morning, and then (sigh) we'll need yet another review...


---

Attachment

Based on Sage 4.3.5 - apply only this to scripts repo


---

Comment by kcrisman created at 2010-04-22 12:54:20

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2010-04-22 12:54:20

Okay, ready for review. Downgrading to critical since it's been four months.


---

Comment by kcrisman created at 2010-04-22 12:54:20

Changing priority from blocker to critical.


---

Comment by was created at 2010-04-29 00:36:33

Resolution: fixed
