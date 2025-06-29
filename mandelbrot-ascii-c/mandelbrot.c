#include <stdio.h>
#include <sys/ioctl.h>
#include <unistd.h>

#define MIN_X -2.5
#define MAX_X 1.5

#define MIN_Y -1.5
#define MAX_Y 1.5

#define ITER 100

int get_window_size(int *rows, int *cols) {
    struct winsize w;
    if (ioctl(STDOUT_FILENO, TIOCGWINSZ, &w) == -1) {
        return -1; // Error getting terminal size
    }
    *rows = w.ws_col;
    *cols = w.ws_row;
    return 0;
}

double map(double n, double start1, double stop1, double start2, double stop2) {
    return (n - start1) / (stop1 - start1) * (stop2 - start2) + start2;
}

int main() {
    int width, height;
    if (get_window_size(&width, &height) != 0) {
        printf("Failed to get terminal size\n");
        return 1;
    }
    for (double row = 0; row < height; row++) {
        double y = map(row, 0, height, MIN_Y, MAX_Y);
        for (double col = 0; col < width; col++) {
            double x = map(col, 0, width, MIN_X, MAX_X);

            double c_real = x;
            double c_imag = y;

            double z_real = 0;
            double z_imag = 0;

            int iter;
            for (iter = 0; iter < ITER; iter++) {
                double z_real_new = z_real * z_real - z_imag * z_imag + c_real;
                double z_imag_new = 2 * z_real * z_imag + c_imag;

                z_real = z_real_new;
                z_imag = z_imag_new;

                double magnitude_squared = z_real * z_real + z_imag * z_imag;
                if (magnitude_squared > 4) {
                    break;
                }
            }

            if (iter == ITER) {
                putchar('*'); // Point is in the set
            } else if (iter > ITER / 2) {
                putchar('-');
            } else if (iter > ITER / 3) {
                putchar('+');
            } else {
                putchar(' '); // Point diverged
            }
        }
        putchar('\n');
    }

    return 0;
}
