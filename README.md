There was a viral video of an interview done at Anthropic recently. The challenge:

> Convert a collection of call stack samples into a chronologically sequenced list of events which represent the lifecycles of the sampled function calls..

I did not use any AI agents producing this. I converted the C++ starter code from the video in some regular Python classes and implemented the trace generation from there.

I watched the video through the interviewer explaining the task (I was vaguely familiar with call stack profilers, but have never written one). I paused the video prior to anything being coded or solved. It was a bit of an odd interview, but nonetheless an interesting challenge.

I did two iterations of the implemention. The first was really bad and utilized sliced and dicing the lists in various ways, incorrectly listed the 'end' events, etc. I then came to realize you can simply care about the difference between the state of the tracked stack and the current observed sample.

My solution simply considers "if the tracked stack is bigger than the sample frame, functions must have ended. If the tracked stack is smaller than the sample frame, functions must have started." This insight means I could implement to while loops with appropriate conditions. Only one would ever execution on any given sample.

Intuition suggested there may be a way to do it without the extra space requirement of tracking the call stack via a "dummy" stack like I implemented. I spent ~30 minutes getting to this point after translating the C++ code in the video to Python, so I kind of just left it there. Maybe I'll give it another shot with that constraint at some point :)

CJ covered the video here with a breakdown review of the entire interview. I paused the video at the 39 minute point before he gave any hints about the implemention :)
https://www.youtube.com/watch?v=XP9Zg--DLr8
