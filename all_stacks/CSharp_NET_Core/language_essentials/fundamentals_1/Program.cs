using System;

namespace fundamentals_1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            for(int val =1; val <= 255; val++)
            {
                Console.WriteLine(val);
            }
            for(int i = 1; i <=100; i++)
            {
                if(i % 3 ==0){
                    Console.WriteLine($"Fizz: Muliple of 3: {i}");
                }
                else if(i % 5 ==0){
                    Console.WriteLine($"Buzz: Multiple of 5: {i}");
                }
                if(i % 3 ==0 && i % 5 ==0){
                    Console.WriteLine($"Fizzbuzz: Both multiple of 3 and 5 {i}");
                }
                
            }
        }
    }
}
