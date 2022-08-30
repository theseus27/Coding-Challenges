#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>
using namespace std;

struct node {
    char name;
    node *child1;
    node *child2;
    node *parent;
    int num_children() {
        if (child1 == nullptr)      return 0;
        else if (child2 == nullptr) return 1;
        else                        return 2;
    }
    bool has_parent() {
        return (parent == nullptr) ? false : true;
    }
};

bool valid_str(string &str);
string nodify(node nodes[], string str);
int find_node(node nodes[], char search);
bool no_cycle(node nodes[], node start, vector<char> visited);
string s_expression(node nodes[], node curr, string exp);

int main() {
    vector<string> node_strs;
    string error = "";
    node nodes[26];
    for (int i = 0; i < 26; i++) nodes[i] = {'\0', nullptr, nullptr, nullptr};
    //Read in nodes and validate formatting
    string tree_str;
    cin >> tree_str;
    while (tree_str != "" && error == "") {
            if (!valid_str(tree_str))   error = "E1";
            else {
                node_strs.push_back(tree_str);
                tree_str = "";
                cin >> tree_str;
            }
    } 
    //Check for duplicates
    if (error == "") {
        set<string> node_set(node_strs.begin(), node_strs.end());
        if (node_set.size() != node_strs.size())    error = "E2";
    }
    //Turn strings into nodes
    if (error == "") {
        for (int i = 0; i < node_strs.size(); i++)
            if (error == "")    error = nodify(nodes, node_strs.at(i));
    }
    int nodes_occupied = find_node(nodes, '\0');
    //Find root
    int root = -1;
    if (error == "") {
        for (int i = 0; i < nodes_occupied; i++) {
            if (!nodes[i].has_parent()) {
                if (root != -1) error = "E4";
                else            root = i;
            }
        }
    }
    //Check for cycles
    if (error == "") {
        for (int i = 0; i < nodes_occupied; i++) {
            vector<char> empty_char_vec;
            if (!no_cycle(nodes, nodes[i], empty_char_vec))
                error = "E5";
        }
    }
     //Print result
    if (error == "") {
        //Reorder children
        for (int i = 0; i < nodes_occupied; i++) {
            if (nodes[i].num_children() == 2) {
                node *c1 = nodes[i].child1;
                node *c2 = nodes[i].child2;
                if (c1->name > c2->name) {
                    node *hold = c1;
                    nodes[i].child1 = c2;
                    nodes[i].child2 = hold;
                }
            }
        }
        cout << s_expression(nodes, nodes[root], "") << endl;
    }
    else cout << error;
    return 0;
}

bool valid_str(string &str) {
    if (str.length() != 5)  return false;
    if ((str[0] != '(') || (str[2] != ',') || (str[4] != ')'))  return false;
    char parent = str[1];
    char child = str[3];
    if ((int)parent < 65 || (int)parent > 90 || (int)child < 65 || (int)child > 90)     return false;

    string parsed = "";
    parsed.push_back(parent);
    parsed.push_back(child);
    str = parsed;
    return true;
}

string nodify(node nodes[], string str) {
    int parent_idx = find_node(nodes, str.at(0));
    int child_idx = find_node(nodes, str.at(1));
    node *parent_p, *child_p;
    //Set parent
    if (parent_idx == -1) {
        parent_p = &nodes[find_node(nodes, '\0')];
        parent_p->name = str.at(0);
    } 
    else parent_p = &nodes[parent_idx];
    //Set child
    if (child_idx == -1) {
        child_p = &nodes[find_node(nodes, '\0')];
        child_p->name = str.at(1);
    } 
    else child_p = &nodes[child_idx];
    //Check for errors
    if (parent_p->num_children() == 2)  return "E3";
    if (child_p->has_parent())          return "E5";
    //Link parent and child
    child_p->parent = parent_p;
    if (parent_p->num_children() == 0)  parent_p->child1 = child_p;
    else                                parent_p->child2 = child_p;   
    return "";
}

int find_node(node nodes[], char search) {
    for (int i = 0; i < 26; i++)
        if (nodes[i].name == search) return i;
    return -1;
}

bool no_cycle(node nodes[], node start, vector<char> visited) {
    if (find(visited.begin(), visited.end(), start.name) != visited.end())
        return false;
    visited.push_back(start.name);

    if (start.num_children() == 0)
        return true;
    else if (start.num_children() == 1)
        return no_cycle(nodes, *(start.child1), visited);
    else
        return no_cycle(nodes, *(start.child1), visited) && no_cycle(nodes, *(start.child2), visited);
}

string s_expression(node nodes[], node curr, string exp) {
    exp += "(";
    exp += curr.name;
   if (curr.num_children() == 2) {
        exp = s_expression(nodes, *(curr.child1), exp);
        exp = s_expression(nodes, *(curr.child2), exp);
    } else if (curr.num_children() == 1)
        exp = s_expression(nodes, *(curr.child1), exp);
    exp += ")";
    return exp;
}