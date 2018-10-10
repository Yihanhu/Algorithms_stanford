#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>

#define MAX 875714
const char INFILE[]="SCC_test.txt";

struct EDGE
{
  long vertex;
  struct EDGE *next;
};

void fetch_g(struct EDGE **g, struct EDGE **revg);
void print_g(struct EDGE **g);
void DFS_loop(struct EDGE **g, long *f, long *leader);
long DFS(struct EDGE **g,long j,long *t,long *s,long *leader,long *state,long *f);
void refresh_g(struct EDGE **g, long *f);

void main()
{
  struct EDGE **g,**revg,**newg;
  long *f,*leader,j,*count,large,i,index;
  g = (struct EDGE **)calloc(MAX,sizeof(struct EDGE *));
  revg = (struct EDGE **)calloc(MAX,sizeof(struct EDGE *));
  fetch_g(g,revg);
  f = (long *)calloc(MAX,sizeof(long));
  leader = (long *)calloc(MAX,sizeof(long));
  DFS_loop(revg,f,leader);
  refresh_g(g,f);
  DFS_loop(g,f,leader);
  free(f);
  count = (long *)calloc(MAX,sizeof(long));
  for (j=0; j<MAX; j++)
        count[j]=0;
  for (j=0; j<MAX; j++)
        count[leader[j]-1]++;
  for (i=0; i<5; i++)        {
        for (j=0,index=0,large=0; j<MAX; j++)
          if (count[j]>large)        {
                large = count[j];
                index = j;
          }
        printf("%ld\n",large);
        count[index]=0;
  }
}

void fetch_g(struct EDGE **g, struct EDGE **revg)
{
  FILE *fp = fopen(INFILE,"r");
  char line[20], *token;
  long left,right,j,k,n,vertex;
  struct EDGE *node;
  for (j=0; j<MAX; j++)        {
        node = (struct EDGE        *)malloc(sizeof(struct EDGE));
        node->next = NULL;
        g[j] = node;
        node = (struct EDGE        *)malloc(sizeof(struct EDGE));
        node->next = NULL;
        revg[j] = node;
  }
  while (fgets(line,100,fp))        {
        left = atoi(strtok(line," "));
        right = atoi(strtok(NULL," "));
        node = (struct EDGE *)malloc(sizeof(struct EDGE));
        node->next = g[left-1]->next;
        node->vertex = right;
        g[left-1]->next = node;
        node = (struct EDGE *)malloc(sizeof(struct EDGE));
        node->next = revg[right-1]->next;
        node->vertex = left;
        revg[right-1]->next = node;

  }
}

void print_g(struct EDGE **g)
{
  struct EDGE *node;
  long k;
  for (k=0; k<MAX; k++)        {
        printf("%ld\t",k+1);
        for (node = g[k]; node->next; node = node->next)
          printf("%ld\t",node->next->vertex);
        printf("\n");
  }
}

void DFS_loop(struct EDGE **g, long *f, long *leader)
{
  long t,s,*state,j;
  //        Initialization
  state = (long *)calloc(MAX,sizeof(long));
  for (j=0; j<MAX; j++)        {
        leader[j] = 0;
        state[j] = 0;
  }
  t = 0;
  //        Loop
  for (j = MAX-1; j>=0; j--)
        if (state[j]==0)        {
          s = j+1;
          f[j] = DFS(g,j,&t,&s,leader,state,f);
        }
}

long DFS(struct EDGE **g,long j,long *t,long *s,long *leader,long *state,long *f)
{
  long i,k,n;
  struct EDGE *node;
  state[j]=1;
  leader[j] = *s;
  for (node = g[j]; node->next; node=node->next)        {
        k = node->next->vertex;
        if (state[k-1]==0)
          f[k-1]=DFS(g,k-1,t,s,leader,state,f);
  }
  (*t)++;
  return (*t);
}

void refresh_g(struct EDGE **g, long *f)
{
  struct EDGE *g2[MAX], *node;
  long j;
  for (j=0; j<MAX; j++)
        g2[j]=g[j];
  for (j=0; j<MAX; j++)        {
        g[f[j]-1] = g2[j];
        for (node=g[f[j]-1]; node->next; node=node->next)
          node->next->vertex = f[node->next->vertex-1];
  }
}
