#include<bits/stdc++.h>
using namespace std;

bool isValid(int i, int j, int n) {
    // Within boundary
    return i >= 0 && i < n && j >= 0 && j < n;
}

int ans = 0;

void ratMaze(vector<vector<int> >& vect, vector<vector<bool> >& visited, int i, int j, int n) {
    
    if(i == n-1 && j == n-1) {
        ans++;
        return;
    }

    if(!isValid(i, j, n)) {
        return;
    }

    visited[i][j] = true;

    if(isValid(i, j + 1, n) && visited[i][j + 1] == false && vect[i][j + 1] == 0) {
        ratMaze(vect, visited, i, j + 1, n);
    }

    if(isValid(i, j - 1, n) && visited[i][j - 1] == false && vect[i][j - 1] == 0) {
        ratMaze(vect, visited, i, j - 1, n);
    }

    if(isValid(i + 1, j, n) && visited[i + 1][j] == false && vect[i + 1][j] == 0) {
        ratMaze(vect, visited, i + 1, j, n);
    }

    if(isValid(i - 1, j, n) && visited[i - 1][j] == false && vect[i - 1][j] == 0) {
        ratMaze(vect, visited, i - 1, j, n);
    }

    visited[i][j] = false;
}

int main() {
    int n;
    cin >> n;

    vector<vector<int> > vect(n, vector<int>(n, 0));
    vector<vector<bool> > visited(n, vector<bool>(n, false));

    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cin >> vect[i][j];
        }
    }

    ratMaze(vect, visited, 0, 0, n);
    cout << ans << endl;

    return 0;
}
