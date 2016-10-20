#include <stdio.h>
////#include <iostream>
#include <cmath>

double function(double x){
   //------------1--------------
   //return x + exp(x);

   //-------------2------------
   //return x-tan(x);

   //-----------4--------------
   //return (pow(x,3)-25);
   //return 135*x/(1-pow(1+x,-360))-1;
   
   //-------------5--------------
   return (x+1)*(x-3);
}

double deriv(double x){
   //------------1--------------
   //return 1 + exp(x);
   //--------------2-------------
   //return 135/(1-pow(1+x,-360)) - 48600*x/(pow(1+x,361)*(1-pow(1+x,-360)));
   //------------5-------------
   return 0;
}

double g(double x){
   //------------1--------------
   //return -exp(x);

   //----------------3---------
   //const double pi  =3.141592653589793238463;
   //return -2*sin(pi * x);

   //----------------5--------------
   return (pow(x,2)-3)/2;
}

//Assumes that f(a)<0 and f(b)>0
double bisection(double a, double b, int count){
   double mid = (a+b)/2;
   double temp = (mid-a)/a;
   if(!(temp < .01 && temp > -.01)){
      double value = function(a)*function(mid);
      if(value > 0){
         return bisection(mid, b, count+1);
      }else if(value < 0){
         return bisection(a, mid, count+1);
      }else{
         //printf("%s%i\n","Bisection count = ", count);
         return mid;
      }
   }
   printf("%s%i\n","Bisection count = ", count);
   return mid;
}

double fixedPoint(double x1,int count){
   double x2 = g(x1);
   float temp = (x2-x1)/x1;
   printf("%s%f%s%f%s%f%s%f%s", "{", x1," ,", x2, "},{", x2,",",x2, "},");
   //printf("%s%f\n","TEMP = ", temp);
   //printf("%f\n",x2);
   if(!(temp<.01&&temp>-.01)&&count<100){
      //printf("%s%i%s%f\n", "x2 at iteration ",count, " = ",x2) 

      
      return fixedPoint(x2, count+1);
   }
   printf("%s%i\n","Fixed pt count = ", count);
   return x2;
}

double newton(double x0, double x, int count){
   double x1 = x0 - function(x0) / deriv(x0);
   double a = (x1-x0)/x0;
   if(!(a<.001&&a>-.001)){
      //printf("%f\n", x1);
      return newton(x1, x0, count+1);
   }
   printf("%s%i\n","Newton count = ", count);
   return x1;
}

double secant(double x1, double x2, int count){
   x2 = x1 - function(x1)*(x2-x1)/(function(x2)-function(x1));
   double a = (x2-x1)/x1;
   if(!(a<.001&&a>-.001)){
      //printf("%f\n", x1);
      return secant(x2, x1, count+1);
   }  
   printf("%s%i\n", "SECANT count =  ", count);
   return x2;
}

//ASSUME f(a)<0 AND f(b)>0
double falsePos(double a, double b, int count){
   double intersect = a - function(a)*(a-b)/(function(a)-function(b));
   double temp = (intersect-a)/a;
   if(!(temp<.001 && temp > -.001)){
      double value = function(a)*function(intersect);
      if(value > 0){
         return falsePos(intersect, b, count+1);
      }else if(value < 0){
         return falsePos(a, intersect, count+1);
      }else{return intersect;}
   }
   printf("%s%i\n","falsePos count = ",count);
   return intersect;   
}  

//uncomment functions above to match problem number
int main(){
   //PROBLEM 1
   /*
   double bis1 = bisection(-1,0,0);
   printf("%s%f\n","Bisection : ", bis1);
   double fP1 = fixedPoint(-1,0);
   printf("%s%f\n","Fixed Pt : ",fP1);
   double newt1 = newton(-1,0,0);
   printf("%s%f\n","Newtons : ", newt1);
   double sec1 = secant(-1,0,0);
   printf("%s%f\n","Secant: ", sec1);
   double fals1 = falsePos(-1,0,0);
   printf("%s%f\n","False Pos : ", fals1);
   */

   //PROBLEM 2  (a and b have diff functions)
   /*
   double bis2a = bisection(4,4.5,0);
   printf("%s%f\n","Bisection 2a: ", bis2a);
   double bis2b = bisection(2,4,1);
   printf("%s%f\n","Bisection 2b : ", bis2b);
   */

   //PROBLEM 3
   //double fp3 = fixedPoint(-4,0);
   //printf("%s%f\n","fixed Point 3: ", fp3);
   
   //PROBLEM 4
   //double newton3 = newton(-3,1,0);
   //printf("%s%f\n","newton3 = ", newton3);
   
   //PROBLEM 5
   double fixpt5 = fixedPoint(-.9,0);
   printf("%s%f\n", "fixpt5 = ", fixpt5);
   return 0;
}

