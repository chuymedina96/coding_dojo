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
            // Primitive c# data types.
                // string name = "Todd";
                // int age = 32;
                // double height = 1.875;
                // bool blueEyed = true;
                // This is a headache! Why is C# strongly typed?
                // One word: Performance

                // Although loosely typed languages may be easier for the developer initially, it reduces performance because the computer has to worry about remembering types and how to store different values of different types. In addition, the computer now has to allocate extra space for each variable and it has to store them in such a way that the variable can hold any type of information. Because C# is strongly typed, it forces the developer to be more conscious about types and allows the computer to run more efficiently by allocating just enough space for each variable.

            // Conditionals
                //Declare a variable called rings that is of the Int Type
                // int numRings = 5;
                // if (numRings >= 5)
                // {
                //     Console.WriteLine("You are welcome to join the party");
                // }
                // else if (numRings > 2)
                // {
                //     Console.WriteLine($"Decent...but {numRings} rings aren't enough");
                // }
                // else
                // {
                //     Console.WriteLine("Go win some more rings");
                // }

                // We can use Logical Operators in our Conditionals as well. Let's say we want to change the criteria for entering our NBA Legends party. Let's say you have to have at least 5 rings AND have the name Kobe to enter the party:
                // int numRings = 5;
                // string name = "Kobe";
                // if (numrings >= 5 && name == "Kobe")
                // {
                // Console.WriteLine($"Welcome to the party {name}, congratulations on your {numRings} championships!");
                // }

                // We can change our criteria and say that you have to have at least 5 rings or more than 3 All-Star appearances.
                // int numRings = 5;
                // int numOfAllStarAppearances = 17;
                // if (numRings >= 5 || numOfAllStarAppearances > 3)
                // {
                // Console.WriteLine("Welcome, you are truly a legend");
                // }

                // // Or we can just let in everyone who is not crazy.
                // bool crazy = true;
                // if (!crazy)
                // {
                //     Console.WriteLine("Let's party!");
                // }

            // Loops
                // Computers are really good at two things: storing information and doing something over and over again. If we want to execute a set of code repeatedly for a given number of iterations or until it reaches a specific condition, we will use loops. There are two basic types of loops: the for loop and the while loop. We use the for loop when we know beforehand how many times we are going to have to repeat the code while we use the while loop when we don't know how many times we have to run the code, but we know we have to run the code until it reaches a particular condition. However, at their core, they are both the same, you can do anything a for loop does with a while loop and vice versa.

                // loop from 1 to 5 including 5
                // for (int i = 1; i <= 5; i++)
                // {
                //     Console.WriteLine(i);
                // }
                // // loop from 1 to 5 excluding 5
                // for (int i = 1; i < 5; i++)
                // {
                //     Console.WriteLine(i);
                // }
                // // You can just as easily use variables to create a range as well!
                // int start = 0;
                // int end = 5;
                // // loop from start to end including end
                // for (int i = start; i <= end; i++)
                // {
                //     Console.WriteLine(i);
                // }
                // // loop from start to end excluding end
                // for (int i = start; i < end; i++)
                // {
                //     Console.WriteLine(i);
                // }

                //The execution section does not always have to use ++
                // for (int i = 1; i < 6; i = i + 1)
                // {
                //     Console.WriteLine(i);
                // }

                // int i = 1;
                // while (i < 6)
                // {
                //     Console.WriteLine(i);
                //     i = i + 1;
                // }

            // Generating Random Values in C#
                Random rand = new Random();
                for(int val = 0; val < 10; val++)
                {
                    //Prints the next random value between 2 and 8
                    Console.WriteLine(rand.Next(1,100));
                }
        }
    }
}
