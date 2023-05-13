#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h> //tolower toupper
#define TRUE 1
#define TEMP_PERCENT    0.30
#define MID_PERCENT     0.30
#define FINAL_PERCENT   0.40
struct student{
    char id[8];
    char name[10];
    double t, m, f;
    double aver;
    struct student *next;
};
void insert();
void edit();
void display();
void write();
void flushBuffer();
double calaverage(struct student *current);
struct student  *head, *prev, *current, *ptrnew, *temp;
FILE *fptr;
int main()
{
    char ch;
    char id[8], name[10];
    double t_score, m_score, f_score;
    head = (struct student *) malloc(sizeof(struct student ));
    head->next = NULL;
    // 讀取「Input3.txt」內學生資料，依照名字英文A~Z排序(只考慮第一個英文字母) 
    if ((fptr = fopen("Input3.txt", "r")) == NULL) {
        puts("File open failed!");
        puts("Create a file!");
        if((fptr = fopen("Output3.txt", "w")) == NULL)
            exit(1);    //非正常運行導致程式中斷
    }
    //依照名字英文A~Z排序(只考慮第一個英文字母)，且計算每位學生的平均成績並印出在終端機。
    
    while(fscanf(fptr, "%s %s %lf %lf %lf", id, name, &t_score, &m_score, &f_score) != EOF){
        ptrnew = (struct student *) malloc(sizeof(struct student ));
        strcpy(ptrnew->id,id);
        strcpy(ptrnew->name,name);
        ptrnew->t=t_score;
        ptrnew->m=m_score;
        ptrnew->f=f_score;
        ptrnew->aver=calaverage(ptrnew);
        prev = head;
        current = prev->next;
        while (current != NULL && ptrnew->name[0] > current->name[0]){
            prev = current;
            current = current->next; 
        }
        ptrnew->next = current;
        prev->next = ptrnew;

    }
    display();

    while (TRUE) {
        printf("\n*****************************************");
        printf("\n* Type 'i' to insert new student's data  *");
        printf("\n* Type 'e' to edit student's data  *");
        printf("\n* Type 'l' to display student's data *");
        printf("\n* Type 'w' to write student's data to file   *");
        printf("\n*****************************************");
        printf("\nplease enter your choice : ");

        ch = tolower(getchar());
        flushBuffer();
        switch (ch) {
            case 'i':
                insert();
                break;
            case 'e':
                edit();
                break;
            case 'l' :
                display();
                break;
            case 'w' :
                write();
                exit(0);
            default  :
                printf("\nPlease select one choice !\n");
         }
    }
    return 0;
}

/**** edit function ****/
void edit(){
    char name[10];
    printf("\nWhich student do you want to modify ? ");
    scanf("%s", name);
    flushBuffer();
    prev = head;
    current=head->next;
    while (current != NULL && strcmp(current->name, name))
        current=current->next; 
    if(current ==NULL) {
        printf("Data is not found\n");
        return;
    }
    /* input new data */
    printf("\nEnter ID            : ");
    scanf("%s", current->id);
    printf("Enter name          : ");
    scanf("%s", current->name);
    printf("Enter Temp Score    : ");
    scanf("%lf", &current->t);
    printf("Enter Mid Score     : ");
    scanf("%lf", &current->m);
    printf("Enter Final Score   : ");
    scanf("%lf", &current->f);
    current->aver=calaverage(current);
    flushBuffer();
    prev->next = current->next;
    temp = current;
    /* new insert algorithm */
    prev = head;
    current = prev->next;
    /*if this node's average is bigger then move to the next node of list*/
    while (current != NULL && temp->name[0] > current->name[0]){
        prev = current;
        current = current->next; 
    }
    /* construct the list */
    temp->next = current;
    prev->next = temp;  
}
/**** list function ****/
void display(){
if(head -> next ==NULL)
        printf("\n list is empty\n");
    else {
        printf("  ID       Name        Temp    Mid     Final   Average \n");
        current = head->next;
        while(current != NULL) {
            printf("  %-7s", current -> id);
            printf("  %-10s", current -> name);
            printf("  %-6.1f", current -> t);
            printf("  %-6.1f", current -> m);
            printf("  %-6.1f", current -> f);
            printf("  %-6.1f", current -> aver);
            printf("\n");
            current = current -> next;
        }
    }
}
void insert()
{
    ptrnew = (struct student *) malloc(sizeof(struct student ));
    printf("\nEnter ID            : ");
    scanf("%s", ptrnew -> id);
    printf("Enter name          : ");
    scanf("%s", ptrnew -> name);
    printf("Enter Temp Score    : ");
    scanf("%lf", &ptrnew -> t);
    printf("Enter Mid Score     : ");
    scanf("%lf", &ptrnew -> m);
    printf("Enter Final Score   : ");
    scanf("%lf", &ptrnew -> f);
    flushBuffer();
    ptrnew->aver=calaverage(ptrnew);
    prev = head;
    current = prev->next;
    while (current != NULL && ptrnew->name[0] > current->name[0]){
        prev = current;
        current = current->next; 
    }
    ptrnew->next = current;
    prev->next = ptrnew;
}
/**** write function ****/
void write(){
    //將每一位學生的資料(包含學期平均成績)輸出到「Output3.txt」
    if((fptr = fopen("Output3.txt", "w")) == NULL) {
        puts("File open failed!");
        exit(1);
    }
    current = (struct student *) malloc(sizeof(struct student));
    current->next = NULL; 
    current = head->next;
    while(current != NULL){
        fprintf(fptr, "%s %s %.2f %.2f %.2f %.2f\n", current->id, current->name, 
                current->t, current->m, current->f, current->aver);
        current = current->next;
    }
    fclose(fptr);
}

void flushBuffer(){
    while (getchar() != '\n')
        continue; 
}

double calaverage(struct student *current)
{
    double avg;
    
    avg = current -> t    * TEMP_PERCENT    +
          current -> m     * MID_PERCENT     +
          current -> f  * FINAL_PERCENT;

    return avg;
    }