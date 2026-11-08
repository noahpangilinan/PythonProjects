# Python Projects

Short Python programs from RIT's CSAPX (Computer Science for AP Students) course. Each lab is a
single script that needs only the standard library.

| Lab | Program | What it does |
| --- | --- | --- |
| 1 | [`transformer.py`](lab1/src/transformer.py) | **Secret Messages.** Encodes and decodes a message by applying a list of operations: shift a letter, rotate the string, duplicate a character, trade two characters, remove duplicates |
| 2 | [`antenna.py`](lab2/src/antenna.py) | **Antenna fractal.** Draws the same recursive fractal two ways with `turtle` (line segments and squares) for a given side length and depth |
| 3 | [`bands.py`](lab3/src/bands.py) | **Battle of the Bands.** Finds the band with the median vote count, comparing a quicksort approach against quickselect |

## Running

Python 3.10 or later.

```sh
python lab1/src/transformer.py
python lab2/src/antenna.py
python lab3/src/bands.py fast path/to/bands.txt    # or: slow
```

`transformer.py` and `antenna.py` prompt for their input. `bands.py` takes `slow` (sort, then pick
the middle) or `fast` (quickselect) and a file of band names and vote counts.
