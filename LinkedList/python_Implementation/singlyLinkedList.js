class Node {
    constructor(val,next = null){
        this.val = val;
        this.next = next;
    }
}

// Iterative Traversal
const iter_Traversal = (head) => {
    let cur_Node = head;

    while (cur_Node != null){
        console.log(cur_Node.val);
        cur_Node = cur_Node.next;
    }
}

// Recursive Traversal
const recur_Traversal = (head) => {
    if (head == null){
        return
    }
    console.log(head.val);
    recur_Traversal(head.next);
}

const A = new Node('A');
const B = new Node('B');
const C = new Node('C');

A.next = B;
B.next = C;

iter_Traversal(A);
recur_Traversal(A);