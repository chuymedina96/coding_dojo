using System;
using System.Collections.Generic;

namespace collections_practice
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            

            // Three Basic Arrays
                // Create an array to hold integer values 0 through 9

                int[] myArray = {0,1,2,3,4,5,6,7,8,9};

                myArray = new int[] {1,2,3,4,5,6,7,8,9};

                foreach(int num in myArray)
                {
                    Console.WriteLine(num);
                }

                // Create an array of the names "Tim", "Martin", "Nikki", & "Sara"

                    string[] names = {"Tim", "Martin", "Nikki", "Sara"};

                    foreach(string name in names)
                    {
                        Console.WriteLine(name);
                    }

                // Create an array of length 10 that alternates between true and false values, starting with true

                    // bool myBoolen = true;
                    // bool[] boolArray = new boolArray{10}; 

            // List of Flavors


                // Create a list of ice cream flavors that holds at least 5 different flavors (feel free to add more than 5!)
                // Output the length of this list after building it
                // Output the third flavor in the list, then remove this value
                // Output the new length of the list (It should just be one fewer!)

                    List<string> iceCream = new List<string>();

                    iceCream.Add("Chocalate");
                    iceCream.Add("Vanilla");
                    iceCream.Add("Cookies and Cream");
                    iceCream.Add("Pistachio");
                    iceCream.Add("Strawberry");
                    iceCream.Add("Oreo");

                    Console.WriteLine(iceCream.Count);

                    Console.WriteLine(iceCream[2]); // This output Cookies and Cream
                    iceCream.RemoveAt(2);

                    foreach(string flavor in iceCream){
                        Console.WriteLine(flavor);
                    }
                    Console.WriteLine(iceCream.Count);

                    // User Info Dictionary

                    // Create a dictionary that will store both string keys as well as string values
                    // Add key/value pairs to this dictionary where:
                    //     each key is a name from your names array
                    //     each value is a randomly select a flavor from your flavors list.
                    // Loop through the dictionary and print out each user's name and their associated ice cream flavor

                    Dictionary<string, string> myDict = new Dictionary<string, string>();

                    myDict.Add("Name", "Oreo");
                    myDict.Add("Name", "Strawberry");
                    myDict.Add("Name", "Pistachio");

                    foreach (var entry in myDict)
                    {
                        Console.WriteLine(entry.Key + " - " + entry.Value);
                    }
        }
    }
}
