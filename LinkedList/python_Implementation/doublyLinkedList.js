class Node{
    constructor(val, prev = null, next = null){
        this.val = val;
        this.prev = prev;
        this.next = next;
    }
}

class DoublyLinkedList{
    constructor(){
        this.head = null;
        this.tail = null;
    }

    insertAtHead = (val) => {
        const new_Node = new Node(val);
        if (this.head === null){
            this.head = new_Node;
            this.tail = new_Node;
        }else{
            this.head.prev = new_Node;
            new_Node.next = this.head;
            this.head = new_Node;
        }
    }

    insertAtTail = (val) => { 
        const new_Node = new Node(val);
        if (this.tail === null){
            this.head = new_Node;
            this.tail = new_Node;
        }else{
            this.tail.next = new_Node;
            new_Node.prev = this.tail;
            this.tail = new_Node;
        }
    }
    
    Print = () => {
        if (this.head === null){
            console.log("The Doubly-Linked-List is empty.");
        }else{
            let curr = this.head;
            while(curr !== null){
                console.log(curr.val);
                curr = curr.next;
            }
        }
    }
    
    ReversePrint = () =>{
        if (this.tail === null){
            console.log("The Doubly-Linked-List is empty.");
        }else{
            let curr = this.tail;
            while(curr !== null){
                console.log(curr.val);
                curr = curr.prev;
            }
        }
    }
}

D_LL = new DoublyLinkedList();
D_LL.insertAtHead(2);
D_LL.insertAtTail(5);
D_LL.insertAtHead(10);
D_LL.Print();
D_LL.ReversePrint();

