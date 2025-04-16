# Custom Hash Table Class
class HashTable:
    def __init__(self, size=40):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    # Insert package into hash table
    def insert(self, package):
        index = hash(package.package_id) % self.size
        bucket = self.table[index]

        # If the bucket is empty, insert the package
        for i, existing_package in enumerate(bucket):
            if existing_package.package_id == package.package_id:
                bucket[i] = package
                return
            
        bucket.append(package)

    # Lookup a packge by ID
    def lookup(self, package_id):
        index = hash(package_id) % self.size
        bucket = self.table[index]

        for package in bucket:
            if package.package_id == package_id:
                return package
        return None    
        