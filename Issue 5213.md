# Issue 5213: [with patch, needs review] make charpoly/minpoly of number field elements use matrix()

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2009-02-09 04:47:01

Assignee: was

Keywords: number field element minpoly charpoly

Sage computes charpoly's of large matrices *much* faster than Pari does.


---

Attachment

The patch speeds up computations of charpoly and minpoly (a lot -- sage's linear algebra is much better than pari's for some of my examples).

It also makes charpoly, minpoly, absolute_charpoly, and absolute_minpoly work for relative order elements.


---

Comment by mabshoff created at 2009-02-09 12:51:57

With this patch applied to my current 3.3.rc0 merge tree all doctests pass.

Nick: It would be nice to have performance numbers before and after to motivate someone to review this ticket :)

Cheers,

Michael


---

Comment by ncalexan created at 2009-02-09 17:50:40

Or perhaps not -- now it seems like this is significantly slower!  All I know is that my code would not return from a charpoly call and when I changed this it was much faster.  Now I can't replicate it.  I will try to split the doctests and order stuff out from the actual change and figure out what I was seeing.


---

Comment by AlexGhitza created at 2009-02-14 23:42:10

Actually, on my laptop, with the example


```
sage: R.<x> = ZZ[]
sage: f = x^32 - x^31 + 2*x^30 - x^28 - 2*x^27 + 8*x^26 + 2*x^25 + 2*x^24 + x^22 - 2*x^20 + x^18 + x^17 - 3*x^16 + 51*x^15 - 2*x^14 - 5*x^13 + 3*x^12 - x^9 + x^8 - x^7 - 2*x^6 - 2*x^5 - x^4 + 5
sage: K.<a> = NumberField(f)
sage: b = -1/2*a^31 - 12*a^30 + a^29 - 1/64*a^28 + 2/3*a^26 + 1/7*a^25 - 2*a^24 + 1/3*a^19 - 6*a^18 - 11*a^17 - 2*a^15 + 1/32*a^14 + a^13 + a^11 - 1/17*a^9 + 2*a^8 + 1/32*a^6 + a^5 + 1/6*a^4 + 2*a^3 - 2/3*a^2 - 59*a + 1
```


I get, before the patch:


```
sage: time c = b.charpoly()
CPU times: user 0.15 s, sys: 0.00 s, total: 0.15 s
Wall time: 0.14 s
```


and after the patch:


```
sage: time c = b.charpoly()
CPU times: user 0.03 s, sys: 0.00 s, total: 0.03 s
Wall time: 0.04 s
```


Just for the heck of it, I tried a degree 61 extension, and I get 7.44 seconds before the patch, and 0.26 seconds after it.

So I'm motivated to review it :)

Nick, if you're reading this, do you have an example where the new code is significantly slower?


---

Comment by AlexGhitza created at 2009-02-15 02:37:19

Some experiments indicate that pari is faster (sometimes significantly) than sage for degrees up to about 20, after which sage becomes significantly faster than pari.  I am attaching a .sage file that has a tuning function in it.  Use it as follows:


```
sage: load tune_charpoly_nf
sage: tune_charpoly_nf(dmin=2, dmax=30)   # dmin to dmax is the range of degrees to test
degree = 2
pari wins 4.00543212891e-06
sage  0.000656795501709

degree = 3
pari wins 1.13964080811e-05
sage  0.000749778747559

degree = 4
pari wins 1.55925750732e-05
sage  0.00109262466431

degree = 5
pari wins 3.01837921143e-05
sage  0.00100917816162

degree = 6
pari wins 4.68254089355e-05
sage  0.00144081115723

degree = 7
pari wins 6.31809234619e-05
sage  0.00146918296814

degree = 8
pari wins 0.000140428543091
sage  0.00191378593445

degree = 9
pari wins 0.000134992599487
sage  0.00177617073059

degree = 10
pari wins 0.000328207015991
sage  0.00198397636414

degree = 11
pari wins 0.000636005401611
sage  0.00321359634399

degree = 12
pari wins 0.000763988494873
sage  0.00339140892029

degree = 13
pari wins 0.000882387161255
sage  0.00338182449341

degree = 14
pari wins 0.00109162330627
sage  0.00367736816406

degree = 15
pari wins 0.00157079696655
sage  0.0045955657959

degree = 16
pari wins 0.00219879150391
sage  0.00466103553772

degree = 17
pari wins 0.00490641593933
sage  0.00696640014648

degree = 18
pari wins 0.00486760139465
sage  0.00733642578125

degree = 19
pari wins 0.00619320869446
sage  0.00774478912354

degree = 20
pari wins 0.00522680282593
sage  0.00600438117981

degree = 21
pari  0.0129831790924
sage wins 0.0107915878296

degree = 22
pari  0.0156112194061
sage wins 0.0101305961609

degree = 23
pari  0.0110792160034
sage wins 0.00913519859314

degree = 24
pari  0.0374025821686
sage wins 0.0117425918579

degree = 25
pari  0.0204313755035
sage wins 0.00851321220398

degree = 26
pari  0.0463576316833
sage wins 0.017144203186

degree = 27
pari  0.0754494190216
sage wins 0.0211450099945

degree = 28
pari  0.0682522296906
sage wins 0.0146000385284

degree = 29
pari  0.0482114315033
sage wins 0.016219997406

degree = 30
pari  0.129074573517
sage wins 0.0263453960419
```


I hope the output is fairly self-explanatory (the times are in seconds).  The above run, on which it appears that degree=21 is a good point to switch algorithms, was on my laptop:


```
[ghitza`@`artin 5213]$ uname -a
Linux artin 2.6.28-ARCH #1 SMP PREEMPT Sun Feb 8 10:13:45 UTC 2009 i686 Intel(R) Core(TM)2 Duo CPU T9300 `@` 2.50GHz GenuineIntel GNU/Linux
```


Michael said he'd run the tuning on a lot of architectures, so we can pick a switch point for the algorithms.


---

Attachment

Note: the tuning function doesn't work properly on sage-3.2.3 because it relies on K.random_element() which was only introduced recently.  Running it on 3.3.rc0 is fine.


---

Comment by mabshoff created at 2009-02-15 06:56:17

Here are raw number from SkyNet using 3.3.a6:

x86-64:

```
degree = 17
pari wins 0.00229816436768
sage  0.00491762161255

degree = 18
pari wins 0.0021155834198
sage  0.00446100234985

degree = 19
pari wins 0.00506358146667
sage  0.00699300765991

degree = 20
pari wins 0.00411558151245
sage  0.00622420310974

degree = 21
pari wins 0.00736718177795
sage  0.00949778556824

degree = 22
pari wins 0.00956983566284
sage  0.00974102020264

degree = 23
pari  0.0127023696899
sage wins 0.0122896194458

degree = 24
pari  0.0149556159973
sage wins 0.0125447750092

degree = 25
pari  0.0175543785095
sage wins 0.0138979911804
```


Itanium:

```
degree = 21
pari wins 0.0198247909546
sage  0.0222320079803

degree = 22
pari wins 0.0186019897461
sage  0.0233061790466

degree = 23
pari wins 0.0215002059937
sage  0.0262903690338

degree = 24
pari wins 0.0237666130066
sage  0.0263331890106

degree = 25
pari wins 0.0279534339905
sage  0.0286905765533

degree = 26
pari  0.0458751678467
sage wins 0.04019780159

degree = 27
pari  0.0536995887756
sage wins 0.0434513568878

degree = 28
pari  0.0577178001404
sage wins 0.0450903892517

degree = 29
pari  0.0635250091553
sage wins 0.0411161899567
```


Sparc:

```
degree = 16
pari wins 0.0125590324402
sage  0.0307261943817

degree = 17
pari wins 0.0167366027832
sage  0.0388498306274

degree = 18
pari wins 0.0165439605713
sage  0.0391522407532

degree = 19
pari wins 0.0277721881866
sage  0.0442552089691

degree = 20
pari wins 0.0381276130676
sage  0.0519647598267

degree = 21
pari wins 0.0364107608795
sage  0.0499869823456

degree = 22
pari  0.0642548084259
sage wins 0.0621823787689

degree = 23
pari  0.124836015701
sage wins 0.0889253616333

degree = 24
pari  0.0919447898865
sage wins 0.0757274150848

degree = 25
pari  0.0899034023285
sage wins 0.0747012138367
```


x86:

```
degree = 21
pari  0.0268085956573
sage wins 0.0253339767456

degree = 22
pari  0.0326518058777
sage wins 0.0288281917572

degree = 23
pari  0.0283989906311
sage wins 0.0185689926147

degree = 24
pari  0.024268579483
sage wins 0.022793006897

degree = 25
pari  0.0552956104279
sage wins 0.036269235611

degree = 26
pari  0.0416465759277
sage wins 0.0275146007538

degree = 27
pari  0.0451163768768
sage wins 0.030538225174

degree = 28
pari  0.0625371932983
sage wins 0.0331691741943
```


G5:

```
degree = 20
pari wins 0.0234020233154
sage  0.0504786014557

degree = 21
pari wins 0.016481590271
sage  0.0431175708771

degree = 22
pari wins 0.030487203598
sage  0.0558780193329

degree = 23
pari wins 0.0218068122864
sage  0.0527520179749

degree = 24
pari wins 0.0816434383392
sage  0.0871819972992

degree = 25
pari wins 0.0597079753876
sage  0.0701484203339

degree = 26
pari  0.12759976387
sage wins 0.11203417778

degree = 27
pari wins 0.0611779689789
sage  0.0773588180542

degree = 28
pari  0.14080581665
sage wins 0.128568601608
```



---

Comment by AlexGhitza created at 2009-02-15 10:50:56

OK, we're going with a threshold degree of 25.  I'm giving Nick's patch a positive review, and someone needs to look at my additional patch which implements the threshold and adds docstrings/doctests.


---

Attachment

I read trac_5213-treshold.patch and give it a positive review. The doctests also pass.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-15 13:33:47

Merged in Sage 3.3.rc1.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-15 13:33:47

Resolution: fixed
