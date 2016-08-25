//Bisection straddles the root between points a and b
//Each step, c is midpoint and then redefined to either a or b
//to maintain root straddling

#include <stdio.h>
#include <iostream>
int function(int value){
   
}  

int main(){
   int a = 0;
   int b = 1;
   int f_a = function(a);
   int f_b = function(b);
   if (f_a*f_b>0){
      printf("Error in choice of a and b \n");
      return 1;
   }
   int c;
   int f_c=1;
   while(f_c!=0){
      c = (a+b)/2;
      f_c = function(c);
      if(f_c*f_a<0){
         b = c;
         f_b = f_c;
      }else if(f_c*f_b<0){
         a = c;
         f_a = f_c;
      }
   }
   
   return 0;
}


 
