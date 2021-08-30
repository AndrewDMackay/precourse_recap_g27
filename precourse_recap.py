what_flavour = input("What is the most common flavour of Python?")
if what_flavour == "CPython":
    print("Well done! Written in C, this is the most common implementation of Python!")

elif what_flavour == "Jython":
    print("Very good, but not the most common, this falvour is written in Java, and compiles in bytecode.")

elif what_flavour == "IronPython":
    print("Very good, but not the most common, this falvour is implemented in C#.")
    
elif what_flavour == "Brython":
    print("Very good, but not the most common, this falvour runs in browser.")

elif what_flavour == "RubyPython":
    print("Very good, but not the most common, this falvour is a bridge between Python, and Ruby interpreters.")

elif what_flavour == "PyPy":
    print("Very good, but not the most common, this falvour is implemented within Python itself.")

elif what_flavour == "MicroPython":
    print("Very good, but not the most common, this falvour runs on a microcontroller.")
    
else:
    print("Sorry, I don't think that's a flavour of Python...")
