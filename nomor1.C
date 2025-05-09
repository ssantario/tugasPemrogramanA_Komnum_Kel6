#include <stdio.h>
#include <stdlib.h>

#define MAKS_DATA 100

int tahun[MAKS_DATA];
double persentase[MAKS_DATA]; // Array untuk persentase pengguna internet
double populasi[MAKS_DATA];
int N = 0; // jumlah data

// Fungsi membaca file CSV
void baca_file_csv(const char *nama_file)
{
    FILE *fp = fopen(nama_file, "r");
    if (!fp)
    {
        printf("Gagal membuka file.\n");
        exit(1);
    }

    char baris[256];
    fgets(baris, sizeof(baris), fp); // skip header

    while (fgets(baris, sizeof(baris), fp))
    {
        sscanf(baris, "%d,%lf,%lf", &tahun[N], &persentase[N], &populasi[N]);
        N++;
    }

    fclose(fp);
}

// Fungsi untuk hitung koefisien regresi kubik untuk populasi
void hitung_koefisien_populasi(double *a, double *b, double *c, double *d)
{
    double sx = 0, sx2 = 0, sx3 = 0, sx4 = 0, sx5 = 0, sx6 = 0;
    double sy = 0, sxy = 0, sx2y = 0, sx3y = 0;

    for (int i = 0; i < N; i++)
    {
        double x = tahun[i];
        double y = populasi[i];
        double x2 = x * x;
        double x3 = x2 * x;
        double x4 = x3 * x;
        double x5 = x4 * x;
        double x6 = x5 * x;

        sx += x;
        sx2 += x2;
        sx3 += x3;
        sx4 += x4;
        sx5 += x5;
        sx6 += x6;

        sy += y;
        sxy += x * y;
        sx2y += x2 * y;
        sx3y += x3 * y;
    }

    double A[4][5] = {
        {N, sx, sx2, sx3, sy},
        {sx, sx2, sx3, sx4, sxy},
        {sx2, sx3, sx4, sx5, sx2y},
        {sx3, sx4, sx5, sx6, sx3y}};

    // Gauss-Jordan Elimination
    for (int i = 0; i < 4; i++)
    {
        double pivot = A[i][i];
        for (int j = 0; j < 5; j++)
            A[i][j] /= pivot;

        for (int k = 0; k < 4; k++)
        {
            if (k != i)
            {
                double faktor = A[k][i];
                for (int j = 0; j < 5; j++)
                {
                    A[k][j] -= faktor * A[i][j];
                }
            }
        }
    }

    *d = A[0][4];
    *c = A[1][4];
    *b = A[2][4];
    *a = A[3][4];
}

// Fungsi untuk hitung koefisien regresi kubik untuk persentase internet
void hitung_koefisien_internet(double *a, double *b, double *c, double *d)
{
    // Hanya gunakan data dari tahun 1994 ke atas (ketika internet mulai ada)
    double sx = 0, sx2 = 0, sx3 = 0, sx4 = 0, sx5 = 0, sx6 = 0;
    double sy = 0, sxy = 0, sx2y = 0, sx3y = 0;
    int count = 0;

    for (int i = 0; i < N; i++)
    {
        // Mulai dari data tahun 1994 (ketika persentase > 0)
        if (tahun[i] >= 1994)
        {
            double x = tahun[i];
            double y = persentase[i];
            double x2 = x * x;
            double x3 = x2 * x;
            double x4 = x3 * x;
            double x5 = x4 * x;
            double x6 = x5 * x;

            sx += x;
            sx2 += x2;
            sx3 += x3;
            sx4 += x4;
            sx5 += x5;
            sx6 += x6;

            sy += y;
            sxy += x * y;
            sx2y += x2 * y;
            sx3y += x3 * y;
            count++;
        }
    }

    double A[4][5] = {
        {count, sx, sx2, sx3, sy},
        {sx, sx2, sx3, sx4, sxy},
        {sx2, sx3, sx4, sx5, sx2y},
        {sx3, sx4, sx5, sx6, sx3y}};

    // Gauss-Jordan Elimination
    for (int i = 0; i < 4; i++)
    {
        double pivot = A[i][i];
        for (int j = 0; j < 5; j++)
            A[i][j] /= pivot;

        for (int k = 0; k < 4; k++)
        {
            if (k != i)
            {
                double faktor = A[k][i];
                for (int j = 0; j < 5; j++)
                {
                    A[k][j] -= faktor * A[i][j];
                }
            }
        }
    }

    *d = A[0][4];
    *c = A[1][4];
    *b = A[2][4];
    *a = A[3][4];
}

// Fungsi prediksi nilai
double prediksi(double a, double b, double c, double d, int x)
{
    return a * x * x * x + b * x * x + c * x + d;
}

int main()
{
    baca_file_csv("DataTugasPemrogramanA.csv");

    double a_pop, b_pop, c_pop, d_pop; // Koefisien untuk populasi
    double a_int, b_int, c_int, d_int; // Koefisien untuk persentase internet

    hitung_koefisien_populasi(&a_pop, &b_pop, &c_pop, &d_pop);
    hitung_koefisien_internet(&a_int, &b_int, &c_int, &d_int);

    int tahun_estimasi[] = {2005, 2006, 2015, 2016};

    printf("==== PREDIKSI POPULASI ====\n");
    printf("Koefisien regresi kubik populasi: a=%g, b=%g, c=%g, d=%g\n", a_pop, b_pop, c_pop, d_pop);

    for (int i = 0; i < 4; i++)
    {
        int t = tahun_estimasi[i];
        double y = prediksi(a_pop, b_pop, c_pop, d_pop, t);
        printf("Prediksi populasi tahun %d = %.0f\n", t, y);
    }

    printf("\n==== PREDIKSI PERSENTASE PENGGUNA INTERNET ====\n");
    printf("Koefisien regresi kubik internet: a=%g, b=%g, c=%g, d=%g\n", a_int, b_int, c_int, d_int);

    for (int i = 0; i < 4; i++)
    {
        int t = tahun_estimasi[i];
        double y = prediksi(a_int, b_int, c_int, d_int, t);
        // Pastikan persentase tidak negatif
        if (y < 0)
            y = 0;
        printf("Prediksi persentase pengguna internet tahun %d = %.2f%%\n", t, y);
    }

    return 0;
}
