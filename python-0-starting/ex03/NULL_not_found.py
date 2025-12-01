def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing: None <class 'NoneType'>")
        return 0
    elif isinstance(object, float) and object != object:
        print("Cheese: nan <class 'float'>")
        return 0
    elif object is False:
        print("Fake: False <class 'bool'>")
        return 0
    elif object == 0:
        print("Zero: 0 <class 'int'>")
        return 0
    elif object == "":
        print("Empty: '' <class 'str'>")
        return 0
    else:
        print("Type not Found")
        return 1
