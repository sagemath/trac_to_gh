# Issue 8307: gfan-0.4plu keeps getting upgraded

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-02-19 12:36:24

Assignee: GeorgSWeber

CC:  mvngu

I think this happens because we misuse [rstrip](http://docs.python.org/library/stdtypes.html#str.rstrip) in `SAGE_LOCAL/bin/sage-update`.


---

Comment by mpatel created at 2010-02-19 14:23:29

Fix rstrip problems.  Various cleanups.  scripts repo.


---

Comment by mpatel created at 2010-02-19 14:30:01

Changing status from new to needs_review.


---

Attachment

The patch

 * Fixes `rstrip` problems.
 * Includes pep8-related cleanup and cosmetic changes.
 * Uses [textwrap](http://docs.python.org/library/textwrap.html).

Feel free to make further improvements, or to undo mine!


---

Comment by mvngu created at 2010-02-20 10:59:54

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-02-20 10:59:54

Based on a freshly compiled Sage 4.3.3.alpha1, I made a source distribution called sage-4.3.3.alpha1.1, which is essentially the same as Sage 4.3.3.alpha1. From a Sage 4.3.3.alpha1 binary, I upgraded it to sage-4.3.3.alpha1.1 and received the following upgrade message:

```
The following packages will be upgraded:
  examples-4.3.3.alpha1.1 extcode-4.3.3.alpha1.1 gfan-0.4plu sage-4.3.3.alpha1.1 sage_scripts-4.3.3.alpha1.1
```

I didn't make any changes to the gfan spkg and yet it is slated for upgrading. After upgrading the Sage library, I received the following message about upgrading gfan:

```
Done
The following packages will be upgraded:
  gfan-0.4plu
```

Answering yes to the upgrade, the install log shows this line:

```
gfan-0.4plus.spkg already present
```

Yep, it's redudant and annoying that gfan is upgraded everytime one does a source upgrade.




Here's another try. With a freshly compiled Sage 4.3.3.alpha1, I applied [trac_8307-update_sage-update.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8307/trac_8307-update_sage-update.patch) to the scripts repository and produced a source distribution sage-4.3.3.alpha1.1. I then applied that same patch on top of a binary version of Sage 4.3.3.alpha1 and upgraded that binary distribution to sage-4.3.3.alpha1.1. This time the upgrade message reads:

```
The following packages will be upgraded:

    examples-4.3.3.alpha1.1 extcode-4.3.3.alpha1.1 sage-4.3.3.alpha1.1
    sage_scripts-4.3.3.alpha1.1
```

with no gfan within sight. The upgrade process didn't upgrade gfan.




The patch moves some code to the following conditional at the end of `sage-update`:

```
if __name__ == '__main__':
   <SNIP>
```

There are some clean up of docstrings and clean up conforming to PEP8. The real change is in adding the new function `chop()` and using it as follows:

```
-    installed = set(os.listdir("%s/installed/"%SPKG_ROOT))
-    to_download = [x for x in packages if not x.rstrip('.spkg') in installed]
+    installed = set(os.listdir("%s/installed/" % SPKG_ROOT))
+    to_download = [x for x in packages if not chop(x, '.spkg') in installed]

```

Previously, the script `sage-update` used `rstrip()` for finding a list of spkg's to upgrade. This function won't work as intended for spkg's that has an "s" at the end of their names just before the extension ".spkg". The new function `chop()` does this better by testing that the name of an spkg actually ends in ".spkg". That's why the update script wants to upgrade "gfan-0.4plu" when the gfan spkg is named "gfan-0.4plus".


---

Comment by mvngu created at 2010-03-02 21:13:25

Merged [trac_8307-update_sage-update.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8307/trac_8307-update_sage-update.patch) in the script repository.


---

Comment by mvngu created at 2010-03-02 21:13:25

Resolution: fixed
