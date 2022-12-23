# Issue 2681: [with patch, needs review] improve doctest coverage in libs/pari/gen.pyx

Issue created by migration from https://trac.sagemath.org/ticket/2681

Original creator: AlexGhitza

Original creation time: 2008-03-27 03:39:00

Assignee: failure

Keywords: doctest pari elliptic

I added a number of doctests to gen.pyx (mostly for the functions dealing with elliptic curves), and did some general cleaning up.  (In the process I ran into a couple of PARI bugs and reported them upstream.)

I intend to continue this at some point, but the patch is getting large so I decided to submit it for review.



---

Attachment


---

Comment by cremona created at 2008-03-27 17:40:45

Great job!  Sage's docs for some of these functions are now better than pari's own.  Merge this!


---

Comment by mabshoff created at 2008-03-28 05:07:25

Merged in Sage 2.11.alpha2


---

Comment by mabshoff created at 2008-03-28 05:07:25

Resolution: fixed


---

Comment by mabshoff created at 2008-03-28 06:35:37

Some slight 64 bit problems: 

```
sage -t -long devel/sage-main/sage/libs/pari/gen.pyx        **********************************************************************
File "gen.pyx", line 4159:
    sage: e.elleta()
Expected:
    [3.605463601432652085915820564, 10.81639080429795625774746169*I]
Got:
    [3.6054636014326520859158205642077267748, 10.816390804297956257747461692623180324*I]
**********************************************************************
File "gen.pyx", line 4184:
    sage: e.ellheight([1,0])
Expected:
    0.4767116593437395373794860589
Got:
    0.47671165934373953737948605888465305946
**********************************************************************
File "gen.pyx", line 4186:
    sage: e.ellheight([1,0], flag=0)
Expected:
    0.4767116593437395373794860589
Got:
    0.47671165934373953737948605888465305946
**********************************************************************
File "gen.pyx", line 4188:
    sage: e.ellheight([1,0], flag=1)
Expected:
    0.4767116593437395373794860589
Got:
    0.47671165934373953737948605888465305946
**********************************************************************
File "gen.pyx", line 4210:
    sage: e.ellheightmatrix([[1,0], [-1,1]])
Expected:
    [0.4767116593437395373794860589, 0.4181889844988605856298894582; 0.4181889844988605856298894582, 0.6866670833055865857235521030]
Got:
    [0.47671165934373953737948605888465305946, 0.41818898449886058562988945821587638238; 0.41818898449886058562988945821587638238, 0.68666708330558658572355210295409678906]
**********************************************************************
File "gen.pyx", line 4382:
    sage: e.elllseries(2.1, A=1.1)
Expected:
    0.4028380479566455158
Got:
    0.4028380479566455157
**********************************************************************
File "gen.pyx", line 4456:
    sage: e.ellordinate(I)
Expected:
    [0.5822035897217411772333894787 - 1.386060824641769718531183421*I, -1.582203589721741177233389479 + 1.386060824641769718531183421*I]
Got:
    [0.58220358972174117723338947874993600727 - 1.3860608246417697185311834209833653345*I, -1.5822035897217411772333894787499360073 + 1.3860608246417697185311834209833653345*I]
**********************************************************************
File "gen.pyx", line 4480:
    sage: e.ellpointtoz([0,0])
Expected:
    1.854074677301371918433850347
Got:
    1.8540746773013719184338503471952600462
**********************************************************************
File "gen.pyx", line 4628:
    sage: e.ellzeta(1)
Expected:
    1.064798412958827927449913418 + 3.491753745 E-251*I
Got:
    1.0647984129588279274499134181598985072 - 8.016988209895862073 E-694*I
**********************************************************************
File "gen.pyx", line 4630:
    sage: e.ellzeta(I-1)
Expected:
    -0.3501226585230491632779704180 - 0.3501226585230491632779704180*I
Got:
    -0.35012265852304916327797041802108326818 - 0.35012265852304916327797041802108326818*I
**********************************************************************
File "gen.pyx", line 4652:
    sage: e.ellztopoint(1+I)
Expected:
    [0.E-251 - 1.021522867956699099826892460*I, -0.1490728137010962128964506933 - 0.1490728137010962128964506933*I]
Got:
    [0.E-694 - 1.0215228679566990998268924596833713669*I, -0.14907281370109621289645069325289375075 - 0.14907281370109621289645069325289375075*I]
**********************************************************************
```

Patch coming up.

Cheers,

Michael


---

Attachment


```
[07:10] <mabshoff> #2681 now has the 64 bit pari fix.
[07:10] <mabshoff> Trivial review anyone?
[07:11] <wstein> [positive review]
```


Merged the doctest fix patch in 2.11.alpha2

Cheers,

Michael
