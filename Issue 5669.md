# Issue 5669: [with patch, needs review] New algorithm for Max Clique in Graph class

archive/issues_005669.json:
```json
{
    "body": "Assignee: rlm\n\nCC:  rlm\n\nKeywords: independant set stable clique\n\nI recently had to compute a maximum stable set in a graph with 100 vertices and ended up waiting a whole day ( to no good end ) for Sage to compute it. The current algorithm uses the library NetworkX whose algorithm is not nearly as efficient as Cliquer :\n\nhttp://www.tkk.fi/~pat/cliquer.html\n\nIt is based on an algorithm published in 2002, and it gave me a result in less than a millisecond ;-)\n\nHere are the modification I made :\n- I created a spkg file containing the sources of this software for it to be available in SAGE\n- I wrote the interface to use it\n- I modified the Graph class to use this software instead.\n- Added to the function to compute the maximum clique, I added the function Maximum independant set ( which is a similar notion for the complement of a graph, a bit more customary ). As the algorithm provided a function to compute all the maximum cliques, I also added this function\n\nIssue created by migration from https://trac.sagemath.org/ticket/5669\n\n",
    "created_at": "2009-04-02T20:16:24Z",
    "labels": [
        "graph theory",
        "minor",
        "enhancement"
    ],
    "title": "[with patch, needs review] New algorithm for Max Clique in Graph class",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5669",
    "user": "ncohen"
}
```
Assignee: rlm

CC:  rlm

Keywords: independant set stable clique

I recently had to compute a maximum stable set in a graph with 100 vertices and ended up waiting a whole day ( to no good end ) for Sage to compute it. The current algorithm uses the library NetworkX whose algorithm is not nearly as efficient as Cliquer :

http://www.tkk.fi/~pat/cliquer.html

It is based on an algorithm published in 2002, and it gave me a result in less than a millisecond ;-)

Here are the modification I made :
- I created a spkg file containing the sources of this software for it to be available in SAGE
- I wrote the interface to use it
- I modified the Graph class to use this software instead.
- Added to the function to compute the maximum clique, I added the function Maximum independant set ( which is a similar notion for the complement of a graph, a bit more customary ). As the algorithm provided a function to compute all the maximum cliques, I also added this function

Issue created by migration from https://trac.sagemath.org/ticket/5669





---

archive/issue_comments_044347.json:
```json
{
    "body": "Attachment [11803.patch](tarball://root/attachments/some-uuid/ticket5669/11803.patch) by ncohen created at 2009-04-02 20:19:07",
    "created_at": "2009-04-02T20:19:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5669",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5669#issuecomment-44347",
    "user": "ncohen"
}
```

Attachment [11803.patch](tarball://root/attachments/some-uuid/ticket5669/11803.patch) by ncohen created at 2009-04-02 20:19:07



---

archive/issue_comments_044348.json:
```json
{
    "body": "Hi,\n\na couple remarks:\n\n* do not attach spkgs to trac tickets, but put them up somewhere on the web and post a link. I did that in this case\n* the spkg contains binaries and object files, i.e. you need to run \"make clean\" on the content of the spkg\n* the patch deletes working code, i.e. it should still be possible to call the NetworkX code even if it sucks\n* your new code has 0% doctest coverage\n\nThere is more, but the above should keep you busy for a while :)\n\nCheers,\n\nMichael",
    "created_at": "2009-04-02T20:34:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5669",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5669#issuecomment-44348",
    "user": "mabshoff"
}
```

Hi,

a couple remarks:

* do not attach spkgs to trac tickets, but put them up somewhere on the web and post a link. I did that in this case
* the spkg contains binaries and object files, i.e. you need to run "make clean" on the content of the spkg
* the patch deletes working code, i.e. it should still be possible to call the NetworkX code even if it sucks
* your new code has 0% doctest coverage

There is more, but the above should keep you busy for a while :)

Cheers,

Michael



---

archive/issue_comments_044349.json:
```json
{
    "body": "Well, to be fair, the new code is half doctested.  The new graph functions are doctested, the interface functions are not doctested.",
    "created_at": "2009-04-15T06:10:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5669",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5669#issuecomment-44349",
    "user": "jason"
}
```

Well, to be fair, the new code is half doctested.  The new graph functions are doctested, the interface functions are not doctested.



---

archive/issue_comments_044350.json:
```json
{
    "body": "Duplication of #6355.",
    "created_at": "2009-06-22T22:34:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5669",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5669#issuecomment-44350",
    "user": "rlm"
}
```

Duplication of #6355.



---

archive/issue_comments_044351.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-06-22T22:34:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5669",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5669#issuecomment-44351",
    "user": "rlm"
}
```

Resolution: duplicate



---

archive/issue_comments_044352.json:
```json
{
    "body": "ncohen,\n\nIf the patch on this ticket is no longer needed, can you delete the \"[with patch, needs work]\" in the title?  If it is still needed, can you either reopen this ticket so the patch is not lost or move the patch to another ticket that is open?  It is confusing to have a patch that \"needs work\" on a closed ticket.\n\nThanks.",
    "created_at": "2009-07-10T11:13:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5669",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5669#issuecomment-44352",
    "user": "jason"
}
```

ncohen,

If the patch on this ticket is no longer needed, can you delete the "[with patch, needs work]" in the title?  If it is still needed, can you either reopen this ticket so the patch is not lost or move the patch to another ticket that is open?  It is confusing to have a patch that "needs work" on a closed ticket.

Thanks.



---

archive/issue_comments_044353.json:
```json
{
    "body": "Actually, I do not know if I can close this ticket and delete the patch : I do not understand how the patches work.\nEach time I create a patch, it contains the differences between the last patch I created and the current version. Hence, as the others patches seem to have been built over this one, can I really delete it or do I need to move it to the current ticket for Cliquer's patch, which is http://trac.sagemath.org/sage_trac/ticket/5793 ?\n\nThanks !\n\nNathann",
    "created_at": "2009-07-16T14:00:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5669",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5669#issuecomment-44353",
    "user": "ncohen"
}
```

Actually, I do not know if I can close this ticket and delete the patch : I do not understand how the patches work.
Each time I create a patch, it contains the differences between the last patch I created and the current version. Hence, as the others patches seem to have been built over this one, can I really delete it or do I need to move it to the current ticket for Cliquer's patch, which is http://trac.sagemath.org/sage_trac/ticket/5793 ?

Thanks !

Nathann



---

archive/issue_comments_044354.json:
```json
{
    "body": "Replying to [comment:7 ncohen]:\n> Actually, I do not know if I can close this ticket and delete the patch\n\nThere is no need for any of this -- what you need to do is make sure that all the patches needed by #5793 are actually on ticket #5793. Also, while you are at it, you should probably use more descriptive names than the five-digit numbers you have been using (this also leads to the confusion that the 11803.patch here is only 6.0KB and the one there is 229.4KB). The suggested format is `trac_####-description.patch`. You also need to indicate at that ticket exactly which patches should go in, and in what order.\n\n> Each time I create a patch, it contains the differences between the last patch I created and the current version. Hence, as the others patches seem to have been built over this one, can I really delete it or do I need to move it to the current ticket for Cliquer's patch, which is http://trac.sagemath.org/sage_trac/ticket/5793 ?\n\nThere is also the option of using Mercurial queues to flatten patches (i.e. roll several patches into one). That way, you could eventually post just one patch which does everything, and then you could ask someone with admin privileges (such as myself) to delete the other patches, in order to clean things up.",
    "created_at": "2009-07-16T18:51:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5669",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5669#issuecomment-44354",
    "user": "rlm"
}
```

Replying to [comment:7 ncohen]:
> Actually, I do not know if I can close this ticket and delete the patch

There is no need for any of this -- what you need to do is make sure that all the patches needed by #5793 are actually on ticket #5793. Also, while you are at it, you should probably use more descriptive names than the five-digit numbers you have been using (this also leads to the confusion that the 11803.patch here is only 6.0KB and the one there is 229.4KB). The suggested format is `trac_####-description.patch`. You also need to indicate at that ticket exactly which patches should go in, and in what order.

> Each time I create a patch, it contains the differences between the last patch I created and the current version. Hence, as the others patches seem to have been built over this one, can I really delete it or do I need to move it to the current ticket for Cliquer's patch, which is http://trac.sagemath.org/sage_trac/ticket/5793 ?

There is also the option of using Mercurial queues to flatten patches (i.e. roll several patches into one). That way, you could eventually post just one patch which does everything, and then you could ask someone with admin privileges (such as myself) to delete the other patches, in order to clean things up.
