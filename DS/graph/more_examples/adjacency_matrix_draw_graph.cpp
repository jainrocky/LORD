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


class Point{
    public:
        int x;
        int y;
        Point(){}
        Point(int x, int y){this->x=x, this->y=y;}
};

class Edge{
    public:
        intll uid;
        intll vid;
        double weight;
        Edge(){}
        Edge(intll u, intll v, double weight=1){this->uid=u, this->vid=v, this->weight=weight;}
};

class Graph{
    private:
        intll nNode;
        vector<vector<intll> > matrix;  /// Adjacency Matrix
        vector<Edge> edge;
    public:
        Graph(intll nNode){
            this->nNode=nNode;
            buildMatrix(this->nNode);
        }
        Graph(vector<Edge> &e){
            this->nNode = e.size();
            buildMatrix(this->nNode);
            for(intll i=0; i<nNode; i++)
                this->addEdge(e[i]);
        }
        void buildMatrix(intll nNode){
            for(intll i=0; i<nNode; i++)
                this->matrix.push_back(vector<intll>(nNode));
        }
        void addEdge(Edge uv){
            if(uv.uid < this->nNode && uv.vid < this->nNode) matrix[uv.uid][uv.vid] = uv.weight, this->edge.push_back(uv);
            else write("Node Range Must be between 0 to "+to_string(nNode-1)), exit(1);

        }
        void printMatrix(intll upto=0){
            upto?true: upto=this->nNode;
            for(intll i=0; i<min(this->nNode, upto); i++){
                for(intll j=0; j<min(this->nNode, upto); j++) write(matrix[i][j], " ");
                write("");
            }
        }
        void maxXY(vector<Point> p, intll &w, intll &h){
            int mw=0, mh=0;
            for(int i=0; i<p.size(); i++){
                if(p[i].x > mh) mh=p[i].x;
                if(p[i].y > mw) mw=p[i].y;
            }
            w=mw, h=mh;
        }
        void draw(vector<Point> p){
            intll width;
            intll height;
            intll pad=4;
            maxXY(p, width, height);
            height += pad;
            width += pad;

            vector<vector<string> > canvas(height);
            for(intll i=0; i<height; i++)
                canvas[i]=vector<string>(width);

            for(intll i=0; i<edge.size(); i++){
                int m_new = 2 * abs(p[edge[i].vid].y - p[edge[i].uid].y);
                int slope_error_new = m_new - abs(p[edge[i].vid].x - p[edge[i].uid].x);
                int x1,y1, x2, y2;
                p[edge[i].uid].x < p[edge[i].vid].x ?
                (x1=p[edge[i].uid].x, x2=p[edge[i].vid].x, y1 = p[edge[i].uid].y , y2 = p[edge[i].vid].y) :
                (x1=p[edge[i].vid].x, x2=p[edge[i].uid].x, y1=p[edge[i].vid].y, y2 = p[edge[i].uid].y);
                if(x1 == x2 || y1 == y2){
                    if(x1 == x2)
                        for(int y=min(y1, y2); y<=max(y2, y1); y++) canvas[x1][y]="*";
                    else
                        for(int x=x1; x<=x2; x++) canvas[x][y1]="*";
                    continue;
                }
                for (int x = x1, y = y1; x <= x2; x++){
                    canvas[x][y]="*";
                    slope_error_new += m_new;
                    if (slope_error_new >= 0){
                        y1 < y2 ? y++ : y--;
                        slope_error_new  -= 2 * abs(p[edge[i].vid].x - p[edge[i].uid].x);
                    }
                }
            }
            for(intll i=0; i<height; i++){
                for(intll j=0; j<width; j++)
                    canvas[i][j]!=""?write(canvas[i][j], " "): write(string(" "), " ");
                write("");
            }
        }
};

int main(){
    BOOSTER
    ///Vertex Coordinate X & Y
    vector<Point> p;
    p.push_back(Point(10, 10));
    p.push_back(Point(10, 30));
    p.push_back(Point(20, 30));
    p.push_back(Point(20, 10));
    p.push_back(Point(30, 20));

    ///Creating graph
    Graph g(5);
    g.addEdge(Edge( 0, 1, 22 ));
    g.addEdge(Edge( 1, 2, 12 ));
    g.addEdge(Edge( 2, 4, 45 ));
    g.addEdge(Edge( 4, 3, 21 ));
    g.addEdge(Edge( 3, 0, 21 ));

    g.draw(p);
    g.printMatrix();

    return 0;
}
