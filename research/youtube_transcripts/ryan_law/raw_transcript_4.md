So Ryan, I was thinking today, uh, it didn't take us too long to go from this

0:05
AI thing cannot really do great content to, oh my god, this is amazing, right?

0:11
And here we are. Uh, you have devised an AI content automation workflow that you

0:18
use to actually publish quite a few articles on HF's blog already. And these are good articles. These are great

0:24
articles. And yeah, full disclosure, I haven't seen it yet, so I'll be checking

0:29
it out live together with uh anyone watching it, and I'm excited. Yeah. Do

0:34
you want to say a few quick words on what people are about to see? Yeah. Well, exactly that. So, we've obviously

0:41
been tinkering with using AI in our content workflows for years at this point, and it's always been very

0:47
effortful. It can be helpful, but you have to sink a ton of time and energy into it. There's still a lot of manual stuff that has to happen. I kind of feel

0:54
like that's not the case anymore. Uh it's a bit spooky actually. I think since Claude code is probably the big

1:00
thing that has changed this this kind of agentic workflow where Claude can make some decisions on your behalf and you

1:06
can provide it with some guard rails to actually make it do things in a certain way. Um so we've basically yeah built I

1:13
call it the blog pipeline. Uh and it is a kind of content automation system for new articles and for content updates. Uh

1:21
we've done maybe like 30 article updates with it so far. Um published maybe uh 10

1:28
15 articles. Got maybe something similar in progress at the moment. Um yeah, it's been pretty cool.

1:35
Let's review it. Show it to me. Yeah, let's do it. Um so obviously two things on the screen right now. We have

Inside Ryan's 23-skill AI content automation system
1:41
a terminal and we have Claude code running in that terminal. So that is just a folder that I've called blog

1:47
pipeline and claude code is living in that folder and it will do stuff in that folder for me when I ask it to. Um and

1:54
we've got VS Code over here. This is just a really good way of showing you the contents of that folder in a way that is a bit easier to understand. Uh

2:02
these are all the folders on the left hand side and they've all got files inside them. And I of course I asked

2:08
Claude I said I'm going to present this process on a podcast with Tim. give me some notes and visualizations to help

2:14
explain this. So, it added a handy little podcast folder here uh that has some notes and visualizations to make

2:21
this a bit more interesting. But the basic premise is uh we have

2:27
basically set it up such that there are maybe 23 or so uh skill files in here.

2:33
You can see them in this folder. Uh and skill 23 skill files. That's that's a lot.

2:39
That is a lot. Um, and each of these skill files is basically a process. It is a process that at some point during

2:46
creating content or updating content as a human, we generally do something like this or very similar to this. Um, and

2:53
this is just a markdown document with very you lost me already. I I kind of

2:59
know what skills are, but you lost me already. Let's start from the beginning. Where does the process start? What do we

3:04
start from? Do we start from a keyword? Do we start from an idea? What's the first step with this? Yes. Uh so what you can do is so this is

3:12
a keyword ideas CSV. Um it's obviously a bit hard to see in this format but

3:18
basically we've even set up a a process right now where we can use the HF's MCP

3:24
which is obviously a way for Claude and other LLMs to access HF's data and it will run a content gap analysis for us

3:31
and I've then set up another process where it will review this list of keywords and prioritize them. Uh it

3:37
looks Ryan, again, let me uh use my Eastern European politeness uh to bring you

3:43
right to the point. We're not talking about keyword research. We're talking about creating content. So, let's say we have a keyword or a topic. Uh what do we

3:50
do with it? We're not we're not talking about keyword research. We want to create content. Let me show you that. Uh

3:55
let me clear this.

4:01
Uh so, I can trigger blog pipeline. And I can put in a keyword like keyword opportunities.

4:08
And if I want, I can add some context to it and explain, you know, if there are points I want to add, I can add that.

4:15
And off claude goes. And probably somewhere from between 8 to 11 minutes from now, it will have a draft ready for

4:22
review. Um, it goes through, yeah, about 12 steps at this point, as you can see.

4:29
Oh, wow. It's actually It's actually telling me we've already It's so clever. it's not letting me do the same one that we've

4:35
already done before. Um, so there's a research step, there's a reference step

4:40
where it looks at existing articles on the HF's blog. There's an outlining step where it turns that into a structured

4:46
outline. There's a like product annotation stage where we look for opportunities to mention specific HS

4:53
products. There is a drafting phase, a citation phase for internal linking and

4:58
finding supporting sources. There's a screenshot phase, which doesn't work very well, but we're working on that.

5:04
Uh, a preview phase where you can actually preview how it would look on the blog. Uh, and then a formatting for

5:10
publish phase where it will add in all the WordPress short codes, all the kind of stuff we need. Um so basically when

5:18
you when you ask it to create uh a piece of content around a given keyword you

5:24
are essentially uh launching a skill which is a combination of steps where

5:31
each step is uh a separate skill and basically it has to finish them one by

5:37
one or how does it work exactly that? Yeah. So what you can

5:42
either trigger the skills individually. So if you just want an outline, you can just ask for an outline by triggering that skill. But I've created these kind

5:49
of master skills and they are very simple. They exist just to tell Claude to work through the other skills in a

5:55
particular order. Um so this one's called blog pipeline and there's also update pipeline. Uh and they literally

6:01
yeah just stitch them together and make Claude systematically work through these processes. Okay. Uh let me go straight

6:09
into the uh phase of being critical of

6:14
this. Uh how is this not a slope? So what makes this process produce good

6:20
content and not some generic stuff? Yeah. So that's a very good question. I

6:27
think this definitely works best for one thing on topics that we have already covered in some capacity on the HF's

6:34
blog. Um, so one we published recently, content gap. We have never written an

6:40
article about content gap spec or is it keyword gap? One of these two, content decay and keyword gap. We've written

6:46
loads about these concepts generally, but in slightly different contexts, but we've never specifically targeted that

6:52
keyword. But because this uh is able to go and look up existing HF's articles

6:57
and anchor the content generation process in what we've already written, uh that goes a long way to getting rid

7:04
of a lot of the problems you'd have. Um and there are also some topics I think

7:09
I'm mainly using this for very straightforwardformational topics, things that the LLMs know a lot about.

7:15
Um there are opportunities for you to provide some context in it. Uh there's a particular step in here that looks for

7:22
um opportunities to add information gain. So it actually reads the top ranking articles, summarizes the

7:28
contents of them and make suggestions for ideas that are not covered but would be useful for the reader to understand

7:34
within this. And I think AI is better at research than a person is as well. Um it can be

7:40
faster and more systematic about it. It can go out and look up uh you know the latest research articles, the latest

7:46
stats, all these kinds of things. Okay. So, we definitely cannot go through uh
The research phase: analyzing competitor content and finding gaps

7:51
all of your skills uh in the course of this podcast episode because there is a lot of uh a lot of content in each of

7:58
the skills. But I want you to uh start from the very first step of creating

8:04
content and then go to the second and third and highlight maybe one or two

8:10
kind of counterintuitive things. So, for example, what what might people get wrong if they would want to kind of

8:16
recreate your process? Because uh I'm not sure that we want to just uh give out your process to everyone else if we

8:22
want just like open source it and have everyone else have access to the same process. And I would imagine that people

8:28
would want to uh make it uh personal to to them and their voice and their blog

8:34
and the style of content that they want. But yeah, walk me through each step and tell me if you uncovered

8:42
anything interesting about uh giving instructions to AI on how to

8:49
kind of improve the output of this specific step if you know what I mean. Yeah. Yeah. Yeah. So you made a very

8:55
good point there as well. I think the way we are using this is not as though this is the universal process that

9:01
everyone the team has to follow. Um, we've actually set it up such that the team can fork their own versions of this

9:07
repo. So, they can make their own version of this folder and they can modify it how they like. This version

9:14
has examples of content that I like and my writing voice uh and it's used as part of the article generation process.

9:20
It would be super weird if SQ or Louise uh did the same thing, used my writing voice for their articles. So, it's very

9:27
easy to actually update it and personalize it. And part of that might be changing the steps it goes through your own personal preferences. Um, this

9:34
is kind of very unique to me, I think, and that's kind of I think how this should be used. Um, another good point

9:41
as well, you said you were surprised at how many steps there were in this process. I think that is actually a very

9:46
very good thing. Um, the more steps you create, the more kind of introspection

9:53
you have into the process, the better you understand it. uh the more opportunities you have to actually control and personalize how the content

9:59
turns out. So one very important thing I learned very quickly obviously I could

10:05
just set this process in motion and it would give me an article in 8 minutes and either it's good or it's bad. It's

10:11
quite hard to work out how to fix and improve the process if you do that. So actually at every single step of the

10:17
process um you can actually see it it will give me an output at every stage.

10:23
So if something goes wrong, if I don't like the article or how it turned out, I can go back and see which part of the

10:28
process it didn't work very well. I'm actually surprised that when you

10:33
initially tried to launch this process, you said that you would wait like 8 to 12 minutes because I was expecting that

10:40
you would actually babysit it from step to step. So you would see the output of

10:45
the first step, see if you want to refine it, if if it's according to your expectations, and then allow it to go to
10:52

the second step. But it's all just batched for you. And the thing is that that's actually an interesting tip. This

10:58
is exactly what I was looking for, some tips for people of uh what they need to look for when they're building this

11:04
themselves. And the tip is make sure that the process saves the output of the

11:09
step. So if you don't like the final thing, you can go step by step and review at which step kind of it went

11:17
sideways so that you could uh like give it more instructions or refine the the skill that that refers to the step uh

11:24
and make it uh do over again and see if that would help. But yeah, I'm surprised that uh you let it run for like 8 to 12

11:32
minutes. Is this the point that you trust it well enough? you like your steps or Yeah, probably it's that I I

11:40
don't see any other reason why would you would just let it cook for so long and follow all the steps. Yeah, great point.

11:46
Very importantly, this is uh actually months and months of refinement has gone

11:51
into this thinking and the process in here and actually the last podcast episode we talked about where we had the

11:56
custom GPTs, it was like the kind of baby version of this process. So a lot of the skills I have in here are things

12:03
that we improved and refined and did handhold and babysit as part of that process. So we'd already written these,

12:09
already tested these, already made dozens and dozens of article outputs with them and kind of learned to refine them. So the thing that Claude does very

12:17
well is just stitching those together. Um actually automating that process.

12:22
Okay, let's go step by step. The first step I think I see it though it is quite small is research, right? any like one

12:28
or two tips to that you saw that would significantly improve the output of this

12:34
step. So it does a combination of things. Maybe most people would assume you know keyword research is the most important

12:40
thing to do and we have that in here. It goes and gets a bunch of HF's data from the MCP uh related keywords parent topic

12:47
all this kind of thing. We don't have this yet but I've asked for it. What is more important I think

12:54
is going and looking at the existing SER the content that is ranking and analyzing that and seeing the topics

13:00
that are kind of consensus and commonly used there opportunities to differentiate from that um that is what

13:07
AI content helper is perfect for doing but we don't have the endpoint for that yet so this does a kind of laborious

13:13
manual version of that but what is ex what is exactly like what are you asking it to do do you ask it like open the top

13:20
ranking articles for this keyword and what and and read them and summarize

13:26
them. What do what do I ask it to do? Like give me something interesting about the research step. Yeah, let me try and

13:32
find it. Here we go. This is the skill file.

13:37
Um so it starts with keyword ideas. It gets uh primary keyword metrics and

13:44
parent topic. Uh it finds longtail keyword variations that share the same parent topic.

13:50
Uh there's some prioritization where it groups them together and discards ones that wouldn't fit the right intent.

13:56
Pulls the questions report through the MCP as well. So we get commonly asked questions that people might have related

14:01
to this topic. Groups them into question themes. So we're not just doing like FAQ spam.

14:07
Uh we get the SER overview. We use that to go and look at the type of content that is ranking, the estimated traffic,

14:13
all these kinds of things. Uh analyze the dominant search intent of the SER results. So we can see what type of

14:19
content performs best. That's kind of going into this process. Uh and then it looks at the actual top ranking pages.

14:25
So it uses web fetch. It retrieves the content. It extracts the headers. It summarizes them. It looks for themes and

14:32
gaps in them. And yeah, creates content gaps and opportunities.

14:38
Um and you can see an example of the kind of output. So it basically creates a report like a research report at this

14:43
step. I don't have to see this, but this is what gets fed into Claude at the next stage of the process. Uh, so you got

14:49
loads of keyword data, questions to answer, organic results. Uh, you know what? At this point, as I'm looking at

14:56
how detailed and sophisticated these steps are, I want to say the word

15:03
overengineered. M I'm actually wondering if you would like remove half of that, would it just do as

15:10
good of a job? Yeah, quite possibly. And that is another really important part of this

15:16
process. Um I'm always surprised at how good increasingly the most like uh

15:21
frontier most up-to-date models actually are on their own without any input. Um

15:27
so a big part of the testing and iteration we've been doing is to we've actually been writing um like test

15:33
cases. We've been following this these steps with the skill file and without it

15:39
and seeing whether the without version is actually good enough. Does the skill file actually add any benefit to it? Um

15:46
a good number of cases the models do a very good job on its own and it just needs a little nudging in a particular

15:52
direction. So, I expect as we continue to improve on these, these skill files and these outputs will just get simpler

15:58
and simpler over time until they're distilled down to the handful of things that are very important for getting the

16:03
output that we want cuz yeah, it's probably completely overengineered at this point, I think. But again, my brain

16:10
wants some kind of structure to what we're trying to do. So the the structure

16:16
I would uh so if I were building this process myself from scratch and they needed to start from research of

16:22
competitors and I know that my competitors are the pages that are ranking uh at the top. Uh what I would

16:29
tell uh AI or Claude specifically to do I would tell it to download all the

16:34
content uh in the folder. uh and then yeah I would I would ask it to extract

16:40
from each piece of content kind of the main themes and the main ideas and then I would ask it to cross reference those

16:47
main themes and the main ideas between the articles and create me one master document with all of the kind of ideas

16:56
stories interesting points uh from all of the content so my my output uh I I

17:03
don't necessarily need like you had the people also ask questions and that stuff. I would just ask it to uh analyze

17:09
articles and create kind of a blended master file with everything unique that

17:15
is pulled from all the articles. Actually, I do a similar process right now when I when I prepare for podcast

17:20
interviews uh with uh marketing leaders. What I do is I do a pretty similar thing. Uh I give Claude uh their

17:29
previous interviews, links to their previous interviews on YouTube. It downloads the transcript and then it

17:35
creates me for each of these transcripts because I don't want to read the whole thing. I want TLDDR too long didn't

17:40
read. So I ask it extract the questions because questions are topics within the interview and then differentiate between

17:47
uh main questions and follow-up questions where the host is digging uh more into this topic. So, uh, yeah, you

17:54
know, like where the main question, where the follow-up question, and then instead of giving me the whole answer,

17:59
uh, give me TLDDR, just a few sentences of what the guest replied, give me if

18:04
there was any hot take, give me if there was any story, give give me if there was any specific number like, oh, we

18:10
increased our leads by 300% or something. Uh, and I think there was

18:15
something else, but I forgot about it. So, it creates me TLDDR for each of the interviews. And as the next step I ask

18:22
it now create me a master TLDDR and this is what I would read uh while preparing

18:29
for for the podcast interview because it would give me all the unique information from like a dozen interviews. So it

18:36
feels that uh when I want to create a piece of content it's kind of the same. I want to know what has been said

18:43
already by uh on this topic. So this is what I would include in the research phase. But uh yeah, you're giving it uh

18:51
people also ask questions, parent topics, but it it feels that when you say that you're extracting kind of

18:56
topics from a page, it feels the same what I'm doing when I'm extracting questions that a host asked uh my guest

19:02
and then I do do you also ask it to create a master document with everything?

19:08
Uh that is yeah basically that research document is the kind of um uh this is

19:14
the research document it would hand over to the next step of the process. Okay. Uh we discussed research. What is

Referencing existing content to maintain consistency
19:20
the next step? So the next step uh uh HF's references.

19:28
So how how does it work? So this was I actually added this very recently and this has been very helpful. Um

19:36
Claude can do a good job writing an article on most topics. It can go and look up other content. That's all well and good. Um, I really wanted a part of

19:43
the process where, you know, as a human writer, I would go and see what we already have on a topic because I want

19:48
to make sure a new article is consistent with old things we've written. I want to interlink between them. Uh, I want to

19:54
make sure the kind of framing is useful. I want to be efficient and make sure I'm not repeating myself. I can just pluck

20:00
elements from existing articles. So this specifically looks up the target keyword to see what we have already published on

20:06
that topic, what is already ranking for similar topics and it incorporates elements of that into the uh like

20:14
outlining and generation process. Okay, it feels like it feels again I

20:21
will try to uh explain it from my perspective. Uh I will try to kind of

20:26
simplify the process. So it feels the same as research as the first step where

20:31
you take the pages where you extract kind of unique information from them and you want to understand kind of the the

20:37
overall topic coverage uh as pulled from like a dozen different pages and now

20:43
what you're doing you're referencing our own content. So rather than searching which are the top 10 ranking pages for

20:49
the topic, you're going and searching okay what relevant pages does hrefs does

20:55
our website already have on this topic and can we pull something interesting from them and again cross reference with

21:02
my master document if we're saying something unique uh that this master

21:07
document is not saying and what's what's important is because our content is very productled and we try to fill our

21:13
content with use cases of our tools and data often times the unique bits that uh

21:20
AI can pull from our content on this topic are those use cases and you can even specifically instruct it so you can

21:26
tell cloud so specifically look for whenever we're discussing this topic how are we uh teaching people to use our

21:33
tools what kind of actionable use cases we're teaching them uh and then it would create you another document with like

21:39
okay this is the master document of what all competitors are talking about this topic and these are unique unique

21:45
insights that I saw published on your blog and here are unique I don't know use cases uh of your product that I saw

21:52
in your articles uh on this topic. So is this more or less what you're looking for? Yeah, exactly that. And this step

22:00
is quite simple as well. It's basically I wanted to provide a almost like a list of modules or sections that could be

22:08
relevant to this topic that we have already covered so that when it comes to outlining and drafting Claude can go and

22:14
look up these examples, incorporate those headers, uh link back to them as an internal linking step just make it

22:20
kind of an integrated part of how we create content. Okay. And then we have next step.

Creating exhaustive outlines using the MECE principle
22:26
Yeah. And then onto the outlining phase. Um, so let's have a look see if I can find the skill for this one.

22:33
So these are this is very similar to what we had in the uh custom GPTs. This is kind of the editorial process that

22:40
when a writer puts together an outline, this is how I expect them to do it. Um,

22:45
so it's got some very simple core concepts. Um, you know, every uh we must

22:50
use the bluff principle. So, every section must open with the most important idea and then segue to

22:56
examples, extra context, that kind of thing. Um, we need to make sure we're logically

23:02
supporting the thesis. So, the headers must make sense within the context of the title you've created. We need to be

23:08
exhaustive in how we cover the topic. We need to be mutually exclusive so we don't have loads of overlap between each

23:14
of the sections. Um, and again, these are things that if you ask Claude to edit an article and make it me, it does

23:21
a fairly good job of that. It has a good comprehension of what that means. Um, and then you can see, uh, an example

23:28
out of an outline here. So, we've got hook, key points, uh, any

23:35
ideas for transition it wants to include or a specific example it wants to include. It wants to include a table.

23:41
Um, these are the bones of the article. you mention a very uh important word.
Why examples beat instructions for teaching AI your voice

23:47
The word is example. Uh I can give you uh a quick reference

23:54
of why I'm talking about it. So I have a bunch of uh skills in my cloud code for

24:01
creating LinkedIn posts. Uh for example, I have uh product based

24:06
LinkedIn posts when I'm announcing a feature. I have uh podcast announcements when I'm announcing that I had a new

24:13
guest on the podcast. Uh or just regular posts when I have an idea and I want to

24:19
kind of deliver it in the best possible and punchy way. The thing is for like

24:25
each of those is a separate skill that I have created and I have instructed uh uh clo code of what I'm looking for because

24:31
when I'm announcing a podcast that's one format when I'm announcing a product update from HFS that's another format.

24:38
when I want just to improve a random post that can be about anything that's a different set of instructions. But the

24:45
thing is for each of those skills I have a folder where I I have given claude

24:50
code a bunch of examples here are the examples of my previous podcast announcements. So that not only you have

24:58
my instructions of how to write them, how to structure them, you have examples of how I did that in my voice already

25:04
previously and also like those examples come uh also with engagement metrics. So

25:09
it's it even sees which posts perform better, which post performed worse. Uh

25:14
same for podcast announcements, same for product announcements, and same for random posts. So it always have uh a

25:21
folder with examples to reference. And I almost feel like when it only has

25:27
instructions versus when it has instructions and like

25:32
five to 10 examples, I feel it does a better job when it has kind of the

25:38
actual examples to fall back to. So when you're saying that this is there's a step of an outline, I almost want to you

25:46
to have a folder where you have five examples of outlines of previous posts.

25:52
We do have that somewhere. Is it templates? Yeah, somewhere we do have that. Maybe

25:58
it's in part of the the skill files because exactly the same thing. I you

26:04
know, we every time we generate something, we generally want it to maybe sound like us or sound a particular way.

26:11
And I used to see a lot of people feed it writing and say, can you distill my writing down to a handful of principles

26:17
that you can then follow? I was I was always very skeptical of that though like how can you reduce somebody's

26:22
unique voice down to a handful of things that then Claude without that example to back it up can actually go away and do.

26:29
I think what you you're right the much better thing to do is let the model infer itself from an actual example

26:35
cuz you know your writing style I don't think is always going to map neatly across to a five bullet point lists of

26:42
your writing style or whatever but Claude is a large language model. it can infer from large samples of text the

26:48
patterns that do actually exist in your content and that is how it will end up sounding like you. So I totally agree

26:54
anchoring it with an actual example and saying make it sound like and feel like this is actually pretty good from what

27:00
I've seen. Yeah. And this is this is exactly how people should create those skills in the first place because the

27:06
way I created my skills is I gave it a bunch of my previous podcast announcements. I said analyze these

27:13
posts. tell me what I'm doing here, tell me what's my style. It would tell me

27:19
like what it kind of inferred from uh reading my posts and I would correct it if I disagree somewhere. If if it

27:25
doesn't feel like it understands what I'm doing, uh sometimes it would understand what I'm doing better than

27:31
myself, which is funny. I'm like, "Oh, that's that's really what I'm doing. I just I I was doing it subconsciously. I

27:37
didn't understand that." And then for example uh speaking of podcast announcements I would give it some

27:42
podcast announcements from Lenny Richitzky how he announces his podcast interviews on LinkedIn and I would say

27:48
okay analyze what Lenny is doing here. Uh it would analyze what Lenny is doing again I would correct if I disagree with

27:55
something and then I would say now create kind of something in between something between my approach and

28:01
Lenny's approach and tell me what set of instructions you would come up with. So basically I'm not creating instructions

28:07
myself. I don't need to write out instructions. I'm giving it examples. I'm telling I'm telling it analyze and

28:13
tell me what you see like what's the kind of principles behind this piece of content. And then I would correct it. If

28:20
I disagree with something, I would monitor what what instructions it is creating for itself and I would correct

28:25
it. And then like I said, it's very important to have those examples for it to fall back on. Uh because then I just

28:32
I just feel the output is always better. Okay. So that's outlining step. Uh like

28:37
you said, you you do have some outline examples. Actually, it's as easy as uh asking Claude, hey, outlining step. Uh

28:44
tell me, do we have examples for it? How are they stored? Are they stored in a text document? Are they stored in a

28:49
folder? And it would tell you. And if you don't, you can just say, okay, then create this folder, add these examples,

28:55
and cross reference it. So, yeah. uh a lot of people kind of

29:01
I'm not sure if I can use the word overengineer but they overthink they overthink what is AI but it's like as

29:07
easy as just talking to it asking it questions like how did you do this how did you do that and guiding it uh well

29:14
of course if you have a good idea of what you want to achieve but it's very important to be able to break the

29:19
process into kind of uh smaller steps into building blocks so to say
Finding natural product placement opportunities

29:26
okay Next, after outline, what's the step? So, now what we do is we look at the outline we've created and we ask Claude

29:33
to find specific opportunities to mention relevant HF's products. Um, I

29:39
tried, you know, having this integrated into other steps and it was a bit hit and miss. And this is obviously something that really matters to us

29:45
because this is why we write content. We want to talk about the product in context where it makes sense to do that.

29:51
So, this is a discrete stage. This will do this every single time. Um

29:57
uh you know it's very simple cuz within the skill I actually have a kind of master list of HFS products and features

30:04
which I asked Claude to create for me and then I updated and tweaked myself to include like newer ones add some

30:10
features. So it goes to that and it looks at the outline. It says which of these can I contextually mention in this

30:17
outline and have it make sense, have it be useful for the reader. And it just adds a little signpost for the next

30:22
step. Uh so that when it comes to drafting, it knows to actually incorporate HFS into it.

30:28
You know, keyword explorer, that kind of thing. And again, probably this is not something that people need to write

30:35
start to finish themselves. Just drop links to your landing pages to your video overviews. Ask it to analyze it

30:43
and tell it tell you what the product is, what is it, what is it good for, what are the top use cases, what are the

30:49
like uh use cases for I don't know for this area, for that area and then you

30:54
just correct it. So yeah, it's actually those things are easier to create than than uh people might think.

31:02
Yeah, exactly. We've got site audit, rank tracker, content explorer. Uh Claude did most of the heavy lifting

31:08
here. I just reviewed it. Um and I added in some I need to add in like fire hose and things like that actually. Um but

31:16
again, Claude can do all this for you. It's a fantastic diligent worker. Uh and then after that is the drafting stage.

31:23
Now I think when most people would do like an AI content process, this is probably the only stage they would create. And certainly when I've talked

31:29
to people, this is all they do. they focus on what are the best prompts for making an article. But yeah, from all of

31:36
our trial and error, I think having tons of steps for research and structure before you get to writing is what ends

31:41
up giving you the best outcome. Um, and this is again similar to the writing

31:48
rules we had in our previous GPT. It just has some this is adapted from our own internal writer like style guide for

31:54
writing. You know, use the problem, agitate, solution uh formula. Here's an example of it in action as part of the

32:01
introduction that works pretty well. Some structural stuff that inverted pyramid uh always explain what and why

32:10
uh all these very simple things and draft very well draft is not a final step right is not

32:18
the final step. So what goes after draft? So uh as we have a kind of verify claims

32:26
stage um internal linking is very important for us and for SEO and also

32:32
making sure we have included useful up to-ate sources for everything that we

32:37
do. So there is a particular step in here that it actually goes through the draft and it looks for the claims

32:43
things you know claims that the article is making that we would need to go out and validate and it makes sure that it

32:49
has an upto-date source for that or it update it reviews it to see if it's

32:54
accurate or not. Um and actually I've been working on this updating this skill

33:00
because this is a big part of our content updating workflow. We want to go back to old articles, find all the

33:05
claims, make sure they have the most up-to-date uh validation and accurate stats for it. Uh so that's the next step

33:11
of that process there. And there's there's more steps after this. Yeah, not too many more. Um so we have

33:19
uh a preview stage. So at this point, I wanted to be able to look at the draft uh and sadly check it and see if I was

33:25
happy with it. And it's not always I don't like looking at markdown files like this. So, it actually generates a

33:30
HTML file that is styled to look like the HF's blog. And I can then open that

33:36
up in my browser just to like see what it would look like and feel like on the blog so I can quickly review it from

33:42
that point of view. And the thing that still takes a ton of my time that I'm trying to work on is uh

33:49
screenshots. So much of our content is productled. It involves using the HF's product.

33:54
Screenshots are so important for that. At the moment, what this does is it will

34:00
uh suggest a report uh that we can actually go and visit and take a screenshot of. And we actually have

34:07
another skill that other people on the in the company have built which allows the claw to structure correct URLs for

34:14
our reports. So it can actually generate a genuine report URL for you to visit in HFS and then I can take a screenshot of

34:21
that. So that's quite useful. I'm trying to automate that with some headless browser stuff and some screenshotting and that

34:27
kind of thing. Um, but at the moment I spend as much time doing the screenshots as I do actually editing, reviewing,

34:34
generating. So that's a big part of it. Okay. Uh, since my my job on this
The critical importance of providing human context

34:40
podcast and in our calls is to essentially criticize everything you do.

34:47
What a fun job. people would would uh think I'm a terrible person, but it is

34:52
what it is. To be honest, one one step I I uh expected to see in this process is

35:00
when you would uh kind of dictate to this system some of your thoughts of

35:07
where to take this article in free form and I would explain uh why ah you have

35:13
it or something. You you're pointing something out. I do indeed. Yeah, I kind of glossed over it. Um, I totally agree. Sometimes

35:19
you just want to provide a few sentences of thought or direction. You want to mention a specific product and you don't

35:24
trust that it will do it itself. So, one of the things I added recently was this context trigger. Um, so this right at

35:31
the get- go when you trigger the workflow, you can provide it with as many sentences of context as you would like and that is then used to shape and

35:38
inform the rest of the process. Um, so often I'll say cover this topic or this topic or review this existing article

35:45
and bring elements of that into it or mention this new product and that kind of thing and it's just a little

35:51
directional nudge and again that seems to be very useful for getting a good outcome from it. Uh, I think it's like a

35:58
critical step in my opinion. Again uh we are still in the very early days of all

36:04
that. We're still experimenting and I like I have thought so many thoughts uh

36:09
in regards to all this. So first of all, I think it's important to point out that what you just showed is a work in

36:15
progress because any any kind of skill, any kind of workflow that you build for

36:20
yourself uh in cloud code or any other AI, it shouldn't be set in stone. Every

36:26
time you run it and every time you analyze the output whether total output

36:31
or whether output of the steps and you don't like something you need to go and refine and you keep refining and

36:37
refining and you're basically teaching your AI workflow AI agent AI skills

36:43
skill to do a better job and with every run it would get better and better. Uh so this is the first point. The second

36:48
point I feel this uh this this step of giving it context is super important

36:55
because it is what will essentially make your content unique because again uh the

37:03
reason why I was also surprised that you would let it run for 8 minutes and just generate something for you is because I

37:09
would expect that uh you would get a TLDDR file from the top competitors. you
37:15
would go through it and you would just like in free form uh I'm I'm using whisper flow this thing to dictate into

37:21
into anywhere basically in text all the time and I would just click a button and I would say oh like so I disagree with

37:28
this part I think this part is good don't even mention this part is not important here is where I think you can

37:34
and you can give it a lot of instructions it's almost as when we had those uh content mastermind calls where

37:40
we would discuss ideas and we would brainstorm where to take every idea In the same way that we were giving each

37:47
other feedback and uh kind of figuring out what angle is best to take uh with

37:53
uh any given content idea in the same way you can provide uh feedback to or

38:00
context to AI and I feel it would it it typically would do a great job at doing

38:06
this and that very another very good point maybe I'll talk briefly about how I

38:12
think conceptually this process should be use for content marketing generally like this is not the HF's content

38:18
process going forward. It is not as though everything we create has to come through this or will come through this.

38:23
Um we spend a lot of time writing stuff that is AI is still not very good at helping with things that require tons of

38:30
thought and experience and unique perspectives and ideas that maybe other people haven't even shared before. I

38:36
think this is really useful because, you know, we've written literally thousands of articles over the years. And what I

38:44
see being really important for us going forward is having this well-maintained library of evergreen search content. I

38:50
want to make sure we cover all the core topics that relate to our product and how to use it, keep them updated. And a

38:55
lot of times that is very simple, quite repetitive stuff like how many ways are there to do keyword research? Quite a

39:01
few as it turns out. So I think this is really good for topics you know we have

39:06
tons of information documenting keyword research and all these kinds of topics that can be used to inform this process.

39:13
This is almost like you know doing our housekeeping for us in some sense. Um it's not something that requires a ton

39:19
of direct involvement guidance because we've already done that. We've written dozens of articles on these topics that

39:24
is using used to shape these articles now. Um, and you know, I've generated

39:29
tons of articles from this that were I could have published and would have been fine, but I didn't know enough about

39:35
them. I didn't think they were interesting enough, and I've chosen not to do that because I still deeply care

39:40
about everything we publish and I'm I want to make sure we put out the best thing we can.

39:45
So yeah, I feel this process and the reason why kind of you let it run on itself with little output, it feels that

39:53
it's best used to take some kind of what we call a general knowledge topic and

39:59
adapt it to us because one of the steps it pulls from our existing content and

40:04
it finds what kind of unique stuff we said. Then it finds the the way to uh

40:09
include HFS in our use cases in this post. So basically for example there's plenty of information about link

40:16
building but it doesn't necessarily share what we have shared about link

40:21
building and it doesn't necessarily makes good use of HF's tools when it comes to link building. So with this

40:27
automated process this is where you don't need to write something from scratch. You can analyze existing content and AI can find a lot of

40:34
information from our existing articles and from our tools to include in the post and yeah you have uh the post

40:40
ready. Am I right? Yeah, exactly that. Yeah. I like to

40:45
think, is this a boring topic that I don't want to write? Um because we've covered it a thousand times. If so,

40:51
maybe it's a good candidate for the AI process, which is not everything we publish

40:58
in that regard. Uh oh, you have you have some something else to say. Yeah. So, very briefly, I because it

Using AI to update thousands of existing articles
41:03
kind of ties on to this. I'm also we built a content updating pipeline. This is a bit newer. I'm still tinkering with

41:09
this but in a similar you know we have yeah thousand published articles for example and it's very hard for human

41:15
people to keep on top of that keep them updated so we're working on a similar process here that is designed to

41:21
basically periodically give you updated content to review and edit and approve and potentially publish um and very

41:29
similar thing there are basically three things this does it looks for claims that might be outdated so there's an old

41:37
stat or something that doesn't make sense, Claude will review it and try and find a new version of that and allow you

41:42
to accept it if you want to. Um, you can find opportunities to add new hrefs

41:47
product features. So, obviously some of our articles were published like 8 years ago. They don't mention our latest

41:53
products like fire hose or you know uh AI content helper. This can make recommendations for you. And lastly,

42:00
updating topic gaps. So this is where it looks at the SER and it says, "Is there anything that has other articles talk

42:06
about that we don't? Perhaps we should draft a section for you to review and edit and include." And it just makes,

42:12
you know, very boring um unstructured process a bit more organized and a bit more um fun for people to engage with. I

42:19
think I I really really like where all of this is going because I think this is

42:24
actually the future of how content is going to be created. And uh I wanted to

42:29
wrap wrap this up from a different perspective because you essentially shared a workflow of how uh to create

42:36
content on what you call like a boring topic, something that has been covered over and over and we just have like some

42:43
unique spin or we want to cover this topic and include our products and services. I wanted to to share a quick

42:49
story uh from the other side when you want to create something completely unique. uh and that is uh so I'm in the

42:56
process of writing a book as I mentioned many times on this podcast already and uh just 8 months ago I was complaining

43:04
to uh a bunch of our team members that it is very hard for me to context switch

43:09
because when I stop working on the book and I do some like projects uh inside

43:15
HFS and then I need to return to the book like a few weeks later I barely remember what I was writing about I

43:21
barely remember my train of thought and it's almost like I need to upload all the information from scratch and uh I

43:28
think it was further who said uh why don't you just upload like all your chapters to AI and kind of ask it to

43:34
guide you like AI would ask like a journalist or a ghost writer who would be interviewing you asking you questions

43:39
and would be kind of writing the book for you it was 8 months ago about 8 months ago and I said I cannot see how I

43:47
would be able to do that so back in the day we didn't have cloud code back in the day like Chad GPT just released

43:53
their custom GPTs or something. I couldn't see how I would upload like my

43:58
entire book and be able to work with it. Fast forward eight months and the last chapter of my book, I just finished the

44:05
the draft. The last chapter I wrote it with AI by dictating my ideas into cloud

44:10
code and my process was I told it, okay, the name of the chapter is this. What is

44:16
going to happen is you're going to create a folder with my random dictations because I have a list of

44:21
notes. what I want to say uh within this chapter and those notes exist in the form of three words or one sentence

44:29
basically talk about this or expand on this idea and I would hit a button and I

44:34
would just ramble. So there's this idea and they wanted to say blah blah blah and we like did this thing at HS and we

44:42
have this interesting story blah blah blah dictation over next idea and I was

44:47
just uh rambling on each of my ideas. I had a few dozen of them. Okay, it saved

44:52
that to the folder. And I said, okay, I'm also like one talking when talking about those ideas, I was referencing a

44:58
few things. Some of the things that I discussed with some other marketing leaders on the podcast, some of the things that we actually covered on HF's

45:04
blog, for example, we have an article about taste and I just said, "Oh, like I'm talking about taste in in my chapter

45:10
and you have my voice dictation with my ramblings about it, but we also wrote a nice post. Please include it as sources

45:17
when talking about taste." So I gave AI I gave it all my dictations and I gave

45:23
it all the resources that I remembered like different uh YouTube videos, interviews, different articles that I

45:28
want to reference etc. Even some LinkedIn posts that I saw from people who are sharing these ideas and then I

45:35
said okay now the general idea of this chapter is this. I'm trying to make a

45:42
point that blah blah blah blah blah now you know like all my dictations now you

45:47
know all my resources all the stories I want to tell me how would you connect

45:52
the dots how would you structure it so essentially create me an outline and it

45:58
would write me oh so I suggest that you lead with this story then it transitions well this and then this argument and

46:04
then these things blah blah blah at which point I would say like I would give it some feedback where change it or

46:10
not or I would say sounds good to me write it and it would write a chapter

46:16
for me and then I also like uh uploaded to cloud code. I uh I downloaded from Google documents all my previous

46:22
chapters and I said okay for each chapter create kind of a synopsis file what this chapter is about what are the

46:29
key arguments that I'm making and what is the TLDDR outline of a chapter what are the main stories and key ideas and

46:35
I'm sharing so for each chapter it created this file kind of with a recap of the chapter and then I said now refer

46:41
to all the files of all the chapters and create me a synopsis of the book I want to know like what the book is about how

46:47
it is structured and what is illogical ical and it is so good. It's like it's

46:52
literally like you're you're offloading some of your brain work to someone else like you have an external brain that

46:59
processes information for you. So this is why kind of when when we started

47:05
talking and when you shared that you created a system for uh creating uh blog post fast and you said that your

47:12
productivity increased that you published like three articles in a few days or something like that. I am

47:17
actually expecting that all of the content that we're going to create, it would go through AI that we will no

47:25
longer manually write stuff. We would just hit a button. We would ramble to AI

47:30
what we want to say. We would point it at like whatever resources we want to

47:35
use to make a point and it would help us write even a better article because its

47:40
ability to connect the dots and understand what you're saying is actually quite crazy. I'm very surprised

47:48
how well it was able to distill my ramblings into coherent ideas and

47:54
connect the dots between them and organize it in a way where I'm like, "Wo, this actually looks quite good." So

How AI eliminates creative drudgery, not creativity itself
48:02
yeah, uh the process that that we just covered uh in in this podcast is uh

48:07
mostly for kind of semi-automated content. you still want to like overlook it and like like you said you have a

48:13
step to give it context of where you want to take it and what's the unique angle and stuff like this but it's still

48:18
like you're you're offloading the majority of the work while I think going

48:24
forward creating content yeah AI would act like a journalist an editor a ghost

48:30
writer and you would act as a source of ideas and opinions and people who don't

48:36
have a good writing skill but have strong opinions would be able to publish their content fast. So, what are your

48:42
thoughts on this? Yeah, I totally agree with that. Um, I always find some people think that human

48:48
creativity is too unique and magical and special that like AI could never help with it and never be a useful aid in

48:54
that process. But actually, there's a lot of mental drudgery we do when we're writing a book or an essay or anything

49:01
like that. I think the ideas, the motivations, the experiences, the things we care about, that is still uniquely

49:07
you in your book. still your book and your ideas. Yeah. But all you just sitting down for hours

49:12
and shuffling these ideas about and working out what are the common themes that is something that AI is fantastic

49:18
at doing. Um yeah, if it can make these writing and creative processes more fun for us,

49:24
then like that shouldn't be scary. I think that should be fun. We'll be more prolific. We'll share more stuff. There'll be more of our unique thoughts

49:30
and ideas out in the world. Um, so if yeah, for all the kind of like sad drudgery and you know, are we automating

49:37
careers and jobs away? Actually, we could create more cool stuff than has ever existed before in human history.

49:42
It's totally possible. Now, I I like I like the word drudgery. I think what what AI does, it it literally eliminates

49:50
drudgery because like I said, for me, it was a pain to go back and to because I

49:56
would need to read my entire chapter again to remember what I was saying there. And now I can say remind me what

50:02
was the synopsis of the chapter where we left off. Uh which ideas need work. It would tell me all that and I'm like

50:08
immediately I can continue working and I can pick up where we left off. So yeah, let's let's not make it longer than uh

50:16
than we need. Uh thanks a lot for sharing your uh process. Thanks a lot for as always letting me to jump in with

50:23
my thoughts and ideas. Uh I generally think we're on the right track with with

50:28
uh these kinds of things and this is the future. Definitely this is the future of content marketing and content creation.

50:35
Thank you Ryan. Thanks Tim.