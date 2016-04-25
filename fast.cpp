#include <string>
#include <fstream>
#include <unordered_map>
#include <iostream>

using namespace std;

int main(int argc, char** argv) {
    string filename = string(argv[1]);
    unordered_map<string, ofstream> out;
    ifstream in(filename);
    string cur;
    const string from = "From ";
    string mail = "";
    while (getline(in, cur)) {
        if (cur.substr(0, from.size()) == from) {
            int fi = cur.find(' ');
            int se = cur.find(' ', fi+1);
            mail = cur.substr(fi+1, se-fi-1);
           // cerr<<"mail = "<<mail<<"\n";
            if (out.find(mail) == out.end()) {
                out.insert(make_pair(mail, ofstream(mail)));
                //cerr <<"add record, out.sz= "<<out.size()<<"\n";
            }
        }
        if (!mail.empty())
            out[mail] << cur;
    }
    for (auto& i : out)
        i.second.close();
    return 0;
}
