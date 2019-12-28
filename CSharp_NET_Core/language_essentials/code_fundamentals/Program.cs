Using System;
using System.Collections.Generic;

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
                int numRings = 5;
                string name = "Kobe";
                if (numRings >= 5 && name == "Kobe"){
                    Console.WriteLine($"Welcome to the party {name}, congratulations on your {numRings} championships!");
                }

                // We can change our criteria and say that you have to have at least 5 rings or more than 3 All-Star appearances.
                int numRings = 5;
                int numOfAllStarAppearances = 17;
                if (numRings >= 5 || numOfAllStarAppearances > 3){
                    Console.WriteLine("Welcome, you are truly a legend");
                }

                // Or we can just let in everyone who is not crazy.
                bool crazy = true;
                if (!crazy){
                    Console.WriteLine("Let's party!");
                }

            // Loops
                // Computers are really good at two things: storing information and doing something over and over again. If we want to execute a set of code repeatedly for a given number of iterations or until it reaches a specific condition, we will use loops. There are two basic types of loops: the for loop and the while loop. We use the for loop when we know beforehand how many times we are going to have to repeat the code while we use the while loop when we don't know how many times we have to run the code, but we know we have to run the code until it reaches a particular condition. However, at their core, they are both the same, you can do anything a for loop does with a while loop and vice versa.

                // loop from 1 to 5 including 5
                    for (int i = 1; i <= 5; i++)
                    {
                        Console.WriteLine(i);
                    }
                // // loop from 1 to 5 excluding 5
                    for (int i = 1; i < 5; i++)
                    {
                        Console.WriteLine(i);
                    }
                // // You can just as easily use variables to create a range as well!
                    int start = 0;
                    int end = 5;
                // // loop from start to end including end
                    for (int i = start; i <= end; i++)
                    {
                        Console.WriteLine(i);
                    }
                // // loop from start to end excluding end
                    for (int i = start; i < end; i++){
                        Console.WriteLine(i);
                    }

                //The execution section does not always have to use ++
                    for (int i = 1; i < 6; i = i + 1){
                        Console.WriteLine(i);
                    }

                    int i = 1;
                    while (i < 6)
                    {
                        Console.WriteLine(i);
                        i = i + 1;
                    }

            // Generating Random Values in C#
                Random rand = new Random();
                for(int val = 0; val < 10; val++)
                {
                    //Prints the next random value between 2 and 8
                    Console.WriteLine(rand.Next(1,100));
                }

            // Arrays
                // With all programming languages, we often need to combine related values into a collection under a single variable name. With C#, there are quite a few ways we can do this, but the first one we will go over is the array. Arrays in C# are similar to other languages we have worked with, such as JavaScript or Python, in that they are a numerically indexed collection of values. However, unlike these other languages, Arrays in C# must have an exact length that is specified when the array is created, and this length cannot be changed.

                // Declaring an array of length 5, initialized by default to all zeroes
                    int[] numArray = new int[5];

                // Declaring an array with pre-populated values
                // For Arrays initialized this way, the length is determined by the size of the given data
                    int[] numArray2 = {1,2,3,4,6};
                    int[] otherArray ={2,3,4,5,6};
                    int[] anotherOne = {24,242,42,42,2};
                    Console.WriteLine(numArray2);

                // The [ ] brackets denote the Array type, and preceding the brackets we place the type of the values that we will store. Just like all other variables we have created so far, an array in C# must have an associated data type that (like length) is immutable. Anything that is placed inside of the array during or after declaration must conform to this value type. It is possible to declare an array without initialization, but you must use the "new" operator once you do define the array's values.

                    int[] array3; //declared by not initialized
                    array3 = new int[] {1,3,5,7,9}; // once you do initialize the array though, you need the "new int[], then values.
                    int[] arrayOfInts = {1, 2, 3, 4, 5};

                    Console.WriteLine(arrayOfInts[0]);    // The first number lives at index 0.
                    Console.WriteLine(arrayOfInts[1]);    // The second number lives at index 1.
                    Console.WriteLine(arrayOfInts[2]);    // The third number lives at index 2.
                    Console.WriteLine(arrayOfInts[3]);    // The fourth number lives at index 3.
                    Console.WriteLine(arrayOfInts[4]);    // The fifth and final number lives at index 4.

                // We can redefine the value at a particular index as well (once the array has an initial set of values).
                    int[] arr = {1, 2, 3, 4};
                    Console.WriteLine($"The first number of the arr is {arr[0]}"); 
                    arr[0] = 8;
                    Console.WriteLine($"The first number of the arr is now {arr[0]}");
                    // The array has now changed!

                // Iterating through an array

                // It would be quite tedious to move through an array by accessing each index by value; imagine if our array had 1000+ values!! Luckily we can use our knowledge from the last chapter to access each array index with a loop. This process (looping through all array indices) is called iterating.

                // string[] myCars = new string[] { "Mazda Miata", "Ford Model T", "Dodge Challenger", "Nissan 300zx"};
                // // The 'Length' property tells us how many values are in the Array (4 in our example here). 
                // // We can use this to determine where the loop ends: Length-1 is the index of the last value. 
                // for (int idx = 0; idx < myCars.Length; idx++)
                // {
                //     Console.WriteLine($"I own a {myCars[idx]}");
                // }

                // This is good, but because looping through an entire array is a common enough occurrence, C# goes even further. The C# language includes another type of loop called a foreach, for exactly this type of operation. A foreach loop just needs a variable that holds each indexed value of the array temporarily and will loop through all of them from there.

                string[] myCars = new string[] { "Mazda Miata", "Ford Model T", "Dodge Challenger", "Nissan 300zx"}; 

                foreach (string car in myCars)
                {
                    // We no longer need the index, because variable 'car' already represents each indexed value
                    Console.WriteLine($"I own a {car}");
                }
            // Generic Lists
                // If we were looking for something more similar to what we call arrays in languages like JavaScript look no further than Generic Lists, or just simply Lists. Lists are an implementation of linked lists that act very much like the dynamically sizing arrays of these other languages. Once you create a list you are able to freely add and remove things as well as access values by index independent of a declared size. This is because lists, just like arrays in JavaScript, are actually just objects with indexed attributes that act as the values of an array. Lists still need a type associated with them, just as every other variable in C#. To get started with Lists, we just need to be sure to include the class of generics to our project page by adding the following line at the top:

                // using System.Collections.Generic; // add this to top when using lists
                //Initializing an empty list of Motorcycle Manufacturers
                List<string> bikes = new List<string>();
                //Use the Add function in a similar fashion to push
                bikes.Add("Kawasaki");
                bikes.Add("Triumph");
                bikes.Add("BMW");
                bikes.Add("Moto Guzzi");
                bikes.Add("Harley Davidson");
                bikes.Add("Suzuki");
                //Accessing a generic list value is the same as you would an array
                Console.WriteLine(bikes[2]); //Prints "BMW"
                Console.WriteLine($"We currently know of {bikes.Count} motorcycle manufacturers.");

                // Iterating through a list
                    // Similar to how we were able to access a list just as we had accessed an array, we can also iterate through a list exactly as we had with an array. This all goes back to the fact that, though a list is an object it is nice enough to keep attributes reference-able by indexing through the use of [] brackets.

                    //Using our array of motorcycle manufacturers from before
                    //we can easily loop through the list of them with a C-style for loop
                    //this time, however, Count is the attribute for a number of items.
                    Console.WriteLine("The current manufacturers we have seen are:");
                    for (var idx = 0; idx < bikes.Count; idx++){
                        Console.WriteLine("-" + bikes[idx]);
                    }
                    // Insert a new item between a specific index
                    bikes.Insert(2, "Yamaha");
                    //Removal from Generic List
                    //Remove is a lot like Javascript array pop, but searches for a specified value
                    //In this case we are removing all manufacturers located in Japan
                    bikes.Remove("Suzuki");
                    // bikes.Remove("Yamaha");
                    bikes.RemoveAt(0); //RemoveAt has no return value however
                    //The updated list can then be iterated through using a foreach loop
                    Console.WriteLine("List of Non-Japanese Manufacturers:");
                    foreach (string manu in bikes)
                    {
                    Console.WriteLine("-" + manu);
                    }

                // Dictionary Class
                    // A dictionary is the final collection type commonly used in C# that we will discuss. It is implemented very similarly to Lists and also makes use of Generics in its instantiation. The major difference that exists between a list and a dictionary is that dictionary values are not referenced by numerical indexes, but rather key-value pairs. The type of both the key and the value must be specified when initializing a dictionary as such: Dictionary<TKey, TValue>. It also is part of the Generic library, so don't forget to include the using statement from the previous chapter on lists.

                    Dictionary<string,string> profile = new Dictionary<string,string>();
                    //Almost all the methods that exists with Lists are the same with Dictionaries
                    profile.Add("Name", "Speros");
                    profile.Add("Language", "PHP");
                    profile.Add("Location", "Greece");
                    Console.WriteLine("Instructor Profile");
                    Console.WriteLine("Name - " + profile["Name"]);
                    Console.WriteLine("From - " + profile["Location"]);
                    Console.WriteLine("Favorite Language - " + profile["Language"]);

                    // One major difference between Lists and Dictionaries when it comes to interacting with them is iterating through their collections. The way we had been using foreach loops with Lists needs to be changed slightly to work with dictionaries because we are working with key-value pairs instead of incremented indices and values. As such, the temp variable that holds the values and how we work with them must be altered slightly:

                    foreach (KeyValuePair<string,string> entry in profile)
                    {
                        Console.WriteLine(entry.Key + " - " + entry.Value);
                    }

                    // This is okay, but that KeyValuePair<string,string> line looks a little scary. We can clean this up by using a pretty cool technique called type inference. Type inference allows us to not have to directly type the type for the variable, but rather will cause the compiler to infer what the type will be based on the very first value assigned to it. A few out there might be feeling "This is awesome! Why weren't we taught this right away!?" This technique can save some time, but it can also greatly reduce clarity that specifying types provides. It is to be used sparingly when the type of a variable can easily be deduced.

                    //The var keyword takes the place of a type in type-inference
                    foreach (var entry in profile)
                    {
                        Console.WriteLine(entry.Key + " - " + entry.Value);
                    }







            

                








        }
    }
}
