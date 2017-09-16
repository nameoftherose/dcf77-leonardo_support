g++ -std=c++11 -o main main.cpp  
./main -vddys -i 1 -I dcf.log  
sed -n '/DCF/,$p' ~/dcf.log |./main -vddys -i 1  
