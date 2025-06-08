#include<stdio.h>

int sum(float a, float b);
int sub(float a, float b);
int mul(float a, float b);
int div(float a, float b);


int main(){

    float a,b;
    char oprator;

    printf("which oprator do you want to use(+,-,*,/) : ");
    scanf("%c",&oprator);
    printf("Enter first value : ");
    scanf("%f",&a);
    printf("Enter second vlaue : ");
    scanf("%f",&b);

    if(oprator=='+'){
        sum(a,b);
    }
    else if(oprator=='-'){
        sub(a,b);
    }
    else if(oprator=='*'){
        mul(a,b);
    }
    else if(oprator=='/'){
        div(a,b);
    }
    else{
        printf("please enter valid oprator!");
    }

    return 0;
}

int sum(float a, float b){
    float c = a + b;
    return printf("value of %.1f + %.1f = %.1f",a,b,c);
}
int sub(float a, float b){
    float c = a - b;
    return printf("value of %.1f - %.1f = %.1f",a,b,c);
}
int mul(float a, float b){
    float c = a * b;
    return printf("value of %.1f * %.1f = %.1f",a,b,c);
}
int div(float a, float b){
    float c = a / b;
    return printf("value of %.2f / %.2f = %.2f",a,b,c);
}