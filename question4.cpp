'''Question: Given a string, find the length of the longest repeating subsequence, such that the two
  subsequences don’t have the same string character at the same position, i.e. any ith character in the two subsequences 
  shouldn’t have the same index in the original string.'''
  
class Main {
	public:
		int LongestRepeatingSubsequence(string &str)
    {
		    string t = str;
		    int n = str.size();
		    int v[n+1][n+1];
		    
		    for(int a=0;a<=n;a++){
		        for(int b=0;b<=n;b++){
		            if(a==0 || b==0){
		                v[a][b] = 0;
		            }
		            else if(str[a-1] == a[b-1] && a!=b){
		                v[a][b] = 1 + v[a-1][b-1];
		            }
		            else v[a][b] = max(v[a-1][b],v[a][b-1]);
		        }
		    }
		    return v[n][n];
		}

};
