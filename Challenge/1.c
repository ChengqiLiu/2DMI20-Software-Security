        #include <stdlib.h>
        #include <stdio.h>
        #include <string.h>

        int UserInput(int x){
            char input[16];
            puts("What is the magic word?");
            gets(input); 
            return(x+1);
        }

        void Mainfunction(void){
            puts("That is not the magic word!");
        }

        void Secretfunction(void){
            printf("That is the magic word!");
        }

        int main(void){
            printf("Data addres of the main function: 0x%p\n", (void *)Mainfunction);
            printf("Data address of the secret function: 0x%p\n", (void *)Secretfunction);
            int x;
            x = UserInput(0);
            if(x == 1){
                Mainfunction();
            }
        }