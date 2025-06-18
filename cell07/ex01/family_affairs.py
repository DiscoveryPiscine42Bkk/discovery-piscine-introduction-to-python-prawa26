def genopum(family):
    return list(filter(lambda name: family[name] == " pum", family.key()))
dupont_family = {
    "pum": "pum",
    "geno": "geno",
    "mairu": "tem",
    "chutinun": "pum",
    "yungmak": "pum",
}
print(genopum(dupont_family))