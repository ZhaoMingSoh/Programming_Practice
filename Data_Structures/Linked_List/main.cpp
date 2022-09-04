#include "singly_linked_list.h"
#include <iostream>

void create_Linked_list(int vals[], int size, Node *first){
    Node *last = first;
    Node *temp = NULL;

    for(int i = 1; i < size; ++i){
        temp = new Node(vals[i], NULL);
        last->ptr_next = temp;
        last = temp;
    }
}

// 1) display Linked-List Iteratively
void display_iteratively(Node *first){
    Node *i = first;
    while(i->ptr_next != NULL){
        std::cout << i->data << std::endl;
        i = i->ptr_next;
    }
}

// 2) display Linked-List Recursively
void display_recursively(Node *first){
    Node *i = first;
    
    if (i->ptr_next != NULL){
        std::cout << i->data << " ";
        display_recursively(i->ptr_next);
    }
}

// Inserting into a linked-list
// 1) Insert a new node before the first node
void Insert_before_first(Node *&first, Node *new_Node){
    new_Node->ptr_next = first;
    first = new_Node;
}

// 2) a) Insert into an arbitrary index position recursively
void Insert_into_arbitrary_position_recursively(Node *first, Node *new_Node, int index_pos, int count, bool f){
    Node *i = first;

    if(i->ptr_next != NULL & f != true){
        if(count == index_pos){
            new_Node->ptr_next = i->ptr_next;
            i->ptr_next = new_Node;
            f = true;
        }
        Insert_into_arbitrary_position_recursively(i->ptr_next, new_Node, index_pos, count + 1, f);
    }
}

// b) Insert into an arbitrary index position iteratively
void Insert_into_arbitrary_position_iteratively(Node *first, Node *new_Node, int index_pos){
    Node *p = first;   
    for(int i=0; i < index_pos - 1; ++i){
        p = p->ptr_next;
    }
    new_Node->ptr_next = p->ptr_next;
    p->ptr_next = new_Node;
}

// Deleting from linked-list
// 1) 

int main(){
    int vals[] = {1,2,3,4,5,6};
    int size = sizeof(vals)/sizeof(*vals);

    Node *first = new Node(vals[0], NULL);
    create_Linked_list(vals, size, first);
    std::cout << "Singly Linked-List : ";
    display_recursively(first);

    std::cout << std::endl;

    Node *new_Node = new Node(0, NULL);
    Insert_before_first(first, new_Node);
    std::cout << "Insert before first node : ";
    display_recursively(first);

    std::cout << std::endl;

    Node *new_Node_2 = new Node(8, NULL);
    Insert_into_arbitrary_position_recursively(first, new_Node_2, 3, 1, false);
    std::cout << "Insert into arbitrary position recursively : ";
    display_recursively(first);

    std::cout << std::endl;

    Node *new_Node_3 = new Node(9, NULL);
    Insert_into_arbitrary_position_recursively(first, new_Node_3, 7, 1, false);
    std::cout << "Insert into arbitrary position recursively: ";
    display_recursively(first);

    std::cout << std::endl;

    Node *new_Node_4 = new Node(11, NULL);
    Insert_into_arbitrary_position_iteratively(first, new_Node_4, 5);
    std::cout << "Insert into arbitrary position iteratively: ";
    display_recursively(first);


    return 0;
}