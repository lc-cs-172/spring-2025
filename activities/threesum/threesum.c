// Measure the time its take to compute some function.

#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

/**
 * Return the number seconds since the Epoch.
 * @returns a number of seconds
 */
double time_get() {
    struct timeval t;
    gettimeofday(&t, NULL);
    return t.tv_sec + t.tv_usec/1000000.;
}

/**
 * Compute the number of distinct triples such that xs[i] + xs[j] + xs[k] = 0
 * @param n  the number of elements in `xs`
 * @param xs  an array of integers
 * @returns the number of distinct triples that sum to zero
 */
int count_triples(int n, int xs[]) {
    int count = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            for (int k = j + 1; k < n; ++k) {
	              if (xs[i] + xs[j] + xs[k] == 0) {
	                  count += 1;
	              }
            }
        }
    }
    return count;
}

/**
 * Run a doubling experiment.
 * @param n  problem size
 * @returns the number of seconds to run the experiment
 */
double time_count_triples(int n) {
    int *xs = malloc(n * sizeof(int));
    if (xs == NULL) {
        exit(1);
    }
    for (int i = 0; i < n; ++i) {
        xs[i] = lrand48();
    }
    double start = time_get();
    count_triples(n, xs);
    double end = time_get();
    free(xs);
    return end - start;
}

int main() {
    int n = 16;
    double t_prev = time_count_triples(n);
    printf("    size     time    ratio\n");
    for (;;) {
        n *= 2;
        double t = time_count_triples(n);
        printf("%8d %8.1f %8.2f\n", n, t, t/t_prev);
        t_prev = t;
    }
}
