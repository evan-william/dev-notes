def main():
    spacecraft = {"name": "Voyager 1"}
    spacecraft["distance"] = 0.01 # Another way to add dictionary instead 
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
    ========= REPORT =========
    Name: {spacecraft["name"]}
    Distance: {spacecraft["distance"]} AU
    =========================
    """

main()

# With get method
def main():
    spacecraft = {"name": "Voyager 1"}
 #  spacecraft.update({"distance": 0.01, "orbit": "Sun"})
    print(create_report(spacecraft))

def create_report(spacecraft): # This Get will print unknown if name doesn't exist
    return f"""
    ========= REPORT =========
    Name: {spacecraft.get("name", "Unknown")} 
    Distance: {spacecraft.get("distance","Unknown")} AU
    Orbit: {spacecraft.get("orbit","Unknown")} 
    =========================
    """

main()
