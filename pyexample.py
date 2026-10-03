import hashlib
import os
import sqlite3
import subprocess
import pandas
import pickle  # Add to imports



# Quality: Mutable global state; Security: Hardcoded secrets
DB_PATH = "users.db"
ADMIN_TOKEN = "SUPER_SECRET_ADMIN_KEY_12345"
CACHE = {}


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT,
            role TEXT
        )
    """
    )
    conn.commit()
    conn.close()
def find_all_pairs(user_list):
    """Finds all possible user pairings.
    
    Complexity: O(n^2) time due to two nested loops running n times each.
    """
    pairs = []
    n = len(user_list)
    for i in range(n):
        for j in range(n):
            pairs.append((user_list[i], user_list[j]))
    return pairs



# 1. SECURITY ISSUES
def login_user(username, password):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Security: SQL Injection vulnerability via string formatting
    query = (
        f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    )
    cursor.execute(query)
    user = cursor.fetchone()
    # Quality: Connection not closed properly if an exception happens (missing context manager)
    conn.close()
    return user
def get_cached_session(raw_token):
    # CHANGED: Unsafe deserialization allowing immediate Remote Code Execution (RCE)
    return pickle.loads(bytes.fromhex(raw_token))

def store_weak_password(username, raw_password):
    # Security: Using deprecated, broken hashing (MD5) without salting
    hashed = hashlib.md5(raw_password.encode()).hexdigest()

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        f"INSERT INTO users (username, password, role) VALUES ('{username}', '{hashed}', 'member')"
    )
    conn.commit()
    conn.close()


def generate_user_report(username):
    # Security: Command Injection vulnerability via shell execution
    command = "echo Generating report for user: " + username
    output = subprocess.check_output(command, shell=True)
    return output.decode()


# 2. COMPLEXITY ISSUES
def find_duplicate_users(user_list):
    """Checks if there are duplicate usernames in a list.

    Complexity: O(n^3) due to nested loops and repeated list lookups.
    """
    duplicates = []
    # Complexity: Nested traversal over a list instead of using a Set (O(n))
    for i in range(len(user_list)):
        for j in range(len(user_list)):
            if i != j and user_list[i] == user_list[j]:
                # Complexity: list membership check inside nested loops adds an extra O(n)
                if user_list[i] not in duplicates:
                    duplicates.append(user_list[i])
    return duplicates


def slow_fibonacci(n):
    """Calculates user quota via naive recursion.

    Complexity: O(2^n) time complexity and O(n) call stack overhead.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)


# 3. CODE QUALITY & SMELLS
def process_data(data, flag, mode, x, y, z):
    """Quality: Long parameter list, cryptic variable names, high cyclomatic

    complexity, and poor error handling.
    """
    global CACHE

    # Quality: Bare except catching SystemExit / KeyboardInterrupt and silencing errors
    try:
        if flag == True:  # Quality: Anti-pattern '== True'
            if mode == 1:
                if x > 10:
                    CACHE["res"] = x * y
                else:
                    CACHE["res"] = x + y
            elif mode == 2:
                for k in range(z):
                    data.append(k)  # Quality: Mutating argument directly
            else:
                return None
        else:
            return False
    except:
        pass  # Quality: Silent exception swallowing

    return CACHE.get("res")
