#include <time.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define N 10
#define SOL 0
#define MER 1
#define VEN 2
#define TIE 3
#define MAR 4
#define JUP 5
#define SAT 6
#define URA 7
#define NEP 8
#define PLU 9
#define idt 37 
#define last 252
#define PI 3.14159265

double data[7*10];

double px[N][last*idt];
double py[N][last*idt];
double pz[N][last*idt];
double vx[N][last*idt];
double vy[N][last*idt];
double vz[N][last*idt];
double masa[N];

double vxHalf[N][last*idt];
double vyHalf[N][last*idt];
double vzHalf[N][last*idt];
double axi[N];
double ayi[N];
double azi[N];


double delta[3];
double mod;


void resta(int b, int a, int ins);
int imprimirDatos(char s[]);
void cargar();
void imprimirIniciales(char s[]);
void imprimirOrbita(char s[], int obj);
void calVel2(int obj,int ins);
void calVel3(int obj,int ins);
void calPos2(int obj,int ins);
void calAcel2(int obj, int ins);

FILE *arc;
int i = 0;
int j = 0;
int k = 0;
double dt;
double G;

int main(){
    
arc = fopen("coordinates.csv", "r");
if(arc){
        
         const size_t tam = 10000;
         char* linea = malloc(tam);
         while (fgets(linea, tam, arc) != NULL) 
		{
			char *recorte = strtok(linea, ",");  
			while (recorte != NULL)
			{
                if(i%8 !=0){ 
			      	double temp = strtod(recorte, NULL);
			      	data[i] = temp;
                  }
				recorte = strtok(NULL, ","); 
				i += 1;
			}
		}
		free(linea); 
fclose(arc);        
         
} 
    

cargar();


for(i = N-1; i>=0; i--){
      masa[i] = masa[i]/masa[0];
      }


dt = 1.0/idt;
G = 4*PI*PI;


for(i = 0; i<last*idt-1;i++){
      for(j = 0;j<N;j++){
      calAcel2(j,i);     
      }
      
      for(j = 0;j<N;j++){
            calVel2(j,i);
                        }
      
      for(j = 0;j<N;j++){
            calPos2(j,i);      
                  }      
                  
      for(j = 0;j<N;j++){
            calAcel2(j,i+1);      
      }
      
      for(j = 0;j<N;j++){
            calVel3(j,i);      
                  }     
                  
}


imprimirOrbita("sol.txt", 0);
imprimirOrbita("mercurio.txt", 1);
imprimirOrbita("venus.txt", 2);
imprimirOrbita("tierra.txt", 3);
imprimirOrbita("marte.txt", 4);
imprimirOrbita("jupiter.txt", 5);
imprimirOrbita("saturno.txt", 6);
imprimirOrbita("urano.txt", 7);
imprimirOrbita("neptuno.txt", 8);
imprimirOrbita("pluton.txt", 9);


}

void resta(int b, int a, int ins){

       delta[0] = px[a][ins]-px[b][ins];
       delta[1] = py[a][ins]-py[b][ins];
       delta[2] = pz[a][ins]-pz[b][ins];
       mod = pow((pow(delta[0],2)+pow(delta[1],2)+pow(delta[2],2)),1.5);       
       }
       

int imprimirDatos(char s[]){
    
    FILE *arch =fopen(s,"w+");    
    for(i = 0;i<10;i++){
      for(j = 0;j<7;j++){
            fprintf(arch,"%f ",data[j+8*i+1]);
            }
            fprintf(arch,"\n");
    } 
    
}


void cargar(){
    for(i = 0;i<10;i++){
            masa[i] = data[8*i+1];
            px[i][0] = data[8*i+2];
            py[i][0] = data[8*i+3];
            pz[i][0] = data[8*i+4];
            vx[i][0] = data[8*i+5];
            vy[i][0] = data[8*i+6];
            vz[i][0] = data[8*i+7];
            }
}


void imprimirIniciales(char s[]){
    FILE *arch =fopen(s,"w+");    
    for(i = 0;i<10;i++){
            fprintf(arch,"%f %f %f %f %f %f %f", masa[i], px[i][0], py[i][0], pz[i][0], vx[i][0], vy[i][0], vz[i][0]);
            fprintf(arch,"\n");
    } 
    
}

void imprimirOrbita(char s[], int obj){
    FILE *arch =fopen(s,"w+");    
    for(i = 0;i<idt*last;i++){
            fprintf(arch,"%f %f %f", px[obj][i], py[obj][i], pz[obj][i]);
            fprintf(arch,"\n");
    } 
    
}

void calVel2(int obj,int ins){
       vxHalf[obj][ins] = vx[obj][ins] + 0.5*dt*axi[obj];
       vyHalf[obj][ins] = vy[obj][ins] + 0.5*dt*ayi[obj];
       vzHalf[obj][ins] = vz[obj][ins] + 0.5*dt*azi[obj];
}

void calVel3(int obj,int ins){
       vx[obj][ins+1] = vxHalf[obj][ins] + 0.5*dt*axi[obj];
       vy[obj][ins+1] = vyHalf[obj][ins] + 0.5*dt*ayi[obj];
       vz[obj][ins+1] = vzHalf[obj][ins] + 0.5*dt*azi[obj];
}


void calPos2(int obj, int ins){
       px[obj][ins+1] = px[obj][ins] + dt*vxHalf[obj][ins];
       py[obj][ins+1] = py[obj][ins] + dt*vyHalf[obj][ins];
       pz[obj][ins+1] = pz[obj][ins] + dt*vzHalf[obj][ins];
       }
     

void calAcel2(int obj, int ins){
     
     double axt = 0;
     double ayt = 0;
     double azt = 0;
     for(int i = 0; i<10;i++){
             if(i != obj){
                  resta(obj, i, ins);
                  axt += masa[i]*delta[0]/mod;
                  ayt += masa[i]*delta[1]/mod;
                  azt += masa[i]*delta[2]/mod;
                  }
             }
     
     axi[obj]=G*axt;
     ayi[obj]=G*ayt;
     azi[obj]=G*azt;
     
     
     }
