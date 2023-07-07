/*********************************************
 * OPL 22.1.1.0 Model
 * Author: zuzan
 * Creation Date: 28 maj 2023 at 19:38:28
 *********************************************/
 
 
int n = 10; // liczba pielegniarek
int d = 7; // liczba dni
int z = 3; //liczba zmian

range i = 1..n; //pielegniarki
range j = 1..z; //zmiany
range k = 1..d; //dni

//liczba pielegniarek potrzebna na kolejno kazda zmiane w kazdym dniu
int a1 = 3;
int a2 = 3;
int a3 = 2;

//preferencja pielegniarki i-tej na zmiane j-tą w dniu k-tym
int p[i][j][k]=[[[2, 3, 4, 5, 6, 7, 8],  [9, 1, 2, 3, 4, 5, 6],  [7, 8, 9, 1, 2, 3, 4]],
 [[5, 6, 7, 8, 9, 1, 2],  [3, 4, 5, 6, 7, 8, 9],  [1, 2, 3, 4, 5, 6, 7]],
 [[8, 9, 1, 2, 3, 4, 5],  [6, 7, 8, 9, 1, 2, 3],  [4, 5, 6, 7, 8, 9, 1]],
 [[2, 3, 4, 5, 6, 7, 8],  [9, 1, 2, 3, 4, 5, 6],  [7, 8, 9, 1, 2, 3, 4]],
 [[5, 6, 7, 8, 9, 1, 2],  [3, 4, 5, 6, 7, 8, 9],  [1, 2, 3, 4, 5, 6, 7]],
 [[8, 9, 1, 2, 3, 4, 5],  [6, 7, 8, 9, 1, 2, 3],  [4, 5, 6, 7, 8, 9, 1]],
 [[2, 3, 4, 5, 6, 7, 8],  [9, 1, 2, 3, 4, 5, 6],  [7, 8, 9, 1, 2, 3, 4]],
 [[5, 6, 7, 8, 9, 1, 2],  [3, 4, 5, 6, 7, 8, 9],  [1, 2, 3, 4, 5, 6, 7]],
 [[8, 9, 1, 2, 3, 4, 5],  [6, 7, 8, 9, 1, 2, 3],  [4, 5, 6, 7, 8, 9, 1]],
 [[2, 3, 4, 5, 6, 7, 8],  [9, 1, 2, 3, 4, 5, 6],  [7, 8, 9, 1, 2, 3, 4]]];

int c = 3; //liczba zmian, jaka ma wykonac dana pielegniarka w tygodniu

dvar boolean x[i][j][k];

maximize sum(i in i, j in j, k in k)p[i][j][k]*x[i][j][k];

subject to {

	//kazda pielegniarka ma co najwyzej jedna zmiane w danym dniu
	forall(i in i, k in k)
	  sum(j in j)x[i][j][k] <= 1; 
	  
	//pielegniarka nie moze pracowac na pierwszej zmianie tuz po zmianie nocnej  
	forall(i in i, k in 1..(d-1))
		x[i][3][k] + x[i][1][k+1] <= 1;	
		
	//kazda pielegniarka ma co najmniej 1 dzien wolnego w harmonogramie tygodnia
	forall(i in i, j in j)
	  sum(k in k) x[i][j][k] <= 6;
	  
	//dla kazdej zmiany musi zgadzac sie liczba potrzebnych pielegniarek
	forall(k in k)
	  sum(i in i)x[i][1][k]==a1;

	forall(k in k)
	  sum(i in i)x[i][2][k]==a2;

	forall(k in k)
	  sum(i in i)x[i][3][k]==a3; 
	  
	//pielegniarka nie moze wykonywac tej samej zmiany wiecej niz 2 razy pod rzad
	forall(i in i, k in 1..(d-2))
	  x[i][1][k]+x[i][1][k+1]+x[i][1][k+2] <= 2;
	  
	forall(i in i, k in 1..(d-2))
	  x[i][2][k]+x[i][2][k+1]+x[i][2][k+2] <= 2;
	  
	forall(i in i, k in 1..(d-2))
	  x[i][3][k]+x[i][3][k+1]+x[i][3][k+2] <= 2;
	  
	//pielegniarka moze miec co najwyzej 3 zmiany nocne w tygodniu
	forall(i in i)
	  sum(k in k)x[i][3][k] <= 3;
	 
	//kazda pielegniarka musi wykonac co najmniej c zmian w tygodniu
	forall(i in i)
	  sum(j in j, k in k)x[i][j][k] >= c;
	  	 
  
}