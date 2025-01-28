dicSkills= {
    "Osama": {
        "css": "30",
        "html":"10",
        "python": "94"
    },
    "Betul": {
        "css": "30",
        "html":"10",
        "python": "94"
    },
    "Rasha": {
        "css": "30",
    "html":"10",
    "python": "94"
    }
}
for key, value in dicSkills.items():
    print(key)
    for key, value in value.items():
        print(key, value)
    print("\n")

print("Thanks")
