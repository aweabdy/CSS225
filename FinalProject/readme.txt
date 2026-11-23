===============================================================================
 SIGNAL FROM ALA-TOO - Technical Documentation
 CSS-225 Final Project: Adventure Game Final Version
 Author: Abdyrakhman Raiapov            Date: November 23, 2026
 Course: CSS-225, National Louis University
===============================================================================

Signal from Ala-Too is a text adventure game written in Python. In the year
2087 a drone mechanic named Nur receives a broken distress message from
Ala-Too Station, a research observatory in the Tian Shan mountains of
Kyrgyzstan. Nur has six hours before a snowstorm hits to reach the station,
get past KEEPER (the station's security AI), free Dr. Omurova, and send a
signal for help. The game has 5 chapters, 2 puzzles and 6 endings
(1 best, 2 neutral, 3 game over), and the player can move forward to the
next chapter or go back to an earlier one.

This document is written for a new developer joining the project or an
administrator who has to maintain it.


-------------------------------------------------------------------------------
 1. WHERE THE CODE IS HOSTED
-------------------------------------------------------------------------------
 GitHub repository:  https://github.com/aweabdy/CSS225
 Game folder:        https://github.com/aweabdy/CSS225/tree/main/FinalProject
 The same files are also submitted to D2L as one zip file
 (Signal_from_Ala-Too_Final_Abdyrakhman_Raiapov.zip).


-------------------------------------------------------------------------------
 2. EXTERNAL SERVICES
-------------------------------------------------------------------------------
 None. The game does not use the internet, a database, an API, or any
 third-party package. It only uses Python's standard library:
   - time    (printcommon.py) - pause between characters for the "radio" effect
   - random  (challenges.py)  - random engine setting and random riddle


-------------------------------------------------------------------------------
 3. LANGUAGES AND TECHNOLOGIES
-------------------------------------------------------------------------------
 - Language: Python 3 (tested with Python 3.14 on Windows 11)
 - Interface: text-based, runs in a terminal / console (input() and print())
 - Python features used: modules and import, functions with parameters and
   return values, a class (Player), lists, dictionaries, tuples, if/elif/else,
   while and for loops, Boolean flags, the global keyword, and
   if __name__ == "__main__" blocks for unit testing.
 - Planning tools: draw.io flowcharts (Milestone 2 and 3).


-------------------------------------------------------------------------------
 4. SYSTEM REQUIREMENTS AND SUPPORTED APPLICATIONS
-------------------------------------------------------------------------------
 - Any computer that can run Python 3.8 or newer: Windows, macOS or Linux.
 - About 50 KB of disk space; no extra memory or graphics card needed.
 - Supported ways to run it:
     * a terminal: Command Prompt / PowerShell (Windows), Terminal (macOS/Linux)
     * IDLE (comes with Python)
     * VS Code, PyCharm, or any IDE that runs Python files
 - Python can be downloaded from https://www.python.org/downloads/
   No pip packages need to be installed.


-------------------------------------------------------------------------------
 5. CODING / NAMING CONVENTIONS
-------------------------------------------------------------------------------
 - File names are lowercase: maingame.py, chapter1.py ... chapter5.py,
   globalvariables.py, printcommon.py, challenges.py, endings.py, player.py.
   One chapter = one file (chapterN.py).
 - Functions and variables use snake_case and describe an action or a value:
   replay_message(), repair_drone(), storm_timer, wrong_answers.
   The one exception is gVariables(), the name used for the reset function
   in the course's example game.
 - The class name uses CapWords: Player.
 - Constants are UPPERCASE: STORM_HOURS, MAX_WRONG_ANSWERS, ENGINE_TRIES,
   FORWARD, BACK, ALARM, ROUTES, ENDINGS.
 - Every chapter module has a play() function. It returns what happened:
   gv.FORWARD, gv.BACK, gv.ALARM, or the name of an ending such as "best".
 - Every file starts with a header comment (author, date, course, purpose),
   and every function has a docstring explaining what it does and returns.
 - Modules import the shared state as "import globalvariables as gv" and use
   dot notation (gv.player.add_item("rope")). Do NOT write
   "from globalvariables import player": a new game replaces the Player
   object, and that import would keep pointing at the old one.
 - Menus are always numbered and use printcommon.get_choice(), which
   rejects anything that is not a valid number, so bad input never crashes
   the game.


-------------------------------------------------------------------------------
 6. HOW TO RUN / BUILD / DEPLOY THE PROGRAM
-------------------------------------------------------------------------------
 Build: Python is interpreted, so there is nothing to compile or build.

 Run:
   1. Install Python 3 (see section 4).
   2. Download the game: on GitHub open the FinalProject folder and download
      the files, or clone the repository:
          git clone https://github.com/aweabdy/CSS225.git
      or unzip the D2L zip file.
   3. Keep ALL the .py files together in the same folder (the chapters import
      each other by file name).
   4. Open a terminal in that folder and type:
          python maingame.py
      (on some Macs/Linux: python3 maingame.py; on Windows also: py maingame.py)

 Deploy: to give the game to another player, share the folder (or the zip /
 GitHub link). The player only needs Python 3.

 Testing a single chapter (unit testing): every module can be run on its own
 because it ends with an  if __name__ == "__main__":  block. For example:
          python chapter3.py
 sets up a test player and plays only Chapter 3, then prints what the chapter
 returned. player.py and globalvariables.py run automatic checks with assert.
 When a chapter is imported by maingame.py, this test code does not run.

 Settings an administrator may want to change:
   - printcommon.DELAY = 0.02   -> set to 0 to print text instantly
   - globalvariables.STORM_HOURS = 6 -> more or less time before the storm
   - globalvariables.MAX_WRONG_ANSWERS = 3 -> riddle tries before the alarm

 Troubleshooting:
   - "ModuleNotFoundError: No module named 'chapter1'": the files are not in
     the same folder, or the terminal is open in a different folder.
   - "'python' is not recognized": Python is not installed or not on PATH;
     try "py maingame.py" on Windows or reinstall Python with "Add to PATH".
   - Text appears too slowly: set DELAY = 0 in printcommon.py.
   - To quit at any time: press Ctrl+C.


-------------------------------------------------------------------------------
 7. OVERVIEW OF THE ARCHITECTURE
-------------------------------------------------------------------------------
 The game is split into small modules. maingame.py controls the story; each
 chapter file controls only what happens inside that chapter.

   maingame.py ------ CHAPTERS table, ROUTES table, game loop
      |
      +-- chapter1.py ... chapter5.py   (one file per chapter, each has play())
      |        |
      |        +-- challenges.py   puzzles: start_engine(), keeper_riddle()
      |        +-- printcommon.py  slow_print(), chapter_title(), show_status(),
      |        |                   get_choice(), storm_check()
      |        +-- globalvariables.py  settings + the shared Player object
      |                   |
      |                   +-- player.py   class Player
      +-- endings.py   ENDINGS dictionary, is_ending(), show_ending()

 Files, functions and data:

 maingame.py
   CHAPTERS     dict: chapter number -> (title, play function)
   ROUTES       dict: chapter number -> {result: next chapter number}
   next_step(current, result)   returns the next chapter or an ending name
   announce_move(current, target)  prints ">>> Moving on" or "<<< Going back"
   play_game()  one full game; main()  title screen and "Play again?"

 player.py - class Player
   attributes: name, inventory (list), storm_timer, wrong_answers,
               route (list of visited chapters), and the story flags
               has_drone, logs_read, keeper_ally, power_cut, engine_started
   methods:    has_item(item), add_item(item), remove_item(item),
               lose_time(hours=1), visit(chapter_number), status_line(),
               route_text(), __str__()

 globalvariables.py
   STORM_HOURS, MAX_WRONG_ANSWERS, PLAYER_NAME, FORWARD, BACK, ALARM
   player       the current game's Player object (a global variable)
   gVariables() creates a new Player, so every new game starts fresh

 printcommon.py   DELAY, slow_print(text), chapter_title(number, title),
                  show_status(), get_choice(options), storm_check()
 challenges.py    start_engine() (3 tries, higher/lower hints),
                  RIDDLES list, keeper_riddle()
 endings.py       ENDINGS dict (name -> (title, text)), is_ending(result),
                  show_ending(name)

 chapter1.py  The Last Message  (Karakol workshop)
   replay_message(), visit_uncle_bakyt(), pack_backpack() (choose 2 of 3
   items), drive_up_the_road() (engine challenge), play()
 chapter2.py  The Frozen Pass   (avalanche)
   repair_drone(), climb_cliff(), walk_around_lake(), play()
 chapter3.py  The Locked Gate   (KEEPER at the gate)
   enter_gate_code(), answer_riddle(), send_drone(), search_snow(), play()
 chapter4.py  Inside the Core   (KEEPER locked the lab)
   read_logs(), talk_to_keeper(), cut_power(), search_storage(), play()
 chapter5.py  Before the Storm  (the antenna on the roof)
   restart_generator(), repair_antenna(), drive_down(), go_back_to_core(),
   play()

 How the main loop works (maingame.play_game):
   1. gVariables() creates a new Player; the game starts at Chapter 1.
   2. The chapter's play() runs and returns a result.
   3. next_step() checks the result: an ending name ends the game; otherwise
      ROUTES gives the next chapter number.
   4. The loop repeats, so the player can go forward and back as many
      times as they like (no recursion), until an ending is reached.

 Story map (ROUTES):
   Chapter 1 --forward--> Chapter 2
   Chapter 2 --forward--> Chapter 3     Chapter 2 --back--> Chapter 1
   Chapter 3 --forward--> Chapter 4     Chapter 3 --back / alarm--> Chapter 2
   Chapter 4 --forward--> Chapter 5     Chapter 4 --back--> Chapter 3
   Chapter 5 --back-----> Chapter 4
 Endings: best (Ch5 antenna repaired), neutral_lab and neutral_drive (Ch5),
 gameover_sleep (Ch1), gameover_road (Ch5), gameover_storm (any chapter,
 when the storm timer reaches 0).

 Changes in the final version (feedback from Milestones 2 and 3):
   - maingame.py now holds the routing logic: chapters report what
     happened, and the ROUTES table sends the player to the next level or
     back to an earlier one.
   - Every chapter (and every helper module) has an
     if __name__ == "__main__": block for unit testing.
   - A Player class replaces the separate global variables.
   - The route the player took is shown at the end of each game.
   - Chapter 1 shows a short "back in the workshop" text when the player
     returns to it.
   - (Milestone 2) Chapter 1 has a challenge (starting the frozen car)
     that must be completed before Chapter 2, and Chapter 5 lets the
     player go back to Chapter 4.


-------------------------------------------------------------------------------
 8. HOW TO START THE PROGRAM (START THE GAME)
-------------------------------------------------------------------------------
   1. Open a terminal in the game folder.
   2. Type:   python maingame.py
   3. Read the story text and choose an action by typing its number and
      pressing Enter. Watch the storm timer and inventory shown above each
      menu.
   4. When an ending appears, the game shows your route through the
      chapters and asks "Play again? (y/n)".

 Hint for the best ending: replay the message, pack the battery and the
 rope, repair the drone, find the spare sensor, and get help from Bulut
 or KEEPER before you repair the antenna.

===============================================================================
