# Issue 4046: add support for Google's new browser to the notebook

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-09-03 15:50:53

Assignee: boothby

It renders fine (rendering is done by WebKit) but the keyboard input doesn't work completely (since it is a new JS engine I suppose).


---

Comment by malb created at 2008-09-03 15:51:22

Here's what I could get out of 

http://sage.math.washington.edu/home/boothby/modular.old/www/keys_capture.html

As you can see, the good keys aren't recognized at all.

key_shift = "16,16!"
key_ctrl = "17,17"
key_alt = "18,18"
key_home = 
key_end = 
key_pgup = 
key_pgdn = 
key_bkspc = 
key_spc = "32,32"
key_enter = "13,13"
key_tab = 
key_q = "113,113"
key_w = "119,119"
key_e = "101,101"
key_r = "114,114"
key_t = "116,116"
key_y = "121,121"
key_u = "117,117"
key_i = "105,105"
key_o = "111,111"
key_p = "112,112"
key_Qu = "81,81!"
key_Wu = "87,87!"
key_Eu = "69,69!"
key_Ru = "82,82!"
key_Tu = "84,84!"
key_Yu = "89,89!"
key_Uu = "85,85!"
key_Iu = "73,73!"
key_Ou = "79,79!"
key_Pu = "80,80!"
key_a = "97,97"
key_s = "115,115"
key_d = "100,100"
key_f = "102,102"
key_g = "103,103"
key_h = "104,104"
key_j = "106,106"
key_k = "107,107"
key_l = "108,108"
key_Au = "65,65!"
key_Su = "83,83!"
key_Du = "68,68!"
key_Fu = "70,70!"
key_Gu = "71,71!"
key_Hu = "72,72!"
key_Ju = "74,74!"
key_Ku = "75,75!"
key_Lu = "76,76!"
key_z = "122,122"
key_x = "120,120"
key_c = "99,99"
key_v = "118,118"
key_b = "98,98"
key_n = "110,110"
key_m = "109,109"
key_Zu = "90,90!"
key_Xu = "88,88!"
key_Cu = "67,67!"
key_Vu = "86,86!"
key_Bu = "66,66!"
key_Nu = "78,78!"
key_Mu = "77,77!"
key_1 = "49,49"
key_2 = "50,50"
key_3 = "51,51"
key_4 = "52,52"
key_5 = "53,53"
key_6 = "54,54"
key_7 = "55,55"
key_8 = "56,56"
key_9 = "57,57"
key_0 = "48,48"
key_bang = "33,33!"
key_at = "64,64!"
key_hash = "35,35!"
key_dollar = "36,36!"
key_mod = "37,37!"
key_caret = "94,94!"
key_amp = "38,38!"
key_ast = "42,42!"
key_lpar = "40,40!"
key_rpar = "41,41!"
key_minus = "45,45"
key_under = "95,95!"
key_plus = "43,43!"
key_eq = "61,61"
key_lbrace = "123,123!"
key_rbrace = "125,125!"
key_lbrack = "91,91"
key_rbrack = "93,93"
key_pipe = "124,124!"
key_slash = "92,92"
key_colon = "58,58!"
key_semi = "59,59"
key_quote = "34,34!"
key_apos = "39,39"
key_bslash = "47,47"
key_quest = "63,63!"
key_comma = "44,44"
key_dot = "46,46"
key_tilde = "126,126!"
key_tick = "96,96"
key_lt = "60,60!"
key_gt = "62,62!"
key_left = 
key_up = 
key_right = 
key_down =


---

Comment by mhansen created at 2008-09-04 03:29:53

From ddrake:

```
When using the notebook with Google Chrome, tab completion does not seem to work; when one hits tab, you just get an orange box around the "evaluate" link. It seems to be using tab in the usual way (to move from one input box to another, etc) instead of doing the completion.

Of course, Chrome is so new that this may very well be a bug on their part, but it's worth investigating. 
```



---

Comment by schilly created at 2008-09-05 08:41:17

I found something related in their issue tracker

[Issue 1355: Arrow keys do not work in Street View popup window from Google Maps](http://code.google.com/p/chromium/issues/detail?id=1355)

i think, let them first get google maps right ;)


---

Comment by mpatel created at 2009-08-14 04:49:28

Keyboard support for Chrome 2 & Safari 4 on Windows and Chromium 3 on Linux.


---

Attachment

Modified keys_capture.html that formats key information for keyboard.py.


---

Comment by mpatel created at 2009-08-14 05:00:49

`keys_capture_v2.html` can capture key information and output it in `keyboard.py`'s format.

According to its output, Chrome 2 and Safari 4 on Windows XP have the same key codes.  The same codes, except for `KEY_SHIFT`, work for Chromium 3 on Linux.

Note: There's still a serious stylesheet gzip-encoding problem with Chrome 2 on Windows, but that should be a separate ticket.


---

Comment by timdumol created at 2009-09-22 16:55:39

Merges fine, and Chromium detects keys properly now.


---

Comment by mvngu created at 2009-09-24 05:37:36

What should be merged and in what order?


---

Comment by mpatel created at 2009-09-24 18:41:56

Replying to [comment:6 mvngu]:
> What should be merged and in what order?
Just [attachment:trac_4046-chrome_and_friends.patch].  The key capture utility _might_ be useful in the future, but it'll be available here.  If/when we switch to using [jQuery Hotkeys](http://code.google.com/p/js-hotkeys/) in the notebook, the patch may become obsolete, too.


---

Comment by mvngu created at 2009-09-25 08:43:51

Resolution: fixed


---

Comment by mvngu created at 2009-09-27 10:34:17

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
