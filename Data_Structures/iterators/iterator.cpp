#include <iostream>
#include <vector>

using namespace std;

void display(const vector<int> &vec){
    cout << '[';
    for(auto const &i : vec){
        cout << i << " ";
    }
    cout << ']' << endl;
}

// The way in which the iterator works is exactly like a pointer, 
// 1) We can index it by doing summation or decrement.
// 2) To look at the content of the iterator, we need to dereference it.
void test_1(const vector<int> &vec){
    cout << "--------------------------------------------------------------------------" << endl;
    auto it = vec.begin(); // set the iterator to the index 0 of the vector

    it ++;
    cout << *it << endl;

    it += 2;
    cout << *it << endl;
    
    it = vec.end() - 1; // set the iterator to the last index of the vector ( reason for - 1 is because the vec.end() return an iterator pass the last index)
    cout << *it << endl;

}

// Use whileloop to traverse through the vector elements via its iterator.
void test_2(vector<int> &vec){
    cout << "--------------------------------------------------------------------------" << endl;
    vector<int>::iterator it = vec.begin();
    while(it != vec.end()){
        cout << *it << " ";
        it++;
    }
    cout << endl;

    // assign all the elements to the value of 1
    it = vec.begin();
    while(it != vec.end()){
        *it = 1;
        cout << *it << " ";
        it++;
    }
    cout << endl;
}

void test_3(vector<int> &vec){
    cout << "--------------------------------------------------------------------------" << endl;
    vector<int>::const_iterator it = vec.begin(); // result in a compiler error because const vector cannot be changed.

    while(it != vec.end()){
        cout << *it << " ";
        it++;
    }
    cout << endl;

    // assign all the elements to the value of 1 -- error because const iterator cannot allow changes
    // it = vec.begin();
    // while(it != vec.end()){
    //     *it = 1;
    //     cout << *it << " ";
    //     it++;
    // }
}


int main(){
    vector<int> vec {1,2,3,4,5,6,7,8};
    display(vec);
    cout << "test 1" << endl;
    test_1(vec);
    cout << "test 2" << endl;
    test_2(vec);
    cout << "test 3" << endl;
    test_3(vec);

    return 0;
}