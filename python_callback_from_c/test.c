#include <stdio.h>

typedef void callback_t(int i);

void callback(int i)
{
  printf("%d\n", i);
}

void call_callback(callback_t func)
{
  func(1);
  func(2);
  func(3);
}

int main()
{
  call_callback(callback);

  return 0;
}
