def array_of_names(name_dict):
    full_names = []
    for first, last in name_dict.items():
        full_name = f"{first.capitalize()} {last.capitalize()}"
        full_names.append(full_name)
    return full_names
persons = {
    "sawittcha": "jiamthanunkul",
    "chutinun": "yungmak",
    "geno": "pum",
    "pum": "geno"
}
print(array_of_names(persons))