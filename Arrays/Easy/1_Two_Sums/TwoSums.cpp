#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution{
    public :
        // Method 1: Uses 2 forloops and in a forwarding method, we take the difference of each element i to the target value and check if the difference results in it being the element j.
        vector <int> TwoSums(vector<int> &nums, int target){
            vector<int> sum;

            // Idea : take target value - nums[i] for which the reuslt will equal to one of the nums[j] 
            // Signifying that nums[j] is the value
            for(int i = 0; i < nums.size(); i++){
                for(int j = i+1; j < nums.size(); j++){
                    if(nums[j] == (target - nums[i])){
                        sum.push_back(i);
                        sum.push_back(j);
                        return sum;
                    }
                }
            }
            return sum;
        }
        // Method 2 : Take the difference between each element from the number array and the target value and check if the difference exist as element in the hash table.
        //            if not, add the current element into the hash table.
        vector <int> Hashmap_TwoSums(vector<int> &nums, int target){
            unordered_map<int,int> m;
            vector<int> temp;
            for(int i = 0; i < nums.size(); ++i){
                int diff = target - nums[i];
                unordered_map<int,int>::iterator it = m.find(diff);
                if(it != m.end()){
                    temp.push_back(it->second);
                    temp.push_back(i);
                    return temp;
                }
                m[nums[i]] = i;
            }
            return temp;
        }

};

void display(const vector<int> &vec){
    vector<int>::const_iterator it = vec.begin();
    while(it != vec.end()){
        cout << *it << " ";
        it++;
    }
    cout << endl;
}

int main(){
    vector<int> x;
    x.push_back(2);
    x.push_back(7);
    x.push_back(11);
    x.push_back(15);
    x.push_back(4);
    x.push_back(5);

    int target = 9;

    Solution S;

    // Method 1
    vector<int> temp = S.TwoSums(x, target);
    display(temp);

    // Method 2
    vector<int> temp_2 = S.Hashmap_TwoSums(x, target);
    display(temp_2);





    return 0;
}