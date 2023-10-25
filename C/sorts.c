#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct node{
    int data;
    struct node* fore;
    struct node* next;
}node;

typedef struct list{
    int count;
    node* first;
    node* last;
}list;

node* create_node(int d){
    node* tmp = (node*)malloc(sizeof(node));
    tmp->data=d;
    tmp->fore=tmp->next=NULL;
    return tmp;
}

list* init_list(){
    list* l=(list*)malloc(sizeof(list));
    l->first=l->last=NULL;
    l->count=0;
    return l;
}

void enque(list* l, node* n){
    if(l->count){
        node* tmp=l->last;
        l->last=tmp->next=n;
        n->fore=tmp;
    }
    else
        l->first=l->last=n;
    l->count++;
}

node* deque(list* l){
    node* tmp=l->first;
    if(l->count){
        if(l->count>1)
            l->first=tmp->next;
        else
            l->first=l->last=NULL;
        tmp->next=tmp->next->fore=NULL;   
        l->count--;
        return tmp;
    }
    else return NULL;
}

node* rand_deque(list* l){
    int i = ((rand()+1)%l->count);
    node* n = l->first;
    while(i!=0){
        n=n->next;
        i--;
    }
    if((n->fore==NULL)&&(n->next==NULL))
        l->first=l->last=NULL;
    else if(n->fore==NULL)
        l->first=n->next;
    else if(n->next==NULL)
        l->last=n->fore;
    else{
        n->fore->next=n->next;
        n->next->fore=n->fore;
    }
    n->fore=n->next=NULL;
    l->count--;
    l->first->fore=l->last->next=NULL;
    return n;
}

void print_list(list* l){
    node* n = l->first;
    while(n!=NULL){
//        if(n->fore!=NULL)
//            printf("%d",n->fore->data);
        printf("%d",n->data);
//        if(n->next!=NULL)
//            printf("%d",n->next->data);
        printf(" -> ");
        n=n->next;
    }
    printf("\n");
}

void suffle_list(list* l){
    int c = l->count;
    while(c!=0){
        enque(l,rand_deque(l));
        c--;
    }
    printf("suffle finish\n");
}

void data_swap(node* n1, node* n2){
    int tmp=n1->data;
    n1->data=n2->data;
    n2->data=tmp;
}

void quick_sort(list* l, node* start, node* end){
    node* tmp1; 
    node* tmp2;
    if(start->next==end){
        if(start->data>end->data)
            data_swap(start,end);
    } 
    else if(start!=end){
        tmp1=start->next;
        tmp2=end;
        while(tmp1!=tmp2){
            if(tmp1->data>start->data){
                data_swap(tmp1,tmp2);
                tmp2=tmp2->fore;
            }
            else if(tmp2->data<=start->data){
                data_swap(tmp1,tmp2);
                tmp1=tmp1->next;
            }
            else if((tmp2->data>start->data)&&(tmp1->data<=start->data)){
                tmp1=tmp1->next;
            }
        }
        printf("%d %d ",tmp1->data,tmp2->data);print_list(l);
        data_swap(start, tmp1);
        quick_sort(l,start,tmp2->fore);
        quick_sort(l,tmp2->next,end);
    }
    return;
}

void sorted_check(list* l){
    node* tmp=l->first;
    while(tmp->next!=NULL){
        if(tmp->data>tmp->next->data){
            printf("sort error\n");
            return;
        }
        tmp=tmp->next;
    }
    printf("sorted clear\n");
    return;
}

int main(int argc, char *argv[]){
    list* l =init_list();
    for(int i=0;i<5;i++)
        enque(l,create_node(i));
    suffle_list(l);
    print_list(l);
    quick_sort(l, l->first, l->last);
    print_list(l);
    sorted_check(l);
    return 0;
}