# Issue 7254: sagenb notebook: automatic worksheet refreshing and synchronization

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-10-20 07:01:14

Assignee: boothby

If two users open the same worksheet, one changing it should appear to the other.  If the same person opens the same worksheet in multiple tabs or browser, changing one should update all views.  Finally, hitting the back button after viewing a worksheet (to get back to it) shouldn't result in massive corruption.  This relatively simple patch solves these problems in a very simple and direct manner.  


---

Attachment


---

Comment by was created at 2009-10-20 07:02:22

Changing status from new to needs_review.


---

Comment by schilly created at 2009-10-20 10:41:29

awesome enhancement! i'm just wondering what happens, if there is a network problem or if a request takes too long. suspend the 2secs request loop, make it a bit longer and then shorter again? well, i think this should go in and we should test it on alpha.sagenb.org to see how it works, for further tuning if necessary...


---

Comment by boothby created at 2009-10-20 16:17:59

I'll review this on the afternoon of Oct 21 if nobody has gotten to it.


---

Comment by boothby created at 2009-10-20 16:21:51

Actually, quick note:

Something seems off with the documentation in this one: there's no 'publish' argument and only do 'do_print' argument is mentioned.

```
	2354	        return cells_html 
 	2355	                        
 	2356	    def html(self, include_title=True, do_print=False, 
 	2357	             confirm_before_leave=False, read_only=False): 
 	2358	        r""" 
 	2359	        INPUT: 
 	2360	         
 	2361	        - publish - a boolean stating whether the worksheet is published 
 	2362	         
 	2363	        - do_print - a boolean 
 	2364	 
 	2365	        OUTPUT: 
 	2366	         
 	2367	        - string -- the HTML for the worksheet 
```



---

Comment by was created at 2009-10-20 17:36:24

> Actually, quick note:

> Something seems off with the documentation in this one: there's no 'publish' argument > and only do 'do_print' argument is mentioned. 

True, but that really has little to do with my patch, since the docs were like that in sage-4.1.1.

Harald:
> awesome enhancement! i'm just wondering what happens, if there is a 
> network problem or if a request takes too long. suspend the 2secs 
> request loop, make it a bit longer and then shorter again?

Good question.  I think what will happen is that if you do something, say insert a cell, evaluate a cell, change a cell, and that entire transaction gets dropped, then a refresh will end up being forced.  You will (1) loose that change, and (2) see that it didn't take.  This is probably much better than thinking that you made that change but actually not making it.   

There may be some other subtle issues I'm missing.  

I should post this to alpha.sagenb.org today for further testing (not done yet).


---

Comment by schilly created at 2009-10-21 16:26:55

Replying to [comment:5 was]:
> Good question.  I think what will happen is that if you do something, say insert a cell, evaluate a cell, change a cell, and that entire transaction gets dropped, then a refresh will end up being forced.  You will (1) loose that change, and (2) see that it didn't take.  This is probably much better than thinking that you made that change but actually not making it. 

Well, that could also happen, probably. What I was thinking about is a flaky connection (or one, where a roundtrip takes longer than 2 secs). Then, the async request is still open, but already some others waiting to get dispatched. The number of requests is limited (FF 6, IE 8 in dial up mode only 2, older browsers also only 2) and therefore all the new requests timeout eventhough the network might be ok. What i propose is a boolean request_state_flag that is set to true when the request is made and set to false, when the async callback 'refresh_cell_list_callback' is in success or in timeout/fail. Then, the request should only be made if the flag is false and it never happens that many simultaneous requests jam the network.

I just don't know all the details and what's already done by the async requests, so that's just a very rough description what i'm thinking about.

Reverting valid new content to an older version just because of bad timing with the server might be another issue. Updates from the client to the server must have higher priority.


---

Comment by mpatel created at 2009-10-23 20:02:53

Can we revert this patch for now (i.e., 4.2)?  I'll try to take a closer look soon, but it's not formally reviewed.  Though it's not difficult to disable in `notebook_lib.js`, it has made working on and debugging other patches somewhat difficult.  What if we had two sagenb repos:

 * A cutting-edge alpha with any changes allowed, running at `ouch.sagenb.org`.  This could just be W. Stein's development branch. 
 * A release-manager's instantaneous alpha with only reviewed changes allowed, running at `alpha.sagenb.org`.

?  Just some thoughts.


---

Comment by mpatel created at 2009-10-24 20:54:01

Replying to [comment:7 mpatel]:
> Can we revert this patch for now (i.e., 4.2)?  I'll try to take a closer look soon, but it's not formally reviewed.
So I should just review it...


---

Comment by mpatel created at 2009-10-24 23:52:01

Below is an example, I think, of Harald's race condition, with a local server.  I instrumented the indicated functions in `notebook_lib.js`.  The last number on each line is my Firefox 3.5.3 tab's `state_number` when "I" call `console.log()`.

```
worksheet_command: alive NOCHANGE 161            # I'm sending an 'alive' command and not increasing my state_number.
server_ping_while_alive_callback: NOREFRESH 161  # The response matches my state_number, so I'm not refreshing.
worksheet_command: eval INCREASED 162            # I 'eval'ed (shift-enter) an auto-updating interact cell with a color control, so I increased my state_number.
worksheet_command: cell_update NOCHANGE 162
worksheet_command: eval INCREASED 163
worksheet_command: cell_update NOCHANGE 163
worksheet_command: cell_update NOCHANGE 163
worksheet_command: cell_update NOCHANGE 163
worksheet_command: cell_update NOCHANGE 163
worksheet_command: alive NOCHANGE 163
server_ping_while_alive_callback: NOREFRESH 163
worksheet_command: eval INCREASED 164            # I begin dragging non-stop to change the color.  I increase my state_number with each 'eval'.
worksheet_command: eval INCREASED 165
[...]
worksheet_command: eval INCREASED 194
worksheet_command: alive NOCHANGE 194            # I remember the state at my last outgoing ping.
worksheet_command: cell_update NOCHANGE 194
worksheet_command: eval INCREASED 195
worksheet_command: eval INCREASED 196
worksheet_command: eval INCREASED 197
server_ping_while_alive_callback: REFRESHING requ= 194 resp= 194 197  # My last ping went out 194 and the response is 194.  But I'm now at 197, so I'm refreshing...
worksheet_command: cell_list NOCHANGE 197        # I request the cell list.
worksheet_command: eval INCREASED 198            # Still 'eval'ing.
worksheet_command: eval INCREASED 199
worksheet_command: eval INCREASED 200
worksheet_command: cell_update NOCHANGE 197
worksheet_command: eval INCREASED 198
worksheet_command: eval INCREASED 199
worksheet_command: eval INCREASED 200
worksheet_command: alive NOCHANGE -1
worksheet_command: cell_update NOCHANGE 200
server_ping_while_alive_callback: REFRESHING requ= -1 resp= 205 200
worksheet_command: cell_list NOCHANGE 200
container is undefined
[Break on this error] return container.farbtastic || (contai...uery._farbtastic(container, callback));\nfarbtastic.js (line 27)
F is undefined
[Break on this error] (function(){var l=this,g,y=l.jQuery,p=l....each(function(){o.dequeue(this,E)})}});\njquery-1....2.min.js (line 12)
worksheet_command: eval INCREASED 201
worksheet_command: cell_update NOCHANGE 201
worksheet_command: alive NOCHANGE -1
worksheet_command: cell_update NOCHANGE 206
server_ping_while_alive_callback: NOREFRESH 206
container is undefined
[Break on this error] return container.farbtastic || (contai...uery._farbtastic(container, callback));\nfarbtastic.js (line 27)
F is undefined
[Break on this error] (function(){var l=this,g,y=l.jQuery,p=l....each(function(){o.dequeue(this,E)})}});\njquery-1....2.min.js (line 12)
worksheet_command: eval INCREASED 207
worksheet_command: cell_update NOCHANGE 207
worksheet_command: cell_update NOCHANGE 207
worksheet_command: cell_update NOCHANGE 207
worksheet_command: cell_update NOCHANGE 207
worksheet_command: alive NOCHANGE 207           # I suspended the server around here.
worksheet_command: alive NOCHANGE 207
```



---

Comment by mpatel created at 2009-10-24 23:59:29

What if we change the refresh condition in `server_ping_while_alive_callback` to

```js
        if(state_number >= 0 && parseInt(response_text) > state_number) {
```

?  We can also save a worksheet's `state_number` with the worksheet and ensure it never decreases on the server, even across re-opens, reloads, restarts, etc.  Then, any browser whose state is smaller than the server's should refresh.


---

Comment by mpatel created at 2009-10-25 00:27:05

Changing status from needs_review to needs_work.


---

Comment by mpatel created at 2009-10-25 00:27:05

Also:

 * It's probably safer to use `parseInt` and to use `===` and `!==`, instead of `==` and `!=`, to avoid JS's implicit conversions (cf. [JSLint's](http://www.jslint.com/) "The Good Parts" setting).  Although I'm not sure how it happened, I saw the successive state "numbers" 480, 4801, 48011, etc.
 * The browser and server do not update their `state_number`s if a new cell is added at the end of a sheet, when text cells are added, or cells are deleted.  Should we add these to the list, along with the `'delete_all_output'`, `'pretty_print'`, `'system'` worksheet commands?

If these changes are worthwhile, I can make a patch, but I'm not sure how/where to store the worksheet's state (or "revision") number.


---

Comment by was created at 2009-10-25 01:49:22

> If these changes are worthwhile, I can make a patch

I've made those changes and pushed the results:

```
flat:sagenb wstein$ hg diff
diff -r 5f1705b928fc sagenb/data/sage/js/notebook_lib.js
--- a/sagenb/data/sage/js/notebook_lib.js	Fri Oct 23 18:06:28 2009 -0700
+++ b/sagenb/data/sage/js/notebook_lib.js	Sat Oct 24 18:48:46 2009 -0700
`@``@` -554,7 +554,7 `@``@`
     var X, y, z, s;
     if (status == 'success') {
          X = response_text.split(SEP);
-         state_number = X[0];
+        state_number = parseInt(X[0]);
          /* Now we replace the HTML for every cell *except* the active cell
             by the contents of X[1]. */
        //   y = get_element("worksheet_cell_list");
`@``@` -1678,7 +1678,7 `@``@`
         server_down();
     } else {
         server_up();
-        if(state_number >= 0 && response_text != state_number) {
+        if(state_number >= 0 && parseInt(response_text) > state_number) {
              /* force a refresh of just the cells in the body */
 	    refresh_cell_list();
         }
`@``@` -2570,7 +2570,7 `@``@`
         a string
     */
     if (cmd == 'eval' || cmd == 'new_cell_before') {
-        state_number += 1;
+        state_number = parseInt(state_number) + 1;
     }
     return ('/home/' + worksheet_filename + '/' + cmd);
 }
```



---

Comment by was created at 2009-10-25 01:49:22

Changing status from needs_work to needs_review.


---

Comment by mpatel created at 2009-10-25 02:18:54

Changing status from needs_review to positive_review.


---

Comment by jason created at 2009-10-31 19:02:26

For some reason, I thought this was already working on sagenb.org.  Is this already in the Sage 4.2?  Is sagenb.org running more current version of sagenb than is it 4.2?  Or am I just confused?


---

Comment by mpatel created at 2009-11-01 01:04:29

Unless I'm wrong, only the [attachment:trac_7254.patch attached patch] and the changes in [comment:13 comment 13] were merged into [an ancestor of] sagenb 0.4 (and Sage 4.2).  Moreover, sagenb 0.4 is exactly the notebook version running on sagenb.org.

I think we should close this ticket.


---

Comment by was created at 2009-11-11 19:47:15

this was merged into sagenb-0.4


---

Comment by was created at 2009-11-11 19:47:15

Resolution: fixed
