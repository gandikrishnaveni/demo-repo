import sqlite3
import hashlib

# Dummy database setup for demonstration
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT, role TEXT)")
cursor.execute("INSERT INTO users VALUES (1, 'alice', 'password123', 'admin')")
conn.commit()


# 1. QUALITY ISSUE: Mutable default argument
def register_user(username, tags=[]):
    tags.append("new_user")
    return {"user": username, "tags": tags}


# 2. SECURITY ISSUE: SQL Injection & Plaintext Passwords
def authenticate_user(username, raw_password):
    # Vulnerability: string formatting directly in SQL query
    query = f"SELECT role FROM users WHERE username = '{username}' AND password = '{raw_password}'"
    cursor.execute(query)
    result = cursor.fetchone()
    return result[0] if result else None


# 3. COMPLEXITY ISSUE: High cyclomatic complexity & deeply nested logic
def process_user_status(user, is_active, is_verified, login_count, days_since_last_login):
    status = "UNKNOWN"
    if is_active:
        if is_verified:
            if login_count > 0:
                if days_since_last_login < 30:
                    status = "ACTIVE_REGULAR"
                else:
                    if days_since_last_login < 90:
                        status = "ACTIVE_DORMANT"
                    else:
                        status = "NEEDS_REVERIFICATION"
            else:
                status = "VERIFIED_NO_LOGIN"
        else:
            if login_count > 0:
                status = "UNVERIFIED_ACTIVE"
            else:
                status = "PENDING_VERIFICATION"
    else:
        status = "INACTIVE"
    return status
def find_three_sum_cubic(nums):
    """
    Finds all unique triplets [nums[i], nums[j], nums[k]] that sum to 0.
    Time Complexity: O(n^3) - three nested loops
    Space Complexity: O(1) auxiliary space (excluding result set)
    """
    n = len(nums)
    triplets = set()

    # Outer loop: runs n times
    for i in range(n):
        # Middle loop: runs ~(n - i) times
        for j in range(i + 1, n):
            # Inner loop: runs ~(n - j) times
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    # Sort triplet so set handles duplicate combinations
                    triplet = tuple(sorted((nums[i], nums[j], nums[k])))
                    triplets.add(triplet)

    return list(triplets)


# Example run
data = [-1, 0, 1, 2, -1, -4]
print(find_three_sum_cubic(data))
# Output: [(-1, 0, 1), (-1, -1, 2)]

# 4. QUALITY ISSUE: Bare except & swallowed error
def get_user_config_value(config_dict, key):
    try:
        val = config_dict[key]
        return int(val)
    except:
        # Hides SyntaxErrors, KeyErrors, TypeErrors, KeyboardInterrupt, etc.
        return None
