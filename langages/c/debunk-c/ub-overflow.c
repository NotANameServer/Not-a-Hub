#include <limits.h>
#include <stdio.h>

void function(int x){
  int old = x ;
  x++ ;
  printf("X is: %d\n", x);
  if(x > old){
    printf("%d > %d\n", x, old);
  }
}

int main(void){
  int x = INT_MAX ;
  function(x);
}
