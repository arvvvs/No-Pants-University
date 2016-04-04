/*
    @author: Ben Rodriguez
    @description: Simple temperature converter from F to C
*/

#import <iostream> 

int main()
{
    double farenheit = 40; // farenheit 
    double celsius = ((farenheit - 32) / 1.8); // conversion formula
    std::cout << celsius << std::endl; // print
}