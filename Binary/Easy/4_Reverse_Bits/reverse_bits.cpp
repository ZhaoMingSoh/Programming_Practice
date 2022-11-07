#include <iostream>
#include <vector>
#include <cmath>

uint32_t reverseBits(uint32_t n) {
    
    std::vector<int> reverse(32,0);
    int count = 0;
    while(n != 0){
        reverse.at(count) = n % 2;
        n /= 2;
        count++;
    }

    uint32_t sum = 0;
    int exponent = 31;
    for(int i = 0; i < 32; ++i){
        sum += (uint32_t) (reverse[i] * pow(2,exponent));
        exponent --;
    }
    
    return sum;
}

int main(int argc, char * argv[]){
    std::cout << reverseBits(43261596) << std::endl;
    return 0;
}