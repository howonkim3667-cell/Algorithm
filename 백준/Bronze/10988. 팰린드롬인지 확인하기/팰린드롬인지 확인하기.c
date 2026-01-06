#include <stdio.h>
int check(char arr[], int len){
    int left = 0;
    int right = len;
    while(left <= right){
        
        if(arr[left]!=arr[right]){
            return 0;
        }
        left++;
        right--;
    }
    return 1;
}

int main(void){
    char arr[101];
    int len=0;
    scanf("%s", arr);
    while(arr[len]!='\0'){
        len++;
    }
    
    printf("%d",check(arr, len-1));
    return 0;
}