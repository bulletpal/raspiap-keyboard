#include <fstream>
#include <iostream>
#include <string>
using namespace std;

int main(){
	ifstream inFile;
	inFile.open("tv_mac");
	string mac;
	if(inFile.good()){
		getline(inFile, mac);
	}
	inFile.close();
	
	inFile.open("ip_addresses");
	string* lines = new string[100];
	int counter = 0;
	if(inFile.good()){
		while(!inFile.eof()){
			getline(inFile, lines[counter]);
			counter++;
		}
	}

	int line = 0;
	for(int i = 0; i < counter; i++){
		if(lines[i].find(mac)!=string::npos){
			line = i;
			break;
		}
	}

	if(line > 1){
		string ip = lines[line-2].substr(21);
		ofstream outFile;
		outFile.open("found_ip");
		if(outFile.good()){
			outFile << ip << endl;
		}
		outFile.close();
	}

	delete [] lines;

	return 0;
}
