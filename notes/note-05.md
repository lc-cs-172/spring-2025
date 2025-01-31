# CS2 Spring 2025 Note 05

## Pair programming

*Pair programming* is a software development process wherein two programmers
work together at one computer.  One programmer takes the role of the *driver*,
thinking about the fine details, actually typing and editing code, and
explaining what they are doing.  The other programmer is the *navigator*,
thinking about the big picture, offering advice and suggestions, asking
questions, and consulting documentation.  The members of the pair should be in
constant conversation so that they can switch roles at any moment.

## Reading a file

To read the content of a file, first you must open the file and then, if the
previous step is successful, read the content.

Below is a program that prints the content of a file to the console.

```python
def main():
    with open('input.txt') as f:
        while True:
            line = f.readline()
            if line == '':
                break
            print(line, end='')

if __name__ == '__main__':
    main()
```

The second line opens a file and, if successful, assigns variable `f` a handle
representing the opened file.

The fourth line reads one line from the opened file.  The function `readline`
returns an empty string when the end of the file has been reached.
