"""This program counts the number of lines it contains.

It is inspired by the `wc` Unix utility (for details, run the command `man wc`
on any Unix-like operating systems).

This program differs in at least two ways compared to `wc`.  One difference is
rather subtle.  Can you find out?
"""

def main():
    l = 0
    with open('activities/wc/wc.py') as f:
        while True:
            line = f.readline()
            if line == "":
                break
            l += 1
    print(l)

if __name__ == '__main__':
    main()
