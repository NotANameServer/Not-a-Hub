#include <stdio.h>

int main(void){
  int x ;
  int err ;
  do {
    err = scanf("%d", &x);
    if(err != 1) scanf ("%*[^\n]");
  } while(err != 1);
  
  printf("Input was: %d\n", x);
}
