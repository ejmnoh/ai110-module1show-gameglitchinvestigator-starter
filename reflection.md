# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  It looked clean and easy to play.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  The first guess doesn't make the number of attempts left decrease.
  I couldn't start a new game without reloading the page.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|Guess of 2|Attempts left: 6|Attempts left: 7|none|
|New Game button|Start a new game|Nothing changes|none|
|Guess of 60|"Go HIGHER!"|"Go LOWER!" (actual answer was 88)|none|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  I used Claude. 
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  Claude suggested creating a function in order to correctly implement a new game and implemented all the necessary attributes to take into consideration. I verified the result by reading over it and making sure I understood it. 
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  Claude suggested adding a test that was unnecessary. I asked Claude about the test because I was confused, and Claude retracted its suggestion.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I used Claude to check with the tests and with Streamlit. I trusted Streamlit more, because I could actually see the changes.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I manually tested the number of attempts by using Streamlit. It showed me that it wasn't taking into account the first attempt.
- Did AI help you design or understand any tests? How?
  Claude helped me to understand that though I changed the attempts used to start at 0, the bug wasn't completely fixed because the attempts increments and saves to the session after the info box.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  Streamlit reruns starts the code from the top with the current session state. This means that reruns take into account and uses variables from session state from the previous runs.


---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  I liked using Claude to ask clarifying questions on the logic.
- What is one thing you would do differently next time you work with AI on a coding task?
  I would spend more time on the task myself first, then use AI.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  This project has made me understand that AI generated code doesn't have to be too complicated and unable to understand. AI generated code can be helpful.
