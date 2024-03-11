#include<iostream>
#include<cmath>

using namespace std;

// Loi voi log vi du voi 30 log(30)/log(5) = 2.1  6*5 = 30 6>5
//int trailingZeroes(int A) {
//    int count5 = 0;
//    for(int i=5; i<= A;i+=5){
//        count5  += (floor(log(i)/log(5)));
//        cout<<i<<' '<<log(i)/log(5)<<endl;        
//    }
//    return count5;
//}


//  Dem boi cua 5 25 125 25 = 2   vd 30 /5  = 6  dem 1 lan 25 và 30/25 =1  dem 1 lan 25 tong 2
int countTrailingZeroes(int A) {
    int count = 0;
    for (int i = 5; A / i >= 1; i *= 5) {
        count += A / i;
    }
    return count;
}

int main(){
	int n;
	cin>>n;
	cout<<trailingZeroes(n);
}
