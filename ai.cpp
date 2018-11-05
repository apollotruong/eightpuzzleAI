#include <iostream>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <iostream>

using namespace std;

vector<vector <int> > puzzle;
vector< vector <vector<int> > > repeats;


void intro(){
    puzzle.resize(3);
    cout << "Enter an input Matrix 3x3. 9 Numbers separated by SPACE " << endl;
    for(int i = 0; i < puzzle.size(); i++){
        for(int j = 0; j < puzzle.size(); j++){
            int input;
            cin >> input;
            cout << ' ';
            puzzle.at(i).push_back(input);
        }
    }
}

// Initializes an empty puzzle
void emptyPuzzleInit(vector<vector <int> > &v){
    v.resize(3);
    for(int i = 0; i < v.size(); i++){
        v[i].resize(3);
    }
}

void puzzleInit(vector<vector <int> > &v, vector<int> nums){
    unsigned counter = 0;
    for(int i = 0; i < v.size(); i++){
        for(int j = 0; j < v.size(); i++, counter++){
            v[i][j] = nums[counter];
        }
    }
}

// Prints Puzzle
void printPuzzle(vector<vector <int> > &v){ 
    for(int i = 0; i < v.size(); i++){
        for(int j = 0; j < v[i].size(); j++){
            cout << v[i][j] << ' ';
        }
        cout << endl;
    }
}
struct edge;
struct vertex{
    vector<vector<int> > state;
    vector<edge> parent;
    vector<edge> child;
    int hn; 
    // heuristic hn =
    // uniform cost search = 0
    // A* Misplaced Tile Heuristic
    // A* Manhattan distance
};

struct edge{
    vector<vertex> vertexes;
    int gn; // gn is weight
};




unsigned locateZeroRow(vector<vector <int> > &v){
    for(unsigned i = 0; i < v.size(); i++){
        for(int j = 0; j < v.size(); j++){
            if(v[i][j] == 0){
                return i;
            }
        }
    }
    return -1;
}

unsigned locateZeroCol(vector<vector <int> > &v){
    for(unsigned i = 0; i < v.size(); i++){
        for(int j = 0; j < v.size(); j++){
            if(v[i][j] == 0){
                return j;
            }
        }
    }
    return -1;
}

// }

int moveRight(vector<vector <int> > &v){
    unsigned posCol = locateZeroCol(v);
    unsigned posRow = locateZeroRow(v);
    if(posCol < 2){
        swap(v[posRow][posCol], v[posRow][posCol+1]);
        return 1;
    }
    return 0;
}
int moveLeft(vector<vector <int> > &v){
    unsigned posCol = locateZeroCol(v);
    unsigned posRow = locateZeroRow(v);
    if(posCol > 0){
        swap(v[posRow][posCol], v[posRow][posCol-1]);
        return 1;
    }
    return 0;
}
int moveUp(vector<vector <int> > &v){
    unsigned posCol = locateZeroCol(v);
    unsigned posRow = locateZeroRow(v);
    if(posRow > 0){
        swap(v[posRow][posCol], v[posRow+1][posCol]);
        return 1;
    }
    return 0;
}
int moveDown(vector<vector <int> > &v){
    unsigned posCol = locateZeroCol(v);
    unsigned posRow = locateZeroRow(v);
    if(posRow < 2){
        swap(v[posRow][posCol], v[posRow-1][posCol]);
        return 1;
    }
    return 0;
}

bool isSolution(vector<vector <int> > &v){
    int counter = 1;
    for(int i = 0; i < v.size(); i++){
        for(int j = 0; j < v.size(); j++)
            if(v[i][j] != counter){
                cout << v[i][j] << endl;
                cout << "false" << endl;
                return false;
            }
            else{
                counter++;
                if(counter == 9){
                    counter = 0;
                }
            }
    }
    cout << "tru" << endl;
    return true;
}

bool isValid(string a, vector<vector <int> > &v){
    unsigned posCol = locateZeroCol(v);
    unsigned posRow = locateZeroRow(v);
    if(a == "up"){
        if(posRow > 0){
            return true;
        }
    }
    if(a == "down"){
        if(posRow < 2){
            return true;
        }
    }
    if(a == "left"){
        if(posCol > 0){
            return true;
        }
    }
    if(a == "right"){
        if(posCol < 2){
            return true;
        }
        
    }
    return false;
}

bool isRepeat(vector< vector <vector<int> > > a, vector< vector<int> > &v){
    bool repeatcheck = false;
    for(int i = 0; i < a.size();i++){
        for(int j = 0; j < v[j].size(); j++){
            for(int k = 0; k < v[k].size(); k++){
                if(v[j][k] == a[i][j][k]){
                    repeatcheck = true;
                }
            }
        }
    }
    return repeatcheck;
}

void astar(unsigned heuristic, vertex vert){
    // using uniform cost search where f(n) = g(n) + <heuristic>(0)
    if(heuristic == 1){
        uniformCostSearch(vert)
    }

}

void uniformCostSearch(vertex vert){
    while(!isSolution(puzzle)){

    }
}



int main(){
    intro();

    cout << "Choose Heuristic\n" 
        << "Uniform Cost Search\n"
        << "Misplaced Tile Search\n"
        << "Manhattan Distance Search\n";
    
    vertex verto
    astar(verto);

    cout << endl;
    printPuzzle(puzzle);

    cout << isSolution(puzzle) << endl;
    


    return 0;
}
