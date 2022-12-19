# :christmas_tree: :snake: :sparkles: Maja's Advent of Code 2022 :sparkles: :snake: :christmas_tree:

Ho, ho, ho, welcome to my 2022 Advent of Code repository!
My goal this year:
- collect at least 30 starts before December 25th

My AoC repositories: [2015](https://github.com/mimikrija/AdventOfCode2015), [2016](https://github.com/mimikrija/AdventOfCode2016), [2017](https://github.com/mimikrija/AdventOfCode2017), [2018](https://github.com/mimikrija/AdventOfCode2018), [2019](https://github.com/mimikrija/AdventOfCode2019), [2020](https://github.com/mimikrija/AdventOfCode2020), [2021](https://github.com/mimikrija/AdventOfCode2021)

## What I learned, what I still don't know

Legend:

:ambulance: - I don't fully understand either the logic or the implementation - HALP!

:hourglass_flowing_sand: - I think this could or should run faster, but I don't know how to optimize it!

:hammer: - Not completely satisfied with solution, but I know how (and plan to) fix it.

Puzzle | Solution(s) | Remarks |
---    |---    |----
[Day 1: Calorie Counting](https://adventofcode.com/2022/day/1) | [Python](python/01.py) | |
[Day 2: Rock Paper Scissors](https://adventofcode.com/2022/day/2) | [Python](python/02.py) | I manually sorted result outcomes and just sum indices of the scores list. It turned out to be the most elegant solution (to me). |
[Day 3: Rucksack Reorganization](https://adventofcode.com/2022/day/3) | [Python](python/03.py) | Sets for the win :heart: |
[Day 4: Camp Cleanup](https://adventofcode.com/2022/day/4) | [Python](python/04.py) | First solution with sets but then opted for working on range limits, similar to very simplified [2021 Day 22](https://adventofcode.com/2021/day/22) |
[Day 5: Supply Stacks](https://adventofcode.com/2022/day/5) | [Python](python/05.py) | Stacks! In my first implementation I didn't bother parsing the first part of input, I just manually typed it - it was faster! |
[Day 6: Tuning Trouble](https://adventofcode.com/2022/day/6) | [Python](python/06.py) | ~~Strings and zips (and combinations).~~ SETS FOR THE WIN again!!
[Day 7: No Space Left On Device](https://adventofcode.com/2022/day/7) | [Python](python/07.py) | Another successful non-tree implementation for an obviously tree-like problem. I guess I will never learn trees.
[Day 8: Treetop Tree House](https://adventofcode.com/2022/day/8) | [Python](python/08.py) | Grids with conditions, satisfying puzzle.
[Day 9: Rope Bridge](https://adventofcode.com/2022/day/9) | [Python](python/09.py) | I really liked this one! Same implementation for both parts, depending on the rope length. Instructions are over engineered, there are actually only two cases (which ~~I feel could be~~ can be reduced to a single case).
[Day 10: Cathode-Ray Tube](https://adventofcode.com/2022/day/10) | [Python](python/10.py) | Straightforward puzzle with pixel printing.
[Day 11: Monkey in the Middle](https://adventofcode.com/2022/day/11) | [Python](python/11.py) | I decided to go with classes to keep track of all the monkey data. This needs further cleanup :hammer:
[Day 12: Hill Climbing Algorithm](https://adventofcode.com/2022/day/12) | [Python](python/12.py) | BFS, but with searching from end to start (hack for part 2, as there are many possible "starts", but we're looking for the closest one).
[Day 14: Regolith Reservoir](https://adventofcode.com/2022/day/14) | [Python](python/14.py) | Pretty slow for part 2, need to think about it... :hourglass:
[Day 17: Pyroclastic Flow](https://adventofcode.com/2022/day/17) | [Python](python/17.py) | Ok this one was like a game of tetris. I kept all occupied positions in a set. For part 2 it was necessary to detect cycles. For the example data I was able to do it manually by printing height deltas, but the numbers were much higher for my input. With some hints from Reddit I decided to keep track of all _states_. Once I detected the first repeating state I did some `divmod` calculations to figure out the result. Still runs relatively long, is it because of sets? :hourglass:
[Day 18: Boiling Boulders](https://adventofcode.com/2022/day/18) | [Python](python/18.py) | `lava` is a set of all the lava cubes. For part 1 I counted how many neighbors each cell has that are not already in `lava` - that gave me the number of free faces. To solve part 2, i.e. find the inner area of trapped pockets I first defined `void` which are cells within the grid size not filled with `lava`. Then I decided to do a BFS (DFS?) starting from any void cell immediatelly adjacent to lava cells. The search returns `True` if a pocket is found, ie. if `potential_pocket` is completely surrounded by `lava` cells. Otherwise (early exit condition), the pocket is actually not a pocket (it is connected to the free space if any of its coordinates is on the grid border). When I return from the search I additionally reduce the search space as to not use any cells which we already concluded are not pockets. Then I use the same function as in part 1 to calculate the area of pockets (bare in mind that pockets by definition cannot contain other pockets, so their area _is_ their total outter area, i.e. total lava inner area). Part 2 solution is part 1 solution (total area) - inner area.
