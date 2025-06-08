#include<stdio.h>
#include<stdlib.h>
#include<string.h>

struct student{
    int rollno;
    char name[85];
    float marks;
};

void addStudent(struct student **students, int *count){
    (*count)++;
    *students = (struct student *)realloc(*students, (*count)*sizeof(struct student));  

    if(students == NULL){
        printf("Memmory Allocation failed!\n");
        exit(1);
    }

    printf("\nEnter Roll No. : ");
    scanf("%d",&((*students)[*count-1].rollno));
    printf("Enter Name : ");
    scanf(" %[^\n]", (*students)[*count - 1].name);
    printf("Enter Marks : ");
    scanf("%f",&((*students)[*count-1].marks));
}

void displayStudent(struct student *students, int count){
    printf("\nStudent List :------\n");
    for(int i=0; i<count; i++){
        printf("Roll no : %d\n",students[i].rollno);
        printf("Name : %s\n",students[i].name);
        printf("marks : %.2f\n",students[i].marks);
        printf("--------------------\n");
    }
}

void searchRoll(struct student *students, int count, int rollno){
    for(int i=0; i<count; i++){
        if(students[i].rollno == rollno){
            printf("\nStudent found :-----\n");
            printf("Rollno : %d\n",students[i].rollno);
            printf("Name : %s\n",students[i].name);
            printf("Marks : %.2f\n",students[i].marks);
            return;
        }
    }
    printf("\n%d roll no student not found!...\n",rollno);
}

int main(){
    struct student *std = NULL;
    int count = 0;
    int chocie, rollno;

    printf("\n\t\tWelcome Bhartiy School.");
    do{
        printf("\n1.add student\n2.display student info\n3.search student by rollno.\n4.exit");
        printf("\n\nEnter your chocie : ");
        scanf("%d",&chocie);

        switch (chocie)
        {
        case 1:
            addStudent(&std,&count);
            break;
        case 2:
            displayStudent(std,count);
            break;
        case 3:
            printf("\nEnter Rollno : ");
            scanf("%d",&rollno);
            searchRoll(std,count,rollno);
            break;
        case 4:
            printf("Exit...");
            break;
        
        default:
            printf("\nEnter valid number");
            break;
        }

    }while(chocie!=4);


    return 0;
}