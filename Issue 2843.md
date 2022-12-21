# Issue 2843: p-adic extension  segfault

Issue created by migration from Trac.

Original creator: jen

Original creation time: 2008-04-07 13:59:48

Assignee: was

Manipulating power series over p-adic extensions causes segfaults:


```
sage: R.<x> = QQ[]
sage: K = Qp(11,10)
sage: J.<a> = K.extension(x^30-11)
sage: M.<t> = PowerSeriesRing(J)
sage: S.<x,y> = QQ[]
sage: F = [x,x^2,x^3]
sage: xr = O(a^152)*t + (8*a^2 + 10*a^32 + 7*a^62 + 10*a^92 + 7*a^122 + O(a^152))*t^2 + O(a^154)*t^3 + (2*a^4 + 10*a^64 + 2*a^124 + O(a^154))*t^4 + O(a^156)*t^5 + (5*a^6 + 2*a^96 + a^126 + O(a^156))*t^6 + O(a^158)*t^7 + (7*a^8 + 6*a^38 + 8*a^68 + 2*a^98 + 5*a^128 + O(a^158))*t^8 + O(a^160)*t^9 + (8*a^10 + 10*a^40 + a^70 + 5*a^130 + O(a^160))*t^10 + O(a^162)*t^11 + (9*a^12 + 7*a^42 + 8*a^72 + 6*a^102 + 9*a^132 + O(a^162))*t^12 + O(a^164)*t^13 + (2*a^14 + 5*a^44 + 3*a^74 + a^104 + 4*a^134 + O(a^164))*t^14 + O(a^166)*t^15 + (2*a^16 + 5*a^46 + 8*a^76 + 5*a^106 + 7*a^136 + O(a^166))*t^16 + O(a^168)*t^17 + (7*a^18 + 3*a^48 + 6*a^78 + 9*a^138 + O(a^168))*t^18 + O(a^172)*t^19 + (7*a^50 + 3*a^80 + 5*a^110 + 5*a^140 + 7*a^170 + O(a^172))*t^20 + O(a^172)*t^21 + (a^22 + a^52 + 3*a^82 + 3*a^112 + 2*a^142 + O(a^172))*t^22 + O(a^174)*t^23 + (4*a^24 + 7*a^54 + 9*a^84 + 4*a^114 + 7*a^144 + O(a^174))*t^24 + O(a^176)*t^25 + (3*a^26 + 8*a^56 + 8*a^116 + 5*a^146 + O(a^176))*t^26 + O(a^178)*t^27 + (2*a^28 + 2*a^58 + 6*a^88 + a^118 + 10*a^148 + O(a^178))*t^28 + O(a^180)*t^29 + (8*a^30 + 5*a^60 + 8*a^90 + 5*a^120 + 6*a^150 + O(a^180))*t^30 + O(a^184)*t^31 + (7*a^62 + 9*a^92 + 2*a^182 + O(a^184))*t^32 + O(a^184)*t^33 + (6*a^34 + 6*a^64 + 6*a^94 + 8*a^124 + O(a^184))*t^34 + O(a^186)*t^35 + (a^36 + 10*a^66 + 6*a^96 + 5*a^126 + 9*a^156 + O(a^186))*t^36 + O(a^188)*t^37 + (a^38 + 2*a^68 + 10*a^98 + 5*a^158 + O(a^188))*t^38 + O(a^190)*t^39 + (9*a^40 + 4*a^70 + 7*a^130 + 7*a^160 + O(a^190))*t^40 + O(a^194)*t^41 + (7*a^72 + 4*a^102 + 10*a^132 + 9*a^162 + a^192 + O(a^194))*t^42 + O(a^194)*t^43 + (4*a^44 + 5*a^74 + 4*a^104 + a^134 + 9*a^164 + O(a^194))*t^44 + O(a^196)*t^45 + (4*a^46 + 8*a^76 + 4*a^106 + 9*a^136 + 7*a^166 + O(a^196))*t^46 + O(a^198)*t^47 + (a^48 + 4*a^78 + 4*a^108 + 6*a^138 + 4*a^168 + O(a^198))*t^48 + O(a^200)*t^49 + (a^50 + 5*a^110 + 5*a^140 + 2*a^170 + O(a^200))*t^50 + O(a^202)*t^51 + (2*a^52 + a^82 + 3*a^112 + 2*a^142 + 3*a^172 + O(a^202))*t^52 + O(a^204)*t^53 + (a^54 + 7*a^84 + 10*a^114 + 5*a^144 + 6*a^174 + O(a^204))*t^54 + O(a^206)*t^55 + (7*a^56 + 8*a^86 + 7*a^116 + 7*a^146 + 4*a^176 + O(a^206))*t^56 + O(a^208)*t^57 + (a^58 + 6*a^88 + a^118 + 5*a^148 + 2*a^178 + O(a^208))*t^58 + O(a^210)*t^59 + (a^60 + 4*a^90 + 6*a^120 + 9*a^150 + 6*a^180 + O(a^210))*t^60 + O(a^212)*t^61 + (9*a^62 + 5*a^92 + 4*a^122 + 6*a^152 + a^182 + O(a^212))*t^62 + O(a^216)*t^63 + (3*a^94 + 4*a^124 + 7*a^154 + 7*a^214 + O(a^216))*t^64 + O(a^216)*t^65 + (7*a^66 + 3*a^96 + a^126 + O(a^216))*t^66 + O(a^218)*t^67 + (6*a^68 + 6*a^98 + 2*a^128 + 2*a^188 + O(a^218))*t^68 + O(a^220)*t^69 + (a^70 + 2*a^100 + 8*a^130 + 5*a^160 + a^190 + O(a^220))*t^70 + O(a^222)*t^71 + (2*a^72 + 4*a^102 + 6*a^132 + 4*a^162 + 9*a^192 + O(a^222))*t^72 + O(a^224)*t^73 + (6*a^74 + 5*a^104 + 3*a^134 + 5*a^194 + O(a^224))*t^74 + O(a^226)*t^75 + (a^76 + a^106 + 3*a^136 + a^166 + O(a^226))*t^76 + O(a^228)*t^77 + (10*a^78 + 3*a^108 + 2*a^138 + 8*a^168 + 4*a^198 + O(a^228))*t^78 + O(a^230)*t^79 + (7*a^80 + 2*a^110 + a^140 + 7*a^170 + O(a^230))*t^80 + O(a^232)*t^81 + (7*a^82 + 3*a^112 + 3*a^142 + 7*a^172 + 9*a^202 + O(a^232))*t^82 + O(a^234)*t^83 + (8*a^84 + 10*a^114 + 9*a^144 + 10*a^174 + a^204 + O(a^234))*t^84 + O(a^238)*t^85 + (2*a^116 + 4*a^146 + 5*a^176 + 5*a^206 + 5*a^236 + O(a^238))*t^86 + O(a^238)*t^87 + (10*a^88 + 9*a^118 + 2*a^178 + 2*a^208 + O(a^238))*t^88 + O(a^240)*t^89 + (7*a^90 + 8*a^120 + 3*a^150 + 4*a^180 + 2*a^210 + O(a^240))*t^90 + O(a^242)*t^91 + (4*a^92 + 10*a^122 + 9*a^152 + 7*a^182 + 6*a^212 + O(a^242))*t^92 + O(a^244)*t^93 + (3*a^94 + 3*a^124 + 7*a^154 + 8*a^184 + a^214 + O(a^244))*t^94 + O(a^246)*t^95 + (2*a^96 + 9*a^126 + 2*a^156 + 4*a^186 + a^216 + O(a^246))*t^96 + O(a^248)*t^97 + (7*a^98 + 3*a^128 + 7*a^158 + 2*a^188 + 5*a^218 + O(a^248))*t^98 + O(a^250)*t^99 + (a^100 + 5*a^160 + 6*a^220 + O(a^250))*t^100 + O(a^252)*t^101 + (10*a^102 + 10*a^132 + 8*a^162 + 9*a^192 + O(a^252))*t^102 + O(a^254)*t^103 + (10*a^104 + 10*a^134 + 6*a^164 + 6*a^194 + O(a^254))*t^104 + O(a^256)*t^105 + (2*a^106 + 4*a^136 + 10*a^166 + 7*a^196 + O(a^256))*t^106 + O(a^260)*t^107 + (4*a^138 + 6*a^168 + 4*a^198 + 2*a^228 + 9*a^258 + O(a^260))*t^108 + O(a^260)*t^109 + (6*a^110 + 9*a^140 + 2*a^170 + 3*a^200 + O(a^260))*t^110 + O(a^262)*t^111 + (10*a^112 + 8*a^142 + 6*a^202 + a^232 + O(a^262))*t^112 + O(a^264)*t^113 + (10*a^114 + 3*a^144 + 4*a^174 + 2*a^204 + 5*a^234 + O(a^264))*t^114 + O(a^266)*t^115 + (5*a^116 + 10*a^146 + 3*a^176 + 3*a^236 + O(a^266))*t^116 + O(a^268)*t^117 + (a^118 + 7*a^148 + 9*a^178 + 2*a^238 + O(a^268))*t^118 + O(a^270)*t^119 + (7*a^120 + 8*a^150 + 9*a^180 + 3*a^210 + a^240 + O(a^270))*t^120 + O(a^274)*t^121 + (10*a^152 + 6*a^182 + 8*a^212 + 6*a^242 + 4*a^272 + O(a^274))*t^122 + O(a^274)*t^123 + (8*a^124 + a^154 + 10*a^184 + 10*a^214 + 6*a^244 + O(a^274))*t^124 + O(a^276)*t^125 + (8*a^126 + 2*a^156 + 10*a^186 + 6*a^216 + O(a^276))*t^126 + O(a^278)*t^127 + (6*a^128 + 7*a^158 + 6*a^188 + 6*a^218 + 10*a^248 + O(a^278))*t^128 + O(a^282)*t^129 + (a^160 + 7*a^190 + a^220 + 3*a^250 + O(a^282))*t^130 + O(a^282)*t^131 + (3*a^132 + a^162 + 4*a^192 + 10*a^222 + 10*a^252 + O(a^282))*t^132 + O(a^284)*t^133 + (3*a^134 + 3*a^164 + 5*a^194 + 5*a^254 + O(a^284))*t^134 + O(a^286)*t^135 + (8*a^136 + 2*a^166 + 7*a^196 + 2*a^226 + 7*a^256 + O(a^286))*t^136 + O(a^288)*t^137 + (6*a^138 + 8*a^168 + 3*a^198 + a^228 + 10*a^258 + O(a^288))*t^138 + O(a^290)*t^139 + (5*a^140 + 3*a^170 + 3*a^200 + 10*a^230 + a^260 + O(a^290))*t^140 + O(a^292)*t^141 + (9*a^142 + 6*a^172 + 3*a^202 + 3*a^232 + 10*a^262 + O(a^292))*t^142 + O(a^294)*t^143 + (8*a^144 + a^174 + 9*a^204 + 8*a^234 + 7*a^264 + O(a^294))*t^144 + O(a^296)*t^145 + (9*a^146 + 10*a^206 + 7*a^236 + 10*a^266 + O(a^296))*t^146 + O(a^298)*t^147 + (9*a^148 + 5*a^208 + a^238 + a^268 + O(a^298))*t^148 + O(a^300)*t^149 + (4*a^150 + 5*a^180 + 4*a^210 + 3*a^240 + 9*a^270 + O(a^300))*t^150 + O(a^332)*t^151 + (2*a^182 + 7*a^212 + a^242 + 5*a^272 + 5*a^302 + O(a^332))*t^152
sage: yr = (a + O(a^151))*t
sage: dtr = xr.derivative() / yr
sage: integrals1 = []
sage: for f in F :
....:     f_dtr = f(xr,yr) * dtr
....:     I = sum([f_dtr[n]/(n+1) for n in xrange(f_dtr.degree())]) # \int_0^1 f dt
....:     integrals1.append(I)
....: 
FFTRep: inconsistent use
/home/jen/sage-2.10.2.alpha1/local/bin/sage-sage: line 212:  7357 Aborted                 sage-ipython -c "$SAGE_STARTUP_COMMAND;" "$`@`"
```



---

Comment by jen created at 2008-04-07 14:00:55

Changing assignee from was to roed.


---

Comment by kedlaya created at 2008-04-07 15:15:52

Here is a slightly shorter code snippet that hits the same error. If the t**32 term is removed from xr, then the error does not get hit.


```
sage: R.<x> = QQ[]
sage: K = Qp(11,10)
sage: J.<a> = K.extension(x^30-11)
sage: M.<t> = PowerSeriesRing(J)
sage: S.<x,y> = QQ[]
sage: xr = O(a^152)*t + (8*a^2 + 10*a^32 + 7*a^62 + 10*a^92 + 7*a^122 + O(a^152))*t^2 + O(a^154)*t^3 + (2*a^4 + 10*a^64 + 2*a^124 + O(a^154))*t^4 + O(a^156)*t^5 + (5*a^6 + 2*a^96 + a^126 + O(a^156))*t^6 + O(a^158)*t^7 + (7*a^8 + 6*a^38 + 8*a^68 + 2*a^98 + 5*a^128 + O(a^158))*t^8 + O(a^160)*t^9 + (8*a^10 + 10*a^40 + a^70 + 5*a^130 + O(a^160))*t^10 + O(a^162)*t^11 + (9*a^12 + 7*a^42 + 8*a^72 + 6*a^102 + 9*a^132 + O(a^162))*t^12 + O(a^164)*t^13 + (2*a^14 + 5*a^44 + 3*a^74 + a^104 + 4*a^134 + O(a^164))*t^14 + O(a^166)*t^15 + (2*a^16 + 5*a^46 + 8*a^76 + 5*a^106 + 7*a^136 + O(a^166))*t^16 + O(a^168)*t^17 + (7*a^18 + 3*a^48 + 6*a^78 + 9*a^138 + O(a^168))*t^18 + O(a^172)*t^19 + (7*a^50 + 3*a^80 + 5*a^110 + 5*a^140 + 7*a^170 + O(a^172))*t^20 + O(a^172)*t^21 + (a^22 + a^52 + 3*a^82 + 3*a^112 + 2*a^142 + O(a^172))*t^22 + O(a^174)*t^23 + (4*a^24 + 7*a^54 + 9*a^84 + 4*a^114 + 7*a^144 + O(a^174))*t^24 + O(a^176)*t^25 + (3*a^26 + 8*a^56 + 8*a^116 + 5*a^146 + O(a^176))*t^26 + O(a^178)*t^27 + (2*a^28 + 2*a^58 + 6*a^88 + a^118 + 10*a^148 + O(a^178))*t^28 + O(a^180)*t^29 + (8*a^30 + 5*a^60 + 8*a^90 + 5*a^120 + 6*a^150 + O(a^180))*t^30 + O(a^184)*t^31 + (7*a^62 + 9*a^92 + 2*a^182 + O(a^184))*t^32
sage: yr = xr^2
sage: dtr = xr.derivative() 
sage: f_dtr = yr*dtr # boom
sage: print f_dtr
```


This error seems to be reproducible, on more than one platform (sage.math, my 32-bit Ubuntu laptop, my 64-bit RHEL box).


---

Comment by wjp created at 2008-04-10 18:05:37

After discussion on IRC with David Roe on tuesday:

Apparently the NTL `ZZ_pX_Modulus` class doesn't
support re-assignment except in specific cases. (I don't understand NTL
well enough to see which cases exactly.) The reason is that the two
`FFTRep` members can't be re-assigned because their operator= can return
this 'inconsistent use' error when their `numPrimes` variables are different.

This is what seems to be causing this crash in `ZZ_pX_eis_shift` in `pow_computer_ext.pyx`.

I'm attaching a patch that solves this by not copying the ZZ_pX_Modulus objects.


---

Attachment


---

Comment by mabshoff created at 2008-04-10 21:25:14

Patch looks good to me. It fixes the crash, passes doctests on sage.math. If somebody would double check the correctness of the patch I will merge it into alpha4.

Cheers,

Michael


---

Comment by roed created at 2008-04-10 22:37:12

Replaces previous patch, changes a few more ZZ_pX_Modulus_c to ZZ_pX_Modulus_c* and added a doctest.


---

Attachment


---

Comment by mabshoff created at 2008-04-10 22:45:05

Merged padics_ZZ_pXModulus2.patch in Sage 3.0.alpha4


---

Comment by mabshoff created at 2008-04-10 22:45:05

Resolution: fixed


---

Attachment

Should be used instead of compile_fix.


---

Attachment

Merged padics_ZZ_pXModulus_fix.patch in Sage 3.0.alpha4
