#include<stdio.h>
#include<conio.h>

int main()
{
  int D,year,week,day;

  printf("enter days :");

  scanf("%d",&D);
  
  year = D/365;

  week = (D%365)/7;

  day = D-((365*year)+(week*7));

  printf("\n years are %d: ",year);

  printf("\n week are %d : ",week);

  printf("\n days are %d : ",day);

  getch();

}












