# Weekly Report 3
*Author:* Henrik Harjula  
*Course:* Aineopintojen harjoitustyö: Tietorakenteet ja algoritmit (loppukesä 2021)  

## Working hours during the week
11.0 hours

## Done during the week
- Enhanced highway data for app (added missing road intersections) in order to make graph more complete
- First version of text user interface
- Making an own module of testing
- Initiating coverage testing
- Initiating pylint code quality checking
- First version of visualizing shortest path to user

## How program has evolved?
- First version of text user interface
- Moving testing to own module
- Coding first version of visualizing shortest path to user

## What I learned during the week?
I learned that Wikipedia's highway data was incomplete in the sense that all road intersections are not in the data (which is natural as there are no big cities in many of them).
I also studied and learned what would be a good way to visualize shortest path - I ended up in using Matplotlib library and its plot.

## What remained unclear or created trouble?
I noticed that all road intersections were not in Wikipedia's highway data - I ended up using Google Maps and collecting manually missing road intersections so that highway data forms a complete graph which can be input to shortest path algorithms.
First it was hard for me to find a good way to visualize shortest path - Then I found Matplotlib library's plot which is pretty easy to use.

## What will I do next?
- Study IDA* algorithm and start coding it
- Implement heap as self-coded data structure (instead of Python's default implementation)
- Improve visualization of shortest path
- Refactor current modules
- Enhance automatic testing of the app
