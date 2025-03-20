#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>

struct BankAccount{
    int AccountID;
    char AccountName[100];
    char Phone_num[11];
    char City[25];
    int Balance;
};

void createAccount(struct BankAccount **bankacc, int *count){
    srand(time(NULL));
    int min = 10000000;
    int max = 99999999;
    (*count)++;
    *bankacc = (struct BankAccount *)realloc(*bankacc, (*count)*sizeof(struct BankAccount));
    if(bankacc==NULL){
        printf("Memmory Allocation Failed!");
        exit(1);
    }

    printf("Enter Name : ");
    scanf(" %[^\n]",(*bankacc)[*count-1].AccountName);
    printf("Enter Phone Number : ");
    scanf("%s",&(*bankacc)[*count-1].Phone_num);
    printf("Enter City Name : ");
    scanf(" %[^\n]",(*bankacc)[*count-1].City);
    printf("How many money do you want add : ");
    scanf("%d",&(*bankacc)[*count-1].Balance);

    int accountid = (rand() % (max - min + 1)) + min;
    printf("\nYour Account Number : %d",accountid);
    (*bankacc)[*count-1].AccountID = accountid;

    free(bankacc);
}

void displayAllAccount(struct BankAccount *bankacc, int count){

    printf("Bank Account :------------------");
    for(int i=0; i<count; i++){
        printf("\nAccount Number : %d",bankacc[i].AccountID);
        printf("\nAccount Name : %s",bankacc[i].AccountName);
        printf("\nAccount Phone No. : %s",bankacc[i].Phone_num);
        printf("\nAccount City : %s",bankacc[i].City);
        printf("\nTotal Balance : %d",bankacc[i].Balance);
        printf("\n------------------------------\n");
    }

}

void displayBySearch(struct BankAccount *bankacc, int count){
    int accno;
    printf("\nEnter Account Number :");
    scanf("%d",&accno);
    int accountfound = 0;
    for(int i=0; i<count; i++){
        if(accno == bankacc[i].AccountID){
            printf("\nAccount Found :-\n");
            printf("AccountID : %d\n",bankacc[i].AccountID);
            printf("Name : %s\n",bankacc[i].AccountName);
            printf("Phone No : %s\n",bankacc[i].Phone_num);
            printf("City : %s\n",bankacc[i].City);
            printf("Balance : %d\n",bankacc[i].Balance);
            accountfound = 1;
            return;
        }
    }
    if(!accountfound){
        printf("\n%d Account not found!...",accno);
    }
}

void deposit(struct BankAccount *bankacc, int count){
    int accno;
    printf("\nEnter account no : ");
    scanf("%d",&accno);
    int accounfound = 0;
    for(int i=0; i<count; i++){
        if(accno == bankacc[i].AccountID){
            printf("Account Found :---\n");
            printf("Name : %s\n",bankacc[i].AccountName);
            printf("Current Balance : %d\n",bankacc[i].Balance);

            int depoitMoney;
            printf("\nEnter Deposit Money : ");
            scanf("%d",&depoitMoney);

            bankacc[i].Balance+=depoitMoney;
            printf("\nNew Balance : %d",bankacc[i].Balance);
            accounfound = 1;
            break;
        }
    }
    if(!accounfound){
        printf("\n%d not found account\n",accno);
    }
}

void withdraw(struct BankAccount *bankacc, int count){
    int accno;
    printf("\nEnter Account No. : ");
    scanf("%d",&accno);
    int accountfound = 0;
    for(int i=0; i<count; i++){
        if(accno == bankacc[i].AccountID){
            printf("\nName : %s",bankacc[i].AccountName);
            printf("\nCurrent Balance : %d",bankacc[i].Balance);
            int withdraw_moeny;
            printf("\nEnter Money For Withdraw : ");
            scanf("%d",&withdraw_moeny);
            
            bankacc[i].Balance-=withdraw_moeny;
            printf("\nNew Balance : %d",bankacc[i].Balance);
            accountfound = 1;
            break;
        }
    }
    if(!accountfound){
        printf("\n%d Account not found!...",accno);
    }
}

void tansfer(struct BankAccount *bankacc, int count){
    int send_money_acc_id;
    printf("\nEnter Account Number Who Send Money : ");
    scanf("%d",&send_money_acc_id);
    int recive_money_acc_id;
    printf("Enter Account Number Who Recive Money : ");
    scanf("%d",&recive_money_acc_id);
    int accountfound = 0;

    for(int i=0; i<count; i++){
        if(send_money_acc_id == bankacc[i].AccountID){
            for(int j=0; j<count; j++){
                if(recive_money_acc_id == bankacc[j].AccountID){
                    int money_send;
                    printf("\nEnter Money To Send %s : ",bankacc[j].AccountName);
                    scanf("%d",&money_send);
                    if(money_send <= bankacc[i].Balance){
                        bankacc[j].Balance+=money_send;
                        bankacc[i].Balance-=money_send;
                        printf("\nSender :- \t%s New Balance : %d",bankacc[i].AccountName,bankacc[i].Balance);
                        printf("\nReciver :- \t%s New Balance : %d\n",bankacc[j].AccountName,bankacc[j].Balance);
                        accountfound = 1;
                        break;
                    }else{
                        for(int i=0; i<count; i++){
                            if(send_money_acc_id == bankacc[i].AccountID){
                                printf("\n%s Balance : %d \n",bankacc[i].AccountName,bankacc[i].Balance);
                                break;
                            }
                        }
                    }
                }
            }
        }
    }
    if(!accountfound){
        printf("\n%d or %d Account ID not found!...\n",send_money_acc_id,recive_money_acc_id);
    }
}

int main(){
    struct BankAccount *ba = NULL;
    int chocie, accountid;
    int count = 0;

    printf("\n\t\tWelcome Dena Bank\t");
    do{
        printf("\nBank Features :");
        printf("\n1.Create Account\n2.Display All Account\n3.Serach Account By ID\n4.Deposit\n5.Withdraw\n6.Transfer\n7.Exit");
        printf("\n\nEnter your chocie : ");
        scanf("%d",&chocie);

        switch(chocie){
            case 1:
                createAccount(&ba, &count);
                break;
            case 2:
                displayAllAccount(ba,count);
                break;
            case 3:
                displayBySearch(ba,count);
                break;
            case 4:
                deposit(ba,count);
                break;
            case 5:
                withdraw(ba,count);
                break;
            case 6:
                tansfer(ba,count);
                break;
            case 7:
                printf("Exit From Application...");
                break;

            default:
                printf("\nInvalid Number, try again...");
                break;
        }

    }while(chocie!=7);

    return 0;
}