/***
                                   _________________________
                                  |                         |           ________________________________________
                                  |_________________________|          |   __   __  __   __   __  ___  __       |
                                  |           * *           |          |  |__  |   |  | | _| |__|  |  |  | |\ | |
                                  |          *@IN*          |          |   __| |__ |__| | \  |    _|_ |__| | \| |
                                  |___________*_*___________|          |________________________________________|
                                  |                         |
                                  |_________________________|

**/

#include<bits/stdc++.h>
#define BOOSTER ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#define REPEAT intll t; cin >> t; for(intll iterator=0; iterator<t; iterator++)
#define BLN 1000000000
#define LKH 100000
#define MLN 1000000
typedef long long intll;
typedef long intl;
using namespace std;
template<typename E>
inline void write(const E &tar, string end="\n"){ cout << tar << end; }
template<typename E, typename L>
inline void write(const E *tar, const L len, string end=" "){ for(L i=0; i<len; i++) cout << tar[i] << end; }
template<typename E>
inline void write(const vector<E> &tar, string end=" "){ for(intll i=0; i<tar.size(); i++) cout << tar[i] << end; }
template<typename E>
inline void read(E &tar){ cin >> tar; }
template<typename E, typename L>
inline void read(E *tar, const L len){ for(L i=0; i<len; i++) cin >> tar[i]; }
template<typename E, typename L>
inline void read(vector<E> &tar, const L len){if(tar.size()>0) for(L i=0; i<tar.size(); i++) cin >> tar[i]; else for(L i=0; i<len; i++){ E temp; cin >> temp; tar.push_back(temp);}}


intll longestSuffix(string pattern, int state, int c){
    if(pattern[state] == c)return state+1;
    for(intll nextState = state; nextState > 0; nextState--){       ///starting with longest suffix  Pk [ Pq(c)
        if(pattern[nextState-1] == c){                              ///checking if last character with the current alphabet
            intll i=0;
            ///checking if all others character is matched or not
            for(; i < (nextState-1) && pattern[i] == pattern[state - (nextState-1) + 1 + i]; i++);
            if(i == nextState-1) return nextState;
        }
    }
    return 0;
}

vector<vector<intll> > buildTransitionTable(string pattern, int pLen){
    int nChars=256;
    vector<vector<intll> > table(pLen+1);
    for(int i=0; i<=pLen; i++) table[i] = vector<intll>(nChars);
    for(int q=0; q<=pLen; q++)
        for(int c = 0; c<nChars; c++)
            table[q][c] = longestSuffix(pattern, q, c);             /// finding next state for transition (q x c) -> Q
    return table;
}

vector<intll> findAll(string pattern, string text){
    vector<intll> pos;
    intll pLen = pattern.size();
    intll tLen = text.size();
    auto table = buildTransitionTable(pattern, pLen);
    intll state = 0;
    for(intll i=0; i<tLen; i++){
        state = table[state][text[i]];
        if(state == pLen) pos.push_back(i-pLen+1);
    }
    return pos;
 }

///Note: case-sensitive

int main(){
    BOOSTER
    ifstream in;
    in.open("../../TEST_DATA/LOREM_IPSUM.txt"); ///Testing data
    string line, text, pattern = "ipsum";

    while(in)
        getline(in, line),
        text += line;

    auto inds = findAll(pattern, text);
//
    write(inds);
    return 0;
}
