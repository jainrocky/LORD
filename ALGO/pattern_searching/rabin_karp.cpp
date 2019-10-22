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


vector<intll> findAll(string pattern, string text){
    vector<intll> pos;
    intll pLen = pattern.size();
    intll tLen = text.size();
    int nChars = 256;
    intll pHash = 0;
    intll tHash = 0;
    intll msb_weight = 1;

    for(intll i=0; i<pLen-1; i++)
        msb_weight = ((msb_weight % INT_MAX) * (nChars % INT_MAX)) % INT_MAX;

    ///First window hash code of text and also for pattern
    for(intll i=0; i<pLen; i++)
        pHash = ((( pHash * nChars ) % INT_MAX ) + ( pattern[i] % INT_MAX ) ) % INT_MAX,
        tHash = ((( tHash * nChars ) % INT_MAX ) + ( text[i] % INT_MAX ) ) % INT_MAX;

    ///Checking for 1 to tLen - pLen windows
    for(intll i=0; i<=tLen-pLen; i++){
        intll j=0;
        if(pHash == tHash)
            for(; j<pLen && (text[i+j] == pattern[j]); j++);
        if(j == pLen) pos.push_back(i); /// pattern found
        ///Text Hash code for next window
        tHash = ( ( tHash - (text[i] * msb_weight) % INT_MAX )  * nChars + text[i+pLen] ) % INT_MAX ;
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
    write(inds);
    return 0;
}






















