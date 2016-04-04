/*
    @author: Ben Rodriguez
    @description: Simple temperature converter F to C
*/

public class FtoC
{
    public static void main(String[] args)
    {
        double farenheit = 40;
        double celsius = ((farenheit - 32) / 1.8);
        System.out.println(celsius);
    }
}