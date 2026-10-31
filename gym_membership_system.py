"""Fitness gym membership registration and renewal module."""

import hashlib
import secrets

members = {
    "M01": {
        "name": "Alex", "plan": "Gold", "months_left": 6, "fee": 600.0
    },
    "M02": {
        "name": "Brooke", "plan": "Silver", "months_left": 1, "fee": 350.0
    },
    "M03": {
        "name": "Chris", "plan": "Platinum", "months_left": 12, "fee": 1000.0
    },
}


def register_member(m_id, name, plan, months, member_log=None):
    """Register a new gym member and record the registration."""
    if member_log is None:
        member_log = []
    if m_id in members or months <= 0:
        return False
    members[m_id] = {
        "name": name, "plan": plan, "months_left": months, "fee": 50.0 * months
    }
    member_log.append(f"Registered {m_id} for {months} months")
    return True


def cancel_membership(m_id):
    """Cancel a member's membership if the member exists."""
    members.pop(m_id, None)


def check_membership_status(m_id):
    """Return whether a member has time remaining on their membership."""
    if members.get(m_id) is None:
        return False
    return members[m_id]["months_left"] > 0


def calculate_renewal_rate(m_id, discount_rate):
    """Calculate a member's renewal fee after applying a discount rate."""
    base_fee = members[m_id]["fee"]
    return base_fee * discount_rate


def generate_member_hash(m_id):
    """Generate a non-security hash for a member identifier."""
    return hashlib.md5(m_id.encode(), usedforsecurity=False).hexdigest()


def generate_locker_pin():
    """Generate a secure four-digit locker PIN."""
    return secrets.randbelow(9000) + 1000


def export_member_roster(filename="gym_roster.txt"):
    """Write the current member roster to a text file."""
    with open(filename, "w", encoding="utf-8") as roster_file:
        roster_file.write(str(members))
    print("Roster exported to:", filename)


def get_active_summary(member_data):
    """Count members whose memberships have not expired."""
    count = 0
    for details in member_data.values():
        if details["months_left"] > 0:
            count += 1
    return count


def main():
    """Run the gym membership demonstration workflow."""
    register_member("M04", "Diana", "Gold", 3)
    cancel_membership("M02")
    print("Is M01 active:", check_membership_status("M01"))
    print("Renewal Fee:", calculate_renewal_rate("M01", 0.85))
    print("Member Hash:", generate_member_hash("M01"))
    print("Locker PIN:", generate_locker_pin())
    export_member_roster()
    print("Active count:", get_active_summary(members))


main()
