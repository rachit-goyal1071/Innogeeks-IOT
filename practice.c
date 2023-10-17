#include <stdio.h>

int main()
{
    char b[26];
    int a[26], c = 0;
    scanf("%s", b);
    
    for (int i = 0; i < 26; i++) {
        a[i] = b[i] - 'A' + 1;
    }
    
    for (int j = 0; j < 26; j++) {
        c = c + a[j];
        printf("%d\n", c);
    }
    
    if (c == 351) {
        printf("yes\n");
    } else {
        printf("No\n");
    }
    
    return 0;
}
