#include<bits/stdc++.h>
using namespace std;
#include<ios>
int n;char s[10001];
string turn(string x)
{
	string ans;
	for(int i=0;i<(int)x.size();i++)
	if(x[i]=='\\')ans+="/";
	else ans+=x[i];
	return ans;
}
void make(int step,string path)
{
	string ans;
	if(step==n+1)return;
	printf("Level %d\n",step);
	ans="cd C: & cd ../../../.. & cd "+path+" & mkdir 0";
	system(ans.data());
//	cout<<ans.data()<<endl;
	make(step+1,path+"/0");
	ans="cd C: & cd ../../../.. & cd "+path+" & mkdir 1";
	system(ans.data());
//	cout<<ans.data()<<endl;
	make(step+1,path+"/1");
}
string getpath()
{
	string ans="";
	string File=__FILE__;
	for(int i=0;i<(int)File.size()-27;i++)
	ans+=__FILE__[i];
	return ans;
}
int main()
{
	system("mkdir 二叉树结构");
	string path=turn(getpath());path+="/二叉树结构";
	scanf("%d",&n);
	make(1,path);
}
