def all_thing_is_obj(object: any) -> int:

    data_structures = ["List", "Tuple", "Set", "Dict"]

    title_type = str(type(object)).split("'")[1].title()

    if title_type in data_structures:
        print(f"{title_type} : {type(object)}")
    elif title_type == "Str":
        print(f"{object} is in the kitchen : {type(object)}")
    else:
        # For `int` data type
        print("Type not found")

    return 42