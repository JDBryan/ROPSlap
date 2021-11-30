#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
int copyData(char *string)
{
    int a;
    int b;
    char c[10];
	char buf[64];
	int d;
	char e[100];
	strcpy(buf, string);
	int f;
	char g[200];
	return (0);
}

int biggerStack(char *string)
{
    char bigBuff[800];
    copyData(string);
    return (0);
}

int main(int argc, char *argv[])
{
	char buffer[1000];
	FILE *file;
    if (argc !=2)
    {
        printf("[*] invalid arguments!\n [*] > %s file_name\n",argv[0]);
        exit(0);
    }
	printf("opening file\n");
	file = fopen(argv[1],"rb");
	if (!file)
	{
		//printf("file not opened %s", strerror(errno));
		fprintf(stderr,"file not opened %s", strerror(errno));
		//printf("error");
		return (0);
	}
	printf("file opened\n");
	fread(buffer, 999,1,file);
	fclose(file);
	copyData(buffer);
	return (0);
}