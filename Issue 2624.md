# Issue 2624: parallel testing: sage -tp foo/bar/file.py is broken

archive/issues_002624.json:
```json
{
    "body": "Assignee: @garyfurnish\n\nOops: \n\n```\n./sage -tp -long devel/sage/sage/plot/plot.py\nGlobal iterations: 1\nFile iterations: 1\nTeX files: 0\nUsage: sage -t <files or directories>.\nFor more information, type 'sage -help'.\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2624\n\n",
    "created_at": "2008-03-21T00:46:53Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "parallel testing: sage -tp foo/bar/file.py is broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2624",
    "user": "mabshoff"
}
```
Assignee: @garyfurnish

Oops: 

```
./sage -tp -long devel/sage/sage/plot/plot.py
Global iterations: 1
File iterations: 1
TeX files: 0
Usage: sage -t <files or directories>.
For more information, type 'sage -help'.
```




Issue created by migration from https://trac.sagemath.org/ticket/2624





---

archive/issue_comments_018015.json:
```json
{
    "body": "Missing number of threads parameter, invalid.",
    "created_at": "2008-03-21T00:48:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2624#issuecomment-18015",
    "user": "@garyfurnish"
}
```

Missing number of threads parameter, invalid.



---

archive/issue_comments_018016.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-03-21T00:48:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2624#issuecomment-18016",
    "user": "@garyfurnish"
}
```

Resolution: invalid



---

archive/issue_comments_018017.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-03-21T00:49:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2624#issuecomment-18017",
    "user": "@garyfurnish"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_018018.json:
```json
{
    "body": "This should be the responsiblity of sage-sage",
    "created_at": "2008-03-21T00:49:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2624#issuecomment-18018",
    "user": "@garyfurnish"
}
```

This should be the responsiblity of sage-sage



---

archive/issue_comments_018019.json:
```json
{
    "body": "Resolution changed from invalid to ",
    "created_at": "2008-03-21T00:49:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2624#issuecomment-18019",
    "user": "@garyfurnish"
}
```

Resolution changed from invalid to 



---

archive/issue_comments_018020.json:
```json
{
    "body": "Changing assignee from @garyfurnish to mabshoff.",
    "created_at": "2008-03-21T00:49:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2624#issuecomment-18020",
    "user": "@garyfurnish"
}
```

Changing assignee from @garyfurnish to mabshoff.



---

archive/issue_comments_018021.json:
```json
{
    "body": "Changing status from reopened to new.",
    "created_at": "2008-03-21T00:49:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2624#issuecomment-18021",
    "user": "@garyfurnish"
}
```

Changing status from reopened to new.



---

archive/issue_comments_018022.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-01-22T18:25:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2624#issuecomment-18022",
    "user": "@aghitza"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_018023.json:
```json
{
    "body": "Here's a patch.  If the first argument after \"tp\" can't be converted to an integer, this sets it to 1 and assumes that the first argument is part of the list of files.  The patch also expands on the error messages, changes the usage warning from \"Usage: sage -t\" to \"Usage: sage -tp\", gives a pointer to \"sage -advanced\" for more help, and adds a corresponding string to the output of \"sage -advanced\".",
    "created_at": "2009-09-21T22:42:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2624#issuecomment-18023",
    "user": "@jhpalmieri"
}
```

Here's a patch.  If the first argument after "tp" can't be converted to an integer, this sets it to 1 and assumes that the first argument is part of the list of files.  The patch also expands on the error messages, changes the usage warning from "Usage: sage -t" to "Usage: sage -tp", gives a pointer to "sage -advanced" for more help, and adds a corresponding string to the output of "sage -advanced".



---

archive/issue_comments_018024.json:
```json
{
    "body": "Changing assignee from mabshoff to @jhpalmieri.",
    "created_at": "2009-09-21T22:42:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2624#issuecomment-18024",
    "user": "@jhpalmieri"
}
```

Changing assignee from mabshoff to @jhpalmieri.



---

archive/issue_comments_018025.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-09-21T22:42:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2624#issuecomment-18025",
    "user": "@jhpalmieri"
}
```

Changing status from new to assigned.



---

archive/issue_comments_018026.json:
```json
{
    "body": "With this patch, when I do something like \"sage -tp fjfjfjfjfj\", it doesn't tell me that I gave it a bad file:\n\n```\ndrake@klee:/var/tmp/sage-4.1.2.alpha2$ ./sage -tp fjfjfj \nGlobal iterations: 1\nFile iterations: 1\nUsing cached timings to run longest doctests first.\nDoctesting 0 files \n \n----------------------------------------------------------------------\nAll tests passed!\nTimings have been updated.\nTotal time for all tests: 0.1 seconds\n```\n\nAlso, when it makes an assumption about the number of threads, I'd like it to print that it's using 1 thread. (Mostly for my own reassurance.)",
    "created_at": "2009-09-23T01:11:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2624#issuecomment-18026",
    "user": "@dandrake"
}
```

With this patch, when I do something like "sage -tp fjfjfjfjfj", it doesn't tell me that I gave it a bad file:

```
drake@klee:/var/tmp/sage-4.1.2.alpha2$ ./sage -tp fjfjfj 
Global iterations: 1
File iterations: 1
Using cached timings to run longest doctests first.
Doctesting 0 files 
 
----------------------------------------------------------------------
All tests passed!
Timings have been updated.
Total time for all tests: 0.1 seconds
```

Also, when it makes an assumption about the number of threads, I'd like it to print that it's using 1 thread. (Mostly for my own reassurance.)



---

archive/issue_comments_018027.json:
```json
{
    "body": "> With this patch, when I do something like \"sage -tp fjfjfjfjfj\", it doesn't tell me that I gave it a bad file:\n\nI feel as though this belongs in another ticket.  For what it's worth, previous authors of the file seem to have made this decision intentionally:\n\n```\n               else:\n                    continue # prefer silence to: raise TypeError, \"Unknown File %s\" % F\n```\n\n\n> Also, when it makes an assumption about the number of threads, I'd like it to print that it's using 1 thread. (Mostly for my own reassurance.)\n\nThat's easy enough to change; see the new patch.  This version also sets numthreads to be no more than the number of files.",
    "created_at": "2009-09-23T02:04:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2624#issuecomment-18027",
    "user": "@jhpalmieri"
}
```

> With this patch, when I do something like "sage -tp fjfjfjfjfj", it doesn't tell me that I gave it a bad file:

I feel as though this belongs in another ticket.  For what it's worth, previous authors of the file seem to have made this decision intentionally:

```
               else:
                    continue # prefer silence to: raise TypeError, "Unknown File %s" % F
```


> Also, when it makes an assumption about the number of threads, I'd like it to print that it's using 1 thread. (Mostly for my own reassurance.)

That's easy enough to change; see the new patch.  This version also sets numthreads to be no more than the number of files.



---

archive/issue_comments_018028.json:
```json
{
    "body": "Replying to [comment:8 jhpalmieri]:\n> > With this patch, when I do something like \"sage -tp fjfjfjfjfj\", it doesn't tell me that I gave it a bad file:\n> \n> I feel as though this belongs in another ticket.  For what it's worth, previous authors of the file seem to have made this decision intentionally:\n> {{{\n>                else:\n>                     continue # prefer silence to: raise TypeError, \"Unknown File %s\" % F\n> }}}\n\nOkay, that does look like another ticket.\n\n> > Also, when it makes an assumption about the number of threads, I'd like it to print that it's using 1 thread. (Mostly for my own reassurance.)\n> \n> That's easy enough to change; see the new patch.  This version also sets numthreads to be no more than the number of files.\n\nThose look like good changes. Magic 8-ball says...positive review likely.",
    "created_at": "2009-09-23T02:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2624#issuecomment-18028",
    "user": "@dandrake"
}
```

Replying to [comment:8 jhpalmieri]:
> > With this patch, when I do something like "sage -tp fjfjfjfjfj", it doesn't tell me that I gave it a bad file:
> 
> I feel as though this belongs in another ticket.  For what it's worth, previous authors of the file seem to have made this decision intentionally:
> {{{
>                else:
>                     continue # prefer silence to: raise TypeError, "Unknown File %s" % F
> }}}

Okay, that does look like another ticket.

> > Also, when it makes an assumption about the number of threads, I'd like it to print that it's using 1 thread. (Mostly for my own reassurance.)
> 
> That's easy enough to change; see the new patch.  This version also sets numthreads to be no more than the number of files.

Those look like good changes. Magic 8-ball says...positive review likely.



---

archive/issue_comments_018029.json:
```json
{
    "body": "Oops, there's a typo: `numthreads = min(numthreads, len(files))` should be *after* `files` is populated; otherwise, a directory with tons of files counts as one file! If you move that bit to line 324 (after the `populatefilelist(infiles)` stanza), everything works as expected. With that change, I give this patch a positive review. John, after updating your patch, you can change the title to positive review. \n\n**Release manager**: please check the files `COPYING.txt`, `install`, and `spkg-install` into the sage_scripts hg repo! Right now they're not tracked at all.",
    "created_at": "2009-09-23T04:54:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2624#issuecomment-18029",
    "user": "@dandrake"
}
```

Oops, there's a typo: `numthreads = min(numthreads, len(files))` should be *after* `files` is populated; otherwise, a directory with tons of files counts as one file! If you move that bit to line 324 (after the `populatefilelist(infiles)` stanza), everything works as expected. With that change, I give this patch a positive review. John, after updating your patch, you can change the title to positive review. 

**Release manager**: please check the files `COPYING.txt`, `install`, and `spkg-install` into the sage_scripts hg repo! Right now they're not tracked at all.



---

archive/issue_comments_018030.json:
```json
{
    "body": "Replying to [comment:10 ddrake]:\n> Oops, there's a typo\n\nGood catch.  Fixed in the new patch.",
    "created_at": "2009-09-23T05:01:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2624#issuecomment-18030",
    "user": "@jhpalmieri"
}
```

Replying to [comment:10 ddrake]:
> Oops, there's a typo

Good catch.  Fixed in the new patch.



---

archive/issue_comments_018031.json:
```json
{
    "body": "apply to scripts repository",
    "created_at": "2009-09-23T05:01:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2624#issuecomment-18031",
    "user": "@jhpalmieri"
}
```

apply to scripts repository



---

archive/issue_comments_018032.json:
```json
{
    "body": "Attachment [trac_2624-ptest-scripts.patch](tarball://root/attachments/some-uuid/ticket2624/trac_2624-ptest-scripts.patch) by @jhpalmieri created at 2009-09-23 05:02:07",
    "created_at": "2009-09-23T05:02:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2624#issuecomment-18032",
    "user": "@jhpalmieri"
}
```

Attachment [trac_2624-ptest-scripts.patch](tarball://root/attachments/some-uuid/ticket2624/trac_2624-ptest-scripts.patch) by @jhpalmieri created at 2009-09-23 05:02:07



---

archive/issue_comments_018033.json:
```json
{
    "body": "Replying to [comment:10 ddrake]:\n> **Release manager**: please check the files `COPYING.txt`, `install`, and `spkg-install` into the sage_scripts hg repo! Right now they're not tracked at all.\nWhen packaging the Sage source tarball, the files `COPYING.txt`, `install`, and `spkg-install` all end up in the package `sage_scripts.x.y.z.spkg`. When building from source, those three files end up as\n\n* `COPYING.txt` becomes SAGE_ROOT/COPYING.txt --- The directory `SAGE_ROOT` is not tracked:\n {{{\n[mvngu`@`sage sage-4.1.2.alpha2]$ hg st\nabort: There is no Mercurial repository here (.hg not found)!\n }}}\n* `install` becomes SAGE_ROOT/spkg/install --- The directory `SAGE_ROOT/spkg` is not tracked:\n {{{\n[mvngu`@`sage spkg]$ pwd\n/scratch/mvngu/release/sage-4.1.2.alpha2/spkg\n[mvngu`@`sage spkg]$ hg st\nabort: There is no Mercurial repository here (.hg not found)!\n }}}\n* `spkg-install` becomes SAGE_ROOT/local/bin/sage-spkg-install --- The directory `SAGE_ROOT/local/bin` is indeed tracked.\n\nAs it now stand, the changes to `spkg-install` can be checked in to `SAGE_ROOT/local/bin/sage-spkg-install`. Changes for the other two files would need to be manually applied to the relevant files.",
    "created_at": "2009-09-25T04:05:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2624#issuecomment-18033",
    "user": "mvngu"
}
```

Replying to [comment:10 ddrake]:
> **Release manager**: please check the files `COPYING.txt`, `install`, and `spkg-install` into the sage_scripts hg repo! Right now they're not tracked at all.
When packaging the Sage source tarball, the files `COPYING.txt`, `install`, and `spkg-install` all end up in the package `sage_scripts.x.y.z.spkg`. When building from source, those three files end up as

* `COPYING.txt` becomes SAGE_ROOT/COPYING.txt --- The directory `SAGE_ROOT` is not tracked:
 {{{
[mvngu`@`sage sage-4.1.2.alpha2]$ hg st
abort: There is no Mercurial repository here (.hg not found)!
 }}}
* `install` becomes SAGE_ROOT/spkg/install --- The directory `SAGE_ROOT/spkg` is not tracked:
 {{{
[mvngu`@`sage spkg]$ pwd
/scratch/mvngu/release/sage-4.1.2.alpha2/spkg
[mvngu`@`sage spkg]$ hg st
abort: There is no Mercurial repository here (.hg not found)!
 }}}
* `spkg-install` becomes SAGE_ROOT/local/bin/sage-spkg-install --- The directory `SAGE_ROOT/local/bin` is indeed tracked.

As it now stand, the changes to `spkg-install` can be checked in to `SAGE_ROOT/local/bin/sage-spkg-install`. Changes for the other two files would need to be manually applied to the relevant files.



---

archive/issue_comments_018034.json:
```json
{
    "body": "Replying to [comment:13 mvngu]:\n> Replying to [comment:10 ddrake]:\n> > **Release manager**: please check the files `COPYING.txt`, `install`, and `spkg-install` into the sage_scripts hg repo! Right now they're not tracked at all.\n> When packaging the Sage source tarball, the files `COPYING.txt`, `install`, and `spkg-install` all end up in the package `sage_scripts.x.y.z.spkg`. When building from source, those three files end up as\n> \n>  * `COPYING.txt` becomes SAGE_ROOT/COPYING.txt --- The directory `SAGE_ROOT` is not tracked:\n[snip]\n>  * `install` becomes SAGE_ROOT/spkg/install --- The directory `SAGE_ROOT/spkg` is not tracked:\n[snip]\n>  * `spkg-install` becomes SAGE_ROOT/local/bin/sage-spkg-install --- The directory `SAGE_ROOT/local/bin` is indeed tracked.\n> \n> As it now stand, the changes to `spkg-install` can be checked in to `SAGE_ROOT/local/bin/sage-spkg-install`. Changes for the other two files would need to be manually applied to the relevant files.\n\nOkay. It does seem weird that basic source files are not version controlled...but whatever. :)  For the purposes of this ticket, you just need to merge the patch to sage-ptest.",
    "created_at": "2009-09-25T05:19:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2624#issuecomment-18034",
    "user": "@dandrake"
}
```

Replying to [comment:13 mvngu]:
> Replying to [comment:10 ddrake]:
> > **Release manager**: please check the files `COPYING.txt`, `install`, and `spkg-install` into the sage_scripts hg repo! Right now they're not tracked at all.
> When packaging the Sage source tarball, the files `COPYING.txt`, `install`, and `spkg-install` all end up in the package `sage_scripts.x.y.z.spkg`. When building from source, those three files end up as
> 
>  * `COPYING.txt` becomes SAGE_ROOT/COPYING.txt --- The directory `SAGE_ROOT` is not tracked:
[snip]
>  * `install` becomes SAGE_ROOT/spkg/install --- The directory `SAGE_ROOT/spkg` is not tracked:
[snip]
>  * `spkg-install` becomes SAGE_ROOT/local/bin/sage-spkg-install --- The directory `SAGE_ROOT/local/bin` is indeed tracked.
> 
> As it now stand, the changes to `spkg-install` can be checked in to `SAGE_ROOT/local/bin/sage-spkg-install`. Changes for the other two files would need to be manually applied to the relevant files.

Okay. It does seem weird that basic source files are not version controlled...but whatever. :)  For the purposes of this ticket, you just need to merge the patch to sage-ptest.



---

archive/issue_comments_018035.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-25T06:24:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2624#issuecomment-18035",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_018036.json:
```json
{
    "body": "Merged in the script repository.",
    "created_at": "2009-09-25T06:24:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2624#issuecomment-18036",
    "user": "mvngu"
}
```

Merged in the script repository.



---

archive/issue_comments_018037.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T10:25:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2624",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2624#issuecomment-18037",
    "user": "mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
