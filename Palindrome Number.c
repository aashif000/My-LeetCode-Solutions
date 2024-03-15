bool isPalindrome(int x){
    unsigned long long int rev=0;
    unsigned long long int y=x;
    if(x<0)
    {
        return false;
    }
  while(x>0)
  {
      rev = rev*10 + x%10;
      x/=10;
  }
  return (y==rev);
  
    }
