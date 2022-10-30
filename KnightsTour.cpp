#include<bits/stdc++.h>
using namespace std;

bool isItSafe(vector<vector<int> > &grid, int row, int col, int n) {

    return row >= 0 and col >=0 and row < n and col < n and grid[row][col] == -1;
}

void display(vector<vector<int> > &grid, int n) {

    for(int i = 0; i < n; i++) {

        for(int j = 0; j < n; j++) {

            cout << grid[i][j] << " ";
        }
        cout << endl;
    }
}

void nKnights(vector<vector<int> > &grid, int row, int col, int count, int n) {

    if(count == n * n) {

        grid[row][col] = count;
        display(grid, n);
        cout<<"\n\n";
        grid[row][col] = -1;
        return;
    }

    if(count > n * n) {

        return;
    }

    int xdir[] = {-2, -1, -2, -1, 1, 2, 2, 1};
    int ydir[] = {1, 2, -1, -2, 2, 1, -1, -2};

    grid[row][col] = count;
    for(int i = 0; i < 8; i++) {

        if(isItSafe(grid, row + xdir[i], col + ydir[i], n)) {

            nKnights(grid, row + xdir[i], col + ydir[i], count + 1, n);
        }
    }

    grid[row][col] = -1;
}

int main() {

    int n = 5;
    vector<vector<int> > grid(n, vector<int> (n, -1));

    nKnights(grid, 0, 0, 1, n);

    return 0;
}
