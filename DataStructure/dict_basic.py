"""
PYTHON DICTIONARY INTERVIEW CHEAT SHEET
-----------------------------------------------------------------------
Property: Ordered (3.7+), Mutable, Unique Keys, Hash-Table Based.

OPERATION      | METHOD            | BIG O    | NOTES
-----------------------------------------------------------------------
Access         | dict[key]         | O(1)     | Constant time lookup.
Insert/Update  | dict[key] = val   | O(1)     | Hash entry creation.
Membership     | "key" in dict     | O(1)     | Fast existence check.
Deletion       | .pop(key)         | O(1)     | Remove specific key.
Iteration      | .items()          | O(n)     | Visit every pair once.
-----------------------------------------------------------------------
"""


def dictionary_revision():
    # 1. Initialization
    # Duplicate keys are not allowed; the last assignment wins.
    user_profile = {
        "first_name": "abc",
        "age": 19,
        "age": 20  # Overwrites 19
    }

    # Using the dict() constructor
    user_alt = dict(first_name="John", age=29)

    # 2. Adding & Updating (O(1))
    user_profile["zip_code"] = "94538"  # New entry
    user_profile.update({"zip_code": "94540"})  # Update via update()

    user_profile["age"] = 21  # Update via assignment
    user_profile.update({"age": 22})

    print(f"Dictionary Content: {user_profile}")
    print(f"Type: {type(user_profile)} | Size: {len(user_profile)}")

    # 3. Accessing Data
    print(f"Keys View: {user_profile.keys()}")
    print(f"Values View: {user_profile.values()}")
    print(f"Direct Access (Age): {user_profile['age']}")
    print(f"Safe Get (Age): {user_profile.get('age')}")
    print(f"Safe Get (Missing Address): {user_profile.get('address')}")  # Returns None
    print(f"Key Existence Check: {'zip_code' in user_profile}")

    # 4. Special Method: .setdefault()
    # Returns the value if key exists; if not, inserts key with the provided value.
    zip_val = user_profile.setdefault("zip_code", "11111")
    print(f"Setdefault (existing zip): {zip_val}")

    country_val = user_profile.setdefault("country", "USA")
    print(f"Setdefault (new country): {country_val}")

    # 5. Copying & Removal
    backup_profile = user_profile.copy()

    backup_profile.pop("age")  # Removes a specific key: O(1)
    backup_profile.popitem()  # Removes the last inserted (key, value) pair: O(1)
    print(f"Backup after removals: {backup_profile}")

    # 6. Iteration
    print("\n--- Iterating over Items ---")
    for key, value in user_profile.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    dictionary_revision()