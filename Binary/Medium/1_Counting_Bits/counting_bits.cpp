#include <iostream>
#include <vector>

// Use a forloop for each value of n and a whileloop to attain the number of 1 bits of each of those value.
std::vector<int> countBits(int n) {
    std::vector<int> res;
    int count_1_bits = 0;

    for(int i=0; i<=n; ++i){
        if(i == 0){
            res.push_back(0);
            continue;
        }
        int temp_i = i;
        while(temp_i != 0){
            if(temp_i % 2 == 1){
                count_1_bits ++;
            }
            temp_i /= 2;
        }
        std::cout << "Count of 1's : " << count_1_bits << std::endl;
        res.push_back(count_1_bits);
        count_1_bits = 0;
    }

    return res;
}

// method 2 : Pass each of the integer i into the 2_number_1_bits() to count the bits of each of them, assign the result into their appropriate index i in the resulting array.
// Time : O(n*log(n)) - An integer x has log x + 1 bits.
// Space : O(n)
int number_1_bits(uint32_t n){
    int num_bits = 0;
    while(n != 0){
        n = n & (n-1);
        num_bits++;
    }
    return num_bits;
}

std::vector<int> countBits_2(int n){
    std::vector<int> count_bits(n+1,0);
    for(int i=0; i<=n; i++){
        count_bits[i] = number_1_bits(i);
    }
    return count_bits;
}

// Intuition : Use previous count to generate count for new integer
// Time : O(n) -  For each integer x, in the range 1 to n, we need to perform a constant number of operations which does not depend on the number of bits in x.
// Space : O(1)
// Ex: n = 3,
//          - x=0,b=1; ans[0+1] = ans[0] + 1 -> [1,1) -> [0,1,_,_]
//                     x++ -> x=1, x<b ? no
//          - x=0,b=2; ans[0+2] = ans[0] + 1 -> [2,3) -> [0,1,1,2]
//                     x++ -> x=1, x<b ? yes and x+b<=n ? yes
//                     ans[1+2] = ans[1] + 1
//                     x++ -> x=2, x<b ? no
//          - x=0,b=4; b <= n ? no, terminate    
std::vector<int> countBits_3(int n) {
    std::vector<int> count_bits(n+1,0);
    int x = 0;
    uint32_t b = 1;

    // [0, b) is calculated
    while (b <= n) {
        // generate [b, 2b) or [b, n) from [0, b)
        while (x < b && x + b <= n) {
            count_bits[x + b] = count_bits[x] + 1;
            ++x;
        }                         
        x = 0; // reset x
        b <<= 1; // b = 2b
    }
                
    return count_bits;
}

// method 4 : using dynamic programming, dp_res[i] = 1 + dp_res[i-offset] -> for each i, check if its MSB is the offset[1,2,4,8,16,32, ..] and use the result from i-offset to get the number of 1 bits for the current i.
std::vector<int> countBits_4(int n) {
    std::vector<int> res(0);
    int offset = 1;

    for(int i = 1; i <= n; ++i){
        if(offset * 2 == i){ // keeps track of the MSB using offset.
            offset = i;
        }
        res.push_back(res[i-offset]);
    }

    return res;
}

int main(int argc, char * argv[]){
    int n = 2;
    std::vector<int> res = countBits_2(n);

    // Iterator
    std::cout << "The bits representation of " << n << " is ";
    std::vector<int>::iterator it = res.begin();
    while(it != res.end()){
        std::cout << *it;
        if(it != res.end()){
            std::cout << " ";
        }
        it++;
    }
    std::cout << std::endl;

    return 0;
}