# CloudFlight Coding Contest — Winter 2022

Solutions to the Pac-Man problem from the [CloudFlight Coding Contest](https://register.codingcontest.org/),
winter 2022.

CCC is a timed contest where one problem is revealed in escalating levels: each
level adds a rule to the previous one, and your solution has to grow with it.

## The problem

You are given a grid, a starting position, and a fixed movement string
(`U`/`D`/`L`/`R`). Walk it and report what happened.

| Grid | Meaning |
|---|---|
| `C` | coin — collect it, then the cell is empty |
| `W` | wall — walking into it is fatal |
| ` ` | free space |

**Level 1** — walk the sequence, count coins, detect walls.
**Level 2** — the same over larger inputs.
**Level 3** — ghosts. Each ghost has its own position and movement string, and
running into one ends the walk.

Input arrives on stdin: grid size, the grid, Pac-Man's 1-indexed start, the
move string, then the ghost count and a position + move string per ghost.

Output differs by level — level 1 expects just the coin count (`18`), level 3
expects the count and survival (`2 YES`).

## Layout

```
Pacman_CCC_contest/
  main.py              the solution
  level1/  level2/  level3/
      *.in             contest inputs
      *.out            expected / produced outputs
level1.zip level2.zip level3.zip   original downloads
```

## Running

```bash
cd Pacman_CCC_contest
python main.py < level3/level3_1.in
```

To check a level against its expected output:

```bash
for f in level1/level1_*.in; do
  python main.py < "$f" | diff -q - "${f%.in}.out" && echo "ok $f"
done
```

## Note

This is contest code, written against the clock and kept as submitted.
`main.py` is the **level 3** solution — it prints `<coins> YES|NO`, so it will
not match level 1's expected output, which is the coin count alone. It also
still contains its debugging `print()` calls, which go to stdout and would
break a diff against the `.out` files. Strip them before running the check
above.
