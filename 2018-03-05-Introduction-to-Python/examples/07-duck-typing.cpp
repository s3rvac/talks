// In C++, templates provide a duck-typing-like behavior.
//
// Based on https://en.wikipedia.org/wiki/Duck_typing#In_C.2B.2B
//
// $ g++ 07-duck-typing.cpp -o 07-duck-typing
// $ ./07-duck-typing

#include <iostream>

class Duck {
public:
	void quack() { std::cout << "quack quack\n"; }
};

class Person {
public:
	void quack() { std::cout << "faked quack quack\n"; }
};

template<typename T>
void in_the_forest(T& duck) {
	duck.quack();
}

int main() {
	Duck duck;
	Person person;

	in_the_forest(duck);   // prints "quack quack"
	in_the_forest(person); // prints "faked quack quack"
}
