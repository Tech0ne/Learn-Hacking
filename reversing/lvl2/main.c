#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int is_flag(char *try)
{
    if (try[0] != 'f') return 0;
    if (try[1] != 'l') return 0;
    if (try[2] != 'a') return 0;
    if (try[3] != 'g') return 0;
    if (try[4] != '{') return 0;
    if (try[5] != '8') return 0;
    if (try[6] != '3') return 0;
    if (try[7] != '8') return 0;
    if (try[8] != 'a') return 0;
    if (try[9] != '1') return 0;
    if (try[10] != '4') return 0;
    if (try[11] != '2') return 0;
    if (try[12] != 'f') return 0;
    if (try[13] != '8') return 0;
    if (try[14] != '6') return 0;
    if (try[15] != 'f') return 0;
    if (try[16] != '0') return 0;
    if (try[17] != 'a') return 0;
    if (try[18] != '2') return 0;
    if (try[19] != '6') return 0;
    if (try[20] != '0') return 0;
    if (try[21] != '1') return 0;
    if (try[22] != '2') return 0;
    if (try[23] != '5') return 0;
    if (try[24] != '1') return 0;
    if (try[25] != '6') return 0;
    if (try[26] != '6') return 0;
    if (try[27] != 'b') return 0;
    if (try[28] != '4') return 0;
    if (try[29] != 'e') return 0;
    if (try[30] != '6') return 0;
    if (try[31] != '3') return 0;
    if (try[32] != 'e') return 0;
    if (try[33] != 'e') return 0;
    if (try[34] != 'd') return 0;
    if (try[35] != '5') return 0;
    if (try[36] != '3') return 0;
    if (try[37] != '}') return 0;

    // I know it's not cs, but it works ;)

    return 1;
}

int main(int argc, char **argv)
{
    if (argc > 1)
        if (is_flag(argv[1]))
            printf("Well done, here is your flag : %s\n", argv[1]);
    printf("Yeah, like the flag is inside of me, but I will not display it, lol\n");
    return 0;
}
