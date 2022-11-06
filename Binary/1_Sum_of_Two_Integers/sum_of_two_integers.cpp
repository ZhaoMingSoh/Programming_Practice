#include <iostream>

// Use Binary operators startsing from 1) Xor(^) to simulate the summation without the carries, 2) And(&) to get the carry, 3) << 1 to move the carry to their correct position
int getSum(int a, int b) {
    int xor_sum = 0;
    int carry = 0;
    bool carry_bool = false;

    while(!carry_bool){
        xor_sum = a ^ b;
        carry =(unsigned int) (a & b) << 1;
        if(carry == 0){
            carry_bool = true;
        }
        a = xor_sum;
        b = carry;
    }

    return xor_sum;
}

int main(){
    int a = -5, b = 3;
    std::cout << getSum(a,b) << std::endl;
    return 0;
}