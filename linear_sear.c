// liner search 
#include <stdio.h>
int function(int A[],int x, int len){
    int i;
    for(i=0;i<len;i++){
        if(A[i]==x){
            return i;
        }
    }
}
int main(){
    int array[5]={5,64,6,8,4},len,x,result;
    len = 5;
    x = 64;
    result =function(array,x,len);
    printf("%d",array[result]);
    
}