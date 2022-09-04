#include "singly_linked_list.h"
#include <iostream>
#include <vector>

Node::Node(){
    data = 0;
    ptr_next = NULL;
}

Node::Node(int data, Node *ptr_next){
    this->data = data;
    this->ptr_next = ptr_next;
}

Node::~Node(){
    std::cout << "Node is destroyed." << std::endl;
}
