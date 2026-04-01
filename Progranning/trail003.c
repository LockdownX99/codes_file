#include <stdio.h>

void greating(void);
int main(void)
{
  greating();
}

void greating(void)
{
  string name = scanf("name? \n");
  printf("hello%s\n", name);
}