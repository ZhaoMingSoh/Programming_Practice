#include <iostream>
#include <map>
#include <vector>

using namespace std;

bool canSum(int targetSum, vector<int> &vec, map<int, bool> &memo) {
    int remainder;
    if (memo.find(targetSum)!=memo.end())
        return memo[targetSum];
    if (targetSum == 0)
        return true;
    if (targetSum < 0)
        return false;
    
    for (auto i : vec) {
        remainder = targetSum - i;
        if (canSum(remainder, vec, memo)) {
            memo.emplace(targetSum, true);
            return true;
        }
    }
    memo.emplace(targetSum, false);
    return false;
}

int main(int argc, char * argv[]){
    int targetnum = 300;
    vector<int> numbers = {7,14};
    map<int, bool> map;
    cout << canSum(targetnum, numbers, map) << endl;
    return 0;
}