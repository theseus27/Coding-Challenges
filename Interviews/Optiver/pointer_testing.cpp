#include <string>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <iostream>
using namespace std;

struct human {
    string name;
    int age;
    string major;
    human *bud;
    void print_friend() {
        cout << (string)bud->name << endl;
    };
};

void func1(vector<human> &people);

int main() {
    human theseus{"theseus", 20, "cs", nullptr};
    vector<human> people = {theseus};
    func1(people);
    cout << people.at(0).name << endl;
    cout << people.size() << endl;
    cout << theseus.bud->name << endl;

    return 0;
}

void func1(vector<human> &people) {
    human marco{"marco", 21, "compsci", (&people[0])};
    marco.bud->name = "Luke";
    (people).push_back(marco);
}
