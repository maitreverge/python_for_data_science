def NULL_not_found(object: any) -> int:
    current_type = type(object)

    # Extract the type name to make a match/case easier.
    type_name = str(current_type).split("'")[1]

    name = ""
    match type_name:
        case "NoneType":
            name = "Nothing"
        case "float":
            name = "Cheese"
        case "int":
            name = "Zero"
        case "str":
            if object:
                print("Type not Found")
                return 1
            else:
                name = "Empty"
        case "bool":
            name = "Fake"
        case "None":
            name = "Fake"
    
    print(f"{name}: {object} {current_type}")
    
    return 0