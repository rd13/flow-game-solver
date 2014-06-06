Flow Game Solver in Python
================

Attempts to generate a solution for the popular iOS and Android game Flow (traditionally known as number link) given an image of the unsolved Flow grid:

![Flow](https://raw.githubusercontent.com/rd13/flow-game-solver/master/flow6x6.png "Flow")

It:

  - Uses OpenCV/Hough transformations to detect grid size, circles, and circle colours
  - Constructs a matrix using the previously found information
  - Attempts to solve the puzzle

For the above image we construct a matrix like so:

```sh
#| _| _| _| _| #| 
#| _| _| #| _| _| 
_| _| _| #| _| #| 
#| #| _| #| _| _| 
#| #| _| _| #| _| 
_| _| _| _| _| _| 
```
And detect the circles and their grid references:

```sh
[
[(1, 0), (3, 0)], // Light Blue
[(0, 5), (4, 1)], // Green
[(3, 3), (4, 4)], // Yellow
[(4, 0), (2, 3)], // Orange
[(3, 1), (0, 0)], // Red
[(2, 5), (1, 3)]  // Blue
]
```

Running the solve method gives us a solution which is the path (grid references) each colour must then take to solve the puzzle:

```sh
[
[(3, 0), (2, 0), (1, 0)], // Light Blue
[(4, 1), (4, 2), (3, 2), (2, 2), (1, 2), (0, 2), (0, 3), (0, 4), (0, 5)], // Green
[(4, 4), (4, 3), (3, 3)], // Yellow
[(2, 3), (2, 4), (3, 4), (3, 5), (4, 5), (5, 5), (5, 4), (5, 3), (5, 2), (5, 1), (5, 0), (4, 0)], // Orange
[(0, 0), (0, 1), (1, 1), (2, 1), (3, 1)], // Red
[(1, 3), (1, 4), (1, 5), (2, 5)] // Blue
]
```

