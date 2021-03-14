using System;

namespace Calculadora
{
    class Program
    {
        static void Main(string[] args)
        {
            Calculadora calc = new Calculadora();

            int num1 = GetValidNumber();
            int num2 = GetValidNumber();

            Console.WriteLine("Please, choose an operator (+,-,*,/)");
            string op = Console.ReadLine();
            if (calc.IsValidOperator(op))
            {
                switch (op)
                {
                    case "+": 
                        Console.WriteLine("Result: " + calc.Add(num1, num2));
                        break;
                    case "-":
                        Console.WriteLine("Result: " + calc.Substract(num1, num2));
                        break;
                    case "*":
                        Console.WriteLine("Result: " + calc.Multiply(num1, num2));
                        break;
                    case "/":
                        Console.WriteLine("Result: " + calc.Divide(num1, num2));
                        break;
                }
            }
            Console.ReadLine();
        }

        static int GetValidNumber()
        {
            Console.WriteLine("Please, write a valid number");
            string num = Console.ReadLine();
            int number = 0;
            while (!int.TryParse(num, out number))
            {
                Console.WriteLine("Wrong value");
                Console.WriteLine("Please, write a valid number");
                num = Console.ReadLine();
            }
            return number;
        }
    }

    class Calculadora
    {
        public int Add(int n1, int n2)
        {
            return n1 + n2;
        }
        public int Substract(int n1, int n2)
        {
            return n1 - n2;
        }
        public int Multiply(int n1, int n2)
        {
            return n1 * n2;
        }
        public int Divide(int n1, int n2)
        {
            return n1 / n2;
        }

        public bool IsValidOperator(string op)
        {
            return op == "+" || op == "-" || op == "*" || op == "/";
        }
    }
}
