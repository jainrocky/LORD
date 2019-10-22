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



///Key point: Generate longestPrefixTable
intll* longestPrefixTable(string pattern){
    int pLen = pattern.size();
    intll* cache = new intll[pLen];
    cache[0]=0;                             ///No longest prefix for first character.
    int longest=0;                          /// Longest matched till now.
    for(int i=1; i<pLen;){
        if(pattern[i] == pattern[longest])
            cache[i++] = ++longest;
        else
            longest > 0 ? longest = cache[longest-1] : cache[i++]=0;
    }
    return cache;
}

vector<intll> findAll(string pattern, string text){
    vector<intll> pos;
    intll pLen = pattern.size();
    intll tLen = text.size();
    auto prefix  = longestPrefixTable(pattern);
    for(intll j=0, i=0; i<tLen;){
        /// check if pattern character matched? if matched increase both pointers(for text and for pattern)
        if(text[i] == pattern[j]) ++i, ++j;
        /**
            validate if pattern is completely matched in last checking?
            if valid: then "OCCURRED" and reset j to last common match in pattern
            for e.g:
                text: AACAACA (0-6)
                pattern: AACAA (0-4) prefix-table [ 0, 1, 0, 1, 2]
                first occurrence at i - j = 5-5 = `0` for next check, instead of checking from i=1
                we are checking for i=5 and j=2 because `AA` is common before and after `C`.
         */
        if(j == pLen) pos.push_back(i-j), j = prefix[j-1];
        /// if pattern not match then reset the value of j to last common pattern in pattern otherwise move `i`.
        else if(text[i] != pattern[j])
            j > 0 ? j = prefix[j-1]: ++i;
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
