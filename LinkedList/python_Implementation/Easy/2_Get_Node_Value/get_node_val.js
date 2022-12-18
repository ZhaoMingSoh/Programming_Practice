class Node{
    constructor(val, next = null){
        this.val = val;
        this.next = next;
    }
}

const getNodeVal = (index, head, count) => {
    if (head === null){
        return -1;
    }
    if (count === index){
        return head.val
    }
    let val = getNodeVal(index, head.next, count + 1);
    return val
}

const A = new Node("A");
const B = new Node("B");
const C = new Node("C");
const D = new Node("D");

A.next = B;
B.next = C;
C.next = D;

console.log(getNodeVal(2,A,0));