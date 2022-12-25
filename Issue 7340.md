# Issue 7340: cayley_table has a syntax error

archive/issues_007340.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @rbeezer @jasongrout mvngu\n\n\n```\nsage: SymmetricGroup(6).cayley_table()\n------------------------------------------------------------\n   File \"<string>\", line 1\n     [(1,154,305,451,577,601,),(2,153,306,452,578,602,),(3,156,302,453,579,603,),(4,155,301,454,580,604,),(5,151,304,455,581,605,),(6,152,303,456,582,606,),(7,160,311,437,583,607,),(8,159,312,438,584,608,),(9,162,308,434,585,609,),(10,161,307,433,586,610,),(11,157,310,436,587,611,),(12,158,309,435,588,612,),(13,166,292,443,589,613,),(14,165,291,444,590,614,),(15,168,294,440,591,615,),(16,167,293,439,592,616,),(17,163,289,442,593,617,),(18,164,290,441,594,618,),(19,145,298,449,595,619,),(20,146,297,450,596,620,),(21,147,300,446,597,621,),(22,148,299,445,598,622,),(23,149,295,448,599,623,),(24,150,296,447,600,624,),(25,178,329,475,499,625,),(26,177,330,476,500,626,),(27,180,326,477,501,627,),(28,179,325,478,502,628,),(29,175,328,479,503,629,),(30,176,327,480,504,630,),(31,184,335,461,485,631,),(32,183,336,462,486,632,),(33,186,332,458,482,633,),(34,185,331,457,481,634,),([...],)]\n                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   ^\nSyntaxError: invalid syntax\n\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7340\n\n",
    "created_at": "2009-10-28T21:42:38Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.2",
    "title": "cayley_table has a syntax error",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7340",
    "user": "https://github.com/jasongrout"
}
```
Assignee: tbd

CC:  @rbeezer @jasongrout mvngu


```
sage: SymmetricGroup(6).cayley_table()
------------------------------------------------------------
   File "<string>", line 1
     [(1,154,305,451,577,601,),(2,153,306,452,578,602,),(3,156,302,453,579,603,),(4,155,301,454,580,604,),(5,151,304,455,581,605,),(6,152,303,456,582,606,),(7,160,311,437,583,607,),(8,159,312,438,584,608,),(9,162,308,434,585,609,),(10,161,307,433,586,610,),(11,157,310,436,587,611,),(12,158,309,435,588,612,),(13,166,292,443,589,613,),(14,165,291,444,590,614,),(15,168,294,440,591,615,),(16,167,293,439,592,616,),(17,163,289,442,593,617,),(18,164,290,441,594,618,),(19,145,298,449,595,619,),(20,146,297,450,596,620,),(21,147,300,446,597,621,),(22,148,299,445,598,622,),(23,149,295,448,599,623,),(24,150,296,447,600,624,),(25,178,329,475,499,625,),(26,177,330,476,500,626,),(27,180,326,477,501,627,),(28,179,325,478,502,628,),(29,175,328,479,503,629,),(30,176,327,480,504,630,),(31,184,335,461,485,631,),(32,183,336,462,486,632,),(33,186,332,458,482,633,),(34,185,331,457,481,634,),([...],)]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   ^
SyntaxError: invalid syntax

```



Issue created by migration from https://trac.sagemath.org/ticket/7340





---

archive/issue_comments_061312.json:
```json
{
    "body": "Changing assignee from tbd to joyner.",
    "created_at": "2009-10-28T23:05:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7340#issuecomment-61312",
    "user": "https://github.com/rbeezer"
}
```

Changing assignee from tbd to joyner.



---

archive/issue_comments_061313.json:
```json
{
    "body": "Looking at the code, its not obvious to me just where this output is coming from.  Maybe from GAP?\n\n`SymmetricGroup(5).cayley_table()` completes properly.\n\n`CyclicPermutationGroup(200).cayley_table()` completes (after a wait).\n\n`CyclicPermutationGroup(720).cayley_table()` ran for a while without an error before I killed it.\n\nSo I don't think the bug is simply a question of the size of the group.\n\nNormal behavior creates a \"Multivariate Polynomial Ring\" with as many variables as the order of the group.  Would a more brute-force approach (form all `n^2` products and locate results in the list of elements) be a more general and less error-prone approach?\n\nRob",
    "created_at": "2009-10-28T23:05:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7340#issuecomment-61313",
    "user": "https://github.com/rbeezer"
}
```

Looking at the code, its not obvious to me just where this output is coming from.  Maybe from GAP?

`SymmetricGroup(5).cayley_table()` completes properly.

`CyclicPermutationGroup(200).cayley_table()` completes (after a wait).

`CyclicPermutationGroup(720).cayley_table()` ran for a while without an error before I killed it.

So I don't think the bug is simply a question of the size of the group.

Normal behavior creates a "Multivariate Polynomial Ring" with as many variables as the order of the group.  Would a more brute-force approach (form all `n^2` products and locate results in the list of elements) be a more general and less error-prone approach?

Rob



---

archive/issue_comments_061314.json:
```json
{
    "body": "Changing component from algebra to group_theory.",
    "created_at": "2009-10-28T23:05:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7340#issuecomment-61314",
    "user": "https://github.com/rbeezer"
}
```

Changing component from algebra to group_theory.



---

archive/issue_comments_061315.json:
```json
{
    "body": "I think this is just the size of the group that is the issue. I could be wrong though.",
    "created_at": "2010-03-05T11:37:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7340#issuecomment-61315",
    "user": "https://github.com/wdjoyner"
}
```

I think this is just the size of the group that is the issue. I could be wrong though.



---

archive/issue_comments_061316.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2010-03-06T02:54:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7340#issuecomment-61316",
    "user": "https://github.com/dimpase"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_061317.json:
```json
{
    "body": "Replying to [comment:1 rbeezer]:\n\nI can easily rewrite this in few gap.eval and gap commands, to get the multiplication table that \n1) works by on order of magnitude, at least, faster\n2) works for bigger groups, including S_6\n\nThe result would be just the table (list of lists) with entries being indices of elements of the group numbered\nin some order.\n\nBut I do not understand why that multivariate ring must be there.\n\nDima\n\n\n> Looking at the code, its not obvious to me just where this output is coming from.  Maybe from GAP?\n> \n> `SymmetricGroup(5).cayley_table()` completes properly.\n> \n> `CyclicPermutationGroup(200).cayley_table()` completes (after a wait).\n> \n> `CyclicPermutationGroup(720).cayley_table()` ran for a while without an error before I killed it.\n> \n> So I don't think the bug is simply a question of the size of the group.\n> \n> Normal behavior creates a \"Multivariate Polynomial Ring\" with as many variables as the order of the group.  Would a more brute-force approach (form all `n^2` products and locate results in the list of elements) be a more general and less error-prone approach?\n> \n> Rob",
    "created_at": "2010-03-06T02:54:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7340#issuecomment-61317",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:1 rbeezer]:

I can easily rewrite this in few gap.eval and gap commands, to get the multiplication table that 
1) works by on order of magnitude, at least, faster
2) works for bigger groups, including S_6

The result would be just the table (list of lists) with entries being indices of elements of the group numbered
in some order.

But I do not understand why that multivariate ring must be there.

Dima


> Looking at the code, its not obvious to me just where this output is coming from.  Maybe from GAP?
> 
> `SymmetricGroup(5).cayley_table()` completes properly.
> 
> `CyclicPermutationGroup(200).cayley_table()` completes (after a wait).
> 
> `CyclicPermutationGroup(720).cayley_table()` ran for a while without an error before I killed it.
> 
> So I don't think the bug is simply a question of the size of the group.
> 
> Normal behavior creates a "Multivariate Polynomial Ring" with as many variables as the order of the group.  Would a more brute-force approach (form all `n^2` products and locate results in the list of elements) be a more general and less error-prone approach?
> 
> Rob



---

archive/issue_comments_061318.json:
```json
{
    "body": "Replying to [comment:3 dimpase]:\n> Replying to [comment:1 rbeezer]:\n> \n> I can easily rewrite this in few gap.eval and gap commands, to get the multiplication table that \n> 1) works by on order of magnitude, at least, faster\n> 2) works for bigger groups, including S_6\n> \n> The result would be just the table (list of lists) with entries being indices of elements of the group numbered\n> in some order.\n> \n> But I do not understand why that multivariate ring must be there.\n> \n> Dima\n> \n> \n\nIf you can do this, then this should be added as the default, IMHO. The multivariate ring is there in case you want to have the multiplication table given more compactly in terms of symbols (as opposed to permutations). I guess it was designed mostly so larger examples could created which then could be latexed for class notes. Note a key feature but I think a useful option for teachers.",
    "created_at": "2010-03-06T06:10:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7340#issuecomment-61318",
    "user": "https://github.com/wdjoyner"
}
```

Replying to [comment:3 dimpase]:
> Replying to [comment:1 rbeezer]:
> 
> I can easily rewrite this in few gap.eval and gap commands, to get the multiplication table that 
> 1) works by on order of magnitude, at least, faster
> 2) works for bigger groups, including S_6
> 
> The result would be just the table (list of lists) with entries being indices of elements of the group numbered
> in some order.
> 
> But I do not understand why that multivariate ring must be there.
> 
> Dima
> 
> 

If you can do this, then this should be added as the default, IMHO. The multivariate ring is there in case you want to have the multiplication table given more compactly in terms of symbols (as opposed to permutations). I guess it was designed mostly so larger examples could created which then could be latexed for class notes. Note a key feature but I think a useful option for teachers.



---

archive/issue_comments_061319.json:
```json
{
    "body": "Replying to [comment:3 dimpase]:\n> Replying to [comment:1 rbeezer]:\n> \n> I can easily rewrite this in few gap.eval and gap commands, to get the multiplication table that \n> 1) works by on order of magnitude, at least, faster\n> 2) works for bigger groups, including S_6\n> \n> The result would be just the table (list of lists) with entries being indices of elements of the group numbered\n> in some order.\n\nHi Dima,\n\nI have something a bit more general working.  An out-of-date version is at #7555.  It just assumes an algebraic structure has a binary operation and builds a table from there.  When complete it should have more flexibility for output.  I'm not sure speed is a big issue because by the time you try to build a big table, you probably can't view it very easily anyway.\n\n> But I do not understand why that multivariate ring must be there.\n\nFor one it made formatting the output very easy - just ask to print a matrix and let the matrix code do the work.  I can't see much more benefit.  I'll likely include this as an optional output form for anybody who needs it.\n\nFinishing this up is my next/current Sage project.  Could I cc you on #7555 and maybe you can review it once I get a decent patch up?\n\nThanks,\nRob",
    "created_at": "2010-03-06T21:09:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7340#issuecomment-61319",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:3 dimpase]:
> Replying to [comment:1 rbeezer]:
> 
> I can easily rewrite this in few gap.eval and gap commands, to get the multiplication table that 
> 1) works by on order of magnitude, at least, faster
> 2) works for bigger groups, including S_6
> 
> The result would be just the table (list of lists) with entries being indices of elements of the group numbered
> in some order.

Hi Dima,

I have something a bit more general working.  An out-of-date version is at #7555.  It just assumes an algebraic structure has a binary operation and builds a table from there.  When complete it should have more flexibility for output.  I'm not sure speed is a big issue because by the time you try to build a big table, you probably can't view it very easily anyway.

> But I do not understand why that multivariate ring must be there.

For one it made formatting the output very easy - just ask to print a matrix and let the matrix code do the work.  I can't see much more benefit.  I'll likely include this as an optional output form for anybody who needs it.

Finishing this up is my next/current Sage project.  Could I cc you on #7555 and maybe you can review it once I get a decent patch up?

Thanks,
Rob



---

archive/issue_comments_061320.json:
```json
{
    "body": "Replying to [comment:5 rbeezer]:\n\n> Finishing this up is my next/current Sage project.  Could I cc you on #7555 and maybe you can review it once I get a decent patch up?\n\nSure!\nBest,\nDima\n> \n> Thanks,\n> Rob",
    "created_at": "2010-03-07T12:50:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7340#issuecomment-61320",
    "user": "https://github.com/dimpase"
}
```

Replying to [comment:5 rbeezer]:

> Finishing this up is my next/current Sage project.  Could I cc you on #7555 and maybe you can review it once I get a decent patch up?

Sure!
Best,
Dima
> 
> Thanks,
> Rob



---

archive/issue_comments_061321.json:
```json
{
    "body": "This is now obsolete/fixed as a result of #7555, so should be retired.\n\nI've cc'ed mvngu (who I think is currently doing release management work?).",
    "created_at": "2010-05-11T18:22:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7340#issuecomment-61321",
    "user": "https://github.com/rbeezer"
}
```

This is now obsolete/fixed as a result of #7555, so should be retired.

I've cc'ed mvngu (who I think is currently doing release management work?).



---

archive/issue_comments_061322.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-11T20:13:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7340#issuecomment-61322",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_017370.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-05-11T20:13:09Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7340",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7340#event-17370"
}
```



---

archive/issue_comments_061323.json:
```json
{
    "body": "Close as fixed by #7555:\n\n```\n[mvngu@sage ~]$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: T = SymmetricGroup(6).cayley_table().table()\nsage: T[0]\n[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, \n26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, \n50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, \n74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, \n98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, \n117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, \n136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, \n155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, \n174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, \n193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, \n212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, \n231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, \n250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, \n269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, \n288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, \n307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, \n326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, \n345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, \n364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, \n383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, \n402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, \n421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, \n440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, \n459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, \n478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, \n497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, \n516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, \n535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, \n554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, \n573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, \n592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, \n611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, \n630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, \n649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, \n668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, \n687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, \n706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719]\n```\n",
    "created_at": "2010-05-11T20:13:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7340#issuecomment-61323",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Close as fixed by #7555:

```
[mvngu@sage ~]$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: T = SymmetricGroup(6).cayley_table().table()
sage: T[0]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 
26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 
50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 
74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 
98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 
117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 
136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 
155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 
174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 
193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 
212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 
231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 
250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 
269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 
288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 
307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 
326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 
345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 
364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 
383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 
402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 
421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 
440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 
459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 
478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 
497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513, 514, 515, 
516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 530, 531, 532, 533, 534, 
535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 
554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 
573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 
592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 
611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 
630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 
649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664, 665, 666, 667, 
668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 685, 686, 
687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704, 705, 
706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719]
```

