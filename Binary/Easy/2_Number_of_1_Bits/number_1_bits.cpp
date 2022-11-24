#include <iostream>
#include <vector>

// Record the number of 1's in the bit representation of the unsigned 32 bit int val using division and modulo.
int hammingWeight(uint32_t n) {
    int bits_freq = 0;
    while(n != 0){
        // count the remainder that is 1
        if((n % 2) == 1){
            bits_freq ++;
        }
        n /= 2; 
    }
    return bits_freq;
}

// Method 2 : n = n & (n-1) -> The and operation between n and n-1 will turn the least significant bit of 1 of n to become 0 essentially taking it off.
int hammingWeight_2(uint32_t n){
    int bits_freq = 0;
    
    // This process will keep going until the n becomes 0 where no least significant bit of 1 remains, thus we have found all the 1 bits.
    while(n != 0){
        std::cout << n << std::endl;
        n = n & (n-1);
        bits_freq ++;
    }

    return bits_freq;
}

int main(){
    uint32_t n = 7;
    // std::cout << hammingWeight(n) << std::endl;
    std::cout << hammingWeight_2(n) << std::endl;
    return 0 ;
}