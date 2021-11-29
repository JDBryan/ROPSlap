#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
int main(int argc, char *argv[], char **envp)
{
	int i;
    printf("%d\n",argc);
    for(i=1;i<argc;i++)
    {
        printf("%s ",argv[i]);
    }
    printf("\n");

    for (char **env = envp; *env != 0; env++)
    {
        char *thisEnv = *env;
        printf("%s\n", thisEnv);
    }
    printf("\n");

	return (0);
}