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

// method 2 : using dynamic programming, dp_res[i] = 1 + dp_res[i-offset] -> for each i, check if its MSB is the offset[1,2,4,8,16,32, ..] and use the result from i-offset to get the number of 1 bits for the current i.
std::vector<int> countBits_2(int n) {
    std::vector<int> res = {0};
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