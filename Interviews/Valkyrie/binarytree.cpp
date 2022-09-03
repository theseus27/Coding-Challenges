#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>


using namespace std;
 
 struct Node{
    int value;
    Node *left;
    Node *right;
 };

Node *createNode(int v, Node *l, Node *r) {
    Node *newnode = new Node;
    newnode->left = l;
    newnode->right = r;
    newnode->value = v;
    return newnode;
}
 
Node *buildTree(std::vector<int> values) {
    Node *root = createNode(values[0], nullptr, nullptr);
    values.erase(values.begin());
    for (int i = 0; i < (int)values.size(); i++) {
        Node *next = createNode(values[i], nullptr, nullptr);
        Node *curr = root;
        bool found = false;
        while(!found) {
            if (curr->value > values[i]) {
                if (curr->left == nullptr) {
                    curr->left = next;
                    found = true;
                }
                curr = curr->left;
            }
            else {
                if (curr->right == nullptr) {
                    curr->right = next;
                    found = true;
                }
                curr = curr->right;
            }
        }
    }
    return root;
}

int findNode(Node *root, int num, vector<Node*> &path, int distance) {
    path.push_back(root);
    if (root->value == num) {
        return distance;
    }
    if (root->left == nullptr && root->right == nullptr) {
        path.pop_back();
        return -1;
    }
    
    if (root->left && root->right) {
        if (findNode(root->left, num, path, distance+1) == -1 && findNode(root->right, num, path, distance+1)== -1) {
            path.pop_back();
            path.pop_back();
            return -1;
        }
        else if (findNode(root->left, num, path, distance+1) == -1)
            return findNode(root->right, num, path, distance+1);
        else if (findNode(root->right, num, path, distance+1) ==-1)
            return findNode(root->left, num, path, distance+1);
    }    
    else if (root->left) {
        return findNode(root->left, num, path, distance+1);
    }
    else if (root->right) {
        return findNode(root->right, num, path, distance+1);
    }
    path.pop_back();
    return -1;
}

int BSTdistance(std::vector<int> values, int nodeA, int nodeB) {
    if (find(values.begin(), values.end(), nodeA) == values.end() || find(values.begin(), values.end(), nodeB) == values.end()) return -1;
    
    Node *root = buildTree(values);
    vector<Node*>path1 = {};
    vector<Node*>path2 = {};
    int d1 = findNode(root, nodeA, path1, 0);
    int d2 = findNode(root, nodeB, path2, 0);
    if (d1 == -1 || d2 == -1) return -1;
    
    return abs(d1 - d2);
}

int main()
{
    std::ofstream fout(std::getenv("OUTPUT_PATH"));

    std::string inputString;
    std::getline(std::cin, inputString);
    inputString.erase(std::remove(inputString.begin(), inputString.end(), ','), inputString.end());
    std::stringstream input(inputString);
    
    std::string vectorInputString;
    std::getline(input, vectorInputString, '{');
    std::getline(input, vectorInputString, '}');
    std::stringstream vectorInput(vectorInputString);
    
    int v;
    std::vector<int> values;
    while (vectorInput >> v)
        values.push_back(v);
    
    int nodeA;
    int nodeB;
    input >> nodeA;
    input >> nodeB;

    fout << BSTdistance(values, nodeA, nodeB);

    fout.close();

    return 0;
}