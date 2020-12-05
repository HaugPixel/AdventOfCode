#include <stdio.h>
#include <stdlib.h>


int * handleInput() {
    // File handling
    FILE *file;
    int number;
    static int numbers[200];
    int i;

    // File handling
    file = fopen("/Users/erlendhaugen/CLionProjects/AdventOfCode/program.txt", "r");

    if (file == NULL) {
        printf("Error! cannot open file");
        // Program exits if the file pointer returns NULL.
        exit(1);
    }

    i = 0;
    while (fscanf(file, "%d", &number) == 1) {
        numbers[i] = number;
        i++;
    }
    fclose(file);

    return numbers;
}

int part1(int *p) {
    // Checks if 2 integers in input equals to 2020

    int n, i, k, l,  m;

    for (i = 0; i < 200; ++i) {
        l = p[i];
        for (k = i+1; k < 200; ++k) {
            m = p[k];
            if (l + m == 2020)
                n = m * l;

        }
    }
    return n;
}

int part2(int *p) {
    int n, i, k,  l, m, j, o;

    for (i = 0; i < 200; ++i) {
        l = p[i];
        for (k = i + 1; k < 200; ++k) {
            m = p[k];
            for (j = k + 1; j < 200; ++j) {
                o = p[j];
                if (l + m + o == 2020)
                    n = m * l * o;
            }
        }
    }

    return n;
}

int main(){
    int *nums;
    int answer1;
    int answer2;
    nums = handleInput();
    answer1 = part1(nums);
    answer2 = part2(nums);
    printf("Answer for part 1 is %d\nAnswer for part 2 is %d\n", answer1, answer2);
    return 0;
}

