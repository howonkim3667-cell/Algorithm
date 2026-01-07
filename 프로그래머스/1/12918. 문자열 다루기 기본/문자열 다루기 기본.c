#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
bool solution(const char* s) {
    bool answer = false;
    int len =strlen(s);
    if (len==0){
        return answer = false;  
    }
    if ((len == 4) || (6 == len)){
        for(int i = 0; i < len; i++){
            if((s[i] >='0'&& '9'>= s[i])){
                answer = true;
            }else{
                return answer = false;        
            }
        }
    } 
    else{
        return answer = false;}
    return answer;
}