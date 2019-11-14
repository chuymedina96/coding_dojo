using System;

namespace FirstCSharp
{
    class Program
    {
        static void Main(string[] args)
        {
            // Variable to interpolate
            string place = "Coding Dojo";
            //Interpolated string, note the $
            string message = $"Hello {place}";
            string myName   = "chuy";
            string otherMessage = $"Hello, {myName}";
            // Displaying final message
            Console.WriteLine(message);
            Console.WriteLine("Hello World!");
            Console.WriteLine(otherMessage);
            Console.WriteLine("The value of pi is " + 3.14159);
            Console.WriteLine("My name is {1}, I am " + 28 + " years old", "Tim", "Chuy");
            Console.WriteLine($"My name is {0}, I am " + 28 + " years old", "Tim"); 
        }
    }
}
