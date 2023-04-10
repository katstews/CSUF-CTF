#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void flag(){
    char flag[128]; 
    FILE *file = fopen("flag.txt","r");  
    fgets(flag, 128, file);  
    puts(flag);
}

int vuln(){
    char password[64]; 
    puts("Enter the password!");  
    gets(password);  
    if(strcmp(password, "thisisnotuseful") == 0){
        puts("okay but where's the flag");
    } else {
        puts("it's not here either");
    }
  
    return 0;
}

int main(){
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
    vuln();
    return 0;
}
