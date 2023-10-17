#include<stdio.h>

int main()
{
	int i,a[7]={15,17,19,5,2,8,7},b=0;
	for(i=0;i<7;i=i+2){
		if(i%2==0)
			b++;
	}
	printf("%d",b);
	return 0;
}