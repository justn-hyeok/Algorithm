#include <stdio.h>
#include <string.h>

int main() {
    int t;
    char s[80];
    int score;
    int cnt;

    scanf("%d", &t);

    for (int i = 0; i < t; i++) {
        scanf("%s", s);
        
        score = 0;
        cnt = 1;

        for (int j = 0; j < strlen(s); j++) {
            if (s[j] == 'O') score += cnt++;
            else if (s[j] == 'X') cnt = 1;
        }

        printf("%d\n", score);
    }

    return 0;
}