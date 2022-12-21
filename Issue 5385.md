# Issue 5385: Sage 3.3: GAP 4.4.12 experiences strange startup problem on some Linux systems

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-02-26 13:53:26

Assignee: mabshoff

As reported in http://groups.google.com/group/sage-support/browse_thread/thread/9f6349d362f0dd64:

I've tried to build from sources sage-3.3 but I still have an 
unexpected error when running sage :-( 

The log is available here: http://www.lri.fr/~oudinet

  /pub/debiansage2.log 

I add that when I manually try to execute the command gap with the 
same options, I get : 

```
$ gap -r -b -p -T -o 9999G /usr/local/sage-3.3/data//extcode/gap/sage.g 
`@`p1.`@`!19924+`@`"2014+`@`#91395+`@`$7138+`@`%24361+`@`&67542+`@`!24824+
`@`"7764+`@`#33736+`@`$5915+`@`%21601+`@`&67542+`@`!48921+`@`"9581+`@`#09404+
`@`$3263+`@`%5248+`@`&67542+`@`!2688+`@`"6321+`@`#95313+`@`$0292+`@`%0796+
`@`&67542+`@`!3448+`@`"5201+`@`#54952+`@`$8622+`@`%2475+`@`&67542+`@`!7689+
`@`"949+`@`#89662+`@`$9281+`@`%2454+`@`&67542+`@`!3448+`@`"1101+`@`#75312+
`@`$7761 +`@`%4233+`@`&67542+`@`nGAP4, 
Version: 4.4.12 of 17-Dec-2008, 
x86_64-unknown-linux-gnu-gcc`@`J`@`!0012+`@`"385+`@`#0944+`@`$144+`@`%6262+`@`&67542+`@`nga p> 
`@`i 
```


Cheers,

Michael


---

Comment by mabshoff created at 2009-04-19 02:07:11

wontfix due to the GAP downgrade at #5697.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-19 02:07:11

Resolution: wontfix
