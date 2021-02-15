#include <stdio.h>
int function(int A[],int x, int len){
    int left,right,mid;
    left = 0;
    right = len -1;
    while(left <= right){
        mid = (left+right)/2;
        if(A[mid]==x){
            return mid;
        }else if(A[mid]<x){
            left = mid + 1 ;
        }else{
            right = mid-1;
        }
    }
}
int main(){
    int array[10]={2,4,5,6,7,8,9,10,11,34},len,x,result;
    len = 10;
    x = 6;
    result =function(array,x,len);
    printf("%d",array[result]);
    
}