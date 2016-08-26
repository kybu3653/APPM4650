#include <stdio.h>
#include <iostream>

int linearIntersect(int point[], int slope){ //point[0] = x, point[1]=y
   return point[1] - slope * point[0];
}

int main(){
   
   printf("HELLO \n");
   return 0;
}
