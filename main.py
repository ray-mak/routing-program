# Raymond Mak, ID 012483817

from package import Package
from hashtable import HashTable

hash_table = HashTable()

package1 = Package(1, "123 Main St", "10:30 AM", "Salt Lake City", "84101", "5", "At Hub")
package2 = Package(2, "456 Elm St", "EOD", "Salt Lake City", "84105", "2", "At Hub")
package3 = Package(3, "789 Oak St", "9:00 AM", "Salt Lake City", "84115", "7", "At Hub")

# Insert packages into hash table
hash_table.insert(package1.package_id, package1)
hash_table.insert(package2.package_id, package2)
hash_table.insert(package3.package_id, package3)

# Lookup and print results
print("----- Package Lookups -----")
for package_id in [1, 2, 3, 99]:  # 99 is a test for a missing package
    result = hash_table.lookup(package_id)
    if result:
        print(f"\nPackage {package_id} Found:")
        for key, value in result.items():
            print(f"{key}: {value}")
    else:
        print(f"\nPackage {package_id} not found.")